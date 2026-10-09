# observe/observe_config.py
# Single source of truth for the limited-observability experiment's configuration.
#
# make_config() returns a complete config-override dict for ONE run. The experiment therefore runs
# through the ORIGINAL main.py path -- main(config_overrides=make_config(...)) -- exactly like any
# other experiment, producing the usual per-round training log, the standard figures and the detailed
# statistics. Both the Colab notebook and run_observability_sweep.py call make_config(), so there is
# one pinned config and no duplicated / divergent settings.
#
# Every training/attack hyper-parameter is pinned in STANDARD at the paper-standard AugMP values, so
# the experiment never silently inherits main.py's default config block (which is used for a different
# experiment and changes over time). Only the observation keys and the few run knobs vary across runs.

from typing import Optional

# ================================================================================================
# EDIT HERE -- the ONE place to choose the observability experiment to run.
# The Colab notebook (Step 3) and any `main(config_overrides=ACTIVE_CONFIG)` call read ACTIVE_CONFIG
# built from this; nothing is configured in the notebook itself. Change these values, not the notebook.
#
#   k      : benign updates the attacker observes -- int count | 0 = Secure Aggregation | 7 = full
#   mode   : 'fixed' | 'random' | 'largest' | 'adaptive'
#   anchor : also use the global-broadcast anchor row (recommended main line)
#   rounds : 30 for the limited-observation sweep runs, 50 for full-observation reference runs
#   attack : 'AugMP' (default) | 'ALIE' | 'none' (benign baseline, no attackers)
# Examples:  dict(k=7, rounds=50)                 full-observation reference
#            dict(k=0, rounds=30)                 Secure Aggregation endpoint
#            dict(k=None, attack='none', rounds=50)  benign baseline
#            dict(k=2, attack='ALIE')             ALIE under the same limitation
# (full signature in make_config() below: model, dataset, alpha, clients, attackers, criterion, ...)
# ================================================================================================
ACTIVE = dict(k=7, rounds=50)   # full observation (attacker sees all 7 benign updates), 50-round reference run

