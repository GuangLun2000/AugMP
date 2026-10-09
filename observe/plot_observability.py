#!/usr/bin/env python3
"""
plot_observability.py — summarise and plot the limited-observability ablation.

Reads the *_results.json files written by main.py (by default results/obs_*_results.json, as
produced by observe/run_observability_sweep.py) and writes to --out (default: results/observe/):
  observability_accuracy_curves.png  global accuracy vs round, one line per observation level
  observability_param_retention.png  accuracy drop vs share of parameters observed (parameter-level runs)
  observability_retention.png        accuracy drop vs observed fraction, ALIE at full observation as reference
  observability_dist_bound.png       attacker-side automatic d_T per round (mechanism: bound shrinkage vs GRL)
  observability_summary.csv          one row per run (accuracy, drop vs benign, retention, stealth in-band rates, d_T)

  --window N     rounds averaged at the end of a run (default 10)
  --at-round R   evaluate every run at round R (align 50-round anchors with 30-round sweeps)
  --suggest-bounds  print d_T / sim_bound_up medians of the full-observation AugMP run, to be
                    passed to run_observability_sweep.py --dist-bound/--sim-bound-up
"""
import argparse
import csv
import glob
import json
import re
import statistics
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent  # repo root (this file lives in observe/)

# ------------------------------------------------------------------ colours (fixed assignment, CVD-safe)
C_BENIGN = '#000000'
C_ALIE = '#E69F00'      # orange
C_OTHER = '#8C8C8C'     # other baselines
AUGMP_RAMP = ['#9ECAE1', '#6BAED6', '#4292C6', '#2171B5', '#08519C', '#08306B']  # light -> dark = fewer -> more observed
VARIANT_COLOURS = {  # attacker-side strategies (fixed assignment)
    'largest': '#009E73', 'anchor': '#CC79A7', 'largest+anchor': '#56B4E9', 'random': '#999999',
    'adaptive-deviant': '#D55E00', 'adaptive-deviant+anchor': '#B04A00',
    'adaptive-representative': '#F0E442', 'adaptive-representative+anchor': '#C8BC2E',
    'secagg': '#7B3294',
}
VARIANT_MARKERS = ['D', 'o', 's', '^', 'v', 'P', 'X', '*', 'h']


def variant_colour(variant: str, frac: float, fracs_sorted: List[float]) -> str:
    base = variant.replace('+fixed-bounds', '').replace('fixed-bounds', 'fixed')
    if base in ('fixed', ''):
        return augmp_colour(frac, fracs_sorted)
    return VARIANT_COLOURS.get(base, '#444444')


@dataclass
class Run:
    name: str
    path: str
    attack: str              # 'benign' | 'AugMP' | 'ALIE' | ...
    n_clients: int
    n_attackers: int
    k: Optional[int]         # observed benign clients (None for the benign baseline)
    mode: str
    obs_seed: Optional[int]
    fixed_bounds: bool
    criterion: str
    anchor: bool
    rounds: List[int]
    acc: List[float]
    logs: List[dict]
    attacker_ids: List[int] = field(default_factory=list)
    param_fraction: float = 1.0   # share of each observed update's coordinates the attackers see

    @property
    def n_benign(self) -> int:
        return self.n_clients - self.n_attackers

    @property
    def frac(self) -> Optional[float]:
        return None if self.k is None else self.k / self.n_benign

    @property
    def variant(self) -> str:
        """Attacker-side strategy tag (used for grouping and legends)."""
        if self.attack == 'benign':
            return 'benign'
        if self.k == 0:
            return 'secagg'
        parts = []
        if self.mode != 'fixed':
            parts.append(self.mode + (f'-{self.criterion}' if self.mode == 'adaptive' else ''))
        if self.anchor:
            parts.append('anchor')
        if self.fixed_bounds:
            parts.append('fixed-bounds')
        if self.param_fraction < 1.0:
            parts.append('params')
        return '+'.join(parts) if parts else 'fixed'

    @property
    def param_level(self) -> bool:
        return self.attack != 'benign' and self.param_fraction < 1.0

    def label(self) -> str:
        if self.attack == 'benign':
            return 'Benign setting'
        if self.k == 0:
            return f"{self.attack}, SecAgg (k=0, global-only)"
        base = f"{self.attack}, k={self.k}/{self.n_benign} ({self.frac:.0%})"
        if self.param_level:
            base += f", {self.param_fraction:.0%} of parameters"
        if self.variant not in ('fixed', 'params'):
            base += f', {self.variant.replace("+params", "")}'
        if self.obs_seed is not None:
            base += f', subset {self.obs_seed}'
        return base


