"""
insert_classified_links.py — Insert 58 LLM-classified tier-1.5/2 links
across TD, EM, CM, RD, FM, KC, QM, GV, CS, BIO, ES, AM, DM clusters.

All pairs confirmed against live cosine similarity at sim >= 0.78.
Safe to re-run — INSERT OR IGNORE guards against duplicates.

Run from project root:
    python3 scripts/insert_classified_links.py
    python3 scripts/insert_classified_links.py --dry-run
"""
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from config import SOURCE_DB

# ── Link definitions ──────────────────────────────────────────────────────────
# (source_id, source_label, target_id, target_label, link_type, description, confidence_tier, sim)
# Tier: 1 = sim ≥ 0.90; 1.5 = 0.85–0.89; 2 = < 0.85

LINKS = [

    # ── TD: Carnot cycle ──────────────────────────────────────────────────────
    ("TD13", "Carnot Efficiency and Thermodynamic Temperature",
     "TD8",  "Carnot's Theorem",
     "couples to",
     "Both express the Carnot cycle constraint: TD8 states η_max=1-T_c/T_h as an upper bound; "
     "TD13 defines thermodynamic temperature through the same Carnot ratio Q_c/Q_h=T_c/T_h.",
     "1",   0.9250),

    ("TD8",  "Carnot's Theorem",
     "TD3",  "Second Law of Thermodynamics",
     "derives from",
     "Carnot's Theorem—no engine surpasses a reversible one operating between the same reservoirs—"
     "is a theorem of the Second Law: violating it would require ΔS_universe < 0.",
     "1.5", 0.8267),

    ("TD13", "Carnot Efficiency and Thermodynamic Temperature",
     "TD3",  "Second Law of Thermodynamics",
     "derives from",
     "Carnot efficiency η=1-T_c/T_h < 1 follows from the Second Law: 100 % efficiency requires "
     "T_c=0 or infinite T_h, forbidden by ΔS_universe ≥ 0.",
     "2",   0.8062),

    # ── TD: Laws 1–4 interactions ─────────────────────────────────────────────
    ("TD2",  "First Law of Thermodynamics",
     "TD3",  "Second Law of Thermodynamics",
     "couples to",
     "Together the First and Second Laws fully constrain thermodynamic processes: the First Law "
     "sets the energy budget (ΔU=Q-W), the Second Law sets the entropy direction (ΔS≥0 for "
     "isolated systems).",
     "1.5", 0.8731),

    ("TD5",  "Fundamental Thermodynamic Relation",
     "TD2",  "First Law of Thermodynamics",
     "derives from",
     "The Fundamental Thermodynamic Relation dU=TdS-PdV follows from the First Law (dU=δQ-δW) "
     "combined with the Second Law reversibility condition δQ_rev=TdS and reversible work δW=PdV.",
     "1.5", 0.8576),

    ("TD5",  "Fundamental Thermodynamic Relation",
     "TD3",  "Second Law of Thermodynamics",
     "derives from",
     "The TdS term in dU=TdS-PdV encodes the Second Law: for irreversible processes dU≤TdS-PdV, "
     "equality holding only for reversible paths.",
     "2",   0.8288),

    ("TD1",  "Zeroth Law of Thermodynamics",
     "TD2",  "First Law of Thermodynamics",
     "couples to",
     "The Zeroth Law defines temperature as a transitive equilibrium property; the First Law uses "
     "temperature in heat transfer Q—temperature equality (Zeroth) is the prerequisite for heat "
     "flow to cease.",
     "1.5", 0.8431),

    ("TD1",  "Zeroth Law of Thermodynamics",
     "TD3",  "Second Law of Thermodynamics",
     "couples to",
     "The Zeroth Law defines thermal equilibrium as a state; the Second Law governs the approach "
     "to that state: entropy increases until temperature is uniform—precisely the Zeroth Law "
     "condition.",
     "1.5", 0.8525),

    # ── TD: Kopp / Dulong-Petit ───────────────────────────────────────────────
    ("TD11", "Kopp's Law",
     "TD12", "Dulong–Petit Law",
     "generalizes",
     "Kopp's Law generalizes Dulong–Petit to molecular compounds: molar heat capacity ≈ sum of "
     "atomic contributions, extending the per-atom 3R rule to multi-atom molecules.",
     "1.5", 0.8500),

    ("TD12", "Dulong–Petit Law",
     "TD4",  "Third Law of Thermodynamics",
     "tensions with",
     "Dulong–Petit predicts C_V=3R at all temperatures; the Third Law requires C_V→0 as T→0 "
     "(phonon freezing), exposing the classical approximation's breakdown at low temperature.",
     "2",   0.8225),

    # ── TD: Heat transfer ─────────────────────────────────────────────────────
    ("TD9",  "Newton's Law of Cooling",
     "TD10", "Fourier's Law of Heat Conduction",
     "analogous to",
     "Both are linear heat transfer laws: Fourier gives the microscopic conductive flux q=-k∇T; "
     "Newton's Cooling is the macroscopic integrated form dT/dt=-h(T-T_env), with h proportional "
     "to k for a slab.",
     "2",   0.7956),

    # ── EM: Gauss / Coulomb / Biot-Savart / Ampère ────────────────────────────
    ("EM1",  "Gauss's Law for Electricity",
     "EM6",  "Coulomb's Law",
     "generalizes",
     "Gauss's Law ∮E·dA=Q_enc/ε₀ generalizes Coulomb's Law: applying the divergence theorem to "
     "a spherical surface around a point charge recovers F=kq₁q₂/r² exactly; Gauss holds for "
     "any charge distribution.",
     "1.5", 0.8654),

    ("EM4",  "Ampère–Maxwell Law",
     "EM7",  "Biot–Savart Law",
     "generalizes",
     "Ampère–Maxwell Law (∇×B=μ₀J+μ₀ε₀∂E/∂t) generalizes Biot–Savart to time-varying fields; "
     "in the magnetostatic limit (∂E/∂t=0) the two are equivalent.",
     "2",   0.8306),

    ("EM8",  "Lenz's Law",
     "EM3",  "Faraday's Law of Induction",
     "derives from",
     "Lenz's Law (induced current opposes the flux change) is the physical interpretation of the "
     "minus sign in Faraday's Law (EMF=-dΦ/dt); it follows directly from EM3 plus energy "
     "conservation.",
     "1.5", 0.8893),

    ("EM11", "Joule's Law",
     "EM9",  "Ohm's Law",
     "derives from",
     "Joule's Law P=I²R=V²/R follows algebraically from Ohm's Law V=IR by substituting into "
     "the general power formula P=IV.",
     "1.5", 0.8728),

    ("EM10", "Kirchhoff's Laws",
     "EM9",  "Ohm's Law",
     "derives from",
     "Kirchhoff's Voltage Law (loop voltages sum to zero) is Ohm's Law applied around a closed "
     "path; Kirchhoff's Current Law follows from charge conservation (Continuity Equation EM5).",
     "2",   0.8337),

    ("EM3",  "Faraday's Law of Induction",
     "EM4",  "Ampère–Maxwell Law",
     "couples to",
     "Faraday and Ampère–Maxwell are the two curl Maxwell equations (∇×E and ∇×B); coupled via "
     "the EM wave equation—Faraday drives ∂B/∂t from curl E, Ampère–Maxwell drives ∂E/∂t from "
     "curl B.",
     "1.5", 0.8674),

    # ── EM / Gravity analogy ──────────────────────────────────────────────────
    ("EM6",  "Coulomb's Law",
     "GV3",  "Gauss's Law for Gravity",
     "analogous to",
     "Both are 1/r² laws expressed via Gauss's theorem: ∮E·dA=Q/ε₀ and ∮g·dA=-4πGM; "
     "mathematical structure identical with 1/ε₀ ↔ 4πG, Q ↔ M, sign reflecting "
     "both-sign vs attraction-only.",
     "2",   0.8337),

    ("GV3",  "Gauss's Law for Gravity",
     "CM2",  "Newton's Law of Universal Gravitation",
     "derives from",
     "Gauss's Law for Gravity ∮g·dA=-4πGM is derived from Newton's Law of Universal Gravitation "
     "by applying the divergence theorem to the 1/r² gravitational field; exact equivalence for "
     "static mass distributions.",
     "1.5", 0.8950),

    ("CM2",  "Newton's Law of Universal Gravitation",
     "EM6",  "Coulomb's Law",
     "analogous to",
     "Both are inverse-square-law forces: F=Gm₁m₂/r² and F=kq₁q₂/r²; same mathematical "
     "structure with G↔k, mass↔charge. Gravity is always attractive; electrostatic force can "
     "repel.",
     "2",   0.8306),

    # ── CM: Newton / Euler / Kepler ───────────────────────────────────────────
    ("CM1",  "Newton's Laws of Motion",
     "CM6",  "Euler's Laws of Motion (Rigid Body)",
     "generalizes",
     "Newton's Laws govern point masses; Euler's Laws extend them to rigid bodies by splitting "
     "into translational (F=ma for centre of mass) and rotational (M=Iα) equations. Euler's Laws "
     "reduce to Newton's for point particles.",
     "1.5", 0.8902),

    ("CM3",  "Kepler's First Law — Elliptical Orbits",
     "CM4",  "Kepler's Second Law — Equal Areas",
     "couples to",
     "Together Kepler's First and Second Laws define the orbit: First gives the elliptical "
     "geometry; Second (dA/dt=const) encodes angular momentum conservation and governs orbital "
     "speed at each position.",
     "1.5", 0.8467),

    ("CM3",  "Kepler's First Law — Elliptical Orbits",
     "CM5",  "Kepler's Third Law — Orbital Period Scaling",
     "couples to",
     "Kepler's First Law establishes the orbit as an ellipse with semi-major axis a; Third Law "
     "T²∝a³ relates that same a to the orbital period, completing the geometric plus dynamical "
     "description.",
     "2",   0.8227),

    ("CM4",  "Kepler's Second Law — Equal Areas",
     "CM5",  "Kepler's Third Law — Orbital Period Scaling",
     "couples to",
     "Second Law (angular momentum conservation) and Third Law (T²∝a³) together constrain orbit "
     "dynamics: area sweep rate gives L, and T²/a³=4π²/GM connects L to period.",
     "2",   0.8145),

    # ── AM: Least Action / Euler-Lagrange / Hamilton ──────────────────────────
    ("AM1",  "Principle of Least Action",
     "CM1",  "Newton's Laws of Motion",
     "generalizes",
     "Applying the Euler–Lagrange equations to the action integral with L=T-V recovers Newton's "
     "F=ma exactly; the Principle of Least Action is the deeper variational foundation of "
     "Newtonian mechanics.",
     "2",   0.8165),

    ("AM2",  "Euler–Lagrange Equations",
     "AM1",  "Principle of Least Action",
     "derives from",
     "The Euler–Lagrange equations δS/δq=0 are the necessary conditions for extremising the "
     "action integral S=∫L dt; derived directly from Hamilton's Principle by calculus of "
     "variations.",
     "1.5", 0.8455),

    ("AM3",  "Hamilton's Equations",
     "AM2",  "Euler–Lagrange Equations",
     "derives from",
     "Hamilton's equations ṗ=-∂H/∂q, q̇=∂H/∂p follow from the Euler–Lagrange equations by "
     "the Legendre transform H(q,p,t)=pq̇-L(q,q̇,t); the two formulations are equivalent.",
     "1.5", 0.8608),

    ("AM4",  "Hamilton–Jacobi Equation",
     "AM2",  "Euler–Lagrange Equations",
     "derives from",
     "The Hamilton–Jacobi Equation H(q,∂S/∂q,t)+∂S/∂t=0 can be derived from Euler–Lagrange "
     "equations via the canonical transformation generated by Hamilton's principal function S, "
     "bypassing the intermediate Hamiltonian formulation.",
     "2",   0.8238),

    # ── RD: Planck / Stefan-Boltzmann / de Broglie ───────────────────────────
    ("RD1",  "Planck's Law of Black-Body Radiation",
     "RD2",  "Stefan–Boltzmann Law",
     "generalizes",
     "Integrating Planck's spectral radiance B(ν,T)=2hν³/c²·1/(e^{hν/kT}-1) over all "
     "frequencies yields the Stefan–Boltzmann Law j=σT⁴; Planck's Law contains Stefan–Boltzmann "
     "as a special case.",
     "1.5", 0.8524),

    ("RD3",  "Planck–Einstein Relation",
     "RD1",  "Planck's Law of Black-Body Radiation",
     "couples to",
     "Planck's Law was derived by quantizing field energy using E=hν (Planck–Einstein Relation); "
     "RD3 is the quantization hypothesis at the core of RD1's derivation.",
     "1.5", 0.8552),

    ("QM4",  "de Broglie Wavelength",
     "RD3",  "Planck–Einstein Relation",
     "derives from",
     "de Broglie's λ=h/p follows from combining Einstein's E=pc (photon momentum) with "
     "Planck–Einstein E=hν=hc/λ, then extending to matter waves: λ=h/p for all particles.",
     "2",   0.8325),

    # ── FM: Navier-Stokes / Euler / Stokes / Faxén / Poiseuille / Bernoulli ──
    ("FM1",  "Navier–Stokes Equations",
     "FM3",  "Euler's Fluid Equations",
     "generalizes",
     "Setting viscosity μ=0 in the Navier–Stokes Equations recovers Euler's Fluid Equations "
     "exactly; NS adds the viscous stress tensor ∇·τ to Euler's inviscid momentum equation.",
     "1.5", 0.8954),

    ("FM1",  "Navier–Stokes Equations",
     "FM5",  "Stokes' Law",
     "generalizes",
     "In the low-Reynolds-number (Stokes) limit Re→0, NS reduces to the Stokes equations; "
     "integrating the Stokes drag on a sphere gives Stokes' Law F=6πηrv.",
     "2",   0.8348),

    ("FM6",  "Faxén's Law",
     "FM5",  "Stokes' Law",
     "generalizes",
     "Faxén's Laws generalise Stokes' Law to particles in non-uniform background flows: "
     "F=6πηa(u∞+a²/6 ∇²u∞-v) reduces to Stokes' Law F=6πηav when the background flow is "
     "uniform.",
     "1.5", 0.8757),

    ("FM4",  "Poiseuille's Law",
     "FM5",  "Stokes' Law",
     "analogous to",
     "Both are exact solutions to the Stokes (zero-inertia) limit of Navier–Stokes: Poiseuille "
     "gives flow rate Q=πr⁴ΔP/8ηL through a cylinder; Stokes gives drag F=6πηrv on a sphere.",
     "2",   0.8205),

    ("FM2",  "Bernoulli's Principle",
     "FM3",  "Euler's Fluid Equations",
     "derives from",
     "Bernoulli's Principle (P+½ρv²+ρgh=const) is obtained by integrating Euler's Fluid "
     "Equations along a streamline for steady, incompressible, inviscid flow—it is a first "
     "integral of the Euler equations.",
     "2",   0.7971),

    # ── KC: Stoichiometry triad ───────────────────────────────────────────────
    ("KC8",  "Law of Definite Composition",
     "KC9",  "Dalton's Law of Multiple Proportions",
     "couples to",
     "Together these are Dalton's two composition laws: Definite Composition establishes that a "
     "pure compound has a fixed mass ratio; Multiple Proportions shows that the same two elements "
     "can form different compounds with small-integer mass ratios.",
     "1.5", 0.8797),

    ("KC10", "Law of Reciprocal Proportions",
     "KC9",  "Dalton's Law of Multiple Proportions",
     "couples to",
     "Reciprocal Proportions (Richter): ratios in which elements combine with a third are related "
     "to ratios in which they combine with each other. With Multiple Proportions they form the "
     "stoichiometric triad of classical chemistry.",
     "1",   0.9019),

    ("KC10", "Law of Reciprocal Proportions",
     "KC8",  "Law of Definite Composition",
     "couples to",
     "Both are foundational stoichiometric laws: Definite Composition gives fixed-mass ratios "
     "within a compound; Reciprocal Proportions links combining ratios across compounds that "
     "share an element.",
     "1.5", 0.8799),

    # ── KC / TD: Gibbs-Helmholtz, Hess, Onsager ──────────────────────────────
    ("KC5",  "Gibbs–Helmholtz Equation",
     "TD5",  "Fundamental Thermodynamic Relation",
     "derives from",
     "Gibbs–Helmholtz (∂(G/T)/∂T)_P=-H/T² is derived from the Fundamental Thermodynamic "
     "Relation by differentiating G=H-TS w.r.t. T at constant P, using dG=-SdT+VdP from TD5.",
     "2",   0.8400),

    ("KC4",  "Hess's Law",
     "TD2",  "First Law of Thermodynamics",
     "derives from",
     "Hess's Law (reaction enthalpy is path-independent) follows directly from the First Law: "
     "enthalpy is a state function because internal energy is conserved—ΔH depends only on "
     "initial and final states.",
     "2",   0.8070),

    ("KC4",  "Hess's Law",
     "KC5",  "Gibbs–Helmholtz Equation",
     "couples to",
     "Hess's Law gives additive, path-independent ΔH; Gibbs–Helmholtz relates ΔG to ΔH via "
     "temperature. Together they enable thermochemical cycle calculations linking standard "
     "enthalpies to free energies.",
     "2",   0.7956),

    ("TD6",  "Onsager Reciprocal Relations",
     "KC2",  "Law of Microscopic Reversibility",
     "derives from",
     "Onsager's Reciprocal Relations (L_ij=L_ji) are derived from the Law of Microscopic "
     "Reversibility: time-reversal symmetry of microscopic dynamics implies symmetry of the "
     "phenomenological transport coefficients.",
     "1.5", 0.8358),

    # ── DM / TD: Transport analogy ────────────────────────────────────────────
    ("DM1",  "Fick's Laws of Diffusion",
     "TD10", "Fourier's Law of Heat Conduction",
     "analogous to",
     "Fick's First Law J=-D∇c and Fourier's Law q=-k∇T are mathematically identical: both are "
     "linear transport laws (flux ∝ gradient). D↔k, concentration c↔temperature T.",
     "1.5", 0.8652),

    # ── QM / RD ───────────────────────────────────────────────────────────────
    ("QM1",  "Schrödinger Equation",
     "QM4",  "de Broglie Wavelength",
     "couples to",
     "The Schrödinger Equation was constructed to reproduce de Broglie's plane-wave solution "
     "ψ=e^{i(kx-ωt)}: inserting λ=h/p and E=hν into a wave equation yields iℏ∂ψ/∂t=Ĥψ; "
     "QM4 is the empirical input that motivated QM1.",
     "1.5", 0.8456),

    # ── Stefan-Boltzmann / 2nd Law ────────────────────────────────────────────
    ("RD2",  "Stefan–Boltzmann Law",
     "TD3",  "Second Law of Thermodynamics",
     "derives from",
     "Stefan–Boltzmann Law (j=σT⁴) follows from thermodynamic radiation arguments: applying the "
     "Second Law and isotropy of blackbody radiation to a cavity yields j∝T⁴; the exact σ "
     "requires Planck's Law.",
     "2",   0.8072),

    # ── GR / GEM ─────────────────────────────────────────────────────────────
    ("GV1",  "General Relativity — Einstein Field Equations",
     "GV2",  "Gravitoelectromagnetism (GEM)",
     "generalizes",
     "GEM is the weak-field, slow-motion linearised limit of General Relativity: expanding the "
     "GR metric perturbatively yields equations formally identical to Maxwell's equations for "
     "electromagnetism.",
     "2",   0.8267),

    # ── ES: Geography / Geology ───────────────────────────────────────────────
    ("ES1",  "Tobler's First Law of Geography",
     "ES2",  "Arbia's Law of Geography",
     "couples to",
     "Arbia's Law ('spatial interaction decreases with distance more rapidly than Tobler's law "
     "predicts because of natural barriers and boundaries') is a quantitative refinement of "
     "Tobler's First Law in spatial statistics.",
     "1.5", 0.8731),

    ("ES5",  "Birch's Law",
     "ES6",  "Byerlee's Law",
     "couples to",
     "Both are empirical constitutive laws for the Earth's crust: Birch's Law relates seismic "
     "wave velocity to density (Vp≈a+bρ); Byerlee's Law gives the frictional stress threshold "
     "for fault slip. Together they constrain crustal rheology.",
     "2",   0.8088),

    # ── CM8 / Lorentz ─────────────────────────────────────────────────────────
    ("CM8",  "Lorentz Force Law",
     "EM6",  "Coulomb's Law",
     "generalizes",
     "Coulomb's Law F=qE describes the electric force on a stationary charge; the Lorentz Force "
     "F=q(E+v×B) generalises this to moving charges in electromagnetic fields by adding the "
     "magnetic v×B term.",
     "2",   0.8303),

    ("CM8",  "Lorentz Force Law",
     "EM3",  "Faraday's Law of Induction",
     "couples to",
     "Faraday's Law gives the induced EMF=-dΦ/dt; the Lorentz Force Law gives the microscopic "
     "force on charges in the changing field. Together they describe motional EMF and "
     "electromagnetic induction at both field and particle levels.",
     "2",   0.8324),

    ("CM8",  "Lorentz Force Law",
     "EM7",  "Biot–Savart Law",
     "couples to",
     "Biot–Savart gives the B field produced by a current; the Lorentz Force Law gives the force "
     "on moving charges in that B field. Together they describe the full picture of magnetic "
     "force between current-carrying conductors.",
     "2",   0.8255),

    # ── AM5 / Noether → EM5 ──────────────────────────────────────────────────
    ("EM5",  "Continuity Equation (Charge Conservation)",
     "AM5",  "Noether's Theorem",
     "derives from",
     "Charge conservation (∂ρ/∂t+∇·J=0) follows from Noether's Theorem applied to the U(1) "
     "gauge symmetry of the electromagnetic Lagrangian: each continuous symmetry yields a "
     "conserved current.",
     "2",   0.8083),

    # ── CS / Information theory ───────────────────────────────────────────────
    ("CS6",  "Nyquist-Shannon Sampling Theorem",
     "INFO2", "Shannon Source Coding Theorem",
     "couples to",
     "Both are foundational Shannon results: Source Coding gives the minimum bit rate for "
     "lossless compression (entropy H); Nyquist-Shannon gives the minimum sampling rate for "
     "perfect reconstruction (2B samples/sec). Together they set the fundamental limits of "
     "digital representation.",
     "2",   0.8203),

    ("INFO2", "Shannon Source Coding Theorem",
     "STAT1", "Maximum Entropy Principle",
     "couples to",
     "Shannon Source Coding establishes entropy H as the minimum compression limit; Maximum "
     "Entropy Principle derives the least-biased distribution subject to constraints. The two "
     "are dual views of entropy: one operational (coding), one inferential.",
     "2",   0.8028),

    ("CS14", "Byzantine Fault Tolerance",
     "CS7",  "CAP Theorem",
     "couples to",
     "Both are foundational distributed-systems impossibility/trade-off results: CAP (at most two "
     "of Consistency, Availability, Partition tolerance) and BFT (consensus requires ≥3f+1 nodes "
     "to tolerate f Byzantine failures). They jointly bound distributed system guarantees.",
     "2",   0.7962),

    # ── Biology ───────────────────────────────────────────────────────────────
    ("BIO2",  "Hardy–Weinberg Principle",
     "BIO1",  "Mendelian Laws of Inheritance",
     "derives from",
     "Hardy–Weinberg Principle derives from Mendelian segregation: assuming random mating in a "
     "large population with Mendelian allele transmission, genotype frequencies p², 2pq, q² are "
     "the statistical consequence of Mendel's Laws.",
     "2",   0.7953),

    ("BIO2",  "Hardy–Weinberg Principle",
     "BIO3",  "Natural Selection — Fisher's Fundamental Theorem",
     "couples to",
     "Hardy–Weinberg gives the null model (no selection, drift, etc.) for allele frequencies; "
     "Fisher's Fundamental Theorem describes how selection changes mean fitness. Together they "
     "are the core of population genetics: HWE as baseline, FFT as the evolutionary driver.",
     "2",   0.8026),
]


