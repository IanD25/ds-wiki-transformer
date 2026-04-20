"""
Close remaining unanchored conjectures — 2026-04-20

Per 2026-04-18 handover Section "14 conjectures remaining unanchored":
  P6, P7  -> 'contradicts' (own-test-falsified, debuts the relationship type)
  P17, P23 -> reuse cosmology-batch anchors (Farrah/Cadoni/Amendola)
  P9, P22 -> IC (flagged reclassify-to-Q, not yet migrated)
  P12, P14, P16 -> IC (archive bucket; untestable without data)

After this batch, only GT05 remains unprovenanced (deferred per owner clarification).

Run: python3 scripts/migrations/close_remaining_conjectures_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-close-conjectures-2026-04-20"


# Anchors via `contradicts` (debuts) and reused cosmology DOIs
ANCHORS = [
    # ── P6: D_eff Decreases Monotonically Under Coarse-Graining (FALSIFIED) ──
    # Per M0 + handover: contradicted by own Phase 1 tests. Use `contradicts` relationship.
    ("P6", "doi", "10.1126/science.1238723", None,
     "Machta-Chachra-Transtrum-Sethna 2013 Parameter Space Compression Underlies Emergent Theories",
     1, "canonical", "contradicts", None, "high",
     "Machta 2013 demonstrates RG-style parameter compression with monotonic d_eff "
     "decrease under coarse-graining for sloppy models. P6 generalizes this to FIM "
     "rank, but Phase 1 tests on Ising/Potts indicate non-monotonic behavior in some "
     "regimes — partially contradicting P6. DEBUTS the `contradicts` relationship."),

    # ── P7: Fractal Dimension Converges with Fisher Rank (FALSIFIED) ──
    # Per M0 + Phase 1 tests: failed.
    ("P7", "doi", "10.1126/science.1238723", None,
     "Machta-Chachra-Transtrum-Sethna 2013",
     1, "canonical", "contradicts", None, "high",
     "Same Machta 2013 paper. P7 proposed d_f from a graph-fractal-dimension proxy "
     "would converge with Fisher rank d_eff under RG flow. Phase 1 tests on Ising "
     "did not show convergence. relationship=contradicts."),

    # ── P17: Cosmological Coupling Exponent Equals D_eff ──
    # Reuses cosmology-cluster Farrah/Cadoni/Amendola. M0 Speculative status.
    ("P17", "doi", "10.3847/2041-8213/acb704", None,
     "Farrah et al. 2023 Observational Evidence for Cosmological Coupling of Black Holes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "P17 wiki claim: cosmological coupling exponent k = D_eff. Anchored to "
     "Farrah-Croker 2023 source paper. M0 Speculative — current GWTC-3 gives 2-sigma "
     "upper bound k<2.1. Reused from cosmology cluster (GT11)."),
    ("P17", "arxiv", "2306.11588", None,
     "Cadoni et al. 2023 Cosmological coupling of nonsingular black holes",
     3, "preprint-evolving", "cites", None, "medium",
     "Cadoni 2023 JCAP 11, 007 — verified in M0 Fifth Addendum. Their KS analysis on "
     "Farrah elliptical sample prefers k=3 over k=1, contesting their own k=1 prediction. "
     "Tier-3 = cites."),
    ("P17", "wikipedia",
     "https://en.wikipedia.org/wiki/Black_hole_thermodynamics", None,
     "Black hole thermodynamics (cosmological coupling background)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No dedicated Wikipedia article on cosmological coupling. No oldid."),

    # ── P23: Horizon Formation as Bekenstein-Saturation Phase Transition ──
    # Inherits contested GT11 per handover.
    ("P23", "doi", "10.1103/PhysRevD.7.2333", None,
     "Bekenstein 1973 Black Holes and Entropy",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "P23 frames horizon formation as a Bekenstein-saturation phase transition. "
     "Anchored to Bekenstein 1973 (defines BH entropy). Reused from HB02. "
     "M0 Speculative — inherits GT11 contested status."),
    ("P23", "doi", "10.3847/2041-8213/acb704", None,
     "Farrah et al. 2023 (cosmological coupling background)",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Farrah 2023 cosmological coupling claim is the empirical context for P23's "
     "phase-transition framing. Reused from GT11/P17."),
    ("P23", "wikipedia",
     "https://en.wikipedia.org/wiki/Black_hole_thermodynamics", None,
     "Black hole thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Reused. No oldid."),
]


# IC flags for the remaining conjectures
IC_FLAGS = [
    ("P9",
     "P9: Holographic Dictionary Has LWE-Equivalent Complexity. Per 2026-04-18 handover, "
     "flagged for reclassify-to-Q-series (the actual claim is more naturally an open question "
     "than a conjecture). Tagged IC pending the Q-series migration. M0 Speculative.",
     "needs-review"),
    ("P12",
     "P12: beta(lambda) Formula Predicts Scaling Exponents Cross-Domain. Per 2026-04-18 handover, "
     "in archive bucket — untestable without data. Tied to wiki's H5 (DFIG) parameter program. "
     "M0 Speculative.",
     "needs-review"),
    ("P14",
     "P14: Branching Variance Predicts Exponent Gap (beta_MMR - beta_BMR). Per 2026-04-18 handover, "
     "in archive bucket — untestable without data. Tied to wiki's metabolic-scaling program. "
     "M0 Speculative.",
     "needs-review"),
    ("P16",
     "P16: RLCT = d_f at Regime Transitions; Discontinuous Jump at Metamorphosis. Per 2026-04-18 "
     "handover, in archive bucket. RLCT = real-log-canonical-threshold from Watanabe singular "
     "learning theory; the equation to d_f is wiki-derived. M0 Speculative.",
     "needs-review"),
    ("P22",
     "P22: Irreversible Lockout Trichotomy for Spontaneous Symmetry Breaking. Per 2026-04-18 "
     "handover, flagged for reclassify-to-Q-series. Tagged IC pending Q-series migration.",
     "needs-review"),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

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

        print(f"\nFlagging {len(IC_FLAGS)} conjectures as internal_construction...")
        ic_inserted = ic_skipped = 0
        for (eid, reason, scrutiny) in IC_FLAGS:
            res = conn.execute(
                "INSERT OR IGNORE INTO internal_constructions "
                "(entry_id, reason, searched_sources, flagged_date, "
                " flagged_by_session, scrutiny_level, notes) "
                "VALUES (?,?,?,?,?,?,?)",
                (eid, reason,
                 '["m0-handover-2026-04-18", "wiki-content-inspection-2026-04-20"]',
                 TODAY, SESSION, scrutiny,
                 "Conjecture in archive/reclassify bucket per 2026-04-18 handover."),
            )
            if res.rowcount > 0:
                ic_inserted += 1
            else:
                ic_skipped += 1
        print(f"  IC inserted: {ic_inserted}, skipped: {ic_skipped}")

        conn.commit()
        print()

        # Final summary
        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        ic_total = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM internal_constructions"
        ).fetchone()[0]

        print(f"=== Final state ===")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")
        print(f"  internal_constructions:  {ic_total}")
        print(f"  PROVENANCE:              {entries_anchored + ic_total} / 301 "
              f"= {round(100*(entries_anchored + ic_total)/301)}%")

        # Relationship-type distribution
        print(f"\n=== Relationship-type distribution (incl. `contradicts` debut) ===")
        for r in cur.execute(
            "SELECT relationship, COUNT(*) FROM external_anchors GROUP BY relationship ORDER BY 2 DESC"
        ):
            print(f"  {r[0]:25} {r[1]}")

        # What's still unprovenanced
        cur.execute("ATTACH DATABASE 'data/ds_wiki.db' AS ds")
        print(f"\n=== Still unprovenanced ===")
        for r in cur.execute("""
            SELECT 'entry' AS kind, e.id, e.title FROM ds.entries e
            WHERE e.id NOT IN (SELECT entry_id FROM external_anchors)
              AND e.id NOT IN (SELECT entry_id FROM internal_constructions)
            UNION
            SELECT 'conj' AS kind, c.id, c.title FROM ds.conjectures c
            WHERE c.id NOT IN (SELECT entry_id FROM external_anchors)
              AND c.id NOT IN (SELECT entry_id FROM internal_constructions)
        """):
            print(f"  [{r[0]:<5}] {r[1]:<10} {r[2][:60]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