def load_run(path: str) -> Run:
    with open(path) as f:
        d = json.load(f)
    cfg = d['config']
    n_att = int(cfg.get('num_attackers', 0) or 0)
    n_cli = int(cfg['num_clients'])
    n_ben = n_cli - n_att
    attack = 'benign' if n_att == 0 else str(cfg.get('attack_method', 'AugMP'))
    if attack == 'GRMP':
        attack = 'AugMP'
    k = None
    if attack != 'benign':
        raw = cfg.get('attacker_observed_benign', None)
        if raw is None:
            k = n_ben
        elif isinstance(raw, float):
            k = max(1, int(round(raw * n_ben)))
        else:
            k = int(raw)          # may be 0 = Secure Aggregation
        k = min(k, n_ben)
    pm = d.get('progressive_metrics', {})
    return Run(
        name=cfg.get('experiment_name', Path(path).stem), path=path, attack=attack,
        n_clients=n_cli, n_attackers=n_att, k=k,
        mode=str(cfg.get('attacker_observation_mode', 'fixed')),
        obs_seed=cfg.get('attacker_observation_seed', None),
        fixed_bounds=(attack != 'benign' and cfg.get('dist_bound', None) is not None),
        criterion=str(cfg.get('attacker_observation_criterion', 'deviant') or 'deviant'),
        anchor=bool(cfg.get('attacker_observation_anchor_global', False)),
        rounds=list(pm.get('rounds', [])), acc=list(pm.get('clean_acc', [])), logs=list(d.get('results', [])),
        attacker_ids=list(range(n_ben, n_cli)),
        param_fraction=float(cfg.get('attacker_observed_param_fraction', None) or 1.0) if attack != 'benign' else 1.0,
    )


def unobserved_energy_series(run: Run) -> List[Optional[float]]:
    """Per-round mean share of the attackers' submitted-update energy on the hidden coordinates."""
    out = []
    for log in run.logs:
        d = log.get('attacker_unobserved_energy_frac') or {}
        vals = [v for v in d.values() if v is not None]
        out.append(float(np.mean(vals)) if vals else None)
    return out


# ------------------------------------------------------------------ metrics
def acc_at(run: Run, at_round: Optional[int], window: int) -> float:
    """Mean accuracy over the `window` rounds ending at `at_round` (or at the last round)."""
    pairs = [(r, a) for r, a in zip(run.rounds, run.acc) if at_round is None or r <= at_round]
    if not pairs:
        return float('nan')
    if at_round is not None and pairs[-1][0] < at_round:
        print(f"  [warn] {run.name}: only {pairs[-1][0]} rounds available (< --at-round {at_round})")
    tail = [a for _, a in pairs[-window:]]
    return float(np.mean(tail))


