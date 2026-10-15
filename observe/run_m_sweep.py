# run_m_sweep.py
# Run main.py's configured experiment for several values of dim_reduction_size (M), back-to-back, each in a
# FRESH Python process, and tabulate the measured per-stage runtime / GPU memory of the attacker versus M.
#
# Everything (model, dataset, seed, rounds, profile_overhead, ...) comes from main.py's own `config` block;
# this driver only overrides, per run:
#     dim_reduction_size = M
#     experiment_name    = <main.py experiment_name>_M<M>        (so the result files do not collide)
#     num_rounds         = --rounds                                (only if given)
#     profile_overhead   = True                                    (the point of the sweep; numerics unchanged)
# A fresh process per M means each run is exactly `python main.py` with those keys edited: fresh CUDA context,
# fresh RNG streams, no state carried over from the previous M.
#
# Usage (repo root):
#   python observe/run_m_sweep.py --M 1000 2000 5000 --rounds 3
#   python observe/run_m_sweep.py --M 1000 2000 5000 --summary-only      # re-tabulate finished runs
# Outputs (in results/): <name>_M<M>_log.txt per run (full stdout+stderr), the usual per-run result files,
# and m_sweep_summary.csv + a printed table (means over rounds >= 2, both attackers pooled).

import argparse
import csv
import json
import os
import statistics
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from visualization import resolve_experiment_name  # noqa: E402  (reads main.py's experiment_name without importing torch)

STAGES = ('select', 'graph', 'vgae', 'spectral', 'expand', 'grl', 'setup', 'optimize', 'finalize', 'diag', 'total')
RUNNER = "import json, sys; from main import main; main(json.loads(sys.argv[1]))"


def run_name(base: str, M: int) -> str:
    return f"{base}_M{M}"


def launch(overrides: dict, log_path: Path) -> int:
    """Run main.main(overrides) in a fresh interpreter; stream its output to the console and to log_path."""
    env = dict(os.environ, TQDM_DISABLE='1', PYTHONUNBUFFERED='1')
    cmd = [sys.executable, '-c', RUNNER, json.dumps(overrides)]
    with open(log_path, 'w', encoding='utf-8') as logf:
        proc = subprocess.Popen(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, bufsize=1)
        for line in proc.stdout:
            sys.stdout.write(line)
            logf.write(line)
        return proc.wait()


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _mean(vals):
    vals = [v for v in vals if v is not None]
    return statistics.fmean(vals) if vals else None


def summarize_run(results_dir: Path, name: str, M: int):
    """Means over rounds >= 2 (both attackers pooled) from the per-run overhead CSVs written by observe/overhead.py."""
    ap = results_dir / f"{name}_overhead_attackers.csv"
    rp = results_dir / f"{name}_overhead_rounds.csv"
    if not ap.exists():
        return None
    arows = [r for r in csv.DictReader(open(ap)) if r.get('has_report') == 'True']
    steady = [r for r in arows if _f(r['round']) is not None and _f(r['round']) >= 2] or arows
    out = {'M': M, 'name': name, 'rounds': len({r['round'] for r in arows}), 'attacker_rounds_r2': len(steady)}
    for s in STAGES:
        out[f'{s}_s'] = _mean([_f(r.get(s)) for r in steady])
    out['steps'] = _mean([_f(r.get('steps')) for r in steady])
    out['s_per_step'] = _mean([_f(r.get('s_per_step')) for r in steady])
    for s in ('select', 'graph', 'vgae', 'spectral', 'expand', 'optimize'):
        vals = [_f(r.get(f'peak_gb_{s}')) for r in steady]
        out[f'peak_gb_{s}'] = max(v for v in vals if v is not None) if any(v is not None for v in vals) else None
    out['peak_gb'] = max((_f(r.get('peak_gb')) or 0.0) for r in steady) if steady else None
    out['grl_mem_extra_mb'] = _mean([_f(r.get('grl_mem_extra_mb')) for r in steady])
    out['grl_mem_resident_mb'] = _mean([_f(r.get('grl_mem_resident_mb')) for r in steady])
    if rp.exists():
        rrows = list(csv.DictReader(open(rp)))
        rsteady = [r for r in rrows if (_f(r['round']) or 0) >= 2] or rrows
        out['train_benign_mean_s'] = _mean([_f(r.get('train_benign_mean')) for r in rsteady])
        out['round_total_s'] = _mean([_f(r.get('round_total')) for r in rsteady])
    return out


