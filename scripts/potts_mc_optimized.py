"""
potts_mc_optimized.py — Glauber-dynamics 2D Potts MC with numba acceleration.

Implements the dynamics and observables needed for the CCA-vs-Brown-GTE Potts
sweep (docs/experiments/CCA_POTTS_SWEEP_SPEC.md). See
docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md for conventions.

Dynamics: Glauber single-site, P(s_i → s_k) = [1 + exp(ΔE/T)]⁻¹.
  - Matches Brown-Bossomaier-Barnett 2022 Sci. Rep. Suppl. Eq. S1.
  - Satisfies detailed balance; equilibrium distribution = canonical.

Per-flip statistics collection for GTE estimation is the caller's
responsibility via run_glauber_sweep_with_flip_log (returns per-attempt
records).

Public entry points:
  potts_tc(q)                        → exact 2D Potts T_c
  site_energy(spins, i, j, q, L)     → −J Σ δ(s_i, s_nn), computes site energy
  run_glauber(...)                   → orchestrator: equil + measurement
  compute_chi_ij(samples, q)         → q-symmetric χ_ij from config list
  compute_magnetisation(spins, q)    → dominant-mode magnetisation
"""

from __future__ import annotations

import numpy as np
from numba import njit, prange


# ── Exact critical temperature ───────────────────────────────────────────────

def potts_tc(q: int) -> float:
    """Exact critical temperature for 2D q-state Potts model."""
    return 1.0 / np.log(1.0 + np.sqrt(q))


# ── Numba-accelerated Glauber core ───────────────────────────────────────────

@njit(cache=True, fastmath=False)
def _site_energy_njit(spins: np.ndarray, i: int, j: int, L: int) -> int:
    """Per-site energy contribution: −(# matching NN) with J=1. Returns int."""
    s = spins[i, j]
    match = 0
    if spins[(i + 1) % L, j] == s:
        match += 1
    if spins[(i - 1) % L, j] == s:
        match += 1
    if spins[i, (j + 1) % L] == s:
        match += 1
    if spins[i, (j - 1) % L] == s:
        match += 1
    return -match


@njit(cache=True, fastmath=False)
def _count_matching_neighbors(spins: np.ndarray, i: int, j: int, L: int,
                              candidate: int) -> int:
    """Count NN sites matching the candidate state."""
    match = 0
    if spins[(i + 1) % L, j] == candidate:
        match += 1
    if spins[(i - 1) % L, j] == candidate:
        match += 1
    if spins[i, (j + 1) % L] == candidate:
        match += 1
    if spins[i, (j - 1) % L] == candidate:
        match += 1
    return match


@njit(cache=True, fastmath=False)
def _glauber_sweep_njit(spins: np.ndarray, T: float, q: int, L: int,
                        random_i: np.ndarray, random_j: np.ndarray,
                        random_k: np.ndarray, random_u: np.ndarray) -> None:
    """
    One Glauber sweep: L² attempted updates.
    Each attempt: pick site (i,j), pick candidate k ∈ {0..q-1}, accept with
    P = [1 + exp((E_k − E_i)/T)]⁻¹ per Brown 2022 Suppl. Eq. S1.

    Random numbers pre-generated in calling scope for numba+reproducibility.
    """
    n = L * L
    beta = 1.0 / T
    for step in range(n):
        i = random_i[step]
        j = random_j[step]
        s_old = spins[i, j]
        s_new = random_k[step]
        if s_new == s_old:
            continue
        # ΔE = E_new − E_old = −(match_new) − (−match_old) = match_old − match_new
        match_old = _count_matching_neighbors(spins, i, j, L, s_old)
        match_new = _count_matching_neighbors(spins, i, j, L, s_new)
        dE = match_old - match_new  # flipping to s_new raises E by (match_old - match_new)
        # Glauber: P(accept) = 1 / (1 + exp(β·dE))
        # Numerically stable via dE * beta only
        if dE <= 0:
            # Always lowers or equals energy → P = 1/(1 + exp(−|βdE|)) ≥ 0.5
            p_accept = 1.0 / (1.0 + np.exp(beta * dE))
        else:
            p_accept = 1.0 / (1.0 + np.exp(beta * dE))
        if random_u[step] < p_accept:
            spins[i, j] = s_new


