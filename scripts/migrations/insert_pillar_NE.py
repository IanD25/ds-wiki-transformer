"""
Pillar Extension — Non-Equilibrium Thermodynamics (NE)
Inserts 6 new reference_law entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Entries:
  NE01: Prigogine Dissipative Structures
  NE02: Maximum Entropy Production Principle
  NE03: Jarzynski Equality
  NE04: Crooks Fluctuation Theorem
  NE05: Fluctuation-Dissipation Theorem
  NE06: England Dissipation-Driven Adaptation
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── NON-EQUILIBRIUM THERMODYNAMICS ────────────────────────────────────────

{
    "id": "NE01",
    "title": "Prigogine Dissipative Structures",
    "filename": "NE01_prigogine_dissipative_structures.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · chemistry · biology",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Prigogine's theory of dissipative structures shows that systems far from thermodynamic equilibrium can spontaneously develop ordered spatial or temporal patterns — structures that are maintained by the continuous dissipation of energy and production of entropy (Prigogine, Nobel Prize 1977). These structures arise through symmetry-breaking instabilities when the entropy production rate exceeds a critical threshold. Examples include Bénard convection cells, the Belousov-Zhabotinsky reaction, and biological organisms. The key insight is counterintuitive: entropy production, far from being the enemy of order, is its driver in open systems. The second law requires that the total entropy of system plus environment increases, but this increase can be concentrated in the environment while the system becomes more ordered — provided energy flows through the system continuously. This connects to gravitational structure formation: gravitational collapse also creates ordered structures (stars, galaxies) while increasing total entropy, making it an astrophysical dissipative structure."),
        ("Mathematical Form", 1,
         "Entropy production rate: σ = dS_i/dt = Σ_k J_k X_k ≥ 0\n\nwhere:\n  J_k = generalised fluxes (heat, matter, charge)\n  X_k = generalised forces (temperature gradient, chemical potential gradient)\n\nLinear regime (near equilibrium): J_k = Σ_j L_kj X_j  (Onsager relations)\n\nInstability criterion (far from equilibrium):\n  δ²S < 0  (second variation of entropy becomes negative)\n  → spontaneous symmetry breaking → dissipative structure\n\nMinimum entropy production (linear): dσ/dt ≤ 0  (Prigogine theorem)"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): Dissipative structures are thermodynamic phenomena: they exist only in open systems with continuous energy flow and entropy production. The structure is a thermodynamic constraint — it is the configuration that satisfies the boundary conditions (energy input from environment) while obeying the second law (total entropy increases). The structure organises the entropy production, channelling it through ordered pathways."),
        ("DS Cross-References", 3,
         "TD3 (Second Law — dissipative structures are fully compatible with the second law: the local decrease in entropy of the structured system is more than compensated by the entropy increase in the environment). NE02 (Maximum Entropy Production Principle — MEPP proposes that dissipative structures maximise entropy production rate, selecting the pattern that most efficiently dissipates the driving energy gradient). NE06 (England — England extends Prigogine's framework to explain biological self-replication as a dissipation-driven process). B5 (Landauer's Principle — information processing in dissipative structures must pay the Landauer cost: k_BT ln 2 per bit erased). NE03 (Jarzynski Equality — Jarzynski provides the exact thermodynamic identity for processes far from equilibrium, extending the linear-regime Onsager relations)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: threshold-transition\n\nDissipative structures arise through a threshold transition: below a critical energy flux the system remains homogeneous; above the threshold, symmetry breaks and ordered patterns emerge spontaneously. The transition is analogous to a phase transition but occurs in a non-equilibrium, open system maintained by continuous energy flow."),
        ("What The Math Says", 5,
         "The entropy production rate sigma equals the sum over all irreversible processes k of the flux J-k times the conjugate force X-k, and is always non-negative by the second law. Near equilibrium, fluxes are linear in forces: J-k equals the sum of Onsager coefficients L-kj times X-j, with L-kj equals L-jk (Onsager reciprocal relations). In this linear regime, the system evolves to minimise entropy production (Prigogine's minimum entropy production theorem). Far from equilibrium, the linear approximation breaks down. When the second variation of entropy delta-squared-S becomes negative, the uniform state becomes unstable and the system spontaneously breaks symmetry, forming a dissipative structure — a spatially or temporally ordered pattern maintained by continuous energy throughput. The Bénard convection cell is the prototype: above a critical temperature gradient, the fluid transitions from conductive (disordered) to convective (ordered roll cells) heat transport."),
        ("Concept Tags", 6,
         "• dissipative structures\n• Prigogine\n• far-from-equilibrium\n• self-organisation\n• entropy production\n• symmetry breaking\n• open systems\n• Bénard convection\n• order from dissipation\n• non-equilibrium thermodynamics"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "dissipative structures, Prigogine, far-from-equilibrium, self-organisation, entropy production, symmetry breaking, open systems, Bénard convection, order from dissipation, non-equilibrium thermodynamics", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("couples to", "NE01", "Prigogine Dissipative Structures", "TD3", "Second Law of Thermodynamics", "Dissipative structures are fully compatible with the second law: local order is maintained by exporting entropy to the environment at a rate that exceeds the local entropy decrease."),
        ("derives from", "NE01", "Prigogine Dissipative Structures", "NE06", "England Dissipation-Driven Adaptation", "England extends Prigogine's framework to biology: biological self-replication is a dissipative structure driven by entropy production."),
        ("couples to", "NE01", "Prigogine Dissipative Structures", "B5", "B5: Landauer's Principle", "Information processing in dissipative structures must obey Landauer's bound: erasing one bit costs at least k_BT ln 2 in dissipated heat."),
    ],
},

{
    "id": "NE02",
    "title": "Maximum Entropy Production Principle",
    "filename": "NE02_maximum_entropy_production.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics · information",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Maximum Entropy Production Principle (MEPP) proposes that non-equilibrium systems with multiple accessible steady states will select the state that maximises the rate of entropy production, subject to the imposed constraints (Ziegler, 1963; Dewar, 2003; Martyushev & Seleznev, 2006). Unlike Prigogine's minimum entropy production theorem (valid only near equilibrium in the linear regime), MEPP applies to far-from-equilibrium systems where multiple dissipative configurations are possible. MEPP has been applied to atmospheric heat transport, planetary energy budgets, crystal growth, and biological evolution. The information-theoretic justification (Dewar, 2003) connects MEPP to the maximum entropy principle (Jaynes): the most probable macroscopic state is the one with the most microscopic realisations, which is the one producing entropy fastest. MEPP remains debated — it is not universally valid and may apply only to specific classes of systems — but its connection to information theory and the second law makes it a key entry for cross-pillar linking."),
        ("Mathematical Form", 1,
         "MEPP: max σ = max Σ_k J_k X_k  subject to constraints\n\nDewar's information-theoretic justification:\n  P(path) ∝ exp(σ[path] · τ / k_B)\n  (path probability proportional to exponential of entropy production)\n\nSteady-state selection: among all states consistent with\n  boundary conditions, the realised state maximises σ\n\nContrast with Prigogine: min σ (near equilibrium, linear)\n  vs. max σ (far from equilibrium, nonlinear)"),
        ("Constraint Category", 2,
         "Thermodynamic-Informatic (Th-In): MEPP is both a thermodynamic selection principle (it selects the most dissipative state) and an information-theoretic principle (the maximum entropy production state is the most probable state, connecting to Jaynes' maximum entropy). The constraint is that among all possible dissipative configurations, nature selects the one that maximises the entropy production rate."),
        ("DS Cross-References", 3,
         "NE01 (Prigogine — MEPP contrasts with Prigogine's minimum entropy production: Prigogine applies near equilibrium (linear), MEPP applies far from equilibrium (nonlinear)). TD3 (Second Law — MEPP is consistent with the second law but goes further: it selects not just the direction of entropy change but the rate). STAT1 (Maximum Entropy Principle — Dewar's justification connects MEPP to Jaynes' MaxEnt: the most probable macroscopic state maximises entropy production, just as the most probable probability distribution maximises Shannon entropy). NE06 (England — England's dissipation-driven adaptation can be viewed as a biological manifestation of MEPP: organisms that produce entropy faster are more likely to replicate)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nMEPP is an optimisation principle: nature selects the state that maximises the rate of entropy production. It extends the second law from a direction constraint (entropy increases) to a rate constraint (entropy increases as fast as possible given the constraints). The optimisation connects to information theory through the maximum entropy formalism."),
        ("What The Math Says", 5,
         "The entropy production rate sigma equals the sum over all irreversible processes k of flux J-k times force X-k. MEPP states that when multiple steady states are consistent with the boundary conditions, the realised state is the one that maximises sigma. Dewar's information-theoretic justification assigns path probabilities proportional to the exponential of the total entropy produced along the path: P of path is proportional to exp of sigma of path times the duration tau over k-B. This makes the most probable path the one producing the most entropy — a maximum-entropy argument applied to trajectory space. The principle contrasts with Prigogine's minimum entropy production theorem, which applies only in the linear near-equilibrium regime where fluxes are proportional to forces. Far from equilibrium, the linear approximation breaks down and MEPP replaces minimum entropy production as the selection principle."),
        ("Concept Tags", 6,
         "• maximum entropy production\n• MEPP\n• non-equilibrium selection\n• entropy production rate\n• Dewar justification\n• far-from-equilibrium\n• steady state selection\n• dissipation maximisation\n• information-theoretic thermodynamics\n• Ziegler principle"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th-In", 0),
        ("entries", "concept_tags", "maximum entropy production, MEPP, non-equilibrium selection, entropy production rate, Dewar justification, far-from-equilibrium, steady state selection, dissipation maximisation, information-theoretic thermodynamics, Ziegler principle", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("tensions with", "NE02", "Maximum Entropy Production Principle", "NE01", "Prigogine Dissipative Structures", "MEPP (maximise entropy production far from equilibrium) contrasts with Prigogine's minimum entropy production (near equilibrium) — they apply in different regimes."),
        ("analogous to", "NE02", "Maximum Entropy Production Principle", "STAT1", "Maximum Entropy Principle", "MEPP extends Jaynes' maximum entropy principle from static distributions to dynamic processes: the most probable steady state maximises the entropy production rate."),
        ("couples to", "NE02", "Maximum Entropy Production Principle", "TD3", "Second Law of Thermodynamics", "MEPP is consistent with but stronger than the second law: it constrains not just the direction of entropy change but selects the maximum rate among possible states."),
    ],
},

{
    "id": "NE03",
    "title": "Jarzynski Equality",
    "filename": "NE03_jarzynski_equality.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Jarzynski equality ⟨e^{−W/k_BT}⟩ = e^{−ΔF/k_BT} relates the exponential average of the work W performed in many repetitions of a non-equilibrium process to the equilibrium free energy difference ΔF between the initial and final states (Jarzynski, PRL 78, 2690, 1997). This is an exact identity — not an inequality or approximation — valid arbitrarily far from equilibrium. The equality recovers the second law as a special case: by Jensen's inequality, ⟨W⟩ ≥ ΔF (the average work is at least the free energy change). But it goes further: it allows the exact reconstruction of equilibrium free energy differences from non-equilibrium work measurements. The Jarzynski equality, along with the Crooks fluctuation theorem, extends thermodynamics from the near-equilibrium regime to arbitrary non-equilibrium processes, providing the exact relationship between irreversible work, free energy, and entropy production at any scale."),
        ("Mathematical Form", 1,
         "⟨e^{−W/k_BT}⟩ = e^{−ΔF/k_BT}\n\nwhere:\n  W = work performed on the system (varies between realisations)\n  ΔF = F_final − F_initial  (equilibrium free energy difference)\n  k_BT = thermal energy\n  ⟨·⟩ = average over many realisations of the process\n\nSecond law recovery (Jensen's inequality):\n  ⟨W⟩ ≥ ΔF  (average work ≥ free energy change)\n\nDissipated work: W_diss = W − ΔF ≥ 0  (on average)\n\nEntropy production: ⟨ΔS_tot⟩ = ⟨W_diss⟩/T ≥ 0"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): The Jarzynski equality is an exact thermodynamic identity valid for all processes, equilibrium or not. It extends the second law from an inequality (⟨W⟩ ≥ ΔF) to an exact equality at the level of exponential averages. The equality has been experimentally verified in single-molecule pulling experiments on RNA hairpins (Liphardt et al., Science 296, 1832, 2002)."),
        ("DS Cross-References", 3,
         "NE04 (Crooks Fluctuation Theorem — Crooks' theorem is the more fundamental result from which Jarzynski follows; it relates the probability of forward and reverse work values). TD3 (Second Law — the Jarzynski equality implies the second law via Jensen's inequality: ⟨e^{−W/kT}⟩ ≥ e^{−⟨W⟩/kT} → ⟨W⟩ ≥ ΔF). NE05 (Fluctuation-Dissipation Theorem — Jarzynski generalises the FDT to far-from-equilibrium processes; the FDT is the near-equilibrium limit). HB06 (Black Hole Area Theorem — both are irreversibility statements: the area theorem says gravitational entropy increases; Jarzynski says ⟨W_diss⟩ ≥ 0. Both await a fluctuation-theorem generalisation in the gravitational case). IT03 (KL Divergence — the dissipated work W_diss/kT equals the KL divergence between forward and time-reversed path distributions, connecting non-equilibrium work to information theory)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nThe Jarzynski equality is an exact identity connecting non-equilibrium measurements to equilibrium properties. It is an equilibrium condition in a generalised sense: the exponential average of non-equilibrium work equals the equilibrium free energy change. This allows equilibrium thermodynamics to be recovered from arbitrarily far-from-equilibrium experiments."),
        ("What The Math Says", 5,
         "Perform a non-equilibrium process many times, starting from the same equilibrium state and ending at the same final control parameter. Each realisation produces a different amount of work W-i due to thermal fluctuations. The Jarzynski equality states that the average of e-to-the-minus-W over k-B-T equals e-to-the-minus-Delta-F over k-B-T, where Delta-F is the equilibrium free energy difference. By Jensen's inequality (since the exponential function is convex), the average work is at least Delta-F: the average W is greater than or equal to Delta-F. The dissipated work W-diss equals W minus Delta-F is non-negative on average, recovering the second law. The deep content is the equality: the exponential average exactly recovers the equilibrium quantity from non-equilibrium data. The dissipated work W-diss over k-B-T equals the KL divergence between the probability distribution over forward paths and the distribution over time-reversed paths — connecting irreversibility to information divergence."),
        ("Concept Tags", 6,
         "• Jarzynski equality\n• non-equilibrium work\n• free energy recovery\n• exponential average\n• dissipated work\n• second law generalisation\n• single-molecule experiments\n• fluctuation theorem\n• path probability\n• information and irreversibility"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Jarzynski equality, non-equilibrium work, free energy recovery, exponential average, dissipated work, second law generalisation, single-molecule experiments, fluctuation theorem, path probability, information and irreversibility", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "NE03", "Jarzynski Equality", "NE04", "Crooks Fluctuation Theorem", "The Jarzynski equality is derived from the Crooks fluctuation theorem by integrating over work values — Crooks is the more fundamental result."),
        ("generalizes", "NE03", "Jarzynski Equality", "TD3", "Second Law of Thermodynamics", "The Jarzynski equality generalises the second law: ⟨W⟩ ≥ ΔF (second law) follows from ⟨e^{-W/kT}⟩ = e^{-ΔF/kT} (Jarzynski) via Jensen's inequality."),
        ("couples to", "NE03", "Jarzynski Equality", "IT03", "Kullback-Leibler Divergence", "The dissipated work W_diss/kT equals the KL divergence between forward and reverse path probability distributions — irreversibility is measured by information divergence."),
    ],
},

{
    "id": "NE04",
    "title": "Crooks Fluctuation Theorem",
    "filename": "NE04_crooks_fluctuation_theorem.md",
    "entry_type": "reference_law",
    "scale": "molecular",
    "domain": "physics · information",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Crooks fluctuation theorem states that the ratio of the probability of performing work W in a forward process to the probability of performing work −W in the time-reversed process equals the exponential of the dissipated work: P_F(W)/P_R(−W) = e^{(W−ΔF)/k_BT} (Crooks, PRE 60, 2721, 1999). This is an exact microscopic symmetry of non-equilibrium thermodynamics — it relates the probability of entropy-producing (forward) and entropy-consuming (reverse) fluctuations. The Crooks theorem is the most fundamental fluctuation theorem: the Jarzynski equality follows from it by integration, and the second law follows from both by Jensen's inequality. The theorem implies that second-law violations are exponentially suppressed but not impossible — they occur with probability proportional to e^{−ΔS/k_B}. At microscopic scales (where W is comparable to k_BT), these violations are observable; at macroscopic scales, they are astronomically improbable."),
        ("Mathematical Form", 1,
         "P_F(W) / P_R(−W) = e^{(W − ΔF)/k_BT}\n\nwhere:\n  P_F(W) = probability of work W in forward process\n  P_R(−W) = probability of work −W in reverse process\n  ΔF = free energy difference\n\nCrossing point: P_F(W*) = P_R(−W*)  when W* = ΔF\n  (the crossing point of forward and reverse work distributions\n   directly gives the free energy difference)\n\nSecond law from Crooks:\n  ∫ P_F(W) e^{−W/kT} dW = e^{−ΔF/kT}  (Jarzynski equality)"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): The Crooks theorem is a fundamental thermodynamic symmetry: it quantifies the asymmetry between forward and reverse processes. The exponential factor e^{(W−ΔF)/kT} measures the irreversibility — the dissipated work — and determines the probability ratio between entropy-producing and entropy-consuming fluctuations."),
        ("DS Cross-References", 3,
         "NE03 (Jarzynski Equality — Jarzynski is derived from Crooks by integrating over work values; Crooks is the more fundamental microscopic identity). TD3 (Second Law — the second law is a macroscopic consequence of Crooks: entropy-producing paths are exponentially more probable than entropy-consuming paths). NE05 (Fluctuation-Dissipation Theorem — the FDT is the near-equilibrium linearisation of the Crooks theorem). IT03 (KL Divergence — the log ratio log[P_F(W)/P_R(−W)] = (W−ΔF)/kT is a KL divergence between forward and reverse path distributions, connecting fluctuation theorems to information theory)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nThe Crooks theorem is a detailed-balance condition generalised to non-equilibrium processes. At ΔF = 0 (free energy preserved), the forward and reverse work distributions are symmetric — this is equilibrium. Non-zero ΔF breaks the symmetry, and the Crooks theorem quantifies exactly how much the forward process is favoured over the reverse."),
        ("What The Math Says", 5,
         "The Crooks fluctuation theorem relates the probability P-F of W of doing work W in a forward non-equilibrium process to the probability P-R of minus-W of doing work minus-W in the time-reversed process. The ratio is exponential in the dissipated work: P-F of W over P-R of minus-W equals e-to-the-(W minus Delta-F) over k-B-T. When the work W equals the free energy difference Delta-F, the forward and reverse probabilities are equal — this crossing point directly measures Delta-F. The Jarzynski equality follows by multiplying both sides by P-R of minus-W, integrating over W, and using the normalisation of P-R. The second law follows because the exponential weight favours the forward direction exponentially: the average dissipated work average of W minus Delta-F is non-negative. For large systems where W is much greater than k-B-T, entropy-consuming fluctuations are exponentially suppressed; for molecular-scale systems, they are directly observable."),
        ("Concept Tags", 6,
         "• Crooks fluctuation theorem\n• time-reversal symmetry\n• work distribution\n• forward-reverse asymmetry\n• detailed balance\n• entropy production\n• microscopic reversibility\n• crossing point method\n• non-equilibrium identity\n• dissipated work"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Crooks fluctuation theorem, time-reversal symmetry, work distribution, forward-reverse asymmetry, detailed balance, entropy production, microscopic reversibility, crossing point method, non-equilibrium identity, dissipated work", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "NE04", "Crooks Fluctuation Theorem", "NE03", "Jarzynski Equality", "Crooks is the more fundamental theorem: the Jarzynski equality follows from Crooks by integration over work values."),
        ("generalizes", "NE04", "Crooks Fluctuation Theorem", "TD3", "Second Law of Thermodynamics", "The second law is a macroscopic consequence of Crooks: entropy-producing forward paths are exponentially more probable than reverse paths."),
        ("couples to", "NE04", "Crooks Fluctuation Theorem", "IT03", "Kullback-Leibler Divergence", "The log ratio of forward to reverse path probabilities equals the dissipated work over kT, which is the KL divergence between forward and reverse path ensembles."),
    ],
},

{
    "id": "NE05",
    "title": "Fluctuation-Dissipation Theorem",
    "filename": "NE05_fluctuation_dissipation_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The fluctuation-dissipation theorem (FDT) states that the linear response of a system to an external perturbation is determined by the equilibrium fluctuations of the same system — the way a system responds to being pushed is encoded in the way it naturally jitters (Nyquist, 1928; Callen & Welton, 1951; Kubo, 1957). Quantitatively, the dissipative part of the response function (how much energy the system absorbs) equals the spectral density of equilibrium fluctuations (how much the observable naturally fluctuates) times a thermal factor k_BT. The FDT is the foundational result linking equilibrium statistical mechanics to near-equilibrium transport: it derives Ohm's law (electrical resistance from voltage fluctuations), Einstein's relation (diffusion from drag), and Nyquist's formula (thermal noise from resistance). The FDT breaks down far from equilibrium, where the Crooks and Jarzynski relations provide the exact non-equilibrium generalisation."),
        ("Mathematical Form", 1,
         "Classical FDT (Kubo):\n  χ''(ω) = (ω/2k_BT) S(ω)\n\nwhere:\n  χ''(ω) = dissipative (imaginary) part of the response function\n  S(ω) = spectral density of equilibrium fluctuations\n\nEinstein relation: D = k_BT / γ  (diffusion = thermal energy / drag)\n\nNyquist formula: ⟨V²⟩ = 4k_BT R Δf  (voltage noise from resistance)\n\nQuantum FDT:\n  χ''(ω) = (1/2ℏ) tanh(ℏω/2k_BT) S(ω)"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): The FDT is a thermodynamic constraint linking two seemingly different physical quantities — response (how a system reacts to perturbation) and fluctuation (how a system spontaneously varies). The linking factor is the temperature k_BT, making the FDT a direct manifestation of the equipartition of thermal energy."),
        ("DS Cross-References", 3,
         "NE04 (Crooks — the FDT is the linear (near-equilibrium) limit of the Crooks fluctuation theorem; Crooks generalises the FDT to arbitrary non-equilibrium processes). TD3 (Second Law — the FDT encodes the second law at the linear level: dissipation and fluctuation are linked by the temperature, and the positivity of dissipation ensures entropy production). NE01 (Prigogine — the FDT operates in the linear near-equilibrium regime where Prigogine's minimum entropy production applies). STAT2 (Ergodic Theorem — the FDT requires ergodicity: the time average of fluctuations must equal the ensemble average for the spectral density to predict the response)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nThe FDT is the defining condition of thermal equilibrium: it states that the ratio of fluctuation to dissipation is fixed by the temperature. Systems violating the FDT are by definition out of equilibrium. The violation of the FDT far from equilibrium is quantified by an effective temperature different from the bath temperature — a measure of how far the system is from equilibrium."),
        ("What The Math Says", 5,
         "The fluctuation-dissipation theorem in its Kubo form states that the dissipative part of the response function chi-double-prime at frequency omega equals omega over 2 k-B T times the spectral density S of omega of equilibrium fluctuations. The response function chi describes how a system responds to a small external perturbation — its imaginary part chi-double-prime determines the rate of energy absorption. The spectral density S describes the natural fluctuations of the system at each frequency. The FDT says these are proportional, with the proportionality constant set by the temperature. Einstein's relation D equals k-B T over gamma is a special case: the diffusion coefficient D (a fluctuation property) equals the thermal energy k-B T divided by the drag coefficient gamma (a dissipation property). Nyquist's formula is another special case: the mean-square voltage noise across a resistor R in bandwidth Delta-f is 4 k-B T R Delta-f."),
        ("Concept Tags", 6,
         "• fluctuation-dissipation theorem\n• Kubo formula\n• linear response\n• equilibrium fluctuations\n• thermal noise\n• Einstein relation\n• Nyquist formula\n• spectral density\n• dissipation\n• response function"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "fluctuation-dissipation theorem, Kubo formula, linear response, equilibrium fluctuations, thermal noise, Einstein relation, Nyquist formula, spectral density, dissipation, response function", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "NE05", "Fluctuation-Dissipation Theorem", "NE04", "Crooks Fluctuation Theorem", "The FDT is the near-equilibrium linear limit of the Crooks fluctuation theorem — Crooks generalises the FDT to arbitrary non-equilibrium processes."),
        ("couples to", "NE05", "Fluctuation-Dissipation Theorem", "TD3", "Second Law of Thermodynamics", "The FDT encodes the second law at the linear level: the positivity of dissipation (chi'' > 0) ensures non-negative entropy production."),
        ("couples to", "NE05", "Fluctuation-Dissipation Theorem", "STAT2", "Ergodic Theorem", "The FDT requires ergodicity: the time-averaged fluctuations must equal the ensemble average for the spectral density to correctly predict the linear response."),
    ],
},

{
    "id": "NE06",
    "title": "England Dissipation-Driven Adaptation",
    "filename": "NE06_england_dissipation_driven_adaptation.md",
    "entry_type": "reference_law",
    "scale": "molecular · cellular",
    "domain": "physics · biology",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "England's theory of dissipation-driven adaptation proposes that self-replication and biological complexity arise because replicating systems are exceptionally good at dissipating energy — they produce entropy faster than non-replicating alternatives (England, JCP 139, 121923, 2013). Starting from the Crooks fluctuation theorem, England derived a lower bound on the entropy produced by a self-replicating system: the irreversibility of replication is bounded by the thermodynamic cost of organising the replicated structure. Systems that are better at absorbing and dissipating energy from their environment (work sources) are thermodynamically favoured to replicate. This provides a physics-based explanation for the emergence of biological complexity: life is not an improbable accident that works against the second law, but a highly probable outcome of non-equilibrium thermodynamics — organisms are dissipative structures that increase the rate of universal entropy production. The theory extends Prigogine's dissipative structures from simple pattern formation to biological self-replication."),
        ("Mathematical Form", 1,
         "Entropy production bound for self-replication:\n  ⟨ΔS_total⟩ ≥ −Δs_int + log(n_rep/n_init)\n\nwhere:\n  ΔS_total = total entropy production (system + environment)\n  Δs_int = internal entropy change of the replicator\n  n_rep/n_init = replication ratio\n\nDerived from Crooks fluctuation theorem:\n  P_F(W)/P_R(−W) = e^{(W−ΔF)/kT}\n  applied to self-replication as the forward process\n\nDissipation-driven selection: systems that dissipate more energy\n  from work sources are more likely to be found replicating"),
        ("Constraint Category", 2,
         "Thermodynamic (Th): England's theory is a thermodynamic constraint on biological self-replication: the minimum entropy cost of replication is set by the Crooks theorem. Replicators that can absorb and dissipate more energy from work sources (sunlight, chemical gradients) are thermodynamically favoured — they occupy the entropy-producing pathways that the second law makes most probable."),
        ("DS Cross-References", 3,
         "NE04 (Crooks Fluctuation Theorem — England's bound is derived directly from the Crooks theorem applied to self-replication as a non-equilibrium process). NE01 (Prigogine — England extends Prigogine's dissipative structures from simple pattern formation to biological self-replication and adaptation). TD3 (Second Law — England's theory reframes the second law positively: biological complexity is not despite the second law but because of it — organisms maximise entropy production). NE02 (MEPP — England's dissipation-driven adaptation is consistent with MEPP: self-replicators are selected because they maximise entropy production rate). B5 (Landauer's Principle — the information content of the replicator sets a minimum thermodynamic cost via Landauer's bound: copying one bit costs at least kT ln 2)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: optimization-principle\n\nEngland's theory is an optimization argument: among all possible molecular configurations in a far-from-equilibrium environment, those that most efficiently dissipate the available work sources (absorb and degrade energy gradients) are thermodynamically most probable. Self-replicators are optimal dissipators because each copy doubles the rate of energy degradation."),
        ("What The Math Says", 5,
         "Starting from the Crooks fluctuation theorem applied to self-replication as the forward process, England derives that the total entropy production averaged over many replication events is at least the negative of the internal entropy change Delta-s-int plus the logarithm of the replication ratio n-rep over n-init. The internal entropy change accounts for the organisational cost of building the replica — a highly ordered structure has low internal entropy, requiring more total entropy production (more dissipation) to create. The log replication ratio accounts for the probability of producing multiple copies versus one. The physical picture is that in a far-from-equilibrium environment with available work sources (sunlight, chemical gradients), configurations that are good at absorbing and dissipating this energy are more likely to persist and replicate. Self-replicating molecules are particularly efficient dissipators because each copy amplifies the rate of energy degradation exponentially. This makes self-replication thermodynamically favoured — not a miraculously improbable event, but the most probable outcome of sustained energy flow."),
        ("Concept Tags", 6,
         "• dissipation-driven adaptation\n• England\n• self-replication thermodynamics\n• biological complexity\n• entropy production bound\n• Crooks theorem biology\n• life as dissipation\n• non-equilibrium biology\n• thermodynamic selection\n• origin of complexity"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "dissipation-driven adaptation, England, self-replication thermodynamics, biological complexity, entropy production bound, Crooks theorem biology, life as dissipation, non-equilibrium biology, thermodynamic selection, origin of complexity", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "NE06", "England Dissipation-Driven Adaptation", "NE04", "Crooks Fluctuation Theorem", "England's entropy production bound for self-replication is derived directly from the Crooks fluctuation theorem applied to the forward (replication) and reverse (degradation) processes."),
        ("generalizes", "NE06", "England Dissipation-Driven Adaptation", "NE01", "Prigogine Dissipative Structures", "England extends Prigogine's dissipative structures from simple pattern formation (Bénard cells, chemical oscillations) to biological self-replication and adaptation."),
        ("couples to", "NE06", "England Dissipation-Driven Adaptation", "B5", "B5: Landauer's Principle", "The information content of the replicator sets a minimum thermodynamic cost via Landauer's bound: the organisational entropy of the replica must be paid for in dissipated heat."),
    ],
},

]  # end ENTRIES


def insert_entries(db_path, entries):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    inserted = skipped = 0

    for e in entries:
        cur.execute("""
            INSERT OR IGNORE INTO entries
                (id, title, filename, entry_type, scale, domain, status, confidence, type_group, authoring_status)
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (e["id"], e["title"], e["filename"], e["entry_type"], e["scale"],
              e["domain"], e["status"], e["confidence"], e["type_group"], None))

        if cur.rowcount == 0:
            print(f"  SKIP (exists): {e['id']}")
            skipped += 1
            continue

        for (sname, sorder, content) in e["sections"]:
            cur.execute("""
                INSERT INTO sections (entry_id, section_name, section_order, content)
                VALUES (?,?,?,?)
            """, (e["id"], sname, sorder, content))

        for (tname, pname, pvalue, porder) in e["properties"]:
            cur.execute("""
                INSERT INTO entry_properties
                    (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?,?,?,?,?)
            """, (e["id"], tname, pname, pvalue, porder))

        for (ltype, src, slabel, tgt, tlabel, desc) in e.get("links", []):
            cur.execute("""
                INSERT OR IGNORE INTO links
                    (link_type, source_id, source_label, target_id, target_label,
                     description, link_order, confidence_tier)
                VALUES (?,?,?,?,?,?,?,?)
            """, (ltype, src, slabel, tgt, tlabel, desc, 0, "1.5"))

        print(f"  INSERT: {e['id']} — {e['title']}")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone: {inserted} inserted, {skipped} skipped.")
    return inserted


if __name__ == "__main__":
    print(f"Inserting NE pillar ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)
