r"""
Consistency pass, Phase 3 — residual-error sweep — 2026-10-18
(audit_ref gsw-consistency-pass-2026-10-18). Mode A: corrections only.

3.1  Corrected claims that survived elsewhere
     - H5 What's Established + What's Conjectured: the fabricated "Xiao et al.
       (2015)" citation was corrected in C1 on 2026-07-25 but survived here as
       fact; corrected to Dodds, Rothman & Weitz 2001. H5 What's Established
       also carried the "~2/3 small / ~3/4 large" slope gloss.
     - H5 What's Conjectured also states P12 as an untested HIGH-confidence
       claim (falsified 2026-07-25), "ENDPOINTS SETTLED" (superseded
       2026-07-25), and the curvature direction as an OPEN PUZZLE (resolved
       2026-07-25). A status note is prepended; text kept.
     - C1 Regime-First Generalization: same slope gloss, missed by the
       07-25 pass.
     - GT11 (three sections) and gate G12: "reject k = 3 at/beyond 5 sigma"
       and Cadoni "generic nonsingular" — same Fifth-Addendum corrections as
       P17/P23 in Phase 2. GT11's "two orders of magnitude" clause is not in
       Amendola et al.'s abstract and is not restated (quoted in the banner).
     - external_anchors id 900 (C1 -> Kolokotrones 2010): slope gloss in note.
     - calibration: saberi_2024_prb_priority_read's latest row still says
       "most direct prior art"; the Sixth Addendum correction was filed on
       CCA-1c instead. Correction row appended for the entity itself.
     Searched, not present as live claims: Bianconi as an independent second
     path; Saberi 2024 as direct prior art (outside calibration history).

3.2  Errors found in the Relatively Human podcast — present in the wiki:
     - Fisher information "underpins"/parallels the uncertainty principle:
       present as analogy-with-errors in IT05 (Constraint Category) and the
       M6 -> QM2 link (id 248). Corrected: Cramér–Rao is an estimation bound
       (and uses Fisher information, not its rank); Heisenberg–Robertson
       follows from the commutator; the quantum CR bound is metrology.
       Anchor added to IT05: Braunstein & Caves 1994 (adjacent_concept).
     - Frank 2009 as mechanism: present, uncited, in BIO3 ("additive genetic
       variance IS Fisher information… Natural selection is Fisher
       information maximization"). Corrected to a reformulation; anchor added
       to BIO3: Frank 2009 (cites).
     Not present: universality-class lump (liquid–gas / iron / percolation),
     91/48 vs 7/4, "confirmed to N decimal places", Kauffman √N cell types,
     Ashby variety ≡ attractor dimension, RG "guaranteed" outside physics,
     Feigenbaum governing the heart.

Calibration rows are appended only for entities that already have a
calibration history and where a correction is recorded (H5, C1,
saberi_2024_prb_priority_read). Labels unchanged. GT11, G12, BIO3, IT05 have
no calibration history; their corrections are recorded in dated banners and
listed in the session handover rather than given a first-ever label here.

Dry run by default; --apply writes. Aborts on duplicate (table, row, column)
targets. Idempotent. Read-back verifies every write.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-consistency-pass-2026-10-18"
D = "2026-10-18"
TAG = f"{D} (`{AUDIT_REF}`"

# (label, table, key-dict, column, prefix, [(find, replace)…], suffix)
EDITS = [
    # ── H5 What's Established ────────────────────────────────────────────────
    ("H5.established", "sections", {"entry_id": "H5", "section_name": "What's Established"}, "content", "",
     [("with slope near 2/3 for small mammals and near 3/4 for large ones, and Xiao et al. (2015) located a breakpoint near 10 kg. C1 records both.",
       "with a local slope rising from about 0.57 to about 0.87 across the fitted mass range (the 'near 2/3 for small mammals, near 3/4 for large ones' gloss comes from sub-range linear fits, not from the fitted derivative), and Dodds, Rothman & Weitz (2001) located a breakpoint near 10 kg (α = 0.668 ± 0.019 below it, 0.877 ± 0.088 above). C1 records both — and since 2026-07-25 records the curvature itself as contested (see C1's replication record).")],
     f"\n\n> **CITATION CORRECTED {TAG}).** The *Competing explanation* paragraph previously read: "
     "\"with slope near 2/3 for small mammals and near 3/4 for large ones, and Xiao et al. (2015) located a breakpoint near 10 kg.\" "
     "**No 'Xiao et al. 2015' paper exists** — the citation was found fabricated and corrected in C1 on 2026-07-25 but survived here. "
     "The ~10 kg breakpoint is Dodds, Rothman & Weitz 2001, already anchored to C1. The slope gloss also understated Kolokotrones et al. "
     "2010's fitted range (0.57–0.87). Original wording recorded here per the no-deletions rule."),

    # ── H5 What's Conjectured ────────────────────────────────────────────────
    ("H5.conjectured", "sections", {"entry_id": "H5", "section_name": "What's Conjectured"}, "content",
     f"> **STATUS NOTE — added {TAG}).** Three items below are superseded and kept as the record. "
     "(1) List item 1 calls P12 a 'HIGH confidence claim, untested' and item 2 calls cross-domain universality 'the primary falsification target': "
     "**P12 was falsified on 2026-07-25** — β(λ) ≤ 1 cannot reach urban exponents ~1.15 (see P12). "
     "(2) *ENDPOINTS SETTLED*: the [2/3, 3/4] decision was neither confirmed nor reversed but **superseded** on 2026-07-25 by the two-process "
     "derivation in *What The Math Says* — the endpoints are the exponents of the two contributing processes, to be identified rather than chosen. "
     "(3) Item (c)'s *OPEN PUZZLE* was **resolved** on 2026-07-25: the error was assuming constraints combine as a minimum rather than a sum "
     "(see C1 and the `curvature_direction_puzzle` calibration record), and Kolokotrones' own mechanism has since been read — a vascular "
     "pulsatile-to-smooth flow transition, not a thermal one. The '2026-05-04' dates in this section are a session label for work done "
     "2026-07-25 (see the date erratum in SESSION_HANDOVER_2026-05-04.md). "
     "*Original text follows, unchanged except for the corrected citation in (b).*\n\n",
     [(r"with Xiao's ~10 kg breakpoint at $\lambda \approx 0.5$. But that makes $\lambda$ mass-dependent rather than a species-level structural parameter — a **third** distinct reading, on top of the state-versus-structure conflation already recorded in H3.",
       r"with the ~10 kg breakpoint of Dodds, Rothman & Weitz (2001) at $\lambda \approx 0.5$. But that makes $\lambda$ mass-dependent rather than a species-level structural parameter — a **third** distinct reading, on top of the state-versus-structure conflation already recorded in H3."
       f"\n\n> **CITATION CORRECTED {TAG}).** Item (b) previously read \"with Xiao's ~10 kg breakpoint at $\\lambda \\approx 0.5$\". "
       "No 'Xiao et al. 2015' exists; the breakpoint is Dodds, Rothman & Weitz 2001. Original wording recorded here per the no-deletions rule.")],
     ""),

    # ── C1 Regime-First Generalization ───────────────────────────────────────
    ("C1.regime_first", "sections", {"entry_id": "C1", "section_name": "Regime-First Generalization (Tier 3 ‡_p)"}, "content", "",
     [("— slope ~2/3 for small mammals, ~3/4 for large ones —",
       "— a local slope rising from about 0.57 to about 0.87 across the fitted range, a curvature now recorded as contested in this entry's *What's Established* —")],
     f"\n\n> **CORRECTION {TAG}).** This section previously gave Kolokotrones et al. 2010's result as \"slope ~2/3 for small mammals, "
     "~3/4 for large ones\" — the understated range already corrected in *What's Established* on 2026-07-25 (fitted local slope 0.57–0.87). "
     "Also: 'the phase coherence of ATP synchronization' is the pre-2026-07-25 reading of λ; under H5's resolved definition λ is the "
     "fractional contribution of one process to total metabolic rate. Original wording recorded here per the no-deletions rule."),

    # ── GT11 ─────────────────────────────────────────────────────────────────
    ("GT11.claims", "sections", {"entry_id": "GT11", "section_name": "What It Claims"}, "content", "",
     [("showed GW merger rates reject k = 3 beyond 5 sigma — predicted merger rates exceed LIGO-Virgo-KAGRA observations by two orders of magnitude.",
       "found GWTC-3 merger-rate data in about 3σ tension with k = 3 (2σ upper limits k < 2.1 for the standard log-uniform delay-time distribution, k < 1.1 for the CCBH-corrected one); their >5σ figure is a forecast for ~250 further events, not a current-data result."),
      ("Cadoni et al. (JCAP, 2023) showed generic nonsingular GR interiors give k = 1, not k = 3 — the k = 3 case requires a very specific (gravastar-like) interior.",
       "Cadoni, Sanna, Pitzalis, Banerjee, Murgia, Hazra & Branchesi (JCAP 11, 007, 2023) showed k = 1 is the universal leading-order prediction for spherically-symmetric regular (nonsingular) GR BHs, with a further model-dependent term for horizonless objects; their own KS analysis of the Farrah sample prefers k = 3, which they read as possible evidence for non-GR BHs. The k = 3 case requires a very specific (gravastar-like) interior.")],
     f"\n\n> **CORRECTION {TAG}; applies M0 Fifth Addendum, Findings 1–2).** The CHALLENGING EVIDENCE paragraph previously read: "
     "\"Amendola et al. (MNRAS 528, 2377, 2024) showed GW merger rates reject k = 3 beyond 5 sigma — predicted merger rates exceed "
     "LIGO-Virgo-KAGRA observations by two orders of magnitude\" and \"Cadoni et al. (JCAP, 2023) showed generic nonsingular GR interiors "
     "give k = 1, not k = 3\". The 5σ figure is Amendola et al.'s forecast; current GWTC-3 data give ~3σ tension. The 'two orders of "
     "magnitude' clause does not appear in the paper's abstract and was not verified in this pass, so it is not restated. Cadoni et al. "
     "say 'universal' for regular BHs, not 'generic'. Original wording recorded here per the no-deletions rule."),
    ("GT11.math_form", "sections", {"entry_id": "GT11", "section_name": "Mathematical Form"}, "content", "",
     [("k = 1: Comoving scaling (generic nonsingular, Cadoni et al.)",
       "k = 1: Comoving scaling (regular/nonsingular GR BHs — universal at leading order, Cadoni et al. 2023)")],
     f"\n\n[Corrected {D}, {AUDIT_REF}: the k = 1 line previously read \"(generic nonsingular, Cadoni et al.)\"; "
     "Cadoni et al. 2023 say 'universal' for regular BHs.]"),
    ("GT11.math_says", "sections", {"entry_id": "GT11", "section_name": "What The Math Says"}, "content", "",
     [("and Cadoni et al. showed that the most natural nonsingular interiors give k = 1, not 3.",
       "and Cadoni et al. 2023 showed that regular (nonsingular) GR BHs give k = 1 at leading order — though their own analysis of the Farrah sample prefers k = 3.")],
     f"\n\n> **CORRECTION {TAG}; applies M0 Fifth Addendum, Finding 2).** Previously: \"Cadoni et al. showed that the most natural "
     "nonsingular interiors give k = 1, not 3.\" Original wording recorded here per the no-deletions rule."),

    # ── Gate G12 ─────────────────────────────────────────────────────────────
    ("G12.blocking", "gates", {"id": "G12"}, "blocking", "",
     [("currently reject k=3 at 5 sigma;",
       f"currently ~3σ tension with k=3 from GWTC-3 2σ upper limits (k < 2.1; Amendola et al. 2024) — not a rejection, the 5σ figure being their forecast [corrected {D}, {AUDIT_REF}; previously \"currently reject k=3 at 5 sigma\"];")],
     ""),

    # ── BIO3 (Frank 2009 as mechanism) ───────────────────────────────────────
    ("BIO3.claims", "sections", {"entry_id": "BIO3", "section_name": "What It Claims"}, "content", "",
     [("The deep structural bridge: additive genetic variance in fitness IS the Fisher information of the population about its environment. Natural selection is Fisher information maximization.",
       "Frank (2009, *J. Evol. Biol.* 22:231) argued that the theorem can be re-expressed in information-geometric terms: maximising the Fisher information a population captures about its environment yields Fisher's fundamental theorem. This is a reformulation of the theorem — it adds no mechanism and no prediction beyond it.")],
     f"\n\n> **CORRECTION {TAG}).** This entry previously read: \"The deep structural bridge: additive genetic variance in fitness IS the "
     "Fisher information of the population about its environment. Natural selection is Fisher information maximization.\" That stated, "
     "uncited, as an identity and a bridge what is Steven A. Frank's 2009 reformulation (doi:10.1111/j.1420-9101.2008.01647.x) — a "
     "re-expression of Fisher's fundamental theorem, not a mechanism. The link to M6 is an analogy: M6 is Fisher Information *Rank*, a "
     "different quantity from the Fisher information in Frank's argument. Original wording recorded here per the no-deletions rule."),
    ("BIO3.xrefs", "sections", {"entry_id": "BIO3", "section_name": "DS Cross-References"}, "content", "", [],
     f"\n\n[Corrected {D}, {AUDIT_REF}: \"maximizing Fisher information (M6) = maximizing fitness (BIO3)\" is Frank 2009's reformulation "
     "of Fisher's theorem, not an identity or a mechanism, and M6 is Fisher Information Rank — not the quantity in Frank's argument. "
     "See What It Claims.]"),
    ("BIO3.archetype", "sections", {"entry_id": "BIO3", "section_name": "Mathematical Archetype"}, "content", "", [],
     f"\n\n[Corrected {D}, {AUDIT_REF}: \"additive genetic variance IS Fisher information\" and \"fitness maximization = Fisher "
     "information maximization\" are Frank 2009's reformulation, not an identity that connects the framework to biology. See What It Claims.]"),

    # ── IT05 + link M6->QM2 (Fisher information vs uncertainty principle) ──
    ("IT05.constraint", "sections", {"entry_id": "IT05", "section_name": "Constraint Category"}, "content", "",
     [("This is the information-theoretic analog of the uncertainty principle — both state that precision is bounded by the curvature of the underlying probability/wavefunction space.",
       "It is at most a loose analogy to the uncertainty principle. Cramér–Rao limits how precisely a parameter can be *estimated* from data; the Heisenberg–Robertson relation limits the joint spread of two non-commuting observables in a *state* and follows from their commutator (Robertson 1929), not from Fisher information. The quantum counterpart of Cramér–Rao is the quantum Cramér–Rao bound of quantum metrology (Braunstein & Caves 1994). Uncertainty relations can be re-expressed in Fisher-information form for particular parameterisations, but that is a reformulation, not their origin.")],
     f"\n\n> **CORRECTION {TAG}).** Previously: \"This is the information-theoretic analog of the uncertainty principle — both state that "
     "precision is bounded by the curvature of the underlying probability/wavefunction space.\" Original wording recorded here per the "
     "no-deletions rule."),
    ("link248.description", "links", {"id": 248}, "description",
     f"[Corrected {D}, {AUDIT_REF}] Analogy only, and not via rank: the Cramér–Rao bound (estimator variance ≥ 1/F, using Fisher "
     "information — not its rank) limits parameter estimation; the Heisenberg–Robertson relation (ΔxΔp ≥ ℏ/2) bounds the spread of "
     "non-commuting observables in a state and follows from the commutator. The quantum Cramér–Rao bound belongs to quantum metrology. "
     "Previously: \"", [], "\""),
]

NEW_ANCHORS = [
    ("BIO3", "doi", "10.1111/j.1420-9101.2008.01647.x", None,
     "Frank 2009 - Natural selection maximizes Fisher information (J. Evol. Biol. 22:231-244; arXiv:0901.3742)",
     1, "active-literature", "cites", None, "high",
     "Source of BIO3's Fisher-information reading of Fisher's fundamental theorem, previously stated uncited as an identity. Frank "
     "re-expresses the theorem in information-geometric terms; it is a reformulation, not a mechanism, and adds no prediction beyond the "
     "theorem. Added 2026-10-18 (gsw-consistency-pass-2026-10-18)."),
    ("IT05", "doi", "10.1103/PhysRevLett.72.3439", None,
     "Braunstein & Caves 1994 - Statistical distance and the geometry of quantum states (PRL 72:3439)",
     1, "canonical", "adjacent_concept", None, "high",
     "Quantum Fisher information and the quantum Cramér–Rao bound — the quantum counterpart of IT05's Cramér–Rao bound, which belongs to "
     "quantum metrology. Recorded to correct IT05's framing of Cramér–Rao as an analog of the uncertainty principle, which follows from "
     "operator non-commutativity (Robertson 1929, anchored on QM2). Added 2026-10-18 (gsw-consistency-pass-2026-10-18)."),
]

ANCHOR_NOTE_FIXES = {
    900: (" CORRECTION 2026-10-18 (gsw-consistency-pass-2026-10-18): 'local slope near 2/3 for small mammals, near 3/4 for large' "
          "understates the paper's fitted range — the local exponent runs 0.57 to 0.87; the 2/3–3/4 gloss comes from sub-range linear "
          "fits. The curvature itself is contested per C1's replication record (2026-07-25)."),
}

CALIBRATIONS = [
    ("H5", "entry", "Speculative", D, AUDIT_REF,
     "Fabricated Xiao 2015 citation + slope gloss corrected; superseded items flagged",
     "Correction recorded, label unchanged. The fabricated 'Xiao et al. (2015)' citation, corrected in C1 on 2026-07-25, survived in H5 as "
     "fact (What's Established; What's Conjectured item b); both now cite Dodds, Rothman & Weitz 2001. The 'slope near 2/3 small / 3/4 large' "
     "gloss was corrected to Kolokotrones et al. 2010's fitted 0.57–0.87. A status note flags three superseded items in What's Conjectured: "
     "P12 described as untested (falsified 2026-07-25); ENDPOINTS SETTLED (superseded 2026-07-25 by the two-process derivation); the "
     "curvature OPEN PUZZLE (resolved 2026-07-25). Supersedes the 'Xiao 2015's ~10 kg breakpoint' statement in calibration row 67."),
    ("C1", "entry", "Established", D, AUDIT_REF,
     "Slope gloss corrected in Regime-First section (missed by 07-25 pass)",
     "Correction recorded, label unchanged (Kleiber-law entry Established; curvature contested per the 2026-07-25 row). The Regime-First "
     "Generalization section still gave Kolokotrones et al. 2010 as 'slope ~2/3 for small mammals, ~3/4 for large'; corrected to the fitted "
     "0.57–0.87 with a banner. Anchor 900's note carried the same gloss and was annotated. Note: calibration row 66's phrase 'Kolokotrones "
     "2010, Xiao 2015 remains Established' is superseded by row 82 and by this row."),
    ("saberi_2024_prb_priority_read", "literature_priority", "Speculative", D, AUDIT_REF,
     "Correction recorded: NOT direct prior art for CCA (Sixth Addendum 2026-04-08)",
     "Correction recorded, label unchanged. This entity's latest row (M0_2026-04-08_deep_research) still read 'Highest-priority single paper: "
     "most direct prior art in CCA mathematical framework'. The primary-source correction (M0 Sixth Addendum, same day) found Saberi, Saber & "
     "Moessner 2024 (PRB 110, L180102) use the spin configuration arranged as an L×L matrix — a different object from CCA's connected "
     "correlation matrix — so it is NOT direct prior art. That correction was recorded on CCA-1c (calibration row 42) rather than on this "
     "entity; appended here so this entity's own latest status is correct. The reading itself was completed 2026-04-08."),
]


def where(key):
    return " AND ".join(f"{k}=?" for k in key), tuple(key.values())


def plan(cur):
    ops, seen = [], set()
    for label, table, key, col, prefix, pairs, suffix in EDITS:
        target = (table, tuple(sorted(key.items())), col)
        if target in seen:
            raise SystemExit(f"[{label}] ABORT — duplicate target {target}")
        seen.add(target)
        w, args = where(key)
        row = cur.execute(f"SELECT {col} FROM {table} WHERE {w}", args).fetchone()
        if row is None:
            raise SystemExit(f"[{label}] ABORT — row not found {table} {key}")
        current = row[0] or ""
        # Applied markers first: banners quote the original wording, so the
        # find-strings legitimately reappear inside them after apply.
        if prefix or suffix:
            applied = (not prefix or current.startswith(prefix)) and (not suffix or current.endswith(suffix))
        else:  # replace-only edit: applied iff every replacement is present
            applied = bool(pairs) and all(r in current for _, r in pairs)
        if applied:
            print(f"  [{label}] OK — already applied, skipping"); continue
        new = current
        for find, repl in pairs:
            if new.count(find) != 1:
                raise SystemExit(f"[{label}] FAIL — anchor count {new.count(find)}: {find[:70]!r}")
            new = new.replace(find, repl, 1)
        new = prefix + new + suffix
        ops.append((label, table, key, col, new))
        print(f"  [{label}] plan — {len(pairs)} replace(s)" + (" + prefix" if prefix else "") + (" + suffix" if suffix else ""))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    print("=" * 72); print("PHASE 1 — validation / dry run"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); ops = plan(conn.cursor()); conn.close()

    hc = sqlite3.connect(WIKI_HISTORY_DB)
    new_anchors = [x for x in NEW_ANCHORS if not hc.execute(
        "SELECT 1 FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND relationship=?",
        (x[0], x[1], x[2], x[7])).fetchone()]
    note_ops = []
    for aid, sfx in ANCHOR_NOTE_FIXES.items():
        r = hc.execute("SELECT entry_id, notes FROM external_anchors WHERE id=?", (aid,)).fetchone()
        if r is None or r[0] != "C1":
            raise SystemExit(f"[anchor {aid}] ABORT — unexpected row {r!r}")
        if not (r[1] or "").endswith(sfx):
            note_ops.append((aid, (r[1] or "") + sfx))
    cals = [c for c in CALIBRATIONS if not hc.execute(
        "SELECT 1 FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?", (c[0], c[3], c[4])).fetchone()]
    for c in cals:  # only entities with an existing history get a row
        if not hc.execute("SELECT 1 FROM confidence_calibration WHERE entity_id=?", (c[0],)).fetchone():
            raise SystemExit(f"[cal {c[0]}] ABORT — no prior calibration history; refusing to set a first label")
    hc.close()
    print(f"\n  {len(ops)} ds_wiki writes; {len(new_anchors)} anchors; {len(note_ops)} anchor notes; {len(cals)} calibration rows")
    if not a.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply."); return

    print("\n" + "=" * 72); print("PHASE 2 — apply"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    for label, table, key, col, new in ops:
        w, args = where(key)
        cur.execute(f"UPDATE {table} SET {col}=? WHERE {w}", (new, *args))
        if cur.rowcount != 1:
            conn.rollback(); conn.close(); raise SystemExit(f"[{label}] hit {cur.rowcount} rows; rolled back")
    conn.commit(); conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for (eid, src, ident, rev, title, tier, stab, rel, role, conf, notes) in new_anchors:
        hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier,
                      source_stability_class, relationship, canonical_role, verified_date, verified_by_session,
                      confidence, notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (eid, src, ident, rev, title, tier, stab, rel, role, D, AUDIT_REF, conf, notes))
    for aid, new in note_ops:
        hc.execute("UPDATE external_anchors SET notes=? WHERE id=?", (new, aid))
    for c in cals:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date,
                      audit_ref, short_status, rationale) VALUES (?,?,?,?,?,?,?)""", c)
    hc.commit(); hc.close()
    print(f"  wrote {len(ops)} values, {len(new_anchors)} anchors, {len(note_ops)} notes, {len(cals)} calibration rows")

    print("\n" + "=" * 72); print("PHASE 3 — read-back verification"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor(); bad = []
    for label, table, key, col, new in ops:
        w, args = where(key)
        if cur.execute(f"SELECT {col} FROM {table} WHERE {w}", args).fetchone()[0] != new:
            bad.append(label)
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for x in NEW_ANCHORS:
        if not hc.execute("SELECT 1 FROM external_anchors WHERE entry_id=? AND identifier=? AND relationship=?", (x[0], x[2], x[7])).fetchone():
            bad.append(f"anchor:{x[0]}")
    for aid, new in note_ops:
        if hc.execute("SELECT notes FROM external_anchors WHERE id=?", (aid,)).fetchone()[0] != new:
            bad.append(f"note:{aid}")
    for c in CALIBRATIONS:
        if hc.execute("SELECT confidence FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                      (c[0], c[3], c[4])).fetchone() != (c[2],):
            bad.append(f"cal:{c[0]}")
    hc.close()
    if bad:
        raise SystemExit(f"Post-write drift: {bad}")
    print("  all writes verified")


if __name__ == "__main__":
    main()