@njit(cache=True, fastmath=False)
def _lattice_energy_njit(spins: np.ndarray, L: int) -> int:
    """Total energy: −Σ_{<i,j>} δ(s_i, s_j). Counts each bond once."""
    E = 0
    for i in range(L):
        for j in range(L):
            if spins[i, j] == spins[(i + 1) % L, j]:
                E -= 1
            if spins[i, j] == spins[i, (j + 1) % L]:
                E -= 1
    return E


@njit(cache=True, fastmath=False)
def _magnetisation_njit(spins: np.ndarray, q: int) -> float:
    """Dominant-mode magnetisation M = (q·S_m − 1)/(q − 1).
    S_m = fraction of sites in modal state.
    """
    N = spins.size
    counts = np.zeros(q, dtype=np.int64)
    for idx in range(N):
        counts[spins.flat[idx]] += 1
    S_m = counts.max() / N
    if q == 1:
        return 1.0
    return (q * S_m - 1.0) / (q - 1.0)


# ── Orchestrator (Python-level, calls numba core) ────────────────────────────

def run_glauber(
    L: int,
    q: int,
    T: float,
    seed: int,
    n_equil: int = 10_000,
    n_measure: int = 20_000,
    sample_every: int = 10,
    init_state: str = "disordered",  # "disordered" | "ordered" | "half_half"
    return_flip_log: bool = False,
) -> dict:
    """
    Run Glauber MC on 2D Potts q-state L×L torus with periodic BCs.

    Args:
        n_equil: equilibration sweeps before measurement
        n_measure: measurement sweeps
        sample_every: record one spin config every `sample_every` sweeps
        init_state:
          "disordered" — all sites random uniform (use for T ≥ T_c)
          "ordered"    — all sites = 0 (use for T ≪ T_c)
          "half_half"  — first L/2 rows random; second half = 0 (bimodal init for T ≈ T_c)

    Returns dict with:
        samples  : (n_samples, L, L) int8 array of spin configs
        energies : (n_samples,) float64 lattice energies (per-site averaged)
        mags     : (n_samples,) float64 dominant-mode magnetisations
        meta     : parameters
    """
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

    # Equilibration
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

    flip_log = [] if return_flip_log else None

    for sweep in range(n_measure):
        ri = rng.integers(0, L, size=n_sweep_sites)
        rj = rng.integers(0, L, size=n_sweep_sites)
        rk = rng.integers(0, q, size=n_sweep_sites)
        ru = rng.random(size=n_sweep_sites)

        if return_flip_log:
            # Record pre-attempt state for GTE
            # This path is slow (Python-level loop); use only for debug/small
            # configs. The GTE estimator in gte_analysis.py uses per-sweep
            # sampling (G^{(s)}) which is statistically coincident with G^{(f)}
            # per Brown 2022 Suppl.
            spins_before = spins.copy()
            _glauber_sweep_njit(spins, T, q, L, ri, rj, rk, ru)
            flip_log.append((spins_before, spins.copy()))
        else:
            _glauber_sweep_njit(spins, T, q, L, ri, rj, rk, ru)

        if sweep % sample_every == 0 and sample_idx < n_samples:
            samples[sample_idx] = spins
            energies[sample_idx] = _lattice_energy_njit(spins, L) / (L * L)
            mags[sample_idx] = _magnetisation_njit(spins, q)
            sample_idx += 1

    result = {
        "samples": samples[:sample_idx],
        "energies": energies[:sample_idx],
        "mags": mags[:sample_idx],
        "meta": {
            "L": L, "q": q, "T": T, "seed": seed,
            "n_equil": n_equil, "n_measure": n_measure,
            "sample_every": sample_every, "n_samples": sample_idx,
            "init_state": init_state,
        },
    }
    if return_flip_log:
        result["flip_log"] = flip_log
    return result


