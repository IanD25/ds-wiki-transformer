"""Baseline indicators B1-B12 and the multivariate additions (pre-registration §4.2).

Moment-based baselines reproduce the pandas/ewstools conventions exactly
(Amendment A3: own numba code, checked against ewstools/pandas in the tests).
"""

import math
import warnings

import numpy as np
from numba import njit
from scipy.stats._levy_stable import _fitstart_S1


@njit(cache=True)
def ac1(w):
    """B1: pandas Series.autocorr(lag=1): Pearson r of (w[:-1], w[1:])."""
    n = w.shape[0] - 1
    ma = 0.0
    mb = 0.0
    for i in range(n):
        ma += w[i]
        mb += w[i + 1]
    ma /= n
    mb /= n
    sab = 0.0
    saa = 0.0
    sbb = 0.0
    for i in range(n):
        da = w[i] - ma
        db = w[i + 1] - mb
        sab += da * db
        saa += da * da
        sbb += db * db
    if saa == 0.0 or sbb == 0.0:
        return np.nan
    return sab / math.sqrt(saa * sbb)


@njit(cache=True)
def _avg_rank(a):
    n = a.shape[0]
    order = np.argsort(a, kind="mergesort")
    r = np.empty(n)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and a[order[j + 1]] == a[order[i]]:
            j += 1
        rk = 0.5 * (i + j) + 1.0
        for q in range(i, j + 1):
            r[order[q]] = rk
        i = j + 1
    return r


@njit(cache=True)
def rank_ac1(w):
    """B2: Spearman correlation of (r_t, r_{t+1}); average ranks for ties."""
    ra = _avg_rank(w[:-1].copy())
    rb = _avg_rank(w[1:].copy())
    n = ra.shape[0]
    ma = ra.mean()
    mb = rb.mean()
    sab = 0.0
    saa = 0.0
    sbb = 0.0
    for i in range(n):
        sab += (ra[i] - ma) * (rb[i] - mb)
        saa += (ra[i] - ma) ** 2
        sbb += (rb[i] - mb) ** 2
    if saa == 0.0 or sbb == 0.0:
        return np.nan
    return sab / math.sqrt(saa * sbb)


@njit(cache=True)
def moments(w):
    """B3 variance (ddof=1), B5 skew (pandas G1), B6 excess kurtosis (pandas G2),
    B7 bimodality coefficient (SAS form, from G1 and G2)."""
    n = w.shape[0]
    mu = w.mean()
    m2 = 0.0
    m3 = 0.0
    m4 = 0.0
    for v in w:
        d = v - mu
        d2 = d * d
        m2 += d2
        m3 += d2 * d
        m4 += d2 * d2
    var = m2 / (n - 1)
    m2 /= n
    m3 /= n
    m4 /= n
    if m2 <= 0.0:
        return var, np.nan, np.nan, np.nan
    g1 = m3 / m2 ** 1.5
    G1 = math.sqrt(n * (n - 1.0)) / (n - 2.0) * g1
    g2 = m4 / (m2 * m2) - 3.0
    G2 = (n - 1.0) / ((n - 2.0) * (n - 3.0)) * ((n + 1.0) * g2 + 6.0)
    bc = (G1 * G1 + 1.0) / (G2 + 3.0 * (n - 1.0) ** 2 / ((n - 2.0) * (n - 3.0)))
    return var, G1, G2, bc


@njit(cache=True)
def robust_spread(w):
    """B4: MAD x 1.4826."""
    med = np.median(w)
    return 1.4826 * np.median(np.abs(w - med))


@njit(cache=True)
def _sd1(a):
    """sample SD (ddof = 1), as MATLAB std / the authors' code."""
    n = a.shape[0]
    mu = a.mean()
    ss = 0.0
    for v in a:
        ss += (v - mu) ** 2
    return math.sqrt(ss / (n - 1))


