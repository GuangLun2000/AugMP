# shadow_defense.py
# Shadow (compute-only) statistics for Byzantine-robust aggregation rules.
#
# Every round the server aggregates the client updates with plain FedAvg. When
# `shadow_defense_enabled` is on, this module additionally evaluates what Krum,
# Multi-Krum, Trimmed Mean and Coordinate-wise Median *would* do with the very same
# updates -- which client each rule would select / reject / trim -- WITHOUT applying
# any of them. The aggregation, the attackers and every random stream are untouched:
# this file is pure torch, uses no RNG, and never looks at attacker/benign labels.
#
# Memory: the rules are evaluated over coordinate chunks `U[:, a:b]`, so the peak
# footprint is O(n * chunk_size) regardless of the model size d.

from typing import Dict, List, Optional, Sequence, Tuple

import math
import torch


def resolve_shadow_defense_params(n: int, f: Optional[int], beta: Optional[int] = None,
                                  m: Optional[int] = None) -> Tuple[Dict[str, int], List[str]]:
    """
    Resolve / clamp the effective rule parameters for `n` submitted updates.

    Returns ({'n', 'f', 'k', 'm', 'beta'}, warnings). Each clamp produces one warning string;
    the caller decides how (and how often) to print them.
      * Krum          : k = n - f - 2 must be >= 1, otherwise k = 1
      * Multi-Krum    : 1 <= m <= n, default m = n - f
      * Trimmed Mean  : n > 2 * beta, otherwise beta = (n - 1) // 2; default beta = f
    """
    n = int(n)
    warnings: List[str] = []
    f = 0 if f is None else int(f)
    if f < 0:
        f = 0

    k = n - f - 2
    if k < 1:
        warnings.append(f"[shadow] Krum needs n - f - 2 >= 1 (n={n}, f={f}); using k=1")
        k = 1
    k = max(0, min(k, n - 1))  # cannot average over more than the n-1 other clients

    m = (n - f) if m is None else int(m)
    if m < 1 or m > n:
        m_new = min(max(m, 1), n)
        warnings.append(f"[shadow] Multi-Krum needs 1 <= m <= n (n={n}, m={m}); using m={m_new}")
        m = m_new

    beta = f if beta is None else int(beta)
    if beta < 0:
        beta = 0
    if n <= 2 * beta:
        beta_new = (n - 1) // 2
        warnings.append(f"[shadow] Trimmed Mean needs n > 2*beta (n={n}, beta={beta}); using beta={beta_new}")
        beta = beta_new

    return {'n': n, 'f': f, 'k': k, 'm': m, 'beta': beta}, warnings


