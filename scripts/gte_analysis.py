"""
gte_analysis.py — Global Transfer Entropy estimator for 2D Potts.

Matches Brown-Bossomaier-Barnett 2022 (Sci. Rep. 12, 15145, arXiv:1810.09607)
main text Eq. 2 and Suppl. §"Transfer Entropy":

    T_{Y→X} = H(X_t | X_{t-1}) − H(X_t | X_{t-1}, Y_{t-1})
    G       = (1/N) Σ_i T_{s_¬i → s_i}

History length k = 1 (single-step).
Estimator: plug-in (no Miller-Madow, no KSG) — matches Brown exactly.
Neighborhood compression (Suppl. §"Neighbourhood Compression"): encode the
4-neighbor state as the pre-sweep site energy E_i ∈ {0,1,2,3,4} (# matching
neighbors). Reduces from q^5 bins → q × q × 5 bins, losing no transition-
probability information.

Variant: G^{(s)} per-sweep (Brown says this tracks G^{(f)} per-flip closely;
per-sweep is simpler to accumulate via before/after snapshots).
"""

from __future__ import annotations

import numpy as np
from numba import njit


# ── Per-sweep accumulation of pre/post and neighbor-energy histograms ───────

@njit(cache=True, fastmath=False)
def accumulate_gte_histograms(
    spins_before: np.ndarray,   # (L, L), state at start of sweep
    spins_after: np.ndarray,    # (L, L), state at end of sweep (post in-place update)
    q: int,
    L: int,
    hist_joint: np.ndarray,     # (q, q, 5) accumulator, updated in place
    hist_marg: np.ndarray,      # (q, q) accumulator, updated in place
) -> None:
    """
    For each site i: record (X_t = s_after, X_{t-1} = s_before, E_before).
    E_before encoded as number of matching neighbors ∈ {0..4} (compression).

    Histograms:
      hist_joint[x_t, x_prev, e]  — P(X_t, X_{t-1}, Y_{t-1}) with Y compressed to E
      hist_marg[x_t, x_prev]      — P(X_t, X_{t-1}) marginal over Y
    """
    for i in range(L):
        for j in range(L):
            s_before = spins_before[i, j]
            s_after = spins_after[i, j]
            match = 0
            if spins_before[(i + 1) % L, j] == s_before:
                match += 1
            if spins_before[(i - 1) % L, j] == s_before:
                match += 1
            if spins_before[i, (j + 1) % L] == s_before:
                match += 1
            if spins_before[i, (j - 1) % L] == s_before:
                match += 1
            # match ∈ {0..4}
            hist_joint[s_after, s_before, match] += 1
            hist_marg[s_after, s_before] += 1


# ── Compute GTE from accumulated histograms ──────────────────────────────────

def gte_from_histograms(hist_joint: np.ndarray,
                         hist_marg: np.ndarray,
                         eps: float = 1e-12) -> dict:
    """
    Plug-in entropy estimator:
        H(X) = −Σ p(x) log p(x)
        H(X | Y) = H(X, Y) − H(Y)

    G = H(X_t | X_{t-1}) − H(X_t | X_{t-1}, Y_{t-1})
      = [H(X_t, X_{t-1}) − H(X_{t-1})]
        − [H(X_t, X_{t-1}, Y_{t-1}) − H(X_{t-1}, Y_{t-1})]

    Returns dict with:
        G         : global transfer entropy (bits; via log2)
        G_nats    : in natural units (via ln)
        H_terms   : individual entropy terms for debug
        n_samples : total flip records
    """
    joint_total = hist_joint.sum()
    marg_total = hist_marg.sum()
    assert joint_total == marg_total, "histogram totals disagree"
    if joint_total == 0:
        return {"G": float("nan"), "G_nats": float("nan"),
                "H_terms": {}, "n_samples": 0}

    # Joint P(X_t, X_{t-1}, Y)
    P_xxy = hist_joint / joint_total
    P_xx = hist_marg / marg_total
    # Marginal P(X_{t-1}, Y) by summing out X_t
    P_xy = P_xxy.sum(axis=0)
    # Marginal P(X_{t-1}) by summing out X_t in P_xx (or P_xy across Y)
    P_x = P_xx.sum(axis=0)

    def H(p: np.ndarray) -> float:
        """Shannon entropy (nats) of non-negative array p; uses natural log."""
        p_pos = p[p > eps]
        return -float(np.sum(p_pos * np.log(p_pos)))

    H_xxy = H(P_xxy)
    H_xx = H(P_xx)
    H_xy = H(P_xy)
    H_x = H(P_x)

    # H(X_t | X_{t-1}) = H(X_t, X_{t-1}) − H(X_{t-1})
    H_xt_given_xp = H_xx - H_x
    # H(X_t | X_{t-1}, Y) = H(X_t, X_{t-1}, Y) − H(X_{t-1}, Y)
    H_xt_given_xpy = H_xxy - H_xy

    G_nats = H_xt_given_xp - H_xt_given_xpy
    G_bits = G_nats / np.log(2)

    return {
        "G": float(G_bits),
        "G_nats": float(G_nats),
        "H_terms": {
            "H_xxy": H_xxy,
            "H_xx": H_xx,
            "H_xy": H_xy,
            "H_x": H_x,
            "H_xt_given_xp": H_xt_given_xp,
            "H_xt_given_xpy": H_xt_given_xpy,
        },
        "n_samples": int(joint_total),
    }


