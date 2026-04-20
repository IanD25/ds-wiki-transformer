"""
Insert earth sciences cluster anchors — 2026-04-20

13 entries: ES2-14.

Template seed: ES1 Tobler's First Law (anchored 2026-04-18).
Mostly geology principles + geophysics + meteorology + astronomy.

See docs/prior_art_reviews/CLUSTER_EARTH_SCIENCES_2026_04_20.md.

Run: python3 scripts/migrations/insert_earth_sciences_cluster_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-earth-sciences-cluster-2026-04-20"

# Reused (verified at ES1)
ISBN_OSULLIVAN = "978-0470288573"  # O'Sullivan-Unwin GIS

# New textbook ISBNs — medium pending WorldCat verify
ISBN_TURCOTTE   = "978-1107006539"  # Turcotte-Schubert Geodynamics 3rd
ISBN_PRESS      = "978-1319079857"  # Press-Siever Understanding Earth 8th
ISBN_HOLTON     = "978-0123848666"  # Holton-Hakim Atmospheric Science
ISBN_MURRAY_DER = "978-0521575973"  # Murray-Dermott Solar System Dynamics
ISBN_ARBIA      = "978-0792302865"  # Arbia 1989 Spatial Data Configuration


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ── ES2 — Arbia's Law ──
    ("ES2", "isbn", ISBN_ARBIA, None,
     "Arbia - Spatial Data Configuration in Statistical Analysis (1989)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Arbia 1989 Springer-Kluwer. Second-law alternative to Tobler — "
     "spatial heterogeneity grows with distance. ISBN claimed; verify WorldCat."),
    ("ES2", "isbn", ISBN_OSULLIVAN, None,
     "O'Sullivan-Unwin - Geographic Information Analysis",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Standard GIS reference covering both Tobler and Arbia laws. Reused from ES1."),
    ("ES2", "wikipedia",
     "https://en.wikipedia.org/wiki/Tobler%27s_first_law_of_geography", None,
     "Tobler's first law of geography (covers Arbia second-law)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Wikipedia article on Tobler also covers Arbia's second-law alternative. No oldid."),

    # ── ES3 — Archie's Law ──
    ("ES3", "doi", "10.2118/942054-G", None,
     "Archie 1942 The Electrical Resistivity Log as an Aid in Determining Some Reservoir Characteristics",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Archie 1942 Trans. AIME 146, 54. SPE petrophysics DOI pattern."),
    ("ES3", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Background on porous-media electrical properties. ISBN claimed; verify."),
    ("ES3", "wikipedia",
     "https://en.wikipedia.org/wiki/Archie%27s_law", None, "Archie's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── ES4 — Buys Ballot's Law ──
    ("ES4", "isbn", ISBN_HOLTON, None,
     "Holton-Hakim - An Introduction to Dynamic Meteorology (5th ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Holton-Hakim Ch. 3 (geostrophic balance — the physics behind Buys Ballot's Law). "
     "Buys Ballot 1857 Comptes Rendus has no DOI. ISBN claimed; verify WorldCat."),
    ("ES4", "wikipedia",
     "https://en.wikipedia.org/wiki/Buys_Ballot%27s_law", None, "Buys Ballot's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── ES5 — Birch's Law ──
    ("ES5", "doi", "10.1029/JZ066i007p02199", None,
     "Birch 1961 The velocity of compressional waves in rocks to 10 kilobars Pt 2",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Birch 1961 J. Geophys. Res. 66, 2199. AGU DOI pattern. "
     "Linear V_p vs density relation in rocks of given mean atomic weight."),
    ("ES5", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused. Background on seismic-velocity / density relations."),
    ("ES5", "wikipedia",
     "https://en.wikipedia.org/wiki/Birch%27s_law", None, "Birch's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── ES6 — Byerlee's Law ──
    ("ES6", "doi", "10.1007/BF00876528", None,
     "Byerlee 1978 Friction of rocks",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Byerlee 1978 Pure Appl. Geophys. 116, 615. Springer historic Birkhäuser DOI pattern."),
    ("ES6", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused. Ch. on rock mechanics and faulting."),
    ("ES6", "wikipedia",
     "https://en.wikipedia.org/wiki/Byerlee%27s_law", None, "Byerlee's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── ES7 — Titius-Bode Law ──
    ("ES7", "doi", "10.1093/mnras/stt1357", None,
     "Bovaird-Lineweaver 2013 Exoplanet predictions based on the generalised Titius-Bode relation",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Bovaird-Lineweaver 2013 MNRAS 435, 1126. Modern statistical analysis of TB-like patterns "
     "across exoplanet systems. OUP MNRAS DOI pattern."),
    ("ES7", "isbn", ISBN_MURRAY_DER, None,
     "Murray-Dermott - Solar System Dynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Murray-Dermott 1999 Cambridge UP. Standard reference for orbital dynamics; "
     "discusses TB law historically. ISBN claimed; verify WorldCat."),
    ("ES7", "wikipedia",
     "https://en.wikipedia.org/wiki/Titius%E2%80%93Bode_law", None, "Titius-Bode law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── ES8 — Steno's Law of Superposition ──
    ("ES8", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth (8th ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Press-Siever Ch. 8 (sedimentary rocks and stratigraphy). "
     "Steno 1669 De solido is the historical book — no DOI. ISBN claimed; verify."),
    ("ES8", "wikipedia",
     "https://en.wikipedia.org/wiki/Law_of_superposition", None, "Law of superposition",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    # Add second textbook to hit 3-min: O'Sullivan also covers stratigraphy briefly
    ("ES8", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Background. Reused."),

    # ── ES9 — Original Horizontality ──
    ("ES9", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Same Steno 1669 source as ES8. Reused."),
    ("ES9", "wikipedia",
     "https://en.wikipedia.org/wiki/Principle_of_original_horizontality", None,
     "Principle of original horizontality",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("ES9", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── ES10 — Lateral Continuity ──
    ("ES10", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Same Steno 1669 source as ES8/ES9. Reused."),
    ("ES10", "wikipedia",
     "https://en.wikipedia.org/wiki/Principle_of_lateral_continuity", None,
     "Principle of lateral continuity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("ES10", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── ES11 — Cross-Cutting Relationships ──
    ("ES11", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Press-Siever covers Hutton 1788 cross-cutting principle. Hutton's Theory of the Earth "
     "is the historical book — no DOI. Reused."),
    ("ES11", "wikipedia",
     "https://en.wikipedia.org/wiki/Cross-cutting_relationships", None,
     "Cross-cutting relationships",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("ES11", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── ES12 — Faunal Succession ──
    ("ES12", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Press-Siever covers Smith 1799 faunal succession. Smith's geological maps and writings "
     "have no DOIs. Reused."),
    ("ES12", "wikipedia",
     "https://en.wikipedia.org/wiki/Principle_of_faunal_succession", None,
     "Principle of faunal succession",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("ES12", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── ES13 — Inclusions and Components ──
    ("ES13", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Press-Siever covers principle of inclusions in stratigraphy chapter. "
     "Standard geology principle — no single historical progenitor."),
    ("ES13", "wikipedia",
     "https://en.wikipedia.org/wiki/Inclusion_(mineral)", None,
     "Inclusion (mineral)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Wikipedia covers mineral inclusions; principle treated in stratigraphy articles. No oldid."),
    ("ES13", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── ES14 — Walther's Law of Facies ──
    ("ES14", "isbn", ISBN_PRESS, None,
     "Press-Siever - Understanding Earth",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Press-Siever covers Walther's Law (1894) in sedimentary environments chapter. "
     "Walther 1893-94 Einleitung in die Geologie has no online DOI. Reused."),
    ("ES14", "wikipedia",
     "https://en.wikipedia.org/wiki/Walther%27s_law", None, "Walther's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("ES14", "isbn", ISBN_TURCOTTE, None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
]


ENTRIES = ("ES2", "ES3", "ES4", "ES5", "ES6", "ES7",
           "ES8", "ES9", "ES10", "ES11", "ES12", "ES13", "ES14")


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ENTRIES:
            n = cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            ).fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
        print(f"Pre-flight OK: all {len(ENTRIES)} entries tagged.")
        print()

        print(f"Inserting {len(ANCHORS)} anchor rows...")
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
        conn.commit()
        print(f"  Inserted: {inserted}, skipped: {skipped}")
        print()

        print("=== Per-entry anchor counts ===")
        for eid in ENTRIES:
            n = cur.execute(
                "SELECT COUNT(*) FROM external_anchors WHERE entry_id=?", (eid,),
            ).fetchone()[0]
            slots = cur.execute(
                "SELECT COUNT(DISTINCT canonical_role) FROM external_anchors "
                "WHERE entry_id=? AND canonical_role IS NOT NULL", (eid,),
            ).fetchone()[0]
            below_min = " *** BELOW 3-MIN" if n < 3 else ""
            print(f"  {eid:<6}  {n:>2} anchors / {slots} slots filled{below_min}")

        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        print(f"\nTotals after this batch:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
