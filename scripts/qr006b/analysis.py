"""Confirmatory analysis (pre-registration §5-§6; Amendments A18, A19).

All functions take `results`: a list of per-pair dicts as produced by
run_pilot._ind_task / run_confirmatory (keys stratum, family, pair, split,
level, tip, L, tr, nu).
"""

import zlib

import numpy as np

from . import config as C
from . import pipeline as P
from . import score as S
from . import strata as ST

PRIMARY_INFO_1D = ["I1_mi", "I3_pe", "I4_sampen", "I5_fi", "I6_rpde"]
PRIMARY_INFO_M = PRIMARY_INFO_1D + ["I2_te"]
TEST_STRATA_1D = ("S1", "S2", "S3", "S4", "S5")


def _rs(results, stratum, family):
    return sorted([r for r in results if r["stratum"] == stratum and r["family"] == family],
                  key=lambda r: r["pair"])


def _split(rs, which):
    return [r for r in rs if r["split"] == which]


def _seed(*parts):
    return zlib.crc32("|".join(map(str, parts)).encode())


def stratum_directions(results, stratum, names, learn_all=False):
    """A19: learned directions are set once per stratum, on the calibration
    split pooled over its model families."""
    fams = sum(ST.family_groups(stratum).values(), [])
    cal = sum([_split(_rs(results, stratum, f), "calibration") for f in fams], [])
    Tc = np.array([r["tr"]["tau_off"] for r in cal])
    Nc = np.array([r["nu"]["tau_off"] for r in cal])
    return S.directions(names, P.DIRECTION, Tc, Nc, learn_all)


def prediction(results, stratum, names, info, base, learn_all=False, n_boot=C.N_BOOT):
    """§5.1, §5.5, §5.6 for one stratum. Returns per-indicator AUCs (families
    a, b, pooled), CIs, chance p-values, best baseline and delta-AUCs."""
    groups = ST.family_groups(stratum)
    dirs = stratum_directions(results, stratum, names, learn_all)
    sgn = np.array([dirs[n] for n in names], float)
    per_model = {}
    for g, fams in groups.items():
        for f in fams:
            rs = _rs(results, stratum, f)
            cal, con = _split(rs, "calibration"), _split(rs, "confirmation")
            Tq = np.array([r["tr"]["tau_off"] for r in con]) * sgn
            Nq = np.array([r["nu"]["tau_off"] for r in con]) * sgn
            Tc = np.array([r["tr"]["tau_off"] for r in cal]) * sgn
            Nc = np.array([r["nu"]["tau_off"] for r in cal]) * sgn
            per_model[f] = dict(
                auc=S._auc_matrix(Tq, Nq), auc_cal=S._auc_matrix(Tc, Nc),
                boot=S.bootstrap_auc(Tq, Nq, n_boot, seed=_seed(stratum, f)),
                n=(len(Tq), len(Nq)))
    fam_auc = {g: np.mean([per_model[f]["auc"] for f in fams], axis=0) for g, fams in groups.items()}
    fam_boot = {g: np.mean([per_model[f]["boot"] for f in fams], axis=0) for g, fams in groups.items()}
    pooled = 0.5 * (fam_auc["a"] + fam_auc["b"])
    pboot = 0.5 * (fam_boot["a"] + fam_boot["b"])
    cal_pooled = 0.5 * (np.mean([per_model[f]["auc_cal"] for f in groups["a"]], axis=0)
                        + np.mean([per_model[f]["auc_cal"] for f in groups["b"]], axis=0))
    bi = [names.index(b) for b in base]
    best = base[int(np.nanargmax(cal_pooled[bi]))]
    jb = names.index(best)
    rows = {}
    for j, n in enumerate(names):
        learned = P.DIRECTION.get(n, 0) == 0 or learn_all
        lo_ = np.mean(pboot[:, j] <= 0.5)
        hi_ = np.mean(pboot[:, j] >= 0.5)
        rows[n] = dict(
            direction=dirs[n], learned=bool(learned),
            auc_a=float(fam_auc["a"][j]), auc_b=float(fam_auc["b"][j]), auc=float(pooled[j]),
            auc_ci=[float(np.nanpercentile(pboot[:, j], 2.5)), float(np.nanpercentile(pboot[:, j], 97.5))],
            p_chance=float(min(1.0, 2 * min(lo_, hi_)) if learned else lo_))
    for n in info:
        j = names.index(n)
        dboot = pboot[:, j] - pboot[:, jb]
        rows[n].update(
            delta=float(pooled[j] - pooled[jb]),
            delta_ci=[float(np.nanpercentile(dboot, 2.5)), float(np.nanpercentile(dboot, 97.5))],
            p_delta=float(np.mean(dboot <= 0)),
            delta_a=float(fam_auc["a"][j] - fam_auc["a"][jb]),
            delta_b=float(fam_auc["b"][j] - fam_auc["b"][jb]),
            vs_each={b: dict(delta=float(pooled[j] - pooled[names.index(b)]),
                             ci=[float(np.nanpercentile(pboot[:, j] - pboot[:, names.index(b)], 2.5)),
                                 float(np.nanpercentile(pboot[:, j] - pboot[:, names.index(b)], 97.5))])
                     for b in base})
    return dict(stratum=stratum, best_baseline=best, rows=rows, directions=dirs,
                n={f: v["n"] for f, v in per_model.items()},
                se_pooled={n: float(np.nanstd(pboot[:, j])) for j, n in enumerate(names)})


