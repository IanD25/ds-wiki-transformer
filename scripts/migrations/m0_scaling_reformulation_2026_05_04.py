"""
Scaling framework reformulation — items 1-4 — 2026-05-04

Owner-approved 2026-05-04, following a working session that traced the
beta(lambda) framework's problems to a single root cause.

ROOT DIAGNOSIS
--------------
beta(lambda) = lambda*[d_f/(d_f+1)] + (1-lambda)*1 was constructed by
INTERPOLATING BETWEEN TWO CHOSEN ENDPOINTS, not derived from a mechanism.
WBE earned 3/4 from three physical premises. beta(lambda) takes that as one
anchor, picks beta=1 as the other because it resembles a no-network limit,
and draws a line. Nothing generates the line.

Every known symptom follows from that one fact:
  - endpoints don't contain the data (mammalian BMR 0.676 < 0.750 floor)
  - lambda is unmeasurable (it entered as an interpolation weight)
  - range fails for cities (a segment can't leave its endpoints)
  - inverted d_f values are unphysical (reptiles 3.2, fish 7.3)
  - lambda means two incompatible things (state in X1, structure in C1)

THE DAMAGING FINDING IS ALREADY IN THE WIKI
-------------------------------------------
C1's What's Established already records Kolokotrones et al. 2010: the
log-log metabolic relation is CURVED (~2/3 small mammals, ~3/4 large), with
Xiao et al. 2015 placing a breakpoint near 10 kg. If the relation is curved
there is NO single exponent, and much of the cross-taxon spread that
beta(lambda) exists to explain may be a sampling artifact of which mass
range a study covered. A framework that explains variance which does not
need explaining is worse than no framework.

EDITS (all distinct table/row/column triples)
---------------------------------------------
  R1  C1.What's Established   — elevate curvature from a recorded fact to a
                                framing statement with its implication drawn.
  R2  H5.What It Says         — reframe as descriptive interpolation with a
                                documented failure, not a law. Preserved per
                                the falsifications-as-learning-artifacts rule.
  R3  H3.What It Says         — record the state-vs-structure conflation and
                                split the question.
  R4  C1.Empirical Values     — retire the implied-D_eff column as a quantity
                                (builds on the geometric-impossibility flag
                                added earlier today).
  R5  X1.Predicted Scaling    — retire the 2.7 figure as a quantity (builds
                                on the mislabel correction added earlier today).

NOT IN SCOPE (deferred, owner's call)
--------------------------------------
  - Promoting P14/P16 to the front of the scaling queue
  - Downgrading P12
Re-prioritising conjectures is a larger decision than correcting text.

Run: python3 scripts/migrations/m0_scaling_reformulation_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-scaling-reformulation-2026-05-04"


EDITS = [
    # ------------------------------------------------------------------ R1
    ("R1", "sections", {"entry_id": "C1", "section_name": "What's Established"},
     "content", "append",
     "\n\n**FRAMING (elevated 2026-05-04).** The curvature result above is not "
     "one fact among several — it constrains what any scaling framework can "
     "claim. **If the log-log relation is curved, there is no single "
     "\"metabolic exponent\" to explain.** The local slope varies with body "
     "mass, so every study reporting *the* exponent is fitting a straight "
     "line to a curve and obtaining a value determined substantially by "
     "which mass range it sampled.\n\n"
     "This offers a parsimonious account of the cross-taxon spread that "
     "does not require any new parameter: small-mammal samples yield ~2/3, "
     "large-mammal samples ~3/4, broad samples something between, and "
     "phylogenetically-corrected strict BMR 0.676. Those need not be four "
     "values of a hidden variable; they are consistent with four samplings "
     "of one curve, plus methodological differences. Dodds, Rothman & Weitz "
     "(2001, anchored on this entry) press further, arguing the data may not "
     "establish 3/4 at all.\n\n"
     "**Consequence for the framework:** H5's $\\beta(\\lambda)$ exists to "
     "explain exponent variation across taxa and states. To the extent that "
     "variation is curvature plus sampling, $\\lambda$ is explaining an "
     "artifact. This does not falsify H5 — a curved relation is compatible "
     "with an underlying two-regime structure — but it removes the "
     "motivation that made $\\lambda$ look necessary, and it means the "
     "burden is on H5 to show it explains something the curve does not "
     "already account for. See H5's reframing note."),

    # ------------------------------------------------------------------ R2
    ("R2", "sections", {"entry_id": "H5", "section_name": "What It Says"},
     "content", "append",
     "\n\n---\n\n"
     "**REFRAMED 2026-05-04 — this is a descriptive interpolation with a "
     "documented failure, not a law.** Retained in full per the "
     "falsifications-as-learning-artifacts rule; the table above is the "
     "original formulation and is preserved unchanged.\n\n"
     "**What is wrong with it, at root:** the formula was built by "
     "interpolating between two *chosen* endpoints rather than derived from "
     "a mechanism. West-Brown-Enquist earned $\\beta = 3/4$ from three "
     "physical premises (space-filling networks, size-invariant terminal "
     "units, transport-cost minimisation). $\\beta(\\lambda)$ adopts that "
     "result as one anchor, selects $\\beta = 1$ as the other because it "
     "resembles a no-network limit, and interpolates linearly. **No "
     "mechanism generates the interpolation.** $\\lambda$ is the position "
     "along a line that was drawn rather than derived.\n\n"
     "**The documented failure.** $\\beta(\\lambda)$ is a weighted average, "
     "so its output is confined between its endpoints. With WBE's own "
     "$d_f = 3$ the achievable range is $\\beta \\in [0.750,\\ 1.000]$, and "
     "with P13's floor $\\lambda_{\\min} = 0.5$ it narrows to "
     "$[0.750,\\ 0.875]$. **Observed strict mammalian BMR is 0.676** (C1, "
     "95% CI ±0.013) — below the floor, outside the range for any "
     "$\\lambda \\in [0,1]$. Forcing the algebra returns $\\lambda = 1.296$, "
     "i.e. \"130% of the theoretical optimum,\" which is meaningless on any "
     "reading of $\\lambda$.\n\n"
     "**This is an endpoint failure, not a $\\lambda$ failure.** $\\lambda$ "
     "is only the weight; a weighted average cannot escape the two values "
     "being averaged. No reinterpretation of $\\lambda$ repairs it. The "
     "endpoints themselves are wrong, and choosing them correctly must "
     "precede any definition of $\\lambda$ — because the endpoints determine "
     "what $\\lambda$ is a fraction *of*.\n\n"
     "**Candidate repairs, none adopted:** (a) keep $[0.75, 1.00]$ and "
     "reject $d_f = 3$, which owes an account of why mammalian vasculature "
     "is not space-filling; (b) use $[2/3,\\ 3/4]$ — surface law to network "
     "optimum — which contains the BMR data and maps onto the historical "
     "2/3-vs-3/4 debate, but cannot reach MMR ~0.87 or urban ~1.15; (c) "
     "different endpoint pairs for different regimes, which is two formulas "
     "wearing one name; (d) abandon the weighted-average form entirely.\n\n"
     "**Related failures recorded elsewhere:** P11 (cannot express urban "
     "superlinear exponents; the same segment-bound argument from the other "
     "side), C1 Empirical Values (inverting this formula yields "
     "geometrically impossible $d_f$ for reptiles and fish), H3 "
     "(state-vs-structure conflation in $\\lambda$)."),

    # ------------------------------------------------------------------ R3
    ("R3", "sections", {"entry_id": "H3", "section_name": "What It Says"},
     "content", "append",
     "\n\n---\n\n"
     "**CONFLATION RECORDED 2026-05-04 — $\\lambda$ is currently used for "
     "two incompatible quantities.**\n\n"
     "- **As a state variable.** X1 assigns $\\lambda = 1$ at rest and "
     "$\\lambda = \\lambda_{\\min} \\approx 0.46$ at maximum exertion for "
     "the *same animal*. This varies minute to minute.\n"
     "- **As a structural variable.** C1's cross-taxon table implies a "
     "distinct value per clade (mammals, birds, reptiles, fish). This is "
     "fixed for a species by its developmental programme.\n\n"
     "These cannot be the same quantity. An animal's vascular anatomy does "
     "not change when it begins to run, so whatever distinguishes resting "
     "from maximal metabolism is not what distinguishes a bird from a "
     "reptile. One symbol has been carrying both, and the two readings need "
     "different explanations:\n\n"
     "- **Cross-species variation** is plausibly curvature plus sampling "
     "plus phylogeny (see C1's framing note) and may require no parameter "
     "at all.\n"
     "- **Within-organism BMR-vs-MMR variation** is a real physiological "
     "difference requiring a real explanation — but it cannot be a "
     "structural parameter, for the reason just given.\n\n"
     "**On the definition itself.** The opening sentence above defines "
     "$\\lambda$ as \"the degree to which a system's output is governed by "
     "its fractal geometry vs. by linear, unstructured dynamics\" — that is, "
     "by its effect on the exponent. A quantity defined by its effect on the "
     "observable it is invoked to explain cannot be measured independently "
     "of that observable, and the framework cannot be contradicted by any "
     "measurement inside its range. **The test a repaired definition must "
     "pass: state what $\\lambda$ is without mentioning $\\beta$ or any "
     "scaling exponent, such that someone could measure it by a route that "
     "does not pass through metabolic rate.**\n\n"
     "**Most promising candidate to date** (owner, this session): "
     "$\\lambda$ as *realisation fraction* — how much of the theoretically "
     "optimal network topology a real organism's vasculature actually "
     "achieves, given developmental and resource constraints. This is "
     "measurable in principle by direct anatomy (micro-CT, corrosion "
     "casting) compared against the computed optimum, with no metabolic "
     "measurement involved. It also changes network *topology* rather than "
     "operating *efficiency*, which matters: efficiency changes move the "
     "prefactor, only topology changes the exponent. Candidates rejected on "
     "that test this session: capillary recruitment (wrong sign), "
     "impedance-matching degradation (prefactor, not exponent).\n\n"
     "**Blocked on the endpoint question.** The realisation-fraction "
     "definition cannot be finalised until H5's endpoints are settled, since "
     "\"fraction of the optimum\" requires knowing which optimum. See H5's "
     "reframing note.\n\n"
     "**Consequence for the cost claim below.** P15's "
     "$\\text{Cost} \\propto (1-\\lambda)^2 \\cdot d_f$ is motivated here as "
     "a Landauer-class cost of *maintaining synchronisation*. If $\\lambda$ "
     "is not a synchronisation, that motivation lapses. The functional form "
     "may survive re-read as a quadratic *penalty for departure from "
     "optimum*, which is a standard shape — but it would need rederiving on "
     "that basis. Note also that as written the cost *vanishes* at "
     "$\\lambda = 1$, which reads oddly for a claim about the cost of "
     "maintaining perfect coherence."),

    # ------------------------------------------------------------------ R4
    ("R4", "sections", {"entry_id": "C1", "section_name": "Empirical Values"},
     "content", "append",
     "\n\n**RETIRED AS A QUANTITY (2026-05-04).** The implied "
     "$D_{\\text{eff}}$ column is withdrawn from use in any inference. It is "
     "retained visibly per the no-deletions rule, and the two notes above "
     "(derived-not-measured; two values geometrically impossible) stand as "
     "the record of why.\n\n"
     "The operation that produced the column — inverting "
     "$\\beta = d_f/(d_f+1)$ on an observed exponent — is invalid here on "
     "three counts: the relation is applied far outside the range it was "
     "derived for; the observed exponents may be samplings of a curve rather "
     "than estimates of a constant (see this entry's framing note); and the "
     "results include values exceeding the embedding dimension. **These "
     "numbers should not appear in downstream reasoning as though they were "
     "measurements of vascular geometry.** Affected: P2, P6, X1, and any "
     "argument routing through a $d_f$ obtained by inversion rather than by "
     "anatomy."),

    # ------------------------------------------------------------------ R5
    ("R5", "sections", {"entry_id": "X1", "section_name": "Predicted Scaling"},
     "content", "append",
     "\n\n**RETIRED AS A QUANTITY (2026-05-04).** Following C1's withdrawal "
     "of its implied-$D_{\\text{eff}}$ column, the figure $d_f \\approx 2.7$ "
     "used throughout this section is withdrawn from use in inference. It "
     "was obtained by inverting $\\beta = d_f/(d_f+1)$ on an observed "
     "exponent, and that operation is no longer treated as valid (see C1 "
     "Empirical Values).\n\n"
     "The predictions computed above from 2.7 are therefore **not "
     "independent predictions** — they reproduce the exponent that was used "
     "to generate the input. Retained per the no-deletions rule as a record "
     "of the circularity, not as a result.\n\n"
     "A genuine test of this entry requires $d_f$ measured **anatomically** "
     "— by micro-CT, corrosion casting, or angiographic reconstruction of "
     "real vascular trees — and then used to predict $\\beta$, which is then "
     "compared against independently measured metabolic rate. No such "
     "measurement has been performed. Until it is, X1 has no predictive "
     "content."),
]


ANCHORS = [
    ("C1", "doi", "10.1038/nature08920", None,
     "Kolokotrones, Savage, Deeds, Fontana 2010 - Curvature in metabolic scaling",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Elevated to framing status 2026-05-04. Demonstrates the log-log "
     "metabolic relation is CURVED rather than a single power law — local "
     "slope near 2/3 for small mammals, near 3/4 for large. Load-bearing "
     "consequence: there is no single 'metabolic exponent' to explain, so "
     "much of the cross-taxon exponent spread may be a sampling artifact of "
     "mass range rather than a physical phenomenon requiring a parameter. "
     "This is the finding that most constrains H5's beta(lambda) framework, "
     "and it was already present in C1's own prose before this session "
     "drew the implication."),
]


CALIBRATIONS = [
    ("H5", "entry", "Speculative", TODAY, SESSION,
     "Reframed: descriptive interpolation with documented endpoint failure, not a law",
     "Root diagnosis: beta(lambda) interpolates between two CHOSEN endpoints "
     "rather than deriving from a mechanism. WBE earned 3/4 from physical "
     "premises; beta(lambda) adopts it as an anchor, picks beta=1 as the "
     "other, and draws a line nothing generates. Documented failure: a "
     "weighted average is confined between its endpoints, so with d_f=3 the "
     "range is [0.750, 0.875] under P13's floor, but observed strict "
     "mammalian BMR is 0.676 — outside for any lambda in [0,1]; forcing the "
     "algebra gives lambda=1.296. This is an ENDPOINT failure, not a lambda "
     "failure, and no reinterpretation of lambda repairs it. Four candidate "
     "repairs recorded in prose, none adopted. Entry preserved in full per "
     "the falsification rule."),

    ("H3", "entry", "Speculative", TODAY, SESSION,
     "lambda conflates a state variable and a structural variable; definition is circular",
     "Two problems recorded. (1) CONFLATION: X1 uses lambda as a state "
     "variable (1 at rest, 0.46 at max exertion, same animal); C1's "
     "cross-taxon table uses it as a structural variable (per-clade). An "
     "animal's anatomy does not change when it starts running, so these "
     "cannot be one quantity. (2) CIRCULARITY: H3 defines lambda by its "
     "effect on the exponent, so it cannot be measured independently of the "
     "observable it explains, and the framework cannot be contradicted "
     "inside its range. Test for a repaired definition stated in prose. Most "
     "promising candidate (owner, this session): realisation fraction — how "
     "much of the theoretically optimal topology a real network achieves — "
     "which is anatomically measurable and changes topology rather than "
     "efficiency. Blocked pending H5's endpoint resolution."),

    ("C1", "entry", "Established", TODAY, SESSION,
     "Curvature elevated to framing; implied-D_eff column retired as a quantity",
     "Kolokotrones 2010 curvature finding promoted from a recorded fact to a "
     "framing statement, with the implication drawn: if the relation is "
     "curved there is no single exponent to explain, and cross-taxon spread "
     "may be sampling artifact rather than physics. Anchored to "
     "doi:10.1038/nature08920. Separately, the implied-D_eff column is "
     "retired from use in inference (retained visibly per no-deletions) — "
     "the inversion operation is invalid outside its derivation range, "
     "applied to possibly-artifactual exponents, and yields values above the "
     "embedding dimension. C1's own empirical content remains Established; "
     "the retirement concerns the derived column only."),

    ("X1", "entry", "Speculative", TODAY, SESSION,
     "d_f = 2.7 retired as a quantity; entry has no independent predictive content",
     "Following C1's retirement of the inverted-d_f operation, X1's 2.7 is "
     "withdrawn from inference. The predictions computed from it are not "
     "independent — they reproduce the exponent used to generate the input. "
     "Retained per no-deletions as a record of the circularity. A genuine "
     "test requires d_f measured anatomically (micro-CT, corrosion casting, "
     "angiographic reconstruction) then used to predict beta against "
     "independently measured metabolic rate. No such measurement exists."),

    ("scaling_framework_root_diagnosis", "structural_observation", "Established",
     TODAY, SESSION,
     "beta(lambda)'s failures trace to interpolation-without-mechanism",
     "Session finding: the beta(lambda) framework's symptoms — endpoints not "
     "containing the data, lambda unmeasurable, range failing for cities, "
     "unphysical inverted d_f, lambda meaning two things — all follow from "
     "one root cause. The formula interpolates between chosen endpoints "
     "rather than deriving from a mechanism. Recorded as Established because "
     "it is a statement about the framework's construction, verifiable by "
     "inspection, not a claim about biology. Constructive consequence: the "
     "surviving research direction is to predict INDIVIDUAL organisms from "
     "measured anatomy rather than cross-species exponents — which sidesteps "
     "the curvature problem, is falsifiable on n=1, and yields the scaling "
     "result as a consequence rather than assuming it. The WBE decomposition "
     "B = N_capillaries x (load per capillary) supports this, splitting the "
     "question into an anatomical part and a physiological part that are "
     "separately measurable, and resolving BMR-vs-MMR without a structural "
     "parameter (same capillary count, different load)."),
]


def fetch(cur, table, where, col):
    wsql = " AND ".join(f"{k}=?" for k in where)
    cur.execute(f"SELECT {col} FROM {table} WHERE {wsql}", tuple(where.values()))
    row = cur.fetchone()
    if row is None:
        raise RuntimeError(f"Row not found: {table} {where}")
    return row[0] or ""


def main() -> None:
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")

    print("=" * 72)
    print("PHASE 1 — validation (dry run)")
    print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    planned, seen = [], set()

    for label, table, where, col, mode, *args in EDITS:
        target = (table, tuple(sorted(where.items())), col)
        if target in seen:
            conn.close()
            raise SystemExit(f"[{label}] ABORT — duplicate target {target}")
        seen.add(target)

        current = fetch(cur, table, where, col)
        if mode == "replace":
            find, repl = args
            if find not in current:
                conn.close()
                raise SystemExit(f"[{label}] FAIL — anchor not found: {find[:80]!r}")
            new = current.replace(find, repl, 1)
            print(f"  [{label}] OK — replace ({len(find)} -> {len(repl)} chars)")
        else:
            (suffix,) = args
            if current.endswith(suffix):
                print(f"  [{label}] OK — already applied, skipping")
                continue
            new = current + suffix
            print(f"  [{label}] OK — append (+{len(suffix)} chars)")
        planned.append((label, table, where, col, new))

    conn.close()

    if planned:
        print()
        print("=" * 72)
        print("PHASE 2 — apply")
        print("=" * 72)
        conn = sqlite3.connect(DS_WIKI_DB)
        cur = conn.cursor()
        for label, table, where, col, new in planned:
            wsql = " AND ".join(f"{k}=?" for k in where)
            cur.execute(f"UPDATE {table} SET {col}=? WHERE {wsql}",
                        (new, *where.values()))
            if cur.rowcount != 1:
                conn.rollback(); conn.close()
                raise SystemExit(f"[{label}] hit {cur.rowcount} rows; rolled back")
            print(f"  [{label}] WRITE — {table} {where}")
        conn.commit(); conn.close()

        print()
        print("=" * 72)
        print("PHASE 3 — post-write verification")
        print("=" * 72)
        conn = sqlite3.connect(DS_WIKI_DB)
        cur = conn.cursor()
        ok = True
        for label, table, where, col, expected in planned:
            if fetch(cur, table, where, col) == expected:
                print(f"  [{label}] OK — verified")
            else:
                print(f"  [{label}] DRIFT")
                ok = False
        conn.close()
        if not ok:
            raise SystemExit("Post-write drift; investigate")
    else:
        print("\nAll prose edits already applied.")

    print()
    print("=" * 72)
    print("PHASE 4 — anchors + calibration")
    print("=" * 72)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    hcur = hc.cursor()
    n_a = 0
    for (eid, src, ident, rev, title, tier, stab, rel, role, conf, notes) in ANCHORS:
        hcur.execute("""
            INSERT OR IGNORE INTO external_anchors (
                entry_id, source, identifier, revision_id, title, tier,
                source_stability_class, relationship, canonical_role,
                verified_date, verified_by_session, confidence, notes
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (eid, src, ident, rev, title, tier, stab, rel, role,
              TODAY, SESSION, conf, notes))
        n_a += hcur.rowcount
    n_c = 0
    for (eid, etype, confv, cdate, aref, short, rationale) in CALIBRATIONS:
        hcur.execute("""
            INSERT INTO confidence_calibration (
                entity_id, entity_type, confidence, calibration_date,
                audit_ref, short_status, rationale
            ) VALUES (?,?,?,?,?,?,?)
        """, (eid, etype, confv, cdate, aref, short, rationale))
        n_c += 1
    hc.commit(); hc.close()
    print(f"  anchors inserted:      {n_a}")
    print(f"  calibrations inserted: {n_c}")
    print()
    print(f"Migration complete. Session: {SESSION}")


if __name__ == "__main__":
    main()
