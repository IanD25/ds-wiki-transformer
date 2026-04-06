"""
Phase B: 2D Ising Monte Carlo — FIM Isotropy at Criticality

Metropolis-Hastings simulation of 2D Ising model on L×L torus.
Computes spin-spin correlations at each temperature, uses them as
edge weights in the FIM graph, and measures (d_eff, η, rho_CCA).

CCA prediction: at T_c = 2/ln(1+√2) ≈ 2.269 (Onsager exact),
the FIM should show BOTH high d_eff AND high η — the joint signature
that Phase A identified as the true CCA diagnostic.

Below T_c: ordered phase → uniform correlations → low d_eff (flat landscape)
At T_c: power-law correlations → scale-free → peak d_eff + high η
Above T_c: disordered → weak correlations → noisy/degenerate

Output: data/reports/ising_fim_test/mc_temperature_sweep.json + PNG plots
"""

import json
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

SRC = Path(__file__).resolve().parent.parent / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from analysis.fisher_diagnostics import (
    KernelType, analyze_node
)


# ── Ising Monte Carlo (numpy-only) ───────────────────────────────────────────

T_C = 2.0 / np.log(1.0 + np.sqrt(2.0))  # 2.26919...


def ising_mc(L: int, T: float, n_equil: int = 5000, n_measure: int = 10000,
             sample_every: int = 10, seed: int = 42) -> np.ndarray:
    """
    Metropolis-Hastings Ising simulation on L×L torus.

    Returns:
        correlations: L×L×L×L array where correlations[i,j,k,l] = <s_{i,j} s_{k,l}>
                      averaged over measurement sweeps.
        (Only neighbor correlations are used, but full array enables diagnostics.)
    """
    rng = np.random.RandomState(seed)

    # Initialize random spin configuration
    spins = rng.choice([-1, 1], size=(L, L))

    beta = 1.0 / T

    # Pre-compute neighbor indices (periodic BC)
    # For each site (i,j), neighbors are (i±1,j) and (i,j±1) mod L

    # Equilibration
    for sweep in range(n_equil):
        _metropolis_sweep(spins, beta, L, rng)

    # Measurement: accumulate <s_i * s_j> for nearest-neighbor pairs
    # Store as edge-level correlations for efficiency
    n_samples = 0
    # Accumulate correlation for each nearest-neighbor edge
    # Edges: horizontal (i,j)-(i,(j+1)%L) and vertical (i,j)-((i+1)%L,j)
    corr_h = np.zeros((L, L), dtype=np.float64)  # horizontal edges
    corr_v = np.zeros((L, L), dtype=np.float64)  # vertical edges

    for sweep in range(n_measure):
        _metropolis_sweep(spins, beta, L, rng)
        if sweep % sample_every == 0:
            # Horizontal: s[i,j] * s[i, (j+1)%L]
            corr_h += spins * np.roll(spins, -1, axis=1)
            # Vertical: s[i,j] * s[(i+1)%L, j]
            corr_v += spins * np.roll(spins, -1, axis=0)
            n_samples += 1

    corr_h /= n_samples
    corr_v /= n_samples

    return corr_h, corr_v


def _metropolis_sweep(spins: np.ndarray, beta: float, L: int, rng):
    """One full Metropolis sweep (L*L single-spin flips)."""
    for _ in range(L * L):
        i = rng.randint(0, L)
        j = rng.randint(0, L)
        s = spins[i, j]
        # Sum of neighbors
        nn_sum = (spins[(i + 1) % L, j] + spins[(i - 1) % L, j] +
                  spins[i, (j + 1) % L] + spins[i, (j - 1) % L])
        dE = 2 * s * nn_sum  # J=1
        if dE <= 0 or rng.random() < np.exp(-beta * dE):
            spins[i, j] = -s


# ── Graph Construction from Correlations ──────────────────────────────────────

def build_correlation_graph(corr_h: np.ndarray, corr_v: np.ndarray, L: int,
                            weight_mode: str = "abs") -> nx.Graph:
    """
    Build NetworkX graph from Ising correlations.

    weight_mode:
        "abs"     : w_ij = |<s_i s_j>|  (0 to 1, higher = more correlated)
        "neglog"  : w_ij = -log(|<s_i s_j>| + eps)  (distance-like, lower = more correlated)
        "inv"     : w_ij = 1 / (|<s_i s_j>| + eps)  (distance-like)
    """
    G = nx.Graph()

    # Add nodes
    for i in range(L):
        for j in range(L):
            G.add_node(f"n_{i}_{j}")

    eps = 1e-8

    for i in range(L):
        for j in range(L):
            # Horizontal edge: (i,j) - (i, (j+1)%L)
            j2 = (j + 1) % L
            c = abs(corr_h[i, j])
            w = _compute_weight(c, weight_mode, eps)
            G.add_edge(f"n_{i}_{j}", f"n_{i}_{j2}", weight=w)

            # Vertical edge: (i,j) - ((i+1)%L, j)
            i2 = (i + 1) % L
            c = abs(corr_v[i, j])
            w = _compute_weight(c, weight_mode, eps)
            G.add_edge(f"n_{i}_{j}", f"n_{i2}_{j}", weight=w)

    return G


