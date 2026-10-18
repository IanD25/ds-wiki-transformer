"""
cca1c_lambda1_reduction.py — CCA-1c λ₁ reduction test on the saved Phase E spectra.

Pre-registration: docs/experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md §1.
No Monte Carlo: reads data/reports/cca_potts_sweep_2026/raw/*.npz only.

Per run:
  d_full   = (Σλ)²/Σλ²   (λ > 1e-10·λ₁, as in cca_observables.extract_cca_observables)
  f1       = λ₁/Σλ
  d_l1only = 1/f1²
  d_bulk   = PR of λ_{j≥2};  d_bulk2 = PR of λ_{j≥3}
  M2       = ⟨M²⟩ from the stored magnetisation series
Identity: 1/d_full = f1² + (1−f1)²/d_bulk  (exact, given the same eigenvalue set).

Outputs → data/reports/cca1c_lambda1_reduction_2026_10/
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/reports/cca_potts_sweep_2026/raw"
BROWN = ROOT / "data/reports/cca_potts_sweep_2026/analysis/brown_comparison_table.csv"
OUT = ROOT / "data/reports/cca1c_lambda1_reduction_2026_10"

T_LO, T_HI = 0.99, 1.01
FIRST_ORDER_Q = (5, 7, 10)


def pr(x: np.ndarray) -> float:
    s2 = (x ** 2).sum()
    return float(x.sum() ** 2 / s2) if s2 > 0 else float("nan")


def d_from(f1: float, d_bulk: float) -> float:
    return 1.0 / (f1 ** 2 + (1.0 - f1) ** 2 / d_bulk)


def per_run(path: Path) -> dict:
    z = np.load(path, allow_pickle=True)
    meta = json.loads(str(z["meta"]))
    lam = np.sort(z["spectrum"])[::-1]
    lam = lam[lam > 1e-10 * max(lam[0], 1.0)]
    total = lam.sum()
    q, L = meta["q"], meta["L"]
    mags = z["mags"].astype(np.float64)
    f1 = lam[0] / total
    return {
        "q": q, "L": L, "T_ratio": round(meta["T_ratio"], 4), "rep": meta["replica"],
        "init_state": meta["init_state"],
        "d_full": pr(lam), "d_full_phaseE": meta["d_eff_CCA"],
        "trace_over_Nq1": total / (L * L * (q - 1)),
        "lambda1": lam[0], "lambda2": lam[1],
        "f1": f1, "d_l1only": 1.0 / f1 ** 2,
        "d_bulk": pr(lam[1:]), "d_bulk2": pr(lam[2:]),
        "M2": float((mags ** 2).mean()),
        "f1_over_M2": f1 / float((mags ** 2).mean()),
        "chi_mag": meta["chi_mag"], "eta_CCA": meta["eta_CCA"], "G_bits": meta["G_bits"],
    }


def agg(rows: list[dict]) -> list[dict]:
    keys = ["d_full", "d_full_phaseE", "trace_over_Nq1", "lambda1", "lambda2", "f1",
            "d_l1only", "d_bulk", "d_bulk2", "M2", "f1_over_M2", "chi_mag", "eta_CCA", "G_bits"]
    groups: dict = {}
    for r in rows:
        groups.setdefault((r["q"], r["L"], r["T_ratio"]), []).append(r)
    out = []
    for (q, L, T), g in sorted(groups.items()):
        rec = {"q": q, "L": L, "T_ratio": T, "n_rep": len(g),
               "init_states": "/".join(sorted({x["init_state"] for x in g}))}
        for k in keys:
            v = np.array([x[k] for x in g], dtype=np.float64)
            rec[k] = float(v.mean())
            rec[k + "_sem"] = float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else 0.0
        out.append(rec)
    return out


def jump(a: float, b: float) -> float:
    return (b - a) / abs(a)


def shapley_f1_share(f_lo, db_lo, f_hi, db_hi) -> float:
    ln = lambda f, d: np.log(d_from(f, d))
    total = ln(f_hi, db_hi) - ln(f_lo, db_lo)
    phi_f1 = 0.5 * ((ln(f_hi, db_lo) - ln(f_lo, db_lo)) + (ln(f_hi, db_hi) - ln(f_lo, db_hi)))
    return float(phi_f1 / total) if total != 0 else float("nan")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = [per_run(p) for p in sorted(RAW.glob("run_*.npz"))]
    cfg = agg(rows)
    brown = {(int(r["q"]), int(r["L"])): r for r in csv.DictReader(open(BROWN))}

    with open(OUT / "per_run.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    with open(OUT / "by_config.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cfg[0]))
        w.writeheader(); w.writerows(cfg)

    idx = {(c["q"], c["L"], c["T_ratio"]): c for c in cfg}
    jumps = []
    for q in (2, 5, 7, 10):
        for L in (16, 24, 32):
            lo, hi = idx[(q, L, T_LO)], idx[(q, L, T_HI)]
            rec = {"q": q, "L": L}
            for k in ("d_full", "d_l1only", "d_bulk", "d_bulk2", "f1", "eta_CCA", "G_bits"):
                rec["J_" + k] = jump(lo[k], hi[k])
            rec["d_full_lo"], rec["d_full_hi"] = lo["d_full"], hi["d_full"]
            rec["d_bulk_lo"], rec["d_bulk_hi"] = lo["d_bulk"], hi["d_bulk"]
            rec["f1_lo"], rec["f1_hi"] = lo["f1"], hi["f1"]
            rec["f1_share"] = shapley_f1_share(lo["f1"], lo["d_bulk"], hi["f1"], hi["d_bulk"])
            rec["dlog_d_full"] = float(np.log(hi["d_full"] / lo["d_full"]))
            rec["dlog_d_bulk"] = float(np.log(hi["d_bulk"] / lo["d_bulk"]))
            jumps.append(rec)
    j2 = {r["L"]: r for r in jumps if r["q"] == 2}
    for r in jumps:
        b = j2[r["L"]]
        for k in ("d_full", "d_bulk", "d_bulk2", "G_bits"):
            r["D_" + k] = r["J_" + k] / b["J_" + k]
        r["D_G_phaseE"] = float(brown[(r["q"], r["L"])]["discrim_G"]) if r["q"] != 2 else 1.0
        r["D_dfull_phaseE"] = float(brown[(r["q"], r["L"])]["discrim_d_eff"]) if r["q"] != 2 else 1.0
    with open(OUT / "jumps.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(jumps[0]))
        w.writeheader(); w.writerows(jumps)

    # ── Pre-registered verdict (§1.5) ──
    def reduces(r):
        return r["f1_share"] >= 0.90 and r["D_d_bulk"] <= r["D_G_phaseE"]

    def survives(r):
        return r["D_d_bulk"] > r["D_G_phaseE"] and r["f1_share"] < 0.90

    fo = [r for r in jumps if r["q"] in FIRST_ORDER_Q]
    red_L32 = all(reduces(r) for r in fo if r["L"] == 32)
    red_perq = all(sum(reduces(r) for r in fo if r["q"] == q) >= 2 for q in FIRST_ORDER_Q)
    surv = sum(survives(r) for r in fo if r["L"] == 32) >= 2
    verdict = "REDUCES" if (red_L32 and red_perq) else ("SURVIVES" if surv else "MIXED")

    # I2 check: f1/<M²> in [1.0, 1.15] where f1 > 0.3
    i2 = [c for c in cfg if c["f1"] > 0.3]
    i2_pass = sum(1.0 - 1e-3 <= c["f1_over_M2"] <= 1.15 for c in i2)

    # Secondary: peak locations of eta_CCA, G, chi_mag at T_ratio >= 0.98
    peaks = []
    for q in (2, 5, 7, 10):
        for L in (16, 24, 32):
            cs = [c for c in cfg if c["q"] == q and c["L"] == L]
            pk = {k: max(cs, key=lambda c: c[k])["T_ratio"] for k in ("eta_CCA", "G_bits", "chi_mag")}
            peaks.append({"q": q, "L": L, **{"peak_" + k: v for k, v in pk.items()}})

    summary = {
        "verdict": verdict,
        "reduces_all_first_order_L32": red_L32,
        "reduces_per_q_2of3_L": red_perq,
        "survives_2of3_L32": surv,
        "identity_check_max_rel_err": max(abs(d_from(r["f1"], r["d_bulk"]) / r["d_full"] - 1) for r in rows),
        "d_full_vs_phaseE_max_rel_err": max(abs(r["d_full"] / r["d_full_phaseE"] - 1) for r in rows),
        "trace_over_Nq1_range": [min(r["trace_over_Nq1"] for r in rows), max(r["trace_over_Nq1"] for r in rows)],
        "I2_pass": f"{i2_pass}/{len(i2)}",
        "I2_f1_over_M2_range": [min(c["f1_over_M2"] for c in i2), max(c["f1_over_M2"] for c in i2)],
        "peaks": peaks,
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps({k: v for k, v in summary.items() if k != "peaks"}, indent=2))
    hdr = ["q", "L", "d_full_lo", "d_full_hi", "f1_lo", "f1_hi", "d_bulk_lo", "d_bulk_hi",
           "f1_share", "J_d_full", "J_d_bulk", "D_d_full", "D_d_bulk", "D_G_phaseE"]
    print("\t".join(hdr))
    for r in jumps:
        print("\t".join(f"{r[k]:.4g}" if isinstance(r[k], float) else str(r[k]) for k in hdr))
    for p in peaks:
        print(p)


if __name__ == "__main__":
    main()