# ---------------------------------------------------------------- controlled variables (paper standard)
STANDARD = {
    # federation: 10 agents = 7 benign + 3 attackers (~30% attackers, close to the paper's 2/7)
    'num_clients': 10,
    'num_attackers': 3,
    'num_benign_clients': None,
    'seed': 42069,
    # data: non-IID Dirichlet 0.3 (paper's main heterogeneity level)
    'data_distribution': 'non-iid',
    'dirichlet_alpha': 0.3,
    'dataset_size_limit': 20000,
    # local training
    'client_lr': 5e-5,
    'server_lr': 1.0,
    'local_epochs': 5,
    'batch_size': 128,
    'test_batch_size': 256,
    'alpha': 0.0,
    # LoRA
    'use_lora': True,
    'lora_r': 8,
    'lora_alpha': 16,
    'lora_dropout': 0.1,
    'lora_target_modules': None,
    # attack: adaptive bounds, exactly as in the main experiments
    'attack_start_round': 0,
    'dist_bound': None,
    'sim_bound_low': 0.0,
    'sim_bound_up': None,
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
    'proxy_sample_size': 512,
    'proxy_max_batches_opt': 1,
    'proxy_max_batches_eval': 1,
    'attacker_proxy_grad_clip_norm': 1.0,
    'early_stop_constraint_stability_steps': 1,
    'attacker_claimed_data_size': None,
    # VGAE + graph
    'dim_reduction_size': 500,
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


def make_config(k=2, *, attack='AugMP', model='distilbert', dataset='ag_news',
                rounds=30, seed=42069, alpha=0.3, clients=10, attackers=3,
                mode='fixed', anchor=False, criterion='deviant', explore_rounds=None,
                global_window=5, obs_seed=None, dist_bound=None, sim_bound_up=None,
                suffix='', extra: Optional[dict] = None) -> dict:
    """Complete config-override dict for one observability run (fed to main(config_overrides=...)).

    k: benign clients the attackers observe -- int count, float in (0,1] fraction, or 0 = Secure
       Aggregation (no benign update observed, only the global broadcast). Ignored when attack='none'.
    attack: 'AugMP' | 'ALIE' | 'Gaussian' | 'SignFlipping' | 'none' (benign baseline, no attackers).
    mode: 'fixed' | 'random' | 'largest' | 'adaptive'. anchor: add the global-broadcast anchor row.
    """
    cfg = dict(STANDARD)
    cfg.update(MODEL_PRESETS[model])
    cfg.update(DATASET_PRESETS[dataset])
    cfg['num_clients'] = clients
    cfg['num_rounds'] = rounds
    cfg['seed'] = seed
    cfg['dirichlet_alpha'] = alpha
    if dist_bound is not None:
        cfg['dist_bound'] = dist_bound
    if sim_bound_up is not None:
        cfg['sim_bound_up'] = sim_bound_up

    n_benign = clients - attackers
    if attack == 'none':
        cfg['num_attackers'] = 0
        name = f"obs_{model}_{dataset}_benign_r{rounds}"
    else:
        cfg['num_attackers'] = attackers
        cfg['attack_method'] = attack
        cfg['attacker_observed_benign'] = k
        cfg['attacker_observation_mode'] = mode
        cfg['attacker_observation_seed'] = obs_seed
        cfg['attacker_observation_criterion'] = criterion
        cfg['attacker_observation_explore_rounds'] = explore_rounds
        cfg['attacker_observation_anchor_global'] = bool(anchor)
        cfg['attacker_observation_global_window'] = global_window
        if isinstance(k, int) and k == 0:
            name = f"obs_{model}_{dataset}_{attack.lower()}_k0of{n_benign}_secagg"
        else:
            mode_tag = mode + (f"-{criterion}" if mode == 'adaptive' else '')
            name = f"obs_{model}_{dataset}_{attack.lower()}_k{k_tag(k)}of{n_benign}_{mode_tag}"
            if anchor:
                name += "_anchor"
        if obs_seed is not None:
            name += f"_os{obs_seed}"
        name += f"_r{rounds}"
    if suffix:
        name += f"_{suffix}"
    cfg['experiment_name'] = name
    if extra:
        cfg.update(extra)
    return cfg


# The active experiment, built once from the ACTIVE block at the top of this file.
ACTIVE_CONFIG = make_config(**ACTIVE)


if __name__ == '__main__':
    # sanity: names match the sweep driver's scheme and the config is fully pinned
    print("ACTIVE_CONFIG:", ACTIVE_CONFIG['experiment_name'])
    a = make_config(2, mode='largest', anchor=True)
    assert a['experiment_name'] == 'obs_distilbert_ag_news_augmp_k2of7_largest_anchor_r30', a['experiment_name']
    assert a['dirichlet_alpha'] == 0.3 and a['model_name'] == 'distilbert-base-uncased'
    assert a['num_clients'] == 10 and a['num_attackers'] == 3 and a['lambda_update_mode'] == 'alm'
    assert make_config(0)['experiment_name'] == 'obs_distilbert_ag_news_augmp_k0of7_secagg_r30'
    assert make_config(7, rounds=50)['experiment_name'] == 'obs_distilbert_ag_news_augmp_k7of7_fixed_r50'
    assert make_config(None, attack='none', rounds=50)['experiment_name'] == 'obs_distilbert_ag_news_benign_r50'
    assert make_config(None, attack='none')['num_attackers'] == 0
    assert 'attacker_observed_benign' not in make_config(None, attack='none')
    assert make_config(0.29)['experiment_name'] == 'obs_distilbert_ag_news_augmp_k0p29of7_fixed_r30'
    print('observe_config.py self-test passed; sample run:', a['experiment_name'])
