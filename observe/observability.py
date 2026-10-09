# observe/observability.py
# Opt-in "limited observability" experiment for the AugMP simulation.
#
# Motivation: AugMP learns the statistical structure of benign updates. In deployments such as
# Secure Aggregation an adversary may observe only a SUBSET of the benign updates. This module lets
# the server hand attackers only the benign updates they are allowed to observe (plus, optionally,
# a pseudo-update derived from the global broadcast), while the server itself still aggregates every
# update (ground truth untouched).
#
# Design constraints:
#   * Zero impact on the original pipeline: everything is a no-op unless the config key
#     `attacker_observed_benign` is set (default None). Attacker classes are not modified.
#   * Private RNGs only: enabling the policy never consumes the global torch/numpy RNG streams,
#     so a run that observes ALL benign clients is bit-identical to a run with the policy disabled.
#   * The attacker-side code already renormalises aggregation weights over the updates it holds,
#     so feature selection, graph construction, VGAE input, the estimated global reference and the
#     automatic d_T / similarity bounds all follow whatever rows the server hands over.
#
# Attacker-side information used by the strategies (all legitimately available to the attacker):
#   - the k observed benign updates of the round;
#   - the global model broadcast every round, hence w_g(t+1) - w_g(t) = server_lr * aggregated update
#     (used by the global anchor and by adaptive peer scoring);
#   - the data sizes / aggregation weights of the benign clients (`largest` mode, anchor weight).

from math import ceil
from typing import Dict, List, Optional, Sequence, Union

import numpy as np

Number = Union[int, float]


def _to_vec(x) -> np.ndarray:
    """torch tensor or array-like -> flat float32 numpy vector (no torch import needed)."""
    if hasattr(x, 'detach'):
        x = x.detach().float().cpu().numpy()
    return np.asarray(x, dtype=np.float32).reshape(-1)


