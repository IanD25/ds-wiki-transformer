"""
Content for qr004_fold_in_2026_10_18.py (audit_ref gsw-qr004-fold-in-2026-10-18).

Thermodynamic limits on biological information processing: the literature that tests biology
against Landauer, the TUR and process-specific bounds, folded in as reference_law entries
NE07-NE10 and BIO17-BIO25 to ground Questions Raised Log item QR-004. Mode A; no new
conjectures, no promotions, no calibration rows. Owner approved all 13 entries, the statuses
and six links from corrected entries (2026-10-18).

Reading rule (EWS precedent): each statement is limited to what was actually read. Reading level per
source is in each anchor's notes: "this session" = read by the fold-in session itself; "QR-004 map
sub-agent" = read by a sub-agent of the literature-map session (reported, not re-read here).
Every DOI was checked on Crossref on 2026-10-18.
"""

AUD = "gsw-qr004-fold-in-2026-10-18"
MAP = "docs/prior_art_reviews/QR-004_THERMO_LIMITS_LITERATURE_MAP_2026_10_18.md"


def facets(cc, tags, archetype, dsens="D-invariant"):
    return [("DS Facets", "Constraint Category", cc, 0),
            ("entries", "concept_tags", ", ".join(tags), 0),
            ("DS Facets", "mathematical_archetype", archetype, 1),
            ("DS Facets", "dimensional_sensitivity", dsens, 2)]


def bullets(tags):
    return "\n".join(f"• {t}" for t in tags)


ENTRIES = []
LINKS = []    # (source_id, target_id, link_type, confidence_tier, description)
ANCHORS = []  # dicts
TAGS = []     # (entry_id, tag_path, primacy, confidence, rationale)


def anchor(entry_id, identifier, title, relationship, notes, role=None, tier=1,
           stability="active-literature", confidence="high", source="doi"):
    ANCHORS.append(dict(entry_id=entry_id, source=source, identifier=identifier, title=title,
                        relationship=relationship, role=role, tier=tier, stability=stability,
                        confidence=confidence, notes=notes))


def tag(entry_id, path, primacy, rationale, confidence="high"):
    TAGS.append((entry_id, path, primacy, confidence, f"QR-004 fold-in ({AUD}): {rationale}"))


DIM = ("Dimensional sensitivity: D-invariant — the result is stated for Markov or Langevin models and "
       "counts states, rates and free energies; nothing in it depends on spatial dimension.")

# ===========================================================================
# NE07 — Logical vs thermodynamic reversibility (Bennett)
# ===========================================================================
_t = ["logical reversibility", "thermodynamic reversibility", "reversible computation", "Bennett",
      "copying onto a blank register", "reversible measurement", "path merging", "Brownian computer",
      "ballistic computer", "Landauer principle scope", "uncomputation", "Maxwell demon"]
ENTRIES.append(dict(
    id="NE07", title="NE07: Logical vs Thermodynamic Reversibility and Reversible Computation (Bennett 1973, 1982)",
    filename="NE07_logical_thermodynamic_reversibility.md",
    scale="cross-scale", domain="physics · information", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "Logical reversibility and thermodynamic reversibility are different properties. An operation is logically "
         "reversible if its input can be recovered from its output. Landauer's bound (B5) prices only logically "
         "irreversible steps: erasure, and the merging of two computation paths. Even then the step is wasteful only "
         "when applied to data whose value is already known; erasing a genuinely random bit is a reversible transfer of "
         "entropy to the environment, like isothermal compression of a gas (Bennett 2003).\n\n"
         "Bennett (1973) showed that any computation can be made logically reversible at every step. The machine "
         "saves its intermediate results, writes out the answer, then runs the first stage backwards to clear the "
         "saved history, ending with only the output and a copy of the input. Logically reversible operations, "
         "including copying onto a blank register and measurement, can in principle be carried out thermodynamically "
         "reversibly. Ballistic (conservative) models do so with no dissipation. Brownian models dissipate per step in "
         "proportion to the driving force, which goes to zero as the step is driven more slowly (Bennett 1982, 2003). "
         "Bennett gives messenger-RNA synthesis as a physical example of nearly reversible copying, driven mainly by "
         "removal of the pyrophosphate product. He calls the belief that every elementary act of information processing "
         "(measuring, copying, a logic operation) costs about kT a misconception, and describes Landauer's principle as "
         "a consequence, or restatement, of the second law (Bennett 2003).\n\n"
         "SCOPE: these are in-principle statements. Real devices run at finite speed and pay excess dissipation that "
         "falls off as 1/τ with operating time (NE08); fault-tolerant error correction must reset its syndrome bits, "
         "which is erasure."),
        ("Mathematical Form",
         "Copy onto a blank register:   y := y + x   (y initially 0)      — logically reversible\n"
         "Erase one of two known copies: y := y − x   (y known to equal x) — logically reversible\n"
         "Erase / merge known data:      ΔS_env ≥ k ln 2 per bit, not compensated → thermodynamically irreversible\n"
         "Erase a uniformly random bit:  ΔS_data = −k ln 2, ΔS_env = +k ln 2 → can be thermodynamically reversible\n"
         "Brownian computer:            dissipation per step ∝ driving force → 0 as speed → 0\n"
         "Bennett 1973 simulation:      compute (keep history) → copy output → uncompute (clear history)"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): decides which logical operations carry a thermodynamic floor (erasure, "
         "path merging) and which carry none in principle (reversible operations, including copying and measurement)."),
        ("DS Cross-References",
         "B5 (Landauer's principle — this entry fixes its scope). NE08 (generalised and finite-time bounds; the 1/τ "
         "excess). BIO19 (biochemical copying — the free energy a persistent copy must store). CS11 (sorting — "
         "comparisons can be done reversibly; the cost lies in discarding the input order). INFO5 (Zurek's K(x)·kT ln 2 "
         "proposal). EM11 (Joule heating is finite-speed resistive loss, not a Landauer floor)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "The floor kT ln 2 per bit applies to a defined class of operations (logically irreversible ones applied to "
         "known data). Outside that class the bound is zero in principle; what remains is a speed-dependent excess.\n\n"
         + DIM),
        ("What The Math Says",
         "Think of a computer step as a function from inputs to outputs. If two different inputs can give the same "
         "output, information is lost and Landauer's price must be paid. If every output has exactly one input, nothing "
         "is lost and, in principle, nothing must be paid. Copying a value onto a blank slot is of the second kind: you "
         "can always undo it by subtracting the value back out. Bennett showed that any calculation can be rearranged "
         "into steps of the second kind by keeping a record of what was done, then unwinding that record once the answer "
         "has been copied out. The only true costs are erasing information and running fast."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "thermodynamic-bound"),
))
anchor("NE07", "10.1007/BF02084158", "Bennett 1982 - The thermodynamics of computation, a review (Int. J. Theor. Phys. 21:905-940)",
       "canonical_authority",
       "Standard review of reversible computation and Maxwell's demon. Read by a QR-004 map sub-agent (full text, selected "
       "sections; " + MAP + " §I); not re-read by this session. DOI verified on Crossref 2026-10-18.",
       role="comprehensive_survey", stability="canonical")
anchor("NE07", "10.1147/rd.176.0525", "Bennett 1973 - Logical reversibility of computation (IBM J. Res. Dev. 17:525-532)",
       "canonical_authority",
       "Progenitor: any Turing machine can be made logically reversible at every step (compute, copy output, uncompute). "
       "Abstract read by this session 2026-10-18 (OpenAlex); body not read. DOI verified on Crossref.",
       role="progenitor", stability="canonical", confidence="medium")
anchor("NE07", "10.1016/S1355-2198(03)00039-X",
       "Bennett 2003 - Notes on Landauer's principle, reversible computation, and Maxwell's demon (Stud. Hist. Phil. Mod. Phys. 34:501-510; arXiv:physics/0210005)",
       "cites",
       "Full text read by this session 2026-10-18 (arXiv v2): copying onto a blank register and measurement are logically "
       "reversible; ballistic computers at zero cost, Brownian ones at a per-step cost vanishing in the slow limit; erasing "
       "random data is a reversible entropy transfer; the ~kT-per-operation belief is a misconception; transcription as "
       "logically reversible copying; Landauer as a consequence of the second law. DOI verified on Crossref.",
       stability="canonical")
tag("NE07", "physics.modern.statistical_mechanics", "primary", "thermodynamics of computation")
tag("NE07", "computer_science.complexity", "secondary", "reversible computation and its space/time cost")
tag("NE07", "information_theory.shannon", "secondary", "information erased vs preserved")
LINKS += [
    ("NE07", "B5", "generalizes", "1",
     "Fixes the scope of Landauer's bound: it prices logically irreversible operations on known data; logically reversible "
     "operations, including copying and measurement, have no floor in principle (Bennett 1973, 1982, 2003)."),
    ("NE07", "TD3", "derives from", "1",
     "Bennett 2003 describes Landauer's principle as a consequence, or restatement, of the second law."),
    ("NE07", "CS11", "constrains", "1.5",
     "Comparisons can be done reversibly, so sorting's unavoidable thermodynamic cost is discarding the input order, "
     "kT ln(n!), and zero if the permutation is kept."),
    ("NE07", "INFO5", "couples to", "2",
     "Zurek's K(x)·kT ln 2 erasure cost presupposes erasing the shortest description; reversible computation shows which "
     "parts of a computation need not be erased."),
]

# ===========================================================================
# NE08 — Generalised and finite-time Landauer bounds; experimental tests
# ===========================================================================
_t = ["generalised Landauer bound", "nonequilibrium free energy", "relative entropy", "information thermodynamics",
      "Sagawa-Ueda", "finite-time erasure", "1/tau excess dissipation", "colloidal particle", "feedback trap",
      "Bérut experiment", "Jun-Gavrilov-Bechhoefer", "memory erasure"]
