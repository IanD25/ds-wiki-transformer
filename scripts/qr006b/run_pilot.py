"""QR-006b pilot (pre-registration §7): pipeline validation; results discarded.

Usage (from scripts/):  ../.venv-qr006b/bin/python -m qr006b.run_pilot [--workers 9]

What it computes and reports:
  * the values the pilot sets (S3 sigma, S4 sigma, S5 r_c and sigma);
  * simulation and indicator diagnostics for every stratum (counts, discards,
    segment lengths, NaN rates, timings);
  * the control safety checks (C0, C0g, CM) and the S4 leakage check.
It does NOT compute any information-versus-baseline comparison, or any AUC,
for the test strata S1, S2, S3, S5 and SM (§7; the task's rule 2).
"""

import argparse
import json
import os
import pickle
import platform
import subprocess
import sys
import time
import zlib
from multiprocessing import Pool

import numpy as np

from . import config as C
from . import pilot_settings as PS
from . import pipeline as P
from . import score as S
from . import strata as ST

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW = os.path.join(REPO, "data", "experiments", "qr006b", "pilot")
OUT = os.path.join(REPO, "data", "reports", "qr006b_pilot")

CONTROLS = ("C0", "CM")          # C0g is derived from C0
TESTS = ("S1", "S2", "S3", "S5", "SM")


def c0g_transform(R, sref):
    """§2.1 C0g: strictly increasing map exp(r / s_ref) (Amendment A14)."""
    return np.exp(R / sref)


# ----------------------------------------------------------------- workers --
def _sim_task(args):
    stratum, family, n, root, ps = args
    ST.PILOT_SET.update(ps)
    t0 = time.time()
    pairs, counts = ST.generate_pairs(stratum, family, n, root, ps=ps)
    counts["sim_seconds"] = time.time() - t0
    return stratum, family, pairs, counts


def _ind_task(args):
    stratum, family, pair, variant = args
    tf = c0g_transform if variant == "C0g" else None
    det_tr = [pair["tip"] - j for j in C.DETECT_OFFSETS]
    t0 = time.time()
    tr = P.compute_series(pair["x_tr"], pair["L"], det_tr, transform=tf)
    t1 = time.time()
    nu = P.compute_series(pair["x_null"], pair["L"], [pair["null_det_end"]], transform=tf)
    t2 = time.time()
    return dict(stratum=stratum if variant is None else variant, family=family,
                pair=pair["pair"], split=pair["split"], level=pair["level"],
                tip=pair["tip"], L=pair["L"], tr=tr, nu=nu,
                sec_tr=t1 - t0, sec_nu=t2 - t1)


# ---------------------------------------------------------------- analysis --
def _collect(results, stratum, family):
    rs = sorted([r for r in results if r["stratum"] == stratum and r["family"] == family],
                key=lambda r: r["pair"])
    return rs


def _auc_table(rs, names, learn_all=False):
    """Directions on calibration, AUC on confirmation (§4, §5.1)."""
    cal = [r for r in rs if r["split"] == "calibration"]
    con = [r for r in rs if r["split"] == "confirmation"]
    Tc = np.array([r["tr"]["tau_off"] for r in cal])
    Nc = np.array([r["nu"]["tau_off"] for r in cal])
    dirs = S.directions(names, P.DIRECTION, Tc, Nc, learn_all)
    sgn = np.array([dirs[n] for n in names], float)
    Tq = np.array([r["tr"]["tau_off"] for r in con]) * sgn
    Nq = np.array([r["nu"]["tau_off"] for r in con]) * sgn
    Tcal = Tc * sgn
    Ncal = Nc * sgn
    auc_con = np.array([S.auc(Tq[:, j], Nq[:, j]) for j in range(len(names))])
    auc_cal = np.array([S.auc(Tcal[:, j], Ncal[:, j]) for j in range(len(names))])
    return dict(dirs=dirs, auc=auc_con, auc_cal=auc_cal, T=Tq, N=Nq)


def _family_weighted(values):
    return float(np.mean(values))