def in_band_rates(run: Run, at_round: Optional[int]) -> Dict[str, float]:
    """Fraction of (round, attacker) pairs whose server-side similarity / distance lies inside the benign range."""
    sim_hits = sim_total = dist_hits = dist_total = 0
    att = set(run.attacker_ids)
    for log in run.logs:
        if at_round is not None and log.get('round', 0) > at_round:
            continue
        agg = log.get('aggregation', {})
        ids = agg.get('accepted_clients', [])
        for key in ('similarities', 'euclidean_distances'):
            vals = agg.get(key, [])
            if len(vals) != len(ids):
                continue
            ben = [v for cid, v in zip(ids, vals) if cid not in att]
            atk = [v for cid, v in zip(ids, vals) if cid in att]
            if not ben or not atk:
                continue
            lo, hi = min(ben), max(ben)
            hits = sum(1 for v in atk if lo <= v <= hi)
            if key == 'similarities':
                sim_hits += hits; sim_total += len(atk)
            else:
                dist_hits += hits; dist_total += len(atk)
    return {
        'sim_in_band': sim_hits / sim_total if sim_total else float('nan'),
        'dist_in_band': dist_hits / dist_total if dist_total else float('nan'),
    }


def dist_bound_series(run: Run) -> List[Optional[float]]:
    """Per-round mean of the attacker-side effective d_T (None when not logged)."""
    out = []
    for log in run.logs:
        db = log.get('attacker_dist_bounds')
        vals = [v for v in (db or {}).values() if v is not None]
        out.append(float(np.mean(vals)) if vals else None)
    return out


def benign_mean_pairwise_similarity(run: Run) -> List[float]:
    """Per-round benign mean pairwise cosine similarity (= attacker's automatic sim_bound_up)."""
    out = []
    att = set(run.attacker_ids)
    for log in run.logs:
        agg = log.get('aggregation', {})
        S = agg.get('similarity_matrix')
        ids = agg.get('accepted_clients', [])
        if not S or len(S) != len(ids):
            continue
        ben_idx = [i for i, cid in enumerate(ids) if cid not in att]
        if len(ben_idx) < 2:
            continue
        per_client = []
        for i in ben_idx:
            others = [S[i][j] for j in ben_idx if j != i]
            per_client.append(float(np.mean(others)))
        out.append(float(np.mean(per_client)))
    return out


def early_stop_stats(run: Run, results_dir: Path) -> Dict[str, float]:
    """From the run's stdout log (results/observe/logs/<name>.log): how many proxy-optimisation steps the
    attackers took before early stopping, and how often the final update still violated the bound."""
    out = {'early_stop_mean_step': float('nan'), 'early_stop_events': float('nan'), 'final_violations': float('nan')}
    log_path = results_dir / 'observe' / 'logs' / f'{run.name}.log'
    if not log_path.exists():
        return out
    steps, violations = [], 0
    pat = re.compile(r'Early stopping:.*?\(step (\d+)/(\d+)\)')
    with open(log_path, errors='ignore') as f:
        for line in f:
            m = pat.search(line)
            if m:
                steps.append(int(m.group(1)) + 1)
            elif 'violat' in line.lower() and 'final' in line.lower():
                violations += 1
    if steps:
        out['early_stop_mean_step'] = float(np.mean(steps))
        out['early_stop_events'] = float(len(steps))
    out['final_violations'] = float(violations)
    return out


# ------------------------------------------------------------------ plotting
def style():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        'font.family': 'serif', 'font.size': 11, 'axes.labelsize': 12, 'axes.titlesize': 12,
        'legend.fontsize': 9, 'xtick.labelsize': 10, 'ytick.labelsize': 10,
        'axes.grid': True, 'grid.alpha': 0.3, 'grid.linestyle': '--',
        'lines.linewidth': 1.8, 'lines.markersize': 5, 'figure.dpi': 120, 'savefig.dpi': 300,
        'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False,
    })
    return plt


def augmp_colour(frac: float, fracs_sorted: List[float]) -> str:
    """Sequential colour: lighter = fewer observed, darker = more observed."""
    if len(fracs_sorted) == 1:
        return AUGMP_RAMP[-1]
    pos = fracs_sorted.index(frac) / (len(fracs_sorted) - 1)
    return AUGMP_RAMP[int(round(pos * (len(AUGMP_RAMP) - 1)))]