ENTRIES.append(dict(
    id="NE08", title="NE08: Generalised and Finite-Time Landauer Bounds, and Their Experimental Tests",
    filename="NE08_generalised_finite_time_landauer.md",
    scale="molecular", domain="physics · information", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "Landauer's kT ln 2 per bit (B5) is the special case of a general second-law statement. Esposito & Van den "
         "Broeck (2011): the work needed to take a system in contact with a heat bath between given non-equilibrium "
         "states is at least the equilibrium free-energy difference plus kT times the change in the relative entropy of "
         "the state with respect to equilibrium. Erasing a symmetric one-bit memory is the case that gives kT ln 2.\n\n"
         "Sagawa & Ueda (2009) derive lower bounds on the work cost of measurement and of erasure separately. Their "
         "erasure bound reproduces Landauer's principle for a symmetric memory; for other memories it departs from it "
         "(the principle breaks down as a statement about erasure alone), while the measurement-plus-erasure cycle "
         "remains bounded by the second law. Proesmans, Ehrich & Bechhoefer (2020) treat erasure in finite time: the "
         "minimum average work exceeds the quasistatic bound, they give a closed expression in the short-time limit, "
         "and optimal protocols can use up to four times less work than protocols constrained to end in local "
         "equilibrium.\n\n"
         "Experiments. Bérut et al. (2012), a colloidal particle in a modulated double-well potential: the mean "
         "dissipated heat saturates at the Landauer bound in the limit of long erasure cycles. Jun, Gavrilov & "
         "Bechhoefer (2014), a feedback trap with full control of the potential: full erasure costs 0.71 ± 0.03 kT (the "
         "asymptotic value of a 1/τ fit; ln 2 ≈ 0.693), while a matched protocol that erases nothing costs "
         "0.05 ± 0.03 kT; in individual cycles the work can fall below the bound, consistent with the Jarzynski "
         "equality (NE03)."),
        ("Mathematical Form",
         "Esposito–Van den Broeck 2011:\n"
         "  W ≥ ΔF_eq + kT [ D(ρ_final‖ρ_eq,final) − D(ρ_initial‖ρ_eq,initial) ]\n"
         "  symmetric double-well erasure: ΔF_eq = 0, ρ_initial = ρ_eq, D(ρ_final‖ρ_eq) = ln 2 ⇒ W ≥ kT ln 2\n"
         "Finite time: for slow protocols the excess work falls off as 1/τ (the form Jun et al. 2014 fit);\n"
         "  Proesmans et al. 2020 give the minimum and a short-time closed form\n"
         "Jun et al. 2014 (asymptotic, from a 1/τ fit): full erasure 0.71 ± 0.03 kT; no erasure 0.05 ± 0.03 kT"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): second-law bounds on the work cost of changing the information content of a "
         "physical memory, including non-equilibrium states and finite operating time."),
        ("DS Cross-References",
         "B5 (Landauer's principle — the special case). IT03 (relative entropy, the quantity in the generalised bound). "
         "NE03 (Jarzynski — single-cycle work below the bound is allowed). NE07 (which operations need erasing at all). "
         "TD3 (second law)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "A lower bound on average work, saturated only quasistatically; finite operating time adds an excess that "
         "vanishes as 1/τ.\n\n" + DIM),
        ("What The Math Says",
         "Landauer's number is what you get for resetting a fair coin-flip memory infinitely slowly. If the memory starts "
         "or ends out of equilibrium, the price is the free-energy change plus kT times how far the state is from "
         "equilibrium, measured by relative entropy. If you hurry, you pay extra, and the extra shrinks roughly as one "
         "over the time you allow. The cleanest experiment measured 0.71 kT for a full erasure against a predicted 0.69, "
         "and almost nothing for an otherwise identical operation that erased nothing."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "thermodynamic-bound"),
))
anchor("NE08", "10.1209/0295-5075/95/40004", "Esposito & Van den Broeck 2011 - Second law and Landauer principle far from equilibrium (EPL 95:40004)",
       "canonical_authority",
       "Progenitor of the relative-entropy form of the bound. Abstract read by this session 2026-10-18; full text read by a "
       "QR-004 map sub-agent (fetch). DOI verified on Crossref.", role="progenitor")
anchor("NE08", "10.1103/PhysRevLett.102.250602", "Sagawa & Ueda 2009 - Minimal energy cost for thermodynamic information processing: measurement and information erasure (PRL 102:250602)",
       "cites", "Abstract read by this session 2026-10-18: erasure bound validates Landauer for a symmetric memory, breaks "
       "down otherwise; second law of information thermodynamics. Body not read. DOI verified.")
anchor("NE08", "10.1103/PhysRevLett.125.100602", "Proesmans, Ehrich & Bechhoefer 2020 - Finite-time Landauer principle (PRL 125:100602)",
       "cites", "Abstract read by this session 2026-10-18 (short-time closed form; optimal protocols up to 4x cheaper than "
       "local-equilibrium-constrained ones); main text read by a QR-004 map sub-agent. DOI verified.")
anchor("NE08", "10.1038/nature10872", "Bérut et al. 2012 - Experimental verification of Landauer's principle linking information and thermodynamics (Nature 483:187-189)",
       "cites", "Abstract read by this session 2026-10-18 (Europe PMC): mean dissipated heat saturates at the bound for long "
       "erasure cycles. Full text read by a QR-004 map sub-agent (equations missed). DOI verified.", stability="canonical")
anchor("NE08", "10.1103/PhysRevLett.113.190601", "Jun, Gavrilov & Bechhoefer 2014 - High-precision test of Landauer's principle in a feedback trap (PRL 113:190601; arXiv:1408.5089)",
       "cites", "Full text read by this session 2026-10-18 (arXiv v1): Table I, 0.71 +/- 0.03 kT full erasure, 0.05 +/- 0.03 "
       "kT no erasure, asymptotic values from a 1/tau fit. DOI verified.", stability="canonical")
tag("NE08", "physics.modern.statistical_mechanics", "primary", "stochastic thermodynamics of information")
tag("NE08", "information_theory.shannon", "secondary", "relative entropy and information content of a memory")
LINKS += [
    ("NE08", "B5", "generalizes", "1",
     "kT ln 2 is the symmetric, quasistatic special case of W >= dF_eq + kT dD(rho||rho_eq) (Esposito & Van den Broeck 2011); "
     "finite time adds an excess ~1/tau (Proesmans et al. 2020). Precision test: Jun et al. 2014."),
    ("NE08", "IT03", "derives from", "1",
     "The generalised bound is written in terms of the relative entropy of the state with respect to equilibrium."),
    ("NE08", "NE03", "derives from", "1.5",
     "Single erasure cycles can cost less than the bound on average-work grounds, consistent with the Jarzynski equality "
     "(Jun et al. 2014)."),
    ("NE08", "TD3", "derives from", "1",
     "All of these bounds are forms of the second law with information counted."),
]

# ===========================================================================
# NE09 — Thermodynamic uncertainty relation: scope and violations
# ===========================================================================
_t = ["thermodynamic uncertainty relation", "TUR", "current fluctuations", "entropy production",
      "nonequilibrium steady state", "Markov jump process", "overdamped dynamics", "precision-cost trade-off",
      "large deviations", "underdamped counterexample", "time-reversal symmetry breaking", "quality factor Q"]
ENTRIES.append(dict(
    id="NE09", title="NE09: Thermodynamic Uncertainty Relation — Scope and Violations (Barato & Seifert 2015; Gingrich et al. 2016)",
    filename="NE09_thermodynamic_uncertainty_relation.md",
    scale="molecular", domain="physics · biology", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "For any current J (steps of a motor, molecules produced) in a non-equilibrium steady state, the relative "
         "uncertainty times the total entropy produced is at least 2k_B: an uncertainty ε requires a cost of at least "
         "2k_BT/ε², independent of how long the output takes to generate (Barato & Seifert 2015, who proved it near "
         "equilibrium and conjectured it in general). Gingrich, Horowitz, Perunov & England (2016) proved it for long "
         "times by a linear-response-like bound on the large-deviation function of currents in Markov jump processes; "
         "Horowitz & Gingrich (2017) proved the finite-time version. It is vacuous at equilibrium.\n\n"
         "SCOPE (Horowitz & Gingrich 2020): continuous-time jump or diffusion processes, with time-independent driving "
         "that does not change sign under time reversal. Each assumption can be relaxed to violate the relation: "
         "time-dependent driving, quantum non-equilibrium dynamics, and dynamics with momenta or magnetic fields; "
         "discrete-time processes can also beat it. Pietzonka (2022) disproved the conjecture that it holds for "
         "underdamped (inertial) Brownian motion, with a thermodynamically consistent model of a pendulum-clock "
         "escapement. Weaker or modified bounds exist for these cases.\n\n"
         "BIOLOGICAL USE: the quality factor Q = (entropy production) × (relative variance), with Q ≥ 2k_B, is used to "
         "compare molecular machines with the bound. The published biological Q values come from fitted kinetic models, "
         "not from measured dissipation (see BIO24, BIO18)."),
        ("Mathematical Form",
         "TUR:  [Var(J_τ) / ⟨J_τ⟩²] · Σ_τ ≥ 2 k_B      (Σ_τ = total entropy produced in time τ)\n"
         "Cost form (Barato & Seifert 2015):  cost ≥ 2 k_BT / ε²,  ε = relative uncertainty of the output\n"
         "Quality factor:  Q ≡ Σ · Var(J)/⟨J⟩² ≥ 2 k_B\n"
         "Valid: continuous-time Markov jump / overdamped diffusion, NESS, time-independent time-symmetric driving\n"
         "Violated: inertia (Pietzonka 2022), time-dependent driving, magnetic fields, quantum transport, discrete time"),
        ("Constraint Category",
         "Thermodynamic (Th): a fluctuation bound — a trade-off between precision and dissipation that holds only within "
         "a stated class of models, unlike second-law mean bounds."),
        ("DS Cross-References",
         "NE04 (Crooks — fluctuation theorems underlie the TUR family). NE05 (near equilibrium the TUR reduces to "
         "linear-response fluctuation–dissipation structure). IT06 (stochastic thermodynamics). NE10 (precision of "
         "oscillators). BIO24 (motor Q values). BIO18 (polymerase and ribosome TUR analyses)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "A product of relative variance and entropy production bounded below by a constant, within a model class; "
         "explicit counterexamples outside it.\n\n" + DIM),
        ("What The Math Says",
         "If a machine is to produce something with small relative scatter, it must burn free energy: halving the "
         "relative error costs four times as much. This holds for machines described by random jumps between states, "
         "or by heavily damped motion, run steadily. It fails for machines with inertia — a pendulum clock beats it — "
         "and for machines driven by a changing schedule, in magnetic fields, or in quantum regimes."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th", _t, "thermodynamic-bound"),
))
anchor("NE09", "10.1103/PhysRevLett.114.158101", "Barato & Seifert 2015 - Thermodynamic uncertainty relation for biomolecular processes (PRL 114:158101)",
       "canonical_authority", "Progenitor. Abstract read by this session 2026-10-18; full text read by a QR-004 map sub-agent. "
       "DOI verified.", role="progenitor")
anchor("NE09", "10.1038/s41567-019-0702-6", "Horowitz & Gingrich 2020 - Thermodynamic uncertainty relations constrain non-equilibrium fluctuations (Nat. Phys. 16:15-20)",
       "canonical_authority", "Perspective. Full text read by this session 2026-10-18 (published version): scope conditions and "
       "the classes that violate them. The article carries an amendment (Box 1; Astumian comment arXiv:2003.10747), not "
       "relied on here. DOI verified.", role="comprehensive_survey")
