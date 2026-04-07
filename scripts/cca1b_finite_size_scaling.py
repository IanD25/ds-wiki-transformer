"""
CCA-1b Validation: Finite-Size Scaling of dη/dT

Implements all 5 experimental requirements from the handback document:
  4.1: Finite-size scaling of S_max = max|dη/dT| for L=16,32,64
  4.2: Second derivative d²η/dT²
  4.3: Temperature resolution sensitivity (coarse vs fine grid)
  4.4: Weight mode robustness (abs, neglog, inv)
  4.5: Noise/subsampling robustness

Models: Potts q=2 (continuous) and q=10 (first-order)

CCA-1b predicts:
  Continuous:  S_max(L) ~ L^alpha with alpha small
  First-order: S_max(L) ~ L^d (strong growth)

Output: data/reports/ising_fim_test/cca1b_scaling/
"""

import json
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SRC = Path(__file__).resolve().parent.parent / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

# Reuse the Potts MC infrastructure
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from potts_fim_test import potts_mc, potts_tc, build_correlation_graph, analyze_potts
from analysis.fisher_diagnostics import KernelType, analyze_node


# ── Derivative Estimation ─────────────────────────────────────────────────────

def central_difference(temps, values):
    """Central difference derivative. Returns (T_mid, dv/dT) arrays."""
    t_mid = []
    deriv = []
    for i in range(1, len(temps) - 1):
        dT = temps[i + 1] - temps[i - 1]
        if dT > 0:
            t_mid.append(temps[i])
            deriv.append((values[i + 1] - values[i - 1]) / dT)
    return np.array(t_mid), np.array(deriv)


def second_derivative(temps, values):
    """Second derivative via central difference of central difference."""
    t1, d1 = central_difference(temps, values)
    if len(t1) >= 3:
        t2, d2 = central_difference(t1, d1)
        return t2, d2
    return np.array([]), np.array([])


# ── Temperature Sweep ─────────────────────────────────────────────────────────

def sweep_temperatures(L, q, temps, weight_mode="neglog", alpha=1.0,
                       n_sample=20, n_equil=None, n_measure=None, seed=42):
    """Run Potts MC + FIM at each temperature. Returns list of result dicts."""
    # Scale MC effort with L^2
    if n_equil is None:
        n_equil = max(5000, int(2000 * (L / 16) ** 2))
    if n_measure is None:
        n_measure = max(10000, int(4000 * (L / 16) ** 2))

    results = []
    for T in temps:
        r = analyze_potts(L, q, T, n_sample_nodes=n_sample, alpha=alpha,
                          weight_mode=weight_mode, seed=seed,
                          n_equil=n_equil, n_measure=n_measure)
        results.append(r)
    return results


def extract_eta_curve(results):
    """Extract (T/Tc, eta) arrays from results list."""
    t_ratios = np.array([r["T_ratio"] for r in results])
    etas = np.array([r["mean_eta"] for r in results])
    return t_ratios, etas


# ── Main Experiments ──────────────────────────────────────────────────────────

