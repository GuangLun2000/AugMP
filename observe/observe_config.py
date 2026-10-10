# observe/observe_config.py
# ONE place to configure the limited-observability experiment.
#
#   EXPERIMENT          the run you want. Every knob that varies between runs lives here -- edit this.
#   FIXED               attack / training hyper-parameters pinned at the paper's AugMP values. Not per-run.
#   make_config(...)    complete config-override dict for ONE run, fed to main(config_overrides=...).
#                       Anything you do not pass is taken from EXPERIMENT, so make_config(k=2) means
#                       "the EXPERIMENT run, but the attackers observe only 2 benign clients".
#   EXPERIMENT_CONFIG   = make_config()  -> what the Colab notebook (Step 3) runs.
#
# A run therefore goes through the ORIGINAL main.py path -- main(config_overrides=make_config(...)) --
# exactly like any other experiment (usual per-round log, standard figures, detailed statistics).
# The Colab notebook, Step 6 and run_observability_sweep.py all call make_config(), so there is one
# pinned config and no duplicated / divergent settings.

from typing import Optional

# ================================================================================================
# EDIT HERE -- the experiment to run.
#   k            benign updates the attackers observe per round: int count | 0 = Secure Aggregation
#                (k=1 is degenerate: the VGAE graph needs >= 2 observed updates, auto d_T -> 0)
#   mode         'fixed' (same peers every round) | 'random' | 'largest' | 'adaptive'
#   anchor       also feed the previous global-broadcast delta as pseudo client -1
#   obs_seed     seed for drawing the observed subset (None = seed)
#   attack       'AugMP' | 'ALIE' | 'Gaussian' | 'SignFlipping' | 'none' (benign baseline, k ignored)
#   clients / attackers   paper setting: 7 agents = 5 benign + 2 attackers
#   rounds       50 for every run (anchors and limited-observation runs alike)
#   alpha        Dirichlet heterogeneity (Qwen reference run / paper Fig. 3(c): 0.3)
#   local_epochs local training epochs per round (Qwen reference run: 2)
#   dist_bound / sim_bound_up   None = adaptive from the observed updates (paper); a float freezes it
#   param_fraction  None = attackers see every coordinate of each observed update (paper). A float p in
#                (0, 1] hides a random (1 - p) share of the coordinates of every observed benign update
#                (same mask for all rows of a round, redrawn each round); the server still aggregates
#                the complete updates. p = 1.0 is a no-op.
#   param_fill   'zero' = hidden coordinates are unknown (0); 'gaussian' = RMS-matched noise (control)
#   param_mask_fixed   True = one mask for the whole run instead of a fresh one per round
# Examples:  make_config()                      the EXPERIMENT run itself
#            make_config(param_fraction=0.2)    20% of the parameters of all 5 benign updates
#            make_config(k=2)                   40% observation
#            make_config(k=0)                   Secure Aggregation endpoint
#            make_config(attack='none')         benign baseline
#            make_config(k=2, attack='ALIE')    ALIE under the same limitation
# ================================================================================================
EXPERIMENT = dict(
    # --- what the attackers may observe ---
    k=3,
    mode='fixed',
    anchor=False,
    obs_seed=None,
    criterion='deviant',      # 'adaptive' mode only: 'deviant' | 'representative'
    explore_rounds=None,      # 'adaptive' mode only: rotation rounds before locking in
    global_window=5,          # Secure Aggregation only: recent global deltas used as pseudo rows
    # --- federation ---
    attack='AugMP',
    clients=7,
    attackers=2,
    rounds=50,
    seed=42069,
    # --- data / training ---
    model='qwen',             # key of MODEL_PRESETS (Qwen/Qwen2.5-0.5B)
    dataset='ag_news',        # key of DATASET_PRESETS
    alpha=0.3,
    local_epochs=2,
    # --- parameter-level partial observation (None = off) ---
    param_fraction=None,
    param_fill='zero',
    param_mask_fixed=False,
    # --- optional frozen bounds ---
    dist_bound=None,
    sim_bound_up=None,
    suffix='',                # appended to the experiment name
)

