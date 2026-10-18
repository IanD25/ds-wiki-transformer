"""Strata, model families, validity rules, null pairing and splits
(pre-registration §2.1, §2.3-§2.5; Amendments A9-A12, A14)."""

import math

import numpy as np

from . import config as C
from . import models as M

# family -> list of noise "levels" split evenly within the family (§2.5)
FAMILIES = {
    "C0": ["a_may", "a_hopf", "a_trans", "b_cubic"],
    "CM": ["a_lever4", "b_lever20"],
    "S1": ["a_may_mul", "b_cubic_mul"],
    "S2": ["a_layritz", "b_may_stable"],
    "S3": ["a_may_high", "b_cubic_high"],
    "S4": ["a_may_fixed", "b_cubic_fixed"],
    "S5": ["a_rtip_sn", "b_rtip_dw"],
    "SM": ["a_lever4_mul", "b_lever20_mul"],
}
LEVELS = {"a_layritz": C.S2_ALPHAS, "b_may_stable": C.S2_ALPHAS}
MULTIVARIATE = {"a_lever4", "b_lever20", "a_lever4_mul", "b_lever20_mul"}

# Values the pilot sets (§7); filled in by run_pilot.py and frozen in config
PILOT_SET = {}


def seed_for(root, stratum, family, cls, run):
    fam = FAMILIES[stratum].index(family)
    return np.random.SeedSequence(entropy=root, spawn_key=(
        C.STRATUM_CODE[stratum], fam, C.CLASS_CODE[cls], run))


def ramp_samples(family):
    if family == "a_layritz":
        P = C.LAYRITZ
        n = int(round(P["k_hi"] / P["k_step"])) + 1
        return (n + P["sample_every"] - 1) // P["sample_every"]
    return int(round(C.T_MAX / C.SAMPLE_EVERY))


def simulate(family, cls, rng, level=None, ps=None):
    """One run of `family` in class 'transition' / 'null' / 'nullB'."""
    ps = PILOT_SET if ps is None else ps
    m_ = {"null": "null", "nullB": "nullB", "transition": "transition"}[cls]
    if family == "a_may":
        return M.simulate_may(rng, m_)
    if family == "a_hopf":
        return M.simulate_cr(rng, m_, "hopf")
    if family == "a_trans":
        return M.simulate_cr(rng, m_, "trans")
    if family == "b_cubic":
        return M.simulate_cubic(rng, m_)
    if family == "a_may_mul":
        x_star = M.may_roots(C.MAY["b_lo"]).max()
        return M.simulate_may(rng, m_, noise="mul", sigma=C.MAY["sigma"] / x_star)
    if family == "b_cubic_mul":
        x_star = M.cubic_roots(C.CUBIC["c_lo"]).min()
        return M.simulate_cubic(rng, m_, noise="mul",
                                sigma=C.CUBIC["sigma"] / math.sqrt(1 + x_star ** 2))
    if family == "a_layritz":
        return M.simulate_layritz(rng, m_, level)
    if family == "b_may_stable":
        return M.simulate_may(rng, m_, noise="stable", alpha=level)
    if family == "a_may_high":
        return M.simulate_may(rng, m_, sigma=ps["S3_sigma_a"], tip_rule="last")
    if family == "b_cubic_high":
        return M.simulate_cubic(rng, m_, sigma=ps["S3_sigma_b"], tip_rule="last")
    if family == "a_may_fixed":
        return _s4(M.simulate_may(rng, "null", sigma=ps["S4_sigma_a"],
                                  fixed_b=C.S4_PARAM["a"]))
    if family == "b_cubic_fixed":
        return _s4(M.simulate_cubic(rng, "null", sigma=ps["S4_sigma_b"],
                                    fixed_c=C.S4_PARAM["b"]))
    if family in ("a_rtip_sn", "b_rtip_dw"):
        model = 0 if family == "a_rtip_sn" else 1
        rc = ps["S5_rc_a" if model == 0 else "S5_rc_b"]
        lo, hi = (1.1, 2.0) if cls == "transition" else (0.5, 0.9)
        r = rc * rng.uniform(lo, hi)
        sig = ps["S5_sigma_a" if model == 0 else "S5_sigma_b"]
        out = M.simulate_rtip(rng, model, r, rc, sig)
        out["r"] = r
        return out
    if family in MULTIVARIATE:
        dim = 4 if "lever4" in family else 20
        noise = "mul" if family.endswith("_mul") else "add"
        return M.simulate_lever(rng, m_, dim, noise)
    raise ValueError(family)


