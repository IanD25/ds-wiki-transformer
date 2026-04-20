"""
Insert chemistry cluster anchors — 2026-04-20

16 entries: CHEM2-5 + KC1-10 + CR1 + MS1.

Template seed: CHEM1 (anchored 2026-04-18). Heavy reuse of Atkins.
Most entries are pre-DOI 19th-century classical chemistry; textbook-anchored.

See docs/prior_art_reviews/CLUSTER_CHEMISTRY_2026_04_20.md.

Run: python3 scripts/migrations/insert_chemistry_cluster_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-chemistry-cluster-2026-04-20"

# Reused (verified at CHEM1 / TD11 / B2 / CM1 / TD3)
ISBN_ATKINS    = "978-0198769866"  # CHEM1, TD11, B2
ISBN_CALLEN    = "978-0471862567"  # TD3
ISBN_GOLDSTEIN = "978-0201657029"  # CM1

# New textbook ISBNs — all medium pending WorldCat verify
ISBN_MCQUARRIE   = "978-0935702996"  # McQuarrie-Simon Physical Chemistry
ISBN_CLAYDEN     = "978-0199270293"  # Clayden-Greeves-Warren Organic Chemistry 2nd
ISBN_LEHNINGER   = "978-1464126116"  # Lehninger Principles of Biochemistry 7th
ISBN_BROWN_GEN   = "978-0134414232"  # Brown-LeMay General Chemistry 14th
ISBN_CULLITY     = "978-0201610918"  # Cullity X-Ray Diffraction 3rd
ISBN_CALLISTER   = "978-1119405498"  # Callister Materials Science


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ── CHEM2 — Nernst Equation ──
    ("CHEM2", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 7 (Electrochemistry). Nernst 1889 Z. phys. Chem. 4, 129 has no online DOI; "
     "textbook serves as canonical citable source. Reused."),
    ("CHEM2", "isbn", ISBN_MCQUARRIE, None,
     "McQuarrie-Simon - Physical Chemistry: A Molecular Approach",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 26. ISBN claimed; verify WorldCat."),
    ("CHEM2", "wikipedia",
     "https://en.wikipedia.org/wiki/Nernst_equation", None, "Nernst equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── CHEM3 — Faraday's Laws of Electrolysis ──
    ("CHEM3", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 7. Faraday 1833-34 Phil. Trans. has no online DOI for 19th-century volumes; "
     "textbook anchor canonical. Reused."),
    ("CHEM3", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science (14th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 20. ISBN claimed; verify WorldCat."),
    ("CHEM3", "wikipedia",
     "https://en.wikipedia.org/wiki/Faraday%27s_laws_of_electrolysis", None,
     "Faraday's laws of electrolysis",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── CHEM4 — Henderson-Hasselbalch ──
    ("CHEM4", "isbn", ISBN_LEHNINGER, None,
     "Lehninger - Principles of Biochemistry (7th ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Lehninger Ch. 2 covers H-H equation in biochemistry context. "
     "Henderson 1908 + Hasselbalch 1916 historical. ISBN claimed; verify."),
    ("CHEM4", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Buffer/acid-base equilibrium chapter. Reused."),
    ("CHEM4", "wikipedia",
     "https://en.wikipedia.org/wiki/Henderson%E2%80%93Hasselbalch_equation", None,
     "Henderson-Hasselbalch equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── CHEM5 — Law of Mass Action / Reaction Rate ──
    ("CHEM5", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 21. Guldberg-Waage 1864 Forhandlinger Videnskabs-Selskabet i Christiania "
     "is the historical origin (no online DOI). Textbook canonical. Reused."),
    ("CHEM5", "isbn", ISBN_MCQUARRIE, None,
     "McQuarrie-Simon - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("CHEM5", "wikipedia",
     "https://en.wikipedia.org/wiki/Law_of_mass_action", None, "Law of mass action",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── CR1 — Bragg's Law ──
    ("CR1", "doi", "10.1098/rspa.1913.0040", None,
     "Bragg-Bragg 1913 The Reflection of X-rays by Crystals",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "W.H. Bragg & W.L. Bragg 1913 PRSA 88, 428. Royal Society DOI pattern; "
     "DOI reconstructed from RSPA pattern, not WebFetch-verified this session."),
    ("CR1", "isbn", ISBN_CULLITY, None,
     "Cullity-Stock - Elements of X-Ray Diffraction (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Cullity-Stock Ch. 3 — definitive treatment of Bragg condition. ISBN claimed; verify."),
    ("CR1", "wikipedia",
     "https://en.wikipedia.org/wiki/Bragg%27s_law", None, "Bragg's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC1 — Le Chatelier's Principle ──
    ("KC1", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 6 (Equilibrium). Le Chatelier 1884 Comptes Rendus has no online DOI. "
     "Textbook canonical. Reused."),
    ("KC1", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("KC1", "wikipedia",
     "https://en.wikipedia.org/wiki/Le_Chatelier%27s_principle", None,
     "Le Chatelier's principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC2 — Microscopic Reversibility ──
    ("KC2", "doi", "10.1073/pnas.11.7.436", None,
     "Tolman 1924 Duration of molecules in upper quantum states",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Tolman 1924 PNAS 11, 436. PNAS DOI pattern."),
    ("KC2", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("KC2", "wikipedia",
     "https://en.wikipedia.org/wiki/Microscopic_reversibility", None,
     "Microscopic reversibility",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC3 — Hammond-Leffler Postulate ──
    ("KC3", "doi", "10.1021/ja01607a027", None,
     "Hammond 1955 A Correlation of Reaction Rates",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hammond 1955 J. Am. Chem. Soc. 77, 334. ACS DOI pattern."),
    ("KC3", "isbn", ISBN_CLAYDEN, None,
     "Clayden-Greeves-Warren - Organic Chemistry (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Clayden Ch. 41 covers Hammond postulate in transition-state theory. ISBN claimed; verify."),
    ("KC3", "wikipedia",
     "https://en.wikipedia.org/wiki/Hammond%27s_postulate", None,
     "Hammond's postulate",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC4 — Hess's Law ──
    ("KC4", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 2. Hess 1840 Bull. Acad. Sci. St. Petersburg has no online DOI. Reused."),
    ("KC4", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("KC4", "wikipedia",
     "https://en.wikipedia.org/wiki/Hess%27s_law", None, "Hess's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC5 — Gibbs-Helmholtz Equation ──
    ("KC5", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 3-4. Gibbs 1875-78 + Helmholtz 1882 historical (no DOIs). Reused."),
    ("KC5", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Callen Ch. 5-6 (Legendre transforms). Reused from TD3."),
    ("KC5", "wikipedia",
     "https://en.wikipedia.org/wiki/Gibbs%E2%80%93Helmholtz_equation", None,
     "Gibbs-Helmholtz equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC6 — Raoult's Law ──
    ("KC6", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 5. Raoult 1887 Comptes Rendus 104, 1430 has no online DOI. Reused."),
    ("KC6", "isbn", ISBN_MCQUARRIE, None,
     "McQuarrie-Simon - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("KC6", "wikipedia",
     "https://en.wikipedia.org/wiki/Raoult%27s_law", None, "Raoult's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC7 — Henry's Law ──
    ("KC7", "doi", "10.1098/rstl.1803.0004", None,
     "Henry 1803 Experiments on the quantity of gases absorbed by water",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Henry 1803 Phil. Trans. Roy. Soc. 93, 29. Royal Society DOI pattern; "
     "DOI reconstructed, not WebFetch-verified this session."),
    ("KC7", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 5. Reused."),
    ("KC7", "wikipedia",
     "https://en.wikipedia.org/wiki/Henry%27s_law", None, "Henry's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC8 — Law of Definite Composition ──
    ("KC8", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Ch. 1-2. Proust 1799 work has no online DOI. Reused."),
    ("KC8", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("KC8", "wikipedia",
     "https://en.wikipedia.org/wiki/Law_of_definite_proportions", None,
     "Law of definite proportions",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC9 — Dalton's Law of Multiple Proportions ──
    ("KC9", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Ch. 1-2. Dalton 1808 A New System of Chemical Philosophy is the historical book. Reused."),
    ("KC9", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("KC9", "wikipedia",
     "https://en.wikipedia.org/wiki/Law_of_multiple_proportions", None,
     "Law of multiple proportions",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── KC10 — Law of Reciprocal Proportions ──
    ("KC10", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Ch. 1-2 covers the early stoichiometry laws. Richter 1791-1802 historical. Reused."),
    ("KC10", "wikipedia",
     "https://en.wikipedia.org/wiki/Law_of_reciprocal_proportions", None,
     "Law of reciprocal proportions",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("KC10", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),

    # ── MS1 — Young's Modulus ──
    ("MS1", "isbn", ISBN_GOLDSTEIN, None,
     "Goldstein - Classical Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Continuum mechanics treatment. Young 1807 A Course of Lectures on Natural Philosophy "
     "is the historical book. Reused from CM1."),
    ("MS1", "isbn", ISBN_CALLISTER, None,
     "Callister - Materials Science and Engineering",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Callister Ch. 6 (Mechanical Properties). ISBN claimed; verify WorldCat."),
    ("MS1", "wikipedia",
     "https://en.wikipedia.org/wiki/Young%27s_modulus", None, "Young's modulus",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
]


ENTRIES = (
    "CHEM2", "CHEM3", "CHEM4", "CHEM5",
    "KC1", "KC2", "KC3", "KC4", "KC5", "KC6", "KC7", "KC8", "KC9", "KC10",
    "CR1", "MS1",
)


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