# ---------------------------------------------------------------- pinned hyper-parameters (paper AugMP)
# Everything that must NOT change between runs of the ablation. Per-run knobs are in EXPERIMENT above.
# Values = the Qwen reference run of paper Fig. 3(c) (observe_results/Qwen_ref-non-iid-0.3历史参考数据, 2026-03-06,
# seed 42069, alpha 0.3); keys its config block does not print were read from its optimisation log.
FIXED = {
    'num_benign_clients': None,
    'data_distribution': 'non-iid',
    'dataset_size_limit': 20000,
    # local training
    'client_lr': 5e-5,
    'server_lr': 1.0,
    'batch_size': 128,
    'test_batch_size': 256,
    'alpha': 0.0,             # FedProx mu (0 = plain FedAvg)
    # LoRA
    'use_lora': True,
    'lora_r': 8,
    'lora_alpha': 16,
    'lora_dropout': 0.1,
    'lora_target_modules': None,
    # attack: adaptive bounds, exactly as in the main experiments
    'attack_start_round': 0,
    'sim_bound_low': None,    # None = observed benign min pairwise sim (band [min, mean] is never empty)
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
    # proxy objective
    'attacker_use_proxy_data': True,
    'proxy_step': 0.001,
    'proxy_steps': 200,
    'proxy_sample_size': 200,
    'proxy_max_batches_opt': 1,
    'proxy_max_batches_eval': 1,
    'attacker_proxy_grad_clip_norm': 1.0,
    'early_stop_constraint_stability_steps': 1,
    'attacker_claimed_data_size': None,
    # VGAE + graph
    'dim_reduction_size': 1000,
    'vgae_epochs': 20,
    'vgae_lr': 0.01,
    'vgae_hidden_dim': 64,
    'vgae_latent_dim': 32,
    'vgae_dropout': 0,
    'vgae_kl_weight': 0.1,
    'graph_threshold': 0.5,
    # keep the ablation lean (no checkpoint / downstream generation)
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


def k_tag(k) -> str:
    """Filename-safe tag for an observation level: '2' (count) or '0p29' (fraction)."""
    return f"{k:.2f}".replace('0.', '0p') if isinstance(k, float) else str(k)


def make_config(k=None, *, extra: Optional[dict] = None, **overrides) -> dict:
    """Complete config-override dict for one run (fed to main(config_overrides=...)).

    Every keyword not given is taken from EXPERIMENT (k included when k is None). `overrides` accepts
    exactly the EXPERIMENT keys; `extra` is a dict of raw main.py config keys applied last.
    k: benign clients the attackers observe -- int count, float in (0,1] fraction, or 0 = Secure
       Aggregation (no benign update observed, only the global broadcast). Ignored when attack='none'.
    """
    unknown = set(overrides) - set(EXPERIMENT)
    if unknown:
        raise TypeError(f"make_config: unknown option(s) {sorted(unknown)}; valid: {sorted(EXPERIMENT)}")
    o = dict(EXPERIMENT)
    o.update(overrides)
    if k is not None:
        o['k'] = k
    if o['attack'] not in ATTACK_CHOICES:
        raise ValueError(f"attack must be one of {ATTACK_CHOICES}, got {o['attack']!r}")
    if o['attackers'] >= o['clients']:
        raise ValueError(f"attackers ({o['attackers']}) must be smaller than clients ({o['clients']})")
    pf = o['param_fraction']
    if pf is not None and (isinstance(pf, bool) or not isinstance(pf, (int, float)) or not (0.0 < float(pf) <= 1.0)):
        raise ValueError(f"param_fraction must be None or a number in (0, 1], got {pf!r}")
    if o['param_fill'] not in ('zero', 'gaussian'):
        raise ValueError(f"param_fill must be 'zero' or 'gaussian', got {o['param_fill']!r}")

    cfg = dict(FIXED)
    cfg.update(MODEL_PRESETS[o['model']])
    cfg.update(DATASET_PRESETS[o['dataset']])
    cfg['num_clients'] = o['clients']
    cfg['num_rounds'] = o['rounds']
    cfg['seed'] = o['seed']
    cfg['dirichlet_alpha'] = o['alpha']
    cfg['local_epochs'] = o['local_epochs']
    cfg['dist_bound'] = o['dist_bound']        # None = adaptive (benign max over the observed updates)
    cfg['sim_bound_up'] = o['sim_bound_up']    # None = adaptive (observed benign mean pairwise similarity)

    model, dataset, attack, rounds = o['model'], o['dataset'], o['attack'], o['rounds']
    n_benign = o['clients'] - o['attackers']
    if attack == 'none':
        cfg['num_attackers'] = 0
        name = f"obs_{model}_{dataset}_benign_r{rounds}"
    else:
        kk = o['k']
        if kk is None:
            raise ValueError("k must be given (int count, float fraction or 0) unless attack='none'")
        if isinstance(kk, int) and kk > n_benign:
            raise ValueError(f"k={kk} exceeds the number of benign clients ({n_benign})")
        cfg['num_attackers'] = o['attackers']
        cfg['attack_method'] = attack
        cfg['attacker_observed_benign'] = kk
        cfg['attacker_observation_mode'] = o['mode']
        cfg['attacker_observation_seed'] = o['obs_seed']
        cfg['attacker_observation_criterion'] = o['criterion']
        cfg['attacker_observation_explore_rounds'] = o['explore_rounds']
        cfg['attacker_observation_anchor_global'] = bool(o['anchor'])
        cfg['attacker_observation_global_window'] = o['global_window']
        if pf is not None:
            cfg['attacker_observed_param_fraction'] = float(pf)
            cfg['attacker_observed_param_fill'] = o['param_fill']
            cfg['attacker_observed_param_mask_fixed'] = bool(o['param_mask_fixed'])
        if isinstance(kk, int) and kk == 0:
            name = f"obs_{model}_{dataset}_{attack.lower()}_k0of{n_benign}_secagg"
        else:
            mode_tag = o['mode'] + (f"-{o['criterion']}" if o['mode'] == 'adaptive' else '')
            name = f"obs_{model}_{dataset}_{attack.lower()}_k{k_tag(kk)}of{n_benign}_{mode_tag}"
            if o['anchor']:
                name += "_anchor"
        if pf is not None and float(pf) < 1.0:
            name += f"_p{k_tag(float(pf))}"
            if o['param_fill'] != 'zero':
                name += f"-{o['param_fill']}"
            if o['param_mask_fixed']:
                name += "-fixedmask"
        if o['obs_seed'] is not None:
            name += f"_os{o['obs_seed']}"
        name += f"_r{rounds}"
    if o['suffix']:
        name += f"_{o['suffix']}"
    cfg['experiment_name'] = name
    if extra:
        cfg.update(extra)
    return cfg


# The experiment the notebook runs, built once from EXPERIMENT above.
EXPERIMENT_CONFIG = make_config()


if __name__ == '__main__':
    # sanity: names follow one scheme, EXPERIMENT drives the defaults, FIXED never leaks a per-run knob
    e = EXPERIMENT_CONFIG
    print("EXPERIMENT_CONFIG:", e['experiment_name'])
    assert e['experiment_name'] == 'obs_qwen_ag_news_augmp_k3of5_fixed_r50', e['experiment_name']
    assert e['num_clients'] == 7 and e['num_attackers'] == 2 and e['local_epochs'] == 2
    assert e['dirichlet_alpha'] == 0.3 and e['model_name'] == 'Qwen/Qwen2.5-0.5B'
    assert e['lambda_update_mode'] == 'alm' and e['dist_bound'] is None and e['sim_bound_up'] is None
    assert e['sim_bound_low'] is None and e['dim_reduction_size'] == 1000 and e['proxy_sample_size'] == 200
    assert not (set(FIXED) & {'num_clients', 'num_attackers', 'num_rounds', 'seed', 'dirichlet_alpha', 'local_epochs'})
    # name-scheme checks use explicit observation keys so they never depend on what EXPERIMENT currently holds
    BASE = dict(mode='fixed', anchor=False, obs_seed=None, param_fraction=None, param_fill='zero', param_mask_fixed=False)
    mc = lambda **kw: make_config(**{**BASE, **kw})
    a = mc(k=2, mode='largest', anchor=True, rounds=30)
    assert a['experiment_name'] == 'obs_qwen_ag_news_augmp_k2of5_largest_anchor_r30', a['experiment_name']
    assert mc(k=0, rounds=30)['experiment_name'] == 'obs_qwen_ag_news_augmp_k0of5_secagg_r30'
    assert mc(k=2, obs_seed=1, rounds=30)['experiment_name'] == 'obs_qwen_ag_news_augmp_k2of5_fixed_os1_r30'
    assert mc(k=2, attack='ALIE', rounds=30)['experiment_name'] == 'obs_qwen_ag_news_alie_k2of5_fixed_r30'
    b = mc(attack='none', rounds=50)
    assert b['experiment_name'] == 'obs_qwen_ag_news_benign_r50' and b['num_attackers'] == 0
    assert 'attacker_observed_benign' not in b
    assert mc(k=0.4, rounds=30)['experiment_name'] == 'obs_qwen_ag_news_augmp_k0p40of5_fixed_r30'
    assert mc(k=7, clients=10, attackers=3, rounds=50)['experiment_name'] == 'obs_qwen_ag_news_augmp_k7of7_fixed_r50'
    assert mc(k=5, local_epochs=2)['local_epochs'] == 2
    assert mc(k=2, dist_bound=0.5, sim_bound_up=0.3)['dist_bound'] == 0.5
    assert mc(k=5, extra={'proxy_steps': 50})['proxy_steps'] == 50
    # parameter-level partial observation
    q = mc(k=5, param_fraction=0.2, rounds=50)
    assert q['experiment_name'] == 'obs_qwen_ag_news_augmp_k5of5_fixed_p0p20_r50', q['experiment_name']
    assert q['attacker_observed_param_fraction'] == 0.2 and q['attacker_observed_param_fill'] == 'zero'
    assert q['attacker_observed_param_mask_fixed'] is False and q['attacker_observed_benign'] == 5
    assert mc(k=5, param_fraction=0.6, param_fill='gaussian', param_mask_fixed=True, rounds=50)['experiment_name'] \
        == 'obs_qwen_ag_news_augmp_k5of5_fixed_p0p60-gaussian-fixedmask_r50'
    assert 'attacker_observed_param_fraction' not in mc(k=5)                         # None: off
    assert mc(k=5, param_fraction=1.0)['experiment_name'] == mc(k=5)['experiment_name']  # p=1 -> same run name
    assert 'attacker_observed_param_fraction' not in mc(attack='none', param_fraction=0.2)  # benign ignores it
    for bad in (dict(param_fraction=0.0), dict(param_fraction=2), dict(param_fill='noise')):
        try:
            make_config(k=5, **bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"make_config accepted {bad}")
    for bad in (dict(k=6), dict(bogus=1), dict(attack='foo'), dict(clients=2, attackers=2)):
        try:
            make_config(**bad)
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError(f"make_config accepted {bad}")
    print('observe_config.py self-test passed; sample run:', a['experiment_name'])
