"""
insert_isolation_links.py — Connect the 12 previously isolated reference_law entries.

35 links across 12 entries, three confidence tiers:
  tier=1   : textbook-certain structural relationships (derives from, couples to)
  tier=1.5 : well-grounded analogical or functional relationships
  tier=2   : plausible cross-domain connections flagged in entry cross-references

All INSERT OR IGNORE — safe to re-run.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ds_wiki.db")


LINKS = [
    # ── CM7: Archimedes' Principle ────────────────────────────────────────────
    {
        "source_id": "CM7", "source_label": "Archimedes' Principle",
        "target_id": "FM1", "target_label": "Navier–Stokes Equations",
        "link_type": "derives from",
        "description": (
            "Archimedes' Principle is the hydrostatic limit of the Navier–Stokes equations: "
            "setting acceleration and viscosity to zero in NS yields ∇P = ρg, from which "
            "F_buoy = ρ_fluid·g·V_displaced follows directly."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "CM7", "source_label": "Archimedes' Principle",
        "target_id": "FM5", "target_label": "Stokes' Law",
        "link_type": "couples to",
        "description": (
            "Stokes' Law gives the viscous drag on a sphere moving through fluid; Archimedes' "
            "Principle gives the opposing buoyant force. Together they determine the terminal "
            "velocity of a submerged or settling particle."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "CM7", "source_label": "Archimedes' Principle",
        "target_id": "A1", "target_label": "A1: Square-Cube Law",
        "link_type": "couples to",
        "description": (
            "Buoyancy force scales as L³ (volume), as does the gravitational weight for a body "
            "of fixed density. The intersection of these two L³ scalings, mediated by Archimedes' "
            "Principle, sets the size limits for floating or neutrally buoyant organisms and "
            "structures — the core application of the Square-Cube Law to aquatic life."
        ),
        "confidence_tier": "1.5",
    },

    # ── DM2: Graham's Law ─────────────────────────────────────────────────────
    {
        "source_id": "DM2", "source_label": "Graham's Law",
        "target_id": "DM1", "target_label": "Fick's Laws of Diffusion",
        "link_type": "couples to",
        "description": (
            "Graham's Law gives the mass-dependent rate of effusion (r ∝ 1/√M); Fick's Laws "
            "give the concentration-gradient-driven flux once the gas has entered the medium. "
            "Both emerge from the same Maxwell-Boltzmann kinetic theory of gases."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "DM2", "source_label": "Graham's Law",
        "target_id": "GL1", "target_label": "Ideal Gas Law",
        "link_type": "derives from",
        "description": (
            "Graham's Law assumes kinetic energy equipartition (½mv² = 3/2 kT), the same "
            "assumption underlying the Ideal Gas Law. The r₁/r₂ = √(M₂/M₁) ratio follows "
            "from setting the mean kinetic energies equal."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "DM2", "source_label": "Graham's Law",
        "target_id": "DM4", "target_label": "Dalton's Law of Partial Pressures",
        "link_type": "couples to",
        "description": (
            "Dalton's Law gives the partial pressures of each gas in a mixture; Graham's Law "
            "acts on those partial pressures to predict the relative effusion rates of each "
            "component — the operational combination used in isotope separation (e.g., uranium "
            "enrichment)."
        ),
        "confidence_tier": "1.5",
    },

    # ── DM3: Lamm Equation ────────────────────────────────────────────────────
    {
        "source_id": "DM3", "source_label": "Lamm Equation",
        "target_id": "DM1", "target_label": "Fick's Laws of Diffusion",
        "link_type": "generalizes",
        "description": (
            "The Lamm Equation is a direct generalization of Fick's Second Law to include a "
            "sedimentation term: ∂c/∂t = D∇²c − sω²r(∂c/∂r). Setting s=0 recovers Fick's "
            "diffusion equation exactly."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "DM3", "source_label": "Lamm Equation",
        "target_id": "X2", "target_label": "X2: Information Geometry — Regime-First Instantiation",
        "link_type": "couples to",
        "description": (
            "The concentration profile produced by the Lamm Equation in analytical "
            "ultracentrifugation can be analyzed using the Fisher information metric — the "
            "curvature of the concentration gradient encodes the same geometric structure "
            "that X2 formalises in information space."
        ),
        "confidence_tier": "2",
    },

    # ── ES3: Archie's Law ─────────────────────────────────────────────────────
    {
        "source_id": "ES3", "source_label": "Archie's Law",
        "target_id": "H2", "target_label": "H2: Fractal Dimension ($d_f$)",
        "link_type": "couples to",
        "description": (
            "The cementation exponent m in Archie's Law (ρ_rock ∝ φ^−m) is a proxy for the "
            "pore network fractal dimension — higher m signals a more tortuous, fractal-like "
            "pore structure. m and d_f are directly correlated across rock types."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "ES3", "source_label": "Archie's Law",
        "target_id": "FM7", "target_label": "Darcy's Law",
        "link_type": "couples to",
        "description": (
            "Archie's Law and Darcy's Law are complementary characterisations of the same porous "
            "medium: Darcy gives the hydraulic permeability (fluid flow) and Archie gives the "
            "electrical formation factor (charge transport). Both exponents encode pore geometry."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "ES3", "source_label": "Archie's Law",
        "target_id": "C3", "target_label": "C3: Heavy-Tailed Distributions (Unified)",
        "link_type": "couples to",
        "description": (
            "Pore size distributions in many rocks follow heavy-tailed (power-law) statistics; "
            "these anomalous distributions produce non-integer Archie cementation exponents m "
            "that deviate from the idealized capillary model."
        ),
        "confidence_tier": "2",
    },

    # ── ES4: Buys Ballot's Law ────────────────────────────────────────────────
    {
        "source_id": "ES4", "source_label": "Buys Ballot's Law",
        "target_id": "CM1", "target_label": "Newton's Laws of Motion",
        "link_type": "derives from",
        "description": (
            "Buys Ballot's Law is a direct consequence of Newton's Second Law applied in a "
            "rotating reference frame: the Coriolis acceleration (−2Ω×v) deflects the pressure "
            "gradient-driven wind to produce the observed left/right low-pressure asymmetry."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "ES4", "source_label": "Buys Ballot's Law",
        "target_id": "CM2", "target_label": "Newton's Law of Universal Gravitation",
        "link_type": "couples to",
        "description": (
            "Geostrophic balance — the planetary-scale wind state that Buys Ballot's Law "
            "describes — requires balancing the Coriolis force against the horizontal pressure "
            "gradient that is ultimately driven by differential solar heating and gravitational "
            "stratification of the atmosphere."
        ),
        "confidence_tier": "1.5",
    },

    # ── ES7: Titius–Bode Law ──────────────────────────────────────────────────
    {
        "source_id": "ES7", "source_label": "Titius–Bode Law",
        "target_id": "CM5", "target_label": "Kepler's Third Law — Orbital Period Scaling",
        "link_type": "couples to",
        "description": (
            "Titius-Bode predicts the semi-major axis a_n of each orbit; Kepler's Third Law "
            "(T² ∝ a³) converts those predicted radii into orbital periods. Together they "
            "generate a predicted frequency table for the solar system."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "ES7", "source_label": "Titius–Bode Law",
        "target_id": "CM3", "target_label": "Kepler's First Law — Elliptical Orbits",
        "link_type": "couples to",
        "description": (
            "Kepler's First Law establishes that each orbit is an ellipse with the Sun at one "
            "focus, parametrised by its semi-major axis a. Titius-Bode is an empirical formula "
            "specifically for those a values — it predicts the input to Kepler's First Law."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "ES7", "source_label": "Titius–Bode Law",
        "target_id": "D2", "target_label": "D2: Feigenbaum Universality",
        "link_type": "analogous to",
        "description": (
            "The geometric 2ⁿ spacing of Titius-Bode may reflect orbital resonance cascades "
            "analogous to period-doubling in nonlinear dynamics (Feigenbaum). Both produce "
            "geometric sequences whose ratio converges to a universal constant — though the "
            "Titius-Bode connection remains contested."
        ),
        "confidence_tier": "2",
    },

    # ── KC3: Hammond–Leffler Postulate ────────────────────────────────────────
    {
        "source_id": "KC3", "source_label": "Hammond–Leffler Postulate",
        "target_id": "B2", "target_label": "B2: Arrhenius Equation",
        "link_type": "couples to",
        "description": (
            "Hammond-Leffler determines the position of the transition state relative to "
            "reactants/products from ΔG; the Arrhenius equation then converts that barrier "
            "height Ea into a reaction rate k = A·e^(−Ea/RT). They are the geometric and "
            "kinetic halves of the same transition state analysis."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "KC3", "source_label": "Hammond–Leffler Postulate",
        "target_id": "KC1", "target_label": "Le Chatelier's Principle",
        "link_type": "analogous to",
        "description": (
            "Both principles predict thermodynamic response direction without solving the full "
            "dynamics: Le Chatelier predicts which way equilibrium shifts; Hammond-Leffler "
            "predicts how the transition state geometry shifts for exo- vs. endothermic "
            "reactions. Structurally parallel heuristics."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "KC3", "source_label": "Hammond–Leffler Postulate",
        "target_id": "KC4", "target_label": "Hess's Law",
        "link_type": "couples to",
        "description": (
            "Hess's Law provides the overall ΔH (or ΔG) for a reaction from additive steps; "
            "Hammond-Leffler uses that ΔH/ΔG value to predict whether the transition state "
            "is early (reactant-like) or late (product-like). Hess gives the input; "
            "Hammond-Leffler gives the structural interpretation."
        ),
        "confidence_tier": "1.5",
    },

    # ── KC6: Raoult's Law ─────────────────────────────────────────────────────
    {
        "source_id": "KC6", "source_label": "Raoult's Law",
        "target_id": "KC7", "target_label": "Henry's Law",
        "link_type": "analogous to",
        "description": (
            "Raoult's Law and Henry's Law are the two complementary limits of solution "
            "thermodynamics: Raoult applies to the solvent (high mole fraction, P_A = x_A P°_A) "
            "and Henry applies to the dilute solute (low mole fraction, C = k_H·P). Together "
            "they partition the composition space of an ideal dilute solution."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "KC6", "source_label": "Raoult's Law",
        "target_id": "KC5", "target_label": "Gibbs–Helmholtz Equation",
        "link_type": "couples to",
        "description": (
            "Deviations from ideal Raoult behavior appear as non-zero excess ΔG_mix; the "
            "Gibbs-Helmholtz equation governs how that ΔG changes with temperature, giving "
            "the temperature dependence of azeotropes and activity coefficients."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "KC6", "source_label": "Raoult's Law",
        "target_id": "GL1", "target_label": "Ideal Gas Law",
        "link_type": "derives from",
        "description": (
            "Raoult's Law assumes ideal gas behavior in the vapor phase above the solution: "
            "P_A = x_A P°_A only holds if the vapor obeys PV = nRT. The Ideal Gas Law is the "
            "necessary boundary condition for the Raoult derivation."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "KC6", "source_label": "Raoult's Law",
        "target_id": "DM4", "target_label": "Dalton's Law of Partial Pressures",
        "link_type": "couples to",
        "description": (
            "The total vapor pressure above an ideal mixture is the sum of Raoult partial "
            "pressures (P_total = Σ x_i P°_i) — which is exactly Dalton's Law applied to the "
            "vapor phase. Dalton provides the additive superposition that makes Raoult's law "
            "composable across mixture components."
        ),
        "confidence_tier": "1.5",
    },

    # ── KC7: Henry's Law ──────────────────────────────────────────────────────
    {
        "source_id": "KC7", "source_label": "Henry's Law",
        "target_id": "F4", "target_label": "F4: Saturation Dynamics (Consolidated)",
        "link_type": "couples to",
        "description": (
            "Henry's Law describes the linear (dilute) regime of gas solubility: C = k_H·P. "
            "F4 (Saturation Dynamics) describes the Michaelis-Menten-like saturation that "
            "occurs at high concentrations. Henry's regime is the initial linear slope of the "
            "F4 saturation curve."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "KC7", "source_label": "Henry's Law",
        "target_id": "F5", "target_label": "F5: Oxygen Viability Corridor",
        "link_type": "predicts for",
        "description": (
            "Henry's Law directly governs oxygen's dissolved concentration in biological fluids "
            "as a function of ambient partial pressure. The bounds of the F5 oxygen viability "
            "corridor — minimum and maximum dissolved O₂ tolerated by organisms — are set by "
            "Henry's constant for O₂ at physiological temperatures."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "KC7", "source_label": "Henry's Law",
        "target_id": "DM1", "target_label": "Fick's Laws of Diffusion",
        "link_type": "couples to",
        "description": (
            "Henry's Law sets the dissolved gas concentration at the gas-liquid interface; "
            "Fick's Laws then govern the subsequent diffusive transport of that dissolved gas "
            "through the liquid. They are the equilibrium and kinetic partners of the same "
            "gas-dissolution process."
        ),
        "confidence_tier": "1.5",
    },

    # ── OP5: Malus's Law ──────────────────────────────────────────────────────
    {
        "source_id": "OP5", "source_label": "Malus's Law",
        "target_id": "OP4", "target_label": "Brewster's Angle",
        "link_type": "couples to",
        "description": (
            "Brewster's Angle is the incidence angle at which reflected light becomes fully "
            "linearly polarized; Malus's Law then governs how that polarized beam attenuates "
            "when it passes through a subsequent polarizer. Brewster produces the polarized "
            "input that Malus's Law acts on."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "OP5", "source_label": "Malus's Law",
        "target_id": "OP3", "target_label": "Snell's Law of Refraction",
        "link_type": "analogous to",
        "description": (
            "Both Malus's Law and Snell's Law describe angle-dependent transformations of "
            "optical amplitude at an interface: Snell governs direction (n₁sinθ₁ = n₂sinθ₂) "
            "and Malus governs transmitted intensity (I = I₀cos²θ). Both are consequences of "
            "the wave boundary conditions of electromagnetism."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "OP5", "source_label": "Malus's Law",
        "target_id": "OP6", "target_label": "Beer–Lambert Law",
        "link_type": "analogous to",
        "description": (
            "Malus's Law (I = I₀cos²θ) and Beer-Lambert (I = I₀e^−αℓ) are complementary "
            "optical intensity reduction laws: Malus reduces intensity through geometric "
            "polarization projection; Beer-Lambert reduces it through absorptive attenuation. "
            "Both are used together in quantitative spectropolarimetry."
        ),
        "confidence_tier": "1.5",
    },

    # ── OP6: Beer–Lambert Law ─────────────────────────────────────────────────
    {
        "source_id": "OP6", "source_label": "Beer–Lambert Law",
        "target_id": "B1", "target_label": "B1: Radioactive Decay (Gamow Tunneling)",
        "link_type": "analogous to",
        "description": (
            "Beer-Lambert (dI/dx = −αI) and Radioactive Decay (dN/dt = −λN) share identical "
            "mathematical structure: both are memoryless exponential processes where the rate "
            "of depletion is proportional to the current quantity. Beer-Lambert is the spatial "
            "analog of radioactive decay's temporal version."
        ),
        "confidence_tier": "1.5",
    },

    # ── QM5: Postulates of Special Relativity ─────────────────────────────────
    {
        "source_id": "QM5", "source_label": "Postulates of Special Relativity",
        "target_id": "GV1", "target_label": "General Relativity — Einstein Field Equations",
        "link_type": "couples to",
        "description": (
            "Special Relativity is the local flat-spacetime limit of General Relativity: "
            "in the absence of spacetime curvature (G_μν = 0), GR reduces exactly to SR. "
            "Conversely, SR provides the Minkowski metric that GR deforms, and the local "
            "Lorentz invariance that the equivalence principle requires."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "QM5", "source_label": "Postulates of Special Relativity",
        "target_id": "G1", "target_label": "G1: Dimensional Redshift Law",
        "link_type": "couples to",
        "description": (
            "SR's Lorentz invariance is valid only in D_eff = 4 Minkowski spacetime — the "
            "same dimensionality structure that G1's Dimensional Redshift Law operates in. "
            "G1's frequency scaling with effective dimension directly constrains the "
            "spacetime structure in which QM5's postulates hold."
        ),
        "confidence_tier": "1.5",
    },
    {
        "source_id": "QM5", "source_label": "Postulates of Special Relativity",
        "target_id": "EM4", "target_label": "Ampère–Maxwell Law",
        "link_type": "couples to",
        "description": (
            "Special Relativity was historically motivated by the need to reconcile Newtonian "
            "mechanics with Maxwell's equations: the Ampère-Maxwell Law implies a constant c "
            "independent of reference frame, which forced SR's second postulate. The two are "
            "mutually reinforcing — Maxwell's equations are Lorentz-covariant by construction."
        ),
        "confidence_tier": "1",
    },
    {
        "source_id": "QM5", "source_label": "Postulates of Special Relativity",
        "target_id": "QM1", "target_label": "Schrödinger Equation",
        "link_type": "generalizes",
        "description": (
            "The Schrödinger Equation is the non-relativistic (v ≪ c) limit of relativistic "
            "quantum mechanics: SR's energy-momentum relation E² = (pc)² + (mc²)² reduces to "
            "E = p²/2m in the low-velocity limit, which is the operator substitution that "
            "gives the Schrödinger equation. QM5 generalizes QM1 to relativistic speeds."
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
        print(
            f"  ADD   {link['source_id']} -> {link['target_id']} "
            f"[{link['link_type']}] tier={link['confidence_tier']}"
        )
        order += 1
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    main()
