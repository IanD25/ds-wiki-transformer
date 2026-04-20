"""
cca_potts_plots.py — Phase 4 analysis + plots for CCA Potts sweep.

Reads:
  data/reports/cca_potts_sweep_2026/derived/observables_by_config.csv
  data/reports/cca_potts_sweep_2026/derived/observables_mean_sem.csv
  data/reports/cca_potts_sweep_2026/raw/*.npz  (optional, for Zipf plots)

Produces:
  figures/d_eff_vs_T_per_q.png      — d_eff_CCA(T/T_c) curves per q, colored by L
  figures/eta_vs_T_per_q.png        — η_CCA(T/T_c) curves
  figures/gte_vs_T_per_q.png        — G(T/T_c) curves
  figures/overlay_all_observables_q{q}.png  — 3-panel overlay per q
  figures/reduction_check_scatter.png       — ζ_L vs 1/L with theory line
  figures/zipf_plot_q{q}_L{L}_Tc.png        — sample eigenspectrum (optional)

  analysis/reduction_check_table.csv  — FSS classification per (q, L)
  analysis/brown_comparison_table.csv — discrim metrics per q
  analysis/outcome_classification.json — final A/B/C verdict
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from reduction_check_fss import (
    zeta_theory, classify_reduction, extrapolate_zeta_Linf, POTTS_2D_EXPONENTS,
)

OUT_ROOT = Path("data/reports/cca_potts_sweep_2026")
DERIVED = OUT_ROOT / "derived"
FIGURES = OUT_ROOT / "figures"
ANALYSIS = OUT_ROOT / "analysis"
RAW = OUT_ROOT / "raw"

L_COLORS = {16: "#1f77b4", 24: "#ff7f0e", 32: "#2ca02c", 48: "#d62728"}
Q_MARKERS = {2: "o", 3: "D", 4: "s", 5: "^", 7: "v", 10: "P"}


# ── Per-observable curves across q ───────────────────────────────────────────

def plot_observable_vs_T(df: pd.DataFrame, obs_key: str,
                         ylabel: str, outfile: Path, log_y: bool = False):
    """
    Plot obs_mean ± obs_sem vs T/T_c, faceted by q, colored by L.

    Assumes df has columns: q, L, T_ratio, {obs_key}_mean, {obs_key}_sem.
    """
    qs = sorted(df["q"].unique())
    fig, axes = plt.subplots(1, len(qs), figsize=(4 * len(qs), 4),
                             sharey=True, squeeze=False)
    for ax, q in zip(axes[0], qs):
        sub_q = df[df["q"] == q]
        for L in sorted(sub_q["L"].unique()):
            s = sub_q[sub_q["L"] == L].sort_values("T_ratio")
            color = L_COLORS.get(L, "black")
            ax.errorbar(s["T_ratio"], s[f"{obs_key}_mean"], yerr=s[f"{obs_key}_sem"],
                        fmt="o-", color=color, label=f"L={L}", capsize=3, lw=1.2, markersize=4)
        ax.axvline(1.0, color="grey", ls="--", alpha=0.5, lw=0.8)
        order = POTTS_2D_EXPONENTS.get(q, {}).get("order", "")
        ax.set_title(f"q={q}\n{order}", fontsize=10)
        ax.set_xlabel("T / T_c")
        if log_y:
            ax.set_yscale("log")
        ax.grid(alpha=0.3)
        if q == qs[0]:
            ax.set_ylabel(ylabel)
            ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {outfile}")


def plot_overlay_per_q(df: pd.DataFrame, q: int, outfile: Path):
    """3-panel overlay for one q: d_eff, η_CCA, GTE in 3 rows."""
    sub = df[df["q"] == q]
    fig, axes = plt.subplots(3, 1, figsize=(6, 9), sharex=True)
    obs_specs = [
        ("d_eff_CCA", "d_eff_CCA (participation ratio of χ)", False),
        ("eta_CCA", "η_CCA (Zipf exponent)", False),
        ("G_bits", "G (GTE, bits)", False),
    ]
    for ax, (obs, yl, logy) in zip(axes, obs_specs):
        for L in sorted(sub["L"].unique()):
            s = sub[sub["L"] == L].sort_values("T_ratio")
            color = L_COLORS.get(L, "black")
            ax.errorbar(s["T_ratio"], s[f"{obs}_mean"], yerr=s[f"{obs}_sem"],
                        fmt="o-", color=color, label=f"L={L}", capsize=3, lw=1.2, markersize=4)
        ax.axvline(1.0, color="grey", ls="--", alpha=0.5, lw=0.8)
        ax.set_ylabel(yl, fontsize=9)
        if logy:
            ax.set_yscale("log")
        ax.grid(alpha=0.3)
        if obs == "eta_CCA":
            zt = zeta_theory(q)
            if zt is not None:
                ax.axhline(zt, color="red", ls=":", alpha=0.5, lw=1,
                           label=f"ζ_theory = {zt:.3f}")
        ax.legend(loc="best", fontsize=7)
    order = POTTS_2D_EXPONENTS.get(q, {}).get("order", "")
    axes[0].set_title(f"q = {q} ({order})", fontsize=11)
    axes[-1].set_xlabel("T / T_c")
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {outfile}")


# ── Reduction check: FSS extrapolation ζ(L) → ζ_∞ ─────────────────────────────

def run_reduction_check(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each (q, L) at T = T_c (T_ratio = 1.00), compute η_CCA mean, SEM,
    classify R1/R2/ambiguous, and FSS-extrapolate ζ_∞ per q.

    Returns dataframe with columns: q, L, eta_CCA_mean, eta_CCA_sem,
    zeta_theory, deviation_sigma, outcome, plus per-q ζ_∞.
    """
    tc_rows = df[np.isclose(df["T_ratio"], 1.0)].copy()
    results = []
    for (q, L), group in tc_rows.groupby(["q", "L"]):
        row = group.iloc[0]
        res = classify_reduction(q=q, L=L,
                                 eta_CCA_mean=row["eta_CCA_mean"],
                                 eta_CCA_sem=row["eta_CCA_sem"])
        results.append({
            "q": q, "L": L,
            "eta_CCA_mean": row["eta_CCA_mean"],
            "eta_CCA_sem": row["eta_CCA_sem"],
            "zeta_theory": res.zeta_theory,
            "deviation_sigma": res.deviation_sigma,
            "outcome": res.outcome,
            "rationale": res.rationale,
        })
    results_df = pd.DataFrame(results)

    # Add FSS extrapolation per q (where applicable)
    extrap_rows = []
    for q in sorted(results_df["q"].unique()):
        sub = results_df[results_df["q"] == q].sort_values("L")
        Ls = sub["L"].values
        zetas = sub["eta_CCA_mean"].values
        sems = sub["eta_CCA_sem"].values
        extrap = extrapolate_zeta_Linf(Ls, zetas, sems)
        extrap_rows.append({
            "q": q,
            "zeta_inf": extrap["zeta_inf"],
            "zeta_inf_sem": extrap["zeta_inf_sem"],
            "zeta_theory": zeta_theory(q),
            "extrap_n_points": extrap["n_points"],
            "extrap_slope": extrap["slope"],
        })
    extrap_df = pd.DataFrame(extrap_rows)
    return results_df, extrap_df


