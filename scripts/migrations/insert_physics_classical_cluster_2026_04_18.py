"""
Physics Classical Cluster — CM2-11 + AM1-4 + EM1-14 — 2026-04-18

Largest physics sub-cluster in the retrospective pass. 28 entries across
three sharing-textbook groups:

  Classical mechanics (CM2-11, 10 entries) — Goldstein + Taylor
  Analytical mechanics (AM1-4, 4 entries)   — Goldstein + Arnold
  Electromagnetism (EM1-14, 14 entries)     — Jackson + Griffiths

All entries get 3-4 anchors (2 textbooks + Wikipedia + optional progenitor).
Per M0/architecture: pre-DOI classical physics (Newton, Gauss, Coulomb, etc.)
often only has textbook + Wikipedia anchors — honest limitation of the
historical record.

Run: python3 scripts/migrations/insert_physics_classical_cluster_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-physics-classical-2026-04-18"


# Textbook ISBNs (shared across sub-clusters)
GOLDSTEIN_ISBN = "978-0201657029"
TAYLOR_ISBN = "978-1891389221"
ARNOLD_ISBN = "978-0387968902"
JACKSON_ISBN = "978-0471309321"     # Classical Electrodynamics 3rd ed
GRIFFITHS_EM_ISBN = "978-1108420419" # Introduction to Electrodynamics 4th ed
PRINCIPIA_ISBN = "978-0520088177"   # Newton Principia (Cohen-Whitman)


def wiki(eid, slug, title, confidence="medium"):
    url = f"https://en.wikipedia.org/wiki/{slug}"
    return (eid, "wikipedia", url, None, title, 2,
            "active-literature", "canonical_authority", "living_reference",
            confidence,
            f"Wikipedia living_reference for {eid}. oldid not pinned in "
            "cluster batch; confidence medium pending revision-pin sweep.")


def isbn(eid, isbn_val, title, role="standard_textbook", confidence="high",
         notes=""):
    return (eid, "isbn", isbn_val, None, title, 1,
            "canonical", "canonical_authority", role, confidence, notes)


ANCHORS = []


# ==========================================================
# Classical mechanics cluster (CM2-11)
# Template: Goldstein + Taylor + Wikipedia, with Principia for Newton-era laws
# ==========================================================
CM_ENTRIES = [
    ("CM2",  "Newton's Law of Universal Gravitation",
     "Newton%27s_law_of_universal_gravitation", True),  # Principia
    ("CM3",  "Kepler's First Law — Elliptical Orbits",
     "Kepler%27s_laws_of_planetary_motion", False),
    ("CM4",  "Kepler's Second Law — Equal Areas",
     "Kepler%27s_laws_of_planetary_motion", False),
    ("CM5",  "Kepler's Third Law — Orbital Period Scaling",
     "Kepler%27s_laws_of_planetary_motion", False),
    ("CM6",  "Euler's Laws of Motion (Rigid Body)", "Euler%27s_laws_of_motion",
     False),
    ("CM7",  "Archimedes' Principle", "Archimedes%27_principle", False),
    ("CM8",  "Lorentz Force Law", "Lorentz_force", False),
    ("CM9",  "Hooke's Law", "Hooke%27s_law", False),
    ("CM10", "Conservation of Momentum", "Momentum", True),  # Principia
    ("CM11", "Conservation of Energy",
     "Conservation_of_energy", False),
]

for eid, title, slug, use_principia in CM_ENTRIES:
    ANCHORS.append(isbn(
        eid, GOLDSTEIN_ISBN,
        "Goldstein, Poole & Safko - Classical Mechanics (3rd ed.)",
        role="standard_textbook", confidence="high",
        notes=f"Goldstein 2001. Cluster-shared CM anchor for {title}."))
    ANCHORS.append(isbn(
        eid, TAYLOR_ISBN,
        "Taylor - Classical Mechanics (2005)",
        role="standard_textbook", confidence="high",
        notes=f"Taylor 2005. Undergraduate-level cluster anchor for {title}."))
    if use_principia:
        ANCHORS.append(isbn(
            eid, PRINCIPIA_ISBN,
            "Newton - Principia (Cohen-Whitman translation)",
            role="progenitor", confidence="high",
            notes=f"Newton 1687 Principia contains the progenitor statement "
                  f"of {title} (within the axioms/laws or Book I). Cross-"
                  f"entry source reuse with CM1."))
    ANCHORS.append(wiki(eid, slug, title, confidence="medium"))


# ==========================================================
# Analytical mechanics cluster (AM1-4)
# Template: Goldstein + Arnold + Wikipedia
# ==========================================================
AM_ENTRIES = [
    ("AM1", "Principle of Least Action",
     "Principle_of_least_action"),
    ("AM2", "Euler–Lagrange Equations", "Euler%E2%80%93Lagrange_equation"),
    ("AM3", "Hamilton's Equations",
     "Hamiltonian_mechanics"),
    ("AM4", "Hamilton–Jacobi Equation",
     "Hamilton%E2%80%93Jacobi_equation"),
]

for eid, title, slug in AM_ENTRIES:
    ANCHORS.append(isbn(
        eid, GOLDSTEIN_ISBN,
        "Goldstein, Poole & Safko - Classical Mechanics (3rd ed.)",
        role="standard_textbook", confidence="high",
        notes=f"Goldstein 2001. AM-cluster shared anchor for {title}."))
    ANCHORS.append(isbn(
        eid, ARNOLD_ISBN,
        "Arnold - Mathematical Methods of Classical Mechanics (2nd ed.)",
        role="standard_textbook", confidence="high",
        notes=f"Arnold 1989. Symplectic-geometric treatment of {title}. "
              "Cross-entry reuse with AM5 Noether."))
    ANCHORS.append(wiki(eid, slug, title, confidence="medium"))


# ==========================================================
# Electromagnetism cluster (EM1-14)
# Template: Jackson + Griffiths + Wikipedia
# ==========================================================
EM_ENTRIES = [
    ("EM1",  "Gauss's Law for Electricity", "Gauss%27s_law"),
    ("EM2",  "Gauss's Law for Magnetism", "Gauss%27s_law_for_magnetism"),
    ("EM3",  "Faraday's Law of Induction",
     "Faraday%27s_law_of_induction"),
    ("EM4",  "Ampère–Maxwell Law", "Amp%C3%A8re%27s_circuital_law"),
    ("EM5",  "Continuity Equation (Charge Conservation)",
     "Continuity_equation"),
    ("EM6",  "Coulomb's Law", "Coulomb%27s_law"),
    ("EM7",  "Biot–Savart Law", "Biot%E2%80%93Savart_law"),
    ("EM8",  "Lenz's Law", "Lenz%27s_law"),
    ("EM9",  "Ohm's Law", "Ohm%27s_law"),
    ("EM10", "Kirchhoff's Laws", "Kirchhoff%27s_circuit_laws"),
    ("EM11", "Joule's Law", "Joule_heating"),
    ("EM12", "Ampère's Circuital Law",
     "Amp%C3%A8re%27s_circuital_law"),
    ("EM13", "Wiedemann–Franz Law", "Wiedemann%E2%80%93Franz_law"),
    ("EM14", "Fine Structure Constant (α)", "Fine-structure_constant"),
]

for eid, title, slug in EM_ENTRIES:
    ANCHORS.append(isbn(
        eid, JACKSON_ISBN,
        "Jackson - Classical Electrodynamics (3rd ed.)",
        role="standard_textbook", confidence="high",
        notes=f"Jackson 1998. Standard graduate E&M textbook for {title}."))
    ANCHORS.append(isbn(
        eid, GRIFFITHS_EM_ISBN,
        "Griffiths - Introduction to Electrodynamics (4th ed.)",
        role="standard_textbook", confidence="high",
        notes=f"Griffiths 2017. Standard undergraduate E&M textbook for "
              f"{title}."))
    ANCHORS.append(wiki(eid, slug, title, confidence="medium"))


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        print(f"Classical-physics cluster — {len(ANCHORS)} anchor rows")
        print(f"  CM entries: {len(CM_ENTRIES)}, AM entries: {len(AM_ENTRIES)}, "
              f"EM entries: {len(EM_ENTRIES)}")
        print()

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

        print(f"  inserted: {inserted}")
        print(f"  skipped:  {skipped}")

        # Global totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM internal_constructions")
        ic = cur.fetchone()[0]

        print()
        print("=== Global state ===")
        print(f"  external_anchors rows:  {total}")
        print(f"  entries anchored:       {entries} / 300")
        print(f"  internal_constructions: {ic}")
        print(f"  processed (anchor OR ic): ~{entries + ic} / 300 "
              f"({(entries + ic)*100/300:.0f}%)")

        # Updated physics domain coverage
        cur.execute("ATTACH DATABASE 'data/ds_wiki.db' AS ds")
        cur.execute("""
            SELECT
                CASE WHEN INSTR(t.tag_path,'.')=0 THEN t.tag_path
                     ELSE SUBSTR(t.tag_path,1,INSTR(t.tag_path,'.')-1) END AS top_level,
                COUNT(DISTINCT e.entry_id) as tagged,
                COUNT(DISTINCT a.entry_id) as anchored
            FROM entry_source_domains e
            JOIN source_domain_taxonomy t ON t.id = e.tag_id
            LEFT JOIN external_anchors a ON a.entry_id = e.entry_id
            WHERE e.primacy='primary' AND e.review_status='current'
            GROUP BY top_level ORDER BY tagged DESC
        """)
        print()
        print("=== Updated domain coverage ===")
        print(f"  {'Domain':28} {'Tagged':>7} {'Anchored':>9}  {'%':>5}")
        for row in cur.fetchall():
            pct = row[2]*100/row[1] if row[1] else 0
            print(f"  {row[0]:28} {row[1]:7} {row[2]:9}  {pct:4.1f}%")

        # Updated co-citation graph
        print()
        print("=== Top co-cited sources ===")
        for r in cur.execute("""
            SELECT identifier, COUNT(DISTINCT entry_id) n,
                   MAX(title) title
            FROM external_anchors
            GROUP BY source, identifier
            HAVING n >= 5
            ORDER BY n DESC
        """):
            print(f"  {r[1]:3}× — {r[2][:55]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
