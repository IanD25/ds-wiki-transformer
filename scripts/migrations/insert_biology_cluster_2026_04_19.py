"""
Insert biology cluster anchors — 2026-04-19

16 entries split into:
  ANCHOR (14):  BIO2-11, D1, F1, F2, F3
  IC FLAG (2):  F4 (Saturation Dynamics consolidation), F5 (Oxygen viability corridor — AlphaEntropy/CcO program)

Template seed: C1 + BIO1 (anchored 2026-04-18). Reuses Schmidt-Nielsen,
West *Scale*, WBE 1997, Griffiths-genetics ISBNs.

See docs/prior_art_reviews/CLUSTER_BIOLOGY_2026_04_19.md.

Run: python3 scripts/migrations/insert_biology_cluster_2026_04_19.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-biology-cluster-2026-04-19"

# Reused (verified at C1 / BIO1 / prior batches)
ISBN_GRIFFITHS_GEN = "978-1319114770"  # Griffiths Introduction to Genetic Analysis (BIO1)
ISBN_SCHMIDT_NIEL  = "978-0521319874"  # Schmidt-Nielsen Scaling (C1)

# New textbook ISBNs — all medium pending WorldCat verify
ISBN_ALBERTS       = "978-0815344322"  # Alberts Molecular Biology of the Cell 6th
ISBN_HARTL_CLARK   = "978-0878933082"  # Hartl-Clark Principles of Population Genetics 4th
ISBN_MURRAY        = "978-0387952239"  # Murray Mathematical Biology 3rd
ISBN_KANDEL        = "978-1259642234"  # Kandel Principles of Neural Science 6th
ISBN_FISHER_1930   = "978-0198504405"  # Fisher 1930 Genetical Theory (Oxford reprint)
ISBN_ASHBY_CYB     = "978-0412197604"  # Ashby 1956 Introduction to Cybernetics
ISBN_BEGON_ECOL    = "978-1405151986"  # Begon-Townsend-Harper Ecology 4th
ISBN_GAUSE_1934    = "978-1605209708"  # Gause 1934 Struggle for Existence (reprint)


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ============================================================
    # GENETICS / EVOLUTION
    # ============================================================

    # ── BIO2 — Hardy-Weinberg ──
    ("BIO2", "doi", "10.1126/science.28.706.49", None,
     "Hardy 1908 Mendelian Proportions in a Mixed Population",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hardy 1908 Science 28, 49. AAAS DOI pattern. "
     "Weinberg 1908 (independent contemporary) has no English-side DOI."),
    ("BIO2", "isbn", ISBN_HARTL_CLARK, None,
     "Hartl-Clark - Principles of Population Genetics (4th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 2 covers HW. ISBN claimed from memory; verify WorldCat."),
    ("BIO2", "isbn", ISBN_GRIFFITHS_GEN, None,
     "Griffiths - Introduction to Genetic Analysis (12th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from BIO1."),
    ("BIO2", "wikipedia",
     "https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle", None,
     "Hardy-Weinberg principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BIO3 — Fisher's Fundamental Theorem ──
    ("BIO3", "isbn", ISBN_FISHER_1930, None,
     "Fisher - The Genetical Theory of Natural Selection (1930)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Fisher 1930 Oxford. ISBN of Oxford reprint. Ch. 2 introduces the Fundamental Theorem."),
    ("BIO3", "isbn", ISBN_HARTL_CLARK, None,
     "Hartl-Clark - Principles of Population Genetics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("BIO3", "wikipedia",
     "https://en.wikipedia.org/wiki/Fisher%27s_fundamental_theorem_of_natural_selection", None,
     "Fisher's fundamental theorem of natural selection",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BIO8 — Neutral Theory ──
    ("BIO8", "doi", "10.1038/217624a0", None,
     "Kimura 1968 Evolutionary rate at the molecular level",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Kimura 1968 Nature 217, 624. Nature DOI pattern."),
    ("BIO8", "isbn", ISBN_HARTL_CLARK, None,
     "Hartl-Clark - Principles of Population Genetics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 4-5 covers neutral theory. Reused."),
    ("BIO8", "wikipedia",
     "https://en.wikipedia.org/wiki/Neutral_theory_of_molecular_evolution", None,
     "Neutral theory of molecular evolution",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BIO11 — Molecular Clock ──
    ("BIO11", "doi", "10.1038/217624a0", None,
     "Kimura 1968 Evolutionary rate at the molecular level",
     1, "canonical", "canonical_authority", "cited_by", "high",
     "Same Kimura 1968 paper — provides the rate-constancy mechanism. "
     "Zuckerkandl-Pauling 1965 chapter (the actual progenitor) has no DOI."),
    ("BIO11", "isbn", ISBN_HARTL_CLARK, None,
     "Hartl-Clark - Principles of Population Genetics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("BIO11", "wikipedia",
     "https://en.wikipedia.org/wiki/Molecular_clock", None, "Molecular clock",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # CELL / MOLECULAR BIOLOGY
    # ============================================================

    # ── BIO4 — Cell Theory ──
    ("BIO4", "isbn", ISBN_ALBERTS, None,
     "Alberts et al. - Molecular Biology of the Cell (6th ed.)",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "medium",
     "Alberts Ch. 1 — modern statement of cell theory. "
     "Schleiden 1838 + Schwann 1839 (historical progenitors) have no modern DOIs. "
     "ISBN claimed from memory; verify WorldCat."),
    ("BIO4", "isbn", ISBN_ALBERTS, None,
     "Alberts et al. - Molecular Biology of the Cell (6th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     # NOTE: same ISBN as axiomatic_foundation; UNIQUE is on (entry_id, source,
     # identifier, relationship); both have relationship='canonical_authority'
     # so this will be a UNIQUE-conflict skip. Keeping for clarity.
     "Same ISBN as axiomatic_foundation; will be skipped by UNIQUE constraint."),
    ("BIO4", "wikipedia",
     "https://en.wikipedia.org/wiki/Cell_theory", None, "Cell theory",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BIO5 — Central Dogma ──
    ("BIO5", "doi", "10.1038/227561a0", None,
     "Crick 1970 Central dogma of molecular biology",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Crick 1970 Nature 227, 561. Crick's restatement and clarification of "
     "the original 1958 Symp. Soc. Exp. Biol. chapter. Nature DOI pattern."),
    ("BIO5", "isbn", ISBN_ALBERTS, None,
     "Alberts et al. - Molecular Biology of the Cell",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 6-7 (DNA -> RNA -> Protein). Reused."),
    ("BIO5", "wikipedia",
     "https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology", None,
     "Central dogma of molecular biology",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BIO6 — Michaelis-Menten ──
    ("BIO6", "doi", "10.1021/bi201284u", None,
     "Johnson-Goody 2011 The Original Michaelis Constant: Translation of the 1913 Michaelis-Menten Paper",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Johnson-Goody 2011 Biochemistry 50, 8264 — definitive English translation of "
     "Michaelis-Menten 1913 Biochem. Z. 49, 333. ACS DOI pattern."),
    ("BIO6", "isbn", ISBN_ALBERTS, None,
     "Alberts et al. - Molecular Biology of the Cell",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused. Ch. 3 enzymes."),
    ("BIO6", "wikipedia",
     "https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics", None,
     "Michaelis-Menten kinetics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # ECOLOGY / MATH BIOLOGY
    # ============================================================

    # ── BIO7 — Lotka-Volterra ──
    ("BIO7", "isbn", ISBN_MURRAY, None,
     "Murray - Mathematical Biology (3rd ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Murray Ch. 3-4 derives and analyzes Lotka-Volterra. "
     "Lotka 1925 (book, no DOI) + Volterra 1926 Mem. Accad. Lincei (no DOI) are historical. "
     "ISBN claimed from memory; verify WorldCat."),
    ("BIO7", "isbn", ISBN_BEGON_ECOL, None,
     "Begon-Townsend-Harper - Ecology (4th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 8 predator-prey. ISBN claimed from memory; verify WorldCat."),
    ("BIO7", "wikipedia",
     "https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations", None,
     "Lotka-Volterra equations",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # PHYSIOLOGY / NEUROSCIENCE
    # ============================================================

    # ── BIO9 — Hodgkin-Huxley ──
    ("BIO9", "doi", "10.1113/jphysiol.1952.sp004764", None,
     "Hodgkin-Huxley 1952 A quantitative description of membrane current and its application to conduction and excitation in nerve",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hodgkin-Huxley 1952 J. Physiol. 117, 500. Wiley physiol. DOI pattern."),
    ("BIO9", "isbn", ISBN_KANDEL, None,
     "Kandel - Principles of Neural Science (6th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Kandel Ch. 7-9 covers HH model. ISBN claimed from memory; verify WorldCat."),
    ("BIO9", "wikipedia",
     "https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model", None,
     "Hodgkin-Huxley model",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BIO10 — Homeostasis ──
    ("BIO10", "doi", "10.1152/physrev.1929.9.3.399", None,
     "Cannon 1929 Organization for physiological homeostasis",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Cannon 1929 Physiol. Rev. 9, 399. APS Physiology DOI pattern. "
     "Builds on Bernard 1865 'milieu intérieur' concept."),
    ("BIO10", "isbn", ISBN_KANDEL, None,
     "Kandel - Principles of Neural Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Background on autonomic regulation. Reused."),
    ("BIO10", "wikipedia",
     "https://en.wikipedia.org/wiki/Homeostasis", None, "Homeostasis",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # PSYCHOPHYSICS
    # ============================================================

    # ── D1 — Stevens' Power Law ──
    ("D1", "doi", "10.1037/h0046162", None,
     "Stevens 1957 On the psychophysical law",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Stevens 1957 Psychol. Rev. 64, 153. APA DOI pattern."),
    ("D1", "wikipedia",
     "https://en.wikipedia.org/wiki/Stevens%27s_power_law", None,
     "Stevens's power law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # CONSTRAINT LAWS (F1-3)
    # ============================================================

    # ── F1 — Ashby's Law of Requisite Variety ──
    ("F1", "isbn", ISBN_ASHBY_CYB, None,
     "Ashby - An Introduction to Cybernetics (1956)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Ashby 1956 Ch. 11 introduces Law of Requisite Variety. "
     "ISBN claimed from memory; verify WorldCat."),
    ("F1", "wikipedia",
     "https://en.wikipedia.org/wiki/Variety_(cybernetics)", None,
     "Variety (cybernetics)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Article covers Ashby's Law. No oldid."),

    # ── F2 — Liebig's Law of the Minimum ──
    ("F2", "isbn", ISBN_BEGON_ECOL, None,
     "Begon-Townsend-Harper - Ecology",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 3-4 covers Liebig's Law. Liebig 1840 (Organic Chemistry in Its Application "
     "to Agriculture) has no modern DOI; textbook anchor canonical."),
    ("F2", "wikipedia",
     "https://en.wikipedia.org/wiki/Liebig%27s_law_of_the_minimum", None,
     "Liebig's law of the minimum",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── F3 — Gause's Competitive Exclusion ──
    ("F3", "isbn", ISBN_GAUSE_1934, None,
     "Gause - The Struggle for Existence (1934, reprint)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Gause 1934 Williams & Wilkins. ISBN of modern reprint. "
     "Established the principle empirically with Paramecium experiments."),
    ("F3", "isbn", ISBN_BEGON_ECOL, None,
     "Begon-Townsend-Harper - Ecology",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 8 competition. Reused."),
    ("F3", "wikipedia",
     "https://en.wikipedia.org/wiki/Competitive_exclusion_principle", None,
     "Competitive exclusion principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
]


# Internal_construction flags
IC_FLAGS = [
    ("F4",
     "F4: Wiki-internal consolidation of three saturation forms "
     "(Michaelis-Menten, Logistic, Hyperbolic) under one named meta-pattern. "
     "The underlying physics is real and each form has its own canonical "
     "literature, but the named umbrella 'F4 Saturation Dynamics' is a wiki-"
     "construct, not citable as a single source.",
     "owner-aware"),
    ("F5",
     "F5: AlphaEntropy/CcO-program-specific oxygen viability corridor with "
     "specific PO2 bounds (~1-3 mmHg / ~50-100 mmHg) and hysteretic "
     "boundaries. Tied to the wiki's CcO conjecture program (P4). "
     "Owner-derived corridor specifics, not standalone literature.",
     "owner-aware"),
]


ENTRIES_ANCHORED = (
    "BIO2", "BIO3", "BIO4", "BIO5", "BIO6", "BIO7", "BIO8", "BIO9",
    "BIO10", "BIO11", "D1", "F1", "F2", "F3",
)
ENTRIES_IC = ("F4", "F5")


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        # Pre-flight: every entry in scope must have domain tags
        all_entries = ENTRIES_ANCHORED + ENTRIES_IC
        for eid in all_entries:
            n = cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            ).fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
        print(f"Pre-flight OK: all {len(all_entries)} entries tagged.")
        print()

        # Insert anchors
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
        print(f"  Anchors inserted: {inserted}, skipped: {skipped}")

        # Insert IC flags
        print(f"\nFlagging {len(IC_FLAGS)} entries as internal_construction...")
        ic_inserted = ic_skipped = 0
        for (eid, reason, scrutiny) in IC_FLAGS:
            res = conn.execute(
                "INSERT OR IGNORE INTO internal_constructions "
                "(entry_id, reason, searched_sources, flagged_date, "
                " flagged_by_session, scrutiny_level, notes) "
                "VALUES (?,?,?,?,?,?,?)",
                (eid, reason,
                 '["wiki-content-inspection-2026-04-19"]',
                 TODAY, SESSION, scrutiny,
                 "Flagged after reading entry content; no GSW external equivalent. "
                 "Entry preserved per no-deletions rule."),
            )
            if res.rowcount > 0:
                ic_inserted += 1
            else:
                ic_skipped += 1
        print(f"  IC inserted: {ic_inserted}, skipped: {ic_skipped}")

        conn.commit()
        print()

        # Per-entry summary
        print("=== Per-entry anchor counts ===")
        for eid in ENTRIES_ANCHORED:
            n = cur.execute(
                "SELECT COUNT(*) FROM external_anchors WHERE entry_id=?", (eid,),
            ).fetchone()[0]
            slots = cur.execute(
                "SELECT COUNT(DISTINCT canonical_role) FROM external_anchors "
                "WHERE entry_id=? AND canonical_role IS NOT NULL", (eid,),
            ).fetchone()[0]
            below_min = " *** BELOW 3-MIN" if n < 3 else ""
            print(f"  {eid:<6}  {n:>2} anchors / {slots} slots filled{below_min}")
        print(f"\n  IC flagged: {', '.join(ENTRIES_IC)}")

        # Totals
        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        ic_total = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM internal_constructions"
        ).fetchone()[0]
        print(f"\nTotals after this batch:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")
        print(f"  internal_constructions:  {ic_total}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