def lead_time(results, stratum, names, dirs, far=C.FAR, n_boot=2000):
    """§5.2-5.3 per model family; thresholds from calibration nulls."""
    out = {}
    for g, fams in ST.family_groups(stratum).items():
        for f in fams:
            rs = _rs(results, stratum, f)
            cal, con = _split(rs, "calibration"), _split(rs, "confirmation")
            if not con:
                continue
            n_on = con[0]["tr"]["tau_on"].shape[1]
            trec = ST.tau_rec0_samples(f)
            fam = {}
            for j, n in enumerate(names[:n_on]):
                s = dirs[n]
                th = S.far_threshold([s * r["nu"]["tau_on"][:, j] for r in cal], far)
                lt = S.lead_times([s * r["tr"]["tau_on"][:, j] for r in con],
                                  [r["tr"]["ends"] for r in con], [r["tip"] for r in con], th)
                null_far = np.mean([S.alarm_index(s * r["nu"]["tau_on"][:, j], th) is not None
                                    for r in con])
                lt0 = np.nan_to_num(lt, nan=0.0)
                fam[n] = dict(theta=th, detect_prob=float(np.mean(np.isfinite(lt))),
                              median_lead=float(np.nanmedian(lt)) if np.isfinite(lt).any() else None,
                              lead_quartiles_misses_zero=[float(q) for q in np.percentile(lt0, [25, 50, 75])],
                              null_alarm_rate_confirmation=float(null_far),
                              actionable={str(m): float(np.mean(lt0 - m * trec > 0))
                                          for m in C.T_RESP_MULTIPLES},
                              lead=lt)
            out[f] = fam
    return out


def lead_median_diff_ci(lead_tbl, fam, a, b, n_boot=2000):
    """Bootstrap CI of median lead (detected series) of a minus b, paired over
    transition series."""
    la, lb = lead_tbl[fam][a]["lead"], lead_tbl[fam][b]["lead"]
    rng = np.random.default_rng(_seed(fam, a, b))
    d = []
    for _ in range(n_boot):
        i = rng.integers(0, len(la), len(la))
        xa, xb = la[i], lb[i]
        if np.isfinite(xa).any() and np.isfinite(xb).any():
            d.append(np.nanmedian(xa) - np.nanmedian(xb))
    if not d:
        return None
    return [float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))]


def detection(results, stratum, names):
    """§5.4: level AUC of 50-point windows ending at t_tip - j; direction learned
    on calibration (sign of median level difference). Abrupt families only."""
    out = {}
    for g, fams in ST.family_groups(stratum).items():
        for f in fams:
            if f not in ST.ABRUPT:
                continue
            rs = _rs(results, stratum, f)
            cal, con = _split(rs, "calibration"), _split(rs, "confirmation")
            k = con[0]["tr"]["det"].shape[1]
            res = {}
            for jj, off in enumerate(C.DETECT_OFFSETS):
                Tc = np.array([r["tr"]["det"][jj] for r in cal])
                Nc = np.array([r["nu"]["det"][0] for r in cal])
                Tq = np.array([r["tr"]["det"][jj] for r in con])
                Nq = np.array([r["nu"]["det"][0] for r in con])
                row = {}
                for j, n in enumerate(names[:k]):
                    s = S.learned_direction(Tc[:, j], Nc[:, j])
                    row[n] = float(S.auc(s * Tq[:, j], s * Nq[:, j]))
                res[str(off)] = row
            out[f] = res
    return out


def decide(pred, holm_p, lead_tbl=None):
    """§6.1 labels for the information indicators of one test stratum.
    holm_p: dict indicator -> Holm-adjusted p for its delta test."""
    labels = {}
    for n, p_adj in holm_p.items():
        r = pred["rows"][n]
        yes = (r["delta"] >= C.DELTA_AUC_MIN and p_adj < 0.05 and r["delta_a"] > 0
               and r["delta_b"] > 0 and r.get("p_chance_holm", 1.0) < 0.05)
        if yes:
            labels[n] = "YES"
        elif r["delta_ci"][1] < C.DELTA_AUC_MIN:
            labels[n] = "NO (clean negative)"
        else:
            labels[n] = "INCONCLUSIVE"
    return labels


def stratum_label(pred, labels):
    """§6.2."""
    if any(v.startswith("YES") for v in labels.values()):
        return "YES"
    if all(v.startswith("NO") for v in labels.values()):
        return "NO"
    if all(r["auc_ci"][0] <= 0.5 <= r["auc_ci"][1] for r in pred["rows"].values()):
        return "UNDETECTABLE"
    return "INCONCLUSIVE"


def n_needed(se_observed, n_now, target_se):
    """Rough n per class for a target SE, from SE ~ 1/sqrt(n)."""
    if not se_observed or se_observed <= 0:
        return None
    return int(np.ceil(n_now * (se_observed / target_se) ** 2))
