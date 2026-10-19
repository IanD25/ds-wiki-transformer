"""Post-hoc audit of the lead-time results (2026-10-19). Exploratory; not part
of the pre-registered decision rules.

Question: are the information indicators' higher online detection rates
(e.g. Fisher index in SM, S3) produced by the causal (past-only) detrending,
which lags a drifting mean and leaves a within-window trend in ramped
transition series but not in the fixed-parameter nulls?

Three checks:
  1. swap: rerun the online alarm rule on the OFFLINE (Lowess) window values
     that the pipeline already stored (same windows, same thresholds rule);
  2. drift: within-window OLS slope of the causal residuals vs the Lowess
     residuals, transitions vs nulls (raw series re-read; no indicators);
  3. fix: Fisher index online, with each causal-residual window linearly
     detrended before binning, on a subset.

Usage (from scripts/):
  QR006B_RAW_DIR=~/qr006b_runs ../.venv-qr006b/bin/python -m qr006b.audit_leadtime
"""

import json
import math
import os
import pickle
from multiprocessing import Pool

import numpy as np

from . import analysis as A
from . import config as C
from . import pipeline as P
from . import score as S
from . import strata as ST
from .indicators import info as I
from .preprocess import causal_residuals, lowess_residuals, window_ends

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAWROOT = os.environ.get("QR006B_RAW_DIR") or os.path.join(
    REPO, "data", "experiments", "qr006b", "confirmatory")
OUT = os.path.join(REPO, "data", "reports", "qr006b")
STRATA = ("C0", "CM", "S1", "S2", "S3", "SM")
INFO = ("I1_mi", "I2_te", "I3_pe", "I4_sampen", "I5_fi", "I6_rpde")


def load(stratum):
    res = []
    for f in ST.FAMILIES[stratum]:
        with open(os.path.join(RAWROOT, "indicators", f"{stratum}__{f}__primary.pkl"), "rb") as fh:
            rs = pickle.load(fh)
        for r in rs:
            r["stratum"] = stratum
        res += rs
    return res


def detect(rs_cal, rs_con, j, sgn, source):
    """Detection probability at 5% FAR and confirmation-null alarm rate."""
    def traj(r, side):
        if source == "online":
            return sgn * r[side]["tau_on"][:, j]
        v = r[side]["vals_off"][:, j].astype(float)
        kmin = int(math.ceil(r[side]["w"] / C.STRIDE))
        return sgn * P.expanding_tau(v, kmin)
    th = S.far_threshold([traj(r, "nu") for r in rs_cal])
    lt = S.lead_times([traj(r, "tr") for r in rs_con], [r["tr"]["ends"] for r in rs_con],
                      [r["tip"] for r in rs_con], th)
    fa = np.mean([S.alarm_index(traj(r, "nu"), th) is not None for r in rs_con])
    return float(np.mean(np.isfinite(lt))), float(fa)


def check_swap():
    out = {}
    for st in STRATA:
        res = load(st)
        names = P.indicator_names(st in ("CM", "SM"))
        dirs = A.stratum_directions(res, st, names)
        n_on = res[0]["tr"]["tau_on"].shape[1]
        for f in ST.FAMILIES[st]:
            rs = A._rs(res, st, f)
            cal, con = A._split(rs, "calibration"), A._split(rs, "confirmation")
            row = {}
            for j, n in enumerate(names[:n_on]):
                d_on, fa_on = detect(cal, con, j, dirs[n], "online")
                d_off, fa_off = detect(cal, con, j, dirs[n], "offline")
                row[n] = dict(online=d_on, offline_values=d_off, far_online=fa_on, far_offline=fa_off)
            out[f"{st}/{f}"] = row
    return out


def _slopes(args):
    """Mean |within-window OLS slope| per window position, causal vs Lowess
    residuals, for one series (all variables averaged)."""
    x, L = args
    X = x[:, None] if x.ndim == 1 else x
    w, ends = window_ends(L)
    t = np.arange(w) - (w - 1) / 2
    den = (t * t).sum()
    res = {}
    for name, R in (("causal", np.column_stack([causal_residuals(X[:L, v], L) for v in range(X.shape[1])])),
                    ("lowess", np.column_stack([lowess_residuals(X[:L, v]) for v in range(X.shape[1])]))):
        sl = []
        for e in ends:
            W = R[e - w + 1: e + 1]
            sd = W.std(axis=0, ddof=1)
            b = (t[:, None] * (W - W.mean(axis=0))).sum(axis=0) / den
            # slope x window length, in units of the window SD: drift across the window
            sl.append(float(np.mean(np.abs(b) * w / np.where(sd > 0, sd, np.nan))))
        res[name] = sl
    return res