# ── Observables from sample array ────────────────────────────────────────────

def compute_chi_ij(samples: np.ndarray, q: int) -> np.ndarray:
    """
    Compute q-symmetric connected correlation matrix χ_ij = ⟨q·δ(s_i, s_j)⟩ − 1.

    Args:
        samples: (n_samples, L, L) int array of Potts states
        q: number of states

    Returns:
        χ: (N, N) float64 matrix where N = L², index convention row-major over (i,j).

    Notes:
      - This is the Borgs-Chayes 1996 Eq. 1.2 covariance matrix up to normalization.
      - Vinayak 2014 Eq. 5 predicts eigenvalue Zipf plot λ_j ~ j^{−ζ} with
        ζ = (d − η_std)/d at criticality (2D Ising: ζ = 7/8).
      - Equivalent to: χ_ij = q · P(s_i = s_j) − 1.
    """
    n_samples, L, _ = samples.shape
    N = L * L
    # Flatten spatial indices to 1D
    flat = samples.reshape(n_samples, N).astype(np.int16)
    # match_ij = # of samples where site i and site j are in same state
    # vectorized: for each sample, create an (N, N) equality matrix
    # To avoid O(N²·n_samples) memory, accumulate iteratively
    chi = np.zeros((N, N), dtype=np.float64)
    for t in range(n_samples):
        s = flat[t]
        # equality matrix: (N, N) bool, summed into chi
        chi += (s[:, None] == s[None, :]).astype(np.float64)
    chi *= q / n_samples
    chi -= 1.0
    return chi


def compute_two_point_decay(samples: np.ndarray, q: int,
                            connected: bool = True) -> tuple:
    """
    Compute r-averaged two-point correlator vs horizontal separation r,
    averaged over all site pairs at distance r and all samples.

    Raw correlator:
        C_raw(r) = ⟨q·δ(s_{i,j}, s_{i, j+r})⟩ − 1
        At r=0: = q·1 − 1 = q − 1 (always in same state)
        Plateau at large r: q·⟨m²⟩ − 1 in broken-symmetry phase, 0 otherwise

    Connected correlator (recommended for η_std fit):
        C_conn(r) = C_raw(r) − C_raw(L/2)
        Subtracts the large-r plateau; decays to 0.
        At T_c on finite L in broken phase: C_conn ~ r^{-η_std} for intermediate r

    Args:
        samples: (n_samples, L, L) int array
        q: number of Potts states
        connected: if True (default), subtract large-r plateau

    Returns:
        r_vals: (max_r + 1,) distances 0..L/2
        C_r:    (max_r + 1,) correlator at each distance

    Use for fitting η_std via C(r) ~ r^{−η_std} over intermediate r.
    """
    n_samples, L, _ = samples.shape
    max_r = L // 2
    C_r = np.zeros(max_r + 1, dtype=np.float64)
    for r in range(max_r + 1):
        matches = (samples == np.roll(samples, -r, axis=2)).astype(np.float64)
        C_r[r] = matches.mean() * q - 1.0
    r_vals = np.arange(max_r + 1, dtype=np.float64)
    if connected:
        C_r = C_r - C_r[max_r]  # subtract plateau at r = L/2
    return r_vals, C_r


def compute_magnetic_susceptibility(mags: np.ndarray, L: int) -> float:
    """
    χ_mag = L² × (⟨M²⟩ − ⟨M⟩²),
    where M is the dominant-mode magnetisation. Used for β/ν extraction.
    """
    N = L * L
    return N * (np.mean(mags ** 2) - np.mean(mags) ** 2)