def plot_curves(plt, runs: List[Run], out: Path, at_round: Optional[int]):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    augmp = [r for r in runs if r.attack == 'AugMP']
    fracs = sorted({r.frac for r in augmp})
    drawn = 0

    def trim(r):
        pts = [(x, 100 * y) for x, y in zip(r.rounds, r.acc) if at_round is None or x <= at_round]
        return [p[0] for p in pts], [p[1] for p in pts]

    for r in [r for r in runs if r.attack == 'benign']:
        x, y = trim(r)
        ax.plot(x, y, color=C_BENIGN, linestyle='--', marker='o', markevery=5, label=r.label()); drawn += 1
    for r in [r for r in runs if r.attack not in ('benign', 'AugMP') and r.frac == 1.0]:
        x, y = trim(r)
        ax.plot(x, y, color=C_ALIE if r.attack == 'ALIE' else C_OTHER, marker='s', markevery=5,
                label=f"{r.attack} baseline (full observation)"); drawn += 1
    for r in sorted(augmp, key=lambda r: (r.frac, r.variant, r.obs_seed or -1)):
        x, y = trim(r)
        col = variant_colour(r.variant, r.frac, fracs)
        ls = ':' if r.fixed_bounds else '-'
        mfc = 'white' if r.fixed_bounds else col
        alpha = 0.6 if (r.obs_seed is not None) else 1.0
        ax.plot(x, y, color=col, linestyle=ls, marker='D', markevery=5, markerfacecolor=mfc,
                alpha=alpha, label=r.label()); drawn += 1
    ax.set_xlabel('Communication rounds')
    ax.set_ylabel('Global testing accuracy (%)')
    ax.set_title('Attack under limited observation of benign updates')
    if drawn:
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=2, frameon=False)
    fig.savefig(out / 'observability_accuracy_curves.png')
    plt.close(fig)


def plot_param_retention(plt, rows: List[dict], out: Path):
    """Accuracy drop vs. share of parameters observed (all benign clients observed, adaptive bounds)."""
    pr = [r for r in rows if r['attack'] == 'AugMP' and not np.isnan(r['drop_pp'])
          and abs(r['frac'] - 1.0) < 1e-9 and r['variant'] in ('fixed', 'params')]
    if not any(r['param_fraction'] < 1.0 for r in pr):
        return
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    pf = sorted({r['param_fraction'] for r in pr})
    means = [np.mean([r['drop_pp'] for r in pr if r['param_fraction'] == f]) for f in pf]
    lo = [means[i] - min(r['drop_pp'] for r in pr if r['param_fraction'] == f) for i, f in enumerate(pf)]
    hi = [max(r['drop_pp'] for r in pr if r['param_fraction'] == f) - means[i] for i, f in enumerate(pf)]
    full = means[pf.index(1.0)] if 1.0 in pf else None
    x = [100 * f for f in pf]
    ax.errorbar(x, means, yerr=[lo, hi], color=AUGMP_RAMP[-2], marker='D', capsize=3, label='AugMP', zorder=4)
    for xi, m in zip(x, means):
        ret = f" ({m / full:.0%})" if full else ""
        ax.annotate(f"{m:.1f}{ret}", (xi, m), textcoords='offset points', xytext=(0, 8), ha='center', fontsize=7)
    if full:
        ax.plot(x, [full * np.sqrt(f) for f in pf], color='grey', linestyle=':', label=r'full drop $\times\sqrt{p}$')
    alie_full = [r for r in rows if r['attack'] == 'ALIE' and abs(r['frac'] - 1.0) < 1e-9 and r['param_fraction'] >= 1.0]
    if alie_full:
        ax.axhline(np.mean([r['drop_pp'] for r in alie_full]), color=C_ALIE, linestyle='--', label='ALIE (full observation)')
    ax.set_ylim(0, max(max(means) * 1.18, 1.0))
    ax.set_xlim(0, 118)
    ax.set_xlabel('Parameters of each benign update observed by the attacker (%)')
    ax.set_ylabel('Accuracy drop vs. benign setting (pp)')
    ax.set_title('Attack effect vs. parameter-level observation')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=False, fontsize=8)
    fig.savefig(out / 'observability_param_retention.png')
    plt.close(fig)


