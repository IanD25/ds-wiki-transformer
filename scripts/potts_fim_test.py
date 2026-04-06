"""
CCA-1 Critical Test: Potts q=10 First-Order Transition

The 2D Potts model with q=10 has a FIRST-ORDER phase transition.
CCA-1 predicts: first-order transitions do NOT show the CCA signature
(d_eff > 1 AND eta > 0.35 simultaneously).

If Potts q=10 at T_transition shows low d_eff or low eta (or both),
CCA-1 survives. If it shows the same (d_eff > 1, high eta) signature
as the 2D Ising continuous transition, CCA-1 is falsified.

For comparison, also runs q=2 (Ising equivalent, continuous transition)
to ensure the same infrastructure produces the CCA signature when it should.

Potts model: H = -J * sum_{<i,j>} delta(s_i, s_j), s_i in {0, 1, ..., q-1}
T_c(q) = 1 / ln(1 + sqrt(q))  (exact for 2D, all q)
  q=2: T_c = 2.269 (continuous, = 2D Ising)
  q=10: T_c = 0.701 (first-order)

Output: data/reports/ising_fim_test/potts_comparison.json + PNG
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

from analysis.fisher_diagnostics import KernelType, analyze_node


# ── Potts MC (numpy-only) ────────────────────────────────────────────────────

def potts_tc(q: int) -> float:
    """Exact critical temperature for 2D q-state Potts model."""
    return 1.0 / np.log(1.0 + np.sqrt(q))


def potts_mc(L: int, q: int, T: float, n_equil: int = 8000,
             n_measure: int = 15000, sample_every: int = 10,
             seed: int = 42) -> tuple:
    """
    Metropolis-Hastings Potts simulation on L×L torus.
    Returns (corr_h, corr_v) — nearest-neighbor delta-correlation arrays.
    corr[i,j] = <delta(s_{i,j}, s_{neighbor})> averaged over measurements.
    """
    rng = np.random.RandomState(seed)
    spins = rng.randint(0, q, size=(L, L))
    beta = 1.0 / T

    # Equilibration
    for _ in range(n_equil):
        _potts_sweep(spins, beta, q, L, rng)

    # Measurement
    n_samples = 0
    corr_h = np.zeros((L, L), dtype=np.float64)
    corr_v = np.zeros((L, L), dtype=np.float64)

    for sweep in range(n_measure):
        _potts_sweep(spins, beta, q, L, rng)
        if sweep % sample_every == 0:
            # Horizontal: delta(s[i,j], s[i,(j+1)%L])
            corr_h += (spins == np.roll(spins, -1, axis=1)).astype(np.float64)
            # Vertical: delta(s[i,j], s[(i+1)%L,j])
            corr_v += (spins == np.roll(spins, -1, axis=0)).astype(np.float64)
            n_samples += 1

    corr_h /= n_samples
    corr_v /= n_samples

    return corr_h, corr_v


def _potts_sweep(spins: np.ndarray, beta: float, q: int, L: int, rng):
    """One Metropolis sweep for Potts model."""
    for _ in range(L * L):
        i = rng.randint(0, L)
        j = rng.randint(0, L)
        s_old = spins[i, j]
        s_new = rng.randint(0, q)
        if s_new == s_old:
            continue

        # Count matching neighbors for old and new state
        neighbors = [
            spins[(i + 1) % L, j], spins[(i - 1) % L, j],
            spins[i, (j + 1) % L], spins[i, (j - 1) % L]
        ]
        n_old = sum(1 for n in neighbors if n == s_old)
        n_new = sum(1 for n in neighbors if n == s_new)

        dE = -(n_new - n_old)  # J=1, delta-function interaction
        if dE <= 0 or rng.random() < np.exp(-beta * dE):
            spins[i, j] = s_new


# ── Graph Construction ────────────────────────────────────────────────────────

def build_correlation_graph(corr_h, corr_v, L, weight_mode="abs"):
    """Build NetworkX graph from Potts correlations."""
    G = nx.Graph()
    eps = 1e-8

    for i in range(L):
        for j in range(L):
            G.add_node(f"n_{i}_{j}")

    for i in range(L):
        for j in range(L):
            j2 = (j + 1) % L
            c = max(abs(corr_h[i, j]), eps)
            w = c if weight_mode == "abs" else (-np.log(c) if weight_mode == "neglog" else 1.0 / c)
            G.add_edge(f"n_{i}_{j}", f"n_{i}_{j2}", weight=max(w, eps))

            i2 = (i + 1) % L
            c = max(abs(corr_v[i, j]), eps)
            w = c if weight_mode == "abs" else (-np.log(c) if weight_mode == "neglog" else 1.0 / c)
            G.add_edge(f"n_{i}_{j}", f"n_{i2}_{j}", weight=max(w, eps))

    return G


# ── FIM Analysis ──────────────────────────────────────────────────────────────

def analyze_potts(L, q, T, n_sample_nodes=25, alpha=1.0, weight_mode="abs",
                  seed=42, n_equil=8000, n_measure=15000):
    """Full pipeline: MC → correlation graph → FIM."""
    t0 = time.time()

    corr_h, corr_v = potts_mc(L, q, T, n_equil=n_equil, n_measure=n_measure, seed=seed)
    t_mc = time.time() - t0

    G = build_correlation_graph(corr_h, corr_v, L, weight_mode=weight_mode)

    nodes = list(G.nodes())
    rng = np.random.RandomState(seed + 1)
    sampled = list(rng.choice(nodes, size=min(n_sample_nodes, len(nodes)), replace=False))

    etas, d_effs, prs, sv_mins = [], [], [], []
    regimes = {"radial_dominated": 0, "isotropic": 0, "noise_dominated": 0, "degenerate": 0}

    for node in sampled:
        r = analyze_node(G, str(node), KernelType.EXPONENTIAL, alpha=alpha)
        if r.skipped:
            regimes["degenerate"] += 1
            continue
        etas.append(r.eta)
        d_effs.append(r.d_eff)
        prs.append(r.pr)
        sv_mins.append(min(r.sv_profile) if len(r.sv_profile) > 1 else 1.0)
        regimes[r.regime.value] += 1

    dt = time.time() - t0
    all_corr = np.concatenate([corr_h.ravel(), corr_v.ravel()])

    return {
        "q": q,
        "L": L,
        "T": T,
        "T_c": float(potts_tc(q)),
        "T_ratio": T / potts_tc(q),
        "transition_order": "continuous" if q <= 4 else "first-order",
        "n_sampled": len(sampled),
        "n_valid": len(etas),
        "mean_eta": float(np.mean(etas)) if etas else 0.0,
        "std_eta": float(np.std(etas)) if etas else 0.0,
        "mean_d_eff": float(np.mean(d_effs)) if d_effs else 0.0,
        "std_d_eff": float(np.std(d_effs)) if d_effs else 0.0,
        "mean_pr": float(np.mean(prs)) if prs else 0.0,
        "mean_rho_cca": float(np.mean(sv_mins)) if sv_mins else 0.0,
        "regime_counts": regimes,
        "mean_abs_correlation": float(np.mean(np.abs(all_corr))),
        "alpha": alpha,
        "weight_mode": weight_mode,
        "time_total_s": round(dt, 2),
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    OUT_DIR = Path("data/reports/ising_fim_test")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    L = 16
    ALPHA = 1.0

    # Both weight modes for comparison
    for WEIGHT_MODE in ["abs", "neglog"]:
        print(f"\n{'='*80}")
        print(f"WEIGHT MODE: {WEIGHT_MODE}")
        print(f"{'='*80}")

        all_results = []

        # ── q=10 (FIRST-ORDER) ────────────────────────────────────
        q = 10
        tc = potts_tc(q)
        print(f"\n--- Potts q={q} (FIRST-ORDER), T_c = {tc:.4f} ---")

        temps_q10 = [
            tc * 0.7, tc * 0.85, tc * 0.95,
            tc * 0.99, tc, tc * 1.01,
            tc * 1.05, tc * 1.15, tc * 1.3, tc * 1.6
        ]

        for T in temps_q10:
            r = analyze_potts(L, q, T, alpha=ALPHA, weight_mode=WEIGHT_MODE,
                              n_equil=10000, n_measure=20000)
            all_results.append(r)
            marker = " *** TRANSITION ***" if abs(T / tc - 1.0) < 0.02 else ""
            print(f"  T={T:.4f} T/Tc={r['T_ratio']:.3f}: "
                  f"eta={r['mean_eta']:.4f} d_eff={r['mean_d_eff']:.2f} "
                  f"PR={r['mean_pr']:.3f} |corr|={r['mean_abs_correlation']:.4f} "
                  f"({r['time_total_s']:.1f}s){marker}")

        # ── q=2 (CONTINUOUS — Ising equivalent) ───────────────────
        q = 2
        tc2 = potts_tc(q)
        print(f"\n--- Potts q={q} (CONTINUOUS / Ising), T_c = {tc2:.4f} ---")

        temps_q2 = [
            tc2 * 0.7, tc2 * 0.85, tc2 * 0.95,
            tc2 * 0.99, tc2, tc2 * 1.01,
            tc2 * 1.05, tc2 * 1.15, tc2 * 1.3, tc2 * 1.6
        ]

        for T in temps_q2:
            r = analyze_potts(L, q, T, alpha=ALPHA, weight_mode=WEIGHT_MODE,
                              n_equil=8000, n_measure=15000)
            all_results.append(r)
            marker = " *** TRANSITION ***" if abs(T / tc2 - 1.0) < 0.02 else ""
            print(f"  T={T:.4f} T/Tc={r['T_ratio']:.3f}: "
                  f"eta={r['mean_eta']:.4f} d_eff={r['mean_d_eff']:.2f} "
                  f"PR={r['mean_pr']:.3f} |corr|={r['mean_abs_correlation']:.4f} "
                  f"({r['time_total_s']:.1f}s){marker}")

        # Save
        fname = f"potts_comparison_{WEIGHT_MODE}.json"
        with open(OUT_DIR / fname, "w") as f:
            json.dump(all_results, f, indent=2)

    # ── Comparison Plot ───────────────────────────────────────────
    # Load abs results for plotting
    with open(OUT_DIR / "potts_comparison_abs.json") as f:
        results_abs = json.load(f)

    q10 = [r for r in results_abs if r["q"] == 10]
    q2 = [r for r in results_abs if r["q"] == 2]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # η vs T/T_c
    ax = axes[0, 0]
    ax.plot([r["T_ratio"] for r in q10], [r["mean_eta"] for r in q10],
            "o-", color="red", label="q=10 (first-order)", markersize=6)
    ax.plot([r["T_ratio"] for r in q2], [r["mean_eta"] for r in q2],
            "s-", color="blue", label="q=2 (continuous)", markersize=6)
    ax.axvline(x=1.0, color="gray", linestyle="--", alpha=0.5)
    ax.axhline(y=0.35, color="gray", linestyle=":", alpha=0.3, label="eta=0.35")
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("Mean eta")
    ax.set_title("Disorder Index: First-Order vs Continuous")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # d_eff vs T/T_c
    ax = axes[0, 1]
    ax.plot([r["T_ratio"] for r in q10], [r["mean_d_eff"] for r in q10],
            "o-", color="red", label="q=10 (first-order)", markersize=6)
    ax.plot([r["T_ratio"] for r in q2], [r["mean_d_eff"] for r in q2],
            "s-", color="blue", label="q=2 (continuous)", markersize=6)
    ax.axvline(x=1.0, color="gray", linestyle="--", alpha=0.5)
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("Mean d_eff")
    ax.set_title("Effective Dimension: First-Order vs Continuous")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # PR vs T/T_c
    ax = axes[1, 0]
    ax.plot([r["T_ratio"] for r in q10], [r["mean_pr"] for r in q10],
            "o-", color="red", label="q=10 (first-order)", markersize=6)
    ax.plot([r["T_ratio"] for r in q2], [r["mean_pr"] for r in q2],
            "s-", color="blue", label="q=2 (continuous)", markersize=6)
    ax.axvline(x=1.0, color="gray", linestyle="--", alpha=0.5)
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("Mean PR")
    ax.set_title("Participation Ratio: First-Order vs Continuous")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # |correlation| vs T/T_c
    ax = axes[1, 1]
    ax.plot([r["T_ratio"] for r in q10], [r["mean_abs_correlation"] for r in q10],
            "o-", color="red", label="q=10 (first-order)", markersize=6)
    ax.plot([r["T_ratio"] for r in q2], [r["mean_abs_correlation"] for r in q2],
            "s-", color="blue", label="q=2 (continuous)", markersize=6)
    ax.axvline(x=1.0, color="gray", linestyle="--", alpha=0.5)
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("Mean |correlation|")
    ax.set_title("NN Correlation: First-Order vs Continuous")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.suptitle(f"CCA-1 Test: Potts q=10 (first-order) vs q=2 (continuous) — L={L}, abs weights",
                 fontsize=12, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "potts_comparison.png", dpi=150)
    print(f"\nPlot saved to {OUT_DIR / 'potts_comparison.png'}")

    # ── Verdict ───────────────────────────────────────────────────
    print(f"\n{'='*80}")
    print("CCA-1 VERDICT")
    print(f"{'='*80}")

    # Find peak diagnostics near T_c for each
    q10_near_tc = [r for r in q10 if 0.95 <= r["T_ratio"] <= 1.05]
    q2_near_tc = [r for r in q2 if 0.95 <= r["T_ratio"] <= 1.05]

    if q10_near_tc:
        q10_peak = max(q10_near_tc, key=lambda r: r["mean_pr"])
        print(f"\nPotts q=10 (FIRST-ORDER) near T_c:")
        print(f"  eta = {q10_peak['mean_eta']:.4f}")
        print(f"  d_eff = {q10_peak['mean_d_eff']:.2f}")
        print(f"  PR = {q10_peak['mean_pr']:.3f}")
        cca_q10 = q10_peak["mean_d_eff"] > 1 and q10_peak["mean_eta"] > 0.35
        print(f"  CCA signature (d_eff>1 AND eta>0.35): {'YES' if cca_q10 else 'NO'}")

    if q2_near_tc:
        q2_peak = max(q2_near_tc, key=lambda r: r["mean_pr"])
        print(f"\nPotts q=2 (CONTINUOUS) near T_c:")
        print(f"  eta = {q2_peak['mean_eta']:.4f}")
        print(f"  d_eff = {q2_peak['mean_d_eff']:.2f}")
        print(f"  PR = {q2_peak['mean_pr']:.3f}")
        cca_q2 = q2_peak["mean_d_eff"] > 1 and q2_peak["mean_eta"] > 0.35
        print(f"  CCA signature (d_eff>1 AND eta>0.35): {'YES' if cca_q2 else 'NO'}")

    if q10_near_tc and q2_near_tc:
        print(f"\n--- DISCRIMINATION ---")
        if cca_q2 and not cca_q10:
            print("  RESULT: CCA-1 SURVIVES")
            print("  Continuous transition shows CCA signature; first-order does not.")
        elif not cca_q2 and not cca_q10:
            print("  RESULT: INCONCLUSIVE (neither shows CCA signature)")
            print("  May be finite-size / weight-mode limitation.")
        elif cca_q2 and cca_q10:
            print("  RESULT: CCA-1 FALSIFIED")
            print("  Both show CCA signature — first-order is not discriminated.")
        else:
            print("  RESULT: UNEXPECTED (first-order shows CCA but continuous doesn't)")


if __name__ == "__main__":
    main()
