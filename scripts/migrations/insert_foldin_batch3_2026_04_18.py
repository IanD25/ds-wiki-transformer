"""
Insert Fold-In Batch 3 — P1 / P3 / P4 — 2026-04-18

Third and final fold-in batch — closes out the 9 fold-in conjectures from
the M0 audit plan. All three use the null_hypothesis pattern (P10-style)
because they are heterodox claims without unique predictions rather than
restatements of existing work.

  P1 Cosmological Redshift as Dim Gradient   → null_hypothesis ΛCDM / Hubble 1929
  P3 Single Ω_D Governs G, ℏ, m              → null_hypothesis std model / Adelberger
  P4 CcO 1.5ms as Thermodynamic Refresh Rate → null_hypothesis std enzyme kinetics

After this batch, the 9 fold-ins identified in the M0 audit are all
anchored. 4 use reframing_of (P2, P5, P8, P11 — genuine restatements).
5 use null_hypothesis (P1, P3, P4, P10, and the original P5 has both
reframing_of AND cites). P21 is Established with canonical_authority.

Run: python3 scripts/migrations/insert_foldin_batch3_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-foldin-batch3-2026-04-18"


ANCHORS = [
    # ==========================================================
    # P1 — Cosmological Redshift as Dimensional Gradient
    #      NULL HYPOTHESIS → standard ΛCDM metric expansion
    # ==========================================================
    ("P1", "doi", "10.1073/pnas.15.3.168", None,
     "Hubble 1929 - A relation between distance and radial velocity",
     1, "canonical", "null_hypothesis", None, "high",
     "Hubble 1929, PNAS 15(3), pp. 168-173. Empirical redshift-"
     "distance relation, interpreted within the metric-expansion "
     "framework. P1 proposes a dimensional-gradient alternative; the "
     "null hypothesis is standard Hubble-Lemaître-ΛCDM. Per M0 audit: "
     "P1 is 'heterodox cosmology, no independent support'. Verified "
     "via CrossRef 2026-04-18."),

    ("P1", "doi", "10.1051/0004-6361/201833910", None,
     "Planck Collaboration 2020 - Planck 2018 results VI. Cosmological parameters",
     1, "canonical", "null_hypothesis", None, "high",
     "Planck Collaboration 2020, A&A 641, A6. Definitive modern "
     "constraints on ΛCDM parameters: H₀ = 67.4 ± 0.5 km/s/Mpc, "
     "Ω_m = 0.315 ± 0.007. The null-hypothesis cosmology P1 would "
     "need to distinguish itself from. Note: paper itself reports "
     "3.6σ tension with local H₀ measurements — the Hubble tension "
     "is real but has multiple proposed explanations; P1's "
     "dimensional-gradient explanation is only one of many."),

    # ==========================================================
    # P3 — Single Ω_D Governs G, ℏ, m
    #      NULL HYPOTHESIS → standard physics: independent running
    # ==========================================================
    ("P3", "doi", "10.1146/annurev.nucl.53.041002.110503", None,
     "Adelberger, Heckel, Nelson 2003 - Tests of the Gravitational Inverse-Square Law",
     1, "canonical", "null_hypothesis", None, "high",
     "Adelberger-Heckel-Nelson 2003, Annu. Rev. Nucl. Part. Sci. 53, "
     "pp. 77-121. Definitive review of precision tests of Newton's "
     "G: no deviation from 1/r² observed down to ~100 μm. Serves as "
     "null_hypothesis anchor for P3's claim that G runs with D_eff: "
     "the data do not currently show such running. Per M0 audit: P3 "
     "has 'three λ exponents, formal audit not performed' (pattern: "
     "over-parameterized-unification)."),

    ("P3", "isbn", "978-0201503975", None,
     "Peskin & Schroeder - Intro to Quantum Field Theory",
     1, "canonical", "null_hypothesis", None, "medium",
     "Peskin-Schroeder 1995 Westview. Standard QFT textbook: ℏ is "
     "constant (dimensional by definition post-2019 SI redefinition); "
     "masses arise from Higgs mechanism + QCD confinement. No common "
     "'Ω_D' operator governs all three. Cross-entry reuse with P10 "
     "(null_hypothesis) — this textbook serves as the standard-model "
     "null for both heterodox-physics conjectures."),

    # ==========================================================
    # P4 — CcO 1.5ms Timescale as Thermodynamic Refresh Rate
    #      NULL HYPOTHESIS → standard enzyme kinetics
    # ==========================================================
    ("P4", "isbn", "978-1319228002", None,
     "Lehninger Principles of Biochemistry (8th ed., Nelson & Cox)",
     1, "canonical", "null_hypothesis", None, "high",
     "Nelson & Cox 2021, 8th edition. Standard graduate biochemistry "
     "textbook. Treats cytochrome c oxidase (CcO) kinetics within "
     "Michaelis-Menten framework; the 1.5ms cycle time is explained "
     "as a kinetic speed limit determined by rate-limiting electron "
     "transfer and proton pumping steps. Null hypothesis for P4's "
     "thermodynamic-refresh-rate reinterpretation."),

    ("P4", "wikipedia",
     "https://en.wikipedia.org/wiki/Cytochrome_c_oxidase", None,
     "Cytochrome c oxidase (Wikipedia)",
     2, "active-literature", "adjacent_concept", None, "medium",
     "Wikipedia article on CcO structure, mechanism, and kinetics. "
     "Standard biochemical framing; no mention of thermodynamic "
     "refresh rate interpretation. oldid not fetched this session "
     "(not central to the null_hypothesis anchor). Included as "
     "adjacent_concept for context."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("P1", "P3", "P4"):
            cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            )
            n = cur.fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
            print(f"{eid} has {n} domain-tag rows.")

        print()
        print(f"Inserting {len(ANCHORS)} anchor rows...")
        inserted = 0
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
            inserted += res.rowcount
        conn.commit()
        print(f"  Inserted: {inserted}")

        print("\nPer-conjecture anchor summary:")
        for eid in ("P1", "P3", "P4"):
            cur.execute("""
                SELECT relationship, canonical_role, COUNT(*)
                FROM external_anchors WHERE entry_id=?
                GROUP BY relationship, canonical_role
            """, (eid,))
            rels = cur.fetchall()
            rel_str = ", ".join(
                f"{r[0]}{'/' + r[1] if r[1] else ''}({r[2]})"
                for r in rels
            )
            print(f"  {eid}: {rel_str}")

        # Complete fold-in coverage audit
        print("\n=== Fold-in coverage (9 original targets) ===")
        foldins = [("P1", "null_hypothesis"), ("P2", "reframing_of"),
                   ("P3", "null_hypothesis"), ("P4", "null_hypothesis"),
                   ("P5", "reframing_of"), ("P8", "reframing_of"),
                   ("P10", "null_hypothesis"), ("P11", "reframing_of"),
                   ("P21", "canonical_authority")]
        for eid, expected_rel in foldins:
            cur.execute(
                "SELECT COUNT(*) FROM external_anchors "
                "WHERE entry_id=? AND relationship=?",
                (eid, expected_rel),
            )
            n = cur.fetchone()[0]
            status = "✓" if n > 0 else "✗"
            print(f"  {status} {eid:4} → {expected_rel:22} ({n} anchor{'s' if n!=1 else ''})")

        # Full relationship distribution
        print("\n=== Final relationship-type distribution (all anchors) ===")
        for r in cur.execute("""
            SELECT relationship, COUNT(*) FROM external_anchors
            GROUP BY relationship ORDER BY COUNT(*) DESC
        """):
            print(f"  {r[0]:25} {r[1]}")

        # Global totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries = cur.fetchone()[0]
        cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors "
            "WHERE relationship IN ('reframing_of', 'null_hypothesis')"
        )
        folded = cur.fetchone()[0]
        print(f"\nGlobal totals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries} / 300")
        print(f"  entries folded in (reframing_of or null_hypothesis): {folded}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
