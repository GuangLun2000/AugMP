# observe/overhead.py
# Wall-clock / GPU-memory accounting of the per-round cost (reviewer request: runtime and memory
# overhead of AugMP, how much of it is the graph part, how it evolves over rounds).
#
# Opt-in through config['profile_overhead'] (default False). When it is off every hook below is a
# no-op, so the original program path is unchanged; when it is on the hooks only read clocks and
# CUDA memory counters (torch.cuda.synchronize / memory_allocated / max_memory_allocated) and never
# touch any tensor, RNG or model state, so the numerical results are identical either way.
#
# Pieces:
#   StageClock                 begin(name) / end(name) pairs around code regions (no re-indentation
#                              needed inside the long camouflage_update); accumulates seconds and the
#                              peak GPU memory of each named stage.
#   ATTACK_STAGES              the attacker-side components recorded in client.camouflage_update.
#   build_round_overhead(...)  server-side: one dict per round -> round_log['overhead'] (saved in the
#                              results JSON like every other per-round key).
#   format_round_overhead(...) the per-round lines printed in the process log.
#   print_overhead_summary(..) end-of-run table (per round + mean/std) and two CSV files.

import csv
import statistics
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import torch

MB = float(2 ** 20)

# Attacker-side components, in execution order (client.AttackerClient.camouflage_update).
#   select     move observed updates to GPU, importance scores, top-k, index_select      (O(I*Mp))
#   graph      column-cosine adjacency over the M selected coordinates                   (O(M^2 I))
#   vgae       VGAE training, E epochs (first round also builds the VGAE)                (O(E M^2 H))
#   spectral   Laplacians, two M x M SVDs, GFT round trip, candidate row selection       (O(M^3))
#   expand     scatter the M-dim GSP vector back into the Mp-dim update (CPU)            (O(Mp))
#   setup      functional-call cache, reference aggregate, benign distance/similarity statistics
#   optimize   the K-step constrained manipulation loop (one backbone forward+backward per step)
#   finalize   model back to CPU, GPU clean-up, final constraint check
#   diag       logging-only forwards (initial-state and final-state prints), not part of the method
ATTACK_STAGES = ('select', 'graph', 'vgae', 'spectral', 'expand', 'setup', 'optimize', 'finalize', 'diag')
GRL_STAGES = ('select', 'graph', 'vgae', 'spectral', 'expand')

# Server-side components (server.Server.run_round).
SERVER_STAGES = ('broadcast', 'prepare', 'aggregate', 'observe', 'eval_global', 'eval_local')


class StageClock:
    """Accumulates wall-clock seconds and peak GPU memory per named stage. Disabled -> every call is a no-op."""

    def __init__(self, enabled: bool, device=None):
        self.enabled = bool(enabled)
        dev_type = getattr(device, 'type', None) if device is not None else None
        self.cuda = self.enabled and torch.cuda.is_available() and (dev_type in (None, 'cuda'))
        self.seconds: Dict[str, float] = {}
        self.peak_mb: Dict[str, float] = {}
        self.base_mb: Dict[str, float] = {}
        self._open: Dict[str, tuple] = {}
        self._t_total: Optional[float] = None
        self.total: Optional[float] = None

    def _sync(self):
        if self.cuda:
            torch.cuda.synchronize()

    def begin(self, name: str, memory: bool = True):
        """Start (or resume) stage `name`. memory=False only times it (use when stages nest)."""
        if not self.enabled:
            return
        self._sync()
        track = bool(memory and self.cuda)
        if track:
            if name not in self.base_mb:
                self.base_mb[name] = torch.cuda.memory_allocated() / MB
            torch.cuda.reset_peak_memory_stats()
        self._open[name] = (time.perf_counter(), track)

    def end(self, name: str):
        if not self.enabled or name not in self._open:
            return
        self._sync()
        t0, track = self._open.pop(name)
        self.seconds[name] = self.seconds.get(name, 0.0) + (time.perf_counter() - t0)
        if track:
            self.peak_mb[name] = max(self.peak_mb.get(name, 0.0), torch.cuda.max_memory_allocated() / MB)

    def start_total(self):
        if self.enabled:
            self._sync()
            self._t_total = time.perf_counter()

    def stop_total(self):
        if self.enabled and self._t_total is not None:
            self._sync()
            self.total = time.perf_counter() - self._t_total

    def report(self, **extra) -> dict:
        out = {'stages': dict(self.seconds), 'peak_mb': dict(self.peak_mb), 'base_mb': dict(self.base_mb),
               'total': self.total if self.total is not None else sum(self.seconds.values())}
        out.update(extra)
        return out