anchor("NE09", "10.1103/PhysRevLett.116.120601", "Gingrich, Horowitz, Perunov & England 2016 - Dissipation bounds all steady-state current fluctuations (PRL 116:120601)",
       "cites", "Long-time proof. Abstract read by this session 2026-10-18. DOI verified.")
anchor("NE09", "10.1103/PhysRevE.96.020103", "Horowitz & Gingrich 2017 - Proof of the finite-time thermodynamic uncertainty relation for steady-state currents (PRE 96:020103)",
       "cites", "Finite-time proof. Abstract read by this session 2026-10-18. DOI verified.")
anchor("NE09", "10.1103/PhysRevLett.128.130606", "Pietzonka 2022 - Classical pendulum clocks break the thermodynamic uncertainty relation (PRL 128:130606; arXiv:2110.02213)",
       "cites", "Underdamped counterexample. Full text (introduction and model) read by this session 2026-10-18. DOI verified.")
tag("NE09", "physics.modern.statistical_mechanics", "primary", "stochastic thermodynamics of fluctuations")
tag("NE09", "statistics_probability.stochastic_processes", "secondary", "large deviations of currents in Markov processes")
tag("NE09", "biology.molecular", "secondary", "applied to molecular motors and enzymes")
LINKS += [
    ("NE09", "NE04", "derives from", "1.5",
     "The TUR family rests on fluctuation-theorem symmetry of entropy production; proofs bound the large-deviation function "
     "of currents (Gingrich et al. 2016)."),
    ("NE09", "NE05", "analogous to", "2",
     "Near equilibrium, current fluctuations are Gaussian with variance set by dissipation; the TUR extends a "
     "linear-response-like bound far from equilibrium."),
    ("NE09", "IT06", "couples to", "1.5",
     "A core result of stochastic thermodynamics. (IT06's own Fisher-Rao geodesic sentence is under separate review.)"),
    ("NE09", "TD3", "derives from", "1.5",
     "Requires positive entropy production; vacuous at equilibrium."),
]

# ===========================================================================
# NE10 — Free-energy cost of biochemical oscillations and synchronization
# ===========================================================================
_t = ["biochemical oscillator", "phase diffusion", "coherent oscillations", "free-energy cost of timekeeping",
      "cycle affinity", "network topology bound", "synchronization cost", "Kuramoto order parameter",
      "KaiABC circadian clock", "KaiC ATPase", "nonequilibrium phase transition", "model dependence"]
ENTRIES.append(dict(
    id="NE10", title="NE10: Free-Energy Cost of Biochemical Oscillations and Synchronization (Cao et al. 2015; Zhang et al. 2020)",
    filename="NE10_cost_of_oscillation_and_synchronization.md",
    scale="molecular", domain="physics · biology", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Coherence of a single oscillator. Cao, Wang, Ouyang & Tu (2015) studied four types of biochemical oscillator "
         "covering three basic motifs and found the same inverse dependence of the phase-diffusion constant on the free "
         "energy dissipated per period; the number of phase-coherent periods is proportional to the free energy "
         "consumed per period (shown analytically in a noisy-oscillator model, with supporting data). Barato & Seifert "
         "(2017) bounded the number of coherent oscillations of any Markov process by the thermodynamic force (cycle "
         "affinity) and the topology of the network of states, and conjectured an eigenvalue constraint; Ohga, Ito & "
         "Kolchinsky (2023) proved that coherence bound. Oberreiter, Seifert & Barato (2022) conjecture a minimum "
         "free-energy cost of 4π²𝒩k_BT per oscillation for 𝒩 coherent oscillations, from numerical evidence only — "
         "not established.\n\n"
         "Synchronization. Zhang, Cao, Ouyang & Tu (2020) solve a mean-field model of coupled molecular (Markov) clocks: "
         "synchronization costs energy even when the coupling is conservative; it appears through a non-equilibrium "
         "phase transition driven by dissipation, with a critical dissipation below which no synchrony is possible; at "
         "the optimal design the minimum extra dissipation per oscillator per period diverges as 1/(1−r) as the "
         "Kuramoto order parameter r → 1 (their Eq. 15). The analysis is mean-field, all-to-all; no dependence on "
         "spatial dimension or network topology is derived. They predict a relation between KaiC ATPase activity and "
         "synchrony of KaiC hexamers.\n\n"
         "MODEL DEPENDENCE: in continuous phase and limit-cycle models synchronization can lower dissipation. Izumida, "
         "Kori & Seifert (2016): the odd part of the coupling always lowers dissipation on synchronization. Chudak, "
         "Esposito & Ptaszyński (2026): in a two-oscillator Markov model there is no extremum principle — "
         "synchronization can raise or lower dissipation. Burnet et al. (2026, preprint): Cartesian coupling always "
         "lowers it. 'The cost of synchronization' therefore has no single universal form.\n\n"
         "DATA: KaiC hydrolyses about 15 ATP per monomer per day, temperature-invariantly, and its ATPase activity is "
         "directly proportional to circadian frequency across wild type and five period mutants (Terauchi et al. 2007). "
         "No study compares a clock's measured dissipation with its measured coherence against a bound."),
        ("Mathematical Form",
         "Cao et al. 2015:  phase diffusion D ∝ 1 / ΔW  (ΔW = free energy dissipated per period, above a threshold)\n"
         "                 number of coherent periods ∝ ΔW\n"
         "Barato–Seifert 2017 (proved by Ohga et al. 2023): coherence ≤ f(cycle affinity, number of states)\n"
         "Oberreiter et al. 2022 (CONJECTURE): ΔW per oscillation ≥ 4π² 𝒩 k_BT\n"
         "Zhang et al. 2020 (mean-field, optimal design):  W − W₀ ≈ π / [e_g (1 − r)]  → ∞ as r → 1;\n"
         "                 no synchrony below a critical dissipation\n"
         "Terauchi et al. 2007: KaiC ATPase ≈ 15 ATP per monomer per day; activity ∝ circadian frequency"),
        ("Constraint Category",
         "Thermodynamic (Th): free-energy dissipation is required to keep a noisy chemical oscillator coherent, and, in "
         "molecular-clock models, to synchronize a population of them."),
        ("DS Cross-References",
         "Q5 (Information Cost of Synchronization — the published answers, which contradict its (1−λ)² ansatz in form "
         "for molecular clocks). H3 (the original 'phase coherence' reading of λ). B5 (this cost is continuous "
         "dissipation, not Landauer erasure). NE09 (precision–cost trade-offs). BIO24 (motors — measured "
         "energetics of another class of driven molecular machine)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "Coherence (number of coherent cycles, or synchrony r) is bounded by, or bought with, dissipation per period; "
         "in the molecular-clock synchronization model the minimum cost diverges at perfect order.\n\n" + DIM),
        ("What The Math Says",
         "A chemical clock drifts because its reactions are random. Burning more fuel per tick makes the ticks more "
         "regular, roughly in proportion. To make many such clocks tick together, a model of molecular clocks says you "
         "must pay a minimum amount before any synchrony appears at all, and that the price grows without limit as the "
         "clocks approach perfect unison. Other kinds of oscillator models disagree about whether synchrony costs or "
         "saves energy, so the answer depends on what the oscillators are."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th", _t, "thermodynamic-bound"),
))
anchor("NE10", "10.1038/nphys3412", "Cao, Wang, Ouyang & Tu 2015 - The free-energy cost of accurate biochemical oscillations (Nat. Phys. 11:772-778; arXiv:1506.05686)",
       "canonical_authority", "Progenitor of the dissipation-coherence relation. Abstract read by this session 2026-10-18 "
       "(arXiv); full text read by a QR-004 map sub-agent (arXiv version; published version may differ). DOI verified.",
       role="progenitor")
anchor("NE10", "10.1103/PhysRevE.95.062409", "Barato & Seifert 2017 - Coherence of biochemical oscillations is bounded by driving force and network topology (PRE 95:062409)",
       "cites", "Abstract read by this session 2026-10-18; full text read by a QR-004 map sub-agent. DOI verified.")
anchor("NE10", "10.1103/PhysRevLett.131.077101", "Ohga, Ito & Kolchinsky 2023 - Thermodynamic bound on the asymmetry of cross-correlations (PRL 131:077101)",
       "cites", "Abstract read by this session 2026-10-18: proves the Barato-Seifert 2017 coherence bound as an application. DOI verified.")
anchor("NE10", "10.1103/PhysRevE.106.014106", "Oberreiter, Seifert & Barato 2022 - Universal minimal cost of coherent biochemical oscillations (PRE 106:014106)",
       "cites", "Abstract read by this session 2026-10-18: the 4 pi^2 N k_BT bound is a CONJECTURE from numerical evidence. DOI verified.")
anchor("NE10", "10.1038/s41567-019-0701-7", "Zhang, Cao, Ouyang & Tu 2020 - The energy cost and optimal design for synchronization of coupled molecular oscillators (Nat. Phys. 16:95-100; arXiv:2001.10479)",
       "cites", "Abstract read by this session 2026-10-18; full text read by the QR-004 map main session (Eqs. 11, 14, 15; "
       "PMC7363412) and by a sub-agent (sections II.C-E, SI). Mean-field only. DOI verified.")
anchor("NE10", "10.1103/PhysRevE.94.052221", "Izumida, Kori & Seifert 2016 - Energetics of synchronization in coupled oscillators rotating on circular trajectories (PRE 94:052221)",
       "cites", "Abstract read by this session 2026-10-18: odd coupling always decreases dissipation on synchronization. DOI verified.")
anchor("NE10", "arXiv:2512.09718", "Chudak, Esposito & Ptaszyński 2026 - Synchronization of thermodynamically consistent stochastic phase oscillators (PRE 113:034129)",
       "cites", "Abstract read by this session 2026-10-18 (arXiv v3; journal ref PRE 113:034129, DOI 10.1103/3dhj-g2vz): no "
       "extremum-dissipation principle; synchronization may reduce or enhance dissipation.", source="arxiv")
anchor("NE10", "10.1073/pnas.0706292104", "Terauchi et al. 2007 - ATPase activity of KaiC determines the basic timing for circadian clock of cyanobacteria (PNAS 104:16377-16381)",
       "cites", "Full text read by this session 2026-10-18 (PMC2042214): ~15 ATP per KaiC monomer per day; 15-25 ATP per KaiC "
       "per cycle; temperature-invariant; activity proportional to frequency across wild type and five period mutants. DOI verified.",
       stability="canonical")
