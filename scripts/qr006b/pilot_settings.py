"""The values the pilot sets (pre-registration §7), each by its stated rule.

Uses its own seed stream (class code 'aux'), so no series used here is
reused anywhere else.
"""

import math

import numpy as np
from numba import njit

from . import config as C
from . import models as M
from .strata import seed_for


# ------------------------------------------------------------------ S3 ----
def s3_sigma(family, root, n_runs=50):
    """Smallest grid sigma at which >= 50% of transition runs flicker before
    t_crit (excursion past the t_tip threshold and back, >= 5 samples)."""
    key = "a" if family == "a_may_high" else "b"
    grid = C.S3_SIGMA_GRID[key]
    table = []
    for gi, sig in enumerate(grid):
        hits = 0
        for r in range(n_runs):
            rng = np.random.default_rng(seed_for(root, "S3", family, "aux", gi * 1000 + r))
            if key == "a":
                s = M.simulate_may(rng, "transition", sigma=sig, tip_rule="last")
                up = False
            else:
                s = M.simulate_cubic(rng, "transition", sigma=sig, tip_rule="last")
                up = True
            hits += M.flickers_before(s["x"], s["thr"], up, s["tcrit"])
        frac = hits / n_runs
        table.append((sig, frac))
        if frac >= 0.5:
            return sig, table
    return None, table


# ------------------------------------------------------------------ S4 ----
@njit(cache=True)
def _fpt(model, x0, p, sigma, dW, dt, every, thr, upward):
    x = x0
    for i in range(dW.shape[0]):
        if model == 0:
            f = x * (1.0 - x) - p * x * x / (0.01 + x * x)
        else:
            f = x - x * x * x + p
        x = x + f * dt + sigma * dW[i]
        if model == 0 and x < 0.0:
            x = 0.0
        if (i + 1) % every == 0:
            if (upward and x > thr) or ((not upward) and x < thr):
                return (i + 1) * dt
    return np.inf


def _kramers_sigma(model, p, record):
    """sigma whose Kramers median escape time equals the record length
    (gradient system dx = -V' dt + sigma dW; Amendment A9 grid centre)."""
    if model == 0:
        f = lambda x: x * (1 - x) - p * x * x / (0.01 + x * x)
        rts = M.may_roots(p)
        a, b = rts.max(), rts[1]                  # upper well, saddle
        fp = lambda x: M.may_jac(x, p)
    else:
        f = lambda x: x - x ** 3 + p
        rts = M.cubic_roots(p)
        a, b = rts.min(), rts[1]                  # left well, saddle
        fp = lambda x: 1 - 3 * x * x
    xs = np.linspace(a, b, 20001)
    dV = -np.trapezoid(f(xs), xs)                 # V(b) - V(a) > 0
    pref = 2 * math.pi / math.sqrt(abs(fp(a)) * abs(fp(b)))
    # median = ln2 * mean;  mean = pref * exp(2 dV / sigma^2)
    return math.sqrt(2 * dV / math.log(record / (math.log(2) * pref))), dV


def s4_sigma(family, root, n_runs=100, horizon_factor=3):
    model = 0 if family == "a_may_fixed" else 1
    p = C.S4_PARAM["a" if model == 0 else "b"]
    record = C.T_MAX
    sig_k, dV = _kramers_sigma(model, p, record)
    grid = sig_k * 2.0 ** np.linspace(-0.5, 0.5, 8)
    if model == 0:
        x0 = M.may_roots(p).max()
        thr, up = M.may_threshold(), False
    else:
        x0 = M.cubic_roots(p).min()
        thr, up = 0.0, True
    every = int(round(C.SAMPLE_EVERY / C.DT))
    nsteps = int(horizon_factor * (record + C.T_BURN) / C.DT)
    table = []
    for gi, sig in enumerate(grid):
        fpts = []
        for r in range(n_runs):
            rng = np.random.default_rng(seed_for(root, "S4", family, "aux", gi * 1000 + r))
            dW = rng.standard_normal(nsteps) * math.sqrt(C.DT)
            # escapes during the burn-in are counted from t = 0 of the burn-in;
            # record time starts after burn-in
            fpts.append(_fpt(model, x0, p, sig, dW, C.DT, every, thr, up) - C.T_BURN)
        med = float(np.median(fpts))
        table.append((float(sig), med))
    best = min(table, key=lambda t: abs(math.log(max(t[1], 1e-9) / record))
               if np.isfinite(t[1]) else np.inf)
    return best[0], dict(kramers_sigma=sig_k, barrier=dV, table=table)


# ------------------------------------------------------------------ S5 ----
def s5_settings(root, n_runs=100):
    out = {}
    for key, model, fam in (("a", 0, "a_rtip_sn"), ("b", 1, "b_rtip_dw")):
        rc = M.rtip_critical_rate(model)
        sig = C.S5["sigma"]
        hist = []
        for attempt in range(8):
            tipped = 0
            for r in range(n_runs):
                rng = np.random.default_rng(seed_for(root, "S5", fam, "aux", attempt * 1000 + r))
                rr = rc * rng.uniform(0.5, 0.9)
                s = M.simulate_rtip(rng, model, rr, rc, sig)
                tipped += s["tip"] is not None
            hist.append((sig, tipped / n_runs))
            if tipped / n_runs <= 0.02:
                break
            sig /= 2
        out[key] = dict(rc=rc, sigma=sig, history=hist)
    return out