@njit(cache=True)
def rad(z, tau=1):
    """f_RAD (Harris, Gollo & Fulcher 2024 Eq. 11) with the authors' code
    semantics (Criticality RAD.m, MIT; = hctsa CR_RAD): lag-tau embedding,
    U/L split at the median of z[:-tau] (U = values >= median), ddof = 1.
    Amendment A6."""
    x = z[:-tau]
    y = z[tau:]
    med = np.median(x)
    lo = x[x < med]
    up = x[x >= med]
    if up.shape[0] < 2 or lo.shape[0] < 2:
        return np.nan
    su = _sd1(up)
    sl = _sd1(lo)
    if su == 0.0 or sl == 0.0:
        return np.nan
    return _sd1(y - x) * (1.0 / su - 1.0 / sl)


@njit(cache=True)
def crad(w):
    """B8: cRAD = f_RAD of |w - median(w)| (full-window median; Eq. 12)."""
    return rad(np.abs(w - np.median(w)), 1)


def stable_scale(w):
    """B9: alpha-stable scale gamma by McCulloch's (1986) quantile estimator,
    via scipy's implementation of it (levy_stable._fitstart, S1; Amendment A7)."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        _a, _b, _d, g = _fitstart_S1(np.asarray(w))
    return float(g)


# --------------------------------------------------------------------------
# B10-B12: Kramers-Moyal estimates in equal-count bins of x (dt = 1 sample)
# --------------------------------------------------------------------------
@njit(cache=True)
def km_indicators(w, nbins, ncentral, dt):
    """Returns (restoring rate = -slope of D1 on x over the central bins,
    D2 at the median, jump intensity lambda_J over the central bins)."""
    x = w[:-1]
    dx = w[1:] - w[:-1]
    n = x.shape[0]
    order = np.argsort(x, kind="mergesort")
    edges = np.empty(nbins + 1, dtype=np.int64)
    for b in range(nbins + 1):
        edges[b] = (b * n) // nbins
    xc = np.empty(nbins)
    d1 = np.empty(nbins)
    m2 = np.empty(nbins)
    m4 = np.empty(nbins)
    m6 = np.empty(nbins)
    for b in range(nbins):
        s0 = 0.0
        s1 = 0.0
        s2 = 0.0
        s4 = 0.0
        s6 = 0.0
        cnt = edges[b + 1] - edges[b]
        for q in range(edges[b], edges[b + 1]):
            i = order[q]
            s0 += x[i]
            s1 += dx[i]
            d2 = dx[i] * dx[i]
            s2 += d2
            s4 += d2 * d2
            s6 += d2 * d2 * d2
        xc[b] = s0 / cnt
        d1[b] = s1 / cnt / dt
        m2[b] = s2 / cnt / dt
        m4[b] = s4 / cnt / dt
        m6[b] = s6 / cnt / dt
    lo = (nbins - ncentral) // 2
    hi = lo + ncentral
    # least-squares slope of D1 on bin centres
    mx = 0.0
    my = 0.0
    for b in range(lo, hi):
        mx += xc[b]
        my += d1[b]
    mx /= ncentral
    my /= ncentral
    sxy = 0.0
    sxx = 0.0
    for b in range(lo, hi):
        sxy += (xc[b] - mx) * (d1[b] - my)
        sxx += (xc[b] - mx) ** 2
    restoring = -sxy / sxx if sxx > 0 else np.nan
    # D2 at the median: the two bins adjacent to the median (Amendment A8)
    c = nbins // 2
    diff2 = 0.5 * (m2[c - 1] + m2[c]) / 2.0
    # jump intensity (Anvari et al. 2016 moment method, as jumpdiff 0.4.2;
    # Amendment A8): per bin sigma_xi^2 = M6 / (5 M4), lambda dt = M4 / (3 sigma_xi^4)
    # with raw conditional moments M_n = <dx^n | x>; averaged over the central
    # bins (equal-count bins, so this is jumpdiff's density-weighted mean)
    lam = 0.0
    cnt = 0
    for b in range(lo, hi):
        if m4[b] > 0 and m6[b] > 0:
            s2j = m6[b] / (5.0 * m4[b])            # jump variance, raw-moment ratio
            lam += m4[b] / (3.0 * s2j * s2j)       # m4 is already M4 / dt
            cnt += 1
    lam = lam / cnt if cnt > 0 else np.nan
    return restoring, diff2, lam