tag("NE10", "physics.modern.statistical_mechanics", "primary", "nonequilibrium thermodynamics of oscillators")
tag("NE10", "biology.molecular", "secondary", "biochemical clocks, KaiABC")
tag("NE10", "networks_systems.dynamical_systems", "secondary", "synchronization and Kuramoto order parameter")
LINKS += [
    ("NE10", "Q5", "tests", "1",
     "Published answers to Q5's question: in molecular-clock models the minimum synchronization cost diverges as 1/(1-r) "
     "(Zhang et al. 2020), the opposite of Q5's (1-lambda)^2 ansatz; continuous oscillator models show model dependence."),
    ("NE10", "H3", "tensions with", "1.5",
     "Under the original 'phase coherence' reading of lambda, coherence costs rise toward perfect order rather than vanish. "
     "(Under H3's 2026-07-25 definition lambda is not a coherence.)"),
    ("NE10", "B5", "disambiguates from", "1",
     "The cost of coherence and synchronization is continuous dissipation to stay out of equilibrium, not Landauer erasure "
     "of phase differences."),
    ("NE10", "NE09", "couples to", "1.5",
     "Both are precision-dissipation trade-offs for driven Markov systems; the TUR's inertial counterexample is itself a clock."),
]

# ===========================================================================
# BIO17 — Kinetic proofreading
# ===========================================================================
_t = ["kinetic proofreading", "Hopfield", "Ninio", "error fraction", "discrimination free energy",
      "GTP hydrolysis", "EF-Tu", "tRNA selection", "DNA polymerase exonuclease", "speed-error-dissipation trade-off",
      "Maxwell demon", "specificity amplification"]
ENTRIES.append(dict(
    id="BIO17", title="BIO17: Kinetic Proofreading (Hopfield 1974; Ninio 1975)",
    filename="BIO17_kinetic_proofreading.md",
    scale="molecular", domain="biology · physics", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "A single equilibrium discrimination between a right substrate C and a wrong one D, differing in binding free "
         "energy ΔG, gives an error fraction no lower than f₀ = exp(−ΔG/RT). Hopfield (1974; independently Ninio 1975) "
         "showed how to do better. Add a nonspecific intermediate step, driven out of equilibrium by nucleoside "
         "triphosphate hydrolysis, from which either substrate can drop off. The same off-rate discrimination then acts "
         "twice, and the error falls to about f₀²; n proofreading stages give about f₀^(n+1). The driving step must be "
         "pushed out of equilibrium by a factor of at least ~1/f₀; triphosphate hydrolysis provides up to ~10⁸. Hopfield "
         "describes the mechanism as an effective delay, which cannot exist at equilibrium and so must consume free "
         "energy, like a Maxwell demon; he maps it onto tRNA selection with EF-Tu·GTP, amino-acid recognition and DNA "
         "replication.\n\n"
         "Trade-offs. Proofreading resets intermediate complexes, costing time and free energy (Murugan, Huse & Leibler "
         "2012, who also found a regime giving an exponential speed-up for a somewhat larger error). For any effective "
         "proofreading scheme, error reduction is limited by the chemical driving of the proofreading reaction "
         "(Sartori & Pigolotti 2015, from the second law). Reaching the minimum error requires unbounded dissipation or "
         "time (Bennett 1979; not read for this entry). Where real enzymes sit on these trade-offs: BIO18."),
        ("Mathematical Form",
         "Equilibrium discrimination (Hopfield 1974):  f ≥ f₀ = K_D/K_C = exp(−ΔG_CD / RT)\n"
         "One driven proofreading step:               f ≈ f₀²   (n steps: f ≈ f₀^(n+1))\n"
         "Driving requirement:                         (m′/m) ≳ (1/f₀)·(m′/m)_equilibrium\n"
         "Sartori & Pigolotti 2015: error reduction bounded by the chemical driving of the proofreading reaction"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): accuracy beyond the equilibrium discrimination limit must be bought with "
         "free-energy dissipation (and time)."),
        ("DS Cross-References",
         "BIO5 (Central Dogma — proofreading is how replication and translation reach their fidelity). BIO6 "
         "(Michaelis–Menten — Hopfield's starting scheme). NE07 (proofreading is not Landauer erasure of an error bit; "
         "its cost is set by the driving). BIO18 (speed over accuracy). TD3 (second law)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "Error is bounded below by exp(−ΔG/RT) at equilibrium; each driven stage multiplies the bound by f₀, at a free-"
         "energy and time cost.\n\n" + DIM),
        ("What The Math Says",
         "An enzyme that tells right from wrong by stickiness alone makes errors at a rate set by the stickiness "
         "difference. If, after the first binding, the molecule is pushed by burning fuel into a second waiting state "
         "from which wrong partners tend to fall off, the same difference is used twice and the error rate is roughly "
         "squared. The price is fuel and time; the fuel must push hard enough, and perfect accuracy would need "
         "unlimited amounts of either."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "thermodynamic-bound"),
))
anchor("BIO17", "10.1073/pnas.71.10.4135", "Hopfield 1974 - Kinetic proofreading: a new mechanism for reducing errors in biosynthetic processes requiring high specificity (PNAS 71:4135-4139)",
       "canonical_authority", "Progenitor. Full text pp. 4135-4137 read by this session 2026-10-18 from the PMC page scans "
       "(PMC434344): f0 = exp(-dG/RT), f ~ f0^2, driving factor >~ 1/f0, delay consumes free energy, EF-Tu GTP mapping. "
       "DOI verified.", role="progenitor", stability="canonical")
anchor("BIO17", "10.1016/S0300-9084(75)80139-8", "Ninio 1975 - Kinetic amplification of enzyme discrimination (Biochimie 57:587-595)",
       "canonical_authority", "Independent progenitor (Hopfield-Ninio scheme). NOT read: search summary only (QR-004 map). "
       "DOI verified on Crossref.", role="progenitor", stability="canonical", confidence="medium")
anchor("BIO17", "10.1073/pnas.1119911109", "Murugan, Huse & Leibler 2012 - Speed, dissipation, and error in kinetic proofreading (PNAS 109:12034-12039)",
       "cites", "Abstract read by this session 2026-10-18; full text read by a QR-004 map sub-agent (equations missed). DOI verified.")
anchor("BIO17", "10.1103/PhysRevX.5.041039", "Sartori & Pigolotti 2015 - Thermodynamics of error correction (PRX 5:041039)",
       "cites", "Abstract read by this session 2026-10-18: error reduction limited by the chemical driving of the proofreading "
       "reaction; three regimes. DOI verified.")
tag("BIO17", "biology.molecular", "primary", "fidelity of replication and translation")
tag("BIO17", "chemistry.biochemistry", "secondary", "enzyme kinetics and specificity")
tag("BIO17", "physics.modern.statistical_mechanics", "secondary", "nonequilibrium discrimination")
LINKS += [
    ("BIO17", "BIO5", "implements", "1",
     "Kinetic proofreading (with exonuclease editing and mismatch repair for DNA) is how replication and translation reach "
     "error rates far below the equilibrium discrimination limit."),
    ("BIO17", "BIO6", "generalizes", "1.5",
     "Hopfield starts from the Michaelis-Menten discrimination scheme and adds a driven, nonspecific intermediate."),
    ("BIO17", "TD3", "derives from", "1.5",
     "Beating equilibrium discrimination requires driving out of equilibrium; the error bound follows from the second law "
     "(Sartori & Pigolotti 2015)."),
    ("BIO17", "NE07", "couples to", "2",
     "Proofreading's cost is set by the free energy of the driving step, not by Landauer erasure of an 'error bit'."),
]

# ===========================================================================
# BIO18 — Speed over accuracy in biological error correction
# ===========================================================================
_t = ["speed-accuracy trade-off", "T7 DNA polymerase", "E. coli ribosome", "tRNA selection", "first-passage time",
      "error-cost bound", "IleRS", "kinetic tuning", "tolerable error", "proofreading cost"]
ENTRIES.append(dict(
    id="BIO18", title="BIO18: Speed over Accuracy in Biological Error Correction (Banerjee et al. 2017; Yu et al. 2022)",
    filename="BIO18_speed_over_accuracy_error_correction.md",
    scale="molecular", domain="biology · physics", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Banerjee, Kolomeisky & Igoshin (2017) analysed the speed and accuracy of DNA replication (T7 DNA polymerase) "
         "and tRNA selection by the E. coli ribosome with a discrete-state first-passage framework fitted to measured "
         "kinetic rates. Both systems tend to optimise speed rather than accuracy, as long as the error level is "
         "tolerable; some kinetic parameters sit in a suboptimal region where changing them would improve both; the "
         "energetic cost of proofreading adds a further constraint. Per the QR-004 map sub-agent's full-text reading: "
         "the minimum achievable error is ~150× (T7) and ~50× (ribosome) lower than the actual one, but reaching it "
         "would make the process ~3,500× and ~500× slower.\n\n"
         "Yu, Kolomeisky & Igoshin (2022) identify an error–cost bound for proofreading networks, set by the difference "
         "between transition-state energies. T7 DNA polymerase sits in the immediate proximity of the bound; E. coli "
         "isoleucyl-tRNA synthetase is close to it but held back by the need for speed; the E. coli ribosome operates "
         "in a high-dissipation regime, possibly to speed up protein production.\n\n"
         "STATUS: contested — one group's models fitted to kinetic data; no measured dissipation."),
        ("Mathematical Form",
         "Quantities: error η = (wrong product rate)/(right product rate); mean first-passage time τ per incorporation;\n"
         "  proofreading cost = free energy spent per product\n"
         "Banerjee 2017 (per map sub-agent): η_min ≈ η/150 (T7), η/50 (ribosome), at τ ≈ 3,500× and 500× slower\n"
         "Yu 2022: error–cost bound fixed by transition-state energy differences; T7 ≈ on the bound; ribosome far above"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): where real proofreaders sit on the speed–accuracy–dissipation trade-off "
         "defined by BIO17."),
        ("DS Cross-References",
         "BIO17 (kinetic proofreading). BIO5 (Central Dogma — fidelity numbers). NE09 (TUR analyses of copy machines). "
         "BIO23 (whether running near a bound buys fitness is open)."),
        ("Mathematical Archetype",
         "Mathematical archetype: optimization-principle\n\n"
         "Fitted kinetic parameters lie near a speed optimum subject to an error ceiling, not at minimum error or "
         "minimum dissipation.\n\n" + DIM),
        ("What The Math Says",
         "Cells could copy DNA and build proteins far more accurately than they do, but it would take hundreds to "
         "thousands of times longer. Models fitted to the measured reaction rates say the copying machines are tuned to "
         "be fast, with errors kept just low enough. One polymerase sits almost exactly on the best achievable "
         "error-for-cost line; the ribosome spends much more energy than that line requires, apparently to go faster."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "optimization-principle"),
))
anchor("BIO18", "10.1073/pnas.1614838114", "Banerjee, Kolomeisky & Igoshin 2017 - Elucidating interplay of speed and accuracy in biological error correction (PNAS 114:5183-5188)",
       "canonical_authority", "Progenitor. Abstract read by this session 2026-10-18; full text (PMC5441828) read by a QR-004 "
       "map sub-agent, the source of the 150x/3,500x and 50x/500x figures. DOI verified.", role="progenitor")
