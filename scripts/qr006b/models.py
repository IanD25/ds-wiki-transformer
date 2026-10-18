"""Simulators for every stratum (pre-registration §2.2, Amendments A1, A9-A12).

Bury et al. 2021's test models (May fold, consumer-resource Hopf and
transcritical) are re-implemented here from the equations and parameter
values in their scripts (Amendment A1); their code is not copied. Wrapper
fidelity against their unmodified scripts is checked in fidelity_bury.py.

Each simulate_* function takes a numpy Generator and returns a dict:
  x       sampled series, shape (n,) or (n, d)
  t       sample times
  tip     index of t_tip in x, or None (null / no tip)
  tcrit   index at which the control parameter crosses its bifurcation, or None
"""

import math

import numpy as np
from numba import njit
from scipy.stats import levy_stable

from . import config as C

# noise kinds for the 1-D kernel
ADD, MUL_X, MUL_SQRT, STABLE = 0, 1, 2, 3
# drift models for the 1-D kernel
MAY, CUBIC = 0, 1


# ------------------------------------------------------------------ kernels --
@njit(cache=True)
def _drift(model, x, p):
    if model == 0:   # May harvesting, r = k = 1, s = 0.1
        return x * (1.0 - x) - p * x * x / (0.01 + x * x)
    else:            # cubic
        return x - x * x * x + p


@njit(cache=True)
def _noise(kind, x, sigma, inc):
    if kind == 0 or kind == 3:
        return sigma * inc
    elif kind == 1:
        return sigma * x * inc
    else:
        return sigma * math.sqrt(1.0 + x * x) * inc


