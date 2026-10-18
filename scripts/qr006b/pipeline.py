"""Per-series indicator pipeline (pre-registration §3-§5).

compute_series() takes one observed series and returns:
  tau_off   Kendall tau of each windowed indicator vs time (offline residuals)
  tau_on    expanding-window Kendall tau trajectories (causal residuals)
  det       indicator levels on the detection windows (causal residuals)
"""

import math

import numpy as np
from numba import njit

from . import config as C
from .indicators import baselines as B
from .indicators import info as I
from .preprocess import causal_residuals, gaussian_residuals, lowess_residuals, window_ends

# ---------------------------------------------------------------- names ----
UNI = ["I1_mi", "I3_pe", "I4_sampen", "I5_fi", "I6_rpde",
       "B1_ac1", "B2_rank_ac1", "B3_var", "B4_mad", "B5_skew", "B6_kurt",
       "B7_bc", "B8_crad", "B9_stable_gamma", "B10_restoring", "B11_diffusion",
       "B12_jump",
       # declared secondaries / sensitivities (exploratory)
       "x_pe3", "x_pe5", "x_rpde_m3", "x_rad"]
MULTI_EXTRA = ["I2_te", "M_maxeig", "M_pc1_share", "M_pc1_ac1"]

DIRECTION = {  # +1 rises towards the transition, -1 falls, 0 learned (§4)
    "I1_mi": 1, "I2_te": 0, "I3_pe": -1, "I4_sampen": -1, "I5_fi": -1,
    "I6_rpde": 0, "B1_ac1": 1, "B2_rank_ac1": 1, "B3_var": 1, "B4_mad": 1,
    "B5_skew": 0, "B6_kurt": 0, "B7_bc": 1, "B8_crad": 1, "B9_stable_gamma": 1,
    "B10_restoring": -1, "B11_diffusion": 1, "B12_jump": 0,
    "M_maxeig": 1, "M_pc1_share": 1, "M_pc1_ac1": 1,      # Amendment A13
    "x_pe3": -1, "x_pe5": -1, "x_rpde_m3": 0, "x_rad": 1, "x_fi_raw": -1,
}
INFO = {"I1_mi", "I2_te", "I3_pe", "I4_sampen", "I5_fi", "I6_rpde"}
BASE = {k for k in DIRECTION if k.startswith("B") or k.startswith("M_")}


def indicator_names(multivariate):
    names = list(UNI)
    if multivariate:
        names = names + MULTI_EXTRA
    return names + ["x_fi_raw"]


# --------------------------------------------------------- window values ---
def _uni_values(w, sos):
    """All univariate indicators on one 1-D residual window."""
    w = np.ascontiguousarray(w, dtype=np.float64)
    var, sk, ku, bc = B.moments(w)
    rest, d2, lam = B.km_indicators(w, C.KM_BINS, C.KM_CENTRAL, 1.0)
    return [
        I.lagged_mi(w, C.KSG_K),
        I.permutation_entropy(w, C.PE_ORDER, 1),
        I.sample_entropy(w, C.SAMPEN_M, C.SAMPEN_R),
        I.fisher_index(w[:, None], np.array([sos]), 100.0),
        I.rpde(w, C.RPDE_M, 1, C.RPDE_EPS),
        B.ac1(w), B.rank_ac1(w), var, B.robust_spread(w), sk, ku, bc,
        B.crad(w), B.stable_scale(w), rest, d2, lam,
        I.permutation_entropy(w, 3, 1), I.permutation_entropy(w, 5, 1),
        I.rpde(w, C.RPDE_M_SENS, 1, C.RPDE_EPS), B.rad(w, 1),
    ]


def _multi_values(W, sos, te_pairs, pc1):
    """Univariate set averaged over variables (I5 replaced by the multivariate
    FI, TL 80%), plus transfer entropy and the covariance baselines."""
    W = np.ascontiguousarray(W, dtype=np.float64)
    d = W.shape[1]
    U = np.array([_uni_values(W[:, v], sos[v]) for v in range(d)])
    vals = list(np.nanmean(U, axis=0))
    vals[UNI.index("I5_fi")] = I.fisher_index(W, sos, 80.0)
    te = np.mean([I.transfer_entropy(W[:, s], W[:, t], C.KSG_K) for s, t in te_pairs])
    cov = np.cov(W, rowvar=False)
    ev = np.linalg.eigvalsh(cov)
    proj = W @ pc1
    vals += [te, ev[-1], ev[-1] / ev.sum(), B.ac1(proj)]
    return vals


def te_pairs_for(d):
    pairs = [(s, t) for s in range(d) for t in range(d) if s != t]
    if d <= 4:
        return pairs
    rng = np.random.default_rng(0)
    idx = rng.choice(len(pairs), size=C.TE_PAIRS_20D, replace=False)
    return [pairs[i] for i in sorted(idx)]


# ------------------------------------------------------------- Kendall ----
@njit(cache=True)
def kendall_tau_b(y):
    """tau-b of y against its index (time has no ties); NaNs dropped."""
    n = y.shape[0]
    c = 0.0
    nties = 0.0
    m = 0
    for i in range(n):
        if math.isnan(y[i]):
            continue
        m += 1
        for j in range(i + 1, n):
            if math.isnan(y[j]):
                continue
            d = y[j] - y[i]
            if d > 0:
                c += 1
            elif d < 0:
                c -= 1
            else:
                nties += 1
    n0 = m * (m - 1) / 2.0
    if n0 == 0 or n0 - nties <= 0:
        return np.nan
    return c / math.sqrt(n0 * (n0 - nties))


