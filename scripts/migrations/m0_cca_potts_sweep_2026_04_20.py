"""
m0_cca_potts_sweep_2026_04_20.py — Calibration updates after CCA Potts sweep.

Audit ref: gsw-cca-potts-sweep-phase-E-2026-04-20
Experiment doc: docs/CCA_POTTS_SWEEP_REPORT_2026.md

Inserts rows into wiki_history.db.confidence_calibration for:
  - CCA-1c   : outcome-dependent (Supported / Speculative / Falsified)
  - STAT3    : outcome-dependent
  - P5       : refined rationale (reduction-check confirms q=2 continuous reduction)
  - P6       : outcome-dependent

This script reads the outcome classification from
data/reports/cca_potts_sweep_2026/analysis/outcome_classification.json
to decide the final status for each entity.

Safe to re-run (uses INSERT OR IGNORE semantics via compound key).
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
import datetime

AUDIT_REF = "gsw-cca-potts-sweep-phase-E-2026-04-20"
CAL_DATE = "2026-04-20"
DB_PATH = Path("data/wiki_history.db")
OUTCOME_PATH = Path("data/reports/cca_potts_sweep_2026/analysis/outcome_classification.json")
REDUCTION_PATH = Path("data/reports/cca_potts_sweep_2026/analysis/reduction_check_table.csv")


def load_outcome():
    if not OUTCOME_PATH.exists():
        return None
    with OUTCOME_PATH.open() as f:
        return json.load(f)


def summarize_brown(outcome: dict | None) -> str:
    """Reduce per-q outcome to a single overall tag."""
    if outcome is None:
        return "UNKNOWN"
    summary = outcome.get("per_q_summary", {})
    # Count majority per q
    tags = []
    for q, s in summary.items():
        counts = s.get("tag_counts", {})
        # majority tag
        if counts:
            majority = max(counts.items(), key=lambda kv: kv[1])[0]
            tags.append((int(q), majority))
    a = sum(1 for _, t in tags if t == "A")
    b = sum(1 for _, t in tags if t == "B")
    c = sum(1 for _, t in tags if t == "C")
    if a >= 2:
        return "A"
    elif b >= 2:
        return "B"
    elif c >= 2:
        return "C"
    else:
        return "MIXED"


def resolve_cca_1c(overall_tag: str) -> tuple:
    """Returns (confidence, short_status, rationale). Based on 2026-04-20 sweep."""
    base = (
        "CCA Potts q=2,5,7,10 × L=16,24,32 × 5-replica sweep completed 2026-04-20 "
        "(540 Glauber-MC runs, 20k measurement sweeps each). "
        "Reduction-check at q=2 (continuous): R1 soft pass (ζ_∞ = 0.858 ± 0.009 vs "
        "ζ_theory = 0.875, 1.89σ) via FSS extrapolation in 1/L across L ∈ {16,24,32}. "
        "CCA's η_CCA at continuous T_c reduces to standard η_std via Vinayak 2014 "
        "Eq. 5. Brown comparison (q=5,7,10 first-order vs q=2 continuous): OUTCOME C "
        "per spec §4.2 — CCA observables discriminate first-order via different "
        "curve signatures than Brown's GTE. Specifically: (a) η_CCA peak locations "
        "track GTE peaks (both converge to T_c as q increases: q=5→1.02, q=7→1.01, "
        "q=10→1.01 at L=32); η_CCA jump magnitude at T_c is 2-5× below GTE's. "
        "(b) d_eff_CCA does NOT peak-track GTE (d_eff keeps growing through 1.10) "
        "but jump magnitude at T_c exceeds GTE's by factor 9-400× (q=10 L=32: "
        "d_eff jumps from 1.5 at T/Tc=0.99 to 370 at T/Tc=1.01). Neither observable "
        "alone meets spec A criterion. No phase-trapped replicas observed. "
    )
    if overall_tag == "A":
        return ("Supported",
                "First-order discrimination via pure 2-point observables tracks GTE",
                base + "CCA-1c promoted from Speculative to Supported.")
    elif overall_tag == "B":
        return ("Falsified",
                "First-order discrimination via pure 2-point observables FAILED",
                base + "CCA-1c falsified for first-order discrimination.")
    elif overall_tag == "C":
        return ("Speculative",
                "Discriminates differently than GTE (pending mechanism)",
                base + "CCA-1c remains Speculative with positive discriminative "
                "evidence. Per spec §4.4 conditions: reduction-check R1 passes (✓); "
                "outcome A not met (got C, ✗); ≥2/3 first-order q show partial "
                "agreement at peak-location level (✓). Sharpened follow-up: is "
                "d_eff_CCA's jump signature reducible to λ_1 ordering-mode collapse "
                "(textbook), or does it capture content beyond the standard "
                "susceptibility scaling? NOT pursued here per charter rule 8.")
    else:
        return ("Speculative", "Mixed/incomplete results",
                base + "Insufficient consistency for A/B/C classification; "
                "CCA-1c remains Speculative.")


def resolve_stat3(overall_tag: str) -> tuple:
    base = (
        "STAT3 CCA class 5-feature descriptive framework strengthened by 2026-04-20 "
        "Phase E Potts sweep. "
    )
    if overall_tag == "A":
        return ("Supported",
                "Narrow novelty: 2-point observables discriminate first-order Potts (peak tracks GTE)",
                base + "η_CCA peak-location convergence to T_c tracks Brown's GTE; "
                "d_eff_CCA jump magnitude exceeds GTE's. Complementary but A-level.")
    elif overall_tag == "B":
        return ("Speculative",
                "Predictive claim for first-order failed",
                base + "Discrimination via 2-point observables failed vs Brown's GTE.")
    elif overall_tag == "C":
        return ("Supported",
                "Framework empirically discriminates first-order Potts (via different signatures than GTE)",
                base + "Both CCA observables (d_eff, η) discriminate first-order vs "
                "continuous in 2D Potts q=5,7,10. η_CCA peak locations track GTE; "
                "d_eff_CCA jump magnitudes exceed GTE by 9-400×. Signatures are "
                "complementary rather than identical to Brown's GTE. STAT3 status "
                "strengthened from descriptive-only to empirically-validated as a "
                "transition-order discriminator in the 2D Potts q-family.")
    else:
        return ("Supported",
                "Descriptive framework; empirical validation partial",
                base + "Empirical validation partially complete after 2026-04-20 sweep.")


def resolve_p5() -> tuple:
    return (
        "Supported",
        "Refined rationale: reduction-check confirms q=2 continuous reduction to η_std",
        "P5 (Fisher rank = D_eff) status confirmed as application of sloppy-models "
        "framework. 2026-04-20 Phase E sweep demonstrates that at continuous T_c in 2D "
        "Potts (q=2), CCA's η_CCA (Zipf exponent of χ spectrum) reduces to the standard "
        "anomalous dimension η_std via Vinayak 2014 relation ζ = (d-η_std)/d within 2σ "
        "under FSS extrapolation. This clarifies P5's 'Fisher rank = d_eff' equivalence "
        "for classical continuous transitions: it is a re-expression of standard "
        "critical exponents, not a new observable.",
    )


def resolve_p6(overall_tag: str) -> tuple:
    if overall_tag == "A":
        return ("Supported",
                "Narrow novelty at first-order",
                "P6 gains narrow-novelty evidence at first-order from 2026-04-20 sweep.")
    else:
        return ("Speculative",
                "Unchanged; first-order novelty not demonstrated",
                "P6 status unchanged after 2026-04-20 Phase E sweep.")


def main():
    # Ensure table exists (created by prior m0 migrations; skip if missing)
    if not DB_PATH.exists():
        print(f"ERROR: {DB_PATH} does not exist")
        return 1
    conn = sqlite3.connect(str(DB_PATH))
    # Check table exists
    c = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='confidence_calibration'"
    ).fetchone()
    if not c:
        print("confidence_calibration table missing — creating (minimal schema)")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS confidence_calibration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                calibration_date TEXT NOT NULL,
                audit_ref TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                confidence TEXT NOT NULL,
                short_status TEXT,
                rationale TEXT,
                UNIQUE(entity_id, audit_ref)
            )
        """)
        conn.commit()

    # Resolve outcome
    outcome = load_outcome()
    tag = summarize_brown(outcome)
    print(f"Overall outcome tag: {tag}")

    updates = [
        ("CCA-1c", "conjecture", *resolve_cca_1c(tag)),
        ("STAT3", "entry", *resolve_stat3(tag)),
        ("P5", "conjecture", *resolve_p5()),
        ("P6", "conjecture", *resolve_p6(tag)),
    ]

    for entity_id, entity_type, confidence, short_status, rationale in updates:
        try:
            conn.execute("""
                INSERT INTO confidence_calibration
                  (entity_id, entity_type, confidence, calibration_date, audit_ref,
                   short_status, rationale)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (entity_id, entity_type, confidence, CAL_DATE, AUDIT_REF,
                  short_status, rationale))
            print(f"  + {entity_id} ({entity_type}): {confidence} "
                  f"({short_status[:60]}...)")
        except sqlite3.IntegrityError as e:
            print(f"  ! {entity_id}: {e} — skipping")

    conn.commit()
    # Verify
    rows = conn.execute(
        "SELECT entity_id, confidence, short_status FROM confidence_calibration "
        "WHERE audit_ref = ? ORDER BY entity_id",
        (AUDIT_REF,)
    ).fetchall()
    print(f"\nRows in DB for audit_ref={AUDIT_REF}:")
    for r in rows:
        print(f"  {r[0]:10s} {r[1]:15s} {r[2]}")
    conn.close()
    return 0


if __name__ == "__main__":
    exit(main())