def plot_reduction_check(results_df: pd.DataFrame,
                          extrap_df: pd.DataFrame,
                          outfile: Path):
    """
    Scatter η_CCA(T_c, L) vs 1/L, with linear-extrapolation line and horizontal
    ζ_theory reference per q.
    """
    fig, ax = plt.subplots(1, 1, figsize=(6, 5))
    for q in sorted(results_df["q"].unique()):
        sub = results_df[results_df["q"] == q].sort_values("L")
        inv_L = 1.0 / sub["L"].values
        ax.errorbar(inv_L, sub["eta_CCA_mean"], yerr=sub["eta_CCA_sem"],
                    fmt="o", label=f"q={q}", capsize=3, markersize=7)
        # Draw extrapolation line
        ext = extrap_df[extrap_df["q"] == q].iloc[0] if len(extrap_df[extrap_df["q"]==q]) else None
        if ext is not None and not np.isnan(ext["zeta_inf"]):
            x_line = np.linspace(0, inv_L.max() * 1.1, 100)
            y_line = ext["zeta_inf"] + ext["extrap_slope"] * x_line
            ax.plot(x_line, y_line, ls="--", alpha=0.7,
                    color=ax.lines[-1].get_color())
        # Theory horizontal line
        zt = zeta_theory(q)
        if zt is not None:
            ax.axhline(zt, color=ax.lines[-1].get_color(), ls=":", alpha=0.4, lw=1)
    ax.set_xlabel("1 / L")
    ax.set_ylabel("η_CCA at T_c")
    ax.set_title("Reduction check: FSS extrapolation of η_CCA to L → ∞")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, None)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {outfile}")


