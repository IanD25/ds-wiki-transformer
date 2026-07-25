"""
Scaling-law accuracy corrections — 2026-05-04

Triggered by review of the Veritasium "1 billion heartbeats" video against
the wiki's scaling cluster. Owner-approved 2026-05-04.

IMPORTANT SCOPE NOTE: an initial review claimed C1 lacked (a) a caveat that
the implied D_eff column is derived-not-measured and (b) the mass-crossover
competing explanation. BOTH WERE ALREADY PRESENT in C1 (Empirical Values
closing note; What's Established citing Kolokotrones 2010 + Xiao 2015).
Those claims were withdrawn. This migration only applies the four
corrections that survived that check.

Edits (all target DISTINCT table/row/column triples — no same-column
collision, which was the B2a bug in the Tier-B prose migration):

  S1  X1.Predicted Scaling   — "d_f ~ 2.7 (empirical WBE value)" is
                               mislabeled. WBE's own derivation uses
                               d_f = 3 (space-filling exchange surface,
                               giving volume ~ L^4 hence L ~ M^(1/4)).
                               2.7 is back-calculated by inverting
                               beta = d_f/(d_f+1) on the empirical
                               beta = 0.73. Relabel + carry C1's caveat.

  S2  C1.Empirical Values    — C1 correctly flags the column as a framework
                               calculation, but does not note that two of
                               the four implied values EXCEED the embedding
                               dimension: reptiles ~3.2 and fish ~7.3. A
                               fractal dimension cannot exceed the dimension
                               of the space the network is embedded in.
                               Add that explicitly.

  S3  P11.critical_gaps      — STRUCTURAL BOUND. beta(lambda) has range
                               [d_f/(d_f+1), 1] for lambda in [0,1]; it is
                               bounded ABOVE BY 1. Urban socioeconomic
                               exponents are ~1.15 (superlinear). P11 claims
                               urban scaling tracks the same D/(D+1) form.
                               The superlinear half of urban scaling is
                               structurally inexpressible in that form.
                               P11 should be narrowed to infrastructure.

  S4  H5.What's Established  — H5 asserts the observed exponent variation is
                               "variation in lambda, not in d_f" without
                               acknowledging the mass-crossover competitor
                               that C1 already documents. Add the competitor
                               and state the separable test.

Run: python3 scripts/migrations/m0_scaling_corrections_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-scaling-corrections-2026-05-04"


# ============================================================================
# TIER B — ds_wiki.db prose edits
# (label, table, where-dict, column, mode, *args)
# ============================================================================

EDITS = [
    # ------------------------------------------------------------------ S1
    ("S1", "sections", {"entry_id": "X1", "section_name": "Predicted Scaling"},
     "content", "replace",
     "For mammals with $d_f \\approx 2.7$ (empirical WBE value):",
     "For mammals with $d_f \\approx 2.7$ — **NOTE (corrected 2026-05-04): "
     "this is NOT an \"empirical WBE value.\"** WBE's own derivation uses "
     "$d_f = 3$: the exchange surface of the circulatory network is "
     "space-filling in 3D, so surface $\\sim L^3$, volume $\\sim L^4$, hence "
     "$L \\propto M^{1/4}$ and $\\beta = 3/4$ exactly. The figure 2.7 here is "
     "**back-calculated** by inverting $\\beta = d_f/(d_f+1)$ on the observed "
     "$\\beta \\approx 0.73$ ($0.73/0.27 = 2.70$). It is the observed exponent "
     "re-expressed, not an independent measurement of vascular geometry — "
     "the same caveat C1 attaches to its implied-$D_{\\text{eff}}$ column. "
     "Any inference that runs from this $d_f$ back to $\\beta$ is circular. "
     "With that caveat stated:"),

    # ------------------------------------------------------------------ S2
    ("S2", "sections", {"entry_id": "C1", "section_name": "Empirical Values"},
     "content", "append",
     "\n\n**Geometric-impossibility flag (added 2026-05-04):** two of the four "
     "implied $D_{\\text{eff}}$ values above **exceed the embedding "
     "dimension** — reptiles at ~3.2 and fish at ~7.3. A fractal dimension "
     "cannot exceed the dimension of the space the network is embedded in; "
     "a physical branching network in 3D space has $d_f \\leq 3$ by "
     "construction. These values are therefore not merely "
     "derived-rather-than-measured (already noted above) but **unphysical as "
     "geometric quantities**. Two readings are available and the wiki does "
     "not currently choose between them: (a) the relation "
     "$\\beta = d_f/(d_f+1)$ does not hold outside the mammalian range it was "
     "fitted on, so inverting it elsewhere produces meaningless numbers; or "
     "(b) $D_{\\text{eff}}$ in this framework is not a spatial fractal "
     "dimension at all but some other effective quantity that happens to "
     "coincide with one for mammals. Reading (b) requires stating what that "
     "quantity is. Until one is chosen, the implied-$D_{\\text{eff}}$ column "
     "should not be used as evidence for any geometric claim. See "
     "[[g:effective_dimension_hausdorff]] vs "
     "[[g:effective_dimension_pr_fim]] for the distinction at issue."),

    # ------------------------------------------------------------------ S3
    ("S3", "conjectures", {"id": "P11"}, "critical_gaps", "append",
     "\n\n**STRUCTURAL BOUND (added 2026-05-04) — this is the load-bearing "
     "gap, not a data gap.** The $\\beta(\\lambda)$ formula in H5, "
     "$\\beta = \\lambda \\cdot [d_f/(d_f+1)] + (1-\\lambda) \\cdot 1$, has "
     "range $[d_f/(d_f+1),\\ 1]$ for $\\lambda \\in [0,1]$. It is **bounded "
     "above by 1**, attained at $\\lambda = 0$. Adding P13's floor "
     "$\\lambda_{\\min} = (d_f-1)/(d_f+1)$ narrows it further: for $d_f = 3$, "
     "$\\lambda \\geq 0.5$ and $\\beta \\in [0.75,\\ 0.875]$.\n\n"
     "Urban scaling has two families of exponent (C2):\n"
     "- **Infrastructure** (roads, cables, gas stations): ~0.80-0.85, "
     "sublinear. **Fits** inside the achievable window.\n"
     "- **Socioeconomic** (wages, GDP, patents, crime): ~1.15, superlinear. "
     "**Structurally inexpressible** — no $\\lambda \\in [0,1]$ yields "
     "$\\beta > 1$. Recovering 1.15 would require $\\lambda \\approx -0.6$, "
     "and H3 defines $\\lambda$ as a coherence fraction on $[0,1]$ with no "
     "meaning below zero.\n\n"
     "P11 as stated claims urban scaling tracks \"the same $D/(D+1)$ "
     "functional form as metabolic scaling.\" That claim is **false for the "
     "superlinear half of urban scaling**, which is also the more "
     "distinctive half of the Bettencourt-West result. Two honest "
     "resolutions: (i) narrow P11 explicitly to urban *infrastructure* "
     "scaling, where it is at least dimensionally admissible; or (ii) supply "
     "a mechanism by which the framework produces exponents above unity — "
     "which the current $\\beta(\\lambda)$ construction cannot. Until one is "
     "taken, P11 should not be described as covering urban scaling "
     "generally. Pattern-tag: over-extension-beyond-formula-range."),

    # ------------------------------------------------------------------ S4
    ("S4", "sections", {"entry_id": "H5", "section_name": "What's Established"},
     "content", "append",
     "\n\n**Competing explanation (added 2026-05-04).** The closing sentence "
     "above attributes observed exponent variation to $\\lambda$ rather than "
     "$d_f$. A well-supported alternative attributes it to **body mass "
     "range**: Kolokotrones et al. (*Nature*, 2010) showed the log-log "
     "metabolic relation is **curved**, with slope near 2/3 for small "
     "mammals and near 3/4 for large ones, and Xiao et al. (2015) located a "
     "breakpoint near 10 kg. C1 records both. Recent bird-metabolism work "
     "and studies of cold-blooded taxa report slopes inconsistent with a "
     "single universal exponent, and Dodds, Rothman & Weitz (2001) argue the "
     "supporting data are too noisy to establish 3/4 at all.\n\n"
     "These are **not** the same claim as H5's. H5 says the exponent varies "
     "with *activity/coherence state*; the crossover account says it varies "
     "with *body mass*. Both fit the same scatter. They are separable in "
     "principle: H5 predicts the exponent shifts with activity state **at "
     "fixed mass**, the crossover account predicts it shifts with mass **at "
     "fixed activity state**. A dataset resolving both axes would "
     "discriminate. **No such test has been run**, and H5 should not be "
     "read as having displaced the crossover explanation. Until that test "
     "exists, H5's reframing is one admissible account among at least two."),
]


# ============================================================================
# TIER A — wiki_history.db anchors
# ============================================================================

ANCHORS = [
    ("C1", "doi", "10.1006/jtbi.2000.2238", None,
     "Dodds, Rothman, Weitz 2001 - Re-examination of the '3/4-law' of metabolism",
     1, "canonical", "contradicts", None, "high",
     "Deep-review 2026-05-04: Dodds-Rothman-Weitz (J. Theor. Biol. 209, 9-27, "
     "2001) re-analyze the classic metabolic datasets and argue the evidence "
     "does not establish a 3/4 exponent — data are consistent with 2/3 for "
     "much of the range and the statistical case for 3/4 is weaker than "
     "usually presented. Dodds has continued to press this line publicly. "
     "Filed as `contradicts` because it disputes the empirical foundation "
     "C1 rests on, not merely the WBE mechanism. Relevant to H5/X1/P2/P11, "
     "all of which take the quarter-power family as given."),
]


# ============================================================================
# TIER A — calibration records
# ============================================================================

CALIBRATIONS = [
    ("P11", "conjecture", "Speculative", TODAY, SESSION,
     "Structurally cannot express urban superlinear exponents; narrow to infrastructure",
     "beta(lambda) is bounded above by 1 for lambda in [0,1]; with P13's "
     "floor and d_f=3 the achievable range is [0.75, 0.875]. Urban "
     "socioeconomic scaling (~1.15 superlinear) is outside that range for "
     "any admissible lambda. P11's claim to cover urban scaling via the same "
     "D/(D+1) form is false for the superlinear half. Urban infrastructure "
     "(~0.80-0.85) does fit. Recommend narrowing P11 to infrastructure or "
     "supplying a super-unity mechanism. Status unchanged (Speculative) but "
     "scope now explicitly bounded."),

    ("X1", "entry", "Speculative", TODAY, SESSION,
     "d_f = 2.7 relabeled: back-calculated, not an empirical WBE value",
     "X1 described d_f ~ 2.7 as the 'empirical WBE value'. It is not. WBE's "
     "derivation uses d_f = 3 (space-filling exchange surface). 2.7 is "
     "obtained by inverting beta = d_f/(d_f+1) on the observed beta = 0.73. "
     "Corrected in prose 2026-05-04. This is the same circularity C1 already "
     "flags for its implied-D_eff column; X1 had not carried the caveat."),

    ("C1", "entry", "Established", TODAY, SESSION,
     "Implied D_eff values for reptiles (~3.2) and fish (~7.3) are unphysical",
     "C1 already correctly flagged the implied-D_eff column as a framework "
     "calculation rather than an independent measurement. Added 2026-05-04: "
     "two of the four values exceed the embedding dimension and are therefore "
     "unphysical as geometric quantities (a fractal dimension cannot exceed "
     "the dimension of the embedding space). Either beta = d_f/(d_f+1) does "
     "not hold outside the mammalian fitting range, or D_eff is not a spatial "
     "fractal dimension. The wiki does not currently choose. C1's own "
     "empirical content (White & Seymour 2003, Kolokotrones 2010, Xiao 2015) "
     "remains Established; the flag concerns the derived column only."),

    ("H5", "entry", "Speculative", TODAY, SESSION,
     "Mass-crossover is a live competing explanation for exponent variation",
     "H5 attributes observed exponent variation to lambda rather than d_f. "
     "The Kolokotrones 2010 curvature result plus Xiao 2015's ~10 kg "
     "breakpoint constitute a competing account attributing the same "
     "variation to body mass. Both fit the scatter. Separable test: lambda "
     "predicts variation with activity state at fixed mass; crossover "
     "predicts variation with mass at fixed activity state. No such test has "
     "been run. Added to H5 prose 2026-05-04. H5 remains Speculative and "
     "should not be presented as having displaced the crossover account."),
]


# ---------------------------------------------------------------- helpers

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

    # ---------------- PHASE 1: validate, no writes ----------------
    print("=" * 72)
    print("PHASE 1 — validation (dry run)")
    print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    planned = []
    seen_targets = set()

    for label, table, where, col, mode, *args in EDITS:
        target = (table, tuple(sorted(where.items())), col)
        if target in seen_targets:
            conn.close()
            raise SystemExit(
                f"[{label}] ABORT — duplicate target {target}. Two edits to the "
                "same column must be composed into one replacement (see B2a bug)."
            )
        seen_targets.add(target)

        current = fetch(cur, table, where, col)

        if mode == "replace":
            find, repl = args
            if find not in current:
                print(f"  [{label}] FAIL — anchor not found")
                print(f"         looking for: {find[:90]!r}")
                conn.close()
                raise SystemExit("Aborting before any writes.")
            new = current.replace(find, repl, 1)
            print(f"  [{label}] OK — replace verified ({len(find)} -> {len(repl)} chars)")
        else:  # append
            (suffix,) = args
            if current.endswith(suffix):
                print(f"  [{label}] OK — already applied (idempotent), skipping")
                continue
            new = current + suffix
            print(f"  [{label}] OK — append verified (+{len(suffix)} chars)")

        planned.append((label, table, where, col, new))

    conn.close()

    if not planned:
        print("\nAll edits already applied. Nothing to do.")
    else:
        # ---------------- PHASE 2: apply ----------------
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
                raise SystemExit(f"[{label}] UPDATE hit {cur.rowcount} rows; rolled back")
            print(f"  [{label}] WRITE — {table} {where} {col}")
        conn.commit()
        conn.close()

        # ---------------- PHASE 3: verify ----------------
        print()
        print("=" * 72)
        print("PHASE 3 — post-write verification")
        print("=" * 72)
        conn = sqlite3.connect(DS_WIKI_DB)
        cur = conn.cursor()
        ok = True
        for label, table, where, col, expected in planned:
            actual = fetch(cur, table, where, col)
            if actual == expected:
                print(f"  [{label}] OK — verified")
            else:
                print(f"  [{label}] DRIFT — {len(actual)} vs expected {len(expected)}")
                ok = False
        conn.close()
        if not ok:
            raise SystemExit("Post-write drift detected; investigate")

    # ---------------- PHASE 4: anchors + calibration ----------------
    print()
    print("=" * 72)
    print("PHASE 4 — anchors + calibration (wiki_history.db)")
    print("=" * 72)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    hcur = hc.cursor()

    n_anchor = 0
    for (eid, src, ident, rev, title, tier, stab, rel, role, conf, notes) in ANCHORS:
        hcur.execute("""
            INSERT OR IGNORE INTO external_anchors (
                entry_id, source, identifier, revision_id, title, tier,
                source_stability_class, relationship, canonical_role,
                verified_date, verified_by_session, confidence, notes
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (eid, src, ident, rev, title, tier, stab, rel, role,
              TODAY, SESSION, conf, notes))
        if hcur.rowcount:
            n_anchor += 1

    n_cal = 0
    for (eid, etype, confv, cdate, aref, short, rationale) in CALIBRATIONS:
        hcur.execute("""
            INSERT INTO confidence_calibration (
                entity_id, entity_type, confidence, calibration_date,
                audit_ref, short_status, rationale
            ) VALUES (?,?,?,?,?,?,?)
        """, (eid, etype, confv, cdate, aref, short, rationale))
        n_cal += 1

    hc.commit()
    hc.close()
    print(f"  anchors inserted:      {n_anchor}")
    print(f"  calibrations inserted: {n_cal}")

    print()
    print(f"Migration complete. Session: {SESSION}")


if __name__ == "__main__":
    main()