anchor("BIO18", "10.1098/rsif.2021.0883", "Yu, Kolomeisky & Igoshin 2022 - The energy cost and optimal design of networks for biological discrimination (J. R. Soc. Interface 19:20210883)",
       "cites", "Abstract read by this session 2026-10-18 (T7 near the bound; IleRS near but speed-limited; ribosome "
       "high-dissipation). DOI verified.")
tag("BIO18", "biology.molecular", "primary", "fidelity and speed of replication and translation")
tag("BIO18", "chemistry.biochemistry", "secondary", "enzyme kinetic optimisation")
LINKS += [
    ("BIO18", "BIO17", "tests", "1.5",
     "Places T7 DNA polymerase and the E. coli ribosome on the proofreading speed-error-cost trade-off: tuned for speed with "
     "tolerable error (one group's fitted models)."),
    ("BIO18", "BIO5", "couples to", "1.5",
     "Explains why replication and translation error rates are not lower: lower error would cost large factors in speed."),
]

# ===========================================================================
# BIO19 — Thermodynamics of biochemical copying
# ===========================================================================
_t = ["biochemical copying", "persistent copy", "mutual information", "readout molecule", "template polymerization",
      "copolymerization", "free energy stored in correlations", "logical reversibility of copying",
      "Ouldridge", "ten Wolde", "measurement cost", "copy accuracy"]
ENTRIES.append(dict(
    id="BIO19", title="BIO19: Thermodynamics of Biochemical Copying (Ouldridge, Govern & ten Wolde 2017)",
    filename="BIO19_thermodynamics_of_biochemical_copying.md",
    scale="molecular", domain="biology · physics", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Copying is logically reversible and has no minimum dissipation in principle (NE07). What copying does require "
         "is set by persistence. Ouldridge, Govern & ten Wolde (2017, PRX): a canonical biochemical readout network, "
         "like a measurement, generates correlations between readout and receptor; generating correlations that persist "
         "after the direct interaction ends requires free energy kT × I (I = mutual information, in nats), and if those "
         "correlations are not used to extract work but lost, that amount sets a lower bound on dissipation. For general "
         "input such networks cannot reach this bound even with arbitrarily slow reactions or weak driving; they face an "
         "accuracy–dissipation trade-off worse than the bound, although the cost stays close to it unless accuracy is "
         "very high. Systems that do not make persistent copies are not bound by equivalent limits.\n\n"
         "Ouldridge & ten Wolde (2017, PRL), persistent polymer copies separated from their templates: template–copy "
         "interactions do not contribute to the overall reaction thermodynamics and cannot drive the process; the "
         "copy's equilibrium state is template-independent, so extra work is needed for specificity; and mixing copies "
         "from different templates makes template–copy correlations unexploitable, reducing the free energy stored. "
         "Andrieux & Gaspard (2008) relate the dissipation of copolymerization, with or without templates, to the "
         "information generated."),
        ("Mathematical Form",
         "Persistent correlation (PRX 2017):  free energy required ≥ kT · I(copy; source)\n"
         "  dissipated only if the correlation is lost without use;  stored (recoverable in principle) otherwise\n"
         "Readout networks (PRX 2017):  w_chem / n_copy ≥ kT · I   (efficiency η = kT·I / (w_chem/n_copy) ≤ 1)\n"
         "Copying itself:  y := y + x  is logically reversible (NE07) — no floor in principle"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): the free-energy cost of making and keeping a copy is set by the mutual "
         "information it holds and by its persistence, not by a per-bit Landauer erasure cost."),
        ("DS Cross-References",
         "NE07 (copying is logically reversible). BIO5 (transcription, translation and replication are template "
         "copying). NE06 (England — the replicator's information is not a Landauer erasure cost). INFO4 (mutual "
         "information). BIO21 (sensing as measurement)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "A lower bound kT × (mutual information) on the free energy needed to create persistent correlations; "
         "dissipated only if the correlations are discarded unused.\n\n" + DIM),
        ("What The Math Says",
         "Writing a copy onto a blank page is not erasing anything, so Landauer's price does not apply. But a copy that "
         "lasts after it leaves its template is a correlation the world would not otherwise have, and building it takes "
         "free energy — about kT for every nat of shared information. That energy is stored in the copy, and is lost as "
         "heat only if the copy's information is later thrown away unused."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "thermodynamic-bound"),
))
anchor("BIO19", "10.1103/PhysRevX.7.021004", "Ouldridge, Govern & ten Wolde 2017 - Thermodynamics of computational copying in biochemical systems (PRX 7:021004; arXiv:1503.00909)",
       "canonical_authority", "Progenitor. Abstract, introduction and key passages read by this session 2026-10-18 (arXiv v4): "
       "persistent correlations need free energy kT*I; lost correlations set a dissipation bound; readout networks cannot "
       "reach it for general input. Full text (first two-thirds) read by a QR-004 map sub-agent. DOI verified.",
       role="progenitor")
anchor("BIO19", "10.1103/PhysRevLett.118.158103", "Ouldridge & ten Wolde 2017 - Fundamental costs in the production and destruction of persistent polymer copies (PRL 118:158103; arXiv:1609.05554)",
       "cites", "Abstract and introduction read by this session 2026-10-18. DOI verified.")
anchor("BIO19", "10.1073/pnas.0802049105", "Andrieux & Gaspard 2008 - Nonequilibrium generation of information in copolymerization processes (PNAS 105:9516-9521)",
       "cites", "Abstract read by this session 2026-10-18; full text read by a QR-004 map sub-agent. DOI verified.")
tag("BIO19", "biology.molecular", "primary", "template copying in replication, transcription, translation and signalling")
tag("BIO19", "physics.modern.statistical_mechanics", "secondary", "information thermodynamics")
tag("BIO19", "information_theory.shannon", "secondary", "mutual information as stored free energy")
LINKS += [
    ("BIO19", "NE07", "derives from", "1",
     "Copying onto a blank register is logically reversible (Bennett); the remaining cost is the free energy kT*I a "
     "persistent correlation stores."),
    ("BIO19", "BIO5", "constrains", "1.5",
     "Sets what template copying must pay: free energy for persistent, accurate copies, not a Landauer cost per base."),
    ("BIO19", "NE06", "tensions with", "1.5",
     "Corrects the 'copying one bit costs at least kT ln 2' reading of replicator thermodynamics."),
    ("BIO19", "INFO4", "derives from", "1.5",
     "The bound is kT times the mutual information between copy and source."),
]

# ===========================================================================
# BIO20 — Physical limits of chemical sensing (Berg-Purcell)
# ===========================================================================
_t = ["Berg-Purcell limit", "chemoreception", "molecule counting noise", "receptor correlation time",
      "concentration sensing precision", "maximum likelihood sensing", "integration time", "diffusion-limited sensing",
      "bacterial chemotaxis", "signalling noise"]
ENTRIES.append(dict(
    id="BIO20", title="BIO20: Physical Limits of Chemical Sensing (Berg & Purcell 1977)",
    filename="BIO20_physical_limits_of_chemical_sensing.md",
    scale="cellular", domain="biology · physics", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "Berg & Purcell (1977) showed that the precision with which a cell can measure a chemical concentration is "
         "limited by the random arrival of molecules at its receptors by diffusion: counting noise. Time averaging over "
         "an integration time T helps, but only in proportion to the number of independent molecule arrivals. Bialek & "
         "Setayeshgar (2005) generalised the argument to signalling inside the cell and argued that experiments are "
         "consistent with performance approaching these limits. Endres & Wingreen (2009) derived a lower limit than "
         "Berg–Purcell by applying maximum likelihood to the receptor occupancy time series: only the unoccupied "
         "intervals carry information about concentration. The review by ten Wolde, Becker, Ouldridge & Mugler (2016) "
         "sets out how the number of receptors, the receptor correlation time and the downstream integration time "
         "together impose the limit.\n\n"
         "SCOPE: this is a counting (statistical) limit, not a thermodynamic one. The energy cost of approaching it is a "
         "separate matter (BIO21)."),
        ("Mathematical Form",
         "Berg–Purcell (order of magnitude):  (δc / c)² ~ 1 / (D a c T)\n"
         "  D = diffusion constant, a = receptor (or cell) size, c = concentration, T = integration time\n"
         "Maximum likelihood (Endres & Wingreen 2009): lower than Berg–Purcell; uses unbound intervals only"),
        ("Constraint Category",
         "Informatic (In): a statistical bound on concentration estimation set by molecule-arrival noise."),
        ("DS Cross-References",
         "NE05 (fluctuation–dissipation — Bialek & Setayeshgar's generalisation). INFO4 (information about the "
         "environment). BIO21 (energy cost of beating equilibrium limits). BIO25 (E. coli is far from this limit)."),
        ("Mathematical Archetype",
         "Mathematical archetype: statistical-distribution\n\n"
         "Poisson counting statistics of molecule arrivals set the relative variance of the concentration estimate.\n\n"
         + DIM),
        ("What The Math Says",
         "A cell measures how much of a chemical is around by counting molecules that bump into its receptors. Arrivals "
         "are random, so the count fluctuates, and the cell's estimate is only as good as the number of independent "
         "arrivals it averages over. More receptors, faster diffusion, higher concentration and longer averaging all help. "
         "This is a limit from counting statistics, not from energy."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "statistical-distribution"),
))
anchor("BIO20", "10.1016/S0006-3495(77)85544-6", "Berg & Purcell 1977 - Physics of chemoreception (Biophys. J. 20:193-219)",
       "canonical_authority", "Progenitor. NOT read by this session (no abstract retrievable); citation and venue confirmed on "
       "Crossref 2026-10-18 and as cited by Endres & Wingreen 2009 and Bialek & Setayeshgar 2005 (abstracts read).",
       role="progenitor", stability="canonical", confidence="medium")
