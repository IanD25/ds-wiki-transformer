"""
Insert Tier-1 anchor batch CM1 / GV1 / AM5 — 2026-04-18

Second live anchor insertion after INFO1. Anchors drafted in
docs/prior_art_reviews/TIER1_BATCH_CM1_GV1_AM5.md.

Adds 19 anchors across three entries:
  CM1 Newton's Laws of Motion  (6 anchors, 3/5 slots)
  GV1 Einstein Field Equations (7 anchors, 3/5 slots)
  AM5 Noether's Theorem        (6 anchors, 4/5 slots — first comprehensive_survey)

Run: python3 scripts/migrations/insert_tier1_batch_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-tier1-batch-2026-04-18"


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ==========================================================
    # CM1 — Newton's Laws of Motion
    # ==========================================================
    ("CM1", "isbn", "978-0520088177", None,
     "Principia Mathematica (Cohen-Whitman translation, UC Press 1999)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Newton 1687 Philosophiae Naturalis Principia Mathematica. The three "
     "axioms (laws) appear in the opening. Cohen-Whitman 1999 is the "
     "standard modern English edition. ISBN-verified; no fetch."),

    ("CM1", "isbn", "978-0201657029", None,
     "Goldstein, Poole & Safko - Classical Mechanics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Goldstein 2001, standard graduate classical mechanics textbook. "
     "Covers Newton's laws in Ch. 1."),

    ("CM1", "isbn", "978-1891389221", None,
     "Taylor - Classical Mechanics (2005)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Taylor 2005, standard undergraduate classical mechanics textbook."),

    ("CM1", "wikipedia",
     "https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion",
     "1349645204",
     "Newton's laws of motion",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article; verified via WebFetch 2026-04-18. Three laws "
     "presented verbatim from Newton; F = dp/dt emphasized. Revision "
     "pinned; 180d calendar refresh per GSW_ANCHOR_ARCHITECTURE §7."),

    ("CM1", "scholarpedia", "http://www.scholarpedia.org/article/Newton%27s_laws",
     None,
     "Newton's laws (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Scholarpedia article confirmed to exist via WebSearch; direct "
     "WebFetch timed out (consistent Scholarpedia flakiness). Confidence "
     "medium pending re-fetch. Trigger: retry on next session."),

    ("CM1", "mathworld",
     "https://mathworld.wolfram.com/topics/ClassicalMechanics.html",
     None,
     "Classical Mechanics (Wolfram MathWorld portal)",
     2, "canonical", "canonical_authority", "living_reference", "medium",
     "MathWorld treats Newton's laws across several pages under classical "
     "mechanics. No single authoritative page; portal link anchored. "
     "Confidence medium — less canonical a living_reference for this "
     "topic than Wikipedia. Included for completeness."),

    # ==========================================================
    # GV1 — General Relativity / Einstein Field Equations
    # ==========================================================
    ("GV1", "ads", "1915SPAW.......844E", None,
     "Einstein 1915 Die Feldgleichungen der Gravitation (Sitzungsberichte)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Einstein 1915 'Die Feldgleichungen der Gravitation', Sitzungsberichte "
     "der Preussischen Akademie der Wissenschaften zu Berlin, pp. 844-847 "
     "(25 Nov 1915). Predates DOI system; anchored via NASA ADS bibcode. "
     "The paper that introduces G_mu_nu = 8 pi G T_mu_nu."),

    ("GV1", "doi", "10.1002/andp.19163540702", None,
     "Einstein 1916 Die Grundlage der allgemeinen Relativitaetstheorie",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Einstein 1916 'Die Grundlage der allgemeinen Relativitaetstheorie', "
     "Annalen der Physik 354(7), pp. 769-822. Definitive long-form "
     "exposition of general relativity. Verified via CrossRef API."),

    ("GV1", "isbn", "978-0716703440", None,
     "Misner, Thorne, Wheeler - Gravitation (1973)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "MTW 1973, canonical encyclopedic reference for GR."),

    ("GV1", "isbn", "978-0226870335", None,
     "Wald - General Relativity (1984)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Wald 1984, rigorous mathematical treatment. Alternative standard "
     "to MTW."),

    ("GV1", "isbn", "978-0805387322", None,
     "Carroll - Spacetime and Geometry (2004)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Carroll 2004, modern graduate GR standard."),

    ("GV1", "wikipedia",
     "https://en.wikipedia.org/wiki/Einstein_field_equations",
     "1347658026",
     "Einstein field equations",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch. States EFE as G_mu_nu + "
     "Lambda g_mu_nu = kappa T_mu_nu with kappa = 8 pi G / c^4. Full "
     "Einstein 1915/1916 citations present."),

    ("GV1", "scholarpedia",
     "http://www.scholarpedia.org/article/Einstein_field_equations", None,
     "Einstein field equations (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Scholarpedia article; direct WebFetch timed out. Confidence medium "
     "pending retry."),

    # ==========================================================
    # AM5 — Noether's Theorem
    # ==========================================================
    ("AM5", "doi", "10.1080/00411457108231446", None,
     "Noether 1918 - Invariant Variation Problems (Tavel 1971 translation)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Noether 1918 'Invariante Variationsprobleme', Nachr. Koenigl. Ges. "
     "Wiss. Goettingen, Math-Phys. Klasse, pp. 235-257. English "
     "translation by M. A. Tavel 1971, Transport Theory and Statistical "
     "Physics 1(3), 186-207. Verified via CrossRef API. The German "
     "original predates DOIs; this is the canonical English-DOI anchor."),

    ("AM5", "isbn", "978-0201657029", None,
     "Goldstein, Poole & Safko - Classical Mechanics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Goldstein 2001 treats Noether's theorem in Ch. 2/13."),

    ("AM5", "isbn", "978-0387968902", None,
     "Arnold - Mathematical Methods of Classical Mechanics (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Arnold 1989, rigorous symplectic-geometric treatment of Noether's "
     "theorem."),

    ("AM5", "isbn", "978-0387878676", None,
     "Kosmann-Schwarzbach - The Noether Theorems (Springer 2011)",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Kosmann-Schwarzbach 2011 'The Noether Theorems: Invariance and "
     "Conservation Laws in the Twentieth Century'. Definitive scholarly "
     "survey of Noether's work, its reception, and applications. First "
     "anchor to fill the comprehensive_survey slot across all batches."),

    ("AM5", "wikipedia",
     "https://en.wikipedia.org/wiki/Noether%27s_theorem",
     "1348624666",
     "Noether's theorem",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch. First theorem and second "
     "theorem distinguished; Noether 1918 citation present."),

    ("AM5", "scholarpedia",
     "http://www.scholarpedia.org/article/Noether%27s_theorem", None,
     "Noether's theorem (Scholarpedia)",
     1, "canonical", "canonical_authority", "living_reference", "medium",
     "Direct WebFetch timed out. Confidence medium pending retry."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        # Verify all three entries have domain tags already
        for eid in ("CM1", "GV1", "AM5"):
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
        skipped = 0
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

        conn.commit()

        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already existed): {skipped}")

        # Per-entry summary
        for eid in ("CM1", "GV1", "AM5"):
            print(f"\nAnchors for {eid}:")
            for row in cur.execute("""
                SELECT source, canonical_role, confidence, tier
                FROM external_anchors
                WHERE entry_id = ?
                ORDER BY
                  CASE relationship WHEN 'canonical_authority' THEN 1 ELSE 2 END,
                  CASE canonical_role
                    WHEN 'progenitor' THEN 1 WHEN 'axiomatic_foundation' THEN 2
                    WHEN 'standard_textbook' THEN 3 WHEN 'living_reference' THEN 4
                    WHEN 'comprehensive_survey' THEN 5 ELSE 6 END,
                  tier
            """, (eid,)):
                role = row[1] if row[1] else "—"
                print(f"  tier{row[3]} {row[0]:15} / {role:22} ({row[2]})")

        # Totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        )
        entries_anchored = cur.fetchone()[0]
        print(f"\nTotals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries_anchored}")

        # Canonical slot coverage across all anchored entries
        cur.execute("""
            SELECT canonical_role, COUNT(*)
            FROM external_anchors
            WHERE canonical_role IS NOT NULL
            GROUP BY canonical_role
            ORDER BY CASE canonical_role
                WHEN 'progenitor' THEN 1 WHEN 'axiomatic_foundation' THEN 2
                WHEN 'standard_textbook' THEN 3 WHEN 'living_reference' THEN 4
                WHEN 'comprehensive_survey' THEN 5 END
        """)
        print(f"\nCanonical-role anchor counts across all entries:")
        for row in cur.fetchall():
            print(f"  {row[0]:22} {row[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
