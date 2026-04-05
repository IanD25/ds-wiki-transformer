"""
Insert P23: Horizon Formation as Bekenstein-Saturation Phase Transition

Horizon formation is a gravitational phase transition where local information
density saturating S = A/4l_P^2 (Bekenstein bound) triggers transition from
decoupled phase (k = 0) to coupled phase (k > 0).

Also inserts gate G12.

Depends on: GT09 (Choptuik), GT10 (Jacobson 2015), GT11 (Farrah/Croker),
            HB01 (Bekenstein Bound), HB02 (BH entropy)

STATUS: State 1 (conjectured, not yet tested)
Inherits contested status from GT11.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

CONJECTURE = {
    "id": "P23",
    "title": "Horizon Formation as Bekenstein-Saturation Phase Transition",
    "claim": (
        "Horizon formation is a gravitational phase transition: local information "
        "density saturating $S = A / 4 l_P^2$ (Bekenstein bound, HB01) triggers a "
        "transition from a decoupled phase ($k = 0$, standard GR, mass constant) to a "
        "coupled phase ($k > 0$, mass evolves with cosmological scale factor as "
        "$M(a) = M(a_i)(a/a_i)^k$). The phase boundary is the horizon itself — the "
        "coincidence between the Schwarzschild radius and the Bekenstein saturation "
        "surface is not incidental but constitutive.\n\n"
        "**Predictions:**\n"
        "1. Universal $k$ within the coupled phase, regardless of BH mass. Phase "
        "identity is determined by horizon formation, not by object scale.\n"
        "2. Strict $k = 0$ for non-horizon objects. Neutron stars have $k = 0$ "
        "regardless of proximity to the TOV limit. Pulsar timing constraints are "
        "satisfied trivially.\n"
        "3. $k$ value determined by interior EoS. Vacuum energy interior ($P = -\\rho$) "
        "gives $k = 3$. Alternative interiors (Cadoni $k = 1$, Mathur fuzzballs) "
        "produce alternative $k$ values.\n"
        "4. Population-level smooth evolution from individual-level sharp transitions. "
        "BH formation is binary per object (horizon yes/no) but aggregate cosmological "
        "effects are smooth because formation events are distributed across cosmic "
        "history. DESI's evolving dark energy tracks the integrated BH formation rate, "
        "not a time-varying per-object $k$.\n\n"
        "Inherits $k = -3P/\\rho$ from Farrah/Croker (GT11, contested — see GT11 for "
        "full evidence and challenges including GW 5$\\sigma$ rejection of $k = 3$, "
        "Gaia BH constraints, and Cadoni $k = 1$ prediction).\n\n"
        "**Structural connection:** The horizon as phase boundary is a candidate "
        "instance of the constrained critical attractor class (STAT3). If horizons are "
        "CCAs, the transition is continuous by construction — individual-sharp plus "
        "population-smooth is the signature of a continuous transition at coarse scale."
    ),
    "depends_on": (
        "GT09 (Choptuik Critical Collapse — establishes that BH formation IS a phase "
        "transition with universal scaling; P23 extends from the formation threshold to "
        "the post-formation coupling regime). "
        "GT10 (Jacobson Entanglement Equilibrium — the Einstein equation as entanglement "
        "equilibrium provides the information-theoretic foundation for the claim that "
        "information saturation triggers a qualitative change). "
        "GT11 (Cosmological Coupling — provides the M(a) = M(a_i)(a/a_i)^k framework "
        "and the k = -3P/rho derivation; P23 inherits all of GT11's tensions). "
        "HB01 (Bekenstein Bound — S <= A/4l_P^2 is the saturation condition that defines "
        "the phase boundary; P23 claims this saturation IS the transition trigger). "
        "HB02 (Bekenstein-Hawking Entropy — S = A/4 exactly saturates the Bekenstein "
        "bound at the horizon; P23 identifies this saturation as the phase transition "
        "surface)."
    ),
    "would_confirm": (
        "1. Universal k across BH masses: LISA (SMBHs, 2030s) and Einstein Telescope "
        "(stellar-mass, 2030s) measure k for both populations and find the same value "
        "within uncertainties.\n"
        "2. DESI evolving dark energy is fully and quantitatively explained by the "
        "integrated BH formation rate (cosmic star formation history convolved with "
        "coupling), with no free parameters beyond the BH formation efficiency.\n"
        "3. A first-principles derivation is found connecting Bekenstein saturation "
        "(information density reaching S = A/4) to the Croker/Weiner coupling "
        "mechanism (mass evolution with scale factor), without assuming the interior "
        "EoS."
    ),
    "would_kill": (
        "1. k varies continuously with BH mass, redshift, or environment within the "
        "BH population — would show coupling is object-level, not phase-level.\n"
        "2. Neutron stars show detectable k > 0 at any proximity to the TOV limit — "
        "would show the transition is not at the horizon.\n"
        "3. Interior EoS is shown to have no effect on cosmological coupling strength "
        "— would break the k = -3P/rho link.\n"
        "4. GW constraints definitively reject ALL k > 0 for stellar-mass BHs "
        "(currently reject k = 3 at 5 sigma but k = 1 still viable — Amendola et al. "
        "MNRAS 528, 2024)."
    ),
    "critical_gaps": (
        "1. INHERITS ALL GT11 TENSIONS: GW 5-sigma rejection of k = 3 (Amendola 2024), "
        "Gaia BH1/BH2 6.9% probability (Andrae 2023), Cadoni k = 1 for generic "
        "nonsingular objects (Cadoni 2023), EP/momentum critique (Avelino 2023), "
        "JWST AGN 95% CL tension (Lei 2024).\n"
        "2. NO FIRST-PRINCIPLES DERIVATION: The hypothesis asserts that Bekenstein "
        "saturation triggers coupling, but no derivation connects the information "
        "density threshold to the Croker/Weiner mass evolution mechanism. The gap "
        "between 'information saturates at the horizon' and 'mass evolves with scale "
        "factor' is bridged by the hypothesis, not by calculation.\n"
        "3. CADONI k = 1 vs k = 3: Generic nonsingular GR interiors give k = 1 "
        "(Cadoni et al. JCAP 2023). Only very specific interiors (gravastar, pure de "
        "Sitter) give k = 3. The phase-transition framing works for any k > 0 but the "
        "dark energy connection requires k = 3 specifically.\n"
        "4. STELLAR-MASS vs SMBH TENSION: LVK constrains k < 1.1-2.1 for stellar-mass "
        "BBHs while Farrah measures k ~ 3 for SMBHs. If k is truly universal (Prediction "
        "1), this tension must resolve as systematics. If it doesn't, the phase-transition "
        "picture may need mass-dependent interiors."
    ),
    "phase1_results": None,
    "gate": "G12 (Critical)",
    "conjecture_order": 22,
    "three_state": "State 1",
}

SUMMARY = {
    "id": "P23",
    "claim_abbreviated": (
        "Horizon formation is a gravitational phase transition where Bekenstein "
        "saturation (S = A/4l_P^2) triggers cosmological coupling (k > 0). "
        "Inherits Farrah/Croker k = -3P/rho (contested)."
    ),
    "gate": "G12",
    "status": "Proposed",
}

GATE = {
    "id": "G12",
    "claim": "BH phase transition from Bekenstein saturation (P23)",
    "priority": "Critical",
    "blocking": (
        "Requires: (a) resolution of GW constraints on k — currently reject k=3 at "
        "5 sigma; (b) first-principles derivation connecting information saturation to "
        "Croker/Weiner coupling; (c) LISA/ET mass-dependent k measurement (2030s)"
    ),
}


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # --- Gate G12 ---
    if cur.execute("SELECT id FROM gates WHERE id = 'G12'").fetchone():
        print("  G12 already exists — skipping gate.")
    else:
        cur.execute(
            "INSERT INTO gates (id, claim, priority, blocking) VALUES (?, ?, ?, ?)",
            (GATE["id"], GATE["claim"], GATE["priority"], GATE["blocking"])
        )
        print(f"  Inserted gate: G12 — {GATE['claim']}")

    # --- Conjecture P23 ---
    if cur.execute("SELECT id FROM conjectures WHERE id = 'P23'").fetchone():
        print("  P23 already exists — skipping conjecture.")
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
    print(f"  Inserted conjecture: P23 — {CONJECTURE['title']}")

    cur.execute(
        "INSERT OR IGNORE INTO conjecture_summary (id, claim_abbreviated, gate, status) "
        "VALUES (?, ?, ?, ?)",
        (SUMMARY["id"], SUMMARY["claim_abbreviated"], SUMMARY["gate"], SUMMARY["status"]),
    )
    print(f"  Inserted conjecture_summary: P23")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Inserting P23 + G12 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
