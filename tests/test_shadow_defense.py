# tests/test_shadow_defense.py -- CPU-only checks of shadow_defense.py against a naive numpy reference.
# Run from the repo root:  python -m pytest tests/test_shadow_defense.py -q
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
import pytest
import torch

from shadow_defense import (compute_shadow_defense_stats, compute_shadow_defense_summary,
                            format_shadow_defense_round, format_shadow_defense_summary,
                            resolve_shadow_defense_params)


# ----------------------------------------------------------------------------------------------
# naive reference (float64 numpy, no chunking)
# ----------------------------------------------------------------------------------------------
def reference(U, f, beta, m):
    U = np.asarray(U, dtype=np.float64)
    n, d = U.shape
    params, _ = resolve_shadow_defense_params(n, f, beta, m)
    k, m, beta = params['k'], params['m'], params['beta']

    norms = np.linalg.norm(U, axis=1)
    D2 = np.zeros((n, n))
    cos = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D2[i, j] = np.sum((U[i] - U[j]) ** 2)
            cos[i, j] = np.dot(U[i], U[j]) / (norms[i] * norms[j])
    krum = np.array([np.sort(np.delete(D2[i], i))[:k].sum() for i in range(n)])
    order = sorted(range(n), key=lambda i: (krum[i], i))
    sel = order[0]
    mk_sel = order[:m]
    rejected = np.array([i not in mk_sel for i in range(n)])

    # per-coordinate ranks (no ties in the random test data)
    rank = np.zeros((n, d), dtype=np.int64)
    for c in range(d):
        rank[np.argsort(U[:, c], kind='stable'), c] = np.arange(n)
    lo = (rank < beta).sum(axis=1)
    hi = (rank >= n - beta).sum(axis=1)
    if n % 2 == 1:
        med_cnt = (rank == n // 2).sum(axis=1).astype(np.float64)
    else:
        med_cnt = 0.5 * ((rank == n // 2 - 1).sum(axis=1) + (rank == n // 2).sum(axis=1))
    med = np.median(U, axis=0)
    dmed = np.sqrt(((U - med[None, :]) ** 2).sum(axis=1))
    return dict(params=params, norms=norms, D2=D2, cos=cos, krum=krum, sel=sel, mk_sel=mk_sel,
                rejected=rejected, lo=lo, hi=hi, med_cnt=med_cnt, dmed=dmed)


def check_against_reference(U, cids, f, beta, m, chunk_size):
    n, d = U.shape
    st = compute_shadow_defense_stats([torch.from_numpy(U[i]) for i in range(n)], cids,
                                      f=f, beta=beta, m=m, chunk_size=chunk_size, device=torch.device('cpu'))
    ref = reference(U, f, beta, m)
    assert st['params'] == dict(ref['params'], d=d)
    assert st['client_ids'] == list(cids)
    np.testing.assert_allclose(st['norms'], ref['norms'], rtol=1e-5)
    np.testing.assert_allclose(np.array(st['pairwise_sq_dist']), ref['D2'], rtol=1e-4, atol=1e-3)
    np.testing.assert_allclose(np.array(st['pairwise_cos']), ref['cos'], rtol=1e-5, atol=1e-6)
    np.testing.assert_allclose(st['krum_score'], ref['krum'], rtol=1e-4)
    assert st['krum_selected'] == cids[ref['sel']]
    assert st['mkrum_selected'] == [cids[i] for i in ref['mk_sel']]
    assert st['mkrum_rejected'] == [cids[i] for i in range(n) if ref['rejected'][i]]
    assert st['mkrum_rejected_flag'] == [bool(v) for v in ref['rejected']]
    assert st['tm_trim_low_count'] == ref['lo'].tolist()
    assert st['tm_trim_high_count'] == ref['hi'].tolist()
    assert st['tm_trim_count'] == (ref['lo'] + ref['hi']).tolist()
    np.testing.assert_allclose(st['tm_trim_frac'], (ref['lo'] + ref['hi']) / d, rtol=0, atol=1e-12)
    np.testing.assert_allclose(st['tm_trim_low_frac'], ref['lo'] / d, rtol=0, atol=1e-12)
    np.testing.assert_allclose(st['tm_trim_high_frac'], ref['hi'] / d, rtol=0, atol=1e-12)
    np.testing.assert_allclose(st['median_provider_count'], ref['med_cnt'], rtol=0, atol=1e-12)
    np.testing.assert_allclose(st['median_provider_frac'], ref['med_cnt'] / d, rtol=0, atol=1e-12)
    np.testing.assert_allclose(st['dist_to_median'], ref['dmed'], rtol=1e-5)
    # sanity identities
    assert sum(st['tm_trim_count']) == 2 * st['params']['beta'] * d
    assert abs(sum(st['median_provider_frac']) - 1.0) < 1e-9
    assert all(a + b == c for a, b, c in zip(st['tm_trim_low_count'], st['tm_trim_high_count'], st['tm_trim_count']))
    # everything must survive json.dump
    json.dumps(st)
    return st


def make_updates(n, d, seed):
    rng = np.random.default_rng(seed)
    U = rng.normal(size=(n, d)).astype(np.float32)
    U *= (0.5 + rng.random((n, 1))).astype(np.float32)     # different scales per client
    return U


# ----------------------------------------------------------------------------------------------
def test_n7_odd_chunk_not_dividing_d():
    n, d = 7, 1000
    U = make_updates(n, d, seed=0)
    st = check_against_reference(U, list(range(n)), f=2, beta=None, m=None, chunk_size=333)
    assert st['params'] == {'n': 7, 'd': 1000, 'f': 2, 'k': 3, 'm': 5, 'beta': 2}
    assert len(st['mkrum_rejected']) == 2
    # chunking must not change anything (float accumulation order only)
    st_full = compute_shadow_defense_stats([torch.from_numpy(U[i]) for i in range(n)], list(range(n)),
                                           f=2, beta=None, m=None, chunk_size=d)
    np.testing.assert_allclose(st_full['krum_score'], st['krum_score'], rtol=1e-6)
    assert st_full['tm_trim_count'] == st['tm_trim_count']
    assert st_full['median_provider_count'] == st['median_provider_count']
    np.testing.assert_allclose(st_full['dist_to_median'], st['dist_to_median'], rtol=1e-6)


def test_n6_even_median():
    n, d = 6, 1000
    U = make_updates(n, d, seed=1)
    cids = [10, 11, 12, 13, 14, 15]
    st = check_against_reference(U, cids, f=1, beta=None, m=None, chunk_size=256)
    assert st['params'] == {'n': 6, 'd': 1000, 'f': 1, 'k': 3, 'm': 5, 'beta': 1}
    # even n: every coordinate splits its median between two clients (0.5 each)
    assert all(abs(2 * c - round(2 * c)) < 1e-12 for c in st['median_provider_count'])
    assert sum(st['median_provider_count']) == d


def test_explicit_beta_and_m():
    n, d = 7, 500
    U = make_updates(n, d, seed=2)
    st = check_against_reference(U, list(range(n)), f=2, beta=1, m=3, chunk_size=128)
    assert st['params']['beta'] == 1 and st['params']['m'] == 3
    assert len(st['mkrum_selected']) == 3 and len(st['mkrum_rejected']) == 4


def test_planted_outlier():
    n, d = 7, 1000
    rng = np.random.default_rng(3)
    U = rng.normal(size=(n, d)).astype(np.float32)
    outlier = 4
    # one client = 10x the others: every coordinate has magnitude in [10, 20] (benign |values| stay < 5)
    U[outlier] = (10.0 * (1.0 + rng.random(d)) * rng.choice([-1.0, 1.0], size=d)).astype(np.float32)
    cids = list(range(n))
    st = check_against_reference(U, cids, f=1, beta=None, m=None, chunk_size=333)
    i = outlier
    assert st['krum_selected'] != cids[i]
    assert st['krum_score'][i] == max(st['krum_score'])
    assert st['mkrum_rejected_flag'][i] is True and st['mkrum_rejected'] == [cids[i]]
    assert st['tm_trim_frac'][i] > 0.99                      # trimmed on ~all coordinates
    assert st['median_provider_frac'][i] < 0.01              # provides ~0 medians
    assert st['dist_to_median'][i] == max(st['dist_to_median'])
    assert st['norms'][i] == max(st['norms'])
    # the (A)/(B) tags are display-only: the same stats come out whatever the labels are
    lines = format_shadow_defense_round(st, {cids[i]: True})
    assert lines[1] != f"    [shadow] Krum selected: C{cids[i]} (A)"
    assert any(l.startswith("    [shadow] C4 (A): norm=") and "mkrum=REJECT" in l for l in lines)
    assert all(not line.lstrip().startswith("Client ") for line in lines)


def test_param_clamping_and_warnings_once():
    n, d = 3, 50
    U = make_updates(n, d, seed=4)
    ups = [torch.from_numpy(U[i]) for i in range(n)]
    params, warns = resolve_shadow_defense_params(n, f=2, beta=None, m=None)
    assert params == {'n': 3, 'f': 2, 'k': 1, 'm': 1, 'beta': 1}        # k clamped, beta clamped
    assert len(warns) == 2
    assert resolve_shadow_defense_params(7, f=2, beta=None, m=9)[0]['m'] == 7
    assert resolve_shadow_defense_params(7, f=2, beta=None, m=0)[0]['m'] == 1
    warned = set()
    st1 = check_against_reference(U, [0, 1, 2], f=2, beta=None, m=None, chunk_size=7)
    compute_shadow_defense_stats(ups, [0, 1, 2], f=2, beta=None, m=None, chunk_size=7, warned=warned)
    assert len(warned) == 2
    compute_shadow_defense_stats(ups, [0, 1, 2], f=2, beta=None, m=None, chunk_size=7, warned=warned)
    assert len(warned) == 2                                             # still printed only once
    assert sum(st1['tm_trim_count']) == 2 * 1 * d


def test_pairwise_cos_reuse_and_dtype_device():
    n, d = 5, 300
    U = make_updates(n, d, seed=5)
    ups = [torch.from_numpy(U[i]).to(torch.float64) for i in range(n)]  # non-float32 input is fine
    st = compute_shadow_defense_stats(ups, list(range(n)), f=1, beta=None, m=None, chunk_size=100)
    pre = np.full((n, n), 0.123)
    st2 = compute_shadow_defense_stats(ups, list(range(n)), f=1, beta=None, m=None, chunk_size=100, pairwise_cos=pre)
    assert np.allclose(np.array(st2['pairwise_cos']), 0.123)          # precomputed matrix is reused verbatim
    assert st2['krum_score'] == st['krum_score']                       # and nothing else changes
    assert all(torch.equal(u, torch.from_numpy(U[i]).to(torch.float64)) for i, u in enumerate(ups))  # inputs untouched


def test_summary_rates():
    n, d = 7, 200
    cids = list(range(n))
    attackers = [5, 6]
    logs = []
    for r in range(4):
        U = make_updates(n, d, seed=100 + r)
        U[5] *= 10.0                                                   # obvious outlier every round
        st = compute_shadow_defense_stats([torch.from_numpy(U[i]) for i in range(n)], cids,
                                          f=2, beta=None, m=None, chunk_size=64)
        logs.append({'round': r + 1, 'aggregation': {'shadow_defense': st}})
    s = compute_shadow_defense_summary(logs, attackers)
    assert s['params'] == {'n': 7, 'f': 2, 'k': 3, 'm': 5, 'beta': 2, 'rounds': 4, 'num_attackers': 2, 'num_benign': 5}
    # recompute the definitions by hand
    att_rej = sum(st['mkrum_rejected_flag'][i] for st in (l['aggregation']['shadow_defense'] for l in logs) for i in attackers)
    ben_rej = sum(st['mkrum_rejected_flag'][i] for st in (l['aggregation']['shadow_defense'] for l in logs) for i in range(5))
    assert s['multi_krum']['DR'] == pytest.approx(att_rej / (2 * 4))
    assert s['multi_krum']['FPR'] == pytest.approx(ben_rej / (5 * 4))
    assert s['multi_krum']['ER'] == pytest.approx(1 - s['multi_krum']['DR'])
    tm_att = np.mean([l['aggregation']['shadow_defense']['tm_trim_frac'][i] for l in logs for i in attackers])
    tm_ben = np.mean([l['aggregation']['shadow_defense']['tm_trim_frac'][i] for l in logs for i in range(5)])
    assert s['trimmed_mean']['DR'] == pytest.approx(tm_att) and s['trimmed_mean']['FPR'] == pytest.approx(tm_ben)
    assert s['trimmed_mean']['chance'] == pytest.approx(4 / 7) and s['multi_krum']['chance'] == pytest.approx(2 / 7)
    assert s['krum']['chance'] == pytest.approx(2 / 7) and s['median']['chance'] == pytest.approx(1 / 7)
    krum_att = sum(l['aggregation']['shadow_defense']['krum_selected'] in attackers for l in logs)
    assert s['krum']['attacker_selection_rate'] == pytest.approx(krum_att / 4)
    infl = np.mean([sum(l['aggregation']['shadow_defense']['median_provider_frac'][i] for i in attackers) for l in logs])
    assert s['median']['attacker_total_influence'] == pytest.approx(infl)
    assert s['median']['attacker_provider_rate'] == pytest.approx(infl / 2)
    assert s['multi_krum']['DR'] >= 0.5                                 # the 10x outlier is always rejected
    json.dumps(s)
    assert len(format_shadow_defense_summary(s)) == 6
    # benign-only run: attacker quantities are n/a, benign ones still defined
    s0 = compute_shadow_defense_summary(logs, [])
    assert s0['multi_krum']['DR'] is None and s0['krum']['attacker_selection_rate'] is None
    assert s0['median']['attacker_total_influence'] is None and s0['multi_krum']['FPR'] is not None
    assert "n/a" in format_shadow_defense_summary(s0)[2]
    assert compute_shadow_defense_summary([{'round': 1, 'aggregation': {}}], attackers) is None