anchor("BIO20", "10.1007/s10955-015-1440-5", "ten Wolde, Becker, Ouldridge & Mugler 2016 - Fundamental limits to cellular sensing (J. Stat. Phys. 162:1395-1424)",
       "canonical_authority", "Review. Abstract read by this session 2026-10-18; ~93% of full text read by a QR-004 map sub-agent. "
       "DOI verified.", role="comprehensive_survey")
anchor("BIO20", "10.1073/pnas.0504321102", "Bialek & Setayeshgar 2005 - Physical limits to biochemical signaling (PNAS 102:10040-10045)",
       "cites", "Abstract read by this session 2026-10-18. DOI verified.")
anchor("BIO20", "10.1103/PhysRevLett.103.158101", "Endres & Wingreen 2009 - Maximum likelihood and the single receptor (PRL 103:158101)",
       "cites", "Abstract read by this session 2026-10-18. DOI verified.")
tag("BIO20", "biology.physiology", "primary", "sensory precision of cells")
tag("BIO20", "physics.modern.statistical_mechanics", "secondary", "diffusion and counting noise")
tag("BIO20", "statistics_probability.inference", "secondary", "concentration estimation, maximum likelihood")
LINKS += [
    ("BIO20", "NE05", "derives from", "1.5",
     "Bialek & Setayeshgar 2005 generalise Berg-Purcell to intracellular signalling via fluctuation-dissipation arguments."),
    ("BIO20", "INFO4", "couples to", "2",
     "Sensing precision bounds the information a cell can acquire about concentration."),
]

# ===========================================================================
# BIO21 — Energy cost of sensing and adaptation
# ===========================================================================
_t = ["sensory adaptation", "energy-speed-accuracy relation", "E. coli chemotaxis", "receptor methylation",
      "SAM hydrolysis", "adaptation error", "push-pull network", "resource allocation", "information-theoretic minimum",
      "nonequilibrium sensing", "Lan", "Govern and ten Wolde"]
ENTRIES.append(dict(
    id="BIO21", title="BIO21: Energy Cost of Sensing and Adaptation (Lan et al. 2012; Govern & ten Wolde 2014)",
    filename="BIO21_energy_cost_of_sensing_and_adaptation.md",
    scale="cellular", domain="biology · physics", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Adaptation. Lan, Sartori, Neumann, Sourjik & Tu (2012) analysed a stochastic model of the minimal negative-"
         "feedback network behind many sensory adaptation systems: adaptation is necessarily dissipative, and continuous "
         "energy consumption is needed to keep the adapted state. They derive an energy–speed–accuracy relation: the "
         "dissipation rate is proportional to the adaptation speed times the logarithm of the inverse adaptation error. "
         "In E. coli one fuel molecule (SAM, ~29 kT) is hydrolysed per methylation–demethylation cycle; for ~10⁴ receptors "
         "and a ~10 s adaptation time the cost is ~3 × 10⁴ kT/s (~10³ ATP/s), about 5–10% of the cost of driving one "
         "flagellar motor. As cells de-energise, adaptation slows (half-time up ~3-fold) while accuracy is kept, as "
         "predicted. Wang, Lan & Tang (2015) solved the model exactly and discussed the relation in a more general "
         "setting (the QR-004 map's sub-agent reports that the relation needs modifying and no strict lower bound was "
         "found).\n\n"
         "Information accounting. Sartori, Granger, Lee & Horowitz (2014): during adaptation, information about the past "
         "is erased while information about the present is written; entropy production exceeds the old information "
         "erased, and the energetic cost is bounded by the new information written. For E. coli receptors under binary "
         "concentration changes the energy consumed is in the range of the information-theoretic minimum — slightly more "
         "than twice it (Discussion).\n\n"
         "Sensing. Govern & ten Wolde (2014, PRL): equilibrium signalling networks cannot beat the sensing limit set by "
         "the number of receptors; a push-pull network must dissipate at least ~1 kT per receptor to do so. Govern & ten "
         "Wolde (2014, PNAS): receptors with their integration time, readout molecules, and energy are three resource "
         "classes that each set a limit and cannot compensate for one another; the E. coli chemotaxis network allocates "
         "them about equally.\n\n"
         "All E. coli figures are model-based, with literature parameters; none is calorimetric."),
        ("Mathematical Form",
         "Energy–speed–accuracy (Lan et al. 2012, Eq. 7):  Ẇ ≈ (c₀ σ_a²) · ω_m · ln(ε₀ / ε)\n"
         "  equivalently ε ≈ ε₀ exp(−α ΔW) below a critical ΔW_c (ΔW = dissipation per methylation time)\n"
         "E. coli: ~3 × 10⁴ kT/s ≈ 10³ ATP/s for ~10⁴ receptors, adaptation time ~10 s\n"
         "Sartori et al. 2014: cost ≥ new information written; E. coli ≈ 2× the minimum\n"
         "Govern & ten Wolde 2014: beating the equilibrium receptor limit needs ≳ 1 kT per receptor"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): accurate adaptation and better-than-equilibrium sensing require continuous "
         "dissipation; energy is a separate, non-substitutable sensing resource."),
        ("DS Cross-References",
         "BIO20 (counting limits). BIO10 (homeostasis — adaptation is a regulatory function with an energy cost). F1 "
         "(Ashby — regulation; the formal thermodynamic route is information thermodynamics, not 'kT ln 2 per bit "
         "suppressed'). NE09 (precision–cost trade-offs). BIO25 (behavioural use of the information)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "Adaptation error falls exponentially with dissipation per adaptation time; sensing precision beyond the "
         "equilibrium limit requires a minimum dissipation per receptor.\n\n" + DIM),
        ("What The Math Says",
         "A bacterium that keeps re-zeroing its senses so it can notice new changes has to burn fuel continuously to do "
         "it. The faster and more accurately it re-zeroes, the more it burns; accuracy improves exponentially with the "
         "fuel spent. For E. coli this comes to roughly a thousand ATP per second — a few per cent of what one flagellar "
         "motor uses — and, in a model with measured parameters, about twice the information-theoretic minimum."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "thermodynamic-bound"),
))
anchor("BIO21", "10.1038/nphys2276", "Lan, Sartori, Neumann, Sourjik & Tu 2012 - The energy-speed-accuracy trade-off in sensory adaptation (Nat. Phys. 8:422-428)",
       "canonical_authority", "Progenitor. Full text read by this session 2026-10-18 (NIH author manuscript PMC3378065): Eq. 7, "
       "Eq. 8, SAM ~29 kT, ~3e4 kT/s for ~1e4 receptors, 5-10% of a flagellar motor, de-energisation experiment. DOI verified.",
       role="progenitor")
anchor("BIO21", "10.1371/journal.pcbi.1003974", "Sartori, Granger, Lee & Horowitz 2014 - Thermodynamic costs of information processing in sensory adaptation (PLoS Comput. Biol. 10:e1003974)",
       "cites", "Abstract read by this session 2026-10-18; the QR-004 map main session read abstract and Discussion ('slightly "
       "larger than twice'); full text read by a sub-agent. DOI verified.")
anchor("BIO21", "10.1103/PhysRevLett.113.258102", "Govern & ten Wolde 2014 - Energy dissipation and noise correlations in biochemical sensing (PRL 113:258102)",
       "cites", "Abstract read by this session 2026-10-18 (>= 1 k_BT per receptor to beat the equilibrium limit). DOI verified.")
anchor("BIO21", "10.1073/pnas.1411524111", "Govern & ten Wolde 2014 - Optimal resource allocation in cellular sensing systems (PNAS 111:17486-17491)",
       "cites", "Abstract read by this session 2026-10-18; full text read by a QR-004 map sub-agent. DOI verified.")
anchor("BIO21", "arXiv:1505.07526", "Wang, Lan & Tang 2015 - Energy dissipation in an adaptive molecular circuit (J. Stat. Mech. 2015, P07025)",
       "cites", "Abstract read by this session 2026-10-18 (exact NESS; ESA relation discussed in a more general setting); full "
       "text read by a QR-004 map sub-agent, who reports the ESA relation needs modification and no strict lower bound.",
       source="arxiv", confidence="medium")
tag("BIO21", "biology.physiology", "primary", "cost of sensory adaptation and signalling")
tag("BIO21", "physics.modern.statistical_mechanics", "secondary", "nonequilibrium steady states of signalling networks")
tag("BIO21", "biology.molecular", "secondary", "chemotaxis receptor methylation")
LINKS += [
    ("BIO21", "BIO20", "generalizes", "1.5",
     "Adds the energy dimension to sensing limits: beating the equilibrium receptor limit needs >= ~1 kT per receptor; "
     "energy is a separate resource class (Govern & ten Wolde 2014)."),
    ("BIO21", "BIO10", "implements", "1.5",
     "Sensory adaptation is a homeostatic feedback that must dissipate continuously to hold the adapted state (Lan et al. 2012)."),
    ("BIO21", "F1", "couples to", "2",
     "Regulation has an energy cost, but through information thermodynamics (measurement and erasure accounting), not a "
     "fixed kT ln 2 per bit of disturbance suppressed."),
    ("BIO21", "NE09", "analogous to", "2",
     "Both are precision-dissipation trade-offs; the ESA relation is model-specific, not a theorem like the TUR."),
]

# ===========================================================================
# BIO22 — Metabolic cost of neural information (Laughlin 1998)
# ===========================================================================
_t = ["metabolic cost of information", "ATP per bit", "blowfly photoreceptor", "chemical synapse", "graded signals",
      "spike coding", "neural energy efficiency", "distributed coding", "Laughlin", "energy budget of signalling"]