def print_table(rows):
    def cell(v, p=3):
        return '-' if v is None else (f'{v:.{p}f}' if isinstance(v, float) else str(v))
    print("\n" + "=" * 100)
    print("M SWEEP SUMMARY  (per attacker-round means over rounds >= 2; GRL = select+graph+vgae+spectral+expand)")
    print("=" * 100)
    lines = [
        ('M', lambda r: r['M'], 0), ('attacker-rounds (r>=2)', lambda r: r['attacker_rounds_r2'], 0),
        ('select  s', lambda r: r['select_s'], 3), ('graph   s', lambda r: r['graph_s'], 3),
        ('vgae    s', lambda r: r['vgae_s'], 3), ('spectral s', lambda r: r['spectral_s'], 3),
        ('expand  s', lambda r: r['expand_s'], 3), ('GRL     s', lambda r: r['grl_s'], 3),
        ('setup   s', lambda r: r['setup_s'], 2), ('optimize s', lambda r: r['optimize_s'], 2),
        ('steps K', lambda r: r['steps'], 1), ('s / step', lambda r: r['s_per_step'], 3),
        ('attack total s', lambda r: r['total_s'], 2), ('benign train s (mean/agent)', lambda r: r.get('train_benign_mean_s'), 2),
        ('GRL mem +MB', lambda r: r['grl_mem_extra_mb'], 1), ('resident before GRL GB', lambda r: (r['grl_mem_resident_mb'] or 0) / 1024.0 if r['grl_mem_resident_mb'] else None, 2),
        ('peak GB select', lambda r: r['peak_gb_select'], 2), ('peak GB graph', lambda r: r['peak_gb_graph'], 2),
        ('peak GB vgae', lambda r: r['peak_gb_vgae'], 2), ('peak GB spectral', lambda r: r['peak_gb_spectral'], 2),
        ('peak GB optimize', lambda r: r['peak_gb_optimize'], 2), ('peak GB attacker', lambda r: r['peak_gb'], 2),
    ]
    w = 14
    print(f"{'':<28}" + ''.join(f"{('M=' + str(r['M'])):>{w}}" for r in rows))
    for label, fn, p in lines[1:]:
        print(f"{label:<28}" + ''.join(f"{cell(fn(r), p):>{w}}" for r in rows))
    print("=" * 100)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--M', type=int, nargs='+', default=[1000, 2000, 5000], help='dim_reduction_size values, run in this order')
    ap.add_argument('--rounds', type=int, default=None, help='override num_rounds for every run (default: main.py value)')
    ap.add_argument('--name-base', default=None, help="result-file prefix (default: main.py's experiment_name)")
    ap.add_argument('--extra', default=None, help='JSON dict of additional config overrides applied to every run (smoke tests)')
    ap.add_argument('--summary-only', action='store_true', help='do not run; tabulate existing result CSVs')
    ap.add_argument('--dry-run', action='store_true', help='print the per-run overrides and exit')
    args = ap.parse_args()

    base = args.name_base or resolve_experiment_name()
    results_dir = ROOT / 'results'          # main.py always writes here (relative to the repo root)
    results_dir.mkdir(parents=True, exist_ok=True)
    extra = json.loads(args.extra) if args.extra else {}

    plan = []
    for M in args.M:
        ov = dict(extra)
        ov.update({'dim_reduction_size': M, 'experiment_name': run_name(base, M), 'profile_overhead': True})
        if args.rounds is not None:
            ov['num_rounds'] = args.rounds
        plan.append((M, ov))

    print(f"M sweep: base '{base}', M = {args.M}, results -> {results_dir}")
    for M, ov in plan:
        print(f"  M={M}: overrides {ov}")
    if args.dry_run:
        return

    status = {}
    if not args.summary_only:
        for M, ov in plan:
            log_path = results_dir / f"{ov['experiment_name']}_log.txt"
            print("\n" + "#" * 100 + f"\n# M = {M}   ->   {ov['experiment_name']}   (log: {log_path})\n" + "#" * 100, flush=True)
            t0 = time.perf_counter()
            rc = launch(ov, log_path)
            status[M] = rc
            print(f"\n# M = {M} finished with exit code {rc} in {(time.perf_counter() - t0) / 60:.1f} min", flush=True)

    rows = []
    for M, ov in plan:
        s = summarize_run(results_dir, ov['experiment_name'], M)
        if s is None:
            print(f"[M={M}] no overhead CSV found for {ov['experiment_name']} (run failed or profile_overhead off)")
        else:
            rows.append(s)
    if rows:
        print_table(rows)
        out = results_dir / 'm_sweep_summary.csv'
        keys = []
        for r in rows:
            keys += [k for k in r if k not in keys]
        with open(out, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(rows)
        print(f"summary saved to: {out}")
    if any(rc != 0 for rc in status.values()):
        sys.exit(1)


if __name__ == '__main__':
    main()