# ── Convenience: run MC with GTE collection ──────────────────────────────────

def run_glauber_with_gte(
    L: int, q: int, T: float, seed: int,
    n_equil: int = 10_000, n_measure: int = 20_000,
    sample_every: int = 10, init_state: str = "disordered",
) -> dict:
    """
    Run Glauber MC and accumulate GTE per-sweep histograms.

    Extends run_glauber (in potts_mc_optimized) with GTE histogram collection
    on each measurement sweep. Returns all run_glauber outputs plus:
        gte: dict from gte_from_histograms
        hist_joint: (q, q, 5) histogram
        hist_marg: (q, q) histogram
    """
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from potts_mc_optimized import (
        _glauber_sweep_njit, _lattice_energy_njit, _magnetisation_njit,
    )

    rng = np.random.default_rng(seed)

    # Initialise lattice
    if init_state == "disordered":
        spins = rng.integers(0, q, size=(L, L), dtype=np.int64)
    elif init_state == "ordered":
        spins = np.zeros((L, L), dtype=np.int64)
    elif init_state == "half_half":
        spins = rng.integers(0, q, size=(L, L), dtype=np.int64)
        spins[L // 2:, :] = 0
    else:
        raise ValueError(f"unknown init_state: {init_state}")

    n_sweep_sites = L * L

    # Equilibration (no GTE collection)
    for _ in range(n_equil):
        ri = rng.integers(0, L, size=n_sweep_sites)
        rj = rng.integers(0, L, size=n_sweep_sites)
        rk = rng.integers(0, q, size=n_sweep_sites)
        ru = rng.random(size=n_sweep_sites)
        _glauber_sweep_njit(spins, T, q, L, ri, rj, rk, ru)

    # Measurement
    n_samples = n_measure // sample_every
    samples = np.zeros((n_samples, L, L), dtype=np.int8)
    energies = np.zeros(n_samples, dtype=np.float64)
    mags = np.zeros(n_samples, dtype=np.float64)
    sample_idx = 0

    # GTE histograms
    hist_joint = np.zeros((q, q, 5), dtype=np.int64)
    hist_marg = np.zeros((q, q), dtype=np.int64)

    for sweep in range(n_measure):
        ri = rng.integers(0, L, size=n_sweep_sites)
        rj = rng.integers(0, L, size=n_sweep_sites)
        rk = rng.integers(0, q, size=n_sweep_sites)
        ru = rng.random(size=n_sweep_sites)

        spins_before = spins.copy()
        _glauber_sweep_njit(spins, T, q, L, ri, rj, rk, ru)

        accumulate_gte_histograms(spins_before, spins, q, L,
                                  hist_joint, hist_marg)

        if sweep % sample_every == 0 and sample_idx < n_samples:
            samples[sample_idx] = spins
            energies[sample_idx] = _lattice_energy_njit(spins, L) / (L * L)
            mags[sample_idx] = _magnetisation_njit(spins, q)
            sample_idx += 1

    gte = gte_from_histograms(hist_joint, hist_marg)

    return {
        "samples": samples[:sample_idx],
        "energies": energies[:sample_idx],
        "mags": mags[:sample_idx],
        "gte": gte,
        "hist_joint": hist_joint,
        "hist_marg": hist_marg,
        "meta": {
            "L": L, "q": q, "T": T, "seed": seed,
            "n_equil": n_equil, "n_measure": n_measure,
            "sample_every": sample_every, "n_samples": sample_idx,
            "init_state": init_state,
        },
    }
