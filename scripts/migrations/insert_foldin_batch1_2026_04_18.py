"""
Insert Fold-In Batch 1 — P2 / P11 / P21 — 2026-04-18

First fold-in anchor batch — demonstrates the `reframing_of` restatement-
catcher pattern in live content.

  P2   Metabolic Exponent Tracks Vascular D_eff → reframing_of WBE 1997
  P11  Urban Scaling Tracks Network Spectral Dim → reframing_of Bettencourt 2007
  P21  Fisher-Rao Metric Universality → canonical_authority Chentsov/Amari

P2 and P11 demonstrate the fold-in pattern per M0 audit:
  - Conjecture claim is a restatement of established published work
  - `reframing_of` row points to the already-anchored canonical source
  - (Cross-entry source reuse: the WBE 1997 DOI anchored on C1 now also
    appears on P2 with a different relationship)

P21 is different — it's the one Established conjecture from M0 audit, and
its anchors are standard canonical_authority rows.

Run: python3 scripts/migrations/insert_foldin_batch1_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-foldin-batch1-2026-04-18"


ANCHORS = [
    # ==========================================================
    # P2 — Metabolic Exponent Tracks Vascular D_eff
    #      FOLD-IN → WBE 1997 (reframing_of)
    # ==========================================================
    ("P2", "doi", "10.1126/science.276.5309.122", None,
     "West, Brown & Enquist 1997 - A General Model for Allometric Scaling Laws",
     1, "canonical", "reframing_of", None, "high",
     "P2 claim 'α = D_eff/(D_eff+1) tracks vascular dimensionality' is a "
     "RESTATEMENT of West-Brown-Enquist 1997 Science. The functional "
     "form is WBE's; the 'tracks D_eff' framing is owner-constructed "
     "but contributes no novelty (per M0 audit 2026-04-08). Pattern-tag: "
     "restatement-in-new-vocabulary. This SAME DOI is already anchored "
     "on C1 Kleiber's Law as axiomatic_foundation — cross-entry source "
     "reuse with different relationship types."),

    ("P2", "doi", "10.3733/hilg.v06n11p315", None,
     "Kleiber 1932 - Body size and metabolism",
     1, "canonical", "cites", None, "high",
     "P2 cites the Kleiber 1932 empirical scaling observation that WBE "
     "1997 later explained. Same DOI anchored on C1 as progenitor; "
     "here it's a `cites` relationship from the conjecture."),

    # ==========================================================
    # P11 — Urban Scaling Tracks Network Spectral Dimension
    #       FOLD-IN → Bettencourt 2007 (reframing_of)
    # ==========================================================
    ("P11", "doi", "10.1073/pnas.0610172104", None,
     "Bettencourt, Lobo, Helbing, Kühnert, West 2007 - Urban Scaling",
     1, "canonical", "reframing_of", None, "high",
     "P11 claim 'urban scaling tracks network spectral dimension via "
     "D/(D+1) functional form' is a RESTATEMENT framing Bettencourt-"
     "West 2007 urban-scaling law through the DFIG network-dimension "
     "vocabulary. The empirical scaling phenomenon is Bettencourt 2007; "
     "the spectral-dimension mechanism is owner-constructed and "
     "untested. Pattern-tag: restatement-in-new-vocabulary (functional "
     "form) + untestable-without-owner-data (for the spectral-dim "
     "mechanism claim). Same DOI anchored on C2 as progenitor."),

    ("P11", "isbn", "978-0143110903", None,
     "West - Scale (2018 paperback)",
     1, "canonical", "cites", None, "high",
     "P11 cites West 2018 as the popular-synthesis volume covering "
     "both metabolic and urban scaling. Cross-entry reuse (already on "
     "C1 and C2 as comprehensive_survey)."),

    # ==========================================================
    # P21 — Fisher-Rao Metric Universality (Established per M0)
    # ==========================================================
    ("P21", "isbn", "978-0821845028", None,
     "Chentsov - Statistical Decision Rules and Optimal Inference (AMS 1982)",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Chentsov 1972 (Russian), 1982 AMS English translation (Trans. "
     "Math. Monographs Vol. 53). Contains the Fisher-Rao uniqueness "
     "theorem: Fisher-Rao is the UNIQUE (up to scale) Riemannian metric "
     "on a statistical manifold invariant under sufficient statistics. "
     "This is the axiomatic_foundation for P21's Established claim. "
     "Verified via WebSearch 2026-04-18."),

    ("P21", "doi", "10.1007/978-1-4612-5056-2", None,
     "Amari 1985 - Differential-Geometrical Methods in Statistics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Amari 1985 Springer LNS 28. ISBN 978-0387960562; DOI "
     "10.1007/978-1-4612-5056-2. The canonical textbook on information "
     "geometry — systematic presentation of Fisher-Rao, alpha-"
     "connections, and dual-flat structures. Verified via CrossRef."),

    ("P21", "isbn", "978-0821843048", None,
     "Amari & Nagaoka - Methods of Information Geometry (AMS 2000)",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Amari & Nagaoka 2000, Translations of Mathematical Monographs "
     "Vol. 191, AMS. Extended modern treatment including applications "
     "to statistics, neural networks, and physics. Fills "
     "comprehensive_survey for P21."),

    ("P21", "wikipedia",
     "https://en.wikipedia.org/wiki/Fisher_information_metric",
     "1346655653",
     "Fisher information metric",
     2, "active-literature", "canonical_authority", "living_reference",
     "high",
     "Wikipedia article verified via WebFetch 2026-04-18. Chentsov "
     "uniqueness theorem present; Amari 1985 + Amari-Nagaoka 2000 "
     "cited."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("P2", "P11", "P21"):
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
        for eid in ("P2", "P11", "P21"):
            cur.execute("""
                SELECT relationship, canonical_role, COUNT(*)
                FROM external_anchors
                WHERE entry_id=?
                GROUP BY relationship, canonical_role
                ORDER BY relationship, canonical_role
            """, (eid,))
            rels = cur.fetchall()
            rel_str = ", ".join(
                f"{r[0]}{'/' + r[1] if r[1] else ''}({r[2]})"
                for r in rels
            )
            print(f"  {eid}: {rel_str}")

        # Updated co-citation graph
        print("\n=== Updated co-citation graph (sources appearing on >=2 entries) ===")
        for r in cur.execute("""
            SELECT source, identifier, COUNT(DISTINCT entry_id) as n,
                   GROUP_CONCAT(DISTINCT entry_id) as entries,
                   MAX(title) as title,
                   COUNT(DISTINCT relationship) as rel_variety
            FROM external_anchors
            GROUP BY source, identifier
            HAVING n > 1
            ORDER BY n DESC, source
        """):
            rel_note = f" [{r[5]} relationship types]" if r[5] > 1 else ""
            print(f"  {r[2]}× — {r[4][:55]}{rel_note}")
            print(f"      entries: {r[3]}")

        # Global totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries = cur.fetchone()[0]
        cur.execute(
            "SELECT COUNT(*) FROM external_anchors WHERE relationship=?",
            ("reframing_of",),
        )
        reframings = cur.fetchone()[0]
        print(f"\nGlobal totals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries} / 300")
        print(f"  reframing_of anchors:      {reframings}  (restatement-catcher active)")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