# ── Zipf plot for representative runs ────────────────────────────────────────

def plot_zipf_spectra(q: int, L: int, T_idx: int = 4,
                       raw_dir: Path = RAW,
                       outfile: Path = None) -> None:
    """
    Log-log Zipf plot of eigenvalue spectrum at T=T_c for a given (q, L).
    Overlays all 5 replicas + Vinayak ζ_theory line.
    """
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    for rep in range(10):  # try up to 10 replicas
        path = raw_dir / f"run_q{q}_L{L}_T{T_idx}_rep{rep}.npz"
        if not path.exists():
            continue
        data = np.load(path, allow_pickle=True)
        spectrum = data["spectrum"]
        js = np.arange(1, len(spectrum) + 1)
        ax.loglog(js, spectrum, 'o', markersize=2, alpha=0.4, label=f"rep {rep}")
    zt = zeta_theory(q)
    if zt is not None:
        js_ref = np.arange(1, L * L + 1)
        # Fit c so the line passes through spectrum at j=10
        lam_10 = spectrum[9] if len(spectrum) > 9 else 1.0
        c_ref = lam_10 * 10 ** zt
        ax.loglog(js_ref, c_ref * js_ref ** (-zt), 'r--',
                  label=f"ζ_theory = {zt:.3f}", alpha=0.7)
    ax.set_xlabel("eigenvalue rank j")
    ax.set_ylabel("λ_j")
    order = POTTS_2D_EXPONENTS.get(q, {}).get("order", "")
    ax.set_title(f"Zipf plot at T=T_c, q={q}, L={L}  ({order})")
    ax.legend(loc="best", fontsize=8)
    ax.grid(which="both", alpha=0.3)
    fig.tight_layout()
    if outfile is None:
        outfile = FIGURES / f"zipf_plot_q{q}_L{L}_Tc.png"
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {outfile}")


# ── Brown comparison metrics ─────────────────────────────────────────────────