def control_checks(results, names_by_stratum):
    """§6.4 controls applied at pilot size; §6.1 YES rule within each control."""
    out = {}
    primary_info = ["I1_mi", "I3_pe", "I4_sampen", "I5_fi", "I6_rpde"]
    for stratum, fams in (("C0", ST.FAMILIES["C0"]), ("C0g", ST.FAMILIES["C0"]),
                          ("CM", ST.FAMILIES["CM"])):
        names = names_by_stratum["CM" if stratum == "CM" else "C0"]
        info = primary_info + (["I2_te"] if stratum == "CM" else [])
        base = [n for n in names if n in P.BASE]
        tabs = {f: _auc_table(_collect(results, stratum, f), names) for f in fams}
        # family (a) = mean over its models (Amendment A18); (b) = its one model
        fa = [f for f in fams if f.startswith("a_")]
        fb = [f for f in fams if f.startswith("b_")]
        auc_a = np.mean([tabs[f]["auc"] for f in fa], axis=0)
        auc_b = np.mean([tabs[f]["auc"] for f in fb], axis=0)
        cal_pooled = np.mean([tabs[f]["auc_cal"] for f in fams], axis=0)
        pooled = 0.5 * (auc_a + auc_b)
        bi = [names.index(b) for b in base]
        best = base[int(np.nanargmax(cal_pooled[bi]))]
        jb = names.index(best)
        # bootstrap of pooled delta-AUC: resample within each model, same
        # resample for all indicators (§5.6)
        boots = {}
        for f in fams:
            boots[f] = S.bootstrap_auc(tabs[f]["T"], tabs[f]["N"], C.N_BOOT, seed=zlib.crc32(f.encode()))
        ba = np.mean([boots[f] for f in fa], axis=0)
        bb = np.mean([boots[f] for f in fb], axis=0)
        bp = 0.5 * (ba + bb)
        rows = {}
        pvals = []
        for n in info:
            j = names.index(n)
            d = pooled[j] - pooled[jb]
            dboot = bp[:, j] - bp[:, jb]
            p = float(np.mean(dboot <= 0))
            pvals.append(p)
            rows[n] = dict(auc_a=float(auc_a[j]), auc_b=float(auc_b[j]), auc_pooled=float(pooled[j]),
                           delta_vs_best=float(d), ci95=[float(np.percentile(dboot, 2.5)),
                                                          float(np.percentile(dboot, 97.5))],
                           p_one_sided=p, delta_a=float(auc_a[j] - auc_a[jb]),
                           delta_b=float(auc_b[j] - auc_b[jb]))
        padj = S.holm(pvals)
        yes = []
        for n, pa in zip(info, padj):
            r = rows[n]
            r["p_holm"] = float(pa)
            r["meets_yes_rule"] = bool(r["delta_vs_best"] >= C.DELTA_AUC_MIN and pa < 0.05
                                       and r["delta_a"] > 0 and r["delta_b"] > 0)
            r["clean_negative"] = bool(r["ci95"][1] < C.DELTA_AUC_MIN)
            if r["meets_yes_rule"]:
                yes.append(n)
        out[stratum] = dict(best_baseline=best, best_baseline_auc_pooled=float(pooled[jb]),
                            info=rows, any_info_meets_yes=bool(yes), yes=yes,
                            baselines={b: float(pooled[names.index(b)]) for b in base})
    # C0g invariances (§6.4)
    inv = {}
    for f in ST.FAMILIES["C0"]:
        r0 = _collect(results, "C0", f)
        rg = _collect(results, "C0g", f)
        names = names_by_stratum["C0"]
        jpe = names.index("I3_pe")
        jr = names.index("B2_rank_ac1")
        dpe = max(max(abs(a["tr"]["tau_off"][jpe] - b["tr"]["tau_off"][jpe]),
                      abs(a["nu"]["tau_off"][jpe] - b["nu"]["tau_off"][jpe])) for a, b in zip(r0, rg))
        drk = max(max(abs(a["tr"]["tau_off"][jr] - b["tr"]["tau_off"][jr]),
                      abs(a["nu"]["tau_off"][jr] - b["nu"]["tau_off"][jr])) for a, b in zip(r0, rg))
        t0 = _auc_table(r0, names)
        tg = _auc_table(rg, names)
        jm = names.index("I1_mi")
        ja = names.index("B1_ac1")
        inv[f] = dict(pe_tau_max_abs_diff=float(dpe), rank_ac1_tau_max_abs_diff=float(drk),
                      mi_auc_diff=float(tg["auc"][jm] - t0["auc"][jm]),
                      ac1_auc_C0=float(t0["auc"][ja]), ac1_auc_C0g=float(tg["auc"][ja]))
    out["C0g_invariance"] = inv
    return out


def s4_leakage(results, names):
    out = {}
    for f in ST.FAMILIES["S4"]:
        tab = _auc_table(_collect(results, "S4", f), names)
        out[f] = {n: float(a) for n, a in zip(names, tab["auc"])}
    flat = [a for f in out for a in out[f].values() if np.isfinite(a)]
    ok = all(abs(a - 0.5) <= 0.1 for a in flat)
    bad = [(f, n, a) for f in out for n, a in out[f].items() if np.isfinite(a) and abs(a - 0.5) > 0.1]
    return dict(auc=out, all_within=ok, outside=bad)


