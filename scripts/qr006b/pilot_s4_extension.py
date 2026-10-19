"""Amendment A15: S4 leakage check extended to 200 + 200 per family (pilot seeds).

Usage (from scripts/): ../.venv-qr006b/bin/python -m qr006b.pilot_s4_extension [--n 200]
"""

import argparse
import json
import os
import pickle
from multiprocessing import Pool

from . import pipeline as P
from . import run_pilot as R
from . import strata as ST
from . import config as C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--workers", type=int, default=9)
    a = ap.parse_args()
    with open(os.path.join(R.RAW, "pilot_results.pkl"), "rb") as fh:
        ps = pickle.load(fh)["ps"]
    with Pool(a.workers) as pool:
        sims = pool.map(R._sim_task, [("S4", f, a.n, C.SEED_PILOT, ps) for f in ST.FAMILIES["S4"]])
        tasks = [(s, f, p, None) for s, f, pairs, _c in sims for p in pairs]
        results = pool.map(R._ind_task, tasks, chunksize=1)
    leak = R.s4_leakage(results, P.indicator_names(False))
    counts = {f"{s}/{f}": c for s, f, _p, c in sims}
    with open(os.path.join(R.RAW, "pilot_s4_extension.pkl"), "wb") as fh:
        pickle.dump(dict(results=results, counts=counts), fh)
    with open(os.path.join(R.OUT, "pilot_s4_extension.json"), "w") as fh:
        json.dump(dict(n_per_class=a.n, counts=counts, leakage=leak), fh, indent=2, default=float)
    print("S4 (n=%d) all within 0.5±0.1:" % a.n, leak["all_within"], leak["outside"])


if __name__ == "__main__":
    main()