ENTRIES.append(dict(
    id="BIO22", title="BIO22: Metabolic Cost of Neural Information (Laughlin, de Ruyter van Steveninck & Anderson 1998)",
    filename="BIO22_metabolic_cost_of_neural_information.md",
    scale="cellular", domain="biology · neuroscience", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Laughlin, de Ruyter van Steveninck & Anderson (1998) estimated, from biophysical measurements on cells of the "
         "blowfly retina, the ATP needed to transmit known amounts of information. Transmitting a bit across a chemical "
         "synapse costs about 10⁴ ATP molecules; graded signals in an interneuron or a photoreceptor, or spike coding, "
         "cost about 10⁶–10⁷ ATP per bit. Energy consumption is several orders of magnitude above the thermodynamic "
         "minimum. In noise-limited signalling a weak, low-capacity pathway transmits information more economically, "
         "which favours distributing information over many pathways.\n\n"
         "At ~20 kT per ATP these figures are roughly 3 × 10⁵ to 3 × 10⁸ times kT ln 2. The gap is not a failure to "
         "approach Landauer: signalling and encoding are not erasures (B5, NE07), and the cost is set by ion pumping "
         "against membrane leak.\n\n"
         "Related: Attwell & Laughlin (2001) budget excitatory signalling in rodent grey matter (action potentials ~47%, "
         "postsynaptic effects ~34%, resting potential ~13%, glutamate recycling ~3%) and predict distributed codes with "
         "≤ 15% of neurons active; the QR-004 map notes these budget figures were later revised (not checked here).\n\n"
         "STATUS: contested — a single study, read at abstract level only."),
        ("Mathematical Form",
         "Chemical synapse:                        ~10⁴ ATP per bit\n"
         "Graded signals (photoreceptor, interneuron), spike coding: ~10⁶–10⁷ ATP per bit\n"
         "In multiples of kT ln 2 (ATP ≈ 20 kT):  ~3 × 10⁵ – 3 × 10⁸"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): an empirical energy cost per bit of neural signalling, far above any erasure "
         "bound."),
        ("DS Cross-References",
         "B5 (Landauer — not the relevant floor; a spike is not an erasure). BIO9 (Hodgkin–Huxley — the ionic currents "
         "whose pumping sets the cost). D1 (Stevens' law — neural encoding). X6 (neural networks). BIO23 (cellular "
         "computation efficiency)."),
        ("Mathematical Archetype",
         "Mathematical archetype: linear-proportionality\n\n"
         "Energy per bit as an empirical ratio of metabolic rate to information rate; it varies by orders of magnitude "
         "with the signalling mechanism.\n\n" + DIM),
        ("What The Math Says",
         "Measured in a fly's eye, sending one bit of information across a synapse costs about ten thousand ATP "
         "molecules, and sending it as a graded or spiking signal costs a million to ten million. That is hundreds of "
         "thousands to hundreds of millions of times Landauer's number — but Landauer is the wrong yardstick here, "
         "because sending a signal does not erase anything. The cost is pumping ions back across leaky membranes."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "linear-proportionality"),
))
anchor("BIO22", "10.1038/236", "Laughlin, de Ruyter van Steveninck & Anderson 1998 - The metabolic cost of neural information (Nat. Neurosci. 1:36-41)",
       "canonical_authority", "Progenitor. Abstract read by this session 2026-10-18 (NCBI E-utilities, PMID 10195106); full text "
       "not available to this session. DOI verified on Crossref.", role="progenitor", stability="canonical", confidence="medium")
anchor("BIO22", "10.1097/00004647-200110000-00001", "Attwell & Laughlin 2001 - An energy budget for signaling in the grey matter of the brain (J. Cereb. Blood Flow Metab. 21:1133-1145)",
       "cites", "Abstract read by this session 2026-10-18. Budget later revised per the QR-004 map (Howarth, Gleeson & Attwell "
       "2012; search summary, not checked). DOI verified.", confidence="medium")
tag("BIO22", "biology.neuroscience", "primary", "energetics of neural coding")
tag("BIO22", "information_theory.shannon", "secondary", "information rates of neural signals")
tag("BIO22", "biology.physiology", "secondary", "ATP budgets of signalling")
LINKS += [
    ("BIO22", "B5", "disambiguates from", "1",
     "Neural costs of 1e4-1e7 ATP per bit are not a near-miss of Landauer's floor: signalling and encoding are not erasures."),
    ("BIO22", "BIO9", "couples to", "1.5",
     "The cost per bit is set by restoring the ionic gradients that Hodgkin-Huxley currents run down."),
    ("BIO22", "D1", "couples to", "2",
     "Neural encoding of stimulus intensity has a measured metabolic cost per bit."),
    ("BIO22", "X6", "constrains", "2",
     "Energy per bit favours low-rate, distributed coding in real neural networks."),
]

# ===========================================================================
# BIO23 — Energetic efficiency of cellular computation, and the open question
# ===========================================================================
_t = ["cellular computation efficiency", "translation energetics", "generalised Landauer bound",
      "free energy per amino acid", "physical bioenergetics", "energy budgets of cells", "open question",
      "fitness cost of energy", "Kempes", "near-bound operation"]
ENTRIES.append(dict(
    id="BIO23", title="BIO23: Energetic Efficiency of Cellular Computation, and Whether Running Near a Bound Matters (Kempes et al. 2017; Yang et al. 2021)",
    filename="BIO23_energetic_efficiency_cellular_computation.md",
    scale="cellular", domain="biology · physics", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Kempes, Wolpert, Cohen & Pérez-Mercader (2017) define the computational efficiency of translation as the free "
         "energy expended per amino-acid operation. It outperforms the best supercomputers by several orders of "
         "magnitude and is only about an order of magnitude worse than the (generalised) Landauer bound; the useful "
         "efficiency depends strongly on cell size and architecture. The QR-004 map's sub-agent reports, from the full "
         "text, ~26× for translation in the body and ~165× for DNA replication; sensing and signalling are not counted.\n\n"
         "Across the processes measured, cells run far above Landauer: ~10× (translation) to ~10⁸× (neural signalling, "
         "BIO22). Against process-specific bounds some machines come within a few times (T7 polymerase, BIO18; E. coli "
         "adaptation, BIO21; kinesin, BIO24), with all such figures from fitted models.\n\n"
         "THE OPEN QUESTION. Yang et al. (2021) state that the energetic costs and constraints of specific cellular "
         "processes remain largely unknown, and ask explicitly whether cells operate near these limits and, if so, how "
         "energetic constraints affect cellular function — including whether energetic costs become fitness costs. The "
         "best current evidence (BIO18) is that error-correcting machines are tuned for speed with tolerable error, not "
         "for minimum energy. Rigorous Landauer or TUR results at organism or ecosystem scale were not found (QR-004 map)."),
        ("Mathematical Form",
         "Efficiency of translation (Kempes et al. 2017): free energy per amino-acid operation ≈ 10× a generalised "
         "Landauer bound (abstract; ~26× per sub-agent)\n"
         "Range across processes:  ~10× (translation) … ~10⁸× (neural signalling) above kT ln 2 per bit"),
        ("Constraint Category",
         "Thermodynamic/Informatic (Th-In): how far cellular information processing sits above thermodynamic floors; the "
         "fitness consequence is an open question."),
        ("DS Cross-References",
         "B5 (Landauer — the benchmark, and why it is often the wrong one). E2 (Koomey — the engineering analogue). BIO22 "
         "(neural costs). BIO17, BIO18 (proofreading and speed). BIO21 (adaptation). BIO24 (motors). QR-004 in "
         "docs/QUESTIONS_RAISED_LOG.md."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "Measured or estimated costs expressed as multiples of a lower bound; the multiple ranges over seven orders of "
         "magnitude depending on the process.\n\n" + DIM),
        ("What The Math Says",
         "How wasteful are cells, measured against physics' floors? Building proteins costs about ten times the floor — "
         "far better than any computer. Nerve signalling costs up to a hundred million times it, but signalling is not "
         "the kind of operation that floor prices. Whether evolution rewards getting closer to the floor is not known; "
         "the evidence so far says cells are tuned to be fast and good enough, not frugal."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th-In", _t, "thermodynamic-bound"),
))
anchor("BIO23", "10.1098/rsta.2016.0343", "Kempes, Wolpert, Cohen & Pérez-Mercader 2017 - The thermodynamic efficiency of computations made in cells across the range of life (Phil. Trans. R. Soc. A 375:20160343)",
       "canonical_authority", "Progenitor. Abstract read by this session 2026-10-18 ('about an order of magnitude worse than the "
       "Landauer bound'); full text (arXiv:1706.05043) read by a QR-004 map sub-agent (~26x translation, ~165x replication). "
       "DOI verified.", role="progenitor")
anchor("BIO23", "10.1073/pnas.2026786118", "Yang et al. 2021 - Physical bioenergetics: energy fluxes, budgets, and constraints in cells (PNAS 118:e2026786118)",
       "open_in_literature", "Abstract read by this session 2026-10-18; Introduction and 'Open Question' sections read by the "
       "QR-004 map main session (PMC8255778). Frames whether cells operate near physical limits, and whether energetic costs "
       "become fitness costs, as open. DOI verified.")
tag("BIO23", "biology.physiology", "primary", "cellular energy budgets")
tag("BIO23", "physics.modern.statistical_mechanics", "secondary", "thermodynamic bounds as benchmarks")
tag("BIO23", "biology.evolution", "secondary", "open question of fitness costs of energy")
LINKS += [
    ("BIO23", "B5", "tests", "1",
     "Cells run 10x (translation) to 1e8x (neural signalling) above Landauer; for many processes Landauer is not the relevant "
     "floor (copying, signalling are not erasures)."),
    ("BIO23", "E2", "analogous to", "2",
     "Engineering's distance-to-Landauer trend has a cellular counterpart; translation beats supercomputers per operation by "
     "orders of magnitude (Kempes et al. 2017)."),
    ("BIO23", "BIO22", "couples to", "1.5",
     "Neural signalling is the far end of the range of measured cellular costs per bit."),
    ("BIO23", "BIO18", "couples to", "1.5",
     "Best evidence on what near-bound operation buys: speed with tolerable error, not minimum energy."),
]

# ===========================================================================
# BIO24 — Molecular-motor energetics
# ===========================================================================
_t = ["molecular motor energetics", "F1-ATPase efficiency", "kinesin-1", "hidden dissipation",
      "Harada-Sasa equality", "fluctuation-response violation", "thermodynamic uncertainty relation", "quality factor Q",
      "mechanochemical coupling", "transport efficiency"]