def compute_brown_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """
    Discrimination metric: peak-height ratio AND jump magnitude at T_c.

    Spec §4.2 called for peak-height difference, but for first-order transitions
    the more informative signature is the JUMP at T_c (the defining feature of
    first-order). We compute both:

      peak_X(q, L)    : max over T ratios (global peak magnitude)
      jump_X(q, L)    : (X(T/Tc=1.01) − X(T/Tc=0.99)) / max(|X(0.99)|, ε)
      peak_T_ratio(q, L) : T_ratio at which X is maximum

    Discrimination = (first-order / continuous) ratio of jump magnitudes.
    """
    rows = []
    for L in sorted(df["L"].unique()):
        sub_L = df[df["L"] == L]
        q2 = sub_L[sub_L["q"] == 2]
        if len(q2) == 0:
            continue

        def peak_and_jump(sub, col):
            """Peak value, peak T/Tc, and T_c jump."""
            peak_val = sub[col].max()
            peak_T = sub.loc[sub[col].idxmax(), "T_ratio"]
            try:
                lo = sub[np.isclose(sub["T_ratio"], 0.99)][col].iloc[0]
                hi = sub[np.isclose(sub["T_ratio"], 1.01)][col].iloc[0]
                jump = (hi - lo) / max(abs(lo), 1e-9)
            except IndexError:
                jump = float("nan")
            return peak_val, peak_T, jump

        peak_d2, peak_T_d2, jump_d2 = peak_and_jump(q2, "d_eff_CCA_mean")
        peak_e2, peak_T_e2, jump_e2 = peak_and_jump(q2, "eta_CCA_mean")
        peak_G2, peak_T_G2, jump_G2 = peak_and_jump(q2, "G_bits_mean")

        for q in sorted(sub_L["q"].unique()):
            if q == 2:
                continue
            sub_q = sub_L[sub_L["q"] == q]
            peak_d, peak_T_d, jump_d = peak_and_jump(sub_q, "d_eff_CCA_mean")
            peak_e, peak_T_e, jump_e = peak_and_jump(sub_q, "eta_CCA_mean")
            peak_G, peak_T_G, jump_G = peak_and_jump(sub_q, "G_bits_mean")
            rows.append({
                "L": L, "q": q,
                # d_eff
                "peak_d_eff": peak_d, "peak_T_d_eff": peak_T_d,
                "jump_d_eff": jump_d, "jump_d_eff_q2": jump_d2,
                "discrim_d_eff": jump_d / max(abs(jump_d2), 1e-9),
                # eta
                "peak_eta": peak_e, "peak_T_eta": peak_T_e,
                "jump_eta": jump_e, "jump_eta_q2": jump_e2,
                "discrim_eta": jump_e / max(abs(jump_e2), 1e-9),
                # G
                "peak_G": peak_G, "peak_T_G": peak_T_G,
                "jump_G": jump_G, "jump_G_q2": jump_G2,
                "discrim_G": jump_G / max(abs(jump_G2), 1e-9),
                # peak tracking flag (does eta peak match G peak?)
                "eta_G_peak_same": np.isclose(peak_T_e, peak_T_G, atol=0.005),
                "d_eff_G_peak_same": np.isclose(peak_T_d, peak_T_G, atol=0.005),
            })
    return pd.DataFrame(rows)


def classify_outcome(brown_df: pd.DataFrame) -> dict:
    """
    Spec §4.2 outcome, applied per-observable (d_eff, eta) vs GTE:

    For each (L, q) and each CCA observable X ∈ {d_eff, eta}:
      A_X : jump_X / jump_X(q=2) > 0.5 · jump_G / jump_G(q=2) AND peak_T tracks peak_T(G)
      B_X : jump ratio < 0.2 · GTE jump ratio OR peak_T diverges
      C_X : otherwise

    Overall CCA-1c classification: A if EITHER observable tracks GTE, C if they
    discriminate differently, B if both fail to discriminate vs GTE.
    """
    verdicts = []
    for _, row in brown_df.iterrows():
        d_ratio = row["discrim_d_eff"]
        e_ratio = row["discrim_eta"]
        g_ratio = row["discrim_G"]

        def class_observable(ratio, peak_same):
            if g_ratio == 0:
                return "N/A"
            if ratio > 0.5 * g_ratio and peak_same:
                return "A"
            if ratio < 0.2 * g_ratio:
                return "B"
            return "C"

        tag_d = class_observable(d_ratio, row["d_eff_G_peak_same"])
        tag_e = class_observable(e_ratio, row["eta_G_peak_same"])

        # Overall tag: best of the two observables
        if tag_d == "A" or tag_e == "A":
            tag = "A"
        elif tag_d == "B" and tag_e == "B":
            tag = "B"
        else:
            tag = "C"

        verdicts.append({
            "L": row["L"], "q": row["q"],
            "discrim_d_eff": d_ratio, "discrim_eta": e_ratio, "discrim_G": g_ratio,
            "eta_G_peak_same": row["eta_G_peak_same"],
            "d_eff_G_peak_same": row["d_eff_G_peak_same"],
            "tag_d_eff": tag_d, "tag_eta": tag_e, "tag": tag,
        })
    verdict_df = pd.DataFrame(verdicts)
    summary = {}
    for q in verdict_df["q"].unique():
        tags = verdict_df[verdict_df["q"] == q]["tag"].value_counts().to_dict()
        tags_d = verdict_df[verdict_df["q"] == q]["tag_d_eff"].value_counts().to_dict()
        tags_e = verdict_df[verdict_df["q"] == q]["tag_eta"].value_counts().to_dict()
        total = verdict_df[verdict_df["q"] == q].shape[0]
        summary[int(q)] = {
            "tag_counts": tags,
            "tag_d_eff_counts": tags_d,
            "tag_eta_counts": tags_e,
            "n_L": total,
        }
    return {"per_config": verdict_df.to_dict(orient="records"), "per_q_summary": summary}