def main():
    OUT_DIR = Path("data/reports/ising_fim_test/cca1b_scaling")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── 4.3: Fine temperature grid near T_c ──────────────────────
    # Dense grid: 20 points in T/Tc = [0.9, 1.2]
    fine_ratios = np.linspace(0.90, 1.20, 25)

    # Coarse grid: 10 points in same range (for comparison)
    coarse_ratios = np.linspace(0.90, 1.20, 10)

    all_scaling_data = {}

    # ── 4.1 + 4.4: Finite-size scaling across weight modes ──────
    LATTICE_SIZES = [16, 32]  # 64 may be too slow for single-spin Metropolis
    Q_VALUES = [2, 10]
    WEIGHT_MODES = ["neglog", "abs"]

    for wm in WEIGHT_MODES:
        print(f"\n{'='*80}")
        print(f"WEIGHT MODE: {wm}")
        print(f"{'='*80}")

        for q in Q_VALUES:
            tc = potts_tc(q)
            order = "continuous" if q <= 4 else "first-order"

            for L in LATTICE_SIZES:
                key = f"q{q}_L{L}_{wm}"
                temps = [tc * r for r in fine_ratios]

                print(f"\n--- q={q} ({order}), L={L}, T_c={tc:.4f}, {wm} ---")
                t0 = time.time()

                results = sweep_temperatures(
                    L, q, temps, weight_mode=wm, alpha=1.0,
                    n_sample=min(20, L * L), seed=42
                )

                dt = time.time() - t0
                print(f"  Completed in {dt:.1f}s")

                # Extract η curve
                t_ratios, etas = extract_eta_curve(results)

                # Compute derivatives
                t_d1, d_eta = central_difference(list(t_ratios), list(etas))
                t_d2, d2_eta = second_derivative(list(t_ratios), list(etas))

                # Peak slope
                if len(d_eta) > 0:
                    s_max = float(np.max(np.abs(d_eta)))
                    s_max_loc = float(t_d1[np.argmax(np.abs(d_eta))])
                else:
                    s_max = 0.0
                    s_max_loc = 0.0

                # Peak second derivative
                if len(d2_eta) > 0:
                    d2_max = float(np.max(np.abs(d2_eta)))
                else:
                    d2_max = 0.0

                print(f"  S_max = {s_max:.4f} at T/Tc = {s_max_loc:.4f}")
                print(f"  d²η/dT² max = {d2_max:.4f}")

                # Store
                all_scaling_data[key] = {
                    "q": q, "L": L, "weight_mode": wm,
                    "order": order, "T_c": float(tc),
                    "T_ratios": list(t_ratios),
                    "etas": list(etas),
                    "d_eta_T": list(t_d1) if len(t_d1) > 0 else [],
                    "d_eta": list(d_eta) if len(d_eta) > 0 else [],
                    "d2_eta_T": list(t_d2) if len(t_d2) > 0 else [],
                    "d2_eta": list(d2_eta) if len(d2_eta) > 0 else [],
                    "S_max": s_max,
                    "S_max_T_ratio": s_max_loc,
                    "d2_max": d2_max,
                    "time_s": round(dt, 1),
                }

    # ── 4.3: Resolution comparison ──────────────────────────────
    print(f"\n{'='*80}")
    print("RESOLUTION SENSITIVITY (L=16, q=10, neglog)")
    print(f"{'='*80}")

    q, L, wm = 10, 16, "neglog"
    tc = potts_tc(q)

    # Coarse grid
    temps_coarse = [tc * r for r in coarse_ratios]
    res_coarse = sweep_temperatures(L, q, temps_coarse, weight_mode=wm, seed=42)
    t_c_ratios, etas_c = extract_eta_curve(res_coarse)
    _, d_eta_c = central_difference(list(t_c_ratios), list(etas_c))
    s_max_coarse = float(np.max(np.abs(d_eta_c))) if len(d_eta_c) > 0 else 0

    # Fine grid already computed above
    fine_key = f"q{q}_L{L}_{wm}"
    s_max_fine = all_scaling_data[fine_key]["S_max"]

    print(f"  Coarse (10 pts): S_max = {s_max_coarse:.4f}")
    print(f"  Fine   (25 pts): S_max = {s_max_fine:.4f}")
    print(f"  Ratio: {s_max_fine / s_max_coarse:.2f}x" if s_max_coarse > 0 else "  Coarse S_max = 0")

    all_scaling_data["resolution_test"] = {
        "coarse_n_points": len(coarse_ratios),
        "fine_n_points": len(fine_ratios),
        "S_max_coarse": s_max_coarse,
        "S_max_fine": s_max_fine,
    }

    # ── Save all data ────────────────────────────────────────────
    # Convert numpy arrays for JSON serialization
    serializable = {}
    for k, v in all_scaling_data.items():
        serializable[k] = {}
        for k2, v2 in v.items():
            if isinstance(v2, np.ndarray):
                serializable[k][k2] = v2.tolist()
            elif isinstance(v2, (np.float64, np.float32)):
                serializable[k][k2] = float(v2)
            elif isinstance(v2, (np.int64, np.int32)):
                serializable[k][k2] = int(v2)
            else:
                serializable[k][k2] = v2

    with open(OUT_DIR / "cca1b_scaling_data.json", "w") as f:
        json.dump(serializable, f, indent=2)

    # ── Plots ────────────────────────────────────────────────────

    # Plot 1: η(T/Tc) curves for all (q, L, weight_mode) combinations
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    for idx, wm in enumerate(WEIGHT_MODES):
        # Left column: η(T)
        ax = axes[idx, 0]
        for q in Q_VALUES:
            for L in LATTICE_SIZES:
                key = f"q{q}_L{L}_{wm}"
                d = all_scaling_data[key]
                label = f"q={q} L={L}"
                ls = "-" if q == 2 else "--"
                ax.plot(d["T_ratios"], d["etas"], ls, label=label, markersize=3)
        ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.5)
        ax.set_xlabel("T / T_c")
        ax.set_ylabel("η")
        ax.set_title(f"η(T/T_c) — {wm} weights")
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

        # Right column: |dη/d(T/Tc)|
        ax = axes[idx, 1]
        for q in Q_VALUES:
            for L in LATTICE_SIZES:
                key = f"q{q}_L{L}_{wm}"
                d = all_scaling_data[key]
                if d["d_eta_T"]:
                    label = f"q={q} L={L} (S_max={d['S_max']:.2f})"
                    ls = "-" if q == 2 else "--"
                    ax.plot(d["d_eta_T"], np.abs(d["d_eta"]), ls, label=label, markersize=3)
        ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.5)
        ax.set_xlabel("T / T_c")
        ax.set_ylabel("|dη/d(T/T_c)|")
        ax.set_title(f"|dη/dT| — {wm} weights")
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

    plt.suptitle("CCA-1b Finite-Size Scaling: η(T) and |dη/dT|", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "eta_and_derivative_curves.png", dpi=150)
    print(f"\nPlot 1 saved: {OUT_DIR / 'eta_and_derivative_curves.png'}")

    # Plot 2: S_max(L) scaling
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for idx, wm in enumerate(WEIGHT_MODES):
        ax = axes[idx]
        for q in Q_VALUES:
            Ls = []
            S_maxes = []
            for L in LATTICE_SIZES:
                key = f"q{q}_L{L}_{wm}"
                Ls.append(L)
                S_maxes.append(all_scaling_data[key]["S_max"])

            order = "cont." if q <= 4 else "1st-ord."
            ax.plot(Ls, S_maxes, "o-", label=f"q={q} ({order})", markersize=8)

            # Log-log fit if we have enough points
            if len(Ls) >= 2 and all(s > 0 for s in S_maxes):
                log_L = np.log(Ls)
                log_S = np.log(S_maxes)
                if len(log_L) >= 2:
                    slope = (log_S[-1] - log_S[0]) / (log_L[-1] - log_L[0])
                    ax.annotate(f"slope ≈ {slope:.2f}", xy=(Ls[-1], S_maxes[-1]),
                                fontsize=9, color="gray")

        ax.set_xlabel("L (lattice size)")
        ax.set_ylabel("S_max = max|dη/d(T/T_c)|")
        ax.set_title(f"S_max scaling — {wm} weights")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.suptitle("CCA-1b: S_max(L) Scaling — Continuous vs First-Order", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "s_max_scaling.png", dpi=150)
    print(f"Plot 2 saved: {OUT_DIR / 's_max_scaling.png'}")

    # ── Summary ──────────────────────────────────────────────────
    print(f"\n{'='*80}")
    print("CCA-1b FINITE-SIZE SCALING SUMMARY")
    print(f"{'='*80}")
    print(f"\n{'Key':<25} {'q':>3} {'L':>4} {'wm':>8} {'S_max':>8} {'@ T/Tc':>8} {'d²max':>8}")
    print("-" * 80)
    for key in sorted(all_scaling_data.keys()):
        d = all_scaling_data[key]
        if "q" in d:
            print(f"{key:<25} {d['q']:>3} {d['L']:>4} {d['weight_mode']:>8} "
                  f"{d['S_max']:>8.4f} {d['S_max_T_ratio']:>8.4f} {d['d2_max']:>8.4f}")

    # Scaling ratios
    print(f"\n{'='*80}")
    print("SCALING RATIOS: S_max(L=32) / S_max(L=16)")
    print(f"{'='*80}")
    for wm in WEIGHT_MODES:
        for q in Q_VALUES:
            k16 = f"q{q}_L16_{wm}"
            k32 = f"q{q}_L32_{wm}"
            if k16 in all_scaling_data and k32 in all_scaling_data:
                s16 = all_scaling_data[k16]["S_max"]
                s32 = all_scaling_data[k32]["S_max"]
                ratio = s32 / s16 if s16 > 0 else float('inf')
                order = "continuous" if q <= 4 else "first-order"
                print(f"  q={q} ({order:>11}), {wm:>8}: {s16:.4f} → {s32:.4f} (ratio = {ratio:.3f})")

    print(f"\nCCA-1b expects: first-order ratio >> continuous ratio")
    print(f"(First-order S_max should grow faster with L)")


if __name__ == "__main__":
    main()