# ----------------------------------------------------------------------------------------------- server side
def build_round_overhead(clock: StageClock, train_ids: Iterable[int], attacker_ids: Iterable[int],
                         attacker_reports: Dict[int, Optional[dict]]) -> dict:
    """Assemble round_log['overhead'] from the server clock and the attackers' own reports."""
    train_ids, attacker_ids = list(train_ids), list(attacker_ids)
    ov = {
        'round_total': clock.total,
        'server': {s: clock.seconds.get(s, 0.0) for s in SERVER_STAGES},
        'server_peak_mb': {s: clock.peak_mb[s] for s in SERVER_STAGES if s in clock.peak_mb},
        'train': {cid: clock.seconds.get(f'train:{cid}', 0.0) for cid in train_ids},
        'train_peak_mb': {cid: clock.peak_mb[f'train:{cid}'] for cid in train_ids if f'train:{cid}' in clock.peak_mb},
        'attack_wall': {cid: clock.seconds.get(f'attack:{cid}', 0.0) for cid in attacker_ids},
        'attack': {cid: attacker_reports.get(cid) for cid in attacker_ids},
        'gpu': torch.cuda.get_device_name(0) if clock.cuda else None,
    }
    accounted = (sum(ov['server'].values()) + sum(ov['train'].values()) + sum(ov['attack_wall'].values()))
    ov['unaccounted'] = (ov['round_total'] - accounted) if ov['round_total'] is not None else None
    return ov


def _stage_seconds(rep: Optional[dict]) -> Dict[str, float]:
    st = (rep or {}).get('stages', {}) or {}
    return {s: float(st.get(s, 0.0)) for s in ATTACK_STAGES}


def _peak_gb(rep: Optional[dict]) -> Optional[float]:
    pk = (rep or {}).get('peak_mb', {}) or {}
    return (max(pk.values()) / 1024.0) if pk else None


def grl_memory_mb(rep: Optional[dict]) -> Optional[dict]:
    """GPU memory of the GRL framework in one camouflage_update (MB, torch.cuda.memory_allocated basis).

    resident = memory already allocated when the GRL part starts (global model, buffers, ...), i.e. the
               base of the first GRL stage ('select');
    peak     = highest allocation reached during any GRL stage (select/graph/vgae/spectral/expand);
    extra    = peak - resident = the memory the GRL framework itself needs on top of what is resident.
    None when no CUDA memory was recorded (CPU run or profiling off).
    """
    pk = (rep or {}).get('peak_mb', {}) or {}
    base = (rep or {}).get('base_mb', {}) or {}
    peaks = [pk[s] for s in GRL_STAGES if s in pk]
    if not peaks or 'select' not in base:
        return None
    peak, resident = max(peaks), float(base['select'])
    return {'peak': peak, 'resident': resident, 'extra': max(0.0, peak - resident)}


