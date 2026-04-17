"""
Insert P18: Fisher-Rao Metric Universality

This conjecture formalises the discovery from the pillar similarity analysis
(snap_20260327_134808): IT08 (Fisher-Rao Metric) appeared as the dominant hub
of the five-pillar structure, connecting IT ↔ BR ↔ RG ↔ GT at similarities
≥ 0.81 — a discovery from the data, not a prediction from the spec.

The claim: the Fisher-Rao metric is not merely analogous across these physical
contexts, but is literally the same mathematical object (Chentsov uniqueness)
appearing in four physical domains because all four are, under the hood,
spaces of probability distributions.

State 1: proposed conjecture, not yet formally tested. The critical gap is
the quantum Fisher metric case (Bianconi/GT04), where the classical Chentsov
uniqueness theorem does not directly apply.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

CONJECTURE = {
    "id": "P21",
    "title": "Fisher-Rao Metric Universality",
    "claim": (
        "The Fisher-Rao metric $g_{ij} = \\mathbb{E}[\\partial_i \\log p \\cdot \\partial_j \\log p]$ "
        "is the unique Riemannian structure on any space of probability distributions "
        "(Chentsov 1982, Amari 1985). Consequently, wherever physical dynamics can be described "
        "as evolution on a space of probability distributions, the Fisher-Rao metric appears as "
        "the natural geometry — not by analogy but by mathematical identity under a coordinate map. "
        "The DS Wiki pillar analysis identifies four independent physical domains where this holds: "
        "(1) thermodynamic state space, where Fisher-Rao equals the Ruppeiner metric on Gibbs "
        "distributions (BR04 $\\leftrightarrow$ IT08, sim 0.880) — a known proven identity; "
        "(2) renormalisation group flow on coupling space, where Fisher-Rao is the metric of RG "
        "flow (IT08 $\\leftrightarrow$ RG06, sim 0.855); "
        "(3) emergent gravitational dynamics from quantum state space, where the Hessian of "
        "quantum relative entropy — the quantum Fisher metric — generates spacetime curvature "
        "(IT08 $\\leftrightarrow$ GT04, sim 0.853); "
        "(4) non-equilibrium thermodynamics, where minimum-dissipation paths between states "
        "are geodesics on the Fisher-Rao manifold (IT06 $\\leftrightarrow$ IT08). "
        "The conjecture is that these four instances are not independent coincidences but "
        "consequences of Chentsov's uniqueness theorem: any physical state space that admits "
        "a statistical interpretation carries the Fisher-Rao metric as its natural geometry, "
        "and therefore thermodynamics, RG flow, and gravity share a common information-geometric "
        "foundation expressible as different coordinate representations of the same metric."
    ),
    "depends_on": (
        "IT08 (Fisher-Rao Metric — the central hub entry whose four physical appearances motivate "
        "the conjecture). "
        "BR04 (Ruppeiner Metric — proven identity with Fisher-Rao on Gibbs distributions; "
        "the strongest empirical anchor). "
        "RG06 (Cotler-Rezchikov — RG flow as Wasserstein gradient flow on Fisher-Rao manifold). "
        "GT04 (Bianconi Gravity — quantum Fisher information Hessian as emergent spacetime metric). "
        "IT06 (Seifert Stochastic Thermodynamics — minimum-dissipation paths as Fisher-Rao "
        "geodesics). "
        "IT05 (Fisher Information — the scalar quantity whose matrix generalisation is IT08)."
    ),
    "would_confirm": (
        "1. A formal proof that the Ruppeiner metric (BR04), the Cotler-Rezchikov RG metric (RG06), "
        "and the Bianconi gravitational metric (GT04) are all pullbacks of the same Fisher-Rao "
        "metric under coordinate maps on the space of probability distributions — this would "
        "upgrade from 'same mathematical object in different contexts' to 'proven coordinate "
        "equivalences of a single metric'. "
        "2. A new physical domain exhibiting Fisher-Rao that was not in the training set — "
        "e.g., the natural metric of quantum error correction codes, or of causal inference — "
        "that the conjecture predicts in advance (not post-hoc). "
        "3. Experimental confirmation that optimal thermodynamic protocols between equilibrium "
        "states follow Fisher-Rao geodesics, with dissipation scaling as (geodesic distance)² / τ "
        "as predicted by Seifert's framework (IT06)."
    ),
    "would_kill": (
        "A physical system whose state space admits a full statistical interpretation but whose "
        "natural geometry is demonstrably not the Fisher-Rao metric — violating Chentsov uniqueness "
        "in a physical context. "
        "OR: a proof that two of the four physical instances use Fisher-Rao metrics with different "
        "curvatures or signatures that cannot be related by any coordinate transformation on the "
        "respective state spaces (ruling out 'same metric, different coordinates'). "
        "OR: the Bianconi quantum Fisher metric (GT04) is shown to belong to the Petz family of "
        "quantum Fisher metrics but not to reduce to the classical Fisher-Rao in the classical "
        "limit — this would break the GT04 arm of the conjecture while leaving the others intact."
    ),
    "critical_gaps": (
        "1. QUANTUM FISHER METRIC GAP: The Bianconi result (GT04) derives gravity from quantum "
        "Fisher information on quantum state space. Quantum states are density matrices, not "
        "classical probability distributions, and Chentsov's uniqueness theorem does not "
        "directly apply. Petz (1996) showed there is a family of quantum Fisher metrics; "
        "establishing which one Bianconi uses, and whether it reduces to the classical Fisher-Rao "
        "in the appropriate classical limit, is the critical gap. If the quantum Fisher metric "
        "used is the symmetric logarithmic derivative (SLD) Fisher metric — the most common "
        "quantum generalisation — then it does reduce to classical Fisher-Rao on commutative "
        "states, partially closing this gap. "
        "2. RG METRIC IDENTIFICATION: The Cotler-Rezchikov result (RG06) identifies RG flow as "
        "a gradient flow in a metric. Establishing that this metric is the Fisher-Rao metric "
        "pulled back to coupling space (rather than the Zamolodchikov metric, which is distinct "
        "for off-diagonal couplings) requires a calculation not yet in the wiki. "
        "3. SEIFERT EXPERIMENTAL GAP: The minimum-dissipation geodesic prediction (IT06 ↔ IT08) "
        "has been demonstrated in colloidal particle experiments (Sivak-Crooks 2012) but not yet "
        "at the precision needed to distinguish Fisher-Rao geodesics from other optimal protocols."
    ),
    "phase1_results": (
        "Discovery origin: pillar similarity analysis (snap_20260327_134808) revealed IT08 as "
        "the dominant hub of the five-pillar structure, appearing in 4 of the top 7 cross-pillar "
        "pairs. The cluster {IT08, BR04, RG06, GT04} has all pairwise similarities ≥ 0.81 — "
        "the highest-coherence cluster in the wiki. This was not predicted by the spec; it "
        "emerged from the embedding analysis. "
        "Similarity evidence: BR04↔IT08 = 0.880, IT08↔RG06 = 0.855, GT04↔IT08 = 0.853, "
        "BR04↔GT04 = 0.831, BR04↔RG06 = 0.812. "
        "The BR04↔IT08 connection (Ruppeiner = Fisher-Rao on Gibbs distributions) is a proven "
        "mathematical identity, not a conjecture — it anchors the empirical arm of P18. "
        "The RG06 and GT04 arms rest on published results (Cotler-Rezchikov 2023, Bianconi 2023) "
        "but the equivalence to classical Fisher-Rao has not been formally verified in those papers."
    ),
    "gate": None,
    "conjecture_order": 20,
    "three_state": "State 1",
}

SUMMARY = {
    "id": "P21",
    "claim_abbreviated": "Fisher-Rao metric is the unique natural geometry on all probability "
                         "state spaces; thermodynamics, RG flow, and gravity are coordinate "
                         "representations of the same metric",
    "gate": None,
    "status": "Proposed",
}


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Check if P18 already exists
    if cur.execute("SELECT id FROM conjectures WHERE id = 'P21'").fetchone():
        print("P18 already exists — skipping.")
        conn.close()
        return

    cur.execute(
        """INSERT INTO conjectures
           (id, title, claim, depends_on, would_confirm, would_kill,
            critical_gaps, phase1_results, gate, conjecture_order, three_state)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            CONJECTURE["id"],
            CONJECTURE["title"],
            CONJECTURE["claim"],
            CONJECTURE["depends_on"],
            CONJECTURE["would_confirm"],
            CONJECTURE["would_kill"],
            CONJECTURE["critical_gaps"],
            CONJECTURE["phase1_results"],
            CONJECTURE["gate"],
            CONJECTURE["conjecture_order"],
            CONJECTURE["three_state"],
        ),
    )
    print(f"  Inserted conjecture: P18 — {CONJECTURE['title']}")

    # conjecture_summary
    cur.execute(
        "INSERT OR IGNORE INTO conjecture_summary (id, claim_abbreviated, gate, status) "
        "VALUES (?, ?, ?, ?)",
        (SUMMARY["id"], SUMMARY["claim_abbreviated"], SUMMARY["gate"], SUMMARY["status"]),
    )
    print(f"  Inserted conjecture_summary: P18")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Inserting P18 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