def online_pipeline_check(results, stratum, names):
    """Exercise the lead-time and detection code. Values are reported only for
    control strata; for test strata only structural diagnostics."""
    rep = {}
    for f in ST.FAMILIES.get(stratum, []):
        rs = _collect(results, stratum, f)
        cal = [r for r in rs if r["split"] == "calibration"]
        con = [r for r in rs if r["split"] == "confirmation"]
        fam = {}
        Tc = np.array([r["tr"]["tau_off"] for r in cal])
        Nc = np.array([r["nu"]["tau_off"] for r in cal])
        dirs = S.directions(names, P.DIRECTION, Tc, Nc)
        n_on = rs[0]["tr"]["tau_on"].shape[1]          # x_fi_raw is offline only
        for j, n in enumerate(names[:n_on]):
            sgn = dirs[n]
            th = S.far_threshold([sgn * r["nu"]["tau_on"][:, j] for r in cal])
            lt = S.lead_times([sgn * r["tr"]["tau_on"][:, j] for r in con],
                              [r["tr"]["ends"] for r in con], [r["tip"] for r in con], th)
            fa = np.mean([S.alarm_index(sgn * r["nu"]["tau_on"][:, j], th) is not None for r in con])
            fam[n] = dict(threshold=th, detect_prob=float(np.mean(np.isfinite(lt))),
                          null_alarm_rate_confirmation=float(fa),
                          median_lead=float(np.nanmedian(lt)) if np.isfinite(lt).any() else None)
        rep[f] = fam
    return rep


def nan_rates(results, stratum, names):
    out = {}
    for f in ST.FAMILIES[stratum] if stratum in ST.FAMILIES else ST.FAMILIES["C0"]:
        rs = _collect(results, stratum, f)
        if not rs:
            continue
        V = np.vstack([np.vstack([r["tr"]["vals_off"], r["nu"]["vals_off"]]) for r in rs])
        tau = np.vstack([np.vstack([r["tr"]["tau_off"], r["nu"]["tau_off"]]) for r in rs])
        det = np.vstack([np.vstack([r["tr"]["det"], r["nu"]["det"]]) for r in rs])
        out[f] = dict(window_nan_frac={n: float(np.isnan(V[:, j]).mean()) for j, n in enumerate(names)
                                       if np.isnan(V[:, j]).any()},
                      tau_nan={n: int(np.isnan(tau[:, j]).sum()) for j, n in enumerate(names)
                               if np.isnan(tau[:, j]).any()},
                      det_nan={n: int(np.isnan(det[:, j]).sum()) for j, n in enumerate(names[:det.shape[1]])
                               if np.isnan(det[:, j]).any()},
                      n_windows_median=int(np.median([len(r["tr"]["ends"]) for r in rs])),
                      window_len_median=int(np.median([r["tr"]["w"] for r in rs])),
                      seg_len=[int(min(r["L"] for r in rs)), int(np.median([r["L"] for r in rs])),
                               int(max(r["L"] for r in rs))],
                      sec_per_series=float(np.mean([0.5 * (r["sec_tr"] + r["sec_nu"]) for r in rs])))
    return out