def _s4(sim):
    """S4: the class is the outcome (§2.4): escaping runs are transitions."""
    sim["s4_escaped"] = sim["tip"] is not None
    return sim


def valid_transition(family, sim):
    """§2.3: must tip, not before 40% of the ramp (record, for S4/S5)."""
    tip = sim["tip"]
    if tip is None:
        return False, "no_tip"
    if tip < C.MIN_TIP_FRACTION * ramp_samples(family):
        return False, "early_tip"
    if not np.all(np.isfinite(sim["x"][: tip + 1])):
        return False, "nonfinite"
    return True, "ok"


def valid_null(family, sim):
    if family in ("a_rtip_sn", "b_rtip_dw", "a_layritz") and sim["tip"] is not None:
        return False, "null_tipped"
    if not np.all(np.isfinite(sim["x"])):
        return False, "nonfinite"
    return True, "ok"


def generate_pairs(stratum, family, n_pairs, root, max_runs_factor=20, ps=None):
    """Yield up to n_pairs matched (transition, null) pairs plus discard counts.

    Each pair k: (x_tr, tip, L, x_null, null_det_end, level, split).
    L = tip - B + 1 (segment indices 0..L-1). The null is truncated to L by the
    pipeline; its detection window ends at a random position in [49, L-1].
    """
    levels = LEVELS.get(family, [None])
    per_level = int(math.ceil(n_pairs / len(levels)))
    pairs = []
    counts = {"discarded": {}, "runs": {"transition": 0, "null": 0}}

    def bump(reason):
        counts["discarded"][reason] = counts["discarded"].get(reason, 0) + 1

    is_s4 = stratum == "S4"
    for li, level in enumerate(levels):
        trs, nus = [], []
        run = 0
        limit = per_level * max_runs_factor
        if is_s4:
            # one stream of runs at the fixed parameter; outcome sets the class
            while (len(trs) < per_level or len(nus) < per_level) and run < 4 * limit:
                ss = seed_for(root, stratum, family, "transition", run * len(levels) + li)
                rng = np.random.default_rng(ss)
                sim = simulate(family, "transition", rng, level, ps)
                counts["runs"]["transition"] += 1
                run += 1
                if sim["s4_escaped"]:
                    ok, why = valid_transition(family, sim)
                    if ok and len(trs) < per_level:
                        trs.append((sim, ss))
                    elif not ok:
                        bump("transition_" + why)
                elif len(nus) < per_level:
                    nus.append((sim, ss))
        else:
            while len(trs) < per_level and run < limit:
                ss = seed_for(root, stratum, family, "transition", run * len(levels) + li)
                sim = simulate(family, "transition", np.random.default_rng(ss), level, ps)
                counts["runs"]["transition"] += 1
                run += 1
                ok, why = valid_transition(family, sim)
                if ok:
                    trs.append((sim, ss))
                else:
                    bump("transition_" + why)
            run = 0
            while len(nus) < per_level and run < limit:
                ss = seed_for(root, stratum, family, "null", run * len(levels) + li)
                sim = simulate(family, "null", np.random.default_rng(ss), level, ps)
                counts["runs"]["null"] += 1
                run += 1
                ok, why = valid_null(family, sim)
                if ok:
                    nus.append((sim, ss))
                else:
                    bump(why)
        for k, ((st, sst), (sn, ssn)) in enumerate(zip(trs, nus)):
            tip = st["tip"]
            L = tip - C.BUFFER + 1
            n_null = len(sn["x"])
            if L > n_null:
                bump("null_too_short")
                continue
            drng = np.random.default_rng(ssn.spawn(1)[0])
            det_end = int(drng.integers(C.DETECT_WINDOW - 1, L))
            pairs.append(dict(x_tr=st["x"], tip=tip, tcrit=st.get("tcrit"), L=L,
                              x_null=sn["x"], null_det_end=det_end, level=level,
                              pair=len(pairs), meta_tr={k_: v for k_, v in st.items() if k_ in ("r",)},
                              meta_null={k_: v for k_, v in sn.items() if k_ in ("r",)}))
    for p in pairs:
        p["split"] = "calibration" if p["pair"] % C.CALIBRATION_EVERY == 0 else "confirmation"
    counts["pairs"] = len(pairs)
    return pairs, counts