@njit(cache=True)
def em_1d(model, kind, x0, p_burn, p, sigma, inc_burn, inc, dt, every, reflect):
    """Euler-Maruyama; parameter p[i] at step i (Bury's scheme); returns x
    sampled every `every` steps starting at step 0."""
    x = x0
    for i in range(inc_burn.shape[0]):
        x = x + _drift(model, x, p_burn) * dt + _noise(kind, x, sigma, inc_burn[i])
        if reflect and x < 0.0:
            x = 0.0
    n = p.shape[0]
    out = np.empty((n + every - 1) // every)
    out[0] = x
    for i in range(n - 1):
        x = x + _drift(model, x, p[i]) * dt + _noise(kind, x, sigma, inc[i])
        if reflect and x < 0.0:
            x = 0.0
        if (i + 1) % every == 0:
            out[(i + 1) // every] = x
    return out


@njit(cache=True)
def em_cr(x0, y0, a_burn, a, r, k, h, e, m, sx, sy, wxb, wyb, wx, wy, dt, every):
    """Consumer-resource model (Bury's cr_hopf / cr_trans), Euler-Maruyama."""
    x = x0
    y = y0
    for i in range(wxb.shape[0]):
        fx = r * x * (1 - x / k) - (a_burn * x * y) / (1 + a_burn * h * x)
        fy = e * a_burn * x * y / (1 + a_burn * h * x) - m * y
        x = x + fx * dt + sx * wxb[i]
        y = y + fy * dt + sy * wyb[i]
    n = a.shape[0]
    out = np.empty(((n + every - 1) // every, 2))
    out[0, 0] = x
    out[0, 1] = y
    for i in range(n - 1):
        ai = a[i]
        fx = r * x * (1 - x / k) - (ai * x * y) / (1 + ai * h * x)
        fy = e * ai * x * y / (1 + ai * h * x) - m * y
        x = x + fx * dt + sx * wx[i]
        y = y + fy * dt + sy * wy[i]
        if x < 0:
            x = 0.0
        if y < 0:
            y = 0.0
        if (i + 1) % every == 0:
            out[(i + 1) // every, 0] = x
            out[(i + 1) // every, 1] = y
    return out


@njit(cache=True)
def em_layritz(x0, k_arr, inc_spin, inc, scale, dt, every):
    """x' = k - x^2 with alpha-stable increments (Layritz 2025 StableFold).
    Stops at escape x < -sqrt(k) - 0.1 k; returns sampled path and the
    sample index of escape (-1 if none)."""
    x = x0
    k0 = k_arr[0]
    for i in range(inc_spin.shape[0]):
        x = x + (k0 - x * x) * dt + scale * inc_spin[i]
    n = k_arr.shape[0]
    out = np.full((n + every - 1) // every, np.nan)
    out[0] = x
    for i in range(n - 1):
        ki = k_arr[i]
        x = x + (ki - x * x) * dt + scale * inc[i]
        kn = k_arr[i + 1]
        if x < -math.sqrt(kn) - 0.1 * kn:
            j = (i + 1 + every - 1) // every
            if j < out.shape[0]:
                out[j] = x
            return out, j
        if (i + 1) % every == 0:
            out[(i + 1) // every] = x
    return out, -1


@njit(cache=True)
def em_rtip(model, x0, t0, dt, nsteps, every, r, lam_max, sigma, dw, stop_after):
    """R-tipping models (S5). model 0: x' = (x+lam)^2 - 1, lam = (L/2)(1+tanh(r t));
    model 1: x' = (x-lam) - (x-lam)^3, lam = -(L/2)(1+tanh(r t)).
    Returns the sampled path (NaN after stopping) and the sample index of the
    first tip (-1 if none). Simulation stops `stop_after` samples after a tip."""
    x = x0
    out = np.full((nsteps + every - 1) // every, np.nan)
    out[0] = x
    tip = -1
    for i in range(nsteps - 1):
        t = t0 + i * dt
        if model == 0:
            lam = 0.5 * lam_max * (1.0 + math.tanh(r * t))
            f = (x + lam) ** 2 - 1.0
        else:
            lam = -0.5 * lam_max * (1.0 + math.tanh(r * t))
            u = x - lam
            f = u - u * u * u
        x = x + f * dt + sigma * dw[i]
        tn = t + dt
        if model == 0:
            lamn = 0.5 * lam_max * (1.0 + math.tanh(r * tn))
            tipped = x + lamn > 1.0
        else:
            lamn = -0.5 * lam_max * (1.0 + math.tanh(r * tn))
            tipped = x - lamn > 0.0
        if (i + 1) % every == 0:
            j = (i + 1) // every
            out[j] = x
            if tip < 0 and tipped:
                tip = j
            if tip >= 0 and j >= tip + stop_after:
                return out, tip
        if model == 0 and x > 1e6:
            break
    return out, tip


# ------------------------------------------------------------ equilibria ----
def may_roots(b, s=0.1):
    """Real equilibria x > 0 of the May model at harvest rate b (sorted)."""
    r = np.roots([-1.0, 1.0, -(s * s + b), s * s])
    return np.sort(r.real[np.abs(r.imag) < 1e-3])


def cubic_roots(c):
    r = np.roots([-1.0, 0.0, 1.0, c])
    return np.sort(r.real[np.abs(r.imag) < 1e-6])


def may_threshold():
    """Midpoint between the upper (fold) and lower stable branch at b_crit (§2.3)."""
    rts = may_roots(C.MAY["b_crit"])
    return 0.5 * (rts.min() + rts.max())


def may_jac(x, b, s=0.1):
    return 1 - 2 * x - b * 2 * x * s * s / (s * s + x * x) ** 2


def tau_rec0(model):
    """Linear recovery time -1/lambda_0 at the starting parameter (§5.2)."""
    if model == "may":
        x = may_roots(C.MAY["b_lo"]).max()
        return -1.0 / may_jac(x, C.MAY["b_lo"])
    if model == "cubic":
        x = cubic_roots(C.CUBIC["c_lo"]).min()
        return -1.0 / (1 - 3 * x * x)
    if model in ("cr_hopf", "cr_trans"):
        P = C.CR_HOPF if model == "cr_hopf" else C.CR_TRANS
        r, k, h, e, m, a = P["r"], P["k"], P["h"], P["e"], P["m"], P["a_lo"]
        # interior equilibrium
        x = m / (a * (e - h * m))
        y = r * (1 - x / k) * (1 + a * h * x) / a
        eps = 1e-7
        def F(v):
            X, Y = v
            return np.array([r * X * (1 - X / k) - a * X * Y / (1 + a * h * X),
                             e * a * X * Y / (1 + a * h * X) - m * Y])
        J = np.column_stack([(F([x + eps, y]) - F([x - eps, y])) / (2 * eps),
                             (F([x, y + eps]) - F([x, y - eps])) / (2 * eps)])
        return -1.0 / np.linalg.eigvals(J).real.max()
    raise ValueError(model)


# ------------------------------------------------------------ helpers ------
def _stable_inc(rng, alpha, size, dt):
    L = levy_stable.rvs(alpha, 0.0, size=size, random_state=rng)
    return L * dt ** (1.0 / alpha)


def _first_crossing(x, thr, upward):
    idx = np.flatnonzero(x > thr) if upward else np.flatnonzero(x < thr)
    return int(idx[0]) if idx.size else None


def _last_crossing(x, thr, upward):
    """Start of the final excursion past thr that lasts to the end of the
    record (Amendment A10, S3); None if the record does not end past thr."""
    past = x > thr if upward else x < thr
    if not past[-1]:
        return None
    back = np.flatnonzero(~past)
    return int(back[-1] + 1) if back.size else 0


def flickers_before(x, thr, upward, tcrit, min_len=C.FLICKER_MIN_LEN):
    """True if an excursion past thr that returns, lasting >= min_len samples,
    starts before tcrit (§7, S3 rule)."""
    past = (x > thr) if upward else (x < thr)
    n = len(x)
    i = 0
    while i < min(tcrit, n):
        if past[i]:
            j = i
            while j < n and past[j]:
                j += 1
            if j < n and (j - i) >= min_len:
                return True
            i = j
        else:
            i += 1
    return False


# --------------------------------------------------------- simulators ------
def _ramp(lo, hi, n):
    return np.linspace(lo, hi, n)


def simulate_may(rng, cls, noise="add", sigma=None, alpha=None, fixed_b=None,
                 tip_rule="first"):
    P = C.MAY
    n = int(round(C.T_MAX / C.DT))
    nb = int(round(C.T_BURN / C.DT))
    every = int(round(C.SAMPLE_EVERY / C.DT))
    if fixed_b is not None:
        b = np.full(n, fixed_b)
    elif cls == "transition":
        b = _ramp(P["b_lo"], P["b_hi"], n)
    elif cls == "nullB":
        b = _ramp(P["b_lo"], P["b_lo"] + 0.5 * (P["b_crit"] - P["b_lo"]), n)
    else:
        b = np.full(n, P["b_lo"])
    x0 = may_roots(b[0]).max()
    if noise == "stable":
        ib = _stable_inc(rng, alpha, nb, C.DT)
        ii = _stable_inc(rng, alpha, n, C.DT)
        kind = STABLE
    else:
        ib = rng.standard_normal(nb) * math.sqrt(C.DT)
        ii = rng.standard_normal(n) * math.sqrt(C.DT)
        kind = {"add": ADD, "mul": MUL_X}[noise]
    sig = P["sigma"] if sigma is None else sigma
    x = em_1d(MAY, kind, x0, b[0], b, sig, ib, ii, C.DT, every, True)
    t = np.arange(len(x)) * C.SAMPLE_EVERY
    thr = may_threshold()
    tcrit = None
    if fixed_b is None and cls == "transition":
        tcrit = int(np.ceil(np.flatnonzero(b > P["b_crit"])[1] / every))
    tip = None
    if cls == "transition" or fixed_b is not None:
        tip = (_last_crossing(x, thr, False) if tip_rule == "last"
               else _first_crossing(x, thr, False))
    return dict(x=x, t=t, tip=tip, tcrit=tcrit, thr=thr)


def simulate_cubic(rng, cls, noise="add", sigma=None, fixed_c=None, tip_rule="first"):
    P = C.CUBIC
    n = int(round(C.T_MAX / C.DT))
    nb = int(round(C.T_BURN / C.DT))
    every = int(round(C.SAMPLE_EVERY / C.DT))
    c_star = 2 / (3 * math.sqrt(3))
    if fixed_c is not None:
        c = np.full(n, fixed_c)
    elif cls == "transition":
        c = _ramp(P["c_lo"], P["c_hi"], n)
    elif cls == "nullB":
        c = _ramp(P["c_lo"], P["c_lo"] + 0.5 * (c_star - P["c_lo"]), n)
    else:
        c = np.full(n, P["c_lo"])
    x0 = cubic_roots(c[0]).min()
    ib = rng.standard_normal(nb) * math.sqrt(C.DT)
    ii = rng.standard_normal(n) * math.sqrt(C.DT)
    kind = {"add": ADD, "mul": MUL_SQRT}[noise]
    sig = P["sigma"] if sigma is None else sigma
    x = em_1d(CUBIC, kind, x0, c[0], c, sig, ib, ii, C.DT, every, False)
    t = np.arange(len(x)) * C.SAMPLE_EVERY
    tcrit = None
    if fixed_c is None and cls == "transition":
        tcrit = int(np.ceil(np.flatnonzero(c > c_star)[0] / every))
    tip = None
    if cls == "transition" or fixed_c is not None:
        tip = (_last_crossing(x, 0.0, True) if tip_rule == "last"
               else _first_crossing(x, 0.0, True))
    return dict(x=x, t=t, tip=tip, tcrit=tcrit, thr=0.0)


def simulate_cr(rng, cls, which):
    P = C.CR_HOPF if which == "hopf" else C.CR_TRANS
    n = int(round(C.T_MAX / C.DT))
    nb = int(round(C.T_BURN / C.DT))
    every = int(round(C.SAMPLE_EVERY / C.DT))
    if cls == "transition":
        a = _ramp(P["a_lo"], P["a_hi"], n)
    elif cls == "nullB":
        a = _ramp(P["a_lo"], P["a_lo"] + 0.5 * (P["a_crit"] - P["a_lo"]), n)
    else:
        a = np.full(n, P["a_lo"])
    sq = math.sqrt(C.DT)
    wxb = rng.standard_normal(nb) * sq
    wx = rng.standard_normal(n) * sq
    wyb = rng.standard_normal(nb) * sq
    wy = rng.standard_normal(n) * sq
    xy = em_cr(P["x0"], P["y0"], a[0], a, P["r"], P["k"], P["h"], P["e"], P["m"],
               P["sigma"], P["sigma"], wxb, wyb, wx, wy, C.DT, every)
    t = np.arange(len(xy)) * C.SAMPLE_EVERY
    tcrit = None
    if cls == "transition":
        # Bury: tcrit = a[a > abif].index[1]; samples with time <= tcrit
        tcrit = int(math.floor(np.flatnonzero(a > P["a_crit"])[1] * C.DT))
    # observed variable: x (Bury's ROC uses x only)
    return dict(x=xy[:, 0].copy(), t=t, tip=tcrit, tcrit=tcrit, thr=None)


def simulate_layritz(rng, cls, alpha, extra_steps=10_000):
    P = C.LAYRITZ
    nramp = int(round(P["k_hi"] / P["k_step"])) + 1
    if cls == "transition":
        k = np.concatenate([P["k_hi"] - P["k_step"] * np.arange(nramp),
                            np.zeros(extra_steps)])
        k[k < 0] = 0.0
    else:
        # same record length as a transition run (ramp + post-ramp extension)
        k = np.full(nramp + extra_steps, P["k_hi"])
    ispin = _stable_inc(rng, alpha, P["spinup"], P["dt"])
    inc = _stable_inc(rng, alpha, len(k), P["dt"])
    x, j = em_layritz(math.sqrt(P["k_hi"]), k, ispin, inc, P["scale"], P["dt"],
                      P["sample_every"])
    t = np.arange(len(x)) * P["sample_every"] * P["dt"]
    nsamp_ramp = (nramp + P["sample_every"] - 1) // P["sample_every"]
    tip = j if j >= 0 else None
    return dict(x=x, t=t, tip=tip, tcrit=nsamp_ramp, thr=None, ramp_len=nsamp_ramp)


def rtip_window(r_c):
    """Amendment A11: record t in [-T, T], T = span_over_rc / r_c, 1500 samples."""
    T = C.S5["span_over_rc"] / r_c
    ds = 2 * T / C.S5["n_samples"]
    return T, ds, ds / C.S5["substeps"]


def simulate_rtip(rng, model, r, r_c, sigma, stop_after=60, burn=10.0):
    T, ds, dt = rtip_window(r_c)
    L = C.S5["lam_max"]
    every = C.S5["substeps"]
    nsteps = C.S5["n_samples"] * every
    lam0 = 0.5 * L * (1 + math.tanh(-r * T))
    if model == 0:
        x0 = -1.0 - lam0
    else:
        x0 = -lam0 - 1.0
    # burn-in at the starting parameter value (the ramp is ~flat there)
    nb = int(round(burn / dt))
    dwb = rng.standard_normal(nb) * math.sqrt(dt)
    xb, _ = em_rtip(model, x0, -1e9, dt, nb, nb, r, L, sigma, dwb, 1)
    x0 = xb[-1] if np.isfinite(xb[-1]) else x0
    dw = rng.standard_normal(nsteps) * math.sqrt(dt)
    x, tip = em_rtip(model, x0, -T, dt, nsteps, every, r, L, sigma, dw, stop_after)
    t = -T + np.arange(len(x)) * ds
    return dict(x=x, t=t, tip=(tip if tip >= 0 else None), tcrit=None, thr=None)


def rtip_critical_rate(model, lo=0.01, hi=5.0, rel=0.01):
    """§7: r_c from deterministic runs, bisection to 1% relative precision."""
    def tips(r):
        T = 60.0 / r + 20.0
        dt = min(0.002, 0.02 / r)
        n = int(2 * T / dt)
        L = C.S5["lam_max"]
        lam0 = 0.5 * L * (1 + math.tanh(-r * T))
        x0 = -1.0 - lam0 if model == 0 else -lam0 - 1.0
        _, tip = em_rtip(model, x0, -T, dt, n, 1, r, L, 0.0, np.zeros(n), 1)
        return tip >= 0
    assert not tips(lo) and tips(hi)
    while (hi - lo) / lo > rel:
        mid = math.sqrt(lo * hi)
        if tips(mid):
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


# ---------------------------------------------------- Lever / Weinans 2021 --
# Eqs. 1-2 of Weinans et al. 2021 (Sci. Rep. 11:9148); parameters from their
# Methods (4D basic scenario) and SI (20D full collapse). Amendment A12.
import os as _os

_DATA = _os.path.join(_os.path.dirname(__file__), "data")


def lever_params(dim):
    if dim == 4:
        g = np.array([[1.0, 0.8], [0.8, 1.0]])
        c = np.array([[0.3, 0.1], [0.1, 0.3]])
        return dict(gA=g, gP=g.copy(), cA=c, cP=c.copy(), rP=np.full(2, -0.5),
                    rA0=np.array([-0.3, -0.2]), h=0.5, sigma=0.02)
    rd = lambda m: np.loadtxt(_os.path.join(_DATA, f"weinans2021_full_{m}.csv"), delimiter=",")
    return dict(gA=rd("gA"), gP=rd("gP"), cA=rd("cA"), cP=rd("cP"),
                rP=np.full(10, -0.1), rA0=np.full(10, -0.0424), h=0.5, sigma=0.02)


@njit(cache=True)
def _lever_drift(P, A, rP, rA, gP, gA, cP, cA, h):
    nP = P.shape[0]
    nA = A.shape[0]
    fP = np.empty(nP)
    fA = np.empty(nA)
    for i in range(nP):
        s = 0.0
        for k in range(nA):
            s += gP[i, k] * A[k]
        comp = 0.0
        for j in range(nP):
            comp += cP[i, j] * P[j]
        fP[i] = rP[i] * P[i] + s / (1.0 + h * s) * P[i] - comp * P[i]
    for k in range(nA):
        s = 0.0
        for i in range(nP):
            s += gA[k, i] * P[i]
        comp = 0.0
        for l in range(nA):
            comp += cA[k, l] * A[l]
        fA[k] = rA[k] * A[k] + s / (1.0 + h * s) * A[k] - comp * A[k]
    return fP, fA


@njit(cache=True)
def em_lever(P0, A0, rP, rA0, delta_burn, delta, gP, gA, cP, cA, h,
             sP, sA, dWb, dW, dt, every):
    """r^A = rA0 - delta[i] at step i. sP, sA: per-species noise coefficients;
    multiplicative if sP/sA are applied to abundance (flag via sign: negative
    coefficient means multiplicative). Abundances reflected at 0."""
    nP = P0.shape[0]
    nA = A0.shape[0]
    P = P0.copy()
    A = A0.copy()
    for i in range(dWb.shape[0]):
        fP, fA = _lever_drift(P, A, rP, rA0 - delta_burn, gP, gA, cP, cA, h)
        for q in range(nP):
            g = sP[q] if sP[q] >= 0 else -sP[q] * P[q]
            P[q] = abs(P[q] + fP[q] * dt + g * dWb[i, q])
        for q in range(nA):
            g = sA[q] if sA[q] >= 0 else -sA[q] * A[q]
            A[q] = abs(A[q] + fA[q] * dt + g * dWb[i, nP + q])
    n = delta.shape[0]
    out = np.empty(((n + every - 1) // every, nP + nA))
    out[0, :nP] = P
    out[0, nP:] = A
    for i in range(n - 1):
        fP, fA = _lever_drift(P, A, rP, rA0 - delta[i], gP, gA, cP, cA, h)
        for q in range(nP):
            g = sP[q] if sP[q] >= 0 else -sP[q] * P[q]
            P[q] = abs(P[q] + fP[q] * dt + g * dW[i, q])
        for q in range(nA):
            g = sA[q] if sA[q] >= 0 else -sA[q] * A[q]
            A[q] = abs(A[q] + fA[q] * dt + g * dW[i, nP + q])
        if (i + 1) % every == 0:
            out[(i + 1) // every, :nP] = P
            out[(i + 1) // every, nP:] = A
    return out


def lever_equilibrium(dim, delta=0.0, T=4000.0, start=None):
    p = lever_params(dim)
    nP = len(p["rP"])
    n = int(T / C.DT)
    x0 = np.ones(2 * nP) * 3.0 if start is None else start
    z = np.zeros((1, 2 * nP))
    out = em_lever(x0[:nP].copy(), x0[nP:].copy(), p["rP"], p["rA0"], delta,
                   np.full(n, delta), p["gP"], p["gA"], p["cP"], p["cA"], p["h"],
                   np.zeros(nP), np.zeros(nP), z[:0], np.zeros((n, 2 * nP)), C.DT, n - 1)
    return out[-1]


def lever_collapse_delta(dim, rel=1e-3):
    """Deterministic collapse point: smallest delta at which the state started at
    the delta = 0 equilibrium loses >= 90% of total pollinator abundance."""
    nP = len(lever_params(dim)["rP"])
    x_start = lever_equilibrium(dim, 0.0)
    a0 = x_start[nP:].sum()
    collapsed = lambda dl: lever_equilibrium(dim, dl, T=6000.0, start=x_start)[nP:].sum() < 0.1 * a0
    lo, hi = 0.0, 0.1
    while not collapsed(hi):
        lo, hi = hi, hi * 1.5
    while (hi - lo) / hi > rel:
        mid = 0.5 * (lo + hi)
        if collapsed(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi), x_start


_LEVER_CACHE = {}


def simulate_lever(rng, cls, dim, noise="add", crit_fraction=0.9):
    if dim not in _LEVER_CACHE:
        _LEVER_CACHE[dim] = lever_collapse_delta(dim)
    dc, x_start = _LEVER_CACHE[dim]
    p = lever_params(dim)
    nP = len(p["rP"])
    n = int(round(C.T_MAX / C.DT))
    nb = int(round(C.T_BURN / C.DT))
    every = int(round(C.SAMPLE_EVERY / C.DT))
    d_end = dc / crit_fraction
    if cls == "transition":
        delta = np.linspace(0.0, d_end, n)
    elif cls == "nullB":
        delta = np.linspace(0.0, 0.5 * dc, n)
    else:
        delta = np.zeros(n)
    sq = math.sqrt(C.DT)
    dWb = rng.standard_normal((nb, 2 * nP)) * sq
    dW = rng.standard_normal((n, 2 * nP)) * sq
    if noise == "add":
        s = np.full(nP, p["sigma"])
        sP, sA = s, s.copy()
    else:   # multiplicative, matched per species at the start (as S1)
        sP = -p["sigma"] / x_start[:nP]
        sA = -p["sigma"] / x_start[nP:]
    X = em_lever(x_start[:nP].copy(), x_start[nP:].copy(), p["rP"], p["rA0"], 0.0,
                 delta, p["gP"], p["gA"], p["cP"], p["cA"], p["h"], sP, sA, dWb, dW,
                 C.DT, every)
    t = np.arange(len(X)) * C.SAMPLE_EVERY
    tcrit = tip = None
    if cls == "transition":
        tcrit = int(np.ceil(np.flatnonzero(delta > dc)[0] / every))
        a0 = x_start[nP:].sum()
        tip = _first_crossing(X[:, nP:].sum(axis=1), 0.1 * a0, False)
    return dict(x=X, t=t, tip=tip, tcrit=tcrit, thr=None)
