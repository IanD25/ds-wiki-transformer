"""Information-theoretic indicators I1-I6 (pre-registration §4.1).

All window-level functions take a 1-D float64 residual window (or, for
transfer entropy, two windows) and return a float. They are numba-compiled;
brute-force neighbour search is exact and, for windows of a few hundred
points, faster than a k-d tree (Amendment A3).
"""

import math

import numpy as np
from numba import njit

# --------------------------------------------------------------------------
# Digamma on integers: psi(n) = -gamma + sum_{j<n} 1/j
# --------------------------------------------------------------------------
_EULER = 0.57721566490153286061
_PSI_MAX = 20001
_PSI = np.empty(_PSI_MAX)
_PSI[0] = np.nan
_PSI[1] = -_EULER
for _n in range(2, _PSI_MAX):
    _PSI[_n] = _PSI[_n - 1] + 1.0 / (_n - 1)

# Fixed tie-breaking jitter (§4.1, I1): standard normals from seed 0, scaled
# per window by 1e-10 x window SD.
_JITTER = np.random.default_rng(0).standard_normal(20000)
JITTER_SCALE = 1e-10


@njit(cache=True)
def _kth_dist(d, k):
    """k-th smallest value of d (k >= 1), by partial insertion."""
    best = np.full(k, np.inf)
    for v in d:
        if v < best[k - 1]:
            j = k - 1
            while j > 0 and best[j - 1] > v:
                best[j] = best[j - 1]
                j -= 1
            best[j] = v
    return best[k - 1]


@njit(cache=True)
def ksg_mi(x, y, k, psi):
    """Kraskov-Stoegbauer-Grassberger estimator, algorithm 1, max-norm, nats."""
    n = x.shape[0]
    d = np.empty(n - 1)
    acc = 0.0
    for i in range(n):
        m = 0
        for j in range(n):
            if j != i:
                d[m] = max(abs(x[i] - x[j]), abs(y[i] - y[j]))
                m += 1
        eps = _kth_dist(d, k)
        nx = 0
        ny = 0
        for j in range(n):
            if j != i:
                if abs(x[i] - x[j]) < eps:
                    nx += 1
                if abs(y[i] - y[j]) < eps:
                    ny += 1
        acc += psi[nx + 1] + psi[ny + 1]
    return psi[k] + psi[n] - acc / n


@njit(cache=True)
def ksg_cmi(x, y, z, k, psi):
    """KSG conditional MI I(X;Y|Z) (Frenzel-Pompe form), max-norm, nats."""
    n = x.shape[0]
    d = np.empty(n - 1)
    acc = 0.0
    for i in range(n):
        m = 0
        for j in range(n):
            if j != i:
                d[m] = max(abs(x[i] - x[j]), abs(y[i] - y[j]), abs(z[i] - z[j]))
                m += 1
        eps = _kth_dist(d, k)
        nxz = 0
        nyz = 0
        nz = 0
        for j in range(n):
            if j != i:
                dz = abs(z[i] - z[j])
                if dz < eps:
                    nz += 1
                    if abs(x[i] - x[j]) < eps:
                        nxz += 1
                    if abs(y[i] - y[j]) < eps:
                        nyz += 1
        acc += psi[nxz + 1] + psi[nyz + 1] - psi[nz + 1]
    return psi[k] - acc / n


def _jitter(w):
    sd = w.std()
    return w + JITTER_SCALE * sd * _JITTER[: w.shape[0]]


def lagged_mi(w, k=4, lag=1):
    """I1: KSG MI between r_t and r_{t+lag}."""
    w = _jitter(np.ascontiguousarray(w, dtype=np.float64))
    return ksg_mi(w[:-lag].copy(), w[lag:].copy(), k, _PSI)


def transfer_entropy(src, tgt, k=4, lag=1):
    """I2: TE src -> tgt = I(tgt_{t+1}; src_t | tgt_t), histories 1, lag 1."""
    s = _jitter(np.ascontiguousarray(src, dtype=np.float64))
    t = _jitter(np.ascontiguousarray(tgt, dtype=np.float64))
    return ksg_cmi(t[lag:].copy(), s[:-lag].copy(), t[:-lag].copy(), k, _PSI)


