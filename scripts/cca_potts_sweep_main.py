"""
cca_potts_sweep_main.py — Orchestrator for CCA Potts q=2,5,7,10 sweep.

Executes the experiment defined in:
  docs/experiments/CCA_POTTS_SWEEP_SPEC.md
  docs/experiments/CCA_POTTS_SWEEP_DERIVATIONS.md (§7 conventions)

Run modes:
  --mode warmup       : q=2, L=16, one replica, one T_ratio (end-to-end test)
  --mode full         : full 108-config × 5-replica sweep per spec §3.2
  --mode custom       : pass explicit q-list, L-list, T-ratios, replicas
  --mode single       : single (q, L, T, replica) — for debug

Outputs under data/reports/cca_potts_sweep_2026/:
  raw/run_q{q}_L{L}_T{Tidx}_rep{rep}.npz   per-run eigenspectrum, C_r, GTE histograms
  derived/observables_by_config.csv        all scalar observables per (q,L,T,rep)
  derived/observables_mean_sem.csv         replica-averaged means + SEM
  analysis/reduction_check_table.csv       FSS comparison at T_c per q,L
  analysis/brown_comparison_table.csv      discrim_d_eff, discrim_eta, discrim_GTE per q
  analysis/outcome_classification.json     A/B/C verdict
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from potts_mc_optimized import (
    potts_tc, compute_chi_ij, compute_two_point_decay,
    compute_magnetic_susceptibility,
)
from cca_observables import extract_cca_observables, fit_eta_std
from gte_analysis import run_glauber_with_gte
from reduction_check_fss import (
    POTTS_2D_EXPONENTS, zeta_theory, classify_reduction,
)


# ── Sweep grid (spec §3.2) ───────────────────────────────────────────────────

Q_VALUES = [2, 5, 7, 10]
L_VALUES = [16, 24, 32]
T_RATIOS = [0.90, 0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05, 1.10]
N_REPLICAS = 5

N_EQUIL_DEFAULT = 10_000
N_MEASURE_DEFAULT = 20_000
SAMPLE_EVERY = 10

OUT_ROOT = Path("data/reports/cca_potts_sweep_2026")
RAW_DIR = OUT_ROOT / "raw"
DERIVED_DIR = OUT_ROOT / "derived"
ANALYSIS_DIR = OUT_ROOT / "analysis"


# ── Per-run helpers ──────────────────────────────────────────────────────────

def run_seed(q: int, L: int, T_idx: int, replica_idx: int) -> int:
    """Deterministic seed from (q, L, T_idx, replica)."""
    key = f"cca_potts_{q}_{L}_{T_idx}_{replica_idx}"
    h = hashlib.md5(key.encode()).hexdigest()
    return int(h[:8], 16)


def init_state_for_T(T_ratio: float, q: int) -> str:
    """
    Spec §3.3 + Brown Suppl.: near first-order T_c use half_half init to avoid
    phase trapping. Deeply ordered (T < 0.9 T_c): ordered init. T >= T_c:
    disordered. At T ≈ T_c for first-order (q ≥ 5), half_half.
    """
    if T_ratio < 0.90:
        return "ordered"
    elif T_ratio >= 1.02:
        return "disordered"
    elif q >= 5:
        return "half_half"
    else:
        return "disordered"


def n_equil_for(T_ratio: float, q: int, base: int = N_EQUIL_DEFAULT) -> int:
    """Spec §3.3: double equilibration near T_c for first-order q."""
    if q >= 5 and 0.95 <= T_ratio <= 1.05:
        return 2 * base
    return base


def run_one_config(q: int, L: int, T_ratio: float, T_idx: int,
                    replica_idx: int, n_equil: int = None,
                    n_measure: int = N_MEASURE_DEFAULT,
                    save_spectrum: bool = True) -> dict:
    """
    Run one (q, L, T, replica) — returns observables dict.
    Saves per-run spectrum + GTE histograms to raw/ if save_spectrum=True.
    """
    Tc = potts_tc(q)
    T = T_ratio * Tc
    seed = run_seed(q, L, T_idx, replica_idx)
    init_state = init_state_for_T(T_ratio, q)
    n_eq = n_equil if n_equil is not None else n_equil_for(T_ratio, q)

    t0 = time.time()
    r = run_glauber_with_gte(
        L=L, q=q, T=T, seed=seed,
        n_equil=n_eq, n_measure=n_measure,
        sample_every=SAMPLE_EVERY, init_state=init_state,
    )
    t_mc = time.time() - t0

    # CCA observables from χ
    chi = compute_chi_ij(r["samples"], q=q)
    cca = extract_cca_observables(chi)

    # Standard 2-point decay fit (for η_std extraction at T_c)
    rv, Cr_conn = compute_two_point_decay(r["samples"], q=q, connected=True)
    eta_std_fit = fit_eta_std(rv, Cr_conn)

    # Magnetic susceptibility
    chi_mag = compute_magnetic_susceptibility(r["mags"], L)

    t_total = time.time() - t0

    out = {
        "q": q, "L": L, "T_ratio": T_ratio, "T_idx": T_idx, "replica": replica_idx,
        "T": float(T), "T_c": float(Tc),
        "seed": seed, "init_state": init_state,
        "n_equil": n_eq, "n_measure": n_measure, "n_samples": int(r["meta"]["n_samples"]),
        "t_mc": t_mc, "t_total": t_total,
        # CCA observables
        "d_eff_CCA": cca.d_eff_CCA,
        "eta_CCA": cca.eta_CCA,
        "eta_CCA_r2": cca.eta_CCA_r2,
        "eta_CCA_range_min": cca.eta_CCA_range[0],
        "eta_CCA_range_max": cca.eta_CCA_range[1],
        "lambda_max": cca.lambda_max,
        "n_positive_eig": cca.n_positive_eig,
        # Standard exponents
        "eta_std_fit": eta_std_fit["eta_std"],
        "eta_std_r2": eta_std_fit["r2"],
        "eta_std_n_points": eta_std_fit["n_points"],
        # GTE
        "G_bits": r["gte"]["G"],
        "G_nats": r["gte"]["G_nats"],
        "G_n_samples": r["gte"]["n_samples"],
        # Thermo
        "mag_mean": float(r["mags"].mean()),
        "mag_std": float(r["mags"].std()),
        "mag_sq_mean": float((r["mags"] ** 2).mean()),
        "chi_mag": float(chi_mag),
        "energy_mean": float(r["energies"].mean()),
        "energy_std": float(r["energies"].std()),
    }

    if save_spectrum:
        spectrum = np.linalg.eigvalsh(chi)[::-1]  # descending
        raw_file = RAW_DIR / f"run_q{q}_L{L}_T{T_idx}_rep{replica_idx}.npz"
        np.savez_compressed(
            raw_file,
            spectrum=spectrum.astype(np.float64),
            C_r_conn=Cr_conn.astype(np.float64),
            r_vals=rv.astype(np.float64),
            hist_joint=r["hist_joint"],
            hist_marg=r["hist_marg"],
            mags=r["mags"].astype(np.float32),
            energies=r["energies"].astype(np.float32),
            meta=json.dumps(out),
        )

    return out


# ── Aggregation (replica-average) ────────────────────────────────────────────

def aggregate_replicas(rows: list[dict]) -> list[dict]:
    """Group by (q, L, T_idx), compute mean + SEM of each scalar observable."""
    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        key = (r["q"], r["L"], r["T_idx"])
        groups[key].append(r)
    NUMERIC_KEYS = [
        "d_eff_CCA", "eta_CCA", "eta_CCA_r2", "lambda_max",
        "eta_std_fit", "eta_std_r2", "G_bits", "G_nats",
        "mag_mean", "mag_sq_mean", "chi_mag", "energy_mean",
    ]
    agg = []
    for (q, L, T_idx), rs in sorted(groups.items()):
        row = {"q": q, "L": L, "T_idx": T_idx,
               "T_ratio": rs[0]["T_ratio"], "T": rs[0]["T"], "T_c": rs[0]["T_c"],
               "n_replicas": len(rs), "init_state": rs[0]["init_state"]}
        for k in NUMERIC_KEYS:
            vals = np.array([r[k] for r in rs if not np.isnan(r[k])], dtype=np.float64)
            if len(vals) > 0:
                row[f"{k}_mean"] = float(vals.mean())
                row[f"{k}_sem"] = float(vals.std(ddof=1) / np.sqrt(len(vals))) if len(vals) > 1 else 0.0
            else:
                row[f"{k}_mean"] = float("nan")
                row[f"{k}_sem"] = float("nan")
        agg.append(row)
    return agg


def write_csv(rows: list[dict], path: Path) -> None:
    import csv
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    # Ensure consistent field set — union of all keys
    for r in rows:
        for k in r:
            if k not in fieldnames:
                fieldnames.append(k)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


# ── Mode runners ─────────────────────────────────────────────────────────────

def run_warmup():
    """End-to-end smoke test: q=2, L=16, T=T_c, single replica, reduced n_measure."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(">>> WARMUP: q=2, L=16, T=T_c, single replica (n_measure=5000)")
    t0 = time.time()
    row = run_one_config(
        q=2, L=16, T_ratio=1.0, T_idx=4, replica_idx=0,
        n_equil=5000, n_measure=5000, save_spectrum=True,
    )
    dt = time.time() - t0
    print(f"\n=== Warmup complete in {dt:.1f}s ===")
    print(f"  d_eff_CCA = {row['d_eff_CCA']:.2f}")
    print(f"  eta_CCA   = {row['eta_CCA']:.3f} ± {row['eta_CCA_r2']:.3f}")
    print(f"    (theory ζ = {zeta_theory(2):.3f} asymptotic; finite-L reduction expected)")
    print(f"  eta_std   = {row['eta_std_fit']:.3f} R²={row['eta_std_r2']:.3f} ({row['eta_std_n_points']} pts)")
    print(f"  G (bits)  = {row['G_bits']:.4f}")
    print(f"  <m>       = {row['mag_mean']:.3f}")
    print(f"  chi_mag   = {row['chi_mag']:.2f}")
    print(f"  MC runtime: {row['t_mc']:.1f}s")
    print(f"\nFull sweep estimate: {dt:.1f}s × 540 configs = {dt*540/60:.1f} min "
          f"(serial, 1× measurement density)")
    return row