def format_round_overhead(ov: dict, round_num: int, attacker_ids: Iterable[int]) -> List[str]:
    """Lines for the process log, printed once per round."""
    attacker_ids = list(attacker_ids)
    srv = ov['server']
    train = ov['train']
    benign_train = {cid: s for cid, s in train.items() if cid not in attacker_ids}
    train_str = ' '.join(f'{cid}:{s:.1f}' for cid, s in benign_train.items())
    att_str = ' '.join(f'{cid}:{s:.1f}' for cid, s in ov['attack_wall'].items())
    rt = ov['round_total'] if ov['round_total'] is not None else float('nan')
    lines = [
        f"⏱️  Overhead round {round_num} (wall-clock s): round {rt:.2f} | broadcast {srv['broadcast']:.2f} | "
        f"prepare {srv['prepare']:.2f} | benign train {sum(benign_train.values()):.2f} [{train_str}] | "
        f"attack {sum(ov['attack_wall'].values()):.2f} [{att_str}] | aggregate {srv['aggregate']:.2f} | "
        f"observe {srv['observe']:.2f} | eval_global {srv['eval_global']:.2f} | "
        f"eval_local {srv['eval_local']:.2f} (bookkeeping) | unaccounted {ov.get('unaccounted') or 0.0:.2f}"
    ]
    for cid in attacker_ids:
        rep = ov['attack'].get(cid)
        if not rep:
            lines.append(f"    [Attacker {cid}] no stage report (not an AugMP attacker or no benign updates); "
                         f"wall {ov['attack_wall'].get(cid, 0.0):.2f}s")
            continue
        st = _stage_seconds(rep)
        grl = sum(st[s] for s in GRL_STAGES)
        steps = int(rep.get('steps', 0) or 0)
        per_step = (st['optimize'] / steps) if steps > 0 else float('nan')
        pk = rep.get('peak_mb', {}) or {}
        pk_str = ''
        if pk:
            top = max(pk, key=pk.get)
            pk_str = f" | peak GPU {pk[top] / 1024.0:.2f} GB ({top})"
        gm = grl_memory_mb(rep)
        if gm:   # GRL framework's own GPU memory: peak during the GRL stages minus what was resident before them
            pk_str += f" | GRL GPU mem +{gm['extra']:.1f} MB (resident {gm['resident'] / 1024.0:.2f} GB)"
        lines.append(
            f"    [Attacker {cid}] select {st['select']:.3f} | graph {st['graph']:.3f} | vgae {st['vgae']:.3f} | "
            f"spectral {st['spectral']:.3f} | expand {st['expand']:.3f} | GRL subtotal {grl:.3f} | "
            f"setup {st['setup']:.2f} | optimize {st['optimize']:.2f} ({steps} steps, {per_step:.3f} s/step) | "
            f"finalize {st['finalize']:.2f} | diag {st['diag']:.2f} | total {rep.get('total', 0.0):.2f}{pk_str}"
        )
    tp = ov.get('train_peak_mb') or {}
    benign_peaks = {cid: mb for cid, mb in tp.items() if int(cid) not in attacker_ids}
    if benign_peaks:
        lines.append("    [Benign fine-tuning peak GPU] " + ' '.join(f'{cid}:{mb / 1024.0:.2f}' for cid, mb in sorted(benign_peaks.items(), key=lambda kv: int(kv[0])))
                     + f" GB (mean {sum(benign_peaks.values()) / len(benign_peaks) / 1024.0:.2f} GB, max {max(benign_peaks.values()) / 1024.0:.2f} GB)")
    return lines


# ----------------------------------------------------------------------------------------------- end of run
def _mean_std(vals: List[float]):
    vals = [v for v in vals if v is not None]
    if not vals:
        return float('nan'), float('nan')
    return statistics.fmean(vals), (statistics.pstdev(vals) if len(vals) > 1 else 0.0)


def summarize_overhead(log_data: List[dict], attacker_ids: Iterable[int]):
    """Per-round rows (attacker stages summed over attackers) and per-(round, attacker) rows."""
    attacker_ids = list(attacker_ids)
    round_rows, attacker_rows = [], []
    for log in log_data:
        ov = log.get('overhead')
        if not ov:
            continue
        r = log.get('round')
        srv = ov['server']
        benign_train = [s for cid, s in ov['train'].items() if int(cid) not in attacker_ids]
        row = {'round': r, 'round_total': ov['round_total'], 'broadcast': srv['broadcast'], 'prepare': srv['prepare'],
               'train_benign_sum': sum(benign_train), 'train_benign_mean': (sum(benign_train) / len(benign_train)) if benign_train else 0.0,
               'attack_wall_sum': sum(ov['attack_wall'].values()), 'aggregate': srv['aggregate'], 'observe': srv['observe'],
               'eval_global': srv['eval_global'], 'eval_local': srv['eval_local'], 'unaccounted': ov.get('unaccounted')}
        bp = [mb for cid, mb in (ov.get('train_peak_mb') or {}).items() if int(cid) not in attacker_ids]
        row['train_benign_peak_gb_mean'] = (sum(bp) / len(bp) / 1024.0) if bp else None
        row['train_benign_peak_gb_max'] = (max(bp) / 1024.0) if bp else None
        for s in ATTACK_STAGES:
            row[f'att_{s}'] = 0.0
        row['att_grl'] = 0.0
        row['att_total'] = 0.0
        row['att_steps'] = 0
        row['att_peak_gb'] = None
        for cid, rep in ov['attack'].items():
            cid = int(cid)
            st = _stage_seconds(rep)
            arow = {'round': r, 'attacker': cid, 'wall': ov['attack_wall'].get(cid, ov['attack_wall'].get(str(cid), 0.0)),
                    'has_report': rep is not None}
            arow.update(st)
            arow['grl'] = sum(st[s] for s in GRL_STAGES)
            # AugMP attackers report their own total; baseline attackers (ALIE/Gaussian/SignFlipping) have no
            # stage report, so their server-side wall time around camouflage_update is the total.
            arow['total'] = float((rep or {}).get('total') or arow['wall'] or 0.0)
            arow['steps'] = int((rep or {}).get('steps', 0) or 0)
            arow['s_per_step'] = (st['optimize'] / arow['steps']) if arow['steps'] > 0 else None
            arow['peak_gb'] = _peak_gb(rep)
            for s, mb in ((rep or {}).get('peak_mb', {}) or {}).items():
                arow[f'peak_gb_{s}'] = mb / 1024.0
            gm = grl_memory_mb(rep)
            arow['grl_mem_extra_mb'] = gm['extra'] if gm else None
            arow['grl_mem_peak_mb'] = gm['peak'] if gm else None
            arow['grl_mem_resident_mb'] = gm['resident'] if gm else None
            attacker_rows.append(arow)
            for s in ATTACK_STAGES:
                row[f'att_{s}'] += st[s]
            row['att_grl'] += arow['grl']
            row['att_total'] += arow['total']
            row['att_steps'] += arow['steps']
            if arow['peak_gb'] is not None:
                row['att_peak_gb'] = max(row['att_peak_gb'] or 0.0, arow['peak_gb'])
        round_rows.append(row)
    return round_rows, attacker_rows


