"""
insert_p17_conjecture.py — Add P17 (Cosmological Coupling d_eff = k) and gate G11.

Source: CCBH cluster Layer 1 analysis (data/rrp/ccbh/layer1_analysis.md)
Evidence: Farrah 2023, Cadoni et al., DESI 2025

Safe to re-run (INSERT OR IGNORE throughout).
"""

import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent.parent / "data" / "ds_wiki.db"


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # ── P17 conjecture ────────────────────────────────────────────────────
    cur.execute("""
        INSERT OR IGNORE INTO conjectures (
            id, title, claim, depends_on,
            would_confirm, would_kill, critical_gaps,
            phase1_results, gate, conjecture_order, three_state
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "P17",
        "Cosmological Coupling Exponent Equals D_eff",
        (
            "For systems cosmologically coupled to the Friedmann background, "
            "the Fisher Information effective dimension $D_{\\text{eff}}$ equals "
            "the cosmological coupling constant $k = -3w_{\\text{phys}}$. "
            "When the interior equation of state is vacuum energy ($w = -1$), "
            "$D_{\\text{eff}} = k = 3 = d_{\\text{spatial}}$. "
            "Black hole mass evolves as $m \\propto a^k$ where $a$ is the "
            "scale factor, and $k = 3$ implies the coupling has exactly three "
            "independent degrees of freedom — the spatial dimensions."
        ),
        (
            "[P5](entries/P5_fisher_rank.md), "
            "[G1](entries/G1_dimensional_redshift.md), "
            "[GV4](entries/GV4_hubble_lemaitre.md), "
            "[OmD](entries/OmD_scaling_operator.md)"
        ),
        (
            "P5 (Fisher Rank = D_eff) receives first cosmological-scale confirmation. "
            "P3 (running constants via Ω_D) gains a direct example: "
            "BH mass as a running constant encoding spatial dimension. "
            "P8 (power-law exponents encode D_eff) gains a textbook case: k = 3 in m ∝ a^k."
        ),
        (
            "Independent k measurement yields k ≠ 3 at >3σ from non-elliptical-galaxy channel, "
            "OR Fisher Information analysis of the matched metric yields D_eff ≠ k, "
            "OR BH interior equation of state confirmed w ≠ -1 with k still = 3 "
            "(would break the w ↔ k ↔ D_eff chain)."
        ),
        (
            "1. Independent k measurement from non-elliptical-galaxy channel (quasars, X-ray binaries). "
            "2. Formal derivation of D_eff = k from Fisher Information on the Cadoni matched metric. "
            "3. Test prediction: w ≠ -1 → k ≠ 3 → D_eff ≠ d_spatial (requires exotic BH interior models)."
        ),
        (
            "CCBH cluster pipeline analysis: PFD score 0.882. "
            "Tier-1 internal coherence 76.5% (MARGINAL — small graph). "
            "Tier-2 bridge quality: WELL-INTEGRATED (100% of entries bridge to DS Wiki, 0 noise). "
            "Structural alignment: mean polarity 0.925, 0 contested. "
            "Pipeline independently recovered all 6 manually identified conjecture targets "
            "(G1, OmD, X0_FIM_Regimes, H5, B5, P15) — 6/6 recall against human Layer 1 gate. "
            "Farrah 2023: k = 3.11 ± 1.19 (90% CL). "
            "DESI 2025: CCBH model with k = 3 improves cosmological fits."
        ),
        "G11 (Critical)",
        16,  # after P16
        "State 2",
    ))

    # ── G11 gate ──────────────────────────────────────────────────────────
    cur.execute("""
        INSERT OR IGNORE INTO gates (id, claim, priority, blocking) VALUES (?, ?, ?, ?)
    """, (
        "G11",
        "Cosmological coupling k measurement + D_eff derivation (P17)",
        "Critical",
        "Requires independent k measurement from non-elliptical channel AND formal Fisher derivation on matched metric",
    ))

    # ── P17 conjecture summary ────────────────────────────────────────────
    cur.execute("""
        INSERT OR IGNORE INTO conjecture_summary (id, claim_abbreviated, gate, status)
        VALUES (?, ?, ?, ?)
    """, (
        "P17",
        "Cosmological coupling $k = -3w = D_{\\text{eff}}$; vacuum energy → $k = 3 = d_{\\text{spatial}}$",
        "G11",
        "Phase 1 partial (CCBH cluster 6/6 recall; Farrah k = 3.11 ± 1.19)",
    ))

    conn.commit()

    # ── Verify ────────────────────────────────────────────────────────────
    row = cur.execute("SELECT id, title FROM conjectures WHERE id = 'P17'").fetchone()
    print(f"Conjecture: {row[0]} — {row[1]}")

    row = cur.execute("SELECT id, claim FROM gates WHERE id = 'G11'").fetchone()
    print(f"Gate: {row[0]} — {row[1]}")

    row = cur.execute("SELECT id, status FROM conjecture_summary WHERE id = 'P17'").fetchone()
    print(f"Summary: {row[0]} — {row[1]}")

    total = cur.execute("SELECT COUNT(*) FROM conjectures").fetchone()[0]
    print(f"\nTotal conjectures: {total}")

    conn.close()


if __name__ == "__main__":
    main()
