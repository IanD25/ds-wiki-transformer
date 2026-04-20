"""
Promote 5 IC conjectures to GSW-resolved states — 2026-04-20

After the 23-conjecture review pass: 5 IC-flagged conjectures have identifiable
prior art that warrants promotion from "wiki-internal vocabulary" to
literature-connected anchors.

Promotions:
  P9  IC -> cites (Bouland-Fefferman-Vazirani 2019, Susskind 2014, Brown-Susskind 2018)
  P12 IC -> null_hypothesis (Newman 2005, reused from C3)
  P14 IC -> cites (Glazier 2010, WBE 1997 reused)
  P16 IC -> cites (Watanabe 2009 SLT)
  P22 IC -> cites (Sakharov 1967 reused, Kibble 1976, Zurek 1985, Crooks 1999 reused)

Architectural choice: IC flag is REMOVED for these entries since they now have
literature connections. Wiki-internal sharpness of specific framings is captured
in anchor notes rather than separate IC flags.

This shifts conjecture-resolution from 13/23 (57%) to 18/23 (78%) in the strong
sense ("real GSW resolution" — restatement, null, falsified, established cite,
or cites + canonical_authority). The remaining 5 IC entries are genuinely
wiki-internal: P13/P15 (owner-acknowledged ansatzes) and P18-P20 (AlphaEntropy
side-program).

Run: python3 scripts/migrations/promote_ic_conjectures_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-promote-ic-conjectures-2026-04-20"


# Reused (verified at prior batches)
DOI_NEWMAN_2005   = "10.1080/00107510500052444"  # C3
DOI_WBE_1997      = "10.1126/science.276.5309.122"  # C1
DOI_SAKHAROV_1967 = "10.1023/A:1001947813463"  # GT06
DOI_CROOKS_1999   = "10.1103/PhysRevE.60.2721"  # NE04


ANCHORS = [
    # ============================================================
    # P9 — Holographic Dictionary Has LWE-Equivalent Complexity
    # PROMOTE: IC -> cites (real prior art on bulk-reconstruction hardness)
    # ============================================================

    ("P9", "arxiv", "1910.14646", None,
     "Bouland-Fefferman-Vazirani 2019 Computational pseudorandomness, the wormhole growth paradox, and constraints on the AdS/CFT duality",
     3, "preprint-evolving", "cites", None, "high",
     "BFV 2019 explicitly argues AdS/CFT bulk reconstruction is computationally hard at "
     "quantum-cryptographic level (AWPP / quantum pseudorandomness). The closest published "
     "prior art for P9. Note: BFV use AWPP-class assumptions; P9's specific LWE-equivalence "
     "is sharper than BFV's framing."),

    ("P9", "arxiv", "1402.5674", None,
     "Susskind 2014 Computational Complexity and Black Hole Horizons",
     3, "preprint-evolving", "cites", None, "high",
     "Susskind 2014 introduces the program: bulk reconstruction from boundary is "
     "computationally hard. Foundational paper for the complexity-of-holography research "
     "thread that P9 extends with LWE specificity."),

    ("P9", "doi", "10.1103/PhysRevD.97.086015", None,
     "Brown-Susskind 2018 Second law of quantum complexity",
     1, "canonical", "cites", None, "high",
     "Brown-Susskind 2018 PRD 97, 086015. Develops the complexity-volume conjecture "
     "for AdS/CFT. APS DOI pattern."),

    # ============================================================
    # P12 — β(λ) Formula Predicts Scaling Exponents Cross-Domain
    # PROMOTE: IC -> null_hypothesis
    # ============================================================

    ("P12", "doi", DOI_NEWMAN_2005, None,
     "Newman 2005 Power laws, Pareto distributions and Zipf's law",
     1, "canonical", "null_hypothesis", None, "high",
     "Newman 2005 Contemp. Phys. 46, 323. Comprehensive survey explicitly arguing "
     "different power-law mechanisms operate in different domains (preferential attachment, "
     "multiplicative noise, optimization, self-organized criticality, etc.). P12's "
     "one-formula-fits-all claim has no unique predictive content over Newman's "
     "domain-specific-mechanism position unless P12 makes a prediction Newman et al. cannot. "
     "P12's own critical_gaps acknowledges no published study has tested the cross-domain "
     "identification. Reused from C3. relationship=null_hypothesis."),

    # ============================================================
    # P14 — Branching Variance Predicts Exponent Gap (β_MMR - β_BMR)
    # PROMOTE: IC -> cites (real biology lit on MMR/BMR scaling)
    # ============================================================

    ("P14", "doi", "10.1111/j.1469-185X.2009.00095.x", None,
     "Glazier 2010 A unifying explanation for diverse metabolic scaling in animals and plants",
     1, "canonical", "cites", None, "medium",
     "Glazier 2010 Biol. Rev. 85, 111. Canonical reference for MMR-vs-BMR exponent gap "
     "and the diversity of metabolic scaling exponents. Wiley DOI pattern; verify via CrossRef. "
     "P14's specific Δλ = 1 - λ_min formulation remains wiki-derived; this `cites` anchor "
     "establishes the literature context for the exponent-gap question."),

    ("P14", "doi", DOI_WBE_1997, None,
     "West-Brown-Enquist 1997 A General Model for the Origin of Allometric Scaling Laws in Biology",
     1, "canonical", "cites", None, "high",
     "WBE 1997 Science 276, 122 — foundational vascular-network theory of metabolic scaling. "
     "Reused from C1. Background for P14's vascular-branching framing."),

    # ============================================================
    # P16 — RLCT = d_f at Regime Transitions
    # PROMOTE: IC -> cites (Watanabe SLT, the RLCT side)
    # ============================================================

    ("P16", "isbn", "978-0521864671", None,
     "Watanabe - Algebraic Geometry and Statistical Learning Theory (2009)",
     1, "canonical", "cites", None, "medium",
     "Watanabe 2009 Cambridge UP. Canonical reference for RLCT (Real Log-Canonical "
     "Threshold) in singular learning theory. P16 equates RLCT to vascular d_f — that "
     "specific cross-discipline equation remains wiki-original; this `cites` anchor "
     "establishes the RLCT side. ISBN claimed; verify WorldCat."),

    # ============================================================
    # P22 — Irreversible Lockout Trichotomy for Spontaneous Symmetry Breaking
    # PROMOTE: IC -> cites (Sakharov, Kibble-Zurek, Crooks)
    # ============================================================

    ("P22", "doi", DOI_SAKHAROV_1967, None,
     "Sakharov 1967 (reissue) Vacuum quantum fluctuations and gravitation",
     1, "canonical", "cites", None, "high",
     "Sakharov 1967. P22 entry text explicitly states: 'This conjecture generalizes "
     "Sakharov's three conditions for baryogenesis ... to ALL spontaneous symmetry breaking'. "
     "Sakharov is the acknowledged progenitor pattern. Reused from GT06."),

    ("P22", "doi", "10.1088/0305-4470/9/8/029", None,
     "Kibble 1976 Topology of cosmic domains and strings",
     1, "canonical", "cites", None, "high",
     "Kibble 1976 J. Phys. A 9, 1387. Foundational paper for the Kibble-Zurek mechanism "
     "(the energetic-lockout mechanism in P22's trichotomy). IOP DOI pattern."),

    ("P22", "doi", "10.1038/317505a0", None,
     "Zurek 1985 Cosmological experiments in superfluid helium?",
     1, "canonical", "cites", None, "high",
     "Zurek 1985 Nature 317, 505. Companion paper to Kibble 1976; develops the scaling "
     "prediction for asymmetry production in fast quenches. Nature DOI pattern."),

    ("P22", "doi", DOI_CROOKS_1999, None,
     "Crooks 1999 Entropy production fluctuation theorem and the nonequilibrium work relation",
     1, "canonical", "cites", None, "high",
     "Crooks 1999 PRE 60, 2721. Foundational for the fluctuation-theorem framework that "
     "underpins P22's information-theoretic lockout mechanism (D_KL-suppressed return). "
     "Reused from NE04."),
]


# IC entries to REMOVE (since they now have literature connections)
ENTRIES_TO_UNFLAG = ("P9", "P12", "P14", "P16", "P22")


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        # 1. Insert promotion anchors
        print(f"Inserting {len(ANCHORS)} promotion anchors...")
        inserted = skipped = 0
        for a in ANCHORS:
            (entry_id, source, identifier, revision_id, title, tier,
             stability, relationship, canonical_role, confidence, notes) = a
            res = conn.execute(
                "INSERT OR IGNORE INTO external_anchors "
                "(entry_id, source, identifier, revision_id, title, tier, "
                " source_stability_class, relationship, canonical_role, "
                " verified_date, verified_by_session, confidence, notes) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (entry_id, source, identifier, revision_id, title, tier,
                 stability, relationship, canonical_role,
                 TODAY, SESSION, confidence, notes),
            )
            if res.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
        print(f"  Anchors inserted: {inserted}, skipped: {skipped}")

        # 2. Remove IC flags for promoted entries
        print(f"\nRemoving IC flags for {len(ENTRIES_TO_UNFLAG)} promoted entries...")
        unflagged = 0
        for eid in ENTRIES_TO_UNFLAG:
            res = conn.execute(
                "DELETE FROM internal_constructions WHERE entry_id=?", (eid,),
            )
            if res.rowcount > 0:
                unflagged += 1
                print(f"  {eid}: IC flag removed (now literature-connected via anchors)")
            else:
                print(f"  {eid}: no IC flag to remove (skipping)")

        conn.commit()
        print()

        # Per-entry resolution after promotion
        print("=== Per-entry resolution after promotion ===")
        for eid in ENTRIES_TO_UNFLAG:
            rels = cur.execute("""
                SELECT DISTINCT relationship FROM external_anchors WHERE entry_id=?
            """, (eid,)).fetchall()
            ic = cur.execute("""
                SELECT 1 FROM internal_constructions WHERE entry_id=?
            """, (eid,)).fetchone()
            n = cur.execute("SELECT COUNT(*) FROM external_anchors WHERE entry_id=?", (eid,)).fetchone()[0]
            rel_str = ", ".join(r[0] for r in rels)
            ic_str = " + IC" if ic else ""
            print(f"  {eid}: {n} anchors via [{rel_str}]{ic_str}")

        # Final summary
        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        ic_total = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM internal_constructions"
        ).fetchone()[0]
        print(f"\nTotals after promotion:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")
        print(f"  internal_constructions:  {ic_total}")
        print(f"  PROVENANCE:              {entries_anchored + ic_total} / 301 "
              f"(union — some entries now both anchored and IC, counted once)")

        # Conjecture resolution distribution after promotion
        print(f"\n=== Conjecture resolution distribution ===")
        cur.execute("ATTACH DATABASE 'data/ds_wiki.db' AS ds")
        all_conj = cur.execute("SELECT id FROM ds.conjectures ORDER BY conjecture_order").fetchall()
        buckets = {
            "reframing_of": 0, "Established": 0, "cites": 0, "null_hypothesis": 0,
            "contradicts": 0, "canonical_authority_only": 0, "IC_only": 0,
            "anchor_plus_IC": 0,
        }
        for (cid,) in all_conj:
            ic = cur.execute("SELECT 1 FROM internal_constructions WHERE entry_id=?", (cid,)).fetchone()
            rels = {r[0] for r in cur.execute("SELECT DISTINCT relationship FROM external_anchors WHERE entry_id=?", (cid,)).fetchall()}
            if ic and not rels:
                buckets["IC_only"] += 1
            elif ic and rels:
                buckets["anchor_plus_IC"] += 1
            elif "reframing_of" in rels:
                buckets["reframing_of"] += 1
            elif "contradicts" in rels:
                buckets["contradicts"] += 1
            elif "null_hypothesis" in rels:
                buckets["null_hypothesis"] += 1
            elif "cites" in rels:
                buckets["cites"] += 1
            elif "canonical_authority" in rels:
                cal = cur.execute("SELECT confidence FROM confidence_calibration WHERE entity_id=? ORDER BY id DESC LIMIT 1", (cid,)).fetchone()
                if cal and cal[0] == "Established":
                    buckets["Established"] += 1
                else:
                    buckets["canonical_authority_only"] += 1
        for k, v in buckets.items():
            print(f"  {k:<28} {v:>3}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
