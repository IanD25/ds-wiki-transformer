"""
cca_observables.py — Extract d_eff_CCA, η_CCA, η_std, β/ν from correlation matrix + samples.

Conventions per docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md §3, §4.

  d_eff_CCA: participation ratio (Σλ)²/Σλ², spec §3.4 #3
  η_CCA:     Zipf-tail exponent from λ_j ~ j^{−η_CCA} fit, spec §3.4 #4
  η_std:     standard stat-mech anomalous dimension from C(r) ~ r^{−η_std}
  β/ν:       from |⟨m⟩| ~ L^{−β/ν} FSS of dominant-mode magnetisation
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass, asdict


# ── CCA scalar observables from χ spectrum ───────────────────────────────────

@dataclass
class CCAObservables:
    """Output of extract_cca_observables; spec §3.4 Observable Set A."""
    d_eff_CCA: float         # (Σλ)² / Σλ², spec §3.4 #3
    eta_CCA: float           # Zipf exponent, spec §3.4 #4 — fitted
    eta_CCA_r2: float        # goodness of fit (R²) for eta_CCA
    eta_CCA_range: tuple     # (j_min, j_max) used for fit
    lambda_max: float        # λ_1 — dominant eigenvalue
    n_positive_eig: int      # count of λ > threshold
    spectrum_sum: float      # Σλ (should equal tr(χ))
    spectrum_sum_sq: float   # Σλ²


def extract_cca_observables(
    chi: np.ndarray,
    j_min_frac: float = 0.04,  # j_min = max(5, j_min_frac · N)
    j_max_frac: float = 0.5,   # j_max = j_max_frac · N
    j_min_absolute: int = 5,
    eps: float = 1e-10,
) -> CCAObservables:
    """
    Extract CCA scalar observables from a connected correlation matrix χ.

    Args:
        chi: (N, N) real symmetric matrix (eigvalsh expected to be real)
        j_min_frac, j_max_frac: Zipf-fit index range as fractions of N
        j_min_absolute: minimum absolute j_min (avoid finite-size corrections at top)
        eps: relative threshold for "positive" eigenvalue

    Returns: CCAObservables dataclass
    """
    N = chi.shape[0]
    # Use eigvalsh for symmetric matrix → real eigenvalues, ascending order
    eigvals = np.linalg.eigvalsh(chi)
    # Sort descending
    eigvals = np.sort(eigvals)[::-1]

    # Clip small/negative eigenvalues (numerical noise) to zero for PR
    thr = eps * max(eigvals[0], 1.0)
    positive = eigvals[eigvals > thr]
    n_positive = len(positive)

    # Participation ratio (all positive eigenvalues)
    s1 = positive.sum()
    s2 = (positive ** 2).sum()
    d_eff = float(s1 ** 2 / s2) if s2 > 0 else 1.0

    # Zipf fit: log(λ_j) = log(c) − η_CCA · log(j) for j ∈ [j_min, j_max]
    j_min = max(j_min_absolute, int(j_min_frac * N))
    j_max = min(int(j_max_frac * N), n_positive)
    if j_max - j_min < 5:
        # Too few eigenvalues to fit — return NaN
        eta_cca = float("nan")
        eta_cca_r2 = float("nan")
    else:
        js = np.arange(j_min, j_max + 1, dtype=np.float64)  # inclusive
        lambdas = positive[j_min - 1: j_max]  # 1-indexed → 0-indexed slice
        # log-log fit
        log_j = np.log(js)
        log_lam = np.log(np.maximum(lambdas, thr))
        # linear regression
        slope, intercept = np.polyfit(log_j, log_lam, 1)
        eta_cca = float(-slope)
        # R² goodness
        residuals = log_lam - (slope * log_j + intercept)
        ss_res = (residuals ** 2).sum()
        ss_tot = ((log_lam - log_lam.mean()) ** 2).sum()
        eta_cca_r2 = float(1 - ss_res / ss_tot) if ss_tot > 0 else 0.0

    return CCAObservables(
        d_eff_CCA=d_eff,
        eta_CCA=eta_cca,
        eta_CCA_r2=eta_cca_r2,
        eta_CCA_range=(j_min, j_max),
        lambda_max=float(eigvals[0]),
        n_positive_eig=n_positive,
        spectrum_sum=float(s1),
        spectrum_sum_sq=float(s2),
    )


# ── Standard critical exponents from samples ─────────────────────────────────

def fit_eta_std(r_vals: np.ndarray, C_r: np.ndarray,
                r_min: int = 2, r_max: int = None) -> dict:
    """
    Fit standard η_std from C(r) ~ r^{−η_std} at criticality.

    For 2D, standard result: C(r) ~ r^{−(d − 2 + η)} = r^{−η_std} (since d=2).

    Args:
        r_vals: distances (0..L/2)
        C_r: CONNECTED correlator at each r (use connected=True from compute_two_point_decay)
        r_min: min distance for fit (avoid short-range lattice effects)
        r_max: max distance for fit; defaults to L/2 − 2 (skip plateau tail)

    Returns: dict with 'eta_std', 'r2', 'range', 'n_points'
    """
    if r_max is None:
        r_max = len(r_vals) - 2  # skip r=0 and the plateau at r=L/2
    r_fit = r_vals[r_min:r_max + 1]
    C_fit = C_r[r_min:r_max + 1]
    mask = C_fit > 0  # connected should be positive in the decaying region
    if mask.sum() < 3:
        return {"eta_std": float("nan"), "r2": float("nan"),
                "range": (r_min, r_max), "n_points": int(mask.sum())}
    slope, intercept = np.polyfit(np.log(r_fit[mask]), np.log(C_fit[mask]), 1)
    eta_std = float(-slope)
    residuals = np.log(C_fit[mask]) - (slope * np.log(r_fit[mask]) + intercept)
    ss_res = (residuals ** 2).sum()
    ss_tot = ((np.log(C_fit[mask]) - np.log(C_fit[mask]).mean()) ** 2).sum()
    r2 = float(1 - ss_res / ss_tot) if ss_tot > 0 else 0.0
    return {"eta_std": eta_std, "r2": r2,
            "range": (r_min, r_max), "n_points": int(mask.sum())}


def extract_all_observables(samples: np.ndarray, mags: np.ndarray,
                            energies: np.ndarray, q: int, L: int) -> dict:
    """
    Convenience wrapper: compute all observables used in the sweep.

    Returns dict ready for CSV export.
    """
    from potts_mc_optimized import compute_chi_ij, compute_two_point_decay, compute_magnetic_susceptibility

    chi = compute_chi_ij(samples, q=q)
    cca = extract_cca_observables(chi)
    r_vals, C_r = compute_two_point_decay(samples, q=q)
    eta_std_fit = fit_eta_std(r_vals, C_r, L=L)
    chi_mag = compute_magnetic_susceptibility(mags, L)

    out = {
        **asdict(cca),
        "eta_std": eta_std_fit["eta_std"],
        "eta_std_r2": eta_std_fit["r2"],
        "eta_std_range": eta_std_fit["range"],
        "magnetisation_mean": float(mags.mean()),
        "magnetisation_std": float(mags.std()),
        "magnetisation_sq_mean": float((mags ** 2).mean()),
        "chi_mag": float(chi_mag),
        "energy_mean": float(energies.mean()),
        "energy_std": float(energies.std()),
        "q": q,
        "L": L,
        "n_samples": len(samples),
    }
    # Save eigenspectrum separately (not in main dict; stored per-run in raw/)
    out["_spectrum"] = np.linalg.eigvalsh(chi)[::-1]  # descending
    out["_C_r"] = C_r
    return out
