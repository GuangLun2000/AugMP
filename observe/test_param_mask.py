# observe/test_param_mask.py -- torch-path checks for parameter-level partial observation.
# Run from the repo root:  python observe/test_param_mask.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import torch
from observe.observability import ObservationPolicy, build_observation_policy


def main():
    torch.manual_seed(0)
    dim, n = 10_000, 5
    originals = [torch.randn(dim) * (0.1 + 0.05 * i) for i in range(n)]
    snapshot = [u.clone() for u in originals]

    # p = 0.2, zero fill, mask redrawn per round
    pol = ObservationPolicy(1.0, 'fixed', seed=42069, param_fraction=0.2)
    seen0 = pol.mask_updates(originals, round_num=0)
    assert all(torch.equal(a, b) for a, b in zip(originals, snapshot)), "server tensors were modified"
    assert all(o is not s for o, s in zip(originals, seen0)), "attackers must get copies"
    nz = [(u != 0).sum().item() for u in seen0]
    assert nz == [2000] * n, nz                                              # exactly round(p*dim) observed coords
    masks = [(u != 0) for u in seen0]
    assert all(torch.equal(masks[0], m) for m in masks), "mask must be shared by all rows of a round"
    obs = masks[0]
    for o, s in zip(seen0, originals):
        assert torch.equal(o[obs], s[obs]), "observed coordinates must be passed through unchanged"
    seen1 = pol.mask_updates(originals, round_num=1)
    assert not torch.equal(seen1[0] != 0, obs), "mask must be redrawn in the next round"
    assert torch.equal(pol.mask_updates(originals, 0)[0], seen0[0]), "same round -> same mask (reproducible)"
    # energy bookkeeping: a benign update has ~(1-p) of its energy hidden; a vector living on the
    # observed coordinates has 0 hidden energy
    pol.mask_updates(originals, 0)
    f_benign = pol.unobserved_energy_fraction(originals[0])
    assert abs(f_benign - 0.8) < 0.03, f_benign
    assert pol.unobserved_energy_fraction(seen0[0]) == 0.0
    assert ObservationPolicy(1.0, 'fixed', param_fraction=0.2).unobserved_energy_fraction(originals[0]) is None

    # fixed mask: identical across rounds
    pf = ObservationPolicy(1.0, 'fixed', seed=1, param_fraction=0.5, param_mask_fixed=True)
    a, b = pf.mask_updates(originals, 0)[0], pf.mask_updates(originals, 7)[0]
    assert torch.equal(a != 0, b != 0) and (a != 0).sum().item() == 5000

    # gaussian fill: hidden coords are non-zero, RMS-matched to the observed part, independent per row
    pg = ObservationPolicy(1.0, 'fixed', seed=3, param_fraction=0.2, param_fill='gaussian')
    g = pg.mask_updates(originals, 0)
    m = pg.param_mask(dim, 0)
    hidden = torch.from_numpy(~m)
    for row, src in zip(g, originals):
        assert torch.equal(row[~hidden], src[~hidden])
        rms_obs = src[~hidden].pow(2).mean().sqrt().item()
        rms_hid = row[hidden].pow(2).mean().sqrt().item()
        assert abs(rms_hid / rms_obs - 1.0) < 0.05, (rms_obs, rms_hid)
        assert abs(row.norm().item() / src.norm().item() - 1.0) < 0.05
    assert not torch.equal(g[0][hidden], g[1][hidden]), "noise must differ between rows"

    # p = 1.0 or off -> the very same tensor objects (bit-identical full-observation path)
    for off in (ObservationPolicy(5, 'fixed'), ObservationPolicy(5, 'fixed', param_fraction=1.0)):
        out = off.mask_updates(originals, 0)
        assert all(o is s for o, s in zip(out, originals))

    # config plumbing
    cfg = {'seed': 42069, 'attacker_observed_benign': 5, 'attacker_observed_param_fraction': 0.2,
           'attacker_observed_param_fill': 'zero', 'attacker_observed_param_mask_fixed': False}
    bp = build_observation_policy(cfg)
    assert bp.param_partial and bp.select([0, 1, 2, 3, 4], 0) == [0, 1, 2, 3, 4]
    # 2-D updates keep their shape
    two_d = [torch.randn(4, 25), torch.randn(4, 25)]
    out = bp.mask_updates(two_d, 0)
    assert out[0].shape == (4, 25) and (out[0] != 0).sum().item() == 20
    print("test_param_mask.py passed")


if __name__ == '__main__':
    main()
