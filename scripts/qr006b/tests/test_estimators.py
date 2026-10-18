"""Estimator checks for QR-006b (pre-registration §7 item 2; Amendments A3, A5-A8).

Run with the experiment environment:
    cd scripts && ../.venv-qr006b/bin/python -m pytest qr006b/tests -q
"""

import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
pytest.importorskip("numba")
pytest.importorskip("scipy")

from qr006b.indicators import baselines as B  # noqa: E402
from qr006b.indicators import info as I  # noqa: E402
from qr006b import pipeline as P  # noqa: E402


def _ar1(n, phi, rng):
    x = np.empty(n)
    x[0] = rng.standard_normal() / math.sqrt(1 - phi * phi)
    e = rng.standard_normal(n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + e[t]
    return x


# ---------------------------------------------------------------- I1 ------
@pytest.mark.parametrize("rho", [0.3, 0.6, 0.9])
def test_ksg_bivariate_gaussian_identity(rho):
    """§7: mean KSG MI on n = 375 bivariate Gaussians within 5% of -1/2 log(1-rho^2)."""
    rng = np.random.default_rng(20261018)
    vals = []
    for _ in range(200):
        z = rng.standard_normal((375, 2))
        x = z[:, 0]
        y = rho * x + math.sqrt(1 - rho * rho) * z[:, 1]
        vals.append(I.ksg_mi(x, y, 4, I._PSI))
    true = -0.5 * math.log(1 - rho * rho)
    assert abs(np.mean(vals) - true) / true < 0.05


def test_lagged_mi_ar1_identity():
    """Lagged MI of a Gaussian AR(1) = -1/2 log(1 - phi^2)."""
    rng = np.random.default_rng(7)
    phi = 0.7
    vals = [I.lagged_mi(_ar1(400, phi, rng)) for _ in range(100)]
    true = -0.5 * math.log(1 - phi * phi)
    assert abs(np.mean(vals) - true) / true < 0.05


def test_transfer_entropy_independent_is_zero_and_coupled_positive():
    rng = np.random.default_rng(3)
    te0, te1 = [], []
    for _ in range(40):
        s = rng.standard_normal(400)
        t = rng.standard_normal(400)
        te0.append(I.transfer_entropy(s, t))
        t2 = np.empty(400)
        t2[0] = 0.0
        t2[1:] = 0.8 * s[:-1] + 0.6 * rng.standard_normal(399)
        te1.append(I.transfer_entropy(s, t2))
    assert abs(np.mean(te0)) < 0.02
    # Gaussian: TE = 1/2 log(var(t|t_past)/var(t|t_past, s_past)) = 1/2 log(1/0.36)
    assert abs(np.mean(te1) - 0.5 * math.log(1 / 0.36)) < 0.1


# ---------------------------------------------------------------- I3 ------
def test_permutation_entropy_matches_ordpy_and_is_invariant():
    ordpy = pytest.importorskip("ordpy")
    rng = np.random.default_rng(1)
    for d in (3, 4, 5):
        for _ in range(5):
            w = _ar1(345, 0.6, rng)
            w[::17] = w[3]                       # inject ties
            assert I.permutation_entropy(w, d, 1) == pytest.approx(
                ordpy.permutation_entropy(w, dx=d), abs=1e-12)
            # exact invariance under a strictly increasing map (C0g)
            assert I.permutation_entropy(np.exp(w), d, 1) == I.permutation_entropy(w, d, 1)


# ---------------------------------------------------------------- I4 ------
def test_sample_entropy_matches_entropyhub():
    EH = pytest.importorskip("EntropyHub")
    rng = np.random.default_rng(2)
    for _ in range(10):
        w = _ar1(345, 0.5, rng)
        ref = EH.SampEn(w, m=2)[0][2]
        assert I.sample_entropy(w, 2, 0.2) == pytest.approx(ref, abs=1e-12)


# ---------------------------------------------------------------- I5 ------
def test_fisher_index_ahmad_2016_worked_example():
    """Ahmad et al. 2016 Table 1 (8 points, 2 variables, dY = (0.5, 1)): FI = 2.136."""
    Y = np.array([[0.6, 1.5], [2, 1.5], [0.3, 1], [3.5, 4.8], [0.95, 2],
                  [3.1, 4], [2.4, 1.8], [2.7, 2.1]])
    assert I.fisher_index(Y, np.array([0.5, 1.0]), 100.0) == pytest.approx(2.1363, abs=1e-4)


def test_fisher_index_falls_as_sigma_rises():
    """Amendment A5 (b): fixed size of state, i.i.d. Gaussian input: FI falls
    monotonically with sigma (the direction of I = 1/sigma^2)."""
    rng = np.random.default_rng(4)
    z = rng.standard_normal((400, 1))
    sos = np.array([2.0])
    fis = [np.mean([I.fisher_index(s * rng.standard_normal((400, 1)), sos, 100.0)
                    for _ in range(20)]) for s in (0.5, 1.0, 2.0, 4.0)]
    assert all(a > b for a, b in zip(fis, fis[1:]))
    assert I.fisher_index(np.zeros((10, 1)), sos, 100.0) == pytest.approx(8.0)


# ---------------------------------------------------------------- I6 ------
def _rpde_reference(w, m, tau, eps):
    """Line-by-line transcription of the published close-returns pseudo-code
    (Little et al. 2007; hctsa EN_rpde normalisation), deliberately naive."""
    x = (w - w.mean()) / w.std(ddof=1)
    M = len(x) - (m - 1) * tau
    Y = [np.array([x[i + a * tau] for a in range(m)]) for i in range(M)]
    rets = [0] * M
    for i in range(M):
        j = i + 1
        left = False
        while j < M and not left:
            if np.sum((Y[i] - Y[j]) ** 2) > eps * eps:
                left = True
            j += 1
        back = False
        while j < M and not back:
            if np.sum((Y[i] - Y[j]) ** 2) <= eps * eps:
                rets[j - i] += 1
                back = True
            j += 1
    p = np.array(rets, float)
    p = p / p.sum()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum() / math.log(M))


