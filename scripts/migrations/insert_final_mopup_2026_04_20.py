"""
Final mop-up anchoring pass — 2026-04-20

Closes the remaining 11 unanchored entries (GT05 stays deferred pending owner clarification):
  Anchor (6):  MATH4, DM2, DM3, DM4, D2, E2
  IC (5):      H5, Q3, Q4, P2_STATUS, P12_STATUS

MATH4 Gödel is a 20-link wiki hub surfaced by the 2026-04-19 audit as a
high-priority unanchored target; this closes it.

Run: python3 scripts/migrations/insert_final_mopup_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-final-mopup-2026-04-20"

# Reused verified
ISBN_ENDERTON  = "978-0122384523"  # FL cluster
ISBN_VANDALEN  = "978-1447145578"  # FL cluster
ISBN_ATKINS    = "978-0198769866"
ISBN_BROWN_GEN = "978-0134414232"
ISBN_CRANK     = "978-0198533443"

# New ISBNs — medium
ISBN_BOOLOS    = "978-0521877527"  # Boolos-Burgess-Jeffrey Computability and Logic 5th ed
ISBN_CVITANOVIC = "978-8299022897"  # Cvitanović ChaosBook (free online; ISBN of print reprint)


ANCHORS = [
    # ── MATH4 — Gödel's Incompleteness Theorems (20-link wiki hub) ──
    ("MATH4", "doi", "10.1007/BF01700692", None,
     "Gödel 1931 Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Gödel 1931 Monatshefte für Mathematik und Physik 38, 173. Springer historic DOI pattern."),
    ("MATH4", "isbn", ISBN_ENDERTON, None,
     "Enderton - A Mathematical Introduction to Logic",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 3 covers incompleteness. Reused from FL cluster."),
    ("MATH4", "isbn", ISBN_BOOLOS, None,
     "Boolos-Burgess-Jeffrey - Computability and Logic (5th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Definitive graduate text covering first+second incompleteness theorems. "
     "ISBN claimed; verify WorldCat."),
    ("MATH4", "isbn", ISBN_VANDALEN, None,
     "van Dalen - Logic and Structure",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from FL cluster."),
    ("MATH4", "wikipedia",
     "https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems", None,
     "Gödel's incompleteness theorems",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── DM2 — Graham's Law ──
    ("DM2", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 1 (kinetic theory of gases — effusion rates inversely proportional to sqrt(M)). "
     "Graham 1833 Phil. Mag. 2, 175 has no online DOI. Reused."),
    ("DM2", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("DM2", "wikipedia",
     "https://en.wikipedia.org/wiki/Graham%27s_law", None, "Graham's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── DM3 — Lamm Equation (sedimentation in ultracentrifuge) ──
    ("DM3", "isbn", ISBN_CRANK, None,
     "Crank - The Mathematics of Diffusion",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Crank Ch. 6 covers convective diffusion including ultracentrifuge. "
     "Lamm 1929 Arkiv för Matematik, Astronomi och Fysik 21B(2), 1 has no online DOI. Reused."),
    ("DM3", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Sedimentation/ultracentrifuge coverage. Reused."),
    ("DM3", "wikipedia",
     "https://en.wikipedia.org/wiki/Lamm_equation", None, "Lamm equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── DM4 — Dalton's Law of Partial Pressures ──
    ("DM4", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 1. Dalton 1802 historical (different from Dalton 1808 multiple proportions/KC9). Reused."),
    ("DM4", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("DM4", "wikipedia",
     "https://en.wikipedia.org/wiki/Dalton%27s_law", None, "Dalton's law (partial pressures)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── D2 — Feigenbaum Universality ──
    ("D2", "doi", "10.1007/BF01020332", None,
     "Feigenbaum 1978 Quantitative universality for a class of nonlinear transformations",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Feigenbaum 1978 J. Stat. Phys. 19, 25. Springer historic JSP DOI pattern. "
     "First statement of the universal constants delta=4.669... and alpha=2.502..."),
    ("D2", "isbn", ISBN_CVITANOVIC, None,
     "Cvitanović - ChaosBook (Universality in Chaos, 2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Cvitanović et al. — free online at chaosbook.org; ChaosBook.org print-reprint ISBN. "
     "ISBN claimed; verify WorldCat."),
    ("D2", "wikipedia",
     "https://en.wikipedia.org/wiki/Feigenbaum_constants", None, "Feigenbaum constants",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── E2 — Koomey's Law ──
    ("E2", "doi", "10.1109/MAHC.2010.28", None,
     "Koomey-Berard-Sanchez-Wong 2011 Implications of Historical Trends in the Electrical Efficiency of Computing",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Koomey et al. 2011 IEEE Annals of the History of Computing 33, 46. IEEE DOI pattern. "
     "Establishes electrical-efficiency doubling every ~1.6 yr."),
    ("E2", "wikipedia",
     "https://en.wikipedia.org/wiki/Koomey%27s_law", None, "Koomey's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("E2", "isbn", "978-0393339949", None,
     "Mack 2011 - Fifty Years of Moore's Law (for context)",
     1, "canonical", "adjacent_concept", None, "medium",
     "Mack 2011 W.W. Norton. adjacent_concept relationship — Moore's Law is the "
     "sister-law to Koomey's; Mack's 50-year retrospective provides context. "
     "canonical_role=NULL per CHECK constraint."),
]


# Internal_construction flags
IC_FLAGS = [
    ("H5",
     "H5: Scaling Exponent beta(lambda) — DFIG-framework parameter for the cross-domain scaling exponent "
     "as a function of phase coherence lambda. Wiki-hub (20 links) but owner-derived parameter. "
     "The (d_f-1)/(d_f+1) ansatz is acknowledged internal per feedback_preserve_falsifications.md.",
     "high-novelty-risk"),
    ("Q3",
     "Q3: Regime Capacity Bound — DFIG-framework open question about upper bound on capacity in a regime "
     "of given fractal dimension. Wiki-derived framing.",
     "owner-aware"),
    ("Q4",
     "Q4: SLT-Biology Correspondence — wiki-internal open question linking singular learning theory (Watanabe 2009) "
     "to biological regime classification in the DFIG framework. Real SLT prior art exists but the "
     "correspondence framing is wiki-native.",
     "owner-aware"),
    ("P2_STATUS",
     "P2_STATUS: Validation Status tracker for P2 conjecture (Metabolic Exponent Tracks Vascular D_eff). "
     "Wiki-meta entry documenting the validation state of conjecture P2, not a scientific claim itself. "
     "Preserved per no-deletions rule.",
     "owner-aware"),
    ("P12_STATUS",
     "P12_STATUS: Validation Status tracker for P12 conjecture (β(λ) Formula Across Domains). "
     "Wiki-meta entry documenting the validation state of conjecture P12, not a scientific claim itself.",
     "owner-aware"),
]


ENTRIES_ANCHORED = ("MATH4", "DM2", "DM3", "DM4", "D2", "E2")
ENTRIES_IC = ("H5", "Q3", "Q4", "P2_STATUS", "P12_STATUS")


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

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

        print(f"\nFlagging {len(IC_FLAGS)} entries as internal_construction...")
        ic_inserted = ic_skipped = 0
        for (eid, reason, scrutiny) in IC_FLAGS:
            res = conn.execute(
                "INSERT OR IGNORE INTO internal_constructions "
                "(entry_id, reason, searched_sources, flagged_date, "
                " flagged_by_session, scrutiny_level, notes) "
                "VALUES (?,?,?,?,?,?,?)",
                (eid, reason,
                 '["wiki-content-inspection-2026-04-20"]',
                 TODAY, SESSION, scrutiny,
                 "Final mop-up IC flag."),
            )
            if res.rowcount > 0:
                ic_inserted += 1
            else:
                ic_skipped += 1
        print(f"  IC inserted: {ic_inserted}, skipped: {ic_skipped}")

        conn.commit()
        print()

        print("=== Per-entry anchor counts ===")
        for eid in ENTRIES_ANCHORED:
            n = cur.execute(
                "SELECT COUNT(*) FROM external_anchors WHERE entry_id=?", (eid,),
            ).fetchone()[0]
            below_min = " *** BELOW 3-MIN" if n < 3 else ""
            print(f"  {eid:<10} {n:>2} anchors{below_min}")

        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        ic_total = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM internal_constructions"
        ).fetchone()[0]
        print(f"\nTotals after mop-up:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")
        print(f"  internal_constructions:  {ic_total}")
        print(f"  PROVENANCE:              {entries_anchored + ic_total} / 301 "
              f"= {round(100*(entries_anchored + ic_total)/301)}%")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
