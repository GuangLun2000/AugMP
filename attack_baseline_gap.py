# attack_baseline_gap.py
# GAP (Gradient Assembly Poisoning) Attack — Model Poisoning baseline
#
# Paper: "Low Rank Comes with Low Security: Gradient Assembly Poisoning Attacks
#         against Distributed LoRA-based LLM Systems" (referred to here as GAP).
#
# GAP is a two-stage poisoning attack: the attacker first builds an offline "target"
# update by fine-tuning toward a degraded model, then each communication round moves its
# submitted update toward that target while keeping the update's Euclidean distance to the
# global update within a plausibility bound. This module reproduces that mechanism for our
# system. Three implementation choices follow from system differences with the original
# paper (and nothing else about the attack is altered):
#
#   (1) Aggregation protocol. The original paper studies "split aggregation", where each
#       agent uploads the two low-rank LoRA matrices A and B separately and the server
#       averages A and B independently before multiplying. Our system uses "coupled
#       aggregation": each client assembles the FULL weight update locally (ΔW = B·A) and
#       the server averages the full updates. GAP therefore operates directly in the
#       full-update space, i.e. the SAME space / SAME interface as the ALIE, Gaussian and
#       Sign-Flipping baselines.
#
#   (2) Attack goal. The original paper demonstrates a targeted attack (specific prompts
#       answered wrong, generation quality preserved, measured by BLEU / perplexity). Here
#       the task is text classification, so GAP's offline target is a degradation direction
#       and the metric is classification accuracy.
#
#   (3) Attacker data. GAP's offline target is built from the attacker's own ordinary local
#       data only — no crafted adversarial dataset and no label flipping.
#
# Mechanism as implemented:
#   Phase 1 (offline, computed ONCE): gradient ASCENT on the attacker's own local data
#     — maximise the ordinary task loss (reverse the normal training gradient) for a few
#     steps — to obtain a "degradation direction" FULL weight update = the target update.
#     Own data only; no adversarial dataset; no label flipping. The number of ascent epochs
#     is a hyper-parameter, defaulting to the same order of magnitude as local training
#     (local_epochs).
#
#   Phase 2 (online, every round): interpolate between the attacker's current honest local
#     update g_own and the fixed target update, then PROJECT the candidate so that its
#     Euclidean distance to the global update does not exceed a bound. GAP constrains ONLY
#     the Euclidean distance — there is NO cosine-similarity constraint.
#
#   Distance bound. The original GAP infers the bound from the SERVER BROADCAST. In our
#     threat model the attacker instead observes a subset of benign LOCAL updates plus the
#     global model, so the bound is taken from the OBSERVED BENIGN UPDATES: their mean is
#     the attacker's estimate of the global update Δ_g, and a statistic (default: the max)
#     of the benign-update-to-Δ_g distances is the upper bound. This is the documented
#     replacement for the broadcast-based bound, and it matches the information our
#     framework already hands every attacker (the same benign-distance convention used
#     elsewhere in this codebase).
#
# Isolated from the AugMP (GRMP) implementation; shares only the Client/BenignClient base
# and the same server interface as the other baselines.

import torch
import torch.nn as nn
import torch.optim as optim
from typing import List, Optional

from client import BenignClient


