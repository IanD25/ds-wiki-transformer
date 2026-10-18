"""
cca1b_cca2_reduction.py — reduction test for CCA-2 (Phase A) and CCA-1b-magnitude (Phases C/D).

Pre-registration: docs/experiments/CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md §1 (commit 9a3c125).
No Monte Carlo: reads the saved April outputs only.

  CCA-2  : Phase A d_eff on hypercubic tori vs the three-level closed form
           λ_T (×d), λ_A (×1), λ_E (×(d−1))   and the centred-FIM control.
  CCA-1b : Phase D/C η(T) vs H_L(α′), α′ = −ln c̄ (uniform-weight reduction),
           S_max ratios q=10 / q=2.
  Secondary: Phase E χ participation ratio at T_c, q=2 (from the CCA-1c by_config.csv).

Outputs → data/reports/cca1b_cca2_reduction_2026_10/
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import networkx as nx
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from analysis.fisher_diagnostics import (  # noqa: E402
    KernelType, analyze_node, build_distance_matrix, build_distribution,
    build_fim, build_score_vectors, decompose_fim, exponential_kernel,
)

REP = ROOT / "data/reports/ising_fim_test"
PHASE_A = REP / "topology_sweep.json"
PHASE_C = REP / "potts_comparison_neglog.json"
PHASE_D = REP / "cca1b_scaling/cca1b_scaling_fast.json"
PHASE_E_CFG = ROOT / "data/reports/cca1c_lambda1_reduction_2026_10/by_config.csv"
OUT = ROOT / "data/reports/cca1b_cca2_reduction_2026_10"

ALPHAS = [0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]
TORI = [("torus_2d_8x8", 2, 8), ("torus_2d_12x12", 2, 12), ("torus_2d_16x16", 2, 16),
        ("torus_3d_4x4x4", 3, 4), ("torus_3d_6x6x6", 3, 6)]


# ── closed form (§1.2) ───────────────────────────────────────────────────────

def levels(alpha: float, L, d: int) -> tuple[float, float, float]:
    """(λ_T, λ_A, λ_E) for the L^d torus, unit edges, kernel exp(−α·hop). L=None → L=∞."""
    if L is None:
        Z = 1.0 / np.tanh(alpha / 2.0)
        p0, ph = 1.0 / Z, 0.0
    else:
        r = np.arange(1, L // 2)
        Z = 1.0 + 2.0 * np.exp(-alpha * r).sum() + np.exp(-alpha * L / 2)
        p0, ph = 1.0 / Z, np.exp(-alpha * L / 2) / Z
    a2 = 2.0 * alpha ** 2
    lam_T = a2 * (1.0 - p0 - ph)
    lam_A = a2 * ((p0 + ph) + (d - 1) * (p0 - ph) ** 2)
    lam_E = a2 * ((p0 + ph) - (p0 - ph) ** 2)
    return lam_T, lam_A, lam_E


def closed_spectrum(alpha, L, d) -> np.ndarray:
    lT, lA, lE = levels(alpha, L, d)
    return np.sort(np.array([lT] * d + [lA] + [lE] * (d - 1)))[::-1]


def closed_decomp(alpha, L, d) -> tuple[int, float]:
    d_eff, _, _, eta = decompose_fim(np.diag(closed_spectrum(alpha, L, d)))
    return d_eff, eta


# ── FIM exactly as analyze_node builds it, but returning F ─────────────────────

def fim(G: nx.Graph, node, alpha: float) -> np.ndarray:
    vids = [str(v) for v in G.nodes()]
    cd = {str(k): v for k, v in build_distance_matrix(G, node).items()}
    ckv = exponential_kernel(cd, alpha)
    nkvs = [exponential_kernel({str(k): v for k, v in build_distance_matrix(G, nb).items()}, alpha)
            for nb in G.neighbors(node)]
    S = build_score_vectors(nkvs, ckv, vids)
    p = build_distribution(ckv, vids)
    return build_fim(S, p), S, p


def fim_exact(G: nx.Graph, node, alpha: float) -> np.ndarray:
    """POST-HOC (not pre-registered): the same F with no EPS = 1e-10 cut on the
    distributions — log-probabilities computed directly, normalisers kept per node."""
    vids = list(G.nodes())
    def logp(src):
        dist = nx.single_source_shortest_path_length(G, src)
        x = -alpha * np.array([dist[v] for v in vids], dtype=float)
        return x - (x.max() + np.log(np.exp(x - x.max()).sum()))
    lc = logp(node)
    S = np.array([logp(nb) - lc for nb in G.neighbors(node)])
    p = np.exp(lc)
    return (S * p) @ S.T, float(p.min())


def torus(d: int, L: int) -> nx.Graph:
    G = nx.grid_graph(dim=[L] * d, periodic=True)
    return nx.relabel_nodes(G, {n: "n_" + "_".join(map(str, n)) for n in G.nodes()})


# ── CCA-2 ────────────────────────────────────────────────────────────────────

def cca2() -> dict:
    recorded = {(r["lattice"], r["alpha"]): r for r in json.load(open(PHASE_A))}
    rows = []
    for name, d, L in TORI:
        G = torus(d, L)
        nodes = list(G.nodes())
        probe = [nodes[0], nodes[len(nodes) // 3], nodes[-1]]
        for a in ALPHAS:
            Fs = [fim(G, n, a) for n in probe]
            sig = [np.linalg.svd(F, compute_uv=False) for F, _, _ in Fs]
            vt_dev = max(float(np.max(np.abs(s - sig[0]) / sig[0][0])) for s in sig)
            F, S, p = Fs[0]
            cs = closed_spectrum(a, L, d)
            spec_dev = float(np.max(np.abs(np.sort(sig[0])[::-1] - cs)) / cs[0])
            d_cf, eta_cf = closed_decomp(a, L, d)
            r_an = analyze_node(G, probe[0], KernelType.EXPONENTIAL, alpha=a)
            rec = recorded[(name, a)]
            mu = S @ p
            Fc = F - np.outer(mu, mu)
            d_c, _, _, eta_c = decompose_fim(Fc)
            lT, lA, lE = levels(a, L, d)
            Fx, pmin = fim_exact(G, probe[0], a)
            sx = np.sort(np.linalg.svd(Fx, compute_uv=False))[::-1]
            rows.append({
                "lattice": name, "d": d, "L": L, "alpha": a,
                "lam_T": lT, "lam_A": lA, "lam_E": lE,
                "spec_rel_dev": spec_dev, "vertex_transitive_dev": vt_dev,
                "posthoc_spec_rel_dev_no_eps_cut": float(np.max(np.abs(sx - cs)) / cs[0]),
                "posthoc_min_p_center": pmin, "posthoc_eps_cut_active": pmin < 1e-10,
                "d_eff_closed": d_cf, "eta_closed": eta_cf,
                "d_eff_analyze_node": r_an.d_eff, "eta_analyze_node": r_an.eta,
                "d_eff_phaseA": rec["mean_d_eff"], "eta_phaseA": rec["mean_eta"],
                "eta_dev_vs_phaseA": abs(eta_cf - rec["mean_eta"]),
                "mean_score_m": float(mu.mean()), "mean_score_spread": float(np.ptp(mu)),
                "d_eff_centred": d_c, "eta_centred": eta_c,
                "lamT_ne_lamE": abs(lT - lE) / max(lT, lE) > 1e-6,
            })
    ok_spec = all(r["spec_rel_dev"] < 1e-8 for r in rows)
    ok_deff = all(r["d_eff_closed"] == r["d_eff_phaseA"] == r["d_eff_analyze_node"] for r in rows)
    ok_eta = all(r["eta_dev_vs_phaseA"] < 1e-6 for r in rows)
    ok_centred = all(r["d_eff_centred"] == r["d"] for r in rows if r["lamT_ne_lamE"])
    by_dim = {}
    for dd in (2, 3):
        sub = [r for r in rows if r["d"] == dd]
        by_dim[dd] = all(r["spec_rel_dev"] < 1e-8 and r["d_eff_closed"] == r["d_eff_phaseA"]
                         and r["eta_dev_vs_phaseA"] < 1e-6 for r in sub)
    cond_i = ok_spec and ok_deff and ok_eta
    if cond_i and ok_centred:
        verdict = "REDUCES"
    elif cond_i or any(by_dim.values()):
        verdict = "PARTLY REDUCES"
    else:
        verdict = "DOES NOT REDUCE"

    # C2.4 α windows (descriptive)
    grid = np.round(np.arange(0.01, 5.0001, 0.01), 2)
    windows = []
    for d in range(2, 7):
        for L in sorted({L for _, dd, L in TORI if dd == d} | {32, 64, 128}) + [None]:
            if d >= 4 and L is not None and L < 32:
                continue
            ds = np.array([closed_decomp(a, L, d)[0] for a in grid])
            hit = grid[ds == d + 1]
            vals = sorted(set(int(x) for x in ds))
            windows.append({"d": d, "L": "inf" if L is None else L,
                            "d_eff_values_seen": vals,
                            "alpha_lo": float(hit.min()) if len(hit) else None,
                            "alpha_hi": float(hit.max()) if len(hit) else None,
                            "window_contiguous": bool(len(hit) and
                                                      np.allclose(np.diff(hit), 0.01)),
                            "frac_of_grid": float(len(hit) / len(grid))})
    bad = [r for r in rows if r["spec_rel_dev"] >= 1e-8]
    posthoc = {"n_configs_failing_1e-8": len(bad),
               "all_failing_have_eps_cut_active": all(r["posthoc_eps_cut_active"] for r in bad),
               "max_spec_rel_dev_no_eps_cut": max(r["posthoc_spec_rel_dev_no_eps_cut"] for r in rows),
               "note": "post-hoc diagnostic, not part of the pre-registered rule"}
    return {"rows": rows, "windows": windows, "posthoc": posthoc,
            "checks": {"spectrum_matches_closed_form_1e-8": ok_spec,
                       "d_eff_closed_eq_phaseA_eq_analyze_node": ok_deff,
                       "eta_closed_within_1e-6_of_phaseA": ok_eta,
                       "centred_d_eff_eq_d": ok_centred,
                       "by_dimension_condition_i": by_dim,
                       "max_spec_rel_dev": max(r["spec_rel_dev"] for r in rows),
                       "max_eta_dev": max(r["eta_dev_vs_phaseA"] for r in rows),
                       "max_vertex_transitive_dev": max(r["vertex_transitive_dev"] for r in rows)},
            "verdict_by_letter_of_rule": verdict}


# ── CCA-1b ───────────────────────────────────────────────────────────────────

def central(t, y):
    t, y = np.asarray(t), np.asarray(y)
    return t[1:-1], (y[2:] - y[:-2]) / (t[2:] - t[:-2])


def uniform_check(L: int, cbar: float) -> tuple[float, int]:
    """analyze_node on an L×L torus with every edge weight −ln c̄, α = 1."""
    G = torus(2, L)
    nx.set_edge_attributes(G, max(-np.log(max(cbar, 1e-8)), 1e-8), "weight")
    r = analyze_node(G, next(iter(G.nodes())), KernelType.EXPONENTIAL, alpha=1.0)
    return r.eta, r.d_eff


def cca1b() -> dict:
    D = json.load(open(PHASE_D))
    pts, curves = [], {}
    for key, c in D.items():
        q, L = c["q"], c["L"]
        t = np.array(c["T_ratios"])
        cbar = np.array(c["mean_corrs"])
        ap = -np.log(cbar)
        pred = [closed_decomp(a, L, 2) for a in ap]
        eta_p = np.array([e for _, e in pred])
        deff_p = np.array([de for de, _ in pred])
        eta_m = np.array(c["etas"])
        td, de_m = central(t, eta_m)
        _, de_p = central(t, eta_p)
        _, dap = central(t, ap)
        _, dc = central(t, cbar)
        i_m, i_p = int(np.argmax(np.abs(de_m))), int(np.argmax(np.abs(de_p)))
        # lens factor |H'| at the measured S_max point = |dη_pred/dT| / |dα′/dT|
        lens = abs(de_p[i_m]) / abs(dap[i_m]) if dap[i_m] != 0 else float("nan")
        curves[key] = {
            "q": q, "L": L,
            "S_max_meas": float(np.abs(de_m).max()), "S_max_meas_recorded": c["S_max"],
            "S_max_meas_T": float(td[i_m]),
            "S_max_pred": float(np.abs(de_p).max()), "S_max_pred_T": float(td[i_p]),
            "max_dalpha_dT": float(np.abs(dap).max()),
            "max_dcbar_dT": float(np.abs(dc).max()),
            "lens_at_Smax_meas": float(lens),
            "R2_eta": float(1 - ((eta_m - eta_p) ** 2).sum() / ((eta_m - eta_m.mean()) ** 2).sum()),
            "rms_resid": float(np.sqrt(((eta_m - eta_p) ** 2).mean())),
            "d_eff_meas_mean_range": [float(min(c["d_effs"])), float(max(c["d_effs"]))],
            "d_eff_pred_values": sorted(set(int(x) for x in deff_p)),
        }
        for i in range(len(t)):
            pts.append({"q": q, "L": L, "T_ratio": float(t[i]), "cbar": float(cbar[i]),
                        "alpha_prime": float(ap[i]), "eta_meas": float(eta_m[i]),
                        "eta_pred": float(eta_p[i]), "d_eff_meas": c["d_effs"][i],
                        "d_eff_pred": int(deff_p[i])})
    em = np.array([p["eta_meas"] for p in pts]); ep = np.array([p["eta_pred"] for p in pts])
    R2 = float(1 - ((em - ep) ** 2).sum() / ((em - em.mean()) ** 2).sum())
    ratios = {}
    for L in (16, 32, 48):
        a, b = curves[f"q10_L{L}"], curves[f"q2_L{L}"]
        Rm, Rp = a["S_max_meas"] / b["S_max_meas"], a["S_max_pred"] / b["S_max_pred"]
        ratios[L] = {"R_meas": Rm, "R_pred": Rp, "R_pred_over_R_meas": Rp / Rm,
                     "energy_factor_ratio_dalpha": a["max_dalpha_dT"] / b["max_dalpha_dT"],
                     "energy_factor_ratio_dcbar": a["max_dcbar_dT"] / b["max_dcbar_dT"],
                     "lens_ratio_at_Smax": a["lens_at_Smax_meas"] / b["lens_at_Smax_meas"]}
    ratio_ok = all(0.5 <= r["R_pred_over_R_meas"] <= 2.0 for r in ratios.values())
    if R2 >= 0.90 and ratio_ok:
        verdict = "REDUCES"
    elif R2 >= 0.50:
        verdict = "PARTLY REDUCES"
    else:
        verdict = "DOES NOT REDUCE"

    # uniform-weight identity spot checks (closed form vs analyze_node on a uniform torus)
    spot = []
    for p in pts[::25]:
        eta_u, d_u = uniform_check(p["L"], p["cbar"])
        spot.append({"q": p["q"], "L": p["L"], "T_ratio": p["T_ratio"], "eta_uniform": eta_u,
                     "eta_closed": p["eta_pred"], "d_uniform": d_u, "d_closed": p["d_eff_pred"]})

    # Phase C secondary (L = 16)
    C = json.load(open(PHASE_C))
    phc = {}
    for q in (2, 10):
        rs = sorted([r for r in C if r["q"] == q], key=lambda r: r["T_ratio"])
        t = np.array([r["T_ratio"] for r in rs])
        ap = -np.log(np.array([r["mean_abs_correlation"] for r in rs]))
        eta_p = np.array([closed_decomp(a, 16, 2)[1] for a in ap])
        eta_m = np.array([r["mean_eta"] for r in rs])
        _, dm = central(t, eta_m); _, dp = central(t, eta_p)
        phc[q] = {"T_ratios": t.tolist(), "eta_meas": eta_m.tolist(), "eta_pred": eta_p.tolist(),
                  "S_max_meas": float(np.abs(dm).max()), "S_max_pred": float(np.abs(dp).max()),
                  "rms_resid": float(np.sqrt(((eta_m - eta_p) ** 2).mean()))}
    em = np.concatenate([np.array(phc[q]["eta_meas"]) for q in (2, 10)])
    ep = np.concatenate([np.array(phc[q]["eta_pred"]) for q in (2, 10)])
    phc["R2_pooled"] = float(1 - ((em - ep) ** 2).sum() / ((em - em.mean()) ** 2).sum())
    return {"points": pts, "curves": curves, "R2_pooled": R2, "ratios": ratios,
            "ratio_ok_all_L": ratio_ok, "uniform_spot_checks": spot, "phase_C": phc,
            "verdict": verdict}


# ── Secondary: χ participation ratio at T_c, q = 2 ───────────────────────────

def chi_secondary() -> dict:
    rows = [r for r in csv.DictReader(open(PHASE_E_CFG))
            if int(r["q"]) == 2 and abs(float(r["T_ratio"]) - 1.0) < 1e-9]
    by_L = {int(r["L"]): {"d_full": float(r["d_full"]), "d_full_sem": float(r["d_full_sem"]),
                          "M2": float(r["M2"]), "inv_M2_sq": 1 / float(r["M2"]) ** 2}
            for r in rows}
    ratio = by_L[32]["d_full"] / by_L[16]["d_full"]
    near3 = all(abs(v["d_full"] - 3) <= 0.3 for v in by_L.values())
    return {"by_L": by_L, "ratio_32_16": ratio, "ratio_in_[1.15,1.6]": 1.15 <= ratio <= 1.6,
            "all_within_0.3_of_3": near3, "asymptotic_prediction": 2 ** 0.5}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    c2, c1b, sec = cca2(), cca1b(), chi_secondary()
    for name, rows in (("cca2_phaseA.csv", c2["rows"]), ("cca2_alpha_windows.csv", c2["windows"]),
                       ("cca1b_phaseD_points.csv", c1b["points"])):
        with open(OUT / name, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    summary = {
        "preregistration_commit": "9a3c125",
        "cca2": {"verdict_by_letter_of_rule": c2["verdict_by_letter_of_rule"],
                 "checks": c2["checks"], "posthoc": c2["posthoc"]},
        "cca1b": {"verdict": c1b["verdict"], "R2_pooled": c1b["R2_pooled"],
                  "ratios": c1b["ratios"], "ratio_ok_all_L": c1b["ratio_ok_all_L"],
                  "curves": c1b["curves"], "uniform_spot_checks": c1b["uniform_spot_checks"],
                  "phase_C": c1b["phase_C"]},
        "secondary_chi_PR_q2_Tc": sec,
    }
    json.dump(summary, open(OUT / "summary.json", "w"), indent=2, default=float)
    print(json.dumps({"cca2": summary["cca2"], "cca1b_verdict": c1b["verdict"],
                      "R2": c1b["R2_pooled"], "ratios": c1b["ratios"],
                      "phaseC_R2": c1b["phase_C"]["R2_pooled"], "secondary": sec},
                     indent=1, default=float))


if __name__ == "__main__":
    main()
