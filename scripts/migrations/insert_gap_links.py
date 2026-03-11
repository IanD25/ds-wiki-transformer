"""
insert_gap_links.py — Close easy structural gaps surfaced by GapAnalyzer + HypothesisGenerator.

18 links across three categories:
  1. β(λ) cluster  : H5, P12_STATUS, T8, T2, Q1, P2_STATUS  (7 links)
  2. Physics analogs: EM1↔GV3, GL2-5 gas law cluster, EM1↔EM4, EM12↔EM3  (9 links)
  3. Cross-type pairs: B5↔Q5, H2↔Q1  (2 links)

All INSERT OR IGNORE — safe to re-run.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ds_wiki.db")


LINKS = [
    # ── β(λ) cluster ─────────────────────────────────────────────────────────
    # H5 (Scaling Exponent β(λ)) is the foundational law for the whole cluster
    {
        "source_id": "H5", "source_label": "Scaling Exponent β(λ)",
        "target_id": "P12_STATUS", "target_label": "P12 Validation Status: β(λ) Formula Across Domains",
        "link_type": "tests",
        "description": (
            "P12 tracks whether β(λ) holds universally across domains; H5 is the formula "
            "under validation. The open question is directly testing H5's cross-domain claim."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "H5", "source_label": "Scaling Exponent β(λ)",
        "target_id": "T2", "target_label": "Metabolic Exponent–Dimensionality Correlation",
        "link_type": "analogous to",
        "description": (
            "T2 measures the empirical correlation between metabolic exponent and fractal "
            "dimensionality — the same structural relationship captured by the β(λ) formula in H5."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "P12_STATUS", "source_label": "P12 Validation Status: β(λ) Formula Across Domains",
        "target_id": "T8", "target_label": "β(λ) Cross-Domain Universality Test",
        "link_type": "tests",
        "description": (
            "T8 is the empirical test procedure for P12's open question. P12 asks whether β(λ) "
            "holds across domains; T8 operationalises that test with a concrete method."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "P12_STATUS", "source_label": "P12 Validation Status: β(λ) Formula Across Domains",
        "target_id": "T2", "target_label": "Metabolic Exponent–Dimensionality Correlation",
        "link_type": "couples to",
        "description": (
            "T2's correlation between metabolic exponent and dimensionality provides empirical "
            "grounding for P12's inquiry into whether β(λ) universally tracks dimension."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "T8", "source_label": "β(λ) Cross-Domain Universality Test",
        "target_id": "T2", "target_label": "Metabolic Exponent–Dimensionality Correlation",
        "link_type": "couples to",
        "description": (
            "T8 and T2 are complementary empirical tests of the same underlying conjecture: "
            "that β-type exponents co-vary with effective dimensionality across physical systems."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "H5", "source_label": "Scaling Exponent β(λ)",
        "target_id": "Q1", "target_label": "Q1: Fractal Dimension from Power-Law Exponent",
        "link_type": "couples to",
        "description": (
            "Q1 asks whether fractal dimension can be systematically derived from power-law "
            "exponents — exactly the question H5's β(λ) formula addresses by linking exponent "
            "to effective dimension λ."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "P2_STATUS", "source_label": "P2 Validation Status: Metabolic Exponent Tracks Vasculature",
        "target_id": "T2", "target_label": "Metabolic Exponent–Dimensionality Correlation",
        "link_type": "tests",
        "description": (
            "T2 is the direct empirical test for P2's conjecture that metabolic exponent tracks "
            "vasculature dimensionality; P2 is validated or falsified by the correlation T2 measures."
        ),
        "confidence_tier": "1.5",
    },

    # ── Physics analogs ───────────────────────────────────────────────────────
    {
        "source_id": "EM1", "source_label": "Gauss's Law for Electricity",
        "target_id": "GV3", "target_label": "Gauss's Law for Gravity",
        "link_type": "analogous to",
        "description": (
            "Both laws share identical mathematical form (∇·F = ρ/ε₀ vs ∇·g = −4πGρ) and "
            "express the same topological fact — inverse-square flux — for electricity and gravity "
            "respectively. A textbook structural analog."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "EM1", "source_label": "Gauss's Law for Electricity",
        "target_id": "EM4", "target_label": "Ampère–Maxwell Law",
        "link_type": "couples to",
        "description": (
            "Gauss's Law for Electricity and the Ampère–Maxwell Law are two of the four Maxwell "
            "equations; together they couple divergence of E with curl of B through the "
            "displacement current term."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "EM12", "source_label": "Ampère's Circuital Law",
        "target_id": "EM3", "target_label": "Faraday's Law of Induction",
        "link_type": "analogous to",
        "description": (
            "Ampère's Circuital Law and Faraday's Law are structurally dual Maxwell equations: "
            "Faraday links curl E to −∂B/∂t while Ampère links curl B to J + ∂E/∂t. "
            "They are the magnetic/electric mirrors of the same induction principle."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "GL2", "source_label": "Boyle's Law",
        "target_id": "GL3", "target_label": "Charles's Law",
        "link_type": "analogous to",
        "description": (
            "Boyle's Law (PV = const at fixed T) and Charles's Law (V/T = const at fixed P) are "
            "two complementary limiting cases of the ideal gas law, each isolating one pair of "
            "state variables."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "GL2", "source_label": "Boyle's Law",
        "target_id": "GL4", "target_label": "Gay-Lussac's Law",
        "link_type": "analogous to",
        "description": (
            "Boyle's Law (PV = const at fixed T) and Gay-Lussac's Law (P/T = const at fixed V) "
            "are complementary limiting cases of the ideal gas law."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "GL2", "source_label": "Boyle's Law",
        "target_id": "GL5", "target_label": "Avogadro's Law",
        "link_type": "analogous to",
        "description": (
            "Boyle's Law and Avogadro's Law are both special cases of the ideal gas law; "
            "Avogadro fixes P and T and varies n, while Boyle fixes T and n and varies P."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "GL3", "source_label": "Charles's Law",
        "target_id": "GL4", "target_label": "Gay-Lussac's Law",
        "link_type": "analogous to",
        "description": (
            "Charles's Law (V/T = const at fixed P) and Gay-Lussac's Law (P/T = const at fixed V) "
            "share the same T-proportionality structure and are related by the combined gas law."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "GL3", "source_label": "Charles's Law",
        "target_id": "GL5", "target_label": "Avogadro's Law",
        "link_type": "analogous to",
        "description": (
            "Charles's Law and Avogadro's Law are both volume-proportionality laws (V∝T and V∝n) "
            "derived from the ideal gas equation under different fixed-variable assumptions."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "GL4", "source_label": "Gay-Lussac's Law",
        "target_id": "GL5", "target_label": "Avogadro's Law",
        "link_type": "analogous to",
        "description": (
            "Gay-Lussac's Law and Avogadro's Law are both limiting cases of the ideal gas law, "
            "completing the full set of pairwise relationships among P, V, T, n."
        ),
        "confidence_tier": "1",
    },

    # ── Cross-type semantic pairs ─────────────────────────────────────────────
    {
        "source_id": "B5", "source_label": "B5: Landauer's Principle",
        "target_id": "Q5", "target_label": "Q5: Information Cost of Synchronization",
        "link_type": "predicts for",
        "description": (
            "Landauer's Principle sets the thermodynamic floor for erasing one bit (kT ln2). "
            "Q5 asks what the full information-theoretic cost of synchronization is — Landauer's "
            "bound is the minimal unit that Q5's answer must respect."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "H2", "source_label": "H2: Fractal Dimension (d_f)",
        "target_id": "Q1", "target_label": "Q1: Fractal Dimension from Power-Law Exponent",
        "link_type": "couples to",
        "description": (
            "H2 defines fractal dimension d_f as a measurable parameter; Q1 asks whether d_f "
            "can be systematically derived from power-law scaling exponents. H2 is the quantity "
            "Q1 is attempting to derive."
        ),
        "confidence_tier": "1.5",
    },
]


def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT MAX(link_order) FROM links")
    max_order = c.fetchone()[0] or 0
    order = max_order + 1

    inserted = 0
    skipped = 0
    for link in LINKS:
        # Check for existing link in either direction
        c.execute(
            "SELECT COUNT(*) FROM links WHERE (source_id=? AND target_id=?) OR (source_id=? AND target_id=?)",
            (link["source_id"], link["target_id"], link["target_id"], link["source_id"]),
        )
        if c.fetchone()[0] > 0:
            print(f"  SKIP  {link['source_id']} <-> {link['target_id']}")
            skipped += 1
            continue

        c.execute(
            """INSERT INTO links
               (link_type, source_id, source_label, target_id, target_label,
                description, link_order, confidence_tier)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                link["link_type"],
                link["source_id"], link["source_label"],
                link["target_id"], link["target_label"],
                link["description"],
                order,
                link["confidence_tier"],
            ),
        )
        print(f"  ADD   {link['source_id']} -> {link['target_id']} [{link['link_type']}] tier={link['confidence_tier']}")
        order += 1
        inserted += 1

    conn.commit()
    conn.close()

    print(f"\nDone: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    main()
