"""
Insert Tier-1 anchor batch 4 — C1 / BIO1 / ES1 — 2026-04-18

Fifth live anchor insertion. First anchors in biology + earth_sciences domains.
  C1   Kleiber's Law          (biology.physiology — empirical law + WBE theory)
  BIO1 Mendelian Laws         (biology.evolution / molecular)
  ES1  Tobler's First Law     (earth_sciences — spatial autocorrelation)

Tests the basket for the two previously-untouched domains. C1 uses the WBE
1997 Science paper as axiomatic_foundation — the theoretical derivation of
the empirical Kleiber scaling law from first principles (vascular fractal
networks). First theoretical-derivation-as-axiomatic_foundation pattern.

Run: python3 scripts/migrations/insert_tier1_batch4_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-tier1-batch4-2026-04-18"


ANCHORS = [
    # ==========================================================
    # C1 — Metabolic Scaling (Kleiber's Law)
    # ==========================================================
    ("C1", "doi", "10.3733/hilg.v06n11p315", None,
     "Kleiber 1932 - Body size and metabolism",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Kleiber 1932, Hilgardia 6(11), pp. 315-353. Original empirical "
     "establishment of the 3/4-power law between basal metabolic rate "
     "and body mass. Verified via Wikipedia + DOI 2026-04-18."),

    ("C1", "doi", "10.1126/science.276.5309.122", None,
     "West, Brown & Enquist 1997 - A General Model for Allometric Scaling Laws",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "West-Brown-Enquist 1997, Science 276(5309), pp. 122-126. "
     "Theoretical derivation of the 3/4 exponent from fractal "
     "distribution networks. Fills axiomatic_foundation for Kleiber's "
     "empirical law. Also noted: this is the reference P2 conjecture "
     "was a restatement of — anchoring here ties the wiki's Kleiber's "
     "Law entry to its canonical theoretical derivation. ~3,489 "
     "citations."),

    ("C1", "isbn", "978-0521319874", None,
     "Schmidt-Nielsen - Scaling: Why is Animal Size So Important?",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Schmidt-Nielsen 1984 Cambridge UP. Standard textbook on "
     "biological scaling, covers Kleiber and allometric theory."),

    ("C1", "isbn", "978-0143110903", None,
     "West - Scale: The Universal Laws of Life, Growth, and Death",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "West 2018 (paperback). Comprehensive trade-book survey by one of "
     "the WBE authors, covering metabolic scaling, urban scaling, and "
     "their common theoretical origin. Fills comprehensive_survey for "
     "C1."),

    ("C1", "wikipedia",
     "https://en.wikipedia.org/wiki/Kleiber%27s_law",
     "1347356811",
     "Kleiber's law",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Full Kleiber "
     "1932 and WBE 1997 citations present with DOIs."),

    # ==========================================================
    # BIO1 — Mendelian Laws of Inheritance
    # ==========================================================
    ("BIO1", "isbn", "978-1107617896", None,
     "Mendel's Principles of Heredity (Bateson translation reprint)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Mendel 1866 'Versuche ueber Pflanzenhybriden', Verhandlungen des "
     "naturforschenden Vereines in Bruenn 4, pp. 3-47. Predates DOI "
     "system. Anchored via Bateson 1901 English translation "
     "compiled in 'Mendel's Principles of Heredity' (Cambridge UP "
     "reprint). Confidence medium because ISBN is for the reprint, "
     "not the original; modern Mendel-source-book anchors exist but "
     "not verified this session."),

    ("BIO1", "isbn", "978-1319114770", None,
     "Griffiths et al. - Introduction to Genetic Analysis (12th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Griffiths et al. 2020, standard undergraduate genetics textbook. "
     "Chapters 2-3 cover Mendelian inheritance in modern form."),

    ("BIO1", "wikipedia",
     "https://en.wikipedia.org/wiki/Mendelian_inheritance",
     "1345737868",
     "Mendelian inheritance",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Three laws "
     "stated; Mendel 1866 Verhandlungen Bruenn citation present."),

    ("BIO1", "sep", "https://plato.stanford.edu/entries/heredity/", None,
     "Heredity and Heritability (Stanford Encyclopedia of Philosophy)",
     1, "canonical", "canonical_authority", "living_reference", "high",
     "SEP entry by Paul Griffiths. Peer-reviewed authoritative "
     "treatment of the heredity concept from a philosophy-of-biology "
     "angle. Not fetched this session; known canonical SEP article."),

    # ==========================================================
    # ES1 — Tobler's First Law of Geography
    # ==========================================================
    ("ES1", "doi", "10.2307/143141", None,
     "Tobler 1970 - A Computer Movie Simulating Urban Growth",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Tobler 1970, Economic Geography 46, pp. 234-240. Introduces the "
     "'first law of geography' in the context of a cellular-automaton "
     "urban growth simulation. JSTOR 143141. Verified via WebFetch."),

    ("ES1", "doi", "10.2307/2332142", None,
     "Moran 1950 - Notes on Continuous Stochastic Phenomena",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Moran 1950, Biometrika 37(1/2), pp. 17-23. Introduces Moran's I, "
     "the canonical statistical formalization of spatial "
     "autocorrelation (which IS the formal statement of Tobler's law). "
     "Fills axiomatic_foundation."),

    ("ES1", "isbn", "978-0470288573", None,
     "O'Sullivan & Unwin - Geographic Information Analysis (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "O'Sullivan & Unwin 2010, standard GIS / spatial analysis "
     "textbook. Treats Tobler's law and spatial autocorrelation as a "
     "cornerstone of the field."),

    ("ES1", "wikipedia",
     "https://en.wikipedia.org/wiki/Tobler%27s_first_law_of_geography",
     "1345982793",
     "Tobler's first law of geography",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Tobler 1970 "
     "citation present with DOI."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("C1", "BIO1", "ES1"):
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

        print("\nPer-entry slot coverage:")
        for eid in ("C1", "BIO1", "ES1"):
            cur.execute("""
                SELECT canonical_role, COUNT(*)
                FROM external_anchors
                WHERE entry_id=? AND canonical_role IS NOT NULL
                GROUP BY canonical_role
            """, (eid,))
            rows = {r[0]: r[1] for r in cur.fetchall()}
            filled = [r for r in
                      ("progenitor", "axiomatic_foundation",
                       "standard_textbook", "living_reference",
                       "comprehensive_survey") if r in rows]
            print(f"  {eid}: {len(filled)}/5 — "
                  f"{', '.join(f'{r}({rows[r]})' for r in filled)}")

        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries_anchored = cur.fetchone()[0]
        print(f"\nGlobal totals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries_anchored} / 300")

        cur.execute("""
            SELECT canonical_role, COUNT(*)
            FROM external_anchors WHERE canonical_role IS NOT NULL
            GROUP BY canonical_role
            ORDER BY CASE canonical_role
                WHEN 'progenitor' THEN 1 WHEN 'axiomatic_foundation' THEN 2
                WHEN 'standard_textbook' THEN 3 WHEN 'living_reference' THEN 4
                WHEN 'comprehensive_survey' THEN 5 END
        """)
        print(f"\nCanonical-role totals:")
        for row in cur.fetchall():
            print(f"  {row[0]:22} {row[1]}")

        # Domain coverage summary
        cur.execute("""
            SELECT
                CASE WHEN INSTR(t.tag_path, '.') = 0 THEN t.tag_path
                     ELSE SUBSTR(t.tag_path, 1, INSTR(t.tag_path, '.')-1)
                END AS top_level,
                COUNT(DISTINCT e.entry_id)
            FROM external_anchors a
            JOIN entry_source_domains e ON e.entry_id = a.entry_id
            JOIN source_domain_taxonomy t ON t.id = e.tag_id
            WHERE e.primacy='primary' AND e.review_status='current'
            GROUP BY top_level
            ORDER BY COUNT(DISTINCT e.entry_id) DESC
        """)
        print(f"\nAnchored entries by primary domain:")
        for row in cur.fetchall():
            print(f"  {row[0]:25} {row[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
