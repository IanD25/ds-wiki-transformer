"""QR-006b confirmatory analysis and report (pre-registration §5.8, §6).

Blinding (§6.4): `--stage controls` opens only C0, C0g, CM and the S4 leakage
check and writes controls.json. `--stage tests` refuses to run unless
controls.json records that every control passed (or --controls-audited names
the §11 deviation that fixed a failed control and re-ran it on fresh seeds).

Usage (from scripts/):
    ../.venv-qr006b/bin/python -m qr006b.report --stage controls
    ../.venv-qr006b/bin/python -m qr006b.report --stage tests
"""

import argparse
import glob
import json
import os
import pickle
import sys

import numpy as np

from . import analysis as A
from . import config as C
from . import pipeline as P
from . import score as S

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW = os.path.join(REPO, "data", "experiments", "qr006b", "confirmatory", "indicators")
OUT = os.path.join(REPO, "data", "reports", "qr006b")


def load(variant="primary", strata=None):
    res = []
    for path in glob.glob(os.path.join(RAW, f"*__*__{variant}.pkl")):
        stratum = os.path.basename(path).split("__")[0]
        if strata and stratum not in strata:
            continue
        with open(path, "rb") as fh:
            rs = pickle.load(fh)
        for r in rs:
            r["stratum"] = stratum if variant in ("primary", "nullB") else r["stratum"].split(":")[0]
        res += rs
    return res


def names_for(stratum):
    return P.indicator_names(stratum in ("CM", "SM"))


def base_for(stratum):
    return [n for n in names_for(stratum) if n in P.BASE]


def controls():
    res = load("primary", {"C0", "CM", "S4"})
    resg = load("C0g", {"C0"})
    for r in resg:
        r["stratum"] = "C0g"
    out = {}
    ok = True
    for st, rs, info in (("C0", res, A.PRIMARY_INFO_1D), ("C0g", res + resg, A.PRIMARY_INFO_1D),
                         ("CM", res, A.PRIMARY_INFO_M)):
        pred = A.prediction(rs, st, names_for("CM" if st == "CM" else "C0"), info, base_for(st))
        padj = S.holm([pred["rows"][n]["p_delta"] for n in info])
        yes = [n for n, p in zip(info, padj)
               if pred["rows"][n]["delta"] >= C.DELTA_AUC_MIN and p < 0.05
               and pred["rows"][n]["delta_a"] > 0 and pred["rows"][n]["delta_b"] > 0]
        out[st] = dict(best_baseline=pred["best_baseline"], yes=yes, rows=pred["rows"])
        if yes:
            ok = False
    # C0g invariances (§6.4)
    names = names_for("C0")
    inv = {}
    for f in ("a_may", "a_hopf", "a_trans", "b_cubic"):
        r0 = A._rs(res, "C0", f)
        rg = A._rs(res + resg, "C0g", f)
        jpe, jr = names.index("I3_pe"), names.index("B2_rank_ac1")
        inv[f] = dict(
            pe_tau_identical=bool(all(np.array_equal(a["tr"]["tau_off"][jpe], b["tr"]["tau_off"][jpe]) and
                                      np.array_equal(a["nu"]["tau_off"][jpe], b["nu"]["tau_off"][jpe])
                                      for a, b in zip(r0, rg))),
            rank_ac1_tau_identical=bool(all(abs(a["tr"]["tau_off"][jr] - b["tr"]["tau_off"][jr]) < 1e-12 and
                                            abs(a["nu"]["tau_off"][jr] - b["nu"]["tau_off"][jr]) < 1e-12
                                            for a, b in zip(r0, rg))))
    c0 = out["C0"]["rows"]
    c0g = out["C0g"]["rows"]
    inv["mi_auc_within_0.02"] = bool(abs(c0g["I1_mi"]["auc"] - c0["I1_mi"]["auc"]) <= 0.02)
    inv["pearson_ac1_auc_not_above_C0"] = bool(c0g["B1_ac1"]["auc"] <= c0["B1_ac1"]["auc"])
    inv_ok = all(v if isinstance(v, bool) else all(v.values()) for v in inv.values())
    ok = ok and inv_ok
    # S4 leakage (§6.4): no prediction AUC > 0.6 with CI excluding 0.5
    p4 = A.prediction(res, "S4", names, A.PRIMARY_INFO_1D, base_for("S4"))
    leak = {n: r for n, r in p4["rows"].items() if r["auc"] > 0.6 and r["auc_ci"][0] > 0.5}
    ok = ok and not leak
    summary = dict(controls_pass=bool(ok), C0g_invariance=inv, S4_leaks=list(leak),
                   C0_yes=out["C0"]["yes"], C0g_yes=out["C0g"]["yes"], CM_yes=out["CM"]["yes"],
                   detail=out, S4=p4["rows"])
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "controls.json"), "w") as fh:
        json.dump(summary, fh, indent=2, default=float)
    print("controls pass:", ok)
    return ok