# --------------------------------------------------------------------------
# I3: permutation entropy (Bandt-Pompe; ties by order of occurrence, as ordpy)
# --------------------------------------------------------------------------
@njit(cache=True)
def permutation_entropy(w, d, delay):
    n = w.shape[0] - (d - 1) * delay
    nfact = 1
    for i in range(2, d + 1):
        nfact *= i
    counts = np.zeros(nfact, dtype=np.int64)
    idx = np.empty(d, dtype=np.int64)
    vals = np.empty(d)
    for t in range(n):
        for a in range(d):
            vals[a] = w[t + a * delay]
            idx[a] = a
        # stable insertion argsort
        for a in range(1, d):
            b = a
            while b > 0 and vals[idx[b - 1]] > vals[idx[b]]:
                tmp = idx[b - 1]
                idx[b - 1] = idx[b]
                idx[b] = tmp
                b -= 1
        # Lehmer code of the permutation idx
        code = 0
        for a in range(d):
            smaller = 0
            for b in range(a + 1, d):
                if idx[b] < idx[a]:
                    smaller += 1
            code = code * (d - a) + smaller
        counts[code] += 1
    h = 0.0
    for c in counts:
        if c > 0:
            p = c / n
            h -= p * math.log(p)
    return h / math.log(nfact)


# --------------------------------------------------------------------------
# I4: sample entropy, matching EntropyHub.SampEn (r = 0.2 * population SD,
# Chebyshev distance, <= r).
# --------------------------------------------------------------------------
@njit(cache=True)
def sample_entropy(w, m, rfrac):
    n = w.shape[0]
    mu = 0.0
    for v in w:
        mu += v
    mu /= n
    ss = 0.0
    for v in w:
        ss += (v - mu) ** 2
    r = rfrac * math.sqrt(ss / n)
    a = 0
    b = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            length = 0
            while length <= m and j + length < n and abs(w[i + length] - w[j + length]) <= r:
                length += 1
            if length >= m and j <= n - m - 1:
                b += 1
            if length >= m + 1:
                a += 1
    if b == 0:
        return np.nan          # EntropyHub: -log(0/0) = nan
    if a == 0:
        return np.inf          # EntropyHub: -log(0/B) = inf
    return -math.log(a / b)


# --------------------------------------------------------------------------
# I5: Fisher Information index, binning method (Karunanithi et al. 2008;
# discrete form and state order as Ahmad et al. 2016 eq. 2.4 and the
# developers' code, csunlab/fisher-information; Amendment A5)
# --------------------------------------------------------------------------
@njit(cache=True)
def fisher_index(W, sos, tl):
    """W: (n, d) window; sos: (d,) size of states (|difference| <= sos joins);
    tl: tightening level in percent. States are created in time order from the
    earliest unbinned point, members tested against the centre only, and kept
    in creation order; FI = 4 sum (q_i - q_{i+1})^2 with q zero-padded."""
    n, d = W.shape
    need = d * tl / 100.0
    binned = np.zeros(n, dtype=np.bool_)
    counts = np.zeros(n, dtype=np.int64)
    ns = 0
    for j in range(n):
        if binned[j]:
            continue
        binned[j] = True
        c = 1
        for i in range(j + 1, n):
            if binned[i]:
                continue
            match = 0
            for v in range(d):
                if abs(W[j, v] - W[i, v]) <= sos[v]:
                    match += 1
            if match >= need:
                binned[i] = True
                c += 1
        counts[ns] = c
        ns += 1
    fi = 0.0
    qprev = 0.0
    for s in range(ns):
        q = math.sqrt(counts[s] / n)
        fi += (qprev - q) ** 2
        qprev = q
    fi += qprev ** 2
    return 4.0 * fi


# --------------------------------------------------------------------------
# I6: recurrence period density entropy (Little et al. 2007 close returns;
# normalisation and defaults as hctsa EN_rpde: z-scored window, H / ln M).
# Re-implemented from the published algorithm (Amendment A5).
# --------------------------------------------------------------------------
@njit(cache=True)
def rpde(w, m, tau, eps):
    n = w.shape[0]
    mu = w.mean()
    ss = 0.0
    for v in w:
        ss += (v - mu) ** 2
    sd = math.sqrt(ss / (n - 1))
    if sd == 0.0:
        return np.nan
    x = (w - mu) / sd
    M = n - (m - 1) * tau
    hist = np.zeros(M, dtype=np.int64)
    e2 = eps * eps
    for i in range(M):
        j = i + 1
        left = False
        while j < M and not left:
            d2 = 0.0
            for a in range(m):
                dd = x[i + a * tau] - x[j + a * tau]
                d2 += dd * dd
            if d2 > e2:
                left = True
            j += 1
        while j < M:
            d2 = 0.0
            for a in range(m):
                dd = x[i + a * tau] - x[j + a * tau]
                d2 += dd * dd
            if d2 <= e2:
                hist[j - i] += 1
                break
            j += 1
    tot = hist.sum()
    if tot == 0:
        return np.nan
    h = 0.0
    for c in hist:
        if c > 0:
            p = c / tot
            h -= p * math.log(p)
    return h / math.log(M)