class GAPAttackerClient(BenignClient):
    """
    GAP (Gradient Assembly Poisoning) — adapted baseline for coupled aggregation.

    Two-stage attack:
      * Phase 1 (offline, once): gradient ascent on the attacker's own data -> fixed
        "degradation direction" full-update (the target update).
      * Phase 2 (online, per round): interpolate current honest update g_own with the
        target, then clip by a Euclidean-distance ball whose radius is estimated from the
        observed benign updates. No cosine constraint.

    Inherits BenignClient so the inherited local_train() produces the honest local update
    g_own (the "current local update" interpolated against the target each round).
    """

    def __init__(self, client_id: int, model, data_manager,
                 data_indices, lr, local_epochs, alpha,
                 data_loader,                      # required: own data, for g_own AND the offline ascent target
                 gap_target_epochs: Optional[int] = None,   # ascent epochs for Phase 1 (None -> local_epochs)
                 gap_interp_lambda: float = 1.0,            # interpolation weight toward the target in Phase 2
                 gap_dist_bound_stat: str = 'max',          # statistic of benign distances used as the bound
                 attack_start_round: Optional[int] = None,
                 claimed_data_size: float = 1.0,
                 grad_clip_norm: float = 1.0):
        """
        Args:
            client_id, model, data_manager, data_indices, lr, local_epochs, alpha:
                standard client arguments (data_manager kept for API parity with main.py).
            data_loader: DataLoader over the attacker's own assigned data. Used both for the
                inherited honest local training (g_own) and for the offline ascent target.
            gap_target_epochs: number of gradient-ASCENT epochs for the offline target
                (Phase 1). None -> local_epochs (same order of magnitude as local training).
            gap_interp_lambda: λ in m = (1-λ)·g_own + λ·target. λ=1.0 => approach the target
                fully each round (then distance-clip); λ=0.0 => honest. Default 1.0.
            gap_dist_bound_stat: which statistic of the observed benign-to-Δ_g distances to
                use as the distance ceiling: 'max' (default, matches framework benign_max),
                'mean', 'median', or 'p90'.
            attack_start_round: round to start attacking (None = immediately). Before it the
                attacker submits its honest update.
            claimed_data_size: data size claimed for weighted FedAvg aggregation.
            grad_clip_norm: gradient clipping norm (shared by g_own training and the ascent).
        """
        super().__init__(
            client_id=client_id,
            model=model,
            data_loader=data_loader,
            lr=lr,
            local_epochs=local_epochs,
            alpha=alpha,
            data_indices=data_indices,
            grad_clip_norm=grad_clip_norm
        )
        self.is_attacker = True
        self.attack_method = "GAP"

        # GAP hyper-parameters
        self.gap_target_epochs = int(gap_target_epochs) if gap_target_epochs is not None else int(local_epochs)
        self.gap_interp_lambda = float(gap_interp_lambda)
        if gap_dist_bound_stat not in ('max', 'mean', 'median', 'p90'):
            raise ValueError(f"gap_dist_bound_stat must be one of max/mean/median/p90, got {gap_dist_bound_stat!r}")
        self.gap_dist_bound_stat = gap_dist_bound_stat
        self.attack_start_round = attack_start_round
        self.claimed_data_size = claimed_data_size

        # Phase-1 offline target (built once, then cached and held FIXED for all rounds)
        self._target_update: Optional[torch.Tensor] = None

        # Observed benign updates (Phase 2 distance bound) and broadcast global params
        self.benign_updates: List[torch.Tensor] = []
        self.benign_update_client_ids: List[int] = []
        self.global_params: Optional[torch.Tensor] = None

        # Dimension bookkeeping (LoRA flat-param count in LoRA mode, else all params)
        self._flat_numel = int(self.model.get_flat_params().numel())
        self.use_lora = hasattr(self.model, 'use_lora') and self.model.use_lora

    # ------------------------------------------------------------------ round hooks
    def prepare_for_round(self, round_num: int):
        """Prepare for a new round."""
        self.set_round(round_num)

    # local_train: inherited from BenignClient -> honest local update g_own on own data.

    def receive_benign_updates(self, updates: List[torch.Tensor],
                               client_ids: Optional[List[int]] = None):
        """
        Receive the benign LOCAL updates the attacker is allowed to observe. These define
        the Phase-2 distance bound (their mean estimates Δ_g; a statistic of their distances
        to that mean is the ceiling). Stored as detached CPU copies.
        """
        self.benign_updates = [u.detach().clone().cpu() for u in updates]
        if client_ids is not None:
            self.benign_update_client_ids = list(client_ids)
        else:
            self.benign_update_client_ids = list(range(len(updates)))

    def receive_attacker_updates(self, updates: List[torch.Tensor],
                                 client_ids: List[int],
                                 data_sizes: Optional[dict] = None):
        """Interface compatibility; GAP does not coordinate across attackers."""
        pass

    def set_global_model_params(self, global_params: torch.Tensor):
        """
        Store the broadcast global parameters (CPU copy). Used as the BASE model for the
        offline ascent target so the target is a degradation delta w.r.t. the global model.
        """
        self.global_params = global_params.detach().clone().cpu()

    def set_constraint_params(self, dist_bound: Optional[float] = None,
                              sim_bound_low: Optional[float] = None,
                              sim_bound_up: Optional[float] = None,
                              total_data_size: Optional[float] = None,
                              benign_data_sizes: Optional[dict] = None):
        """
        Interface compatibility. GAP derives its distance bound itself, from the observed
        benign updates (see camouflage_update). Server-provided bounds are intentionally
        ignored, and no cosine-similarity bound is used (GAP constrains distance only).
        """
        pass

    def set_lagrangian_params(self, **kwargs):
        """Interface compatibility; GAP does not use Lagrangian optimisation."""
        pass

    # ------------------------------------------------------------------ Phase 1 (offline)
    def _compute_target_update(self) -> torch.Tensor:
        """
        Build the offline degradation target (computed ONCE, then cached).

        Gradient ASCENT on the attacker's own data starting from the broadcast global model:
        maximise the ordinary cross-entropy loss (equivalently, reverse the normal training
        gradient). No proximal term, no adversarial data, no label flipping. Returns the
        flattened CPU update (ascent_params - base_params), in the same space as g_own.
        """
        device = self.device

        # Base the ascent on the broadcast global params. (By the time camouflage runs, the
        # inherited local_train has already overwritten the model with the honest-trained
        # weights, so we must explicitly reset to the global model first.)
        if self.global_params is not None:
            base_params = self.global_params.clone()
        else:
            base_params = self.model.get_flat_params().clone().cpu()

        self.model.to(device)
        self._model_on_gpu = True
        self.model.set_flat_params(base_params.to(device))

        trainable = [p for p in self.model.parameters() if p.requires_grad]
        optimizer = optim.Adam(trainable, lr=self.lr)
        self.model.train()

        initial_params = self.model.get_flat_params().clone().cpu()  # == base_params

        for _ in range(self.gap_target_epochs):
            for batch in self.data_loader:
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['labels'].to(device)

                logits = self.model(input_ids, attention_mask)
                ce_loss = nn.CrossEntropyLoss()(logits, labels)

                # ASCENT: maximise the task loss == minimise its negative.
                loss = -ce_loss

                if not torch.isfinite(loss).item():
                    # Skip non-finite batches (decoder models can be unstable), as in local_train.
                    continue

                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=self.grad_clip_norm)
                optimizer.step()

        target = self.get_model_update(initial_params)  # CPU: ascent_params - base_params

        # Restore the model to the broadcast base and free GPU memory (the next round's
        # broadcast will overwrite it anyway, but keep side effects out of this round).
        self.model.set_flat_params(initial_params.to(device))
        self.model.cpu()
        self._model_on_gpu = False
        del optimizer
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        return target.detach().cpu().float()

    # ------------------------------------------------------------------ Phase 2 (online)
    def _distance_bound(self, ref: torch.Tensor) -> Optional[float]:
        """Statistic of the observed benign updates' Euclidean distances to ref (= Δ_g estimate)."""
        if not self.benign_updates:
            return None
        dists = torch.stack([torch.norm(u.cpu().float() - ref) for u in self.benign_updates])
        if self.gap_dist_bound_stat == 'max':
            return float(dists.max())
        if self.gap_dist_bound_stat == 'mean':
            return float(dists.mean())
        if self.gap_dist_bound_stat == 'median':
            return float(dists.median())
        # 'p90'
        return float(torch.quantile(dists, 0.90))

    def camouflage_update(self, poisoned_update: torch.Tensor) -> torch.Tensor:
        """
        Produce the GAP malicious update.

        poisoned_update is the attacker's honest local update g_own (from the inherited
        local_train). Steps:
          1. (first active round) build & cache the offline degradation target.
          2. interpolate: m = (1-λ)·g_own + λ·target.
          3. project m into the Euclidean ball of radius `bound` around Δ_g (estimated as
             the mean of observed benign updates). Distance only — no cosine constraint.
        """
        # Hold fire until the configured start round (submit the honest update meanwhile).
        if self.attack_start_round is not None and self.current_round < self.attack_start_round:
            return poisoned_update

        g_own = poisoned_update.detach().cpu().float()

        # Validate dimensions (critical for LoRA mode).
        if int(g_own.numel()) != self._flat_numel:
            raise RuntimeError(
                f"[GAP Attacker {self.client_id}] g_own dimension mismatch: "
                f"{int(g_own.numel())} vs expected {self._flat_numel} (LoRA mode: {self.use_lora})."
            )

        # --- Phase 1: build the offline target once, then reuse the cached target direction.
        if self._target_update is None:
            self._target_update = self._compute_target_update()
            print(f"    [GAP Attacker {self.client_id}] Offline degradation target built "
                  f"(gradient ascent, {self.gap_target_epochs} epoch(s)): "
                  f"||target||={float(torch.norm(self._target_update)):.4f}, param_dim={self._flat_numel}")
        target = self._target_update
        if int(target.numel()) != self._flat_numel:
            raise RuntimeError(
                f"[GAP Attacker {self.client_id}] target dimension mismatch: "
                f"{int(target.numel())} vs expected {self._flat_numel}."
            )

        # --- Phase 2a: interpolate current honest update with the fixed degradation target.
        lam = self.gap_interp_lambda
        candidate = (1.0 - lam) * g_own + lam * target

        # --- Phase 2b: Euclidean-distance projection (distance only; GAP uses no cosine constraint).
        # Bound comes from the OBSERVED BENIGN updates (replaces GAP's broadcast-based bound;
        # see module header). ref = mean(observed benign) is the attacker's estimate of Δ_g.
        if self.benign_updates:
            ref = torch.stack([u.cpu().float() for u in self.benign_updates]).mean(dim=0)
            bound = self._distance_bound(ref)
            cand_dist = float(torch.norm(candidate - ref))
            projected = False
            if bound is not None and cand_dist > bound and cand_dist > 0.0:
                candidate = ref + (bound / cand_dist) * (candidate - ref)
                projected = True
            final_dist = float(torch.norm(candidate - ref))
            print(f"    [GAP Attacker {self.client_id}] λ={lam:.2f}, ||g_own||={float(torch.norm(g_own)):.4f}, "
                  f"||target||={float(torch.norm(target)):.4f}, bound[{self.gap_dist_bound_stat}]={bound:.4f}, "
                  f"dist(cand,Δ_g): {cand_dist:.4f}->{final_dist:.4f} ({'projected' if projected else 'within bound'}), "
                  f"||m||={float(torch.norm(candidate)):.4f}")
        else:
            # No observable benign updates -> no bound; submit the unprojected interpolation.
            print(f"    [GAP Attacker {self.client_id}] No benign updates observed; "
                  f"submitting unprojected interpolation (λ={lam:.2f}), ||m||={float(torch.norm(candidate)):.4f}")

        malicious = candidate.detach().cpu().float()
        if int(malicious.numel()) != self._flat_numel:
            raise RuntimeError(
                f"[GAP Attacker {self.client_id}] malicious update dimension mismatch: "
                f"{int(malicious.numel())} vs expected {self._flat_numel}."
            )
        return malicious
