"""
reduction_check_fss.py — Analytical FSS predictions at T_c and comparison.

Per docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md §4.

Predicts η_CCA at T_c from Vinayak 2014 Eq. 5:
    λ_j ≈ c · j^{−ζ},   ζ = (d − θ)/d   (θ = η_std in 2D)

For 2D Potts q=2,3,4:
    q=2: η_std = 1/4,  ζ_theory = 7/8 = 0.875
    q=3: η_std = 4/15, ζ_theory = 13/15 ≈ 0.867
    q=4: η_std = 1/4,  ζ_theory = 7/8 = 0.875

The reduction-check tests whether η_CCA from simulation matches ζ_theory within
error bars. Outcome:
    R1 (|Δ| < 2σ) — CCA observables at T_c reduce to standard critical exponent
    R2 (|Δ| > 3σ) — CCA captures something beyond standard exponent
    ambiguous    — in between

Finite-size corrections expected: Vinayak's own L=192 Ising yields ζ_empirical
≈ 0.850 vs asymptotic 0.875. Our L ∈ {16,24,32} will show stronger corrections.
The reduction-check uses FSS extrapolation: fit ζ(L) vs 1/L, extrapolate to
L→∞, compare with ζ_theory.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass


# ── Standard 2D Potts critical exponents ─────────────────────────────────────

POTTS_2D_EXPONENTS = {
    2: {"eta_std": 1/4,   "beta_over_nu": 1/8,  "nu": 1.0,      "order": "continuous"},
    3: {"eta_std": 4/15,  "beta_over_nu": 2/15, "nu": 5/6,      "order": "continuous"},
    4: {"eta_std": 1/4,   "beta_over_nu": 1/8,  "nu": 2/3,      "order": "continuous_marginal"},
    5: {"eta_std": None,  "beta_over_nu": None, "nu": None,     "order": "first_order_weak"},
    7: {"eta_std": None,  "beta_over_nu": None, "nu": None,     "order": "first_order"},
    10: {"eta_std": None, "beta_over_nu": None, "nu": None,     "order": "first_order_strong"},
}


def zeta_theory(q: int, d: int = 2) -> float | None:
    """
    Vinayak 2014 Eq. 5 prediction: ζ = (d − θ)/d where θ = η_std in 2D.

    Returns None for first-order q (Vinayak framework doesn't apply).
    """
    exp = POTTS_2D_EXPONENTS.get(q)
    if exp is None or exp["eta_std"] is None:
        return None
    return (d - exp["eta_std"]) / d


# ── Reduction-check outcome classification ───────────────────────────────────

@dataclass
class ReductionCheckResult:
    q: int
    L: int
    eta_CCA_measured: float
    eta_CCA_sem: float
    zeta_theory: float
    deviation_sigma: float      # |measured − theory| / sem
    outcome: str                # "R1" | "R2" | "ambiguous" | "N/A_first_order"
    rationale: str


def classify_reduction(q: int, L: int, eta_CCA_mean: float,
                        eta_CCA_sem: float) -> ReductionCheckResult:
    """
    Decision rule from DERIVATIONS §4.4.1:
        |Δ/σ| < 2 → R1 (reduction confirmed)
        |Δ/σ| > 3 → R2 (something else)
        else       → ambiguous
    """
    zt = zeta_theory(q)
    if zt is None:
        return ReductionCheckResult(
            q=q, L=L, eta_CCA_measured=eta_CCA_mean, eta_CCA_sem=eta_CCA_sem,
            zeta_theory=float("nan"), deviation_sigma=float("nan"),
            outcome="N/A_first_order",
            rationale=f"q={q} is first-order in 2D; Vinayak framework not applicable.",
        )
    dev = abs(eta_CCA_mean - zt) / max(eta_CCA_sem, 1e-6)
    if dev < 2.0:
        outcome = "R1"
        rationale = (f"|η_CCA − ζ_theory| = {abs(eta_CCA_mean-zt):.3f} < 2σ "
                     f"({2*eta_CCA_sem:.3f}); reduction confirmed at L={L}.")
    elif dev > 3.0:
        outcome = "R2"
        rationale = (f"|η_CCA − ζ_theory| = {abs(eta_CCA_mean-zt):.3f} > 3σ "
                     f"({3*eta_CCA_sem:.3f}); CCA captures beyond η_std.")
    else:
        outcome = "ambiguous"
        rationale = (f"|η_CCA − ζ_theory| = {abs(eta_CCA_mean-zt):.3f} in "
                     f"[2σ, 3σ]; ambiguous — report finite-size extrapolation.")
    return ReductionCheckResult(
        q=q, L=L, eta_CCA_measured=eta_CCA_mean, eta_CCA_sem=eta_CCA_sem,
        zeta_theory=zt, deviation_sigma=dev, outcome=outcome, rationale=rationale,
    )


# ── FSS extrapolation helper ──────────────────────────────────────────────────

def extrapolate_zeta_Linf(Ls: np.ndarray, zetas: np.ndarray,
                           zetas_sem: np.ndarray) -> dict:
    """
    FSS extrapolation: fit ζ(L) = ζ_∞ + a/L^c form, linear in 1/L for simplicity.
    Returns extrapolated zeta at L → ∞ with uncertainty.

    Args:
        Ls: array of lattice sizes
        zetas: mean η_CCA at T_c for each L
        zetas_sem: standard errors

    Returns dict with zeta_inf, zeta_inf_sem, slope, intercept.
    """
    inv_L = 1.0 / np.asarray(Ls, dtype=np.float64)
    mask = np.isfinite(zetas) & (zetas_sem > 0)
    if mask.sum() < 2:
        return {"zeta_inf": float("nan"), "zeta_inf_sem": float("nan"),
                "slope": float("nan"), "intercept": float("nan"),
                "n_points": int(mask.sum())}
    x = inv_L[mask]
    y = np.asarray(zetas)[mask]
    w = 1.0 / np.asarray(zetas_sem)[mask] ** 2
    # Weighted linear regression: y = a + b·x, intercept a = zeta_inf
    W = np.diag(w)
    X = np.vstack([np.ones_like(x), x]).T
    XtWX = X.T @ W @ X
    XtWy = X.T @ W @ y
    coefs = np.linalg.solve(XtWX, XtWy)
    cov = np.linalg.inv(XtWX)
    intercept = float(coefs[0])
    slope = float(coefs[1])
    intercept_sem = float(np.sqrt(cov[0, 0]))
    return {"zeta_inf": intercept, "zeta_inf_sem": intercept_sem,
            "slope": slope, "intercept": intercept,
            "n_points": int(mask.sum())}


if __name__ == "__main__":
    print("2D Potts critical exponents and Vinayak ζ_theory predictions:")
    print(f"{'q':>3} | {'η_std':>8} | {'β/ν':>8} | {'ν':>6} | {'ζ_theory':>9} | order")
    print("-" * 60)
    for q in [2, 3, 4, 5, 7, 10]:
        exp = POTTS_2D_EXPONENTS[q]
        zt = zeta_theory(q)
        eta = f"{exp['eta_std']:.4f}" if exp["eta_std"] is not None else "—"
        bn = f"{exp['beta_over_nu']:.4f}" if exp["beta_over_nu"] is not None else "—"
        nu = f"{exp['nu']:.4f}" if exp["nu"] is not None else "—"
        zt_s = f"{zt:.4f}" if zt is not None else "—"
        print(f"{q:>3} | {eta:>8} | {bn:>8} | {nu:>6} | {zt_s:>9} | {exp['order']}")
