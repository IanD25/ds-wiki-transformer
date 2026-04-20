"""
Insert Fold-In Batch 2 — P5 / P8 / P10 — 2026-04-18

Second fold-in anchor batch. Debuts the `null_hypothesis` relationship for
P10 — a honest relationship type for claims where the existing literature
serves as the null hypothesis against which the conjecture is tested.

  P5  Fisher Information Rank Equals D_eff        → reframing_of Machta 2013
  P8  Continuous Critical Exponents on Fractal-D  → reframing_of Gefen 1980 + JJK 2004
  P10 Hadron Charge Radii / Running ℏ             → null_hypothesis Pohl 2010 + std QCD

P5 and P8 continue the reframing_of pattern from batch 1 (P2/P11).
P10 is different — standard QCD is the null hypothesis, and the M0 audit
found P10 makes no unique predictions distinguishing it. The honest
relationship is null_hypothesis: "our claim has not yet distinguished
itself from this accepted framework."

Run: python3 scripts/migrations/insert_foldin_batch2_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-foldin-batch2-2026-04-18"


ANCHORS = [
    # ==========================================================
    # P5 — Fisher Information Rank Equals D_eff
    #      FOLD-IN → Sethna sloppy-models lineage
    # ==========================================================
    ("P5", "doi", "10.1126/science.1238723", None,
     "Machta, Chachra, Transtrum, Sethna 2013 - Parameter Space Compression",
     1, "canonical", "reframing_of", None, "high",
     "Machta-Chachra-Transtrum-Sethna 2013, Science 342(6158), pp. "
     "604-607. Shows that coarse-graining compresses parameter space, "
     "leaving only a small number of stiff directions — EXACTLY the "
     "'D_eff = rank of FIM at scale ℓ' operational definition P5 "
     "proposes. Per M0 audit 2026-04-08: P5 is a re-parameterization "
     "of this sloppy-models program. Pattern-tag: restatement-in-new-"
     "vocabulary. Caveat per Quinn 2023: Ising at its microscopic "
     "parameterization is not sloppy — sloppiness emerges under "
     "coarse-graining (see P5 notes). Verified via CrossRef 2026-04-18."),

    ("P5", "doi", "10.1063/1.4918623", None,
     "Transtrum et al. 2015 - Perspective: Sloppiness and emergent theories",
     1, "canonical", "cites", None, "high",
     "Transtrum, Machta, Brown, Daniels, Myers, Sethna 2015, J. Chem. "
     "Phys. 143, 010901. Canonical Sethna-group perspective on "
     "sloppiness and emergent theories. Cited by P5 as the broader "
     "framing. DOI 10.1063/1.4918623."),

    # ==========================================================
    # P8 — Continuous Critical Exponent Interpolation on Fractional-D
    #      FOLD-IN → Gefen 1980 + JJK 2004 (dual reframing)
    # ==========================================================
    ("P8", "doi", "10.1103/physrevlett.45.855", None,
     "Gefen, Mandelbrot, Aharony 1980 - Critical Phenomena on Fractal Lattices",
     1, "canonical", "reframing_of", None, "high",
     "Gefen-Mandelbrot-Aharony 1980, PRL 45, pp. 855-858. The "
     "PROGENITOR of critical exponents on fractional-dimensional "
     "substrates. P8's continuous-interpolation claim is the textbook "
     "consequence of this work. Verified via CrossRef 2026-04-18."),

    ("P8", "doi", "10.1016/j.physa.2004.01.023", None,
     "Janke, Johnston, Kenna 2004 - Information geometry and phase transitions",
     1, "canonical", "reframing_of", None, "high",
     "JJK 2004, Physica A 336, pp. 181-186. Shows FIM scalar curvature "
     "distinguishes transition order (continuous vs first-order) — "
     "the FIM spectroscopy part of P8's claim. Phase-transition-"
     "distinction via FIM structure predates and subsumes the DFIG "
     "framing. Dual-progenitor with Gefen 1980: the geometric "
     "phenomenon (Gefen) + the FIM-spectroscopy treatment (JJK)."),

    # ==========================================================
    # P10 — Hadron Charge Radii Imply Running Effective ℏ
    #       NULL HYPOTHESIS → Pohl 2010 + standard QCD
    # ==========================================================
    ("P10", "doi", "10.1038/nature09250", None,
     "Pohl et al. 2010 - The size of the proton",
     1, "canonical", "null_hypothesis", None, "high",
     "Pohl et al. 2010, Nature 466(7303), pp. 213-216. Definitive "
     "muonic-hydrogen Lamb-shift measurement of proton RMS charge "
     "radius. The data P10 claims to explain via running-ℏ/GUP is "
     "accounted for by standard QCD + electroweak physics within "
     "existing uncertainties. Per M0 audit: P10 is 'one of several "
     "consistent interpretations with no unique predictions.' This "
     "paper serves as the null_hypothesis anchor — the standard-model "
     "explanation against which P10 would need to distinguish itself. "
     "**First null_hypothesis relationship anchor in the graph.**"),

    ("P10", "isbn", "978-0201503975", None,
     "Peskin & Schroeder - An Introduction to Quantum Field Theory",
     1, "canonical", "null_hypothesis", None, "medium",
     "Peskin-Schroeder 1995 Westview. Standard QFT textbook treating "
     "hadron form factors via standard QCD without any need for "
     "running ℏ. Serves as null_hypothesis textbook anchor. Confidence "
     "medium because the textbook is general and doesn't specifically "
     "address P10's alternative; it describes the STANDARD framework "
     "P10 departs from."),

    ("P10", "wikipedia",
     "https://en.wikipedia.org/wiki/Proton_radius_puzzle", None,
     "Proton radius puzzle",
     2, "active-literature", "adjacent_concept", None, "medium",
     "Wikipedia article on the proton-radius anomaly — the observed "
     "discrepancy between muonic-hydrogen and electronic-hydrogen "
     "measurements that P10 invokes. Adjacent_concept: the puzzle "
     "itself is real; P10 proposes running ℏ as a resolution, but "
     "standard-model explanations (systematic effects, lattice QCD "
     "corrections) are active. oldid not fetched this session; "
     "confidence medium."),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ("P5", "P8", "P10"):
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
        for eid in ("P5", "P8", "P10"):
            cur.execute("""
                SELECT relationship, canonical_role, COUNT(*)
                FROM external_anchors WHERE entry_id=?
                GROUP BY relationship, canonical_role
                ORDER BY relationship, canonical_role
            """, (eid,))
            rels = cur.fetchall()
            rel_str = ", ".join(
                f"{r[0]}{'/' + r[1] if r[1] else ''}({r[2]})"
                for r in rels
            )
            print(f"  {eid}: {rel_str}")

        # Full relationship-type distribution
        print("\n=== Relationship-type distribution (all anchors) ===")
        for r in cur.execute("""
            SELECT relationship, COUNT(*)
            FROM external_anchors
            GROUP BY relationship
            ORDER BY COUNT(*) DESC
        """):
            print(f"  {r[0]:25} {r[1]}")

        # Drift-pattern witnesses via reframing_of anchors
        print("\n=== Restatement-catcher active rows (reframing_of) ===")
        for r in cur.execute("""
            SELECT entry_id, source, identifier, title
            FROM external_anchors
            WHERE relationship='reframing_of'
            ORDER BY entry_id
        """):
            print(f"  {r[0]:6} → {r[3][:55]}")

        # Global totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries = cur.fetchone()[0]
        print(f"\nGlobal totals:")
        print(f"  external_anchors rows:     {total}")
        print(f"  entries with any anchor:   {entries} / 300")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
