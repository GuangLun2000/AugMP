#!/usr/bin/env python3
"""
run_observability_sweep.py — limited-observability ablation driver for AugMP.

Reviewer concern: in practice an adversary may observe only a subset of the benign updates.
This driver re-uses main.py unchanged (config overrides only) and launches every run in a fresh
subprocess, so each run gets a clean CUDA context and its own log under results/observe/logs/.

Ablation setting (observe/observe_config.py:EXPERIMENT supplies every default, override with CLI flags):
  paper setting 7 agents = 5 benign + 2 attackers, Dirichlet 0.3, 20k AG News samples,
  DistilBERT + LoRA(r=8), 5 local epochs.  Attackers observe k of the 5 benign updates.

Typical sequence (run from the repo root as `python observe/run_observability_sweep.py ...`):
  # 1) anchors at full observation (50 rounds): benign baseline, ALIE, AugMP
  python observe/run_observability_sweep.py --attack none ALIE AugMP --k 5 --rounds 50
  # 2) observability sweep (30 rounds; compare with the anchors at round 30)
  python observe/run_observability_sweep.py --k 3 2 --rounds 30
  # 3) a second observed subset at k=2 (subset variance)
  python observe/run_observability_sweep.py --k 2 --obs-seed 1 --rounds 30
  # 4) k=2 with d_T / sim_bound_up frozen at the full-observation values (isolates the GRL part)
  #    (get the values with: python observe/plot_observability.py --suggest-bounds)
  python observe/run_observability_sweep.py --k 2 --rounds 30 --dist-bound <dT> --sim-bound-up <s> --suffix fixedbounds
  # 5) ALIE under the same limited observation
  python observe/run_observability_sweep.py --attack ALIE --k 2 --rounds 30
  # 6) attacker-side strategies at k=2 (all use only information the attacker legitimately has)
  python observe/run_observability_sweep.py --k 2 --rounds 30 --mode largest                 # most influential peers
  python observe/run_observability_sweep.py --k 2 --rounds 30 --mode largest --anchor        # + previous broadcast as anchor row
  python observe/run_observability_sweep.py --k 2 --rounds 30 --mode adaptive --criterion deviant --anchor
  # 7) Secure Aggregation endpoint (k=0): attackers observe no benign updates, only the global broadcast
  python observe/run_observability_sweep.py --k 0 --rounds 30
Then:  python observe/plot_observability.py --at-round 30
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent  # repo root (this file lives in observe/)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))  # so `observe` is importable when run as `python observe/...`

# Config is built by observe/observe_config.py (single source of truth; the Colab notebook uses the
# same make_config()). EXPERIMENT supplies the defaults; FIXED holds the pinned hyper-parameters.
from observe.observe_config import (EXPERIMENT, MODEL_PRESETS, DATASET_PRESETS, ATTACK_CHOICES,
                                    make_config, k_tag)


def parse_k(text: str):
    """'2' -> 2 (count), '0.29' -> 0.29 (fraction)."""
    if '.' in text:
        v = float(text)
        if not (0.0 < v <= 1.0):
            raise argparse.ArgumentTypeError(f"fraction must be in (0,1], got {text}")
        return v
    v = int(text)
    if v < 0:
        raise argparse.ArgumentTypeError(f"count must be >= 0 (0 = Secure Aggregation), got {text}")
    return v




def build_overrides(args, attack, k, obs_seed):
    """Delegate to observe_config.make_config so the driver and the notebook share one pinned config."""
    extra = json.loads(args.extra) if args.extra else None
    cfg = make_config(
        k, attack=attack, model=args.model, dataset=args.dataset, rounds=args.rounds,
        seed=args.seed, alpha=args.alpha, clients=args.clients, attackers=args.attackers, local_epochs=args.local_epochs,
        mode=args.mode, anchor=args.anchor, criterion=args.criterion, explore_rounds=args.explore_rounds,
        global_window=args.global_window, obs_seed=obs_seed, dist_bound=args.dist_bound,
        sim_bound_up=args.sim_bound_up, suffix=args.suffix, extra=extra,
    )
    return cfg['experiment_name'], cfg


def run_one(name: str, cfg: dict, results_dir: Path, dry_run: bool) -> int:
    log_dir = results_dir / 'observe' / 'logs'
    print("\n" + "=" * 78)
    print(f"RUN {name}")
    shown = {k: cfg[k] for k in ('model_name', 'dataset', 'num_clients', 'num_attackers', 'num_rounds',
                                 'dirichlet_alpha', 'local_epochs', 'attack_method', 'attacker_observed_benign',
                                 'attacker_observation_mode', 'attacker_observation_seed',
                                 'attacker_observation_criterion', 'attacker_observation_explore_rounds',
                                 'attacker_observation_anchor_global', 'attacker_observation_global_window',
                                 'dist_bound', 'sim_bound_up') if k in cfg}
    print("  " + json.dumps(shown))
    print("=" * 78)
    if dry_run:
        return 0
    log_dir.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, '-u', '-c',
           'import json, sys; from main import main; main(json.loads(sys.argv[1]))',
           json.dumps(cfg)]
    log_path = log_dir / f"{name}.log"
    t0 = time.time()
    with open(log_path, 'w') as log:
        proc = subprocess.Popen(cmd, cwd=str(REPO_ROOT), stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, bufsize=1)
        for line in proc.stdout:
            log.write(line)
            # keep the console readable: progress + key attacker/observability lines only,
            # with the elapsed time prefixed to each round header for cost calibration
            if line.startswith('Round ') and '/' in line:
                sys.stdout.write(f"[+{(time.time() - t0) / 60:6.1f} min] {line}")
            elif any(tok in line for tok in ('Clean Accuracy', 'Observability', 'Results saved',
                                              'Error', 'error', 'Traceback', 'Partitioning', 'ATTACKER', 'BENIGN')):
                sys.stdout.write(line)
        proc.wait()
    status = 'OK' if proc.returncode == 0 else f'FAILED (exit {proc.returncode})'
    print(f"  -> {status} in {(time.time() - t0) / 60:.1f} min; log: {log_path}")
    return proc.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--attack', nargs='+', default=['AugMP'], choices=ATTACK_CHOICES,
                    help="attack method(s); 'none' = benign baseline with num_attackers=0")
    ap.add_argument('--k', nargs='+', type=parse_k, default=[2],
                    help="observed benign clients per run: int = count, float in (0,1] = fraction")
    ap.add_argument('--mode', default='fixed', choices=('fixed', 'random', 'largest', 'adaptive'))
    ap.add_argument('--criterion', default='deviant', choices=('deviant', 'representative'),
                    help="adaptive mode: lock onto the most deviant or the most representative peers")
    ap.add_argument('--explore-rounds', type=int, default=None,
                    help="adaptive mode: rotation rounds before locking in (default ceil(benign / k))")
    ap.add_argument('--anchor', action='store_true',
                    help="also hand attackers the previous broadcast update as an anchor row (pseudo client -1)")
    ap.add_argument('--global-window', type=int, default=5,
                    help="SecAgg (--k 0): number of recent global-broadcast deltas used as pseudo benign rows")
    ap.add_argument('--obs-seed', nargs='*', type=int, default=[None],
                    help="seed(s) for drawing the observed subset (default: the experiment seed)")
    ap.add_argument('--rounds', type=int, default=30)
    ap.add_argument('--model', default='distilbert', choices=sorted(MODEL_PRESETS))
    ap.add_argument('--dataset', default='ag_news', choices=sorted(DATASET_PRESETS))
    ap.add_argument('--clients', type=int, default=EXPERIMENT['clients'])
    ap.add_argument('--attackers', type=int, default=EXPERIMENT['attackers'])
    ap.add_argument('--alpha', type=float, default=EXPERIMENT['alpha'], help='Dirichlet alpha')
    ap.add_argument('--seed', type=int, default=EXPERIMENT['seed'])
    ap.add_argument('--local-epochs', type=int, default=EXPERIMENT['local_epochs'])
    ap.add_argument('--dist-bound', type=float, default=None, help='freeze d_T (default: adaptive from observed updates)')
    ap.add_argument('--sim-bound-up', type=float, default=None, help='freeze the similarity upper bound')
    ap.add_argument('--suffix', default='', help='appended to experiment names')
    ap.add_argument('--extra', default='', help='JSON dict of additional config overrides')
    ap.add_argument('--skip-existing', action='store_true', help='skip runs whose *_results.json already exists')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if args.attackers >= args.clients:
        ap.error('--attackers must be smaller than --clients')
    results_dir = REPO_ROOT / 'results'  # main.py writes to ./results (relative to the repo root)

    plan = []
    for attack in args.attack:
        if attack == 'none':
            plan.append(build_overrides(args, attack, None, None))
            continue
        for k in args.k:
            for obs_seed in (args.obs_seed or [None]):
                plan.append(build_overrides(args, attack, k, obs_seed))

    # de-duplicate while keeping order (e.g. 'none' listed with several k)
    seen, ordered = set(), []
    for name, cfg in plan:
        if name not in seen:
            seen.add(name)
            ordered.append((name, cfg))

    print(f"Planned {len(ordered)} run(s):")
    for name, _ in ordered:
        print(f"  - {name}")

    failures = []
    for name, cfg in ordered:
        if args.skip_existing and (results_dir / f"{name}_results.json").exists():
            print(f"\nSKIP {name} (results exist)")
            continue
        rc = run_one(name, cfg, results_dir, args.dry_run)
        if rc != 0:
            failures.append(name)

    print("\n" + "=" * 78)
    if failures:
        print(f"{len(failures)} run(s) failed: {failures}")
        sys.exit(1)
    print("All runs finished." if not args.dry_run else "Dry run complete.")
    print("Next: python observe/plot_observability.py --at-round", args.rounds)


if __name__ == '__main__':
    main()