def _git(*a):
    try:
        return subprocess.check_output(["git", *a], cwd=REPO, text=True).strip()
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=9)
    ap.add_argument("--n", type=int, default=C.N_PER_CLASS_PILOT)
    ap.add_argument("--s4-n", type=int, default=None, help="Amendment A15 extension")
    args = ap.parse_args()
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    root = C.SEED_PILOT
    log = {"started": time.strftime("%Y-%m-%d %H:%M:%S"), "commit": _git("rev-parse", "HEAD"),
           "python": sys.version, "machine": platform.platform(), "workers": args.workers}

    # 1. values the pilot sets
    t0 = time.time()
    ps = {}
    settings = {}
    for fam in ("a_may_high", "b_cubic_high"):
        sig, table = PS.s3_sigma(fam, root)
        ps["S3_sigma_" + fam[0]] = sig
        settings["S3_" + fam] = dict(sigma=sig, flicker_fraction_by_sigma=table)
    for fam in ("a_may_fixed", "b_cubic_fixed"):
        sig, info = PS.s4_sigma(fam, root)
        ps["S4_sigma_" + fam[0]] = sig
        settings["S4_" + fam] = dict(sigma=sig, **info)
    s5 = PS.s5_settings(root)
    for k in ("a", "b"):
        ps[f"S5_rc_{k}"] = s5[k]["rc"]
        ps[f"S5_sigma_{k}"] = s5[k]["sigma"]
    settings["S5"] = s5
    settings["Lever_collapse_delta"] = {}
    from . import models as M
    for d in (4, 20):
        dc, xs = M.lever_collapse_delta(d)
        settings["Lever_collapse_delta"][str(d)] = dict(delta_c=dc, x_start=xs.tolist())
    log["settings_seconds"] = time.time() - t0
    with open(os.path.join(OUT, "pilot_settings.json"), "w") as fh:
        json.dump(settings, fh, indent=2, default=float)
    print("pilot settings:", json.dumps(ps), flush=True)
    if any(v is None for v in ps.values()):
        print("A pilot-set value could not be determined; see pilot_settings.json")
    ST.PILOT_SET.update(ps)

    # 2. simulate
    t0 = time.time()
    tasks = []
    for stratum in ("C0", "CM", "S1", "S2", "S3", "S4", "S5", "SM"):
        n = args.s4_n if (stratum == "S4" and args.s4_n) else args.n
        for fam in ST.FAMILIES[stratum]:
            tasks.append((stratum, fam, n, root, ps))
    with Pool(args.workers) as pool:
        sims = pool.map(_sim_task, tasks, chunksize=1)
    log["simulation_seconds"] = time.time() - t0
    counts = {f"{s}/{f}": c for s, f, _p, c in sims}
    print("simulated", flush=True)

    # 3. indicators
    t0 = time.time()
    itasks = []
    for stratum, fam, pairs, _c in sims:
        for p in pairs:
            itasks.append((stratum, fam, p, None))
            if stratum == "C0":
                itasks.append((stratum, fam, p, "C0g"))
    # longest first for load balance
    itasks.sort(key=lambda a: -(a[2]["x_tr"].size))
    results = []
    with Pool(args.workers) as pool:
        for i, r in enumerate(pool.imap_unordered(_ind_task, itasks, chunksize=1)):
            results.append(r)
            if (i + 1) % 100 == 0:
                print(f"  indicators {i + 1}/{len(itasks)}", flush=True)
    log["indicator_seconds_wall"] = time.time() - t0
    log["indicator_cpu_seconds"] = float(sum(r["sec_tr"] + r["sec_nu"] for r in results))
    log["n_series"] = 2 * len(results)
    with open(os.path.join(RAW, "pilot_results.pkl"), "wb") as fh:
        pickle.dump(dict(results=results, counts=counts, ps=ps), fh)

    # 4. diagnostics and checks
    names1 = P.indicator_names(False)
    namesM = P.indicator_names(True)
    names_by = {"C0": names1, "CM": namesM}
    diag = {}
    for stratum in ("C0", "C0g", "CM", "S1", "S2", "S3", "S4", "S5", "SM"):
        names = namesM if stratum in ("CM", "SM") else names1
        if stratum == "C0g":
            diag[stratum] = {f: nan_rates(results, "C0g", names)[f] for f in ST.FAMILIES["C0"]}
        else:
            diag[stratum] = nan_rates(results, stratum, names)
    checks = control_checks(results, names_by)
    leak = s4_leakage(results, names1)
    online = {s: online_pipeline_check(results, s, names_by.get(s, names1)) for s in ("C0", "CM")}
    # test strata: exercise the online code; keep only structure
    struct = {}
    for s in TESTS + ("S4",):
        names = namesM if s == "SM" else names1
        rep = online_pipeline_check(results, s, names)
        struct[s] = {f: dict(n_indicators=len(v), thresholds_finite=int(sum(
            np.isfinite(x["threshold"]) for x in v.values()))) for f, v in rep.items()}
    log["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    summary = dict(log=log, pilot_set=ps, counts=counts, diagnostics=diag, controls=checks,
                   s4_leakage=leak, online_controls=online, online_structure_tests=struct)
    with open(os.path.join(OUT, "pilot_summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print("C0 any info meets YES:", checks["C0"]["any_info_meets_yes"],
          "| C0g:", checks["C0g"]["any_info_meets_yes"], "| CM:", checks["CM"]["any_info_meets_yes"])
    print("S4 leakage all within 0.5±0.1:", leak["all_within"], leak["outside"])
    print("C0g invariance:", json.dumps(checks["C0g_invariance"]))
    print("timings:", json.dumps({k: v for k, v in log.items() if "seconds" in k}))


if __name__ == "__main__":
    main()