def test_rpde_matches_transcription_and_periodic_limit():
    rng = np.random.default_rng(5)
    for k in range(10):
        w = _ar1(300, 0.3 + 0.06 * k, rng)
        for m in (2, 3):
            assert I.rpde(w, m, 1, 0.12) == pytest.approx(_rpde_reference(w, m, 1, 0.12), abs=1e-12)
    per = np.sin(2 * np.pi * np.arange(400) / 25.0)
    assert I.rpde(per, 2, 1, 0.12) < 0.1


# ---------------------------------------------------------------- B -------
def test_moments_and_ac1_match_pandas():
    pd = pytest.importorskip("pandas")
    rng = np.random.default_rng(6)
    w = _ar1(345, 0.8, rng) ** 3
    s = pd.Series(w)
    var, sk, ku, bc = B.moments(w)
    assert var == pytest.approx(s.var(), rel=1e-12)
    assert sk == pytest.approx(s.skew(), rel=1e-10)
    assert ku == pytest.approx(s.kurt(), rel=1e-10)
    assert B.ac1(w) == pytest.approx(s.autocorr(1), rel=1e-12)
    assert B.rank_ac1(w) == pytest.approx(
        pd.Series(w[:-1]).corr(pd.Series(w[1:]), method="spearman"), rel=1e-12)
    n = len(w)
    assert bc == pytest.approx((sk ** 2 + 1) / (ku + 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))))
    assert B.robust_spread(w) == pytest.approx(1.4826 * np.median(np.abs(w - np.median(w))))


def test_crad_hand_computed_example():
    """Amendment A6: x = [1,3,2,5,4,8,6]: RAD = -1.2903, cRAD = -1.6959."""
    x = np.array([1, 3, 2, 5, 4, 8, 6], float)
    assert B.rad(x, 1) == pytest.approx(-1.2903, abs=1e-4)
    assert B.crad(x) == pytest.approx(-1.6959, abs=1e-4)


@pytest.mark.slow
@pytest.mark.parametrize("alpha", [1.5, 1.8])
def test_mcculloch_gamma_vs_ml(alpha):
    """§7 / Amendment A7: median relative difference to the scipy ML fit <= 10%."""
    from scipy.stats import levy_stable
    rng = np.random.default_rng(int(alpha * 10))
    rel = []
    for _ in range(10):
        x = levy_stable.rvs(alpha, 0.0, scale=1.0, size=300, random_state=rng)
        g_mc = B.stable_scale(x)
        g_ml = levy_stable.fit(x)[3]
        rel.append(abs(g_mc - g_ml) / g_ml)
    assert np.median(rel) <= 0.10


def test_km_restoring_rate_and_jump_rate():
    """B10 recovers the OU restoring rate; B12 recovers the jump rate of a
    simulated jump-diffusion (jumpdiff's moment method)."""
    rng = np.random.default_rng(8)
    n = 200_000
    theta = 0.3
    x = np.zeros(n)
    e = rng.standard_normal(n)
    for t in range(1, n):
        x[t] = x[t - 1] - theta * x[t - 1] + e[t]
    rest, d2, lam = B.km_indicators(x, 20, 16, 1.0)
    assert rest == pytest.approx(theta, rel=0.05)
    assert d2 == pytest.approx(0.5, rel=0.05)
    # jump-diffusion: lambda = 0.05 per step, jump SD 3, diffusion SD 0.1
    lam_true = 0.05
    jumps = (rng.random(n) < lam_true) * rng.normal(0, 3.0, n)
    y = np.zeros(n)
    e2 = 0.1 * rng.standard_normal(n)
    for t in range(1, n):
        y[t] = y[t - 1] - 0.05 * y[t - 1] + e2[t] + jumps[t]
    lam_hat = B.km_indicators(y, 20, 16, 1.0)[2]
    assert lam_hat == pytest.approx(lam_true, rel=0.25)


def test_kendall_and_expanding_tau_match_scipy():
    from scipy.stats import kendalltau
    rng = np.random.default_rng(9)
    y = np.round(rng.standard_normal(200), 1)       # ties
    assert P.kendall_tau_b(y) == pytest.approx(kendalltau(np.arange(200), y)[0], abs=1e-12)
    et = P.expanding_tau(y, 10)
    for k in (10, 57, 199):
        assert et[k] == pytest.approx(kendalltau(np.arange(k + 1), y[: k + 1])[0], abs=1e-12)
    assert np.isnan(et[:10]).all()