def insert_links(db_path: Path, dry_run: bool = False) -> None:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    inserted = 0
    skipped  = 0

    for src_id, src_lbl, tgt_id, tgt_lbl, ltype, desc, tier, sim in LINKS:
        # Bidirectional duplicate guard
        cur.execute("""
            SELECT COUNT(*) FROM links
            WHERE (source_id=? AND target_id=?) OR (source_id=? AND target_id=?)
        """, (src_id, tgt_id, tgt_id, src_id))
        if cur.fetchone()[0] > 0:
            print(f"  SKIP (exists): {src_id} → {tgt_id}")
            skipped += 1
            continue

        if dry_run:
            print(f"  DRY [{tier}] {src_id} --{ltype}--> {tgt_id}  sim={sim:.4f}")
            print(f"       {desc[:90]}")
            inserted += 1
            continue

        cur.execute("""
            INSERT INTO links
              (link_type, source_id, source_label, target_id, target_label,
               description, link_order, confidence_tier)
            VALUES (?, ?, ?, ?, ?, ?, 0, ?)
        """, (ltype, src_id, src_lbl, tgt_id, tgt_lbl, desc, tier))
        print(f"  [{tier}] {src_id} --{ltype}--> {tgt_id}")
        inserted += 1

    if not dry_run:
        conn.commit()
    conn.close()

    print(f"\n{'DRY RUN' if dry_run else 'INSERTED'}: {inserted} links, {skipped} skipped")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = parser.parse_args()

    print(f"{'DRY RUN — ' if args.dry_run else ''}Inserting {len(LINKS)} links into {SOURCE_DB}")
    print("─" * 70)
    insert_links(SOURCE_DB, dry_run=args.dry_run)