def _compute_weight(c: float, mode: str, eps: float) -> float:
    if mode == "abs":
        return max(c, eps)
    elif mode == "neglog":
        return -np.log(max(c, eps))
    elif mode == "inv":
        return 1.0 / max(c, eps)
    else:
        return max(c, eps)


# ── FIM Analysis ──────────────────────────────────────────────────────────────

def analyze_ising_at_temperature(L: int, T: float, n_sample_nodes: int = 20,
                                 alpha: float = 1.0, weight_mode: str = "neglog",
                                 seed: int = 42) -> dict:
    """
    Full pipeline: MC simulation → correlation graph → FIM analysis.
    """
    t0 = time.time()

    # Run MC
    corr_h, corr_v = ising_mc(L, T, seed=seed)
    t_mc = time.time() - t0

    # Build graph
    G = build_correlation_graph(corr_h, corr_v, L, weight_mode=weight_mode)

    # Sample nodes for FIM analysis
    nodes = list(G.nodes())
    rng = np.random.RandomState(seed + 1)
    if len(nodes) > n_sample_nodes:
        sampled = list(rng.choice(nodes, size=n_sample_nodes, replace=False))
    else:
        sampled = nodes

    # Analyze each node
    etas = []
    d_effs = []
    prs = []
    sv_mins = []
    regimes = {"radial_dominated": 0, "isotropic": 0, "noise_dominated": 0, "degenerate": 0}

    for node in sampled:
        r = analyze_node(G, str(node), KernelType.EXPONENTIAL, alpha=alpha)
        if r.skipped:
            regimes["degenerate"] += 1
            continue
        etas.append(r.eta)
        d_effs.append(r.d_eff)
        prs.append(r.pr)
        if len(r.sv_profile) > 1:
            sv_mins.append(min(r.sv_profile))
        else:
            sv_mins.append(1.0)
        regimes[r.regime.value] += 1

    dt = time.time() - t0

    # Correlation statistics
    all_corr = np.concatenate([corr_h.ravel(), corr_v.ravel()])
    mean_corr = float(np.mean(np.abs(all_corr)))
    std_corr = float(np.std(np.abs(all_corr)))

    result = {
        "L": L,
        "T": T,
        "T_c": float(T_C),
        "T_ratio": T / T_C,
        "n_nodes": L * L,
        "n_sampled": len(sampled),
        "n_valid": len(etas),
        "mean_eta": float(np.mean(etas)) if etas else 0.0,
        "std_eta": float(np.std(etas)) if etas else 0.0,
        "mean_d_eff": float(np.mean(d_effs)) if d_effs else 0.0,
        "std_d_eff": float(np.std(d_effs)) if d_effs else 0.0,
        "mean_pr": float(np.mean(prs)) if prs else 0.0,
        "mean_rho_cca": float(np.mean(sv_mins)) if sv_mins else 0.0,
        "regime_counts": regimes,
        "mean_abs_correlation": mean_corr,
        "std_abs_correlation": std_corr,
        "alpha": alpha,
        "weight_mode": weight_mode,
        "time_mc_s": round(t_mc, 2),
        "time_total_s": round(dt, 2),
    }

    return result


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    OUT_DIR = Path("data/reports/ising_fim_test")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Temperature sweep
    TEMPERATURES = [1.5, 1.8, 2.0, 2.1, 2.2, 2.269, 2.3, 2.4, 2.6, 3.0, 4.0]

    L = 16  # 256 spins — fast enough for numpy MC
    ALPHA = 1.0
    WEIGHT_MODE = "neglog"  # -log(|corr|) as distance

    print(f"2D Ising MC: L={L}, T_c={T_C:.5f}")
    print(f"Weight mode: {WEIGHT_MODE}, FIM alpha: {ALPHA}")
    print(f"Temperatures: {TEMPERATURES}")
    print(f"{'='*80}")

    all_results = []

    for T in TEMPERATURES:
        print(f"\n--- T = {T:.3f} (T/T_c = {T/T_C:.3f}) ---")
        result = analyze_ising_at_temperature(
            L=L, T=T, n_sample_nodes=25, alpha=ALPHA,
            weight_mode=WEIGHT_MODE, seed=42
        )
        all_results.append(result)

        marker = " *** CRITICAL ***" if abs(T - T_C) < 0.01 else ""
        print(f"  η={result['mean_eta']:.4f}  d_eff={result['mean_d_eff']:.2f}  "
              f"PR={result['mean_pr']:.3f}  rho_CCA={result['mean_rho_cca']:.4f}  "
              f"|corr|={result['mean_abs_correlation']:.4f}{marker}  "
              f"({result['time_total_s']:.1f}s)")
        print(f"  Regimes: {result['regime_counts']}")

    # Also run with different weight modes for comparison
    print(f"\n{'='*80}")
    print("Weight mode comparison at T_c:")
    for wm in ["abs", "neglog", "inv"]:
        r = analyze_ising_at_temperature(L=L, T=T_C, n_sample_nodes=25,
                                          alpha=ALPHA, weight_mode=wm, seed=42)
        print(f"  {wm:>8}: η={r['mean_eta']:.4f}  d_eff={r['mean_d_eff']:.2f}  "
              f"PR={r['mean_pr']:.3f}  rho_CCA={r['mean_rho_cca']:.4f}")

    # Also try different alpha at T_c
    print(f"\nAlpha comparison at T_c (weight={WEIGHT_MODE}):")
    for alpha in [0.25, 0.5, 1.0, 2.0, 3.0]:
        r = analyze_ising_at_temperature(L=L, T=T_C, n_sample_nodes=25,
                                          alpha=alpha, weight_mode=WEIGHT_MODE, seed=42)
        print(f"  α={alpha:.2f}: η={r['mean_eta']:.4f}  d_eff={r['mean_d_eff']:.2f}  "
              f"PR={r['mean_pr']:.3f}  rho_CCA={r['mean_rho_cca']:.4f}")

    # Save primary results
    with open(OUT_DIR / "mc_temperature_sweep.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {OUT_DIR / 'mc_temperature_sweep.json'}")

    # --- Plots ---
    temps = [r["T"] for r in all_results]
    etas = [r["mean_eta"] for r in all_results]
    d_effs = [r["mean_d_eff"] for r in all_results]
    prs = [r["mean_pr"] for r in all_results]
    rho_ccas = [r["mean_rho_cca"] for r in all_results]
    corrs = [r["mean_abs_correlation"] for r in all_results]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Top left: η vs T
    ax = axes[0, 0]
    ax.plot(temps, etas, "o-", color="tab:blue", markersize=6)
    ax.axvline(x=T_C, color="red", linestyle="--", alpha=0.7, label=f"T_c={T_C:.3f}")
    ax.set_xlabel("Temperature T")
    ax.set_ylabel("Mean η (disorder index)")
    ax.set_title("FIM Disorder Index vs Temperature")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Top right: d_eff vs T
    ax = axes[0, 1]
    ax.plot(temps, d_effs, "s-", color="tab:orange", markersize=6)
    ax.axvline(x=T_C, color="red", linestyle="--", alpha=0.7, label=f"T_c={T_C:.3f}")
    ax.set_xlabel("Temperature T")
    ax.set_ylabel("Mean d_eff")
    ax.set_title("Effective Dimension vs Temperature")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Bottom left: PR vs T (joint d_eff × isotropy)
    ax = axes[1, 0]
    ax.plot(temps, prs, "^-", color="tab:green", markersize=6)
    ax.axvline(x=T_C, color="red", linestyle="--", alpha=0.7, label=f"T_c={T_C:.3f}")
    ax.set_xlabel("Temperature T")
    ax.set_ylabel("Mean PR (participation ratio)")
    ax.set_title("Participation Ratio vs Temperature")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Bottom right: |correlation| vs T
    ax = axes[1, 1]
    ax.plot(temps, corrs, "d-", color="tab:purple", markersize=6)
    ax.axvline(x=T_C, color="red", linestyle="--", alpha=0.7, label=f"T_c={T_C:.3f}")
    ax.set_xlabel("Temperature T")
    ax.set_ylabel("Mean |⟨s_i s_j⟩| (NN correlation)")
    ax.set_title("Nearest-Neighbor Correlation vs Temperature")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.suptitle(f"2D Ising Model FIM Analysis — L={L}, α={ALPHA}, weight={WEIGHT_MODE}",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "mc_temperature_sweep.png", dpi=150)
    print(f"Plot saved to {OUT_DIR / 'mc_temperature_sweep.png'}")

    # --- Summary ---
    print(f"\n{'='*80}")
    print(f"SUMMARY: 2D Ising L={L}, T_c={T_C:.5f}")
    print(f"{'='*80}")
    print(f"{'T':>6} {'T/Tc':>6} {'η':>8} {'d_eff':>7} {'PR':>7} {'ρ_CCA':>8} {'|corr|':>8}")
    print("-" * 80)
    for r in all_results:
        marker = " <<<" if abs(r["T"] - T_C) < 0.01 else ""
        print(f"{r['T']:>6.3f} {r['T_ratio']:>6.3f} {r['mean_eta']:>8.4f} "
              f"{r['mean_d_eff']:>7.2f} {r['mean_pr']:>7.3f} {r['mean_rho_cca']:>8.4f} "
              f"{r['mean_abs_correlation']:>8.4f}{marker}")


if __name__ == "__main__":
    main()
