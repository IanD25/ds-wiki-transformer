r"""
Consistency pass, Phase 4 — triviality check + prior-art gate on H5's two-process
"derivation" — 2026-10-18 (audit_ref gsw-consistency-pass-2026-10-18). Mode A.

Report: docs/prior_art_reviews/H5_TWO_PROCESS_PRIOR_ART_2026_10_18.md

Verdict: RESTATEMENT of West, Savage, Gillooly, Enquist, Woodruff & Brown 2003
(Nature 421:713; preprint arXiv:physics/0211058), which gives b = Σ cᵢbᵢ with
cᵢ = Bᵢ/B as the corrected form of Darveau et al. 2002's Eq. 2 — itself the
elasticity-of-a-sum rule. Re-derivation under charter rule 2. H5 stays
Speculative.

Writes:
- H5 What The Math Says: dated banner inserted immediately before the
  "DERIVATION FOUND" block (single composed write; original text unchanged).
- external_anchors on H5 (it had none; its internal_construction flag stays):
  reframing_of West 2003; specialization_of elasticity sum rule;
  contradicts Darveau 2002; generalization_of Ballesteros 2018;
  adjacent_concept Zhao 2015; adjacent_concept Glazier 2010.
- calibration (append-only, labels unchanged): H5 (under the owner-approved collision
  sub-ref gsw-consistency-pass-2026-10-18-h5-gate — H5 already held this pass's slot from
  Phase 3); endpoint_decision_revised.

Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-consistency-pass-2026-10-18"
D = "2026-10-18"
REPORT = "docs/prior_art_reviews/H5_TWO_PROCESS_PRIOR_ART_2026_10_18.md"

ANCHOR_TEXT = r"**DERIVATION FOUND 2026-05-04 — the $\beta(\lambda)$ form is not arbitrary after all.**"
BANNER = (
    f"> **PRIOR-ART GATE — added {D} (`{AUDIT_REF}`; report: `{REPORT}`).** **Re-derivation, not a finding (charter rule 2).** "
    "The identity below — the log-slope of a sum of power laws is the share-weighted average of their exponents — is the "
    "elasticity-of-a-sum rule, and it is already in the metabolic-scaling literature in exactly this role. West, Savage, Gillooly, "
    "Enquist, Woodruff & Brown 2003 (*Nature* 421:713; preprint arXiv:physics/0211058) give b = Σ cᵢbᵢ with cᵢ = Bᵢ/B for "
    "contributions added in parallel, as \"the formula that DSAH should have used\" in place of Darveau et al. 2002's fixed-weight "
    "Eq. 2, and call the additive model \"only a consistency check of energy conservation, which must be trivially correct\". "
    "Verdict: **RESTATEMENT of West et al. 2003**; H5 stays **Speculative**. Three claims below overreach. (1) \"The endpoints are "
    "not a free choice\": p and q are inputs to the identity, which says nothing about their values. (2) \"Measurable by measuring "
    "the two contributions separately\": only where the two fluxes are genuinely separate and add in parallel, which has to be shown "
    "for any proposed pair. (3) \"There is one [mechanism]\": the identity gives λ a meaning but supplies no mechanism; the "
    "explanatory content lies entirely in which two processes, and why their exponents take the values they do. Also: Ballesteros "
    "et al. 2018's f is a mass-independent constant, not this λ (the λ-equivalent in their model is fkM/B); and Zhao 2015 is not a "
    "two-process decomposition but a single-network model, B = αM^x / log(M/β), that yields convex curvature with no second process — "
    "a rival account of the curvature, not a candidate pair. The '2026-05-04' in the heading is a session label for work done "
    "2026-07-25. *Original text follows, unchanged.*\n\n"
)

ANCHORS = [  # entry, source, identifier, title, tier, stability, relationship, confidence, notes
    ("H5", "doi", "10.1038/421713a",
     "West, Savage, Gillooly, Enquist, Woodruff, Brown 2003 - Why does metabolic rate scale with body size? (Nature 421:713; preprint arXiv:physics/0211058)",
     1, "canonical", "reframing_of", "high",
     "H5's two-process identity (local slope = share-weighted average of exponents, lambda = B_i/B) is the two-process case of West et al.'s "
     "correction to Darveau et al. 2002: b = sum c_i b_i with c_i = B_i/B for parallel contributions, 'the formula that DSAH should have used'. "
     "Verified against the preprint full text 2026-10-18. Pattern-tag: restatement-in-new-vocabulary. See " + REPORT + "."),
    ("H5", "wikipedia", "https://en.wikipedia.org/wiki/Elasticity_of_a_function",
     "Elasticity of a function — elasticity of a sum rule (cf. Sydsaeter & Hammond, Mathematics for Economic Analysis)",
     2, "active-literature", "specialization_of", "medium",
     "The log-log slope is the elasticity; El(f+g) = (f El f + g El g)/(f+g). H5's identity is this rule applied to metabolic scaling. "
     "Textbook page not seen directly; verified via the encyclopedia statement and course notes."),
    ("H5", "doi", "10.1038/417166a",
     "Darveau, Suarez, Andrews, Hochachka 2002 - Allometric cascade as a unifying principle of body mass effects on metabolism (Nature 417:166)",
     1, "canonical", "contradicts", "high",
     "Darveau's Eq. 2, MR = a sum c_i M^b_i with fixed control coefficients summing to 1, is the fixed-weight form that H5's share-weighted "
     "identity corrects; West et al. 2003 show it is not dimensionally homogeneous (b ~ 0.76 in kg, 0.78 in g, 1.08 in pg on the same data). "
     "Their objection that summed steps acting in series double-count applies to any process pair H5 proposes."),
    ("H5", "doi", "10.1038/s41598-018-19853-6",
     "Ballesteros et al. 2018 - On the thermodynamic origin of metabolic scaling (Sci. Rep. 8:1448)",
     1, "active-literature", "generalization_of", "high",
     "B = f k M + (1-f) k' M^(2/3): the special case p = 1, q = 2/3 of H5's form. CAUTION: their f is 'the fraction of the energy income that "
     "is used efficiently' and is independent of M; it is NOT H5's lambda, which in their model is f k M / B and varies with mass. "
     "Verified against the PMC full text 2026-10-18."),
    ("H5", "arxiv", "1509.08912",
     "Zhao 2015 - A common origin for 3/4- and 2/3-power rules in metabolic scaling",
     3, "preprint-evolving", "adjacent_concept", "medium",
     "Rival single-network account, NOT a two-process decomposition: B = alpha M^x / log(M/beta), x = 11/12 (fit 0.868), from one Murray-law "
     "network; convex curvature arises from the log normalisation with no second process; 'the 2/3-rule does not originate from the classical "
     "surface law'. The scaling queue's 'Ballesteros vs Zhao' framing as competing decompositions is therefore wrong. Verified against the "
     "full text 2026-10-18."),
    ("H5", "doi", "10.1111/j.1469-185X.2009.00095.x",
     "Glazier 2010 - A unifying explanation for diverse metabolic scaling in animals and plants (Biol. Rev.)",
     1, "active-literature", "adjacent_concept", "medium",
     "Metabolic-level boundaries hypothesis: exponent bounded between 2/3 and 1 by shifts in the relative importance of surface- and "
     "volume-related processes. Same qualitative picture as H5's two-process reading, stated without a share-weighted formula. Reading via "
     "the 2014 review; 2010 text not read directly in this pass."),
]

CALIBRATIONS = [
    # Owner-approved 2026-10-18: confidence_calibration is UNIQUE(entity_id, calibration_date,
    # audit_ref) and H5 already holds today's slot from Phase 3 (Xiao correction), so this row
    # uses the collision sub-ref AUDIT_REF + "-h5-gate".
    ("H5", "entry", "Speculative", D, AUDIT_REF + "-h5-gate",
     "Two-process form = re-derivation (charter rule 2): RESTATEMENT of West et al. 2003",
     "Correction recorded, label unchanged. Triviality check: for B = aM^p + bM^q the local log-log slope p f + q(1-f), f = aM^p/B, is the "
     "elasticity-of-a-sum rule — a re-derivation, not a finding. Prior-art gate (" + REPORT + "): RESTATEMENT of West, Savage, Gillooly, "
     "Enquist, Woodruff & Brown 2003 (Nature 421:713), who give b = sum c_i b_i with c_i = B_i/B as the corrected form of Darveau et al. 2002's "
     "Eq. 2. The identity gives lambda a meaning (a process's share of the total) but no mechanism; it does not fix the endpoints (p, q are "
     "inputs); lambda is measurable only where the fluxes are separable and parallel. Ballesteros 2018's f is a constant, not lambda; Zhao 2015 "
     "is a single-network rival, not a decomposition. Qualifies the 2026-07-25 row 'Form is DERIVABLE from a two-process sum'. Anchors added."),
    ("endpoint_decision_revised", "structural_observation", "Speculative", D, AUDIT_REF,
     "Correction: 'endpoints derivable, not chosen' overstates — p and q are inputs to the identity",
     "Correction recorded, label unchanged. The 2026-07-25 row said the endpoints 'are now derivable, not chosen'. The H5 prior-art gate "
     "(" + REPORT + ") shows the two-process identity takes the exponents p and q as inputs and says nothing about their values; it relocates "
     "the endpoint question to identifying the processes (and showing they add in parallel) but does not answer it. The [2/3, 3/4] decision "
     "remains superseded-in-form, not resolved."),
]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB)
    cur_v = conn.execute("SELECT content FROM sections WHERE entry_id='H5' AND section_name='What The Math Says'").fetchone()[0]
    conn.close()
    if BANNER + ANCHOR_TEXT in cur_v:
        new_v = None; print("  [H5.math_says] OK — already applied")
    else:
        if cur_v.count(ANCHOR_TEXT) != 1: raise SystemExit(f"[H5.math_says] FAIL — anchor count {cur_v.count(ANCHOR_TEXT)}")
        new_v = cur_v.replace(ANCHOR_TEXT, BANNER + ANCHOR_TEXT, 1); print(f"  [H5.math_says] plan — banner (+{len(BANNER)})")
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    anc = [x for x in ANCHORS if not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND relationship=?",
                                                 (x[0], x[1], x[2], x[6])).fetchone()]
    cals = []
    for c in CALIBRATIONS:
        got = hc.execute("SELECT short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                         (c[0], c[3], c[4])).fetchone()
        if got is None:
            cals.append(c)
        elif got[0] != c[5]:
            # UNIQUE(entity_id, calibration_date, audit_ref): another row from this pass already holds the slot.
            print(f"  [cal {c[0]}] COLLISION — slot held by a different row ({got[0][:60]!r}); NOT written")
        else:
            print(f"  [cal {c[0]}] OK — already present")
    for c in cals:
        if not hc.execute("SELECT 1 FROM confidence_calibration WHERE entity_id=?", (c[0],)).fetchone():
            raise SystemExit(f"[cal {c[0]}] ABORT — no prior history")
    hc.close()
    print(f"  {1 if new_v else 0} section write, {len(anc)} anchors, {len(cals)} calibration rows")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    if new_v:
        conn = sqlite3.connect(DS_WIKI_DB)
        c = conn.execute("UPDATE sections SET content=? WHERE entry_id='H5' AND section_name='What The Math Says'", (new_v,))
        if c.rowcount != 1: conn.rollback(); raise SystemExit("rowcount")
        conn.commit(); conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for (eid, src, ident, title, tier, stab, rel, conf, notes) in anc:
        hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier, source_stability_class,
                      relationship, canonical_role, verified_date, verified_by_session, confidence, notes)
                      VALUES (?,?,?,NULL,?,?,?,?,NULL,?,?,?,?)""", (eid, src, ident, title, tier, stab, rel, D, AUDIT_REF, conf, notes))
    for c in cals:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date, audit_ref,
                      short_status, rationale) VALUES (?,?,?,?,?,?,?)""", c)
    hc.commit()
    bad = []
    if new_v:
        conn = sqlite3.connect(DS_WIKI_DB)
        if conn.execute("SELECT content FROM sections WHERE entry_id='H5' AND section_name='What The Math Says'").fetchone()[0] != new_v: bad.append("H5")
        conn.close()
    for x in ANCHORS:
        if not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id=? AND identifier=? AND relationship=?", (x[0], x[2], x[6])).fetchone(): bad.append(x[2])
    for c in CALIBRATIONS:
        if c in cals and hc.execute("SELECT short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                                    (c[0], c[3], c[4])).fetchone() != (c[5],): bad.append(c[0])
    hc.close()
    if bad: raise SystemExit(f"Post-write drift: {bad}")
    print("  verified")


if __name__ == "__main__":
    main()