def check_drift(n_series=60, workers=9):
    out = {}
    for st in STRATA:
        for f in ST.FAMILIES[st]:
            with open(os.path.join(RAWROOT, "series", f"{st}__{f}.pkl"), "rb") as fh:
                pairs = pickle.load(fh)["pairs"][:n_series]
            jobs = [(p["x_tr"], p["L"]) for p in pairs] + [(p["x_null"], p["L"]) for p in pairs]
            with Pool(workers) as pool:
                r = pool.map(_slopes, jobs)
            k = len(pairs)
            summ = {}
            for cls, rr in (("transition", r[:k]), ("null", r[k:])):
                for det in ("causal", "lowess"):
                    first = np.nanmean([s[det][0] for s in rr])
                    last = np.nanmean([s[det][-1] for s in rr])
                    summ[f"{cls}_{det}"] = dict(first_window=float(first), last_window=float(last))
            out[f"{st}/{f}"] = summ
    return out


def _fi_online(args):
    """Expanding tau of the online Fisher index with and without a linear
    detrend of each causal-residual window."""
    x, L, multi = args
    X = x[:, None] if x.ndim == 1 else x
    w, ends = window_ends(L)
    nref = int(C.REFERENCE_FRACTION * L)
    R = np.column_stack([causal_residuals(X[:L, v], L) for v in range(X.shape[1])])
    sos = 2.0 * R[:nref].std(axis=0, ddof=1)
    tl = 80.0 if multi else 100.0
    t = np.arange(w) - (w - 1) / 2
    raw, lin = [], []
    for e in ends:
        W = np.ascontiguousarray(R[e - w + 1: e + 1])
        raw.append(I.fisher_index(W, sos, tl))
        b = (t[:, None] * (W - W.mean(axis=0))).sum(axis=0) / (t * t).sum()
        Wd = np.ascontiguousarray(W - t[:, None] * b)
        lin.append(I.fisher_index(Wd, sos, tl))
    kmin = int(math.ceil(w / C.STRIDE))
    return (P.expanding_tau(np.array(raw), kmin), P.expanding_tau(np.array(lin), kmin), ends)


def check_fix(cells=(("SM", "b_lever20_mul"), ("SM", "a_lever4_mul"), ("S3", "a_may_high"),
                     ("S3", "b_cubic_high")), workers=9):
    out = {}
    for st, f in cells:
        with open(os.path.join(RAWROOT, "series", f"{st}__{f}.pkl"), "rb") as fh:
            pairs = pickle.load(fh)["pairs"]
        multi = f in ST.MULTIVARIATE
        jobs = [(p["x_tr"], p["L"], multi) for p in pairs] + [(p["x_null"], p["L"], multi) for p in pairs]
        with Pool(workers) as pool:
            r = pool.map(_fi_online, jobs)
        k = len(pairs)
        tr, nu = r[:k], r[k:]
        cal = [i for i, p in enumerate(pairs) if p["split"] == "calibration"]
        con = [i for i, p in enumerate(pairs) if p["split"] == "confirmation"]
        res = {}
        for which, idx in (("as_run", 0), ("window_linear_detrend", 1)):
            for sgn, lab in ((-1, "falling(pre-registered)"), (1, "rising")):
                th = S.far_threshold([sgn * nu[i][idx] for i in cal])
                lt = S.lead_times([sgn * tr[i][idx] for i in con], [tr[i][2] for i in con],
                                  [pairs[i]["tip"] for i in con], th)
                res[f"{which}/{lab}"] = float(np.mean(np.isfinite(lt)))
        out[f"{st}/{f}"] = res
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    rep = {}
    rep["swap"] = check_swap()
    print("swap done", flush=True)
    rep["drift"] = check_drift()
    print("drift done", flush=True)
    rep["fix"] = check_fix()
    print("fix done", flush=True)
    with open(os.path.join(OUT, "leadtime_audit.json"), "w") as fh:
        json.dump(rep, fh, indent=1)


if __name__ == "__main__":
    main()
