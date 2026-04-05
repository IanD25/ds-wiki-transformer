"""
Update P17 critical_gaps and phase1_results with 2024-2025 research findings.
Update GT03 DS Cross-References to include GT10.
Add link GT03 -> GT10.

Idempotent: checks if 'Amendola' is already in P17 critical_gaps and
if 'GT10' is already in GT03 cross-references before appending.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

P17_GAP_APPEND = (
    "\n\n--- 2026-04-04 research update ---\n"
    "5. GW MERGER RATE REJECTION: Amendola et al. (MNRAS 528, 2377, 2024) showed GW "
    "merger rates reject k = 3 beyond 5 sigma — predicted rates exceed LIGO-Virgo-KAGRA "
    "observations by two orders of magnitude.\n"
    "6. GAIA BH CONSTRAINTS: Andrae et al. (A&A, 2023) found Gaia BH1/BH2 have only "
    "6.9% combined probability of forming above the TOV limit under k = 3.\n"
    "7. CADONI k = 1 PREDICTION: Cadoni et al. (JCAP, 2023) showed generic nonsingular "
    "GR interiors give k = 1, not k = 3. The k = 3 case requires very specific "
    "(gravastar-like) interiors.\n"
    "8. JWST HIGH-z TENSION: Lei et al. (Science China Physics, 2024) found JWST "
    "NIRSpec-resolved AGNs at z ~ 4.5-7 in tension with k = 3 at 95% CL."
)

P17_RESULTS_APPEND = (
    "\n\n--- 2026-04-04 research update ---\n"
    "SUPPORTING (2024-2025):\n"
    "- DESI DR2 (March 2025): Strengthened evolving dark energy signal to 3.9 sigma.\n"
    "- CCBH model recovers H0 = 69.94 +/- 0.81 km/s/Mpc, reducing Hubble tension to "
    "2.7 sigma (Croker et al. 2024).\n"
    "- CCBH framework yields positive neutrino masses (~0.106 eV summed) where standard "
    "Lambda-CDM + DESI pushes to unphysical negative values.\n"
    "- DESI official blog (Aug 2025): three independent observational signatures.\n\n"
    "CHALLENGING (2024-2025):\n"
    "- GW merger rates reject k = 3 at >5 sigma (Amendola 2024).\n"
    "- Gaia BH1/BH2: 6.9% probability of forming above TOV under k = 3.\n"
    "- LVK O4: k < 2.1 (standard), k < 1.1 (CCBH-corrected) at 2 sigma.\n"
    "- Cadoni et al.: generic nonsingular GR gives k = 1, not k = 3.\n"
    "- JWST AGN tension at 95% CL.\n\n"
    "STATUS: Empirical case strengthened by DESI but severely challenged by GW and "
    "stellar-mass BH constraints. The hypothesis survives for k ~ 1 but the dark "
    "energy connection (requiring k = 3) is under heavy pressure."
)

GT03_XREF_APPEND = (
    " GT10 (Jacobson Entanglement Equilibrium — quantum-information upgrade of "
    "Jacobson 1995; the condition delta_S_EE|_V = 0 for maximal vacuum entanglement "
    "entropy at fixed volume is the microscopic foundation for Padmanabhan's "
    "holographic equipartition N_sur = N_bulk)."
)


def update(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # --- Update P17 critical_gaps ---
    row = cur.execute("SELECT critical_gaps FROM conjectures WHERE id = 'P17'").fetchone()
    if row and row[0]:
        if "Amendola" in row[0]:
            print("  P17 critical_gaps: already updated — skipping.")
        else:
            new_gaps = row[0] + P17_GAP_APPEND
            cur.execute("UPDATE conjectures SET critical_gaps = ? WHERE id = 'P17'", (new_gaps,))
            print("  P17 critical_gaps: appended 2024-2025 research tensions.")
    else:
        cur.execute("UPDATE conjectures SET critical_gaps = ? WHERE id = 'P17'", (P17_GAP_APPEND.strip(),))
        print("  P17 critical_gaps: set (was empty).")

    # --- Update P17 phase1_results ---
    row = cur.execute("SELECT phase1_results FROM conjectures WHERE id = 'P17'").fetchone()
    if row and row[0]:
        if "Amendola" in row[0]:
            print("  P17 phase1_results: already updated — skipping.")
        else:
            new_results = row[0] + P17_RESULTS_APPEND
            cur.execute("UPDATE conjectures SET phase1_results = ? WHERE id = 'P17'", (new_results,))
            print("  P17 phase1_results: appended 2024-2025 research update.")
    else:
        cur.execute("UPDATE conjectures SET phase1_results = ? WHERE id = 'P17'", (P17_RESULTS_APPEND.strip(),))
        print("  P17 phase1_results: set (was empty).")

    # --- Update GT03 DS Cross-References ---
    row = cur.execute(
        "SELECT content FROM sections WHERE entry_id = 'GT03' AND section_name = 'DS Cross-References'"
    ).fetchone()
    if row and row[0]:
        if "GT10" in row[0]:
            print("  GT03 DS Cross-References: already contains GT10 — skipping.")
        else:
            new_content = row[0] + GT03_XREF_APPEND
            cur.execute(
                "UPDATE sections SET content = ? WHERE entry_id = 'GT03' AND section_name = 'DS Cross-References'",
                (new_content,)
            )
            print("  GT03 DS Cross-References: appended GT10 reference.")
    else:
        print("  GT03 DS Cross-References: section not found — skipping.")

    # --- Add link GT03 -> GT10 ---
    labels = {r[0]: r[1] for r in cur.execute("SELECT id, title FROM entries")}
    gt03_label = labels.get("GT03", "GT03")
    gt10_label = labels.get("GT10", "GT10")

    cur.execute(
        "INSERT OR IGNORE INTO links "
        "(link_type, source_id, source_label, target_id, target_label, description, link_order, confidence_tier) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        ("couples to", "GT03", gt03_label, "GT10", gt10_label,
         "Padmanabhan's holographic equipartition N_sur = N_bulk is the global version "
         "of Jacobson 2016's local entanglement equilibrium delta_S_EE|_V = 0",
         0, "1.5")
    )
    print("  Link: GT03 -> GT10 (couples to)")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Updating P17 + GT03 in:\n  {SOURCE_DB}\n")
    update(SOURCE_DB)