@torch.no_grad()
def compute_shadow_defense_stats(updates: List[torch.Tensor], client_ids: List[int],
                                 f: int, beta: int, m: int, chunk_size: int,
                                 device: Optional[torch.device] = None,
                                 pairwise_cos=None,
                                 warned: Optional[set] = None) -> Dict:
    """
    Evaluate Krum / Multi-Krum / Trimmed Mean / Coordinate-wise Median on `updates`
    (one flat tensor per client, in `client_ids` order) without applying any of them.

    Args:
        updates:      list of n flat update tensors (any device / float dtype, same length d)
        client_ids:   client id of each update (used only to label the outputs)
        f:            number of Byzantine clients assumed by Krum / Multi-Krum
        beta:         Trimmed Mean trim count per side (None -> f)
        m:            Multi-Krum selection size (None -> n - f)
        chunk_size:   coordinates per chunk for the coordinate-wise rules
        device:       device for the computation (default: device of updates[0])
        pairwise_cos: optional precomputed (n, n) cosine matrix to reuse (numpy or tensor);
                      when None it is derived from the Gram matrix
        warned:       optional set used to print each parameter-clamp warning only once
                      (pass the same set every round); None -> print every time

    Returns a dict of JSON-serialisable Python types (lists / floats / ints / bools):
        params                : {'n', 'd', 'f', 'k', 'm', 'beta'} (effective, after clamping)
        client_ids            : the client id order used for every per-client list below
        norms                 : ||U_i||_2
        pairwise_sq_dist      : (n, n) ||U_i - U_j||^2
        pairwise_cos          : (n, n) cosine similarity
        krum_score            : sum of the k smallest squared distances to other clients
        krum_selected         : client id with the smallest Krum score
        mkrum_selected        : m client ids with the smallest Krum scores (score order)
        mkrum_rejected        : the remaining client ids (client_ids order)
        mkrum_rejected_flag   : per-client bool
        tm_trim_count / tm_trim_low_count / tm_trim_high_count : per-client coordinate counts
        tm_trim_frac  / tm_trim_low_frac  / tm_trim_high_frac  : the same divided by d
        median_provider_count : per-client number of coordinates whose median is this client's
                                value (even n: 0.5 for each of the two middle order statistics)
        median_provider_frac  : the same divided by d (sums to 1 over clients)
        dist_to_median        : ||U_i - median(U)||_2

    Per-coordinate ranks are `chunk.argsort(dim=0).argsort(dim=0)`; ties are broken
    arbitrarily (torch sort order), which does not affect the count identities
    sum_i tm_trim_count[i] == 2 * beta * d and sum_i median_provider_frac[i] == 1.
    """
    n = len(updates)
    if n == 0:
        raise ValueError("compute_shadow_defense_stats needs at least one update")
    if len(client_ids) != n:
        raise ValueError("client_ids must have one entry per update")
    d = int(updates[0].numel())
    for u in updates:
        if int(u.numel()) != d:
            raise ValueError("all updates must have the same number of coordinates")
    if device is None:
        device = updates[0].device
    chunk_size = int(chunk_size) if chunk_size else d
    chunk_size = max(1, min(chunk_size, d))

    params, warnings = resolve_shadow_defense_params(n, f, beta, m)
    for w in warnings:
        if warned is None:
            print(f"  ⚠️ {w}")
        elif w not in warned:
            warned.add(w)
            print(f"  ⚠️ {w}")
    k, m, beta = params['k'], params['m'], params['beta']

    # ---- accumulators (tiny, float64 / int64, on `device`) ----
    gram = torch.zeros(n, n, dtype=torch.float64, device=device)
    trim_low_count = torch.zeros(n, dtype=torch.int64, device=device)
    trim_high_count = torch.zeros(n, dtype=torch.int64, device=device)
    med_count_a = torch.zeros(n, dtype=torch.int64, device=device)   # rank == n//2      (odd: the median)
    med_count_b = torch.zeros(n, dtype=torch.int64, device=device)   # rank == n//2 - 1  (even n only)
    dist_to_median_sq = torch.zeros(n, dtype=torch.float64, device=device)
    odd = (n % 2 == 1)

    # ---- single pass over coordinate chunks ----
    for a in range(0, d, chunk_size):
        b = min(a + chunk_size, d)
        chunk = torch.stack([u.detach().reshape(-1)[a:b] for u in updates]).to(device=device, dtype=torch.float32)  # (n, c)

        # Gram matrix (float32 product, float64 accumulation)
        gram += (chunk @ chunk.T).to(torch.float64)

        # Per-coordinate order statistics. `sort(dim=0).indices` is exactly `argsort(dim=0)`,
        # so rank == chunk.argsort(dim=0).argsort(dim=0) and the sorted values give the medians.
        sorted_vals, order = torch.sort(chunk, dim=0)
        rank = torch.argsort(order, dim=0)
        del order

        # Trimmed Mean: the beta smallest and beta largest values of every coordinate are dropped
        if beta > 0:
            trim_low_count += (rank < beta).sum(dim=1)
            trim_high_count += (rank >= n - beta).sum(dim=1)

        # Coordinate-wise Median: which client supplies the median value of each coordinate
        med_count_a += (rank == n // 2).sum(dim=1)
        if odd:
            med = sorted_vals[n // 2]                                           # == kthvalue(n//2 + 1)
        else:
            med_count_b += (rank == n // 2 - 1).sum(dim=1)
            med = 0.5 * (sorted_vals[n // 2 - 1] + sorted_vals[n // 2])         # mean of the two middle values
        dist_to_median_sq += ((chunk - med.unsqueeze(0)) ** 2).sum(dim=1).to(torch.float64)

        del chunk, sorted_vals, rank, med

    # ---- derived (n, n) quantities ----
    diag = gram.diagonal()
    norms = diag.clamp_min(0).sqrt()
    sq_dist = (diag.unsqueeze(1) + diag.unsqueeze(0) - 2.0 * gram).clamp_min(0)
    sq_dist.fill_diagonal_(0.0)
    if pairwise_cos is not None:
        cos = torch.as_tensor(pairwise_cos, dtype=torch.float64).reshape(n, n).cpu()
    else:
        denom = norms.unsqueeze(1) * norms.unsqueeze(0)
        cos = torch.where(denom > 0, gram / denom.clamp_min(1e-300), torch.zeros_like(gram)).cpu()

    # ---- Krum / Multi-Krum ----
    if n >= 2 and k >= 1:
        offdiag = sq_dist.clone()
        offdiag.fill_diagonal_(float('inf'))
        krum_score = offdiag.topk(k, dim=1, largest=False).values.sum(dim=1).cpu()
        del offdiag
    else:
        krum_score = torch.zeros(n, dtype=torch.float64)
    scores = [float(s) for s in krum_score.tolist()]
    ranking = sorted(range(n), key=lambda i: (scores[i], i))               # deterministic tie-break
    krum_selected_idx = ranking[0]
    mkrum_selected_idx = ranking[:m]
    mkrum_rejected_flag = [True] * n
    for i in mkrum_selected_idx:
        mkrum_rejected_flag[i] = False

    # ---- Trimmed Mean / Median bookkeeping ----
    trim_low = [int(v) for v in trim_low_count.tolist()]
    trim_high = [int(v) for v in trim_high_count.tolist()]
    trim_total = [lo + hi for lo, hi in zip(trim_low, trim_high)]
    if odd:
        med_provider = [float(v) for v in med_count_a.tolist()]
    else:
        med_provider = [0.5 * (float(va) + float(vb)) for va, vb in zip(med_count_a.tolist(), med_count_b.tolist())]
    dist_to_median = [math.sqrt(max(v, 0.0)) for v in dist_to_median_sq.tolist()]

    cids = [int(c) for c in client_ids]
    stats = {
        'params': {'n': n, 'd': d, 'f': params['f'], 'k': k, 'm': m, 'beta': beta},
        'client_ids': cids,
        'norms': [float(v) for v in norms.tolist()],
        'pairwise_sq_dist': [[float(v) for v in row] for row in sq_dist.cpu().tolist()],
        'pairwise_cos': [[float(v) for v in row] for row in cos.tolist()],
        'krum_score': scores,
        'krum_selected': cids[krum_selected_idx],
        'mkrum_selected': [cids[i] for i in mkrum_selected_idx],
        'mkrum_rejected': [cids[i] for i in range(n) if mkrum_rejected_flag[i]],
        'mkrum_rejected_flag': [bool(v) for v in mkrum_rejected_flag],
        'tm_trim_count': trim_total,
        'tm_trim_low_count': trim_low,
        'tm_trim_high_count': trim_high,
        'tm_trim_frac': [v / d for v in trim_total],
        'tm_trim_low_frac': [v / d for v in trim_low],
        'tm_trim_high_frac': [v / d for v in trim_high],
        'median_provider_count': med_provider,
        'median_provider_frac': [v / d for v in med_provider],
        'dist_to_median': dist_to_median,
    }
    del gram, diag, norms, sq_dist, cos, krum_score, trim_low_count, trim_high_count, med_count_a, med_count_b, dist_to_median_sq
    return stats


def format_shadow_defense_round(stats: Dict, is_attacker: Dict[int, bool]) -> List[str]:
    """
    Per-round console lines for one `compute_shadow_defense_stats` result. `is_attacker`
    maps client id -> bool and is used for the (A)/(B) tags ONLY (display).
    The lines intentionally never match `^\\s*Client (\\d+) \\((Benign|Attacker)\\): `,
    which the log parser uses for the cosine / Euclidean per-client values.
    """
    p = stats['params']
    tag = lambda cid: f"C{cid} ({'A' if is_attacker.get(cid, False) else 'B'})"
    lines = [f"  🛡️ Shadow defenses (computed only, NOT applied; "
             f"n={p['n']}, f={p['f']}, k={p['k']}, m={p['m']}, beta={p['beta']})",
             f"    [shadow] Krum selected: {tag(stats['krum_selected'])}"]
    rejected = stats['mkrum_rejected']
    lines.append("    [shadow] Multi-Krum rejected: " + (", ".join(tag(c) for c in rejected) if rejected else "none"))
    for i, cid in enumerate(stats['client_ids']):
        lines.append(
            f"    [shadow] {tag(cid)}: norm={stats['norms'][i]:.6f} krum={stats['krum_score'][i]:.6f} "
            f"mkrum={'REJECT' if stats['mkrum_rejected_flag'][i] else 'KEEP'} "
            f"tm_trim={stats['tm_trim_frac'][i]:.4f} (lo {stats['tm_trim_low_frac'][i]:.4f} / hi {stats['tm_trim_high_frac'][i]:.4f}) "
            f"med_prov={stats['median_provider_frac'][i]:.4f} d_med={stats['dist_to_median'][i]:.6f}")
    return lines


def compute_shadow_defense_summary(server_log_data: Sequence[Dict], attacker_ids: Sequence[int]) -> Optional[Dict]:
    """
    Aggregate the per-round shadow statistics stored under
    `round_log['aggregation']['shadow_defense']` into run-level rates.

    Definitions (R = rounds with shadow stats, A / B = attacker / benign submissions per round):
      Krum          attacker_selection_rate = #rounds whose Krum-selected update is malicious / R
      Multi-Krum    DR = #attacker submissions rejected / (A*R), FPR = #benign rejected / (B*R), ER = 1 - DR
      Trimmed Mean  DR = mean tm_trim_frac over attacker submissions, FPR = mean over benign, ER = 1 - DR
      Median        attacker_provider_rate = mean median_provider_frac over attacker submissions,
                    attacker_total_influence = mean over rounds of the attackers' summed provider fraction,
                    benign_provider_rate = mean over benign submissions
    Attacker-side quantities are None when there is no attacker. Returns None when no round
    carries shadow statistics.
    """
    per_round = [log['aggregation']['shadow_defense'] for log in server_log_data
                 if isinstance(log.get('aggregation'), dict) and log['aggregation'].get('shadow_defense')]
    if not per_round:
        return None
    attacker_set = {int(c) for c in attacker_ids}
    p = per_round[-1]['params']
    R = len(per_round)

    krum_att_rounds = 0
    mk_att_rej = mk_ben_rej = 0
    n_att_sub = n_ben_sub = 0
    tm_att = tm_ben = 0.0
    med_att = med_ben = 0.0
    med_att_total = 0.0
    for st in per_round:
        cids = st['client_ids']
        if int(st['krum_selected']) in attacker_set:
            krum_att_rounds += 1
        round_att_med = 0.0
        for i, cid in enumerate(cids):
            is_att = int(cid) in attacker_set
            rej = bool(st['mkrum_rejected_flag'][i])
            if is_att:
                n_att_sub += 1
                mk_att_rej += int(rej)
                tm_att += float(st['tm_trim_frac'][i])
                med_att += float(st['median_provider_frac'][i])
                round_att_med += float(st['median_provider_frac'][i])
            else:
                n_ben_sub += 1
                mk_ben_rej += int(rej)
                tm_ben += float(st['tm_trim_frac'][i])
                med_ben += float(st['median_provider_frac'][i])
        med_att_total += round_att_med

    n = int(p['n'])
    A = len([c for c in per_round[-1]['client_ids'] if int(c) in attacker_set])
    B = n - A
    div = lambda num, den: (num / den) if den > 0 else None

    mk_dr = div(mk_att_rej, n_att_sub)
    tm_dr = div(tm_att, n_att_sub)
    return {
        'params': {'n': n, 'f': int(p['f']), 'k': int(p['k']), 'm': int(p['m']), 'beta': int(p['beta']),
                   'rounds': R, 'num_attackers': A, 'num_benign': B},
        'krum': {'attacker_selection_rate': div(krum_att_rounds, R) if A > 0 else None,
                 'attacker_selected_rounds': krum_att_rounds,
                 'chance': div(A, n)},
        'multi_krum': {'DR': mk_dr, 'FPR': div(mk_ben_rej, n_ben_sub),
                       'ER': (1.0 - mk_dr) if mk_dr is not None else None,
                       'attacker_rejections': mk_att_rej, 'benign_rejections': mk_ben_rej,
                       'chance': div(n - int(p['m']), n)},
        'trimmed_mean': {'DR': tm_dr, 'FPR': div(tm_ben, n_ben_sub),
                         'ER': (1.0 - tm_dr) if tm_dr is not None else None,
                         'chance': div(2 * int(p['beta']), n)},
        'median': {'attacker_provider_rate': div(med_att, n_att_sub),
                   'attacker_total_influence': div(med_att_total, R) if A > 0 else None,
                   'benign_provider_rate': div(med_ben, n_ben_sub),
                   'chance': div(1, n)},
    }


def format_shadow_defense_summary(summary: Dict) -> List[str]:
    """Console lines for `compute_shadow_defense_summary`."""
    fmt = lambda v: "n/a" if v is None else f"{v:.4f}"
    p = summary['params']
    kr, mk, tm, md = summary['krum'], summary['multi_krum'], summary['trimmed_mean'], summary['median']
    return [
        "🛡️  SHADOW DEFENSE SUMMARY (computed only, NOT applied)",
        f"  Parameters: n={p['n']}, f={p['f']}, k={p['k']}, m={p['m']}, beta={p['beta']}, rounds={p['rounds']}",
        f"  Krum        : attacker selection rate = {fmt(kr['attacker_selection_rate'])}   "
        f"(chance = A/n = {fmt(kr['chance'])})   [rounds where the selected update is malicious]",
        f"  Multi-Krum  : DR = {fmt(mk['DR'])}  FPR = {fmt(mk['FPR'])}  ER = {fmt(mk['ER'])}   "
        f"(chance DR = FPR = (n-m)/n = {fmt(mk['chance'])})",
        f"  Trimmed Mean: DR = {fmt(tm['DR'])}  FPR = {fmt(tm['FPR'])}  ER = {fmt(tm['ER'])}   "
        f"(chance = 2*beta/n = {fmt(tm['chance'])})   [DR/FPR = mean trim fraction over attacker/benign submissions]",
        f"  Median      : attacker provider rate = {fmt(md['attacker_provider_rate'])}  "
        f"attacker total influence = {fmt(md['attacker_total_influence'])}  "
        f"benign provider rate = {fmt(md['benign_provider_rate'])}   "
        f"(chance per client = 1/n = {fmt(md['chance'])})   [no rejection step: DR/FPR n/a]",
    ]