def tests(audited=None):
    path = os.path.join(OUT, "controls.json")
    if not os.path.exists(path):
        sys.exit("Run --stage controls first.")
    with open(path) as fh:
        ctl = json.load(fh)
    if not ctl["controls_pass"] and not audited:
        sys.exit("A control failed (§6.4): audit, fix as a §11 deviation, re-run on fresh seeds.")
    res = load("primary")
    preds, chance_p, primary = {}, [], []
    for st in ("C0", "CM", "S1", "S2", "S3", "S4", "S5", "SM"):
        info = A.PRIMARY_INFO_M if st in ("CM", "SM") else A.PRIMARY_INFO_1D
        preds[st] = A.prediction(res, st, names_for(st), info, base_for(st))
        for n, r in preds[st]["rows"].items():
            if not n.startswith("x_"):
                chance_p.append((st, n, r["p_chance"]))
        if st not in ("C0", "CM"):
            primary += [(st, n, preds[st]["rows"][n]["p_delta"]) for n in info]
    ch_adj = S.holm([p for _s, _n, p in chance_p])
    for (st, n, _p), pa in zip(chance_p, ch_adj):
        preds[st]["rows"][n]["p_chance_holm"] = float(pa)
    assert len(primary) == 31, len(primary)
    pr_adj = S.holm([p for _s, _n, p in primary])
    table = {}
    for st in ("S1", "S2", "S3", "S4", "S5", "SM"):
        names = names_for(st)
        holm_p = {n: float(pa) for (s, n, _p), pa in zip(primary, pr_adj) if s == st}
        for n, pa in holm_p.items():
            preds[st]["rows"][n]["p_delta_holm"] = pa
        labels = A.decide(preds[st], holm_p)
        lt = A.lead_time(res, st, names, preds[st]["directions"])
        best = preds[st]["best_baseline"]
        for n in holm_p:
            if labels[n] == "YES":
                worse = []
                for f in lt:
                    ci = A.lead_median_diff_ci(lt, f, n, best)
                    if ci is not None and ci[1] < 0:
                        worse.append(f)
                if worse:
                    labels[n] = "YES, mixed (ROC only)"
        det = A.detection(res, st, names)
        table[st] = dict(label=A.stratum_label(preds[st], labels), labels=labels,
                         best_baseline=best, prediction=preds[st]["rows"],
                         lead_time={f: {n: {k: v for k, v in d.items() if k != "lead"}
                                        for n, d in fam.items()} for f, fam in lt.items()},
                         detection=det)
    labels = [table[s]["label"] for s in table]
    if not ctl["controls_pass"]:
        answer = "NOT ANSWERED (control failed)"
    elif sum(l_ == "INCONCLUSIVE" for l_ in labels) > sum(l_ != "INCONCLUSIVE" for l_ in labels):
        answer = "NOT ANSWERED (inconclusive strata outnumber decided ones)"
    elif any(l_ == "YES" for l_ in labels) and any(l_ in ("NO", "UNDETECTABLE") for l_ in labels):
        answer = "REGIME-DEPENDENT"
    elif any(l_ == "YES" for l_ in labels):
        answer = "YES (regime-specific)"
    else:
        answer = "NO" if all(l_ in ("NO", "UNDETECTABLE") for l_ in labels) else "NOT ANSWERED"
    # sensitivity analyses (§5.7): reported, not decisive, uncorrected
    sens = {}
    for v in ("window0.5", "detrend_gaussian", "detrend_none", "buffer50", "obsnoise"):
        rv = load(v)
        if not rv:
            continue
        sens[v] = {}
        for st in sorted({r["stratum"] for r in rv}):
            info = A.PRIMARY_INFO_M if st in ("CM", "SM") else A.PRIMARY_INFO_1D
            sens[v][st] = {n: dict(auc=r["auc"], delta=r.get("delta"), delta_ci=r.get("delta_ci"))
                           for n, r in A.prediction(rv, st, names_for(st), info, base_for(st))["rows"].items()}
    sens["learned_directions"] = {
        st: {n: r["auc"] for n, r in A.prediction(res, st, names_for(st),
                                                  A.PRIMARY_INFO_M if st in ("CM", "SM") else A.PRIMARY_INFO_1D,
                                                  base_for(st), learn_all=True)["rows"].items()}
        for st in ("S1", "S2", "S3", "S4", "S5", "SM")}
    nb = load("nullB")
    if nb:
        prim = {(r["stratum"], r["family"], r["pair"]): r for r in res}
        merged = []
        for r in nb:
            p = prim.get((r["stratum"], r["family"], r["pair"]))
            if p is not None and r["nu"] is not None:
                merged.append(dict(p, nu=r["nu"]))
        sens["nullB_unusable"] = sum(r["nu"] is None for r in nb)
        sens["nullB"] = {}
        for st in sorted({r["stratum"] for r in merged}):
            info = A.PRIMARY_INFO_M if st in ("CM", "SM") else A.PRIMARY_INFO_1D
            try:
                sens["nullB"][st] = {n: r["auc"] for n, r in A.prediction(
                    merged, st, names_for(st), info, base_for(st))["rows"].items()}
            except (ValueError, KeyError):
                pass
    result = dict(answer=answer, strata=table, sensitivity=sens, controls=ctl)
    with open(os.path.join(OUT, "results.json"), "w") as fh:
        json.dump(result, fh, indent=2, default=float)
    print("QR-006b answer:", answer, {s: table[s]["label"] for s in table})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=("controls", "tests"), required=True)
    ap.add_argument("--controls-audited", default=None,
                    help="§11 deviation number that fixed a failed control (re-run on fresh seeds)")
    a = ap.parse_args()
    if a.stage == "controls":
        controls()
    else:
        tests(a.controls_audited)


if __name__ == "__main__":
    main()
