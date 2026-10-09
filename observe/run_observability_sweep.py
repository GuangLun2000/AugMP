#!/usr/bin/env python3
"""
run_observability_sweep.py — limited-observability ablation driver for AugMP.

Reviewer concern: in practice an adversary may observe only a subset of the benign updates.
This driver re-uses main.py unchanged (config overrides only) and launches every run in a fresh
subprocess, so each run gets a clean CUDA context and its own log under results/observe/logs/.

Ablation setting (ABLATION_SETTING below, override with CLI flags):
  10 agents = 7 benign + 3 attackers (30% attackers, close to the paper's 2/7), Dirichlet 0.3,
  20k AG News samples, DistilBERT + LoRA(r=8).  Attackers observe k of the 7 benign updates.

Typical sequence (run from the repo root as `python observe/run_observability_sweep.py ...`):
  # 1) anchors at full observation (50 rounds): benign baseline, ALIE, AugMP
  python observe/run_observability_sweep.py --attack none ALIE AugMP --k 7 --rounds 50
  # 2) observability sweep (30 rounds; compare with the anchors at round 30)
  python observe/run_observability_sweep.py --k 4 3 2 --rounds 30
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

# Fully pinned config for the observability experiment. Every training/attack hyper-parameter is
# fixed HERE so the experiment is reproducible on its own and never inherits main.py's default block
# (main.py is used for a different experiment and changes over time). Only the observation keys and
# the CLI-exposed knobs (model, dataset, k, mode, rounds, seed, alpha) vary across runs; everything
# below is a controlled variable held at the paper-standard AugMP values.
ABLATION_SETTING = {
    # --- federation: 10 agents = 7 benign + 3 attackers (~30% attackers, close to the paper's 2/7) ---
    'num_clients': 10,
    'num_attackers': 3,
    'num_benign_clients': None,
    'seed': 42069,
    # --- data (paper standard; non-IID Dirichlet 0.3) ---
    'data_distribution': 'non-iid',
    'dirichlet_alpha': 0.3,
    'dataset_size_limit': 20000,
    # --- local training (paper standard) ---
    'client_lr': 5e-5,
    'server_lr': 1.0,
    'local_epochs': 5,
    'batch_size': 128,
    'test_batch_size': 256,
    'alpha': 0.0,
    # --- LoRA (paper standard) ---
    'use_lora': True,
    'lora_r': 8,
    'lora_alpha': 16,
    'lora_dropout': 0.1,
    'lora_target_modules': None,
    # --- attack: adaptive bounds, exactly as in the main experiments ---
    'attack_start_round': 0,
    'dist_bound': None,            # auto-estimate d_T from the observed subset (overridden by --dist-bound)
    'sim_bound_low': 0.0,
    'sim_bound_up': None,          # auto = benign mean pairwise similarity (overridden by --sim-bound-up)
    'server_similarity_mode': 'pairwise',
    'use_lagrangian_dual': True,
    'use_cosine_similarity_constraint': True,
    'use_pairwise_similarity_in_constraint': True,
    'use_augmented_lagrangian': True,
    'lambda_update_mode': 'alm',
    'lambda_dist_init': 0.1, 'lambda_dist_lr': 0.01,
    'lambda_sim_low_init': 0.1, 'lambda_sim_up_init': 0.1,
    'lambda_sim_low_lr': 0.01, 'lambda_sim_up_lr': 0.01,
    'rho_dist_init': 1.0, 'rho_sim_low_init': 1.0, 'rho_sim_up_init': 1.0,
    'rho_adaptive': True, 'rho_theta': 0.5, 'rho_increase_factor': 2.0,
    'rho_min': 1e-4, 'rho_max': 1e4,
    # --- proxy objective (paper standard) ---
    'attacker_use_proxy_data': True,
    'proxy_step': 0.001,
    'proxy_steps': 200,
    'proxy_sample_size': 512,
    'proxy_max_batches_opt': 1,
    'proxy_max_batches_eval': 1,
    'attacker_proxy_grad_clip_norm': 1.0,
    'early_stop_constraint_stability_steps': 1,
    'attacker_claimed_data_size': None,
    # --- VGAE + graph (paper standard) ---
    'dim_reduction_size': 500,
    'vgae_epochs': 20,
    'vgae_lr': 0.01,
    'vgae_hidden_dim': 64,
    'vgae_latent_dim': 32,
    'vgae_dropout': 0,
    'vgae_kl_weight': 0.1,
    'graph_threshold': 0.5,
    # --- keep the ablation lean (no checkpoint / downstream generation) ---
    'save_global_checkpoint': False,
    'run_downstream_after_fl': False,
}

MODEL_PRESETS = {
    'distilbert': {'model_name': 'distilbert-base-uncased', 'grad_clip_norm': 1.0},
    'gpt2':       {'model_name': 'gpt2', 'grad_clip_norm': 1.0},
    'pythia':     {'model_name': 'EleutherAI/pythia-160m', 'grad_clip_norm': 0.5},
    'opt':        {'model_name': 'facebook/opt-125m', 'grad_clip_norm': 1.0},
    'qwen':       {'model_name': 'Qwen/Qwen2.5-0.5B', 'grad_clip_norm': 1.0},
}
DATASET_PRESETS = {
    'ag_news':       {'dataset': 'ag_news', 'num_labels': 4, 'max_length': 128},
    'yahoo_answers': {'dataset': 'yahoo_answers', 'num_labels': 10, 'max_length': 256},
    'imdb':          {'dataset': 'imdb', 'num_labels': 2, 'max_length': 256},
    'dbpedia':       {'dataset': 'dbpedia', 'num_labels': 14, 'max_length': 256},
}
ATTACK_CHOICES = ('AugMP', 'ALIE', 'Gaussian', 'SignFlipping', 'none')


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


def k_tag(k) -> str:
    return f"{k:.2f}".replace('0.', '0p') if isinstance(k, float) else str(k)


def build_overrides(args, attack: str, k, obs_seed):
    cfg = dict(ABLATION_SETTING)
    cfg.update(MODEL_PRESETS[args.model])
    cfg.update(DATASET_PRESETS[args.dataset])
    cfg['num_clients'] = args.clients
    cfg['num_rounds'] = args.rounds
    cfg['seed'] = args.seed
    cfg['dirichlet_alpha'] = args.alpha
    if args.dist_bound is not None:
        cfg['dist_bound'] = args.dist_bound
    if args.sim_bound_up is not None:
        cfg['sim_bound_up'] = args.sim_bound_up

    n_benign = args.clients - args.attackers
    if attack == 'none':
        cfg['num_attackers'] = 0
        name = f"obs_{args.model}_{args.dataset}_benign_r{args.rounds}"
    else:
        cfg['num_attackers'] = args.attackers
        cfg['attack_method'] = attack
        cfg['attacker_observed_benign'] = k
        cfg['attacker_observation_mode'] = args.mode
        cfg['attacker_observation_seed'] = obs_seed
        cfg['attacker_observation_criterion'] = args.criterion
        cfg['attacker_observation_explore_rounds'] = args.explore_rounds
        cfg['attacker_observation_anchor_global'] = bool(args.anchor)
        cfg['attacker_observation_global_window'] = args.global_window
        if isinstance(k, int) and k == 0:
            mode_tag = 'secagg'  # Secure Aggregation: no benign updates observed, only the global broadcast
            name = f"obs_{args.model}_{args.dataset}_{attack.lower()}_k0of{n_benign}_secagg"
        else:
            mode_tag = args.mode + (f"-{args.criterion}" if args.mode == 'adaptive' else '')
            name = f"obs_{args.model}_{args.dataset}_{attack.lower()}_k{k_tag(k)}of{n_benign}_{mode_tag}"
            if args.anchor:
                name += "_anchor"
        if obs_seed is not None:
            name += f"_os{obs_seed}"
        name += f"_r{args.rounds}"
    if args.suffix:
        name += f"_{args.suffix}"
    cfg['experiment_name'] = name
    if args.extra:
        cfg.update(json.loads(args.extra))
    return name, cfg


def run_one(name: str, cfg: dict, results_dir: Path, dry_run: bool) -> int:
    log_dir = results_dir / 'observe' / 'logs'
    print("\n" + "=" * 78)
    print(f"RUN {name}")
    shown = {k: cfg[k] for k in ('model_name', 'dataset', 'num_clients', 'num_attackers', 'num_rounds',
                                 'dirichlet_alpha', 'attack_method', 'attacker_observed_benign',
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
    ap.add_argument('--clients', type=int, default=ABLATION_SETTING['num_clients'])
    ap.add_argument('--attackers', type=int, default=ABLATION_SETTING['num_attackers'])
    ap.add_argument('--alpha', type=float, default=ABLATION_SETTING['dirichlet_alpha'], help='Dirichlet alpha')
    ap.add_argument('--seed', type=int, default=ABLATION_SETTING['seed'])
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