class ObservationPolicy:
    """Decides which benign client updates the attackers may observe in a given round.

    Args:
        num_observed: int  -> number of benign clients observed (count);
                      float in (0, 1] -> fraction of benign clients observed (rounded, at least 1).
        mode: 'fixed'    -> the same random subset every round (compromised peers / tapped links).
              'random'   -> a fresh random subset each round (varying eavesdropping opportunities).
              'largest'  -> the k benign clients holding the most data (most aggregation weight).
              'adaptive' -> explore by rotating through the peers for `explore_rounds` rounds, score
                            every observed peer by its deviation from the broadcast aggregated update,
                            then lock onto the k best peers according to `criterion`.
        seed: seed of the private RNG used to draw the subset (fixed / random modes).
        criterion: adaptive mode only. 'deviant' = lock onto the most deviant peers (largest
                   ||Δ_i - Δ_g|| / ||Δ_g||, enlarges the attacker's automatic distance bound);
                   'representative' = lock onto the peers closest to the aggregated update.
        explore_rounds: adaptive mode only; default ceil(B / k) so every peer is seen once.
        anchor_global: if True the server also hands the attackers the previous round's broadcast
                       update as an extra pseudo benign row (client id -1) whose aggregation weight
                       is the data mass of the UNOBSERVED benign clients. This re-centres the
                       attacker's aggregate estimate and constraint statistics on the true global.
    """

    MODES = ('fixed', 'random', 'largest', 'adaptive')
    CRITERIA = ('deviant', 'representative')
    ANCHOR_ID = -1

    def __init__(self, num_observed: Number, mode: str = 'fixed', seed: int = 0,
                 criterion: str = 'deviant', explore_rounds: Optional[int] = None,
                 anchor_global: bool = False, global_window: int = 5):
        if mode not in self.MODES:
            raise ValueError(f"attacker_observation_mode must be one of {self.MODES}, got {mode!r}")
        if criterion not in self.CRITERIA:
            raise ValueError(f"attacker_observation_criterion must be one of {self.CRITERIA}, got {criterion!r}")
        if isinstance(num_observed, bool) or not isinstance(num_observed, (int, float, np.integer, np.floating)):
            raise TypeError(f"attacker_observed_benign must be int (count, >= 0) or float in (0,1] (fraction), got {num_observed!r}")
        if isinstance(num_observed, (float, np.floating)) and not (0.0 < float(num_observed) <= 1.0):
            raise ValueError(f"attacker_observed_benign as a float must lie in (0, 1], got {num_observed}")
        if isinstance(num_observed, (int, np.integer)) and int(num_observed) < 0:
            raise ValueError(f"attacker_observed_benign as an int must be >= 0 (0 = Secure Aggregation), got {num_observed}")
        if explore_rounds is not None and int(explore_rounds) < 1:
            raise ValueError("attacker_observation_explore_rounds must be >= 1 (or None)")
        if int(global_window) < 1:
            raise ValueError("attacker_observation_global_window must be >= 1")
        self.num_observed = num_observed
        self.mode = mode
        self.seed = int(seed)
        self.criterion = criterion
        self.explore_rounds = None if explore_rounds is None else int(explore_rounds)
        self.anchor_global = bool(anchor_global)
        self.global_window = int(global_window)
        # Secure Aggregation endpoint: k == 0 means the attacker observes NO individual benign update
        # and may only use the global model it is broadcast each round (handled server-side as a window
        # of recent global-broadcast deltas). The selection mode is irrelevant in this case.
        self.secagg = isinstance(num_observed, (int, np.integer)) and not isinstance(num_observed, bool) and int(num_observed) == 0
        self._fixed_ids: Optional[List[int]] = None
        self._rng = np.random.default_rng(self.seed)  # private generator, never the global one
        # adaptive-mode state
        self._scores: Dict[int, List[float]] = {}
        self._locked_ids: Optional[List[int]] = None
        self.locked_at_round: Optional[int] = None

    # ------------------------------------------------------------------ helpers
    def resolve_count(self, total: int) -> int:
        """Number of benign clients to observe given `total` benign clients."""
        if total <= 0:
            return 0
        if isinstance(self.num_observed, (float, np.floating)):
            k = int(round(float(self.num_observed) * total))
            k = max(1, k)
        else:
            k = int(self.num_observed)
        return max(0, min(k, total))

    def is_full(self, total: int) -> bool:
        return self.resolve_count(total) >= total

    def _rank(self, ids: List[int], k: int) -> List[int]:
        """Adaptive lock-in: top-k peers by mean deviation score (never-scored peers rank last)."""
        means = {cid: float(np.mean(v)) for cid, v in self._scores.items() if v}
        if self.criterion == 'deviant':
            missing = float('-inf')
            key = lambda cid: (-means.get(cid, missing), cid)
        else:
            missing = float('inf')
            key = lambda cid: (means.get(cid, missing), cid)
        chosen = set(sorted(ids, key=key)[:k])
        return [cid for cid in ids if cid in chosen]

    # ------------------------------------------------------------------ main API
    def select(self, benign_ids: Sequence[int], round_num: int,
               data_sizes: Optional[Dict[int, float]] = None) -> List[int]:
        """Return the observed benign client ids for this round, preserving the order of `benign_ids`.

        Deterministic given (round_num, policy state); the state only changes in observe_round().
        """
        ids = list(benign_ids)
        total = len(ids)
        if total == 0:
            return []
        k = self.resolve_count(total)
        if k == 0:
            return []  # Secure Aggregation: no benign update is observed
        if k >= total:
            return ids  # full observation: nothing drawn, nothing filtered

        if self.mode == 'fixed':
            if self._fixed_ids is None:
                pick = self._rng.choice(total, size=k, replace=False)
                self._fixed_ids = [ids[i] for i in sorted(int(p) for p in pick)]
            chosen = set(self._fixed_ids)
        elif self.mode == 'random':
            rng = np.random.default_rng([self.seed, int(round_num)])  # reproducible per round
            pick = rng.choice(total, size=k, replace=False)
            chosen = {ids[int(p)] for p in pick}
        elif self.mode == 'largest':
            sizes = data_sizes or {}
            ranked = sorted(ids, key=lambda cid: (-float(sizes.get(cid, 0.0)), cid))
            chosen = set(ranked[:k])
        else:  # adaptive
            if self._locked_ids is not None:
                chosen = set(self._locked_ids)
            else:
                explore = self.explore_rounds if self.explore_rounds is not None else ceil(total / k)
                if int(round_num) < explore:
                    # deterministic rotation: every peer is observed within ceil(total/k) rounds
                    chosen = {ids[(int(round_num) * k + j) % total] for j in range(k)}
                else:
                    self._locked_ids = self._rank(ids, k)
                    self.locked_at_round = int(round_num)
                    chosen = set(self._locked_ids)

        return [cid for cid in ids if cid in chosen]

    def observe_round(self, round_num: int, observed_ids: Sequence[int], observed_updates: Sequence,
                      global_delta) -> None:
        """Feedback the attacker obtains from the next broadcast: w_g(t+1) - w_g(t) = aggregated update.

        Adaptive mode scores every observed peer by ||Δ_i - Δ_g|| / ||Δ_g||. Other modes ignore it.
        """
        if self.mode != 'adaptive' or self._locked_ids is not None:
            return
        g = _to_vec(global_delta)
        gn = float(np.linalg.norm(g)) + 1e-12
        for cid, u in zip(observed_ids, observed_updates):
            if cid is None or int(cid) < 0:
                continue  # skip the anchor pseudo-row
            d = float(np.linalg.norm(_to_vec(u) - g)) / gn
            self._scores.setdefault(int(cid), []).append(d)

    @property
    def locked_ids(self) -> Optional[List[int]]:
        return None if self._locked_ids is None else list(self._locked_ids)

    def describe(self) -> str:
        if self.secagg:
            return (f"Secure Aggregation: attackers observe NO benign updates, only the global broadcast "
                    f"(window of {self.global_window} recent global-model deltas), seed={self.seed}")
        if isinstance(self.num_observed, (float, np.floating)):
            amount = f"{float(self.num_observed):.0%} of benign clients"
        else:
            amount = f"{int(self.num_observed)} benign client(s)"
        s = f"attackers observe {amount}, mode={self.mode}"
        if self.mode == 'adaptive':
            s += f" (criterion={self.criterion}, explore_rounds={self.explore_rounds or 'auto'})"
        if self.anchor_global:
            s += ", + global-broadcast anchor row"
        return s + f", seed={self.seed}"


