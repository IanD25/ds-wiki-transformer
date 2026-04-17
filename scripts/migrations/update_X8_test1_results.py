"""
Update X8 with Test 1 empirical results from AlphaEntropy session.

Key findings:
  1. σ(t) is NOT redundant with D_eff (lag-0 correlation = 0.035)
  2. σ is LAGGING, not leading (peak correlation at lag -10, D_eff leads σ)
  3. σ is a characterization measure, not a predictive signal
  4. Total Σ discriminates episode types; peak σ is partially stable
  5. Episode rankings: 2025 Stress highest total Σ, 2007-03 highest peak σ
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB


def run(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ------------------------------------------------------------------
    # Overview — add Test 1 results paragraph, correct the framing
    # ------------------------------------------------------------------
    old_overview_end = (
        "IMPORTANT: σ(t) is a proxy motivated by dimensional analogy with thermodynamic "
        "entropy production — it is NOT a formally derived entropy production rate from "
        "a statistical model of the return-generating process. The formal connection "
        "requires computing the true Fisher Information on the return distribution and "
        "deriving the Onsager-type dissipation from it. This has not been done."
    )

    new_overview_end = (
        "IMPORTANT: σ(t) is a proxy motivated by dimensional analogy with thermodynamic "
        "entropy production — it is NOT a formally derived entropy production rate from "
        "a statistical model of the return-generating process. The formal connection "
        "requires computing the true Fisher Information on the return distribution and "
        "deriving the Onsager-type dissipation from it. This has not been done.\n\n"
        "TEST 1 RESULTS (2026-03-29): σ(t) carries independent information from D_eff "
        "(lag-0 correlation = 0.035 — nearly uncorrelated contemporaneously). However, "
        "σ is a LAGGING indicator: peak cross-correlation occurs at lag −10 (D_eff leads "
        "σ by ~10 days). σ does not provide early warning of crises. Its value is as a "
        "retrospective characterization of crisis intensity — total Σ (integrated "
        "dissipation) discriminates episode types and is stable across smoothing spans "
        "for the largest episodes. σ(t) is a diagnostic measure, not a trading signal."
    )

    row = cur.execute(
        "SELECT content FROM sections WHERE entry_id='X8' AND section_name='Overview'"
    ).fetchone()
    if row and old_overview_end in row[0]:
        new_content = row[0].replace(old_overview_end, new_overview_end)
        cur.execute(
            "UPDATE sections SET content=? WHERE entry_id='X8' AND section_name='Overview'",
            (new_content,)
        )
        print("  Updated X8/Overview — added Test 1 results")
    else:
        print("  SKIP X8/Overview — fragment not found")

    # ------------------------------------------------------------------
    # Three Crisis Archetypes — add empirical episode table
    # ------------------------------------------------------------------
    old_archetypes_end = (
        "STATUS: Archetypes identified from normalized phase-space chart.\n"
        "Formal k-means clustering with statistical validation is pending."
    )

    new_archetypes_end = (
        "STATUS: Archetypes identified from normalized phase-space chart.\n"
        "Formal k-means clustering with statistical validation is pending.\n\n"
        "EMPIRICAL EPISODE TABLE (Test 1, 2026-03-29, EMA span=5):\n\n"
        "  Episode          | Peak σ    | Total Σ  | Character\n"
        "  -----------------+-----------+----------+---------------------------\n"
        "  2025 Stress      | 0.00263   | 0.0131   | Highest total Σ — sustained high dissipation\n"
        "  2007-03 (pre-GFC)| 0.00424   | 0.0112   | Highest peak σ — sharp initial shock\n"
        "  Euro Crisis      | 0.00133   | 0.0058   | Moderate peak, long duration\n"
        "  Rate Shock 2022  | 0.00062   | 0.0062   | Low peak, very long — classic Slow Grind\n"
        "  COVID Mar 2020   | 0.00058   | 0.0057   | Moderate everything\n"
        "  GFC 2008–2009    | 0.00072   | 0.0030   | Surprisingly low (only 61 days detected)\n\n"
        "GFC NOTE: The low GFC σ values likely reflect episode boundary detection — the\n"
        "adaptive percentile thresholds identify a 61-day window, but the full GFC\n"
        "unfolded over ~18 months. The episode detection may be splitting the GFC into\n"
        "sub-episodes. Total Σ is sensitive to episode boundary definition.\n\n"
        "RANKING STABILITY: 11 of 21 detected episodes have stable peak σ rankings\n"
        "(±2 rank) across EMA spans 3/5/10/21. The top 3 (2007-03, Euro Crisis,\n"
        "2025 Stress) are consistently ranked highest. Mid-range episodes shuffle\n"
        "significantly — GFC moves from rank 9 to 6, COVID from rank 11 to 4.\n"
        "This means peak σ is reliable for discriminating major vs. minor episodes\n"
        "but not for fine-grained ordering of moderate crises."
    )

    row = cur.execute(
        "SELECT content FROM sections WHERE entry_id='X8' AND section_name='Three Crisis Archetypes'"
    ).fetchone()
    if row and old_archetypes_end in row[0]:
        new_content = row[0].replace(old_archetypes_end, new_archetypes_end)
        cur.execute(
            "UPDATE sections SET content=? WHERE entry_id='X8' AND section_name='Three Crisis Archetypes'",
            (new_content,)
        )
        print("  Updated X8/Three Crisis Archetypes — added empirical table")
    else:
        print("  SKIP X8/Three Crisis Archetypes — fragment not found")

    # ------------------------------------------------------------------
    # Geodesic Test — update status to reflect Test 1 findings
    # ------------------------------------------------------------------
    old_geodesic_end = (
        "STATUS: Trajectory data exists in AlphaEntropy (normalized phase-space\n"
        "chart, crisis overlays). Path integral computation has not been done.\n"
        "This is the highest-priority quantitative test connecting X8 to P21."
    )

    new_geodesic_end = (
        "STATUS (updated 2026-03-29): Trajectory data exists. σ(t) time series\n"
        "computed (Test 1). σ is confirmed to carry independent information from\n"
        "D_eff (lag-0 corr = 0.035) but is a lagging measure — it characterizes\n"
        "dissipation after the fact, not before. This means the geodesic test\n"
        "remains the primary test of P21: it asks whether the PATHS are\n"
        "near-geodesic, which is a geometric question about the trajectory shape,\n"
        "not a predictive question about timing. The σ(t) lag result does not\n"
        "affect the geodesic test's validity.\n\n"
        "Path integral computation (Test 3: riemannian_distance on daily\n"
        "correlation matrices, efficiency ratio η = d_geodesic / L_actual)\n"
        "has not yet been done. This remains the highest-priority quantitative\n"
        "test connecting X8 to P21."
    )

    row = cur.execute(
        "SELECT content FROM sections WHERE entry_id='X8' AND section_name='Geodesic Test'"
    ).fetchone()
    if row and old_geodesic_end in row[0]:
        new_content = row[0].replace(old_geodesic_end, new_geodesic_end)
        cur.execute(
            "UPDATE sections SET content=? WHERE entry_id='X8' AND section_name='Geodesic Test'",
            (new_content,)
        )
        print("  Updated X8/Geodesic Test — updated status with Test 1 findings")
    else:
        print("  SKIP X8/Geodesic Test — fragment not found")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Updating X8 with Test 1 results in:\n  {SOURCE_DB}\n")
    run(SOURCE_DB)
