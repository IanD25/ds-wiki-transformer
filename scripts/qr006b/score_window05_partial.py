"""Score of the window-0.5 sensitivity (§5.7) for the decidable test strata S1-S3 and SM.

Uses report.py's own sensitivity call (A.prediction on the window0.5 variant), so the
numbers are what the full report will print. Writes
data/reports/qr006b/window05_interim.json only; results.json is untouched.
Sensitivity analyses are reported, not decisive, and uncorrected (§5.7).

Usage (from scripts/):
    QR006B_RAW_DIR=~/qr006b_runs ../.venv-qr006b/bin/python -m qr006b.score_window05_partial
"""

import json
import os

from . import analysis as A
from . import report as R

STRATA = ("S1", "S2", "S3", "SM")


def main():
    rv = R.load("window0.5", strata=set(STRATA))
    res = R.load("primary", strata=set(STRATA))
    out = {}
    for st in STRATA:
        names = R.names_for(st)
        info = A.PRIMARY_INFO_M if st in ("CM", "SM") else A.PRIMARY_INFO_1D
        w = A.prediction(rv, st, names, info, R.base_for(st))
        p = A.prediction(res, st, names, info, R.base_for(st))
        out[st] = dict(
            best_baseline_w05=w["best_baseline"], best_baseline_primary=p["best_baseline"],
            rows={n: dict(auc_w05=r["auc"], delta_w05=r.get("delta"), delta_ci_w05=r.get("delta_ci"),
                          auc_primary=p["rows"][n]["auc"], delta_primary=p["rows"][n].get("delta"))
                  for n, r in w["rows"].items()})
    path = os.path.join(R.OUT, "window05_interim.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    for st, d in out.items():
        bw = d["best_baseline_w05"]
        print(f"{st}: best baseline (w0.5) {bw} AUC {d['rows'][bw]['auc_w05']:.3f} "
              f"(primary best {d['best_baseline_primary']} {d['rows'][d['best_baseline_primary']]['auc_primary']:.3f})")
        for n in (A.PRIMARY_INFO_M if st in ("CM", "SM") else A.PRIMARY_INFO_1D):
            r = d["rows"][n]
            ci = r["delta_ci_w05"]
            print(f"   {n:10s} AUC w0.5 {r['auc_w05']:.3f} (primary {r['auc_primary']:.3f})  "
                  f"delta {r['delta_w05']:+.3f} [{ci[0]:+.3f}, {ci[1]:+.3f}]")
    print("written", path)


if __name__ == "__main__":
    main()
