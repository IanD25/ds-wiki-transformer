"""QR-006b confirmatory run, compute stage (pre-registration §2.5, §5.7, §8, §9).

Refuses to run unless config.FROZEN is True and the protocol and the code are
committed (no uncommitted changes under scripts/qr006b or in the
pre-registration). Resumable: each (stratum, family, variant) is checkpointed
under data/experiments/qr006b/confirmatory/.

Usage (from scripts/):
    ../.venv-qr006b/bin/python -m qr006b.run_confirmatory --workers 9 [--only C0,C0g,CM,S4]

The analysis is a separate step (report.py) that opens the controls first (§6.4).
"""

import argparse
import json
import os
import pickle
import platform
import subprocess
import sys
import time
from multiprocessing import Pool

import numpy as np

from . import config as C
from . import pipeline as P
from . import strata as ST

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW = os.path.join(REPO, "data", "experiments", "qr006b", "confirmatory")
PREREG = "docs/experiments/QR006B_BENCHMARK_PREREGISTRATION.md"

RAMPED = {"a_may", "a_hopf", "a_trans", "b_cubic", "a_lever4", "b_lever20", "a_may_mul",
          "b_cubic_mul", "a_layritz", "b_may_stable", "a_may_high", "b_cubic_high",
          "a_lever4_mul", "b_lever20_mul"}

# variant -> (strata it applies to, compute_series kwargs, sides)
VARIANTS = {
    "primary": (None, {}, "both"),
    "C0g": (("C0",), {"transform": "c0g"}, "both"),
    "window0.5": (None, {"window": C.WINDOW_SENS}, "both"),
    "detrend_gaussian": (None, {"detrend": "gaussian", "online": False}, "both"),
    "detrend_none": (None, {"detrend": "none", "online": False}, "both"),
    "buffer50": (None, {"buffer": C.BUFFER_SENS}, "both"),
    "obsnoise": (("C0", "S2"), {"obs_noise": True}, "both"),
    "nullB": (None, {}, "nullB"),
}


def _guard():
    if not C.FROZEN:
        sys.exit("config.FROZEN is False: freeze the protocol first (§9).")
    dirty = subprocess.check_output(
        ["git", "status", "--porcelain", "--", "scripts/qr006b", PREREG], cwd=REPO, text=True)
    if dirty.strip():
        sys.exit("Uncommitted changes in the protocol or the code:\n" + dirty)


def _version(m):
    from importlib.metadata import PackageNotFoundError, version
    try:
        return version(m)
    except PackageNotFoundError:
        return None


def _c0g(R, sref):
    return np.exp(R / sref)


def _sim(args):
    stratum, family, n, root = args
    path = os.path.join(RAW, "series", f"{stratum}__{family}.pkl")
    if os.path.exists(path):
        return stratum, family, path
    pairs, counts = ST.generate_pairs(stratum, family, n, root)
    for p in pairs:
        p["x_tr"] = p["x_tr"].astype(np.float64)
        p["x_null"] = p["x_null"].astype(np.float64)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path + ".tmp", "wb") as fh:
        pickle.dump(dict(pairs=pairs, counts=counts), fh)
    os.replace(path + ".tmp", path)
    return stratum, family, path


def _nullB_series(stratum, family, pair, root):
    ss = ST.seed_for(root, stratum, family, "nullB", pair["pair"])
    sim = ST.simulate(family, "nullB", np.random.default_rng(ss), pair["level"])
    return sim["x"]


def _ind(args):
    stratum, family, pair, variant, root = args
    _strata, kw, sides = VARIANTS[variant]
    kw = dict(kw)
    tf = _c0g if kw.pop("transform", None) == "c0g" else None
    buffer = kw.pop("buffer", C.BUFFER)
    obs = kw.pop("obs_noise", False)
    L = pair["tip"] - buffer + 1
    det_tr = [pair["tip"] - j for j in C.DETECT_OFFSETS]
    det_nu = [min(pair["null_det_end"], L - 1)]
    out = dict(stratum=stratum if variant == "primary" else f"{stratum}:{variant}",
               family=family, pair=pair["pair"], split=pair["split"], level=pair["level"],
               tip=pair["tip"], L=L)
    rng_obs = (lambda side: np.random.default_rng(
        ST.seed_for(root, stratum, family, "aux", 10_000_000 + 2 * pair["pair"] + side))) if obs else None
    t0 = time.time()
    if sides in ("both",):
        out["tr"] = P.compute_series(pair["x_tr"], L, det_tr, transform=tf,
                                     obs_noise_rng=rng_obs(0) if obs else None, **kw)
        out["nu"] = P.compute_series(pair["x_null"], L, det_nu, transform=tf,
                                     obs_noise_rng=rng_obs(1) if obs else None, **kw)
    else:   # nullB: new null series paired with the same transition
        xb = _nullB_series(stratum, family, pair, root)
        if len(xb) < L or not np.all(np.isfinite(xb[:L])):
            out["nu"] = None            # Null-B run escaped or diverged: counted, not used
        else:
            out["nu"] = P.compute_series(xb, L, det_nu, **kw)
    out["seconds"] = time.time() - t0
    return out


def main():
    _guard()
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=9)
    ap.add_argument("--only", default=None, help="comma-separated strata")
    ap.add_argument("--variants", default=",".join(VARIANTS))
    args = ap.parse_args()
    root = C.SEED_CONFIRMATORY
    strata = args.only.split(",") if args.only else ["C0", "CM", "S1", "S2", "S3", "S4", "S5", "SM"]
    strata = [s for s in strata if s != "C0g"]
    variants = args.variants.split(",")
    os.makedirs(RAW, exist_ok=True)
    manifest = dict(started=time.strftime("%Y-%m-%d %H:%M:%S"),
                    commit=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip(),
                    seed_root=root, n_per_class=C.N_PER_CLASS_CONFIRMATORY, pilot_values=C.PILOT_VALUES,
                    python=sys.version, machine=platform.platform(), variants=variants, strata=strata,
                    versions={m: _version(m) for m in ("numpy", "scipy", "pandas", "statsmodels",
                                                       "numba", "ewstools", "ordpy", "EntropyHub")})
    with open(os.path.join(RAW, f"manifest_{int(time.time())}.json"), "w") as fh:
        json.dump(manifest, fh, indent=2, default=str)
    # 1. simulate (checkpointed per family)
    tasks = [(s, f, C.N_PER_CLASS_CONFIRMATORY, root) for s in strata for f in ST.FAMILIES[s]]
    with Pool(args.workers) as pool:
        paths = pool.map(_sim, tasks, chunksize=1)
    # 2. indicators per (stratum, family, variant), checkpointed
    for stratum, family, path in paths:
        with open(path, "rb") as fh:
            pairs = pickle.load(fh)["pairs"]
        for variant in variants:
            vstrata, _kw, sides = VARIANTS[variant]
            if vstrata is not None and stratum not in vstrata:
                continue
            if variant == "nullB" and family not in RAMPED:
                continue
            out = os.path.join(RAW, "indicators", f"{stratum}__{family}__{variant}.pkl")
            if os.path.exists(out):
                continue
            t0 = time.time()
            with Pool(args.workers) as pool:
                res = pool.map(_ind, [(stratum, family, p, variant, root) for p in pairs], chunksize=1)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out + ".tmp", "wb") as fh:
                pickle.dump(res, fh)
            os.replace(out + ".tmp", out)
            print(f"{stratum}/{family}/{variant}: {len(res)} pairs, {time.time() - t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
