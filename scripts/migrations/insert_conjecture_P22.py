"""
Insert P22: Irreversible Lockout Trichotomy for Spontaneous Symmetry Breaking

Generalized Sakharov conditions: every spontaneous symmetry breaking that
persists requires one of three lockout mechanisms (irreversible, energetic,
or topological). The degree of asymmetry scales with log(tau_process/tau_relax).

Derived from stress-testing the SDEO framework's claim that irreversibility
is the universal constraint. Survived 5 attacks; the open test is MBL
(many-body localization in the thermodynamic limit).
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

CONJECTURE = {
    "id": "P22",
    "title": "Irreversible Lockout Trichotomy for Spontaneous Symmetry Breaking",
    "claim": (
        "Every spontaneous symmetry breaking that persists for timescale "
        "$\\tau_{\\text{persist}}$ requires one of three lockout mechanisms:\n\n"
        "1. **Irreversible lockout:** $D_{KL}(P_{\\text{symmetric}} \\| P_{\\text{broken}})$ "
        "large enough that Crooks fluctuation back is suppressed: "
        "$\\tau_{\\text{persist}} \\sim \\exp(D_{KL})$. This is the information-theoretic "
        "mechanism — the broken state is so distinguishable from the symmetric state "
        "that thermal/quantum fluctuations cannot bridge the gap.\n\n"
        "2. **Energetic lockout:** $\\tau_{\\text{relax}} \\sim \\exp(\\sigma \\cdot L^{d-1})$ "
        "where $\\sigma$ is the interface energy density and $L$ is the system size. "
        "The energy barrier between symmetric and broken states diverges with system "
        "size, making the return path energetically inaccessible.\n\n"
        "3. **Topological lockout:** The symmetric and broken states are in distinct "
        "topological sectors, inaccessible to any sequence of local operations. "
        "$D_{KL} \\to \\infty$ for topological reasons, not dynamical ones.\n\n"
        "**Scaling prediction (generalized Kibble-Zurek):** The degree of asymmetry "
        "produced during a symmetry-breaking transition scales with "
        "$\\log(\\tau_{\\text{process}} / \\tau_{\\text{relax}})$. Fast quenches through "
        "the transition (adiabatic limit, $\\tau_{\\text{process}} \\ll \\tau_{\\text{relax}}$) "
        "produce maximal asymmetry. Slow transitions allow partial relaxation and "
        "produce less asymmetry.\n\n"
        "**No symmetry breaking is eternal** in a universe with finite entropy "
        "(de Sitter). Permanence is relative to $\\exp(D_{KL})$ or $\\exp(S_{dS})$, "
        "whichever is smaller.\n\n"
        "This conjecture generalizes Sakharov's three conditions for baryogenesis "
        "(baryon number violation + CP violation + departure from equilibrium) to ALL "
        "spontaneous symmetry breaking: ingredient (1) = the rules allow the broken "
        "state, ingredient (2) = a perturbation selects one vacuum, ingredient (3) = "
        "one of the three lockout mechanisms prevents return. The Sakharov conditions "
        "are the baryogenesis-specific instance."
    ),
    "depends_on": (
        "IT06 (Seifert Stochastic Thermodynamics — s_tot = log(P_F/P_R), the "
        "information-theoretic formulation of irreversibility that underlies mechanism 1). "
        "IT03 (KL Divergence — D_KL >= 0 is the mathematical identity that makes "
        "irreversible lockout possible; the non-negativity is the universal constraint). "
        "GT07 (Chirco Non-Equilibrium Spacetime Thermodynamics — gravitational entropy "
        "production sigma >= 0 is the gravitational instance of mechanism 1). "
        "HB09 (Generalised Second Law — dS_total/dt >= 0 is the integrated form of "
        "mechanism 1 for black hole processes). "
        "NE03 (Jarzynski Equality — the Crooks fluctuation probability P_return ~ "
        "exp(-D_KL) quantifies how suppressed the return to the symmetric state is). "
        "X8 (Financial Entropy Production — the tau_relax scaling law eta = f(log(dur/tau)) "
        "with r = -0.896 is the financial market instance of the scaling prediction). "
        "P21 (Fisher-Rao Universality — the tau_relax timescale that separates "
        "geodesic from non-geodesic behavior is the same tau_relax that separates "
        "permanent from transient symmetry breaking)."
    ),
    "would_confirm": (
        "1. The Kibble-Zurek scaling prediction (defect density ~ tau_quench^{-nu/(1+nu*z)}) "
        "is extended to a NEW system where it hasn't been tested and the predicted "
        "exponent matches. Candidate: quenched BEC through the superfluid transition.\n"
        "2. The tau_relax scaling law from AlphaEntropy (eta = f(log(dur/tau)), r = -0.896) "
        "is reproduced in a SECOND non-equilibrium system (ecological regime shifts, "
        "neural criticality, or another financial market) with a comparable r value.\n"
        "3. A spontaneous symmetry breaking event is found where the lockout mechanism "
        "can be cleanly classified as EXACTLY ONE of the three types, and the "
        "persistence timescale matches the predicted exp(D_KL), exp(sigma*L^{d-1}), "
        "or infinity (topological).\n"
        "4. The de Sitter permanence ceiling: a theoretical calculation shows that "
        "the electroweak vacuum's persistence time is bounded by exp(S_dS) ~ "
        "exp(10^122), and this bound is tighter than the energetic lockout bound "
        "exp(sigma*L^3) for the observable universe."
    ),
    "would_kill": (
        "1. **Many-body localization in the thermodynamic limit:** If MBL is proven to "
        "exist as a stable phase in infinite systems, it provides a fourth lockout "
        "mechanism (ergodicity breaking without energy barriers, topology, or "
        "irreversibility) that falsifies the trichotomy.\n"
        "2. **Permanent symmetry breaking with tau_process >> tau_relax and no explicit "
        "breaking term:** A system that maintains broken symmetry despite having ample "
        "time and energy to relax back to the symmetric state, without topological "
        "protection. This would mean the lockout is something other than the three "
        "mechanisms.\n"
        "3. **Kibble-Zurek violation:** A quench experiment where defect density does "
        "NOT scale with quench rate as predicted — asymmetry is independent of "
        "tau_process/tau_relax.\n"
        "4. **Equilibrium time crystal:** A system that spontaneously breaks continuous "
        "time-translation symmetry in thermal equilibrium, contradicting the "
        "Watanabe-Oshikawa no-go theorem. Would show that symmetry breaking can "
        "occur without any of the three lockout mechanisms."
    ),
    "critical_gaps": (
        "1. MBL STATUS (critical): Whether many-body localization survives the "
        "thermodynamic limit is an open question in condensed matter theory. "
        "The avalanche instability (De Roeck & Huveneers) suggests MBL is "
        "destroyed by rare thermal inclusions in infinite systems, which would "
        "preserve the trichotomy. But this is unresolved as of 2026.\n"
        "2. SCOPE BOUNDARY: The conjecture applies only to spontaneous symmetry "
        "breaking. Explicit symmetry breaking (asymmetric rules, e.g., CP "
        "violation in the CKM matrix) is outside scope — no lockout is needed "
        "because the symmetry was never there.\n"
        "3. TOPOLOGICAL MECHANISM FORMALIZATION: The claim that topological lockout "
        "is equivalent to D_KL -> infinity needs formalization. What is the "
        "correct information-theoretic distance between topological sectors? "
        "Is it D_KL, trace distance, or something else?\n"
        "4. SCALING PREDICTION PRECISION: The claim 'degree of asymmetry scales "
        "with log(tau_process/tau_relax)' is qualitative. The Kibble-Zurek "
        "exponent nu/(1+nu*z) is precise for specific universality classes. "
        "The conjecture should predict which universality class governs the "
        "scaling for each type of lockout mechanism.\n"
        "5. COSMOLOGICAL TEST: The baryogenesis instance requires calculating "
        "D_KL for the electroweak phase transition, which depends on the "
        "order of the transition (first-order vs. crossover in the Standard "
        "Model). Current lattice QCD results suggest the SM electroweak "
        "transition is a crossover, not first-order — which means the SM alone "
        "cannot produce the observed baryon asymmetry. BSM physics is needed, "
        "and the conjecture's prediction depends on which BSM model is correct."
    ),
    "phase1_results": (
        "STRESS TEST (2026-03-30):\n"
        "5 theoretical systems tested as potential falsifiers:\n\n"
        "1. Topological protection: Does not falsify. Forces expansion to "
        "include topological lockout as mechanism 3. Absorbed into the "
        "trichotomy.\n"
        "2. Many-body localization: OPEN. If MBL survives the thermodynamic "
        "limit, it falsifies the trichotomy by providing a 4th mechanism. "
        "If the avalanche instability kills MBL, the trichotomy holds.\n"
        "3. Discrete time crystals: SUPPORTS the conjecture. The "
        "Watanabe-Oshikawa no-go theorem for equilibrium time crystals "
        "IS the conjecture applied to time-translation symmetry.\n"
        "4. Vacuum without symmetric solution (SUSY): Does not falsify. "
        "Sharpens scope to spontaneous breaking only.\n"
        "5. De Sitter / Poincare recurrence: Does not falsify. "
        "Universalizes the claim — nothing is eternal, permanence scales "
        "with exp(D_KL), ceiling set by exp(S_dS) ~ exp(10^122).\n\n"
        "EMPIRICAL SUPPORT:\n"
        "- Kibble-Zurek mechanism: confirmed in superfluid helium, "
        "trapped ion chains, and BEC experiments. Defect density scales "
        "with quench rate as predicted.\n"
        "- AlphaEntropy tau_relax scaling: eta = f(log(dur/tau)), "
        "r = -0.896 across 21 crisis episodes (2003-2025). The financial "
        "market instance of the scaling prediction.\n"
        "- Sakharov conditions: the baryogenesis-specific instance. "
        "All three ingredients confirmed as necessary for matter "
        "dominance."
    ),
    "gate": None,
    "conjecture_order": 21,
    "three_state": "State 1",
}

SUMMARY = {
    "id": "P22",
    "claim_abbreviated": (
        "Permanent spontaneous symmetry breaking requires one of three lockout "
        "mechanisms (irreversible D_KL, energetic barrier, topological sector). "
        "Degree of asymmetry scales with log(tau_process/tau_relax). Generalizes "
        "Sakharov conditions."
    ),
    "gate": None,
    "status": "Proposed",
}


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if cur.execute("SELECT id FROM conjectures WHERE id = 'P22'").fetchone():
        print("P22 already exists — skipping.")
        conn.close()
        return

    cur.execute(
        """INSERT INTO conjectures
           (id, title, claim, depends_on, would_confirm, would_kill,
            critical_gaps, phase1_results, gate, conjecture_order, three_state)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            CONJECTURE["id"], CONJECTURE["title"], CONJECTURE["claim"],
            CONJECTURE["depends_on"], CONJECTURE["would_confirm"],
            CONJECTURE["would_kill"], CONJECTURE["critical_gaps"],
            CONJECTURE["phase1_results"], CONJECTURE["gate"],
            CONJECTURE["conjecture_order"], CONJECTURE["three_state"],
        ),
    )
    print(f"  Inserted conjecture: P22 — {CONJECTURE['title']}")

    cur.execute(
        "INSERT OR IGNORE INTO conjecture_summary (id, claim_abbreviated, gate, status) "
        "VALUES (?, ?, ?, ?)",
        (SUMMARY["id"], SUMMARY["claim_abbreviated"], SUMMARY["gate"], SUMMARY["status"]),
    )
    print(f"  Inserted conjecture_summary: P22")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Inserting P22 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