def _fmt(v, w=8, p=2):
    if v is None:
        return ' ' * (w - 1) + '-'
    if isinstance(v, float) and v != v:
        return ' ' * (w - 3) + 'nan'
    if isinstance(v, int):
        return f'{v:>{w}d}'
    return f'{v:>{w}.{p}f}'


def print_overhead_summary(log_data: List[dict], attacker_ids: Iterable[int], totals: Optional[dict] = None,
                           results_dir: Optional[Path] = None, experiment_name: str = 'experiment') -> None:
    """End-of-run summary: per-round table, mean/std over rounds >= 2, per-stage attacker table, CSVs."""
    attacker_ids = list(attacker_ids)
    round_rows, attacker_rows = summarize_overhead(log_data, attacker_ids)
    if not round_rows:
        print("⏱️  No overhead records found (profile_overhead was off or no round completed).")
        return
    has_attack = bool(attacker_rows)
    gpu = next((log['overhead'].get('gpu') for log in log_data if log.get('overhead')), None)

    print("\n" + "=" * 118)
    print("⏱️  PER-ROUND OVERHEAD SUMMARY (wall-clock seconds)" + (f"  --  GPU: {gpu}" if gpu else "  --  CPU"))
    print("=" * 118)
    print("Attacker columns are summed over all attackers of the round; GRL = select+graph+vgae+spectral+expand;")
    print("optimize = the K-step manipulation loop; diag = logging-only forwards; eval_local = per-client test-set")
    print("evaluation kept for the local-accuracy figure (experiment bookkeeping, not part of the FL protocol).")
    cols = [('round', 10, 0), ('att_grl', 8, 3), ('att_setup', 8, 2), ('att_optimize', 9, 2), ('att_steps', 6, 0),
            ('att_finalize', 9, 2), ('att_diag', 7, 2), ('att_total', 9, 2), ('att_peak_gb', 8, 2),
            ('train_benign_sum', 10, 2), ('aggregate', 9, 2), ('eval_global', 10, 2), ('eval_local', 10, 2),
            ('round_total', 10, 2)]
    if not has_attack:
        cols = [c for c in cols if not c[0].startswith('att_')]
    header = {'round': 'round', 'att_grl': 'GRL', 'att_setup': 'setup', 'att_optimize': 'optimize', 'att_steps': 'steps',
              'att_finalize': 'finalize', 'att_diag': 'diag', 'att_total': 'attack', 'att_peak_gb': 'att_GB',
              'train_benign_sum': 'train_ben', 'aggregate': 'aggregate', 'eval_global': 'eval_glob',
              'eval_local': 'eval_loc', 'round_total': 'round'}
    width = sum(w for _, w, _ in cols) + len(cols) - 1
    print('-' * width)
    print(' '.join(f'{header[c]:>{w}}' for c, w, _ in cols))
    print('-' * width)
    for row in round_rows:
        print(' '.join(_fmt(row[c], w, p) for c, w, p in cols))
    print('-' * width)
    steady = [r for r in round_rows if (r['round'] or 0) >= 2] or round_rows
    for label, agg in (('mean r>=2', 'mean'), ('std r>=2', 'std'), ('mean all', 'mean_all'), ('sum all', 'sum')):
        source = steady if agg in ('mean', 'std') else round_rows
        cells = []
        for c, w, p in cols:
            if c == 'round':
                cells.append(f'{label:>{w}}')
                continue
            vals = [r[c] for r in source if r[c] is not None]
            if not vals:
                cells.append(_fmt(None, w, p))
                continue
            if agg == 'sum':
                v = float(max(vals) if c == 'att_peak_gb' else sum(vals))  # peaks do not add up: show the max
            else:
                m, s = _mean_std([float(x) for x in vals])
                v = s if agg == 'std' else m
            cells.append(_fmt(v, w, 1 if c == 'att_steps' else max(p, 2)))
        print(' '.join(cells))
    print('-' * width)

    reported = [r for r in attacker_rows if r.get('has_report')]  # AugMP attackers only (baselines have no stages)
    if reported:
        print("\nPer attacker-round means over rounds >= 2 (each attacker counted separately):")
        print(f"{'stage':<10}{'mean s':>10}{'std s':>10}{'share %':>10}{'peak GB':>10}")
        srows = [r for r in reported if (r['round'] or 0) >= 2] or reported
        tot_mean, _ = _mean_std([r['total'] for r in srows])
        for s in ATTACK_STAGES + ('grl', 'total'):
            m, sd = _mean_std([r[s] for r in srows])
            share = (100.0 * m / tot_mean) if tot_mean else float('nan')
            pk = [r.get(f'peak_gb_{s}') for r in srows if r.get(f'peak_gb_{s}') is not None]
            pk_s = f'{max(pk):>10.2f}' if pk else f'{"-":>10}'
            print(f"{s:<10}{m:>10.3f}{sd:>10.3f}{share:>10.1f}{pk_s}")
        steps = [r['steps'] for r in srows]
        sps = [r['s_per_step'] for r in srows if r['s_per_step'] is not None]
        if steps:
            print(f"steps: mean {statistics.fmean(steps):.1f}, median {statistics.median(steps):.1f}, max {max(steps)}"
                  + (f"; {statistics.fmean(sps):.3f} s/step" if sps else ''))
        gx = [r['grl_mem_extra_mb'] for r in srows if r.get('grl_mem_extra_mb') is not None]
        if gx:
            gp = [r['grl_mem_peak_mb'] for r in srows if r.get('grl_mem_peak_mb') is not None]
            gr = [r['grl_mem_resident_mb'] for r in srows if r.get('grl_mem_resident_mb') is not None]
            print(f"GRL GPU memory (peak during GRL stages minus memory resident before them, rounds >= 2): "
                  f"mean +{statistics.fmean(gx):.1f} MB, max +{max(gx):.1f} MB "
                  f"(GRL-stage peak {max(gp) / 1024.0:.2f} GB, resident {statistics.fmean(gr) / 1024.0:.2f} GB)")
        bpk = [r['train_benign_peak_gb_max'] for r in steady if r.get('train_benign_peak_gb_max') is not None]
        if bpk:
            bpm = [r['train_benign_peak_gb_mean'] for r in steady if r.get('train_benign_peak_gb_mean') is not None]
            print(f"Benign local fine-tuning peak GPU memory (rounds >= 2): mean over clients {statistics.fmean(bpm):.2f} GB, "
                  f"max {max(bpk):.2f} GB")
        bt = [r['train_benign_mean'] for r in steady if r['train_benign_mean']]
        if bt and tot_mean:
            print(f"attacker total / mean benign local training (r>=2): {tot_mean / statistics.fmean(bt):.2f}x")

    if totals:
        print("\nWall-clock totals (s): " + ', '.join(f"{k} {v:.1f}" for k, v in totals.items() if isinstance(v, (int, float))))

    if results_dir is not None:
        results_dir = Path(results_dir)
        results_dir.mkdir(parents=True, exist_ok=True)
        rp = results_dir / f"{experiment_name}_overhead_rounds.csv"
        with open(rp, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(round_rows[0].keys()))
            w.writeheader()
            w.writerows(round_rows)
        print(f"Overhead per round saved to: {rp}")
        if attacker_rows:
            keys = []
            for r in attacker_rows:
                for k in r:
                    if k not in keys:
                        keys.append(k)
            ap = results_dir / f"{experiment_name}_overhead_attackers.csv"
            with open(ap, 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=keys)
                w.writeheader()
                w.writerows(attacker_rows)
            print(f"Overhead per attacker-round saved to: {ap}")
