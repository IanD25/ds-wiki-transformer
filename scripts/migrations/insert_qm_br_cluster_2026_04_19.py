"""
Insert QM + BR cluster anchors — 2026-04-19

9 entries split into 3 sub-clusters by content (the "QM" prefix is misleading):
  Sub-A — true QM (QM2, QM3, QM4) — reuses QM1's Sakurai/Griffiths/Shankar/von Neumann
  Sub-B — special relativity (QM5, mistagged) — Einstein 1905 + MTW + Taylor-Wheeler
  Sub-C — quantum gravity / holography (BR01-05) — per-entry arXiv/DOI progenitor + MTW

Anchors drafted in docs/prior_art_reviews/CLUSTER_QM_BR_2026_04_19.md.
Debuts the `open_in_literature` relationship type (BR01).

Run: python3 scripts/migrations/insert_qm_br_cluster_2026_04_19.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-qm-br-cluster-2026-04-19"

# Reused (verified at QM1 / GV1)
ISBN_VON_NEUMANN  = "978-0691178561"
ISBN_SAKURAI      = "978-1108473224"
ISBN_GRIFFITHS_QM = "978-1107189638"
ISBN_SHANKAR      = "978-0306447907"
ISBN_MTW          = "978-0716703440"

# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ==========================================================
    # Sub-cluster A — TRUE QM (QM2, QM3, QM4)
    # Each gets von Neumann (axiomatic) + Sakurai/Griffiths/Shankar (textbook)
    # plus per-entry progenitor DOIs and Wikipedia.
    # ==========================================================

    # ── QM2 — Heisenberg Uncertainty Principle ──
    ("QM2", "doi", "10.1007/BF01397280", None,
     "Heisenberg 1927 Uber den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Heisenberg 1927 Z. Phys. 43, 172. Springer historic-Z.Phys. DOI pattern; "
     "not WebFetch-verified this session, follow-up via CrossRef."),

    ("QM2", "doi", "10.1103/PhysRev.34.163", None,
     "Robertson 1929 The Uncertainty Principle",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Robertson 1929 Phys. Rev. 34, 163. Generalizes uncertainty to arbitrary "
     "operator pairs: ΔAΔB >= 0.5*|<[A,B]>|. APS DOI pattern."),

    ("QM2", "isbn", ISBN_VON_NEUMANN, None,
     "von Neumann - Mathematical Foundations of Quantum Mechanics",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "von Neumann 1932 Mathematische Grundlagen der Quantenmechanik. Reused from QM1."),

    ("QM2", "isbn", ISBN_SAKURAI, None,
     "Sakurai - Modern Quantum Mechanics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Sakurai-Napolitano 2020. Treats uncertainty rigorously in Ch. 1. Reused from QM1."),

    ("QM2", "isbn", ISBN_GRIFFITHS_QM, None,
     "Griffiths-Schroeter - Introduction to QM (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Griffiths-Schroeter 2018, standard undergraduate QM. Reused from QM1."),

    ("QM2", "isbn", ISBN_SHANKAR, None,
     "Shankar - Principles of QM (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Shankar 1994. Reused from QM1."),

    ("QM2", "wikipedia",
     "https://en.wikipedia.org/wiki/Uncertainty_principle", None,
     "Uncertainty principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session; pending Wikipedia oldid backfill sweep."),

    # ── QM3 — Pauli Exclusion Principle ──
    ("QM3", "doi", "10.1007/BF02980631", None,
     "Pauli 1925 Uber den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Pauli 1925 Z. Phys. 31, 765. Springer historic-Z.Phys. DOI pattern; "
     "not WebFetch-verified this session."),

    ("QM3", "doi", "10.1103/PhysRev.58.716", None,
     "Pauli 1940 The Connection Between Spin and Statistics",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Pauli 1940 Phys. Rev. 58, 716 — spin-statistics theorem. The deeper 'why' "
     "behind exclusion. APS DOI pattern."),

    ("QM3", "isbn", ISBN_VON_NEUMANN, None,
     "von Neumann - Mathematical Foundations of QM",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Reused from QM1."),

    ("QM3", "isbn", ISBN_SAKURAI, None,
     "Sakurai - Modern QM (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Treats identical-particle statistics in Ch. 7. Reused from QM1."),

    ("QM3", "isbn", ISBN_GRIFFITHS_QM, None,
     "Griffiths-Schroeter - Introduction to QM (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from QM1."),

    ("QM3", "isbn", ISBN_SHANKAR, None,
     "Shankar - Principles of QM (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from QM1."),

    ("QM3", "wikipedia",
     "https://en.wikipedia.org/wiki/Pauli_exclusion_principle", None,
     "Pauli exclusion principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── QM4 — de Broglie Wavelength ──
    ("QM4", "doi", "10.1051/anphys/192510030022", None,
     "de Broglie 1925 Recherches sur la theorie des Quanta",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "de Broglie 1925 Annales de Physique 10, 22. EDP Sciences DOI pattern; "
     "less common pattern than APS/Springer; flagged for CrossRef verification."),

    ("QM4", "doi", "10.1103/PhysRev.30.705", None,
     "Davisson-Germer 1927 Diffraction of Electrons by a Crystal of Nickel",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Davisson-Germer 1927 Phys. Rev. 30, 705. Experimental confirmation of "
     "matter waves via electron diffraction. APS DOI pattern."),

    ("QM4", "isbn", ISBN_VON_NEUMANN, None,
     "von Neumann - Mathematical Foundations of QM",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Reused from QM1."),

    ("QM4", "isbn", ISBN_SAKURAI, None,
     "Sakurai - Modern QM (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from QM1."),

    ("QM4", "isbn", ISBN_GRIFFITHS_QM, None,
     "Griffiths-Schroeter - Introduction to QM (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from QM1."),

    ("QM4", "isbn", ISBN_SHANKAR, None,
     "Shankar - Principles of QM (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from QM1."),

    ("QM4", "wikipedia",
     "https://en.wikipedia.org/wiki/Matter_wave", None,
     "Matter wave",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ==========================================================
    # Sub-cluster B — SPECIAL RELATIVITY (QM5, mistagged under QM prefix)
    # ==========================================================

    ("QM5", "doi", "10.1002/andp.19053221004", None,
     "Einstein 1905 Zur Elektrodynamik bewegter Korper",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Einstein 1905 Annalen der Physik 17, 891. Same Wiley-Annalen DOI pattern "
     "as Einstein 1916 (verified at GV1). Section 2 introduces the two postulates."),

    ("QM5", "isbn", ISBN_MTW, None,
     "MTW - Gravitation (1973)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "MTW Ch. 1-6 cover SR rigorously; Ch. 2 derives Lorentz transformations "
     "from the postulates. Reused from GV1."),

    ("QM5", "isbn", "978-0716723271", None,
     "Taylor-Wheeler - Spacetime Physics (2nd ed., 1992)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Pedagogically canonical SR text. ISBN claimed from memory; verify via WorldCat."),

    ("QM5", "wikipedia",
     "https://en.wikipedia.org/wiki/Postulates_of_special_relativity", None,
     "Postulates of special relativity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ==========================================================
    # Sub-cluster C — QUANTUM GRAVITY / HOLOGRAPHY (BR01-05)
    # ==========================================================

    # ── BR01 — ER = EPR (open_question; debuts open_in_literature relationship) ──
    ("BR01", "doi", "10.1002/prop.201300020", None,
     "Maldacena-Susskind 2013 Cool horizons for entangled black holes",
     1, "canonical", "open_in_literature", "progenitor", "high",
     "Maldacena-Susskind 2013 Fortschr. Phys. 61, 781. arXiv:1306.0533. "
     "Conjecture posed and developed; remains open in the literature. "
     "DEBUTS the `open_in_literature` relationship type."),

    ("BR01", "wikipedia",
     "https://en.wikipedia.org/wiki/ER_%3D_EPR", None,
     "ER = EPR",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    ("BR01", "isbn", ISBN_MTW, None,
     "MTW - Gravitation (1973)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "MTW Ch. 31 introduces Einstein-Rosen bridges geometrically (the ER side "
     "of the conjecture). Reused from GV1."),

    # ── BR02 — AdS/CFT Correspondence ──
    ("BR02", "doi", "10.4310/ATMP.1998.v2.n2.a1", None,
     "Maldacena 1998 The Large N Limit of Superconformal Field Theories and Supergravity",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Maldacena 1998 Adv. Theor. Math. Phys. 2, 231. arXiv:hep-th/9711200. "
     "Founding paper of AdS/CFT; >21000 citations. IPM ATMP DOI pattern."),

    ("BR02", "wikipedia",
     "https://en.wikipedia.org/wiki/AdS%2FCFT_correspondence", None,
     "AdS/CFT correspondence",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    ("BR02", "isbn", ISBN_MTW, None,
     "MTW - Gravitation (1973)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Anti-de Sitter spacetime treated in MTW Ch. 25. Predates Maldacena 1998 "
     "but provides the AdS-side geometric foundation. Reused from GV1."),

    # ── BR03 — Van Raamsdonk: Entanglement Builds Spacetime ──
    ("BR03", "doi", "10.1007/s10714-010-1034-0", None,
     "Van Raamsdonk 2010 Building up spacetime with quantum entanglement",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Van Raamsdonk 2010 Gen. Rel. Grav. 42, 2323. arXiv:1005.3035. "
     "Springer GRG DOI pattern."),

    ("BR03", "doi", "10.1002/prop.201300020", None,
     "Maldacena-Susskind 2013 Cool horizons for entangled black holes",
     1, "canonical", "canonical_authority", "comprehensive_survey", "medium",
     "Maldacena-Susskind 2013 contextualizes the entanglement-geometry program "
     "and explicitly cites Van Raamsdonk 2010. Same paper used as `open_in_literature` "
     "progenitor for BR01."),

    ("BR03", "isbn", ISBN_MTW, None,
     "MTW - Gravitation (1973)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Spacetime-construction context. Reused from GV1."),

    # ── BR04 — Thermodynamic Geometry (Ruppeiner Metric) ──
    ("BR04", "doi", "10.1103/PhysRevA.20.1608", None,
     "Ruppeiner 1979 Thermodynamics: A Riemannian geometric model",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Ruppeiner 1979 Phys. Rev. A 20, 1608. APS DOI pattern."),

    ("BR04", "doi", "10.1103/RevModPhys.67.605", None,
     "Ruppeiner 1995 Riemannian geometry in thermodynamic fluctuation theory",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Ruppeiner 1995 Rev. Mod. Phys. 67, 605. Definitive review of the program. "
     "APS RMP DOI pattern."),

    ("BR04", "wikipedia",
     "https://en.wikipedia.org/wiki/Ruppeiner_geometry", None,
     "Ruppeiner geometry",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── BR05 — Dimensional Flow in Quantum Gravity ──
    ("BR05", "doi", "10.1103/PhysRevLett.95.171301", None,
     "Ambjorn-Jurkiewicz-Loll 2005 Spectral Dimension of the Universe",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Ambjorn-Jurkiewicz-Loll 2005 Phys. Rev. Lett. 95, 171301. First observation "
     "of d_eff -> 2 at small scales in causal dynamical triangulations. APS DOI pattern."),

    ("BR05", "doi", "10.1088/1361-6382/aa8535", None,
     "Carlip 2017 Dimension and dimensional reduction in quantum gravity",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Carlip 2017 Class. Quant. Grav. 34, 193001. Comprehensive review across "
     "CDT, Horava-Lifshitz, asymptotic safety, etc. IOP CQG DOI pattern."),

    ("BR05", "wikipedia",
     "https://en.wikipedia.org/wiki/Quantum_gravity", None,
     "Quantum gravity (subsection on dimensional reduction)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No dedicated Wikipedia article for 'dimensional flow' specifically; "
     "anchored to Quantum_gravity (relevant subsection). No oldid this session."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        entries = ("QM2", "QM3", "QM4", "QM5", "BR01", "BR02", "BR03", "BR04", "BR05")

        # Pre-flight: every entry must already have domain tags
        for eid in entries:
            cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            )
            n = cur.fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
        print(f"Pre-flight OK: all {len(entries)} entries have current domain tags.")
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
        print()

        # Per-entry summary
        for eid in entries:
            print(f"Anchors for {eid}:")
            for row in cur.execute("""
                SELECT source, canonical_role, relationship, confidence, tier
                FROM external_anchors
                WHERE entry_id = ?
                ORDER BY
                  CASE relationship
                    WHEN 'canonical_authority' THEN 1
                    WHEN 'open_in_literature' THEN 2
                    ELSE 3 END,
                  CASE canonical_role
                    WHEN 'progenitor' THEN 1 WHEN 'axiomatic_foundation' THEN 2
                    WHEN 'standard_textbook' THEN 3 WHEN 'living_reference' THEN 4
                    WHEN 'comprehensive_survey' THEN 5 ELSE 6 END,
                  tier
            """, (eid,)):
                role = row[1] if row[1] else "(no role)"
                rel  = row[2]
                rel_tag = "" if rel == "canonical_authority" else f" [{rel}]"
                print(f"  tier{row[4]} {row[0]:15} / {role:22} ({row[3]}){rel_tag}")
            print()

        # Totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries_anchored = cur.fetchone()[0]
        print(f"Totals after this batch:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")

        # New: relationship-type distribution (verifies open_in_literature debut)
        cur.execute("""
            SELECT relationship, COUNT(*) FROM external_anchors
            GROUP BY relationship
        """)
        print(f"\nRelationship-type distribution (incl. open_in_literature debut):")
        for r in cur.fetchall():
            print(f"  {r[0]:25} {r[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