def plot_retention(plt, rows: List[dict], out: Path):
    augmp = [r for r in rows if r['attack'] == 'AugMP' and not np.isnan(r['drop_pp']) and r['param_fraction'] >= 1.0]
    if not augmp:
        return
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    # one series per attacker-side variant: mean / min / max over observed subsets at each fraction
    full_rows = [r for r in augmp if r['variant'] == 'fixed' and abs(r['frac'] - 1.0) < 1e-9]
    full = float(np.mean([r['drop_pp'] for r in full_rows])) if full_rows else None
    variants = sorted({r['variant'] for r in augmp}, key=lambda v: (v != 'fixed', v))
    for vi, variant in enumerate(variants):
        rows_v = [r for r in augmp if r['variant'] == variant]
        fr = sorted({r['frac'] for r in rows_v})
        means = [np.mean([r['drop_pp'] for r in rows_v if r['frac'] == f]) for f in fr]
        lo = [means[i] - min(r['drop_pp'] for r in rows_v if r['frac'] == f) for i, f in enumerate(fr)]
        hi = [max(r['drop_pp'] for r in rows_v if r['frac'] == f) - means[i] for i, f in enumerate(fr)]
        x = [100 * f for f in fr]
        col = AUGMP_RAMP[-2] if variant == 'fixed' else variant_colour(variant, fr[0], fr)
        hollow = 'fixed-bounds' in variant
        label = 'AugMP' + ('' if variant == 'fixed' else f' ({variant})')
        ax.errorbar(x, means, yerr=[lo, hi], color=col, marker=VARIANT_MARKERS[vi % len(VARIANT_MARKERS)],
                    markerfacecolor='white' if hollow else col, linestyle='-' if variant == 'fixed' else 'none',
                    capsize=3, label=label, zorder=4)
        for xi, m in zip(x, means):
            ret = f" ({m / full:.0%})" if full else ""
            if variant == 'fixed':
                ax.annotate(f"{m:.1f}{ret}", (xi, m), textcoords='offset points', xytext=(0, 8), ha='center', fontsize=7, color=col)
            else:  # strategy variants share the same x: stagger their labels to the right
                dy = -4 + 9 * ((vi % 3) - 1)
                ax.annotate(f"{m:.1f}{ret} {variant}", (xi, m), textcoords='offset points', xytext=(12, dy),
                            ha='left', fontsize=6.5, color=col)
    ymax = max(r['drop_pp'] for r in augmp)
    ax.set_ylim(0, max(ymax * 1.18, 1.0))
    alie_full = [r for r in rows if r['attack'] == 'ALIE' and abs(r['frac'] - 1.0) < 1e-9]
    if alie_full:
        ax.axhline(np.mean([r['drop_pp'] for r in alie_full]), color=C_ALIE, linestyle='--',
                   label='ALIE (full observation)')
    alie_part = [r for r in rows if r['attack'] == 'ALIE' and r['frac'] < 1.0 and r['param_fraction'] >= 1.0]
    if alie_part:
        ax.scatter([100 * r['frac'] for r in alie_part], [r['drop_pp'] for r in alie_part], color=C_ALIE,
                   marker='s', s=40, zorder=5, label='ALIE (limited observation)')
    ax.set_xlabel('Benign updates observed by the attacker (%)')
    ax.set_ylabel('Accuracy drop vs. benign setting (pp)')
    ax.set_xlim(0, 118)
    ax.set_title('Attack effect vs. observation level')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False, fontsize=8)
    fig.savefig(out / 'observability_retention.png')
    plt.close(fig)