def build_observation_policy(config: dict) -> Optional[ObservationPolicy]:
    """Create a policy from the experiment config, or None when the ablation is disabled."""
    value = config.get('attacker_observed_benign', None)
    if value is None:
        return None
    mode = config.get('attacker_observation_mode', 'fixed') or 'fixed'
    seed = config.get('attacker_observation_seed', None)
    if seed is None:
        seed = config.get('seed', 0)
    return ObservationPolicy(
        value, mode=mode, seed=seed,
        criterion=config.get('attacker_observation_criterion', 'deviant') or 'deviant',
        explore_rounds=config.get('attacker_observation_explore_rounds', None),
        anchor_global=bool(config.get('attacker_observation_anchor_global', False)),
        global_window=int(config.get('attacker_observation_global_window', 5) or 5),
    )


def to_float(x) -> Optional[float]:
    """Best-effort conversion of a scalar / 0-d tensor to float for JSON logging."""
    if x is None:
        return None
    try:
        if hasattr(x, 'detach'):
            x = x.detach()
        if hasattr(x, 'item'):
            return float(x.item())
        return float(x)
    except Exception:
        return None


if __name__ == '__main__':
    # Lightweight self-test (no torch needed).
    ids = [0, 1, 2, 3, 4, 5, 6]
    p = ObservationPolicy(2, 'fixed', seed=42069)
    a, b = p.select(ids, 0), p.select(ids, 7)
    assert a == b and len(a) == 2 and a == sorted(a), (a, b)
    assert ObservationPolicy(7, 'fixed').select(ids, 0) == ids
    assert ObservationPolicy(1.0, 'fixed').select(ids, 0) == ids
    assert len(ObservationPolicy(0.29, 'fixed').select(ids, 0)) == 2
    r = ObservationPolicy(3, 'random', seed=1)
    assert r.select(ids, 3) == r.select(ids, 3) and len(r.select(ids, 3)) == 3
    sizes = {0: 10, 1: 500, 2: 20, 3: 400, 4: 30, 5: 1, 6: 2}
    assert ObservationPolicy(2, 'largest').select(ids, 0, sizes) == [1, 3]
    # adaptive: rotation covers every peer, then locks onto the most deviant two
    ad = ObservationPolicy(2, 'adaptive', criterion='deviant')
    seen = set()
    rng = np.random.default_rng(0)
    g = rng.normal(size=50)
    dev = {cid: 0.1 * (cid + 1) for cid in ids}  # peer 6 most deviant, peer 5 next
    for rnd in range(4):  # ceil(7/2) = 4 exploration rounds
        obs = ad.select(ids, rnd)
        assert len(obs) == 2 and ad.locked_ids is None
        seen.update(obs)
        ups = [g + dev[cid] * rng.normal(size=50) for cid in obs]
        ad.observe_round(rnd, obs + [-1], ups + [g], g)  # anchor row must be ignored
    assert seen == set(ids), seen
    locked = ad.select(ids, 4)
    assert locked == [5, 6] and ad.locked_ids == [5, 6] and ad.locked_at_round == 4, locked
    assert ad.select(ids, 9) == [5, 6]
    rep = ObservationPolicy(2, 'adaptive', criterion='representative')
    for rnd in range(4):
        obs = rep.select(ids, rnd)
        rep.observe_round(rnd, obs, [g + dev[cid] * rng.normal(size=50) for cid in obs], g)
    assert rep.select(ids, 4) == [0, 1], rep.select(ids, 4)
    cfg = {'seed': 3, 'attacker_observed_benign': 2, 'attacker_observation_mode': 'adaptive',
           'attacker_observation_anchor_global': True, 'attacker_observation_explore_rounds': 5}
    bp = build_observation_policy(cfg)
    assert bp.seed == 3 and bp.anchor_global and bp.explore_rounds == 5 and bp.mode == 'adaptive'
    assert build_observation_policy({'seed': 3}) is None
    assert to_float(None) is None and to_float(1.5) == 1.5
    # Secure Aggregation endpoint: k = 0 observes nothing
    sa = ObservationPolicy(0, 'fixed', global_window=5)
    assert sa.secagg and sa.resolve_count(7) == 0 and sa.select(ids, 0) == [] and not sa.is_full(7)
    sap = build_observation_policy({'seed': 1, 'attacker_observed_benign': 0, 'attacker_observation_global_window': 4})
    assert sap.secagg and sap.global_window == 4 and sap.select(ids, 0) == []
    assert not ObservationPolicy(2, 'fixed').secagg
    try:
        ObservationPolicy(-1, 'fixed'); assert False
    except ValueError:
        pass
    print("observability.py self-test passed:", p.describe(), "->", a, "| adaptive locked", locked)
    print("  SecAgg:", sap.describe())