ENTRIES.append(dict(
    id="BIO24", title="BIO24: Molecular-Motor Energetics (Toyabe et al. 2010, 2011; Ariga et al. 2018; Hwang & Hyeon 2018)",
    filename="BIO24_molecular_motor_energetics.md",
    scale="molecular", domain="biology · physics", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "F1-ATPase. Toyabe et al. (2010) applied a non-equilibrium equality (Harada–Sasa) with electrorotation to single "
         "F1-ATPase motors: the heat flow through the probe plus the work against the load almost equals the free-energy "
         "change of one ATP hydrolysis, implying near-100% efficiency in a thermally fluctuating environment. Toyabe et "
         "al. (2011) drove reversible 120° steps by controlling torque and ATP chemical potential and found the maximum "
         "work per step nearly equal to the free energy of one ATP over a broad range of conditions: ~100% transduction "
         "efficiency with tight mechanochemical coupling.\n\n"
         "Kinesin-1. Ariga, Tomishige & Mizuno (2018) measured heat dissipation from violation of the fluctuation–response "
         "relation of an optically trapped probe: dissipation plus work did not add up to the input free energy, "
         "indicating large hidden dissipation, mostly internal to the motor. Per the QR-004 map's sub-agent: ~80% of the "
         "input lost internally at 2 pN, ~19% efficiency at maximum power.\n\n"
         "TUR quality factors. Hwang & Hyeon (2018) computed Q (heat × squared relative error of displacement, bound "
         "2k_BT) from motility data via kinetic models: for kinesin-1, Q approaches the bound near 4 pN across 1 μM–10 mM "
         "ATP; motors are 'semi-optimized' under cellular conditions. Per the map's sub-agent: Q ≈ 7.2 k_BT for "
         "kinesin-1 at cellular conditions, and ≈ 7.7, 9.1 and 13 for F1, dynein and myosin V.\n\n"
         "STATUS: contested. The efficiency results are measured; the Q values come from fitted models, and 'semi-"
         "optimized' is an interpretation without a baseline."),
        ("Mathematical Form",
         "F1-ATPase (Toyabe 2010, 2011): stall work per 120° step ≈ Δμ_ATP → efficiency ≈ 100%\n"
         "Harada–Sasa equality: heat dissipated through a probe = (friction) × [⟨v⟩² + integrated violation of the\n"
         "  fluctuation–response relation]; hidden dissipation = input free energy − (probe heat + work)\n"
         "TUR quality factor:  Q = Q̇·τ · Var(x)/⟨x⟩² ≥ 2 k_BT\n"
         "Kinesin-1: Q → 2 k_BT near f ≈ 4 pN (Hwang & Hyeon 2018)"),
        ("Constraint Category",
         "Thermodynamic (Th): measured free-energy transduction of single motors, and their distance from the TUR bound."),
        ("DS Cross-References",
         "NE09 (TUR — the bound Q is compared with). NE05 (fluctuation–response relations; Harada–Sasa measures their "
         "violation). TD8 (Carnot — the macroscopic efficiency ceiling; motors are isothermal chemical engines). BIO23 "
         "(cellular efficiency)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "Efficiency ≤ 1 of chemical free energy into work, and Q ≥ 2k_BT; F1 sits at the first, kinesin near the second "
         "only at specific load.\n\n" + DIM),
        ("What The Math Says",
         "The rotary motor F1-ATPase turns almost all the free energy of each ATP into mechanical work — close to perfect "
         "efficiency, measured directly. The walking motor kinesin is different: most of its fuel energy is lost inside "
         "the molecule. Measured against the 'precision costs energy' bound, kinesin comes close only at one particular "
         "load; under cellular conditions it is a few times above it, according to model fits."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th", _t, "thermodynamic-bound"),
))
anchor("BIO24", "10.1103/PhysRevLett.104.198103", "Toyabe et al. 2010 - Nonequilibrium energetics of a single F1-ATPase molecule (PRL 104:198103)",
       "canonical_authority", "Progenitor (single-molecule energetics via Harada-Sasa). Abstract read by this session 2026-10-18; "
       "full text read by a QR-004 map sub-agent. DOI verified.", role="progenitor")
anchor("BIO24", "10.1073/pnas.1106787108", "Toyabe et al. 2011 - Thermodynamic efficiency and mechanochemical coupling of F1-ATPase (PNAS 108:17951-17956)",
       "cites", "Abstract read by this session 2026-10-18. DOI verified.")
anchor("BIO24", "10.1103/PhysRevLett.121.218101", "Ariga, Tomishige & Mizuno 2018 - Nonequilibrium energetics of molecular motor kinesin (PRL 121:218101)",
       "cites", "Abstract read by this session 2026-10-18 (large hidden, mostly internal, dissipation); full text read by a "
       "QR-004 map sub-agent (~80% at 2 pN). DOI verified.")
anchor("BIO24", "10.1021/acs.jpclett.7b03197", "Hwang & Hyeon 2018 - Energetic costs, precision, and transport efficiency of molecular motors (J. Phys. Chem. Lett. 9:513-520; arXiv:1710.03499)",
       "cites", "Abstract read by this session 2026-10-18 (journal and arXiv): Q approaches the bound near 4 pN for kinesin-1; "
       "semi-optimized. The Q values 7.2/7.7/9.1/13 come from a QR-004 map sub-agent's full-text reading. DOI verified.")
tag("BIO24", "biology.molecular", "primary", "molecular motors")
tag("BIO24", "physics.modern.statistical_mechanics", "secondary", "single-molecule stochastic energetics")
LINKS += [
    ("BIO24", "NE09", "tests", "1.5",
     "Motor Q values (from fitted models) range from near the TUR bound (kinesin near 4 pN) to several times above it."),
    ("BIO24", "NE05", "derives from", "1.5",
     "Hidden dissipation is measured from violations of the fluctuation-response relation (Harada-Sasa)."),
    ("BIO24", "TD8", "constrains", "2",
     "Isothermal chemical engines are not Carnot engines; F1-ATPase reaches ~100% of the free energy of ATP, kinesin far less."),
]

# ===========================================================================
# BIO25 — Information-limited chemotaxis
# ===========================================================================
_t = ["E. coli chemotaxis", "information rate", "gradient climbing speed", "behavioural performance bound",
      "information-limited behaviour", "chemosensing accuracy", "internal signalling noise", "molecule counting limit",
      "Mattingly", "sensory-motor efficiency"]
ENTRIES.append(dict(
    id="BIO25", title="BIO25: Information-Limited Chemotaxis in E. coli (Mattingly et al. 2021; 2026)",
    filename="BIO25_information_limited_chemotaxis.md",
    scale="cellular", domain="biology · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Mattingly, Kamino, Machta & Emonet (2021) derive a theoretical limit on the maximum gradient-climbing speed "
         "achievable for a given rate of information acquisition, then measure both in E. coli. Cells make behavioural "
         "decisions with much less than the 1 bit needed to know whether they are swimming up-gradient, but use that "
         "information efficiently, performing near the limit. Per the QR-004 map's sub-agent: about 65% of the maximum "
         "drift speed. The bound is information-theoretic, not thermodynamic; energy is not part of it.\n\n"
         "Mattingly et al. (Nature Physics, 2026; arXiv:2407.07264) ask what limits the information acquired. Comparing "
         "information rates from molecule arrivals (the physical limit) with those from chemotaxis signalling activity, "
         "measured in single cells across background concentrations, they find E. coli encode about two orders of "
         "magnitude less information than the physical limit: chemosensing is limited by internal noise in signal "
         "processing, not by the physics of molecule diffusion (BIO20).\n\n"
         "STATUS: contested — one group; follow-up read at abstract level only."),
        ("Mathematical Form",
         "Drift speed bound:  v_drift ≤ v_max(İ),  İ = information acquisition rate (bits/s)\n"
         "E. coli (2021): near the bound (~65% per map sub-agent)\n"
         "E. coli (2026): encoded information ≈ 10⁻² × the molecule-counting limit"),
        ("Constraint Category",
         "Informatic (In): behavioural performance bounded by the rate of information acquisition."),
        ("DS Cross-References",
         "BIO20 (counting limits — E. coli sits far below them). INFO3 (channel capacity — information rate as the "
         "limiting resource). BIO21 (energy cost of the same pathway). BIO23 (efficiency of cellular computation)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "An upper bound on a performance measure (drift speed) set by an information rate; the system reaches a large "
         "fraction of it while acquiring far less information than physics allows.\n\n" + DIM),
        ("What The Math Says",
         "How fast a bacterium can climb towards food depends on how much information it gathers about the direction of "
         "the gradient. E. coli gathers very little — much less than one bit per decision — but uses it almost as well "
         "as possible. What holds it back is noise in its own signalling chemistry, which wastes about 99% of the "
         "information physically available; not counting noise, and not energy."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "thermodynamic-bound"),
))
anchor("BIO25", "10.1038/s41567-021-01380-3", "Mattingly, Kamino, Machta & Emonet 2021 - Escherichia coli chemotaxis is information limited (Nat. Phys. 17:1426-1431; arXiv:2102.11732)",
       "canonical_authority", "Progenitor. Abstract read by this session 2026-10-18 (arXiv); full text (PMC8758097, ~92%) read by "
       "a QR-004 map sub-agent (~65% of maximum drift speed). DOI verified.", role="progenitor")
anchor("BIO25", "10.1038/s41567-025-03111-4", "Mattingly, Kamino, Ong, Kottou, Emonet & Machta 2026 - Chemotaxing E. coli do not count single molecules (Nat. Phys.; arXiv:2407.07264)",
       "cites", "Abstract read by this session 2026-10-18 (arXiv v3, which gives this DOI): two orders of magnitude less "
       "information than the physical limit; internal noise. Journal volume and pages not checked.", confidence="medium")
tag("BIO25", "biology.physiology", "primary", "bacterial chemotaxis behaviour")
tag("BIO25", "information_theory.shannon", "secondary", "information rates bounding behaviour")
LINKS += [
    ("BIO25", "BIO20", "tests", "1.5",
     "E. coli encode ~100x less information than the molecule-counting limit; internal noise, not diffusion, limits them."),
    ("BIO25", "INFO3", "derives from", "2",
     "The behavioural bound is set by the rate of information acquisition through the signalling pathway."),
    ("BIO25", "BIO21", "couples to", "2",
     "The same pathway's adaptation has a measured-parameter energy cost; the behavioural bound itself is not thermodynamic."),
]

# ===========================================================================
# Links from corrected entries (owner-approved 2026-10-18)
# ===========================================================================
LINKS += [
    ("B5", "NE07", "couples to", "1",
     "Which operations pay the bound: only logically irreversible ones on known data; copying and measurement can be free in "
     "principle (Bennett)."),
    ("B5", "NE08", "couples to", "1",
     "Generalised (relative-entropy) and finite-time forms of the bound; precision test Jun et al. 2014."),
    ("NE06", "BIO19", "tensions with", "1.5",
     "Replicator copying is not a Landauer erasure: persistent copies store free energy kT*I (Ouldridge et al. 2017)."),
    ("BIO5", "BIO17", "couples to", "1",
     "Replication and translation fidelity rely on kinetic proofreading (Hopfield 1974), exonuclease editing and mismatch repair."),
    ("Q5", "NE10", "tensions with", "1",
     "The published synchronization cost (Zhang et al. 2020, mean-field molecular clocks) diverges at full synchrony; Q5's "
     "ansatz vanishes there."),
    ("D1", "BIO22", "couples to", "1.5",
     "The measured metabolic cost of neural encoding: ~1e4-1e7 ATP per bit (Laughlin et al. 1998)."),
    ("EM11", "NE07", "disambiguates from", "1.5",
     "Joule heating is finite-speed resistive dissipation; reversible computation has no kT ln 2 floor."),
]
