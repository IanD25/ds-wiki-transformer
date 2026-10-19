r"""
DFIG reduction test — 2026-10-19 (audit_ref gsw-dfig-reduction-2026-10-19). Mode B.

Report: docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md (pre-registration commit f29dd61; results 68091ab)
Analysis: scripts/dfig_reduction_2026_10_19.py → data/reports/dfig_reduction_2026_10/

Verdicts (pre-registered rules): H-T REDUCES, H-CG REDUCES, H-ER REDUCES, H-RGG DOES NOT REDUCE,
H-P6 FALSIFIED (PR form; kagome lattice, d_H = 2, gives PR 1.61).

*** PROPOSAL — NOT YET OWNER-APPROVED. Do not run with --apply until the owner has ruled on:
    (1) P7: are σ ∝ side block-spin schedules valid coarse-grainings? (yes → Falsified, as coded;
        no → change P7 to Retired, forced by definition);
    (2) P5: correction row with label unchanged (as coded) or Speculative;
    (3) the new pattern tag `local-geometry-coincidence` (P6). ***
Also wait until the qr005-corrections session has committed its DB changes.

Writes:
- calibration (append-only): P6 Speculative → Falsified; P7 Speculative → Falsified;
  P5 correction row (Supported, unchanged); M6 correction row (Established, unchanged).
- ds_wiki.db conjectures: dated banner prepended to P5/P6/P7 `claim`; P6/P7 `three_state` relabelled
  ("<new> | was: <old>", as for P8/P11 on 2026-10-18).
- ds_wiki.db sections: dated banners prepended to M6 "Phase 1 Validation…", Ax2 "Grounding and Risk",
  T1 "Phase 1 Results…"; one sentence appended to gloss_effective_dimension "Why this disambig exists".

Dry run by default; --apply writes. Idempotent (banner/qualifier presence checks; calibration slot checks);
read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-dfig-reduction-2026-10-19"
D = "2026-10-19"
REPORT = "docs/experiments/DFIG_REDUCTION_TEST_2026_10_19.md"
TAG = f"({D}, `{AUDIT_REF}`; {REPORT})"

P6_LABEL = ("Falsified by the 2026-10-19 kagome counter-test: the participation ratio of the Phase 1 Fisher matrix "
            "is 1.61 on the kagome lattice (d_H = 2), levelling at 2/(1 + cos² 60°) = 1.6; it follows neighbour angles, "
            "not d_H. Gap-rank form already contradicted (mixed integers)")
P7_LABEL = ("Falsified by own Phase 1 data, shown exact 2026-10-19: under σ ∝ side block-spin schedules the gap rank "
            "rises d → d + 1; PR fails at every level; the fixed-σ rank 'pass' is the torus closed form at shrinking L "
            "and the DPI is not engaged")
P5_SHORT = ("Correction, label unchanged: Phase 1 torus 'rank = d' is the translation sector of the hypercubic point "
            "group (exact closed form); ER rank 1 is the uncentred mean term; RGGs give d + 1, unexplained")
M6_SHORT = ("Correction, label unchanged: Established covers the textbook Fisher matrix only; Phase 1 graph validation "
            "is symmetry-forced (tori, coarse-graining) or an estimator term (ER); RGG d + 1 unexplained; PR → d_H falsified")

CALIBRATIONS = [
    ("P6", "conjecture", "Falsified", D, AUDIT_REF, P6_LABEL,
     "Pre-registered reduction test (commit f29dd61) — " + REPORT + ". P6's gap-rank form was already contradicted by "
     "Phase 1 (mixed integers on fractals). Its participation-ratio form was tested against a lattice with the gasket's "
     "local geometry (degree 4, two corner-sharing triangles, neighbours on two lines at 60°) but d_H = 2: the kagome "
     "torus (M = 704, diameter 469 vs gasket L = 9, 512). At the decisive σ = 130: kagome PR = 1.612 (rule: falsified if "
     "outside [1.90, 2.10]); gasket 1.768 ± 0.250; square-torus control 2.020; triangular torus 2.011. Kagome levels at "
     "1.610 (σ = 220), the 2/(1 + cos²60°) = 1.6 of an isotropic distance field with 60° neighbour axes. The gasket's "
     "Phase 1 '≈ d_H within 4.7%' is the last σ tried on a curve still falling. Pattern tags: contradicted-by-own-tests; "
     "local-geometry-coincidence (new). Revertible by appending a later row."),
    ("P7", "conjecture", "Falsified", D, AUDIT_REF, P7_LABEL,
     "Pre-registered reduction test (commit f29dd61) — " + REPORT + ". Phase 1 coarse-graining uses the uncentred "
     "gap-position Fisher rank; block-spin of an L^d torus is the (L/2)^d torus (checked edge for edge), so each level "
     "is the three-level closed form λ_T(×d), λ_A(×1), λ_E(×(d−1)) at (1/σ, L, d). All 43 recorded entries (V1, V2 "
     "tables; three σ schedules) match: ranks exactly, PR within 4.5e-4. Fixed σ = 3: [2,2,2,2,2,1] is the closed form "
     "as L shrinks. Under σ = side/8 and side/16 (fixed physical scale) the rank rises 2 → 3 (2D) and 3 → 4 (3D): exact "
     "closed-form values, previously set aside as 'σ < 2, unreliable'. F is recomputed on each new graph, so the Fisher "
     "DPI (Zamir 1998) is not engaged; in its valid setting monotonicity is a theorem. PR fails at every level (Phase "
     "1). Owner ruled the σ ∝ side schedules valid coarse-grainings. Pattern tags: contradicted-by-own-tests; "
     "answer-forced-by-definition (the rank pass). Revertible by appending a later row."),
    ("P5", "conjecture", "Supported", D, AUDIT_REF, P5_SHORT,
     "Pre-registered reduction test (commit f29dd61) — " + REPORT + ". P5's M0 support rows rest on Phase 1 "
     "(D_eff-Test-1.0 @ 8f8094b): uncentred gap-position rank of a k×k neighbour-basis Fisher matrix. Tori: every rank "
     "and PR (2D 200², 3D 50³, 4D 12⁴ σ sweep) is the closed form, identity to 1.1e-12; 'rank = d' is the d-fold "
     "translation sector = Fisher rank of a d-dimensional location family, holding only for σ ≳ 1.7–2.3 (d + 1 below, "
     "then 1). ER 'rank 1': top singular vector aligned with the mean-score vector at 180/180 vertices (median |cos| "
     "0.999). RGG: rank d + 1 survives centring (centred mode 3 in 2D, 4 in 3D) — not the mean term, unexplained; so "
     "on RGGs the rank is not the dimension. Pre-registered rule: not REDUCES (needs the RGG leg); label unchanged. "
     "The 2026-04-20 row concerns the χ spectrum, a different object. Machta 2013 is a vocabulary anchor: the Phase 1 "
     "matrix has no model parameters. Pattern tags: answer-forced-by-definition; restatement-in-new-vocabulary."),
    ("M6", "entry", "Established", D, AUDIT_REF, M6_SHORT,
     "Pre-registered reduction test (commit f29dd61) — " + REPORT + ". M6's Established label (2026-05-04) is for the "
     "Fisher matrix as a parameter-space diagnostic, which is textbook. M6's own 'Phase 1 Validation' section reports "
     "the graph construction: tori and coarse-graining reduce exactly to lattice symmetry (closed form, all values); "
     "ER rank 1 is the uncentred mean term; the RGG d + 1 survives centring and is unexplained; PR → d_H is falsified "
     "by the kagome lattice (PR 1.61 at d_H = 2). Mapping verdict: PARTLY REDUCES. Pattern tag: "
     "answer-forced-by-definition."),
]

CLAIM_BANNERS = {
    "P6": (f"> **CLOSED {D} (`{AUDIT_REF}`).** Closed as **Falsified**. The participation ratio of the Phase 1 Fisher "
           "matrix is 1.61 on the kagome lattice, an ordinary 2D lattice (d_H = 2) with the gasket's local 60° "
           "neighbour geometry; it follows neighbour angles, not the Hausdorff dimension. The gap-rank form was "
           f"already contradicted (mixed integers). See `{REPORT}`.\n\n"),
    "P7": (f"> **CLOSED {D} (`{AUDIT_REF}`).** Closed as **Falsified** by the project's own Phase 1 data: with the "
           "physical scale held fixed (σ ∝ lattice side), block-spin coarse-graining raises the gap rank d → d + 1, "
           "an exact closed-form value, not noise. The fixed-σ 'pass' is the torus closed form at shrinking size; the "
           "data processing inequality is not engaged because F is recomputed on a new graph. "
           f"See `{REPORT}`.\n\n"),
    "P5": (f"> **UPDATE {D} (`{AUDIT_REF}`), label unchanged.** Phase 1's torus result ('rank = d') is the "
           "translation sector of the hypercubic lattice in a σ window, an exact closed form (the Fisher rank of a "
           "d-dimensional location family). The Erdős–Rényi 'rank 1' is the estimator's mean term. On random "
           f"geometric graphs the rank is d + 1, not d, and the +1 is unexplained. See `{REPORT}`.\n\n"),
}
NEW_THREE_STATE = {
    "P6": f"{P6_LABEL} [contradicted-by-own-tests; local-geometry-coincidence] ({AUDIT_REF})",
    "P7": f"{P7_LABEL} [contradicted-by-own-tests; answer-forced-by-definition] ({AUDIT_REF})",
}

SECTION_BANNERS = [
    ("M6", "Phase 1 Validation (Darling, 2026 — preprint)",
     f"> **Re-examined {D}** {TAG}: items 1 and 3 (tori, coarse-grained tori) are an exact closed-form function of "
     "σ, lattice size and d, fixed by the lattice's symmetry: the rank is d only in a σ window (d + 1 below it, then 1), "
     "and rises d → d + 1 under coarse-graining at fixed physical scale. Item 5's 'rank 1' is the uncentred estimator's "
     "mean term. Item 4's d + 1 survives centring and is unexplained. Item 2 (PR → d_H) is falsified: the kagome "
     "lattice (d_H = 2) gives PR 1.61.\n\n"),
    ("Ax2", "Grounding and Risk",
     f"> **Re-examined {D}** {TAG}: the Phase 1 evidence cited below is forced by lattice symmetry (exact integers on "
     "tori, rank monotonicity under block-spin), falsified (PR convergence to Hausdorff dimension: the kagome lattice, "
     "d_H = 2, gives 1.61), or gives d + 1 rather than d (random geometric graphs). As a definition, Ax2 is untestable; "
     "no Phase 1 result supports the identification of Fisher rank with physical dimension beyond the textbook fact "
     "that a d-dimensional location family has Fisher rank d.\n\n"),
    ("T1", "Phase 1 Results (Darling, 2026 — preprint)",
     f"> **Re-examined {D}** {TAG}: the 'pass' below is the torus closed form at shrinking lattice size (each "
     "block-spin level is a smaller torus, and F is recomputed on it, so the data processing inequality is not "
     "engaged). Holding the physical scale fixed (σ ∝ side), the same closed form gives rank increases d → d + 1. In "
     "its valid setting (one fixed family, data passed through a parameter-independent kernel) monotonicity is a "
     "theorem (Zamir 1998), so there is nothing left to test.\n\n"),
]
GLOSS = ("gloss_effective_dimension", "Why this disambig exists",
         "fixed by lattice symmetry and the kernel setting; see `docs/experiments/CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md`.)",
         f" (Added {D}, `{AUDIT_REF}`: M6's Phase 1 validation (Darling 2026 preprint) used this same gap-position "
         f"sense; see `{REPORT}`.)")


def plan_text(cur, banner, prepend=True):
    if banner.strip() in cur:
        return None
    return banner + cur if prepend else cur + banner


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    w = sqlite3.connect(DS_WIKI_DB)
    claim_w, ts_w, sec_w = {}, {}, []
    for cid, banner in CLAIM_BANNERS.items():
        r = w.execute("SELECT claim, three_state FROM conjectures WHERE id=?", (cid,)).fetchall()
        if len(r) != 1: raise SystemExit(f"[{cid}] FAIL — {len(r)} rows")
        new = plan_text(r[0][0], banner)
        if new: claim_w[cid] = new; print(f"  [{cid} claim] plan — banner (+{len(banner)} chars)")
        else: print(f"  [{cid} claim] OK — already applied")
        if cid in NEW_THREE_STATE:
            if r[0][1].startswith(NEW_THREE_STATE[cid]): print(f"  [{cid} three_state] OK — already applied")
            else:
                ts_w[cid] = NEW_THREE_STATE[cid] + " | was: " + r[0][1]
                print(f"  [{cid} three_state] plan — {NEW_THREE_STATE[cid][:60]}…")
    for eid, sname, banner in SECTION_BANNERS:
        r = w.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (eid, sname)).fetchall()
        if len(r) != 1: raise SystemExit(f"[{eid}/{sname}] FAIL — {len(r)} sections")
        new = plan_text(r[0][0], banner)
        if new: sec_w.append((eid, sname, new)); print(f"  [{eid} / {sname}] plan — banner (+{len(banner)} chars)")
        else: print(f"  [{eid} / {sname}] OK — already applied")
    eid, sname, anchor, add = GLOSS
    cur = w.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (eid, sname)).fetchone()[0]
    if anchor + add in cur: print(f"  [{eid}] OK — already applied")
    else:
        if cur.count(anchor) != 1: raise SystemExit(f"[{eid}] FAIL — anchor count {cur.count(anchor)}")
        sec_w.append((eid, sname, cur.replace(anchor, anchor + add, 1))); print(f"  [{eid}] plan — qualifier")
    w.close()

    hc = sqlite3.connect(WIKI_HISTORY_DB)
    cals = []
    for c in CALIBRATIONS:
        got = hc.execute("SELECT short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                         (c[0], c[3], c[4])).fetchone()
        if got is None:
            if not hc.execute("SELECT 1 FROM confidence_calibration WHERE entity_id=?", (c[0],)).fetchone():
                raise SystemExit(f"[cal {c[0]}] ABORT — no prior history")
            cals.append(c); print(f"  [cal {c[0]}] plan — {c[2]}: {c[5][:70]}")
        elif got[0] != c[5]:
            print(f"  [cal {c[0]}] COLLISION — slot held by a different row; NOT written")
        else:
            print(f"  [cal {c[0]}] OK — already present")
    hc.close()
    print(f"  {len(claim_w)} claim, {len(ts_w)} three_state, {len(sec_w)} section writes; {len(cals)} calibration rows")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return

    w = sqlite3.connect(DS_WIKI_DB)
    for cid, new in claim_w.items():
        if w.execute("UPDATE conjectures SET claim=? WHERE id=?", (new, cid)).rowcount != 1: w.rollback(); raise SystemExit(cid)
    for cid, new in ts_w.items():
        if w.execute("UPDATE conjectures SET three_state=? WHERE id=?", (new, cid)).rowcount != 1: w.rollback(); raise SystemExit(cid)
    for eid, sname, new in sec_w:
        if w.execute("UPDATE sections SET content=? WHERE entry_id=? AND section_name=?", (new, eid, sname)).rowcount != 1:
            w.rollback(); raise SystemExit(eid)
    w.commit()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for c in cals:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date, audit_ref,
                      short_status, rationale) VALUES (?,?,?,?,?,?,?)""", c)
    hc.commit()

    bad = []
    for cid, new in claim_w.items():
        if w.execute("SELECT claim FROM conjectures WHERE id=?", (cid,)).fetchone()[0] != new: bad.append(cid)
    for cid, new in ts_w.items():
        if w.execute("SELECT three_state FROM conjectures WHERE id=?", (cid,)).fetchone()[0] != new: bad.append(cid + "/ts")
    for eid, sname, new in sec_w:
        if w.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (eid, sname)).fetchone()[0] != new:
            bad.append(eid)
    for c in CALIBRATIONS:
        if hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                      (c[0], c[3], c[4])).fetchone() != (c[2], c[5]):
            bad.append("cal " + c[0])
    w.close(); hc.close()
    if bad: raise SystemExit(f"Post-write drift: {bad}")
    print("  verified")


if __name__ == "__main__":
    main()
