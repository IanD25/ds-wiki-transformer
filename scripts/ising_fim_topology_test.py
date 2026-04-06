"""
Phase A: FIM Isotropy Test on Lattice Topologies

Tests whether the Fisher Information Matrix eigenvalue spectrum becomes
isotropic on regular lattice graphs as the kernel parameter alpha sweeps
from short-range (high alpha) to long-range (low alpha).

CCA prediction: higher lattice dimension → higher peak isotropy.
Expected ordering: peak η(3D) ≥ peak η(2D) > peak η(1D).

No physical simulation needed — pure topology + FIM kernel sweep.

Output: data/reports/ising_fim_test/topology_sweep.json + PNG plots
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

# Bootstrap src/
SRC = Path(__file__).resolve().parent.parent / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from analysis.fisher_diagnostics import (
    KernelType, sweep_graph, analyze_node, FisherSweepResult
)


# ── Lattice Builders ──────────────────────────────────────────────────────────

def build_2d_torus(L: int) -> nx.Graph:
    """L×L grid with periodic boundary conditions (torus)."""
    G = nx.grid_2d_graph(L, L, periodic=True)
    # Relabel to string node IDs for compatibility with fisher_diagnostics
    mapping = {(i, j): f"n_{i}_{j}" for i in range(L) for j in range(L)}
    return nx.relabel_nodes(G, mapping)


def build_3d_torus(L: int) -> nx.Graph:
    """L×L×L grid with periodic BC."""
    G = nx.grid_graph(dim=[L, L, L], periodic=True)
    mapping = {node: f"n_{'_'.join(map(str, node))}" for node in G.nodes()}
    return nx.relabel_nodes(G, mapping)


def build_path(N: int) -> nx.Graph:
    """1D chain (no periodic BC)."""
    G = nx.path_graph(N)
    mapping = {i: f"n_{i}" for i in range(N)}
    return nx.relabel_nodes(G, mapping)


def build_complete(N: int) -> nx.Graph:
    """Complete graph K_N."""
    G = nx.complete_graph(N)
    mapping = {i: f"n_{i}" for i in range(N)}
    return nx.relabel_nodes(G, mapping)


# ── Sweep ─────────────────────────────────────────────────────────────────────

ALPHAS = [0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]


def sweep_lattice(G: nx.Graph, name: str, sample_nodes: int = 20) -> list:
    """
    Sweep alpha values for a given graph.
    For large graphs, sample a subset of interior nodes to keep runtime reasonable.

    Returns list of dicts, one per alpha value.
    """
    results = []

    # Identify interior nodes (degree >= 2) and sample if large
    interior = [n for n in G.nodes() if G.degree(n) >= 2]
    if len(interior) > sample_nodes:
        rng = np.random.RandomState(42)
        sampled = list(rng.choice(interior, size=sample_nodes, replace=False))
    else:
        sampled = interior

    for alpha in ALPHAS:
        t0 = time.time()

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
            # rho_CCA = min(sv_profile) — since sv_profile is normalized with first=1.0
            if len(r.sv_profile) > 1:
                sv_mins.append(min(r.sv_profile))
            else:
                sv_mins.append(1.0)
            regimes[r.regime.value] += 1

        dt = time.time() - t0

        entry = {
            "lattice": name,
            "alpha": alpha,
            "n_nodes": G.number_of_nodes(),
            "n_sampled": len(sampled),
            "n_valid": len(etas),
            "mean_eta": float(np.mean(etas)) if etas else 0.0,
            "std_eta": float(np.std(etas)) if etas else 0.0,
            "mean_d_eff": float(np.mean(d_effs)) if d_effs else 0.0,
            "mean_pr": float(np.mean(prs)) if prs else 0.0,
            "mean_rho_cca": float(np.mean(sv_mins)) if sv_mins else 0.0,
            "regime_counts": regimes,
            "time_s": round(dt, 2),
        }
        results.append(entry)
        print(f"  {name} α={alpha:.2f}: η={entry['mean_eta']:.4f}  d_eff={entry['mean_d_eff']:.2f}  "
              f"rho_CCA={entry['mean_rho_cca']:.4f}  ({dt:.1f}s)")

    return results


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    OUT_DIR = Path("data/reports/ising_fim_test")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    all_results = []

    # --- 2D Tori ---
    for L in [8, 12, 16]:
        name = f"torus_2d_{L}x{L}"
        print(f"\n=== {name} ({L*L} nodes, degree=4) ===")
        G = build_2d_torus(L)
        results = sweep_lattice(G, name)
        all_results.extend(results)

    # --- 3D Tori ---
    for L in [4, 6]:
        name = f"torus_3d_{L}x{L}x{L}"
        print(f"\n=== {name} ({L**3} nodes, degree=6) ===")
        G = build_3d_torus(L)
        results = sweep_lattice(G, name)
        all_results.extend(results)

    # --- 1D Path (control) ---
    for N in [20, 50]:
        name = f"path_{N}"
        print(f"\n=== {name} ({N} nodes, degree=2 interior) ===")
        G = build_path(N)
        results = sweep_lattice(G, name)
        all_results.extend(results)

    # --- Complete Graph (control) ---
    for N in [8, 16]:
        name = f"complete_{N}"
        print(f"\n=== {name} ({N} nodes, degree={N-1}) ===")
        G = build_complete(N)
        results = sweep_lattice(G, name, sample_nodes=N)
        all_results.extend(results)

    # Save results
    with open(OUT_DIR / "topology_sweep.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {OUT_DIR / 'topology_sweep.json'}")

    # --- Plot: α vs mean η ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Group by lattice
    lattices = {}
    for r in all_results:
        lattices.setdefault(r["lattice"], []).append(r)

    # Left plot: η vs α
    ax = axes[0]
    for name, data in sorted(lattices.items()):
        alphas = [d["alpha"] for d in data]
        etas = [d["mean_eta"] for d in data]
        ax.plot(alphas, etas, "o-", label=name, markersize=4)
    ax.set_xlabel("α (kernel decay)")
    ax.set_ylabel("Mean η (disorder index)")
    ax.set_title("FIM Isotropy vs Kernel Range")
    ax.set_xscale("log")
    ax.legend(fontsize=7, loc="best")
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0.35, color="gray", linestyle="--", alpha=0.5, label="RADIAL/ISO boundary")
    ax.axhline(y=0.65, color="gray", linestyle=":", alpha=0.5, label="ISO/NOISE boundary")

    # Right plot: d_eff vs α
    ax = axes[1]
    for name, data in sorted(lattices.items()):
        alphas = [d["alpha"] for d in data]
        d_effs = [d["mean_d_eff"] for d in data]
        ax.plot(alphas, d_effs, "o-", label=name, markersize=4)
    ax.set_xlabel("α (kernel decay)")
    ax.set_ylabel("Mean d_eff")
    ax.set_title("Effective Dimension vs Kernel Range")
    ax.set_xscale("log")
    ax.legend(fontsize=7, loc="best")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_DIR / "alpha_vs_eta.png", dpi=150)
    print(f"Plot saved to {OUT_DIR / 'alpha_vs_eta.png'}")

    # --- Summary table ---
    print("\n" + "=" * 80)
    print("SUMMARY: Peak η per lattice")
    print("=" * 80)
    print(f"{'Lattice':<25} {'Peak η':>8} {'@ α':>6} {'d_eff':>7} {'rho_CCA':>9}")
    print("-" * 80)
    for name, data in sorted(lattices.items()):
        peak = max(data, key=lambda d: d["mean_eta"])
        print(f"{name:<25} {peak['mean_eta']:>8.4f} {peak['alpha']:>6.2f} "
              f"{peak['mean_d_eff']:>7.2f} {peak['mean_rho_cca']:>9.4f}")


if __name__ == "__main__":
    main()