def run_custom(q_list, L_list, T_ratios, n_replicas, n_measure):
    """Flexible subset sweep."""
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    total = len(q_list) * len(L_list) * len(T_ratios) * n_replicas
    i = 0
    t_start = time.time()
    for q in q_list:
        for L in L_list:
            for T_idx, T_ratio in enumerate(T_ratios):
                for rep in range(n_replicas):
                    i += 1
                    t0 = time.time()
                    row = run_one_config(
                        q=q, L=L, T_ratio=T_ratio, T_idx=T_idx,
                        replica_idx=rep, n_measure=n_measure,
                    )
                    rows.append(row)
                    elapsed = time.time() - t_start
                    eta = elapsed * (total - i) / i
                    print(f"[{i}/{total}] q={q} L={L} T/Tc={T_ratio:.2f} rep={rep}: "
                          f"d_eff={row['d_eff_CCA']:.2f} eta_CCA={row['eta_CCA']:.3f} "
                          f"G={row['G_bits']:.3f} <m>={row['mag_mean']:.3f} "
                          f"({time.time()-t0:.1f}s; ETA {eta/60:.1f}m)")

    # Save results
    write_csv(rows, DERIVED_DIR / "observables_by_config.csv")
    agg = aggregate_replicas(rows)
    write_csv(agg, DERIVED_DIR / "observables_mean_sem.csv")
    print(f"\n=== Sweep complete in {(time.time()-t_start)/60:.1f} min ===")
    print(f"  Observables: {DERIVED_DIR}/observables_by_config.csv")
    print(f"  Aggregated:  {DERIVED_DIR}/observables_mean_sem.csv")
    return rows, agg