# ── Main driver ─────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-zipf", action="store_true",
                    help="Also generate Zipf plots (requires raw/ .npz files)")
    args = ap.parse_args()

    FIGURES.mkdir(parents=True, exist_ok=True)
    ANALYSIS.mkdir(parents=True, exist_ok=True)

    # Load aggregated observables
    df = pd.read_csv(DERIVED / "observables_mean_sem.csv")
    print(f"Loaded {len(df)} (q,L,T) configs")
    print(f"  q: {sorted(df['q'].unique())}")
    print(f"  L: {sorted(df['L'].unique())}")
    print(f"  T_ratios: {sorted(df['T_ratio'].unique())}")

    # Main curves
    print("\nPlotting observable curves...")
    plot_observable_vs_T(df, "d_eff_CCA", "d_eff_CCA",
                         FIGURES / "d_eff_vs_T_per_q.png")
    plot_observable_vs_T(df, "eta_CCA", "η_CCA",
                         FIGURES / "eta_vs_T_per_q.png")
    plot_observable_vs_T(df, "G_bits", "G (GTE, bits)",
                         FIGURES / "gte_vs_T_per_q.png")

    # Per-q overlays
    for q in sorted(df["q"].unique()):
        plot_overlay_per_q(df, q, FIGURES / f"overlay_all_observables_q{q}.png")

    # Reduction check
    print("\nRunning reduction check...")
    red_df, extrap_df = run_reduction_check(df)
    red_df.to_csv(ANALYSIS / "reduction_check_table.csv", index=False)
    extrap_df.to_csv(ANALYSIS / "reduction_check_extrapolation.csv", index=False)
    print(f"  wrote {ANALYSIS}/reduction_check_table.csv")
    print(f"\nReduction check summary:")
    print(red_df[["q", "L", "eta_CCA_mean", "eta_CCA_sem",
                  "zeta_theory", "deviation_sigma", "outcome"]].to_string(index=False,
                                                                          float_format="%.3f"))
    print(f"\nFSS extrapolation (L → ∞):")
    print(extrap_df[["q", "zeta_inf", "zeta_inf_sem", "zeta_theory",
                     "extrap_n_points"]].to_string(index=False, float_format="%.3f"))
    plot_reduction_check(red_df, extrap_df,
                         FIGURES / "reduction_check_scatter.png")

    # Brown comparison (only if we have first-order q values)
    if set(df["q"].unique()) & {5, 7, 10}:
        print("\nComputing Brown comparison metrics...")
        brown_df = compute_brown_comparison(df)
        brown_df.to_csv(ANALYSIS / "brown_comparison_table.csv", index=False)
        print(brown_df.to_string(index=False, float_format="%.3f"))
        outcome = classify_outcome(brown_df)
        with (ANALYSIS / "outcome_classification.json").open("w") as f:
            json.dump(outcome, f, indent=2, default=str)
        print(f"\nOutcome classification:")
        for q, s in outcome["per_q_summary"].items():
            print(f"  q={q}: {s}")
    else:
        print(f"\nBrown comparison skipped (no first-order q values in data)")

    # Zipf plots (optional)
    if args.include_zipf:
        print("\nGenerating Zipf plots...")
        for q in sorted(df["q"].unique()):
            for L in sorted(df["L"].unique()):
                try:
                    plot_zipf_spectra(q, L, T_idx=4)
                except Exception as e:
                    print(f"  skipped q={q} L={L}: {e}")


if __name__ == "__main__":
    main()
