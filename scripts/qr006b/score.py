"""Scoring (pre-registration §5-§6): AUC, directions, bootstrap, Holm,
online alarms at a fixed false-alarm rate, lead time, detection."""

import numpy as np
from scipy.stats import rankdata

from . import config as C


def auc(pos, neg):
    """Mann-Whitney P(pos > neg) + 0.5 P(tie). Amendment A20: a pair in which
    either value is undefined (NaN) counts as a tie, so undefined values are
    uninformative instead of being dropped from one class only."""
    pos = np.asarray(pos, float)
    neg = np.asarray(neg, float)
    n_all = len(pos) * len(neg)
    if n_all == 0:
        return np.nan
    p = pos[~np.isnan(pos)]
    q = neg[~np.isnan(neg)]
    if len(p) == 0 or len(q) == 0:
        return 0.5
    r = rankdata(np.concatenate([p, q]))
    u = r[: len(p)].sum() - len(p) * (len(p) + 1) / 2
    return (u + 0.5 * (n_all - len(p) * len(q))) / n_all


def learned_direction(tr_cal, nu_cal):
    """§4: sign of the median Kendall-tau difference, transition minus null."""
    d = np.nanmedian(tr_cal) - np.nanmedian(nu_cal)
    return 1 if d >= 0 else -1


def directions(names, fixed, tau_tr_cal, tau_nu_cal, learn_all=False):
    out = {}
    for j, n in enumerate(names):
        dflt = fixed.get(n, 0)
        if dflt == 0 or learn_all:
            out[n] = learned_direction(tau_tr_cal[:, j], tau_nu_cal[:, j])
        else:
            out[n] = dflt
    return out


def _auc_matrix(P, N):
    """AUC per column; vectorised when there are no NaNs."""
    if not (np.isnan(P).any() or np.isnan(N).any()):
        nP, nN = P.shape[0], N.shape[0]
        r = rankdata(np.vstack([P, N]), axis=0)
        return (r[:nP].sum(axis=0) - nP * (nP + 1) / 2) / (nP * nN)
    return np.array([auc(P[:, j], N[:, j]) for j in range(P.shape[1])])


def bootstrap_auc(P, N, n_boot=C.N_BOOT, seed=0):
    """Paired, stratified bootstrap over series (§5.6): the same resample of
    transition and null series for every indicator. Returns (n_boot, k)."""
    rng = np.random.default_rng(seed)
    nP, nN = P.shape[0], N.shape[0]
    out = np.empty((n_boot, P.shape[1]))
    for b in range(n_boot):
        out[b] = _auc_matrix(P[rng.integers(0, nP, nP)], N[rng.integers(0, nN, nN)])
    return out


def holm(pvals):
    p = np.asarray(pvals, float)
    order = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    run = 0.0
    for r, i in enumerate(order):
        run = max(run, (m - r) * p[i])
        adj[i] = min(1.0, run)
    return adj


# ------------------------------------------------------------ online ------
def run_min(tau_on, run=C.ALARM_RUN):
    """m_k = min(tau_{k-run+1..k}); NaN until `run` defined values in a row."""
    n = len(tau_on)
    m = np.full(n, np.nan)
    for k in range(run - 1, n):
        seg = tau_on[k - run + 1: k + 1]
        if not np.isnan(seg).any():
            m[k] = seg.min()
    return m


def far_threshold(null_tau_on, far=C.FAR):
    """θ such that at most a fraction `far` of (calibration) null series ever
    satisfy tau >= θ for ALARM_RUN consecutive evaluation points (§5.2)."""
    mx = np.array([np.nanmax(run_min(t)) if np.isfinite(run_min(t)).any() else -np.inf
                   for t in null_tau_on])
    desc = np.sort(mx)[::-1]
    k = int(np.floor(far * len(desc)))
    if k >= len(desc):
        return -np.inf
    return float(np.nextafter(desc[k], np.inf))


def alarm_index(tau_on, theta):
    m = run_min(tau_on)
    hit = np.flatnonzero(m >= theta)
    return int(hit[0]) if hit.size else None


def lead_times(tau_on_list, ends_list, tips, theta, buffer=C.BUFFER):
    """Lead time t_tip - t_alarm in samples; misses (no alarm, or an alarm after
    t_tip - B) are NaN."""
    out = []
    for tau_on, ends, tip in zip(tau_on_list, ends_list, tips):
        k = alarm_index(tau_on, theta)
        if k is None or ends[k] > tip - buffer:
            out.append(np.nan)
        else:
            out.append(float(tip - ends[k]))
    return np.array(out)