def run_full():
    return run_custom(Q_VALUES, L_VALUES, T_RATIOS, N_REPLICAS, N_MEASURE_DEFAULT)


def run_single(q: int, L: int, T_ratio: float, replica: int):
    """Single-config debug runner."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    row = run_one_config(q=q, L=L, T_ratio=T_ratio,
                         T_idx=0, replica_idx=replica)
    print(json.dumps({k: v for k, v in row.items() if not isinstance(v, (dict, tuple))},
                     indent=2, default=str))
    return row


# ── CLI ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["warmup", "full", "custom", "single"],
                    default="warmup")
    ap.add_argument("--q", type=int, nargs="+", help="q values (for custom/single)")
    ap.add_argument("--L", type=int, nargs="+", help="L values")
    ap.add_argument("--T-ratios", type=float, nargs="+")
    ap.add_argument("--replicas", type=int, default=5)
    ap.add_argument("--n-measure", type=int, default=N_MEASURE_DEFAULT)
    ap.add_argument("--single-q", type=int)
    ap.add_argument("--single-L", type=int)
    ap.add_argument("--single-T-ratio", type=float, default=1.0)
    ap.add_argument("--single-replica", type=int, default=0)
    args = ap.parse_args()

    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    if args.mode == "warmup":
        run_warmup()
    elif args.mode == "full":
        run_full()
    elif args.mode == "custom":
        if not all([args.q, args.L, args.T_ratios]):
            ap.error("--mode custom requires --q, --L, --T-ratios")
        run_custom(args.q, args.L, args.T_ratios, args.replicas, args.n_measure)
    elif args.mode == "single":
        if not all([args.single_q, args.single_L]):
            ap.error("--mode single requires --single-q, --single-L")
        run_single(args.single_q, args.single_L, args.single_T_ratio, args.single_replica)


if __name__ == "__main__":
    main()
