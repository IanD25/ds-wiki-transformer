"""
CCA-1b Finite-Size Scaling — Numba-Accelerated Edition

Tests whether S_max = max|dη/dT| scales differently for first-order vs continuous
phase transitions, using JIT-compiled Potts MC for L=16, 32, 48 feasibility.

CCA-1b prediction:
  Continuous (q=2): S_max(L) ~ L^α with α small (slow growth)
  First-order (q=10): S_max(L) ~ L^d (strong growth)

If the scaling exponents differ by a clear factor, CCA-1b is validated.

Uses numba.njit for the inner Metropolis sweep — ~50-100x speedup vs pure Python.

Output: data/reports/ising_fim_test/cca1b_scaling/
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
from numba import njit

SRC = Path(__file__).resolve().parent.parent / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from analysis.fisher_diagnostics import KernelType, analyze_node


# ── JIT-Compiled Potts MC ─────────────────────────────────────────────────────

@njit(cache=True)
def potts_sweep_jit(spins, beta, q, L, rand_i, rand_j, rand_new, rand_accept):
    """One Metropolis sweep — fully JIT-compiled.
    Pre-generated random numbers for batch efficiency."""
    n = L * L
    for k in range(n):
        i = rand_i[k]
        j = rand_j[k]
        s_old = spins[i, j]
        s_new = rand_new[k]
        if s_new == s_old:
            continue
        # Neighbor sum
        s_up = spins[(i + 1) % L, j]
        s_dn = spins[(i - 1) % L, j]
        s_rt = spins[i, (j + 1) % L]
        s_lt = spins[i, (j - 1) % L]
        n_old = (s_up == s_old) + (s_dn == s_old) + (s_rt == s_old) + (s_lt == s_old)
        n_new = (s_up == s_new) + (s_dn == s_new) + (s_rt == s_new) + (s_lt == s_new)
        dE = -(n_new - n_old)
        if dE <= 0 or rand_accept[k] < np.exp(-beta * dE):
            spins[i, j] = s_new


@njit(cache=True)
def measure_correlations_jit(spins, L):
    """Compute one-shot NN correlations (delta function for Potts)."""
    corr_h = np.zeros((L, L), dtype=np.float64)
    corr_v = np.zeros((L, L), dtype=np.float64)
    for i in range(L):
        for j in range(L):
            corr_h[i, j] = 1.0 if spins[i, j] == spins[i, (j + 1) % L] else 0.0
            corr_v[i, j] = 1.0 if spins[i, j] == spins[(i + 1) % L, j] else 0.0
    return corr_h, corr_v


def run_potts_jit(L, q, T, n_equil, n_measure, sample_every, seed=42):
    """Full Potts MC using JIT-compiled inner loop."""
    rng = np.random.default_rng(seed)
    spins = rng.integers(0, q, size=(L, L)).astype(np.int64)
    beta = 1.0 / T
    n = L * L

    # Equilibration
    for _ in range(n_equil):
        rand_i = rng.integers(0, L, size=n).astype(np.int64)
        rand_j = rng.integers(0, L, size=n).astype(np.int64)
        rand_new = rng.integers(0, q, size=n).astype(np.int64)
        rand_accept = rng.random(size=n)
        potts_sweep_jit(spins, beta, q, L, rand_i, rand_j, rand_new, rand_accept)

    # Measurement
    corr_h_total = np.zeros((L, L), dtype=np.float64)
    corr_v_total = np.zeros((L, L), dtype=np.float64)
    n_samples = 0

    for sweep in range(n_measure):
        rand_i = rng.integers(0, L, size=n).astype(np.int64)
        rand_j = rng.integers(0, L, size=n).astype(np.int64)
        rand_new = rng.integers(0, q, size=n).astype(np.int64)
        rand_accept = rng.random(size=n)
        potts_sweep_jit(spins, beta, q, L, rand_i, rand_j, rand_new, rand_accept)

        if sweep % sample_every == 0:
            ch, cv = measure_correlations_jit(spins, L)
            corr_h_total += ch
            corr_v_total += cv
            n_samples += 1

    return corr_h_total / n_samples, corr_v_total / n_samples


def potts_tc(q):
    return 1.0 / np.log(1.0 + np.sqrt(q))


# ── Graph Construction ────────────────────────────────────────────────────────

def build_graph(corr_h, corr_v, L, weight_mode="neglog"):
    G = nx.Graph()
    eps = 1e-8
    for i in range(L):
        for j in range(L):
            G.add_node(f"n_{i}_{j}")
    for i in range(L):
        for j in range(L):
            j2 = (j + 1) % L
            c = max(abs(corr_h[i, j]), eps)
            w = -np.log(c) if weight_mode == "neglog" else c
            G.add_edge(f"n_{i}_{j}", f"n_{i}_{j2}", weight=max(w, eps))
            i2 = (i + 1) % L
            c = max(abs(corr_v[i, j]), eps)
            w = -np.log(c) if weight_mode == "neglog" else c
            G.add_edge(f"n_{i}_{j}", f"n_{i2}_{j}", weight=max(w, eps))
    return G


def analyze_at_T(L, q, T, n_sample, weight_mode, alpha, n_equil, n_measure, seed=42):
    """MC + FIM at single temperature."""
    corr_h, corr_v = run_potts_jit(L, q, T, n_equil, n_measure, sample_every=5, seed=seed)
    G = build_graph(corr_h, corr_v, L, weight_mode=weight_mode)

    nodes = list(G.nodes())
    rng = np.random.default_rng(seed + 1)
    sampled = list(rng.choice(nodes, size=min(n_sample, len(nodes)), replace=False))

    etas, d_effs, prs = [], [], []
    for node in sampled:
        r = analyze_node(G, str(node), KernelType.EXPONENTIAL, alpha=alpha)
        if not r.skipped:
            etas.append(r.eta)
            d_effs.append(r.d_eff)
            prs.append(r.pr)

    return {
        "T": float(T),
        "T_ratio": float(T / potts_tc(q)),
        "eta": float(np.mean(etas)) if etas else 0.0,
        "d_eff": float(np.mean(d_effs)) if d_effs else 0.0,
        "pr": float(np.mean(prs)) if prs else 0.0,
        "mean_corr": float(np.mean(np.abs(np.concatenate([corr_h.ravel(), corr_v.ravel()])))),
    }


# ── Derivative Estimation ─────────────────────────────────────────────────────

def central_difference(t, y):
    t_arr = np.asarray(t)
    y_arr = np.asarray(y)
    n = len(t_arr)
    if n < 3:
        return np.array([]), np.array([])
    t_mid = t_arr[1:-1]
    deriv = (y_arr[2:] - y_arr[:-2]) / (t_arr[2:] - t_arr[:-2])
    return t_mid, deriv


# ── Main Experiment ───────────────────────────────────────────────────────────

def main():
    OUT_DIR = Path("data/reports/ising_fim_test/cca1b_scaling")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("CCA-1b FINITE-SIZE SCALING — JIT-Accelerated")
    print("=" * 80)

    # Warm up JIT
    print("\nJIT warmup (compiling sweep functions)...")
    t0 = time.time()
    _, _ = run_potts_jit(8, 2, 1.0, n_equil=100, n_measure=100, sample_every=10, seed=0)
    print(f"  JIT compiled in {time.time() - t0:.1f}s")

    # Configuration
    LATTICE_SIZES = [16, 32, 48]
    Q_VALUES = [2, 10]
    WEIGHT_MODE = "neglog"  # The mode where CCA-1b separation appeared
    ALPHA = 1.0
    N_SAMPLE = 25

    # Fine temperature grid: 21 points spanning T/T_c ∈ [0.92, 1.12]
    fine_ratios = np.linspace(0.92, 1.12, 21)

    # MC effort (scales with L²)
    def mc_effort(L):
        scale = (L / 16) ** 2
        return int(3000 * scale), int(8000 * scale)

    all_data = {}

    for q in Q_VALUES:
        tc = potts_tc(q)
        order = "continuous" if q <= 4 else "first-order"

        for L in LATTICE_SIZES:
            n_eq, n_me = mc_effort(L)
            print(f"\n{'─' * 60}")
            print(f"q={q} ({order}), L={L}, T_c={tc:.4f}")
            print(f"  MC: {n_eq} equil + {n_me} measure sweeps")
            print(f"{'─' * 60}")

            t_start = time.time()
            results = []
            temps = [tc * r for r in fine_ratios]

            for idx, T in enumerate(temps):
                t0 = time.time()
                r = analyze_at_T(L, q, T, n_sample=N_SAMPLE, weight_mode=WEIGHT_MODE,
                                 alpha=ALPHA, n_equil=n_eq, n_measure=n_me, seed=42 + idx)
                results.append(r)
                dt = time.time() - t0
                print(f"  T/Tc={r['T_ratio']:.3f}: η={r['eta']:.4f} d_eff={r['d_eff']:.2f} "
                      f"PR={r['pr']:.3f} |c|={r['mean_corr']:.4f}  ({dt:.1f}s)")

            total_dt = time.time() - t_start
            print(f"  Total: {total_dt:.1f}s")

            # Extract η curve and compute derivative
            t_ratios = np.array([r["T_ratio"] for r in results])
            etas = np.array([r["eta"] for r in results])

            t_d, d_eta = central_difference(t_ratios, etas)
            S_max = float(np.max(np.abs(d_eta))) if len(d_eta) > 0 else 0.0
            S_max_T = float(t_d[np.argmax(np.abs(d_eta))]) if len(d_eta) > 0 else 0.0

            print(f"  → S_max = {S_max:.4f} at T/Tc = {S_max_T:.4f}")

            key = f"q{q}_L{L}"
            all_data[key] = {
                "q": q, "L": L, "order": order, "T_c": float(tc),
                "T_ratios": t_ratios.tolist(),
                "etas": etas.tolist(),
                "d_effs": [r["d_eff"] for r in results],
                "prs": [r["pr"] for r in results],
                "mean_corrs": [r["mean_corr"] for r in results],
                "d_eta_T": t_d.tolist(),
                "d_eta": d_eta.tolist(),
                "S_max": S_max,
                "S_max_T_ratio": S_max_T,
                "n_equil": n_eq,
                "n_measure": n_me,
                "time_s": round(total_dt, 1),
            }

            # Save incrementally
            with open(OUT_DIR / "cca1b_scaling_fast.json", "w") as f:
                json.dump(all_data, f, indent=2)

    # ── Scaling Analysis ─────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("SCALING ANALYSIS")
    print(f"{'=' * 80}")

    scaling_results = {}
    for q in Q_VALUES:
        Ls = []
        S_maxes = []
        for L in LATTICE_SIZES:
            key = f"q{q}_L{L}"
            if key in all_data:
                Ls.append(L)
                S_maxes.append(all_data[key]["S_max"])

        if len(Ls) >= 2 and all(s > 0 for s in S_maxes):
            log_L = np.log(Ls)
            log_S = np.log(S_maxes)
            slope, intercept = np.polyfit(log_L, log_S, 1)
            order = "continuous" if q <= 4 else "first-order"

            print(f"\nq={q} ({order}):")
            for L, S in zip(Ls, S_maxes):
                print(f"  L={L}: S_max = {S:.4f}")
            print(f"  Power-law fit: S_max ~ L^{slope:.3f}")

            scaling_results[f"q{q}"] = {
                "Ls": Ls,
                "S_maxes": S_maxes,
                "scaling_exponent": float(slope),
                "intercept": float(intercept),
            }

    # ── Verdict ──────────────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("CCA-1b VERDICT")
    print(f"{'=' * 80}")

    if "q2" in scaling_results and "q10" in scaling_results:
        alpha_cont = scaling_results["q2"]["scaling_exponent"]
        alpha_1st = scaling_results["q10"]["scaling_exponent"]
        ratio = alpha_1st / alpha_cont if alpha_cont != 0 else float("inf")

        print(f"\n  q=2 (continuous):  S_max ~ L^{alpha_cont:.3f}")
        print(f"  q=10 (first-order): S_max ~ L^{alpha_1st:.3f}")
        print(f"  Ratio of exponents: {ratio:.2f}")

        if alpha_1st > alpha_cont * 1.5 and alpha_1st > 0.3:
            print("\n  ✓ CCA-1b SUPPORTED: First-order scales significantly faster than continuous")
        elif abs(alpha_1st - alpha_cont) < 0.2:
            print("\n  ✗ CCA-1b WEAKENED: Both classes scale similarly")
        else:
            print("\n  ? CCA-1b UNCLEAR: Modest difference, needs more data")

    # Save scaling results
    with open(OUT_DIR / "cca1b_scaling_summary.json", "w") as f:
        json.dump({
            "scaling_results": scaling_results,
            "all_data": all_data,
        }, f, indent=2, default=float)

    # ── Plots ────────────────────────────────────────────────────

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Top left: η(T/Tc) for all (q, L)
    ax = axes[0, 0]
    colors = {2: "tab:blue", 10: "tab:red"}
    linestyles = {16: "-", 32: "--", 48: ":"}
    for q in Q_VALUES:
        for L in LATTICE_SIZES:
            key = f"q{q}_L{L}"
            if key in all_data:
                d = all_data[key]
                ax.plot(d["T_ratios"], d["etas"],
                        color=colors[q], linestyle=linestyles[L],
                        label=f"q={q} L={L}", marker="o", markersize=3)
    ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.5)
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("η")
    ax.set_title("η(T/T_c) — All (q, L)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Top right: |dη/dT|
    ax = axes[0, 1]
    for q in Q_VALUES:
        for L in LATTICE_SIZES:
            key = f"q{q}_L{L}"
            if key in all_data:
                d = all_data[key]
                if d["d_eta_T"]:
                    ax.plot(d["d_eta_T"], np.abs(d["d_eta"]),
                            color=colors[q], linestyle=linestyles[L],
                            label=f"q={q} L={L} (S_max={d['S_max']:.2f})",
                            marker="o", markersize=3)
    ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.5)
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("|dη/d(T/T_c)|")
    ax.set_title("|dη/dT| — All (q, L)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Bottom left: S_max vs L (log-log)
    ax = axes[1, 0]
    for q in Q_VALUES:
        if f"q{q}" in scaling_results:
            sr = scaling_results[f"q{q}"]
            order = "continuous" if q <= 4 else "first-order"
            ax.loglog(sr["Ls"], sr["S_maxes"], "o-",
                      color=colors[q], markersize=10,
                      label=f"q={q} ({order}), α={sr['scaling_exponent']:.2f}")

    ax.set_xlabel("L (lattice size)")
    ax.set_ylabel("S_max = max|dη/d(T/Tc)|")
    ax.set_title("S_max(L) Scaling")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, which="both")

    # Bottom right: |correlation|
    ax = axes[1, 1]
    for q in Q_VALUES:
        for L in LATTICE_SIZES:
            key = f"q{q}_L{L}"
            if key in all_data:
                d = all_data[key]
                ax.plot(d["T_ratios"], d["mean_corrs"],
                        color=colors[q], linestyle=linestyles[L],
                        label=f"q={q} L={L}", marker="o", markersize=3)
    ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.5)
    ax.set_xlabel("T / T_c")
    ax.set_ylabel("|⟨s_i s_j⟩|")
    ax.set_title("NN Correlation")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f"CCA-1b Finite-Size Scaling (JIT) — neglog weights, α={ALPHA}",
                 fontsize=12, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "cca1b_scaling_full.png", dpi=150)
    print(f"\nPlot saved: {OUT_DIR / 'cca1b_scaling_full.png'}")


if __name__ == "__main__":
    main()