def plot_dist_bound(plt, runs: List[Run], out: Path, at_round: Optional[int]):
    augmp = [r for r in runs if r.attack == 'AugMP' and any(v is not None for v in dist_bound_series(r))]
    if not augmp:
        return
    fracs = sorted({r.frac for r in augmp})
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    for r in sorted(augmp, key=lambda r: (r.frac, r.variant)):
        series = dist_bound_series(r)
        pts = [(rd, v) for rd, v in zip([l.get('round') for l in r.logs], series)
               if v is not None and (at_round is None or rd <= at_round)]
        if not pts:
            continue
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=variant_colour(r.variant, r.frac, fracs),
                linestyle=':' if r.fixed_bounds else '-', label=r.label())
    ax.set_xlabel('Communication rounds')
    ax.set_ylabel(r'Attacker-side distance bound $d_T$')
    ax.set_title(r'Automatic $d_T$ estimated from the observed subset')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False)
    fig.savefig(out / 'observability_dist_bound.png')
    plt.close(fig)


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='*', help='result JSON files (default: results/obs_*_results.json)')
    ap.add_argument('--results-dir', default='results', help='where main.py wrote the *_results.json files (relative to the repo root)')
    ap.add_argument('--out', default=None, help='output directory (default: <results-dir>/observe)')
    ap.add_argument('--window', type=int, default=10)
    ap.add_argument('--at-round', type=int, default=None)
    ap.add_argument('--suggest-bounds', action='store_true')
    ap.add_argument('--no-plots', action='store_true')
    args = ap.parse_args()

    results_dir = Path(args.results_dir)
    if not results_dir.is_absolute():
        results_dir = REPO_ROOT / results_dir
    files = args.files or sorted(glob.glob(str(results_dir / 'obs_*_results.json')))
    if not files:
        raise SystemExit(f"No result files found (looked for {results_dir / 'obs_*_results.json'})")
    out = Path(args.out) if args.out else results_dir / 'observe'
    if not out.is_absolute():
        out = REPO_ROOT / out
    out.mkdir(parents=True, exist_ok=True)
    runs = [load_run(f) for f in files]
    print(f"Loaded {len(runs)} run(s)")

    benign = [r for r in runs if r.attack == 'benign']
    benign_acc = float(np.mean([acc_at(r, args.at_round, args.window) for r in benign])) if benign else float('nan')
    if not benign:
        print("  [warn] no benign baseline among the inputs: accuracy drops will be NaN")

    rows = []
    for r in runs:
        a = acc_at(r, args.at_round, args.window)
        bands = in_band_rates(r, args.at_round) if r.attack != 'benign' else {'sim_in_band': float('nan'), 'dist_in_band': float('nan')}
        dts = [v for v in dist_bound_series(r) if v is not None]
        es = early_stop_stats(r, results_dir) if r.attack != 'benign' else {}
        ue = [v for v in unobserved_energy_series(r) if v is not None]
        rows.append({
            'name': r.name, 'attack': r.attack, 'k': r.k if r.k is not None else '', 'n_benign': r.n_benign,
            'frac': r.frac if r.frac is not None else float('nan'), 'mode': r.mode if r.attack != 'benign' else '',
            'variant': r.variant if r.attack != 'benign' else '',
            'obs_seed': '' if r.obs_seed is None else r.obs_seed, 'fixed_bounds': r.fixed_bounds,
            'param_fraction': r.param_fraction if r.attack != 'benign' else float('nan'),
            'rounds_used': min(r.rounds[-1], args.at_round) if (r.rounds and args.at_round) else (r.rounds[-1] if r.rounds else 0),
            'acc_mean': a, 'drop_pp': 100 * (benign_acc - a) if r.attack != 'benign' else 0.0,
            'retention': float('nan'), 'sim_in_band': bands['sim_in_band'], 'dist_in_band': bands['dist_in_band'],
            'dT_median': statistics.median(dts) if dts else float('nan'),
            'early_stop_mean_step': es.get('early_stop_mean_step', float('nan')),
            'final_violations': es.get('final_violations', float('nan')),
            'unobs_energy_median': statistics.median(ue) if ue else float('nan'),
        })
    # retention relative to the full-observation adaptive-bound run of the same attack
    for row in rows:
        ref = [x for x in rows if x['attack'] == row['attack'] and abs(x['frac'] - 1.0) < 1e-9
               and x['variant'] in ('fixed', '') and not (x['param_fraction'] < 1.0)]
        if ref and row['attack'] != 'benign':
            ref_drop = float(np.mean([x['drop_pp'] for x in ref]))
            row['retention'] = row['drop_pp'] / ref_drop if ref_drop else float('nan')

    csv_path = out / 'observability_summary.csv'
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for row in rows:
            w.writerow(row)

    print(f"\nBenign reference accuracy: {benign_acc:.4f}  (window={args.window}, at_round={args.at_round})")
    hdr = f"{'run':<58} {'variant':<26} {'k':>3} {'obs%':>5} {'par%':>5} {'acc':>7} {'drop':>6} {'ret':>6} {'simIB':>6} {'distIB':>6} {'dT':>7} {'steps':>6} {'uE':>5}"
    print(hdr); print('-' * len(hdr))
    for row in sorted(rows, key=lambda x: (x['attack'] != 'benign', x['attack'], -x['frac'] if not np.isnan(x['frac']) else 0, x['fixed_bounds'])):
        f_ = lambda v, fmt: ('   -' if (isinstance(v, float) and np.isnan(v)) else format(v, fmt))
        print(f"{row['name']:<58} {row['variant']:<26} {str(row['k']):>3} {f_(100 * row['frac'], '5.0f') if not np.isnan(row['frac']) else '  -':>5} "
              f"{f_(100 * row['param_fraction'], '5.0f') if not np.isnan(row['param_fraction']) else '  -':>5} "
              f"{f_(row['acc_mean'], '7.4f')} {f_(row['drop_pp'], '6.2f')} {f_(row['retention'], '6.2f')} "
              f"{f_(row['sim_in_band'], '6.2f')} {f_(row['dist_in_band'], '6.2f')} {f_(row['dT_median'], '7.4f')} {f_(row['early_stop_mean_step'], '6.1f')} "
              f"{f_(row['unobs_energy_median'], '5.2f')}")
    print(f"\nSummary CSV: {csv_path}")

    if args.suggest_bounds:
        full = [r for r in runs if r.attack == 'AugMP' and r.frac == 1.0 and r.variant == 'fixed']
        if not full:
            print("\n[suggest-bounds] need a full-observation AugMP run with adaptive bounds")
        else:
            r = max(full, key=lambda r: len(r.rounds))
            dts = [v for v in dist_bound_series(r) if v is not None]
            sims = benign_mean_pairwise_similarity(r)
            print(f"\n[suggest-bounds] from {r.name}:")
            if dts:
                print(f"  --dist-bound {statistics.median(dts):.4f}   (median over {len(dts)} rounds of the attacker-side d_T)")
            else:
                print("  d_T not logged in this run (re-run with the observability policy enabled, e.g. --k <all>)")
            if sims:
                print(f"  --sim-bound-up {statistics.median(sims):.4f}   (median benign mean pairwise cosine similarity)")

    if not args.no_plots:
        plt = style()
        plot_curves(plt, runs, out, args.at_round)
        plot_retention(plt, rows, out)
        plot_param_retention(plt, rows, out)
        plot_dist_bound(plt, runs, out, args.at_round)
        print(f"Figures written to {out}/observability_*.png")


if __name__ == '__main__':
    main()