@njit(cache=True)
def expanding_tau(y, kmin):
    """tau_k = Kendall tau of y[0..k] vs time, for k >= kmin (NaN before)."""
    n = y.shape[0]
    out = np.full(n, np.nan)
    c = 0.0
    nties = 0.0
    m = 0
    for k in range(n):
        if not math.isnan(y[k]):
            for i in range(k):
                if math.isnan(y[i]):
                    continue
                d = y[k] - y[i]
                if d > 0:
                    c += 1
                elif d < 0:
                    c -= 1
                else:
                    nties += 1
            m += 1
        if k >= kmin:
            n0 = m * (m - 1) / 2.0
            if n0 > 0 and n0 - nties > 0:
                out[k] = c / math.sqrt(n0 * (n0 - nties))
    return out


# ----------------------------------------------------------- the series ----
def _as2d(x):
    return x[:, None] if x.ndim == 1 else x


def _window_matrix(R, ends, w, sos, multi, te_pairs, pc1):
    rows = []
    for e in ends:
        W = R[e - w + 1: e + 1]
        if multi:
            rows.append(_multi_values(W, sos, te_pairs, pc1))
        else:
            rows.append(_uni_values(W[:, 0], sos[0]))
    return np.array(rows, dtype=np.float64)


def compute_series(x, seg_len, det_ends, *, window=C.WINDOW, detrend="lowess",
                   transform=None, online=True, obs_noise_rng=None):
    """x: observed series (n,) or (n, d), at least as long as max(det_ends)+1.
    seg_len: pre-transition segment length L (indices 0..L-1).
    det_ends: indices at which 50-point detection windows end.
    transform: optional strictly increasing map applied to residuals (C0g).
    """
    X = _as2d(np.asarray(x, dtype=np.float64))
    if obs_noise_rng is not None:
        X = X.copy()
    d = X.shape[1]
    multi = d > 1
    L = int(seg_len)
    seg = X[:L]
    nref = int(C.REFERENCE_FRACTION * L)

    detr = {"lowess": lowess_residuals, "gaussian": gaussian_residuals,
            "none": lambda v: v - v.mean()}[detrend]
    R_off = np.column_stack([detr(seg[:, v]) for v in range(d)])
    if obs_noise_rng is not None:
        # §5.7: Gaussian observation noise at 10% of the residual SD
        sdr = R_off[:nref].std(axis=0, ddof=1)
        X = X + obs_noise_rng.standard_normal(X.shape) * 0.1 * sdr
        seg = X[:L]
        R_off = np.column_stack([detr(seg[:, v]) for v in range(d)])
    sref = R_off[:nref].std(axis=0, ddof=1)
    if transform is not None:
        R_off = transform(R_off, sref)
        sref_t = R_off[:nref].std(axis=0, ddof=1)
    else:
        sref_t = sref
    sos = 2.0 * sref_t                      # FI size of states (±2 SD, §4.1 I5)

    te_pairs = te_pairs_for(d) if multi else None
    pc1 = None
    if multi:
        ev, evec = np.linalg.eigh(np.cov(R_off[:nref], rowvar=False))
        pc1 = evec[:, -1]

    w, ends = window_ends(L, window)
    out = {"ends": ends, "w": w, "seg_len": L}
    M_off = _window_matrix(R_off, ends, w, sos, multi, te_pairs, pc1)
    # declared secondary: FI on raw, undetrended data (Karunanithi usage)
    raw = seg
    sos_raw = 2.0 * raw[:nref].std(axis=0, ddof=1)
    fi_raw = np.array([I.fisher_index(np.ascontiguousarray(raw[e - w + 1: e + 1]),
                                      sos_raw, 80.0 if multi else 100.0) for e in ends])
    M_off = np.column_stack([M_off, fi_raw])
    out["tau_off"] = np.array([kendall_tau_b(M_off[:, j]) for j in range(M_off.shape[1])])
    out["vals_off"] = M_off.astype(np.float32)

    if online:
        n_full = max(L, (max(det_ends) + 1) if len(det_ends) else 0)
        R_c = np.column_stack([causal_residuals(X[:n_full, v], L) for v in range(d)])
        # online quantities use only the causal residuals' own reference period
        sref_c = R_c[:nref].std(axis=0, ddof=1)
        if transform is not None:
            R_c = transform(R_c, sref_c)
        sos_c = 2.0 * R_c[:nref].std(axis=0, ddof=1)
        pc1_c = None
        if multi:
            _ev, evec = np.linalg.eigh(np.cov(R_c[:nref], rowvar=False))
            pc1_c = evec[:, -1]
        M_on = _window_matrix(R_c[:L], ends, w, sos_c, multi, te_pairs, pc1_c)
        # Amendment A4: online tau starts once the window ends span >= w points
        kmin = int(math.ceil(w / C.STRIDE))
        out["tau_on"] = np.column_stack(
            [expanding_tau(M_on[:, j], kmin) for j in range(M_on.shape[1])]).astype(np.float32)
        det = []
        for e in det_ends:
            Wd = R_c[e - C.DETECT_WINDOW + 1: e + 1]
            det.append(_multi_values(Wd, sos_c, te_pairs, pc1_c) if multi
                       else _uni_values(Wd[:, 0], sos_c[0]))
        out["det"] = np.array(det, dtype=np.float64)
    return out
