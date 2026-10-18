"""§7 pass criterion 1, wrapper fidelity (Amendments A1, A17).

Runs Bury et al. 2021's UNMODIFIED test-model scripts (external/bury2021, a
git-ignored clone, CC BY-NC-SA 4.0) in a scratch directory, then recomputes
AC1 and variance Kendall tau on the same series with this pipeline's own
code, and reports the largest absolute difference.

Bury's scripts import seaborn and sklearn without using them; those two
modules are stubbed (they are not installed). Nothing in the scripts is edited.

Usage: python -m qr006b.fidelity_bury OUTDIR
"""

import json
import os
import runpy
import sys
import tempfile
import types

import numpy as np
import pandas as pd

from .indicators import baselines as B
from .preprocess import lowess_residuals

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BURY = os.path.join(REPO, "external", "bury2021", "test_models")
MODELS = {"may_fold_1500": ("sim_may_fold.py", "sim_may_fold_null.py"),
          "cr_hopf_1500": ("sim_cr_hopf.py", "sim_cr_hopf_null.py"),
          "cr_trans_1500": ("sim_cr_trans.py", "sim_cr_trans_null.py")}


def _stub(name):
    if name in sys.modules:
        return
    try:
        __import__(name)
    except ImportError:
        mod = types.ModuleType(name)
        sys.modules[name] = mod
        if name == "sklearn":
            sub = types.ModuleType("sklearn.metrics")
            sys.modules["sklearn.metrics"] = sub
            mod.metrics = sub


def _run(script, workdir):
    old = os.getcwd()
    os.chdir(workdir)
    try:
        runpy.run_path(script, run_name="__main__")
    finally:
        os.chdir(old)


def ours_ktau(state_pre, rw=0.25, span=0.2, t_res=10):
    """Our code in 'Bury mode': stride 1 rolling window, tau from the second
    defined value up to each t in index[::t_res] (Bury's compute_ktau)."""
    x = state_pre.values.astype(float)
    t = state_pre.index.values.astype(float)
    res = lowess_residuals(x, span)
    w = int(rw * len(x))
    var = np.full(len(x), np.nan)
    ac = np.full(len(x), np.nan)
    for e in range(w - 1, len(x)):
        win = np.ascontiguousarray(res[e - w + 1: e + 1])
        var[e] = B.moments(win)[0]
        ac[e] = B.ac1(win)
    from scipy.stats import kendalltau
    out = {}
    for name, v in (("variance", var), ("ac1", ac)):
        s = pd.Series(v, index=t)
        t0 = s[pd.notnull(s)].index[1]
        vals = {}
        for tf in s.index[::t_res]:
            r = s.loc[t0:tf]
            vals[tf] = kendalltau(r.index.values, r.values)[0]
        out[name] = pd.Series(vals)
    return out, pd.Series(res, index=t), pd.Series(var, index=t), pd.Series(ac, index=t)


def main(outdir):
    for m in ("seaborn", "sklearn"):
        _stub(m)
    import matplotlib
    matplotlib.use("Agg")
    report = {}
    for model, (sim, sim_null) in MODELS.items():
        work = tempfile.mkdtemp(prefix=f"bury_{model}_")
        src = os.path.join(BURY, model)
        for f in (sim, sim_null, "compute_ktau.py"):
            _run(os.path.join(src, f), work)
        ews = pd.read_csv(os.path.join(work, "data/ews/df_ews_forced.csv"))
        kt = pd.read_csv(os.path.join(work, "data/ews/df_ktau_forced.csv"))
        if "Variable" in ews.columns:
            ews = ews[ews["Variable"] == "x"]
        diffs = {"residuals": 0.0, "variance": 0.0, "ac1": 0.0,
                 "ktau_variance": 0.0, "ktau_ac": 0.0}
        for tsid, df in ews.groupby("tsid"):
            df = df.set_index("Time")
            pre = df[df["residuals"].notna()]
            ours, res, var, ac = ours_ktau(pre["state"])
            diffs["residuals"] = max(diffs["residuals"],
                                     float(np.nanmax(np.abs(res.values - pre["residuals"].values))))
            for col, s in (("variance", var), ("ac1", ac)):
                bv = pre[col].values
                ok = ~np.isnan(bv)
                diffs[col] = max(diffs[col], float(np.nanmax(np.abs(s.values[ok] - bv[ok]))))
            k = kt[kt["tsid"] == tsid].set_index("Time")
            for ours_name, bury_name in (("variance", "ktau_variance"), ("ac1", "ktau_ac")):
                b_ = k[bury_name].dropna()
                o_ = ours[ours_name].reindex(b_.index)
                diffs[bury_name] = max(diffs[bury_name], float(np.nanmax(np.abs(o_.values - b_.values))))
        report[model] = diffs
        print(model, diffs, flush=True)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "fidelity_bury.json"), "w") as fh:
        json.dump(report, fh, indent=2)
    worst = max(max(d.values()) for d in report.values())
    print("worst abs difference:", worst, "PASS" if worst <= 1e-6 else "FAIL")


if __name__ == "__main__":
    main(sys.argv[1])
