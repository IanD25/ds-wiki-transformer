"""
Glossary seed — 20 load-bearing words + sense entries — 2026-05-04

Inserts:
  - 20 disambiguation_page entries (one per load-bearing word)
  - 18 defined_term sense entries (only for senses NOT already covered by
    existing wiki entries — for the rest, the disambig page points at the
    existing entry)
  - Anchors for each defined_term entry (canonical_authority where known)
  - Internal links: disambig pages link to senses; senses cross-link via
    'disambiguates from'

Owner pre-approved: see conversation 2026-05-04 (Maldacena deep-research
follow-up).

Run: python3 scripts/migrations/m0_glossary_seed_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-glossary-seed-2026-05-04"


# ============================================================================
# DISAMBIGUATION PAGES (one per load-bearing word)
# ============================================================================
DISAMBIG: list[dict] = [
    # ------- High-priority words -------
    {
        "id": "gloss_fisher_information",
        "title": "Fisher information (disambiguation)",
        "domain": "information_theory.shannon · mathematics",
        "senses": [
            ("[[g:fisher_information_classical|Classical Fisher information]]", "Matrix of expectations of pairwise log-likelihood derivatives on a parameter manifold of probability distributions; unique by Chentsov.", "IT05, IT08, M6, P21"),
            ("[[g:fisher_information_quantum_bures|Quantum Fisher information / Bures metric]]", "Smallest member of the Petz family of quantum monotone metrics on density matrices; non-unique in the quantum case.", "GT04 (used implicitly via quantum relative entropy)"),
            ("Bogoliubov-Kubo-Mori (BKM) metric", "Unique self-dual member of the Petz family.", "(no current wiki entry; see Petz 1996)"),
        ],
        "why": "Three distinct mathematical objects share the phrase 'Fisher information.' The classical case (Chentsov uniqueness) and the quantum case (Petz family classification) are not the same; equating them is the category error flagged by the Maldacena deep-research pass 2026-05-04.",
    },
    {
        "id": "gloss_effective_dimension",
        "title": "Effective dimension / d_eff (disambiguation)",
        "domain": "information_theory.shannon · physics.modern.statistical_mechanics",
        "senses": [
            ("[[g:effective_dimension_mattingly|Mattingly d_eff]]", "Σ_r r·Ω_r from optimal maximally-informative discrete prior on parameter-manifold edges (Mattingly et al. 2018 PNAS).", "(Sethna lineage; not the project's d_eff)"),
            ("[[g:effective_dimension_pr_fim|Participation ratio of FIM eigenvalue spectrum]]", "(Σλ)²/Σλ² applied to a Fisher information matrix. The Constrained Critical Attractor framework's d_eff. Renamed PR_FIM going forward.", "Ax2, M6, X-series, the CCA framework"),
            ("[[g:effective_dimension_hausdorff|Hausdorff / fractal dimension]]", "Geometric measure of point sets; box-counting / Hausdorff measure.", "(Mandelbrot 1982; used in P6 falsified context)"),
            ("[[g:effective_dimension_spectral_network|Spectral / network dimension]]", "d_s = -2 d log P_return(t) / d log t from random walk return probability.", "(Alexander-Orbach 1982)"),
            ("Sethna sloppy-models 'effective dimensionality'", "Deliberately not a single scalar — uses hyperribbon widths and FIM eigenvalue spectrum directly.", "(Quinn 2023 Rep. Prog. Phys.)"),
        ],
        "why": "At least five distinct mathematical objects share the phrase 'effective dimension' or symbol 'd_eff'. The Sethna group itself avoids collapsing the FIM spectrum to a scalar; Mattingly's 2018 PNAS paper uses d_eff with a different formula than the participation ratio used in the project's CCA framework. Wiki conjectures referencing 'D_eff' must pin which sense applies.",
    },
    {
        "id": "gloss_relative_entropy",
        "title": "Relative entropy (disambiguation)",
        "domain": "information_theory.shannon",
        "senses": [
            ("[[g:relative_entropy_classical_kl|Classical Kullback-Leibler divergence]]", "D_KL(p‖q) = Σ p log(p/q) on probability distributions.", "IT03"),
            ("Quantum relative entropy (Umegaki / von Neumann)", "S(ρ‖σ) = Tr[ρ ln ρ - ρ ln σ] on density matrices.", "IT04"),
            ("[[g:relative_entropy_modular_hamiltonian|Modular-Hamiltonian first-law usage (Jacobson 2016)]]", "δS_EE = δ⟨H_mod⟩/T entanglement-equilibrium condition; same vocabulary, different operational role from classical KL or quantum Umegaki.", "GT10"),
        ],
        "why": "The Fisher-gravity chain in earlier wiki framings stacked 'relative entropy' across these three distinct objects. The M0 audit 2026-04-08 + Maldacena deep-research pass 2026-05-04 confirmed no theorem-level bridge composes the chain. Use the specific sense, never the bare phrase.",
    },
    {
        "id": "gloss_anomalous_dimension",
        "title": "Anomalous dimension / η (disambiguation)",
        "domain": "physics.modern.statistical_mechanics",
        "senses": [
            ("[[g:anomalous_dimension_critical|Standard anomalous dimension η_critical]]", "Critical exponent of the two-point correlation function: C(r) ~ r^(-(d-2+η)). For 2D Ising η=1/4 exact.", "(textbook stat mech; cf. STAT3 prose)"),
            ("[[g:anomalous_dimension_cca_isotropy_iota|CCA isotropy indicator (renamed ι)]]", "Zipf-tail log-log slope of the FIM eigenvalue spectrum; the Constrained Critical Attractor framework's project-internal observable. NOT η_critical.", "X-series, CCA experiments"),
        ],
        "why": "Wiki/CCA usage of 'η' collides with the standard stat-mech anomalous-dimension critical exponent. The two are mathematically related at criticality (Vinayak 2014) but not the same number. Rename to ι (iota) per CCA_TERMINOLOGY_RENAME_PROPOSAL.md.",
    },
    {
        "id": "gloss_information_geometry",
        "title": "Information geometry (disambiguation)",
        "domain": "mathematics.geometry_topology · information_theory.shannon",
        "senses": [
            ("Fisher-Rao classical metric", "Unique invariant Riemannian metric on classical statistical manifolds; Chentsov uniqueness.", "IT08, P21"),
            ("[[g:information_geometry_amari_dual_connections|Amari α-geometries]]", "Dual ±1 connections coupled to Fisher metric; α-divergences; e/m-flat coordinates.", "(Amari 1985; not yet a dedicated wiki entry)"),
            ("Ruppeiner thermodynamic geometry", "Negative-Hessian-of-entropy metric on equilibrium state space. Brody-Rivier 1995: equals Fisher-Rao on Gibbs canonical family in thermodynamic limit.", "BR04"),
            ("[[g:information_geometry_petz_quantum_family|Petz quantum monotone-metric family]]", "Family of Riemannian metrics on density matrices parameterized by operator-monotone functions; Bures/BKM/RLD/Wigner-Yanase as distinguished members. NO single canonical metric in the quantum case.", "(Petz 1996; not yet a dedicated wiki entry)"),
            ("Information geometry of phase transitions", "Fisher-Rao on a low-dimensional thermodynamic-coupling manifold; scalar curvature divergence at criticality.", "(Janke-Johnston-Kenna 2004; Brody-Rivier 1995)"),
        ],
        "why": "Five distinct mathematical structures share this label. Chentsov uniqueness applies only to the classical case (extended by Ay-Jost-Lê-Schwachhöfer 2015 to general statistical manifolds). The quantum case admits a parameterized FAMILY (Petz 1996), not a unique metric.",
    },
    {
        "id": "gloss_observer",
        "title": "Observer (disambiguation)",
        "domain": "physics.modern.quantum_mechanics · physics.modern.general_relativity",
        "senses": [
            ("[[g:observer_algebraic_clpw|Algebraic observer (CLPW / type-II crossed-product)]]", "Observer's clock Hamiltonian as the auxiliary variable converting a type-III von Neumann factor to type II via crossed product (Witten 2112.12828; CLPW 2206.10780).", "(Maldacena 2412.14014 builds on this)"),
            ("[[g:observer_thermodynamic|Thermodynamic / Gibbons-Hawking observer]]", "Static observer in a stationary spacetime experiencing horizon temperature; Unruh-style.", "HB05"),
            ("[[g:observer_qm_measurement|QM measurement observer]]", "External system performing a projective or POVM measurement on a quantum system; foundations-of-QM sense.", "(QM2, QM5 prose)"),
            ("[[g:observer_classical_gr|Classical GR coordinate observer]]", "Worldline carrying a frame; reference frame for coordinate measurements; classical, no mass/energy budget.", "(implicit in classical GR entries)"),
        ],
        "why": "'Observer' is used for at least four distinct constructions, and the Maldacena 2024 'Real Observers Solve Imaginary Problems' result depends on the algebraic / mass-and-energy-carrying sense specifically. Conflating with the classical-GR coordinate observer drops the load-bearing physical content.",
    },
    {
        "id": "gloss_emergent_spacetime",
        "title": "Emergent spacetime (disambiguation)",
        "domain": "physics.modern.general_relativity · physics.modern.quantum_gravity",
        "senses": [
            ("AdS/CFT bulk reconstruction", "Bulk operators reconstructed from boundary CFT operators; Ryu-Takayanagi minimal surfaces; HKLL smearing kernel; quantum error correction reading.", "BR02, HB07, T6"),
            ("Jacobson 1995 thermodynamic", "Einstein equation as equation of state from Clausius δQ=T·dS on local Rindler horizons + Bekenstein-Hawking area-entropy.", "GT01"),
            ("Jacobson 2016 entanglement equilibrium", "Linearized Einstein equations from δS_EE=0 condition on geodesic balls + modular-Hamiltonian-as-boost assumption (fails for some QFTs per Casini-Galante-Myers 2016).", "GT10"),
            ("Verlinde entropic gravity", "Newtonian gravity as entropic force from holographic-screen equipartition (2011); MOND-like dark-matter in dS (2017). Contested in published literature.", "GT02"),
            ("Padmanabhan holographic equipartition", "Field equations as thermodynamic identity on local Rindler horizons; Friedmann equation from N_sur−N_bulk equipartition.", "GT03"),
            ("Bianconi 2025 quantum-relative-entropy gravity", "Action principle: S(ρ‖σ) on density-matrix-valued metric; Einstein equations as Euler-Lagrange equations. Single-author program; quantum, not classical, Fisher.", "GT04"),
            ("Sloppy models / parameter-space compression", "Sethna 2013 et seq. — explicitly does NOT make an emergent-spacetime claim; the wiki should not interpolate one.", "M6, Ax2 (as parameter-space-diagnostic only)"),
        ],
        "why": "Seven distinct programs each making different mathematical claims. Only AdS/CFT bulk reconstruction and Jacobson 2016 produce theorem-level Einstein-like dynamics, and both are linearized only and within stated regimes. Verlinde and Bianconi are contested or single-author programs. The Sethna lineage explicitly does not endorse a spacetime claim; framing it as such is a wiki-internal interpolation.",
    },
    {
        "id": "gloss_holography",
        "title": "Holography (disambiguation)",
        "domain": "physics.modern.quantum_gravity",
        "senses": [
            ("Bekenstein-Bousso holographic principle", "Information / entropy in a region bounded by area-divided-by-4 in Planck units. Foundational principle.", "HB01, HB03, HB08"),
            ("AdS/CFT correspondence", "Specific duality: d-dim CFT on boundary of AdS_{d+1}; concrete realization of holography with proven examples (N=4 SYM, ABJM).", "BR02"),
            ("Loose / metaphorical 'holography'", "Used in adjacent contexts (de Sitter holography conjectures, flat-space holography, celestial holography) where the duality is conjectural or under construction. Use with caveats.", "(scattered prose; tag explicitly when used)"),
        ],
        "why": "The bound principle, the specific AdS/CFT duality, and metaphorical extensions are commonly conflated. Citing 'holography' as an established framework when the meaning is the conjectural extension is overclaim. Maldacena 2024-2025 interview emphasizes dS/CFT remains 'intrinsically approximate' — should not be cited as established.",
    },
    {
        "id": "gloss_entropy",
        "title": "Entropy (disambiguation)",
        "domain": "physics · information_theory.shannon",
        "senses": [
            ("Boltzmann / coarse-grained / thermodynamic", "S = k_B ln W or S = -k_B Σ p_i log p_i in equilibrium; the second-law quantity.", "TD-cluster, B-cluster"),
            ("Shannon entropy", "H(X) = -Σ p(x) log p(x) on a classical random variable.", "INFO1, IT01"),
            ("von Neumann entropy", "S(ρ) = -Tr(ρ log ρ) on a density matrix; the quantum / fine-grained sense; coincides with Shannon entropy of eigenvalue distribution.", "IT02"),
            ("Bekenstein-Hawking entropy", "S = A/(4G_N ℏ) for a black hole horizon area A.", "HB02"),
            ("[[g:entropy_entanglement|Entanglement entropy (von Neumann of reduced density matrix)]]", "S(ρ_A) for ρ_A = Tr_B|ψ⟩⟨ψ|; quantifies entanglement between subsystems A and B. Used heavily in the gravity-from-entanglement program.", "(used implicitly in BR03, GT10, HB07; no dedicated wiki entry yet)"),
            ("Generalized entropy S_gen", "S_gen = A/(4G_N) + S_outside-the-horizon-matter; updated by the island formula in the BH information paradox program.", "(HB09 prose mentions; no dedicated entry)"),
        ],
        "why": "Same word, six distinct mathematical objects. Maldacena 2024-2025 interview is explicit: 'this notion of entropy [von Neumann] is intimately connected with the Shannon entropy' — that's a connection between two specific objects, not 'entropy unifies things.' Wiki entries must pin which sense is meant, especially in chains crossing classical/quantum/gravitational regimes.",
    },
    {
        "id": "gloss_quantum_corrections",
        "title": "Quantum corrections (disambiguation)",
        "domain": "physics.modern.quantum_field_theory",
        "senses": [
            ("[[g:quantum_corrections_perturbative|Small perturbative corrections]]", "Loop expansion in ℏ or 1/N around a classical saddle point; usually small.", "(generic QFT)"),
            ("[[g:quantum_corrections_regime_changing|Regime-changing corrections]]", "Quantum effects that qualitatively change classical predictions. Example: extremal BHs near zero temperature where one mode of geometry becomes quantum mechanical (Iliesiu-Turiaci 2020s).", "(GT-cluster prose)"),
            ("[[g:quantum_corrections_nonperturbative|Non-perturbative effects (instantons, wormholes)]]", "Effects invisible in any finite-order perturbation expansion; e.g., wormhole contributions to gravity path integrals.", "(BR-cluster prose, Maldacena 2024-2025 wormhole discussion)"),
        ],
        "why": "Maldacena 2024-2025 distinguishes these explicitly. 'Small quantum corrections' versus 'corrections that change the regime' versus 'genuinely non-perturbative effects' have different load-bearing roles in any quantum-gravity argument. Wiki entries citing 'quantum corrections' should specify which.",
    },
    # ------- Medium-priority words (disambig only, no separate sense entries yet) -------
    {
        "id": "gloss_modular_hamiltonian",
        "title": "Modular Hamiltonian (disambiguation)",
        "domain": "physics.modern.quantum_field_theory",
        "senses": [
            ("Modular Hamiltonian H_mod = -log ρ_A", "For reduced density matrix ρ_A on a subalgebra; appears in the modular flow of Tomita-Takesaki theory; reduces to a boost generator for half-space in CFT vacuum (Bisognano-Wichmann).", "GT10"),
            ("Subregion modular flow", "Flow generated by H_mod; underlies the 'crossed product' construction in algebraic-observer work.", "(CLPW 2022-2023, see also gloss_observer_algebraic_clpw)"),
        ],
        "why": "The Bisognano-Wichmann assumption — that H_mod equals the boost generator on small geodesic balls in a CFT vacuum — is what Casini-Galante-Myers 2016 showed FAILS for relevant operators with low conformal dimensions. Citations of 'modular Hamiltonian' should specify whether the boost-generator property is needed or assumed.",
    },
    {
        "id": "gloss_phase_transition",
        "title": "Phase transition (disambiguation)",
        "domain": "physics.modern.statistical_mechanics",
        "senses": [
            ("Continuous (second-order) transition", "Free energy / its derivatives are continuous; correlation length diverges; universal critical exponents (η, ν, β...).", "(2D Ising, Potts q≤4, BKT-like physics)"),
            ("First-order transition", "Discontinuity in entropy / order parameter; latent heat; finite correlation length at T_c; metastability.", "(2D Potts q≥5, water-vapor)"),
            ("Infinite-order (BKT) transition", "Vortex-pair unbinding; correlation length grows as exp(c/√(T-T_c)); essential singularity in free energy.", "(2D XY model)"),
        ],
        "why": "These have qualitatively different phenomenology and different mathematical signatures. CCA experiments distinguish first-order from continuous via curve-shape signatures (Phase E 2026-04-20, Outcome C). Conjectures about 'phase transitions' must specify the order.",
    },
    {
        "id": "gloss_criticality",
        "title": "Criticality (disambiguation)",
        "domain": "physics.modern.statistical_mechanics",
        "senses": [
            ("Critical point of a continuous transition", "Scale-invariant fixed point of the renormalization group; divergent correlation length; universal exponents.", "(textbook: Cardy 1996, Goldenfeld 1992)"),
            ("Pseudo-critical point of a first-order transition", "Apparent peak in susceptibility / specific heat that does NOT correspond to a true critical fixed point — a finite-size artifact of the latent-heat-driven transition.", "(Janke 1992; relevant for CCA Phase E q≥5)"),
            ("Self-organized criticality (SOC)", "Power-law correlations in driven dissipative systems without parameter tuning. Different mechanism from equilibrium critical points.", "(Bak-Tang-Wiesenfeld 1987; not currently in wiki)"),
        ],
        "why": "The word 'critical' often masks whether the system is at a true RG fixed point or near a first-order transition. Especially relevant for CCA-1c claims about discriminating transition order — the discrimination IS between true criticality and pseudo-criticality.",
    },
    {
        "id": "gloss_monotonicity",
        "title": "Monotonicity (disambiguation)",
        "domain": "physics · information_theory.shannon · mathematics",
        "senses": [
            ("Entropy non-decrease (second law / GSL)", "S_total never decreases under closed-system evolution; Bekenstein-Hawking + outside matter for black holes.", "HB09, IT06"),
            ("FIM monotonicity under sufficient statistics (Chentsov)", "Pulling back the Fisher metric through a Markov morphism gives the same metric; defines the classical Fisher metric uniquely.", "P21"),
            ("Petz monotone metrics under CPTP maps (quantum)", "Quantum analog: a Riemannian metric on density matrices is 'monotone' if it contracts under any quantum channel. Petz 1996 classifies all such.", "(see gloss_information_geometry_petz_quantum_family)"),
            ("RG monotonicity (c-theorem, F-theorem, a-theorem)", "Specific scalar quantities decrease under RG flow in particular dimensions and theory classes.", "(Zamolodchikov 1986 c-theorem)"),
            ("D_eff under coarse-graining (P7 — FALSIFIED)", "Project-internal claim that effective dimension decreases monotonically under coarse-graining. Partially falsified in own Phase 1 results: participation ratio does NOT satisfy this.", "P7 (status: Falsified-for-PR)"),
        ],
        "why": "The wiki's P7 monotonicity claim was falsified for participation ratio per Phase 1 own-tests. Conflating the project's specific 'D_eff under coarse-graining' claim with the established mathematical monotonicity statements (Chentsov, Petz, second law) is the same kind of vocabulary stack the deep-research pass diagnosed.",
    },
    {
        "id": "gloss_coarse_graining",
        "title": "Coarse-graining (disambiguation)",
        "domain": "physics.modern.statistical_mechanics",
        "senses": [
            ("Block-spin / Kadanoff renormalization", "Replace a block of N spins with a single effective spin; iterate; defines a flow in coupling space.", "(Kadanoff 1966, Wilson 1971)"),
            ("Wilsonian momentum-shell integration", "Integrate out high-momentum modes; track flow of effective action.", "(Wilson 1971)"),
            ("General averaging / projection (Mori-Zwanzig)", "Project full microscopic dynamics onto a slow subspace; produces non-Markovian effective dynamics.", "M4"),
            ("Information-geometric coarse-graining (Sethna)", "Manifold-Boundary Approximation: optimal projection onto lower-dimensional model manifold via FIM eigenvalue hierarchy.", "(Mattingly et al. 2018; Sethna lineage)"),
        ],
        "why": "These produce different effective theories from the same microscopic input. RG-flow claims and information-geometric-compression claims are different mathematical operations even when both are called 'coarse-graining.'",
    },
    {
        "id": "gloss_duality",
        "title": "Duality (disambiguation)",
        "domain": "physics.modern.quantum_field_theory",
        "senses": [
            ("AdS/CFT correspondence", "Conjectured (but well-supported in concrete examples) equivalence between bulk gravity in AdS and boundary CFT.", "BR02"),
            ("Kramers-Wannier duality (2D Ising)", "High-T ↔ low-T self-duality on the square-lattice Ising model.", "(Kramers-Wannier 1941)"),
            ("Electric-magnetic duality (Maxwell, Seiberg)", "E ↔ B in vacuum Maxwell; Seiberg duality between gauge theories.", "EM cluster, (Seiberg 1995)"),
            ("Particle-vortex duality, etc.", "Various 2+1d field-theory dualities relating different microscopic descriptions of the same IR physics.", "(modern condensed matter)"),
        ],
        "why": "'Duality' is used both for proven exact equivalences and for conjectural correspondences. Citing one as evidence for another is generally not justified; each duality has its own derivation status.",
    },
    {
        "id": "gloss_symmetry",
        "title": "Symmetry (disambiguation)",
        "domain": "physics.modern.classical_mechanics",
        "senses": [
            ("Global symmetry", "Action invariant under transformation parameterized globally (translation, rotation in flat space, U(1) phase rotation).", "AM-cluster"),
            ("Gauge / local symmetry", "Action invariant under transformation parameterized point-by-point; necessitates connection field. NOT a 'symmetry' in the same sense — it's a redundancy of description.", "EM, GV cluster"),
            ("Spontaneously broken symmetry", "Symmetry of the Hamiltonian / Lagrangian but not of the ground state; Goldstone modes.", "(Anderson 1958, Nambu 1960)"),
            ("Modular / generalized / categorical symmetries", "Modern non-invertible / higher-form generalizations.", "(2020s literature; not in wiki)"),
        ],
        "why": "Distinguishing global from gauge symmetry is foundational; conflating them obscures whether physical degrees of freedom or redundancies are at issue. Modern non-invertible symmetries are a separate framework that should not be conflated with classical Noether-style global symmetries.",
    },
    {
        "id": "gloss_connection",
        "title": "Connection (disambiguation)",
        "domain": "mathematics.geometry_topology.differential_geometry",
        "senses": [
            ("Levi-Civita connection (Riemannian geometry)", "Unique torsion-free connection compatible with a given metric; underlies covariant derivative in GR.", "(GR cluster)"),
            ("Amari ±1 (e and m) connections (information geometry)", "Pair of dual connections on a statistical manifold; flat in exponential / mixture coordinates respectively.", "(see gloss_information_geometry_amari_dual_connections)"),
            ("Gauge connection / vector potential", "Connection on a principal bundle; gauge field A_μ in physics.", "(EM cluster, Yang-Mills theory)"),
        ],
        "why": "The same word covers three distinct mathematical structures. The information-geometric ±1 connections are NOT compatible with a metric in the Levi-Civita sense — they're the dual structure on a statistical manifold.",
    },
    {
        "id": "gloss_fluctuation",
        "title": "Fluctuation (disambiguation)",
        "domain": "physics.modern.statistical_mechanics",
        "senses": [
            ("Thermal fluctuation", "Variance of an observable in a thermal ensemble; ~k_B T at high temperature; vanishes as T→0 in classical systems.", "(Reif, Callen)"),
            ("Quantum fluctuation", "Variance from non-commuting observables in a pure state; survives at T=0; uncertainty principle floor.", "(QM-cluster prose)"),
            ("Critical fluctuation", "Long-wavelength modes near a continuous critical point; scale-invariant; characterized by critical exponents.", "(stat-mech criticality)"),
        ],
        "why": "Thermal and quantum fluctuations have different temperature dependence and different mathematical origins. Claims about 'fluctuations' near a critical point should distinguish the regime (classical-thermal vs quantum-critical).",
    },
    {
        "id": "gloss_participation_ratio",
        "title": "Participation ratio (disambiguation)",
        "domain": "physics · information_theory.shannon",
        "senses": [
            ("Random-matrix / Anderson-localization PR", "(Σ|ψ_i|²)² / Σ|ψ_i|⁴ on an eigenvector ψ; counts effective number of sites the eigenvector spans. Bell-Dean 1970.", "(Anderson localization literature)"),
            ("PR of FIM eigenvalue spectrum (CCA usage)", "(Σλ)² / Σλ² on the FIM eigenvalue spectrum; the project's d_eff. Renamed PR_FIM going forward. NO canonical primary-source citation found in physics literature for this specific application — folklore transfer from neural-population covariance contexts.", "X-series, CCA experiments"),
        ],
        "why": "The participation ratio formula has well-established usage in random matrix theory and neural-population covariance analysis. Its application to the FIM eigenvalue spectrum specifically — the way the CCA framework uses it — does NOT have a verified canonical citation per the deep-research pass 2026-05-04. The terminology is folklore-transferred; the rename to PR_FIM acknowledges this.",
    },
]


# ============================================================================
# DEFINED-TERM SENSE ENTRIES
# Only senses NOT already covered by an existing wiki entry.
# Each: {id, title, domain, sections{...}, anchors[...], disambiguates_from[...]}
# ============================================================================
SENSES: list[dict] = [
    # ----- Fisher information -----
    {
        "id": "gloss_fisher_information_classical",
        "title": "Fisher information (classical, on a probability-distribution parameter manifold)",
        "domain": "information_theory.shannon",
        "definition":
            "The matrix of expectations of pairwise log-likelihood derivatives "
            "for a parametric family of probability distributions. Equivalently, "
            "the second-derivative coefficient of the KL divergence between "
            "p(·|θ_0) and p(·|θ_0+Δθ).",
        "math":
            "g_ij(θ) = E_p(·|θ)[∂_i log p · ∂_j log p] = -E[∂_i ∂_j log p]",
        "regime":
            "Classical statistics; parametric families of probability "
            "distributions on a parameter manifold of any finite dimension.",
        "distinguished_from":
            "- [[g:fisher_information_quantum_bures|Quantum Fisher / Bures metric]]: "
            "operates on density matrices, not probability distributions; "
            "Petz family of quantum monotone metrics is non-unique. "
            "Coincides with classical Fisher only in the commutative limit.\n"
            "- Mattingly d_eff (PNAS 2018): different formula entirely "
            "(boundary-prior weight, not Hessian-of-KL).",
        "anchors": [
            ("doi", "10.1017/S0305004100009580", "Rao 1945 - Information and accuracy attainable in the estimation of statistical parameters", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-0821843024", "Amari & Nagaoka, Methods of Information Geometry (AMS Translations 2000)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
            ("arxiv", "1306.1465", "Ay, Jost, Lê, Schwachhöfer 2015 - The uniqueness of the Fisher metric as information metric", 3, "preprint-evolving", "canonical_authority", "axiomatic_foundation", "high"),
            ("wikipedia", "https://en.wikipedia.org/wiki/Fisher_information_metric", "Wikipedia: Fisher information metric", 2, "active-literature", "canonical_authority", "living_reference", "medium"),
        ],
        "disambiguates_from": ["gloss_fisher_information_quantum_bures"],
    },
    {
        "id": "gloss_fisher_information_quantum_bures",
        "title": "Fisher information (quantum / Bures metric on density matrices)",
        "domain": "information_theory.shannon · physics.modern.quantum_mechanics",
        "definition":
            "The smallest member of the Petz 1996 family of quantum monotone "
            "metrics on density matrices. Used in quantum Cramér-Rao bounds "
            "and quantum metrology. Coincides with the symmetric logarithmic "
            "derivative (SLD) construction (Helstrom 1969).",
        "math":
            "⟨A,B⟩^Bures_ρ = Tr[A · m_f(L_ρ,R_ρ)^{-1}(B)]  with f(x) = (1+x)/2",
        "regime":
            "Quantum estimation theory; quantum metrology; finite-dimensional "
            "or trace-class density matrices on a Hilbert space.",
        "distinguished_from":
            "- [[g:fisher_information_classical|Classical Fisher information]]: "
            "operates on probability distributions, not density matrices. "
            "Coincides with Bures only in the commutative limit.\n"
            "- BKM (Bogoliubov-Kubo-Mori) metric: f(x)=(x-1)/log(x), unique "
            "self-dual member of the Petz family.\n"
            "- RLD (right log derivative) metric: largest Petz-family member.\n"
            "- Wigner-Yanase skew information.",
        "anchors": [
            ("doi", "10.1016/0024-3795(94)00211-8", "Petz 1996 - Monotone metrics on matrix spaces", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-1107026254", "Bengtsson & Życzkowski, Geometry of Quantum States (Cambridge 2nd ed. 2017)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_fisher_information_classical"],
    },
    # ----- Effective dimension -----
    {
        "id": "gloss_effective_dimension_mattingly",
        "title": "Effective dimension (Mattingly 2018: weighted manifold-boundary)",
        "domain": "information_theory.shannon · statistics_probability.bayesian",
        "definition":
            "Σ_r r·Ω_r where Ω_r is the total weight of the optimal "
            "maximally-informative discrete prior p*(θ) on parameter-manifold "
            "edges of dimension r. Tracks how prior mass migrates from "
            "low-dimensional manifold boundaries (small d_eff) into the "
            "manifold interior (d_eff → D) as data quality improves.",
        "math":
            "d_eff = Σ_{r=1}^{D} r · Ω_r,  with Ω_r the optimal-prior weight on dim-r edges",
        "regime":
            "Bayesian model selection under finite measurement noise σ. Sethna "
            "sloppy-models lineage. Discrete by construction.",
        "distinguished_from":
            "- [[g:effective_dimension_pr_fim|FIM participation ratio]]: "
            "different formula, (Σλ)²/Σλ². Same name, same Sethna-adjacent "
            "vocabulary, but operationally different.\n"
            "- Sethna sloppy-models 'effective dimensionality' as used in Quinn "
            "2023: hyperribbon widths + this Mattingly d_eff; explicitly NOT "
            "the participation ratio.",
        "anchors": [
            ("doi", "10.1073/pnas.1715306115", "Mattingly, Transtrum, Abbott, Machta 2018 - Maximizing the information learned from finite data", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("arxiv", "1705.01166", "Mattingly et al. 2018 (arXiv preprint)", 3, "preprint-evolving", "cites", None, "high"),
        ],
        "disambiguates_from": ["gloss_effective_dimension_pr_fim"],
    },
    {
        "id": "gloss_effective_dimension_pr_fim",
        "title": "Effective dimension PR_FIM (participation ratio of FIM eigenvalue spectrum)",
        "domain": "information_theory.shannon · physics.modern.statistical_mechanics",
        "definition":
            "Participation ratio applied to the eigenvalue spectrum of a Fisher "
            "information matrix. Counts the effective number of eigenvalues "
            "carrying meaningful weight when the spectrum is heavy-tailed. "
            "The Constrained Critical Attractor framework's d_eff. Renamed "
            "PR_FIM going forward to disambiguate from Mattingly d_eff.",
        "math":
            "PR_FIM = (Σ_i λ_i)² / Σ_i λ_i²,  bounded 1 ≤ PR_FIM ≤ rank(FIM)",
        "regime":
            "Project-internal; used in CCA experiments (Phase A-D 2026-04-07; "
            "Phase E 2026-04-20). NO canonical primary-source citation found "
            "for this specific scalar applied to FIM in the physics literature "
            "— folklore transfer from random-matrix / neural-population "
            "covariance contexts (Gao-Trautmann-Ganguli 2017).",
        "distinguished_from":
            "- [[g:effective_dimension_mattingly|Mattingly d_eff]]: different "
            "formula (boundary-prior weight, not participation ratio).\n"
            "- General participation ratio in random matrix theory / Anderson "
            "localization (Bell-Dean 1970): same scalar applied to "
            "eigenvectors, not to FIM eigenvalue spectra.\n"
            "- Sethna group itself does NOT collapse the spectrum to PR; "
            "Quinn 2023 uses hyperribbon widths.",
        "anchors": [
            ("arxiv", "1806.01316", "Karakida, Akaho, Amari 2019 - Universal Statistics of Fisher Information in Deep Neural Networks", 3, "preprint-evolving", "adjacent_concept", None, "medium"),
        ],
        "disambiguates_from": ["gloss_effective_dimension_mattingly", "gloss_effective_dimension_hausdorff", "gloss_effective_dimension_spectral_network"],
    },
    {
        "id": "gloss_effective_dimension_hausdorff",
        "title": "Hausdorff / fractal dimension",
        "domain": "mathematics.geometry_topology",
        "definition":
            "Geometric measure of point sets. Defined via Hausdorff outer "
            "measure or equivalently (for fractals satisfying the open-set "
            "condition) via box-counting.",
        "math":
            "dim_H(S) = inf{ s ≥ 0 : H^s(S) = 0 };  dim_box(S) = lim ln N(ε)/ln(1/ε)",
        "regime":
            "Geometric measure theory; fractal sets, attractors of dynamical "
            "systems. dim_H ≤ dim_box always; equal for most natural fractals.",
        "distinguished_from":
            "- [[g:effective_dimension_pr_fim|PR_FIM]]: a real number ≥1 from "
            "an eigenvalue spectrum; not a geometric set invariant.\n"
            "- [[g:effective_dimension_spectral_network|Spectral / network "
            "dimension]]: governs random-walk return probability, not box-"
            "covering. d_s ≤ dim_H always.",
        "anchors": [
            ("isbn", "978-0716711865", "Mandelbrot - The Fractal Geometry of Nature (W.H. Freeman 1982)", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-0470848623", "Falconer - Fractal Geometry: Mathematical Foundations and Applications (Wiley 3rd ed.)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
            ("wikipedia", "https://en.wikipedia.org/wiki/Hausdorff_dimension", "Wikipedia: Hausdorff dimension", 2, "active-literature", "canonical_authority", "living_reference", "medium"),
        ],
        "disambiguates_from": ["gloss_effective_dimension_pr_fim", "gloss_effective_dimension_spectral_network"],
    },
    {
        "id": "gloss_effective_dimension_spectral_network",
        "title": "Spectral / network dimension (random-walk return probability)",
        "domain": "physics.modern.statistical_mechanics · networks_systems.graph_theory",
        "definition":
            "Defined via the long-time scaling of the random-walk return "
            "probability on a graph or fractal lattice. Governs heat-kernel "
            "asymptotics and vibrational density of states ('fractons').",
        "math":
            "d_s = -2 d log P_return(t) / d log t,  P_return(t) ~ t^{-d_s/2}",
        "regime":
            "Graphs, fractals, lattices. For Z^d: d_s = d. For Sierpinski "
            "gasket: d_s = 2 log(d+1)/log(d+3). d_s ≤ dim_H always.",
        "distinguished_from":
            "- [[g:effective_dimension_hausdorff|Hausdorff dimension]]: a "
            "geometric set invariant; can differ from d_s (e.g. Sierpinski "
            "gasket).\n"
            "- [[g:effective_dimension_pr_fim|PR_FIM]]: a Fisher-spectrum "
            "scalar, no direct relation.",
        "anchors": [
            ("doi", "10.1051/jphyslet:019820043017062500", "Alexander, Orbach 1982 - Density of states on fractals: 'fractons'", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("doi", "10.1051/jphyslet:0198300440101300", "Rammal, Toulouse 1983 - Random walks on fractal structures and percolation clusters", 1, "canonical", "canonical_authority", "progenitor", "high"),
        ],
        "disambiguates_from": ["gloss_effective_dimension_hausdorff", "gloss_effective_dimension_pr_fim"],
    },
    # ----- Relative entropy (modular Hamiltonian sense) -----
    {
        "id": "gloss_relative_entropy_classical_kl",
        "title": "Relative entropy (classical Kullback-Leibler divergence)",
        "domain": "information_theory.shannon",
        "definition":
            "Asymmetric measure of distinguishability between two probability "
            "distributions. Hessian gives the classical Fisher information.",
        "math":
            "D_KL(p ‖ q) = Σ_x p(x) log[p(x) / q(x)]   (or ∫ over continuous case)",
        "regime":
            "Classical probability theory and statistics; information-theoretic "
            "data processing.",
        "distinguished_from":
            "- Quantum von Neumann / Umegaki relative entropy: S(ρ‖σ) = Tr[ρ ln ρ - ρ ln σ]; "
            "operates on density matrices, see IT04.\n"
            "- [[g:relative_entropy_modular_hamiltonian|Modular Hamiltonian "
            "first-law usage]]: Jacobson 2016 entanglement-equilibrium framing.",
        "anchors": [
            ("doi", "10.1214/aoms/1177729694", "Kullback, Leibler 1951 - On information and sufficiency", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-0471241959", "Cover & Thomas, Elements of Information Theory (Wiley 2nd ed.)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_relative_entropy_modular_hamiltonian"],
    },
    {
        "id": "gloss_relative_entropy_modular_hamiltonian",
        "title": "Relative entropy (modular-Hamiltonian first-law usage, Jacobson 2016)",
        "domain": "physics.modern.quantum_field_theory · physics.modern.general_relativity",
        "definition":
            "Operational quantity in the entanglement-equilibrium derivation of "
            "Einstein equations: δS_EE = δ⟨H_mod⟩ / T, where S_EE is entanglement "
            "entropy of a small geodesic ball and H_mod is its modular Hamiltonian. "
            "The 'relative entropy' here is between the perturbed quantum state and "
            "the vacuum, treated as a measure of departure from entanglement equilibrium.",
        "math":
            "δS_EE = δ⟨H_mod⟩ / T  →  G_μν = 8πG T_μν  (linearized; under modular-H-as-boost)",
        "regime":
            "Linearized gravity around maximally-symmetric vacua; CFTs with "
            "small geodesic balls. REQUIRES modular Hamiltonian to reduce to "
            "boost generator — fails for relevant operators with low conformal "
            "dimensions per Casini-Galante-Myers 2016 (JHEP 03 (2016) 194).",
        "distinguished_from":
            "- [[g:relative_entropy_classical_kl|Classical KL divergence]]: not "
            "the same mathematical object; the Jacobson 2016 quantity is a "
            "quantum-information first-law statement on a subalgebra.\n"
            "- Quantum Umegaki relative entropy on density matrices (IT04): "
            "related but operates differently in this context.",
        "anchors": [
            ("doi", "10.1103/PhysRevLett.116.201101", "Jacobson 2016 - Entanglement equilibrium and the Einstein equation", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("arxiv", "1505.04753", "Jacobson 2016 (arXiv preprint)", 3, "preprint-evolving", "cites", None, "high"),
            ("doi", "10.1007/JHEP03(2016)194", "Casini, Galante, Myers 2016 - Comments on Jacobson's entanglement-equilibrium derivation", 1, "canonical", "contradicts", None, "high"),
        ],
        "disambiguates_from": ["gloss_relative_entropy_classical_kl"],
    },
    # ----- Anomalous dimension -----
    {
        "id": "gloss_anomalous_dimension_critical",
        "title": "Anomalous dimension η_critical (standard stat-mech)",
        "domain": "physics.modern.statistical_mechanics",
        "definition":
            "Critical exponent of the two-point correlation function at a "
            "continuous critical point. Universal across universality classes; "
            "for 2D Ising η = 1/4 exactly.",
        "math":
            "C(r) ~ r^{-(d - 2 + η)}  at criticality",
        "regime":
            "Continuous (second-order) phase transitions; renormalization-group "
            "fixed points. Defined for the universality classes; universal "
            "values per class.",
        "distinguished_from":
            "- [[g:anomalous_dimension_cca_isotropy_iota|CCA ι (isotropy "
            "indicator on FIM eigenvalue spectrum)]]: project-internal "
            "observable. Mathematically related at criticality (Vinayak 2014: "
            "the Zipf exponent of correlation-matrix eigenvalues is fixed by "
            "η_critical), but they are different scalars.",
        "anchors": [
            ("isbn", "978-0521499590", "Cardy, Scaling and Renormalization in Statistical Physics (Cambridge 1996)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
            ("isbn", "978-0201554090", "Goldenfeld, Lectures on Phase Transitions and the Renormalization Group (Westview 1992)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_anomalous_dimension_cca_isotropy_iota"],
    },
    {
        "id": "gloss_anomalous_dimension_cca_isotropy_iota",
        "title": "CCA isotropy indicator ι (Zipf-tail slope of FIM spectrum)",
        "domain": "information_theory.shannon · physics.modern.statistical_mechanics",
        "definition":
            "Project-internal observable on the Fisher information matrix "
            "eigenvalue spectrum. Defined as the negative log-log slope of the "
            "eigenvalue tail. Originally called 'η' in CCA prose, renamed ι "
            "(iota) per CCA_TERMINOLOGY_RENAME_PROPOSAL.md to disambiguate "
            "from η_critical.",
        "math":
            "ι = -slope( log λ_j  vs  log j )  on j ∈ [j_min, N/2]   (Zipf-tail fit)",
        "regime":
            "Project-internal (Constrained Critical Attractor framework). "
            "Used in Phase E 2026-04-20 q=2,5,7,10 sweep on 2D Potts.",
        "distinguished_from":
            "- [[g:anomalous_dimension_critical|Standard η_critical]]: the "
            "anomalous-dimension critical exponent in textbook stat-mech. ι "
            "is mathematically related to η_critical at continuous T_c "
            "(Vinayak-Prosen-Buča-Seligman 2014 EPL) but is a different "
            "observable. At first-order transitions they decouple.",
        "anchors": [
            ("arxiv", "1403.7218", "Vinayak, Prosen, Buča, Seligman 2014 - Spectral analysis of finite-time correlation matrices near equilibrium phase transitions", 3, "preprint-evolving", "canonical_authority", "progenitor", "high"),
        ],
        "disambiguates_from": ["gloss_anomalous_dimension_critical"],
    },
    # ----- Information geometry: missing senses -----
    {
        "id": "gloss_information_geometry_amari_dual_connections",
        "title": "Amari dual ±1 (e/m) connections on a statistical manifold",
        "domain": "mathematics.geometry_topology.differential_geometry · information_theory.shannon",
        "definition":
            "Pair of torsion-free affine connections on a statistical manifold, "
            "mutually dual w.r.t. the Fisher metric. The +1 (exponential / e) "
            "connection is flat in natural parameters; the -1 (mixture / m) "
            "connection is flat in expectation parameters. KL divergence is the "
            "canonical divergence of this dually-flat structure.",
        "math":
            "∇^(α) = (1+α)/2 · ∇^(e) + (1-α)/2 · ∇^(m),  α ∈ [-1, 1]",
        "regime":
            "Classical statistical manifolds with a chosen exponential family. "
            "Underlies Amari's α-divergence family. Quantum analog: BKM is the "
            "unique Petz-family member with dually-flat ±1 quantum connections.",
        "distinguished_from":
            "- Levi-Civita connection: torsion-free + metric-compatible; the "
            "Amari ±1 are NOT Levi-Civita (only the 0-connection ∇^(0) is, and "
            "that's the self-dual midpoint).",
        "anchors": [
            ("isbn", "978-0387960562", "Amari 1985 - Differential-Geometrical Methods in Statistics (Springer LN Stat 28)", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-0821843024", "Amari & Nagaoka, Methods of Information Geometry (AMS 2000)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_information_geometry_petz_quantum_family"],
    },
    {
        "id": "gloss_information_geometry_petz_quantum_family",
        "title": "Petz family of quantum monotone Riemannian metrics",
        "domain": "information_theory.shannon · physics.modern.quantum_mechanics",
        "definition":
            "Petz 1996 classification: every monotone Riemannian metric on the "
            "manifold of full-rank density matrices has the form ⟨A,B⟩^f_ρ = "
            "Tr[A · m_f(L_ρ,R_ρ)^{-1}(B)] for some symmetric, normalized, "
            "operator-monotone function f with f(1)=1, f(t)=t·f(1/t). "
            "Distinguished members: Bures/SLD (smallest), Bogoliubov-Kubo-Mori "
            "BKM (unique self-dual), RLD (largest), Wigner-Yanase (skew "
            "information). Quantum analog of Chentsov uniqueness — a "
            "classification, not a uniqueness theorem.",
        "math":
            "⟨A,B⟩^f_ρ = Tr[A · m_f(L_ρ,R_ρ)^{-1}(B)],   m_f(x,y) = y·f(x/y)",
        "regime":
            "Quantum estimation theory; quantum metrology; quantum information "
            "geometry. CPTP (completely-positive trace-preserving) maps form the "
            "natural contraction class.",
        "distinguished_from":
            "- Classical Fisher-Rao under Chentsov: SINGLE canonical metric on "
            "classical statistical manifolds. The Petz family contains "
            "infinitely many distinct quantum metrics that all reduce to "
            "classical Fisher-Rao in the commutative limit.",
        "anchors": [
            ("doi", "10.1016/0024-3795(94)00211-8", "Petz 1996 - Monotone metrics on matrix spaces", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-1107026254", "Bengtsson & Życzkowski, Geometry of Quantum States (Cambridge 2nd ed.)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_information_geometry_amari_dual_connections"],
    },
    # ----- Observer senses -----
    {
        "id": "gloss_observer_algebraic_clpw",
        "title": "Algebraic observer (type-II crossed-product construction, CLPW)",
        "domain": "physics.modern.quantum_gravity",
        "definition":
            "Observer's clock Hamiltonian as the auxiliary variable converting a "
            "type-III von Neumann factor (no trace, no density matrix) to a "
            "type-II algebra (admits a trace, finite generalized entropy) via "
            "crossed product with the modular automorphism group. Witten "
            "2112.12828; Chandrasekaran-Longo-Penington-Witten 2206.10780 (dS).",
        "math":
            "A_obs = A_QFT  ⋊_α  R   (crossed product with modular flow);  type III → type II",
        "regime":
            "Semiclassical gravity at 1/N; subregion algebras (Rindler wedge, "
            "static patch of de Sitter, etc.). Maldacena 2412.14014 'Real "
            "Observers Solve Imaginary Problems' uses this machinery.",
        "distinguished_from":
            "- [[g:observer_thermodynamic|Thermodynamic / Gibbons-Hawking observer]]: "
            "static observer experiencing horizon temperature; classical-thermo "
            "framing without the algebraic crossed-product machinery.\n"
            "- [[g:observer_qm_measurement|QM measurement observer]]: external "
            "system performing projective / POVM measurement; foundations of QM.\n"
            "- [[g:observer_classical_gr|Classical GR coordinate observer]]: "
            "worldline carrying frame; no mass/energy budget required.",
        "anchors": [
            ("arxiv", "2112.12828", "Witten 2022 - Gravity and the Crossed Product (JHEP 10 (2022) 008)", 3, "preprint-evolving", "canonical_authority", "progenitor", "high"),
            ("arxiv", "2206.10780", "Chandrasekaran, Longo, Penington, Witten 2022 - An Algebra of Observables for de Sitter Space", 3, "preprint-evolving", "canonical_authority", "progenitor", "high"),
            ("arxiv", "2209.10454", "Chandrasekaran, Penington, Witten 2022 - Large N algebras and generalized entropy", 3, "preprint-evolving", "canonical_authority", "comprehensive_survey", "high"),
            ("arxiv", "2412.14014", "Maldacena 2024 - Real Observers Solving Imaginary Problems", 3, "preprint-evolving", "cites", None, "high"),
        ],
        "disambiguates_from": ["gloss_observer_thermodynamic", "gloss_observer_qm_measurement", "gloss_observer_classical_gr"],
    },
    {
        "id": "gloss_observer_thermodynamic",
        "title": "Thermodynamic / Gibbons-Hawking observer",
        "domain": "physics.modern.general_relativity · physics.modern.statistical_mechanics",
        "definition":
            "Static (or stationary) observer in a stationary spacetime experiencing "
            "a temperature associated with a horizon. Gibbons-Hawking de Sitter "
            "temperature; Unruh effect for accelerated observers; Hawking "
            "temperature for BH static observers far from the horizon.",
        "math":
            "T = ℏ a / (2π c k_B)   (Unruh, with a = local acceleration)",
        "regime":
            "Stationary spacetimes with a horizon; semiclassical QFT in curved "
            "spacetime. Pre-dates the algebraic-observer machinery; classical "
            "thermodynamic framing.",
        "distinguished_from":
            "- [[g:observer_algebraic_clpw|Algebraic observer]]: precise "
            "quantum-information-theoretic construction; type-II algebra via "
            "crossed product. The thermodynamic observer is the heuristic "
            "predecessor.\n"
            "- [[g:observer_classical_gr|Classical GR coordinate observer]]: "
            "no thermal budget; pure coordinate frame.",
        "anchors": [
            ("doi", "10.1103/PhysRevD.15.2738", "Gibbons, Hawking 1977 - Cosmological event horizons, thermodynamics, and particle creation", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("doi", "10.1103/PhysRevD.14.870", "Unruh 1976 - Notes on black-hole evaporation", 1, "canonical", "canonical_authority", "progenitor", "high"),
        ],
        "disambiguates_from": ["gloss_observer_algebraic_clpw", "gloss_observer_classical_gr"],
    },
    {
        "id": "gloss_observer_qm_measurement",
        "title": "QM measurement observer (foundations sense)",
        "domain": "physics.modern.quantum_mechanics",
        "definition":
            "External system performing a measurement on a quantum system: "
            "projective measurement (von Neumann), POVM (positive operator-"
            "valued measure), or general quantum instrument. Foundations-of-QM "
            "sense; usually treated as classical for purposes of the Born rule.",
        "math":
            "POVM: {E_k},  E_k ≥ 0,  Σ_k E_k = I;  P(k|ρ) = Tr(E_k ρ)",
        "regime":
            "Quantum mechanics in flat space; no gravity; observer is external "
            "to the system being measured. Different role from the algebraic-"
            "observer construction in gravity, where the observer must carry "
            "energy and gravitate.",
        "distinguished_from":
            "- [[g:observer_algebraic_clpw|Algebraic observer]]: in gravity, "
            "the observer cannot be 'external' — it must be physical and "
            "carry energy; the algebraic crossed-product makes this precise.",
        "anchors": [
            ("isbn", "978-1107002173", "Nielsen & Chuang, Quantum Computation and Quantum Information (Cambridge 10th anniversary ed.)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_observer_algebraic_clpw"],
    },
    {
        "id": "gloss_observer_classical_gr",
        "title": "Classical GR coordinate observer",
        "domain": "physics.modern.general_relativity",
        "definition":
            "Worldline carrying a frame (tetrad / vierbein) along which "
            "physical quantities are measured. Used in classical GR for "
            "synchronizing clocks, exchanging signals, comparing rulers — no "
            "mass / energy budget required at the classical level.",
        "math":
            "u^μ = dx^μ/dτ  (4-velocity);  e_a^μ  (tetrad)",
        "regime":
            "Classical general relativity; semi-classical limit. Maldacena "
            "2024 emphasizes that this no-mass-no-energy framing fails in "
            "quantum gravity — observers must be physical systems.",
        "distinguished_from":
            "- [[g:observer_algebraic_clpw|Algebraic observer]]: in quantum "
            "gravity, the observer must carry energy and gravitate; the "
            "algebraic construction makes this precise.\n"
            "- [[g:observer_thermodynamic|Thermodynamic observer]]: same "
            "worldline equipped with horizon-temperature interpretation.",
        "anchors": [
            ("isbn", "978-0716703440", "Misner, Thorne, Wheeler - Gravitation (W.H. Freeman 1973)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_observer_algebraic_clpw", "gloss_observer_thermodynamic"],
    },
    # ----- Entropy: entanglement subsystem sense -----
    {
        "id": "gloss_entropy_entanglement",
        "title": "Entanglement entropy (von Neumann of reduced density matrix)",
        "domain": "information_theory.shannon · physics.modern.quantum_mechanics",
        "definition":
            "Von Neumann entropy of the reduced density matrix obtained by "
            "tracing out a subsystem. Quantifies entanglement between A and "
            "the rest of the system in a pure state |ψ⟩. Foundational in "
            "the gravity-from-entanglement program (Ryu-Takayanagi area "
            "formula, Van Raamsdonk's entanglement-builds-spacetime, "
            "island formula).",
        "math":
            "S(ρ_A) = -Tr(ρ_A log ρ_A),   ρ_A = Tr_B |ψ⟩⟨ψ|",
        "regime":
            "Quantum field theory and quantum many-body physics; subregion / "
            "subsystem entanglement. UV-divergent in continuum QFT (regulated "
            "by area-divided-by-cutoff leading term).",
        "distinguished_from":
            "- General von Neumann entropy S(ρ) = -Tr(ρ log ρ) on any density "
            "matrix (IT02): same formula, different operational role — "
            "entanglement entropy is specifically about a subsystem's reduced "
            "state.\n"
            "- Generalized entropy S_gen = A/(4G_N) + S_outside-matter: "
            "combines entanglement entropy with horizon-area entropy in BH "
            "thermodynamics.",
        "anchors": [
            ("doi", "10.1103/PhysRevLett.96.181602", "Ryu, Takayanagi 2006 - Holographic Derivation of Entanglement Entropy from AdS/CFT", 1, "canonical", "canonical_authority", "progenitor", "high"),
            ("isbn", "978-1107002173", "Nielsen & Chuang, Quantum Computation and Quantum Information (Cambridge 10th anniversary ed.)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": [],
    },
    # ----- Quantum corrections senses -----
    {
        "id": "gloss_quantum_corrections_perturbative",
        "title": "Perturbative quantum corrections",
        "domain": "physics.modern.quantum_field_theory",
        "definition":
            "Loop-expansion corrections in ℏ or 1/N (or coupling constant g) "
            "around a classical saddle point. Series typically asymptotic, "
            "small leading terms.",
        "math":
            "O = O_classical + ℏ·O_1-loop + ℏ²·O_2-loop + ...",
        "regime":
            "Weakly-coupled QFT; large-N theories. Borel-summable in some cases.",
        "distinguished_from":
            "- [[g:quantum_corrections_regime_changing|Regime-changing "
            "corrections]]: not a small expansion — qualitative change.\n"
            "- [[g:quantum_corrections_nonperturbative|Non-perturbative "
            "effects]]: invisible at any finite order.",
        "anchors": [
            ("isbn", "978-0201503975", "Peskin & Schroeder, An Introduction to Quantum Field Theory (Westview 1995)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_quantum_corrections_regime_changing", "gloss_quantum_corrections_nonperturbative"],
    },
    {
        "id": "gloss_quantum_corrections_regime_changing",
        "title": "Regime-changing quantum corrections",
        "domain": "physics.modern.quantum_field_theory · physics.modern.quantum_gravity",
        "definition":
            "Quantum effects that qualitatively change classical predictions "
            "in a particular regime. Maldacena example: extremal black holes, "
            "where one mode of the geometry (the throat length) becomes "
            "quantum mechanical near zero temperature while the rest stays "
            "classical — a 'controllable quantum corner' of an otherwise "
            "classical solution.",
        "math":
            "(no closed-form general expression; case-specific)",
        "regime":
            "Special points in parameter space (extremality, critical points, "
            "transition boundaries) where some classical mode acquires a "
            "quantum scale despite the rest of the system remaining classical.",
        "distinguished_from":
            "- [[g:quantum_corrections_perturbative|Perturbative corrections]]: "
            "small additive corrections, no qualitative change.\n"
            "- [[g:quantum_corrections_nonperturbative|Non-perturbative "
            "effects]]: invisible at any finite order; usually globally "
            "controlled (instanton, wormhole).",
        "anchors": [
            ("arxiv", "2104.12695", "Iliesiu, Turiaci 2021 - The statistical mechanics of near-extremal black holes (representative)", 3, "preprint-evolving", "canonical_authority", "progenitor", "medium"),
        ],
        "disambiguates_from": ["gloss_quantum_corrections_perturbative", "gloss_quantum_corrections_nonperturbative"],
    },
    {
        "id": "gloss_quantum_corrections_nonperturbative",
        "title": "Non-perturbative quantum effects (instantons, wormholes)",
        "domain": "physics.modern.quantum_field_theory · physics.modern.quantum_gravity",
        "definition":
            "Effects invisible at any finite order in perturbation theory. "
            "Examples: instanton contributions to vacuum decay, wormhole "
            "contributions to gravity path integrals (Coleman 1988, Giddings-"
            "Strominger 1988; modern revival in BH information paradox).",
        "math":
            "exp(-S_inst / ℏ)    (typically)",
        "regime":
            "Globally non-trivial saddle points in path integrals. Does not "
            "show up in any finite-order perturbative expansion.",
        "distinguished_from":
            "- [[g:quantum_corrections_perturbative|Perturbative corrections]]: "
            "appear order-by-order in ℏ; small.\n"
            "- [[g:quantum_corrections_regime_changing|Regime-changing corrections]]: "
            "qualitative change in a localized regime, but not necessarily "
            "globally non-trivial.",
        "anchors": [
            ("isbn", "978-0521282857", "Coleman, Aspects of Symmetry (Cambridge 1985, esp. Erice lectures on instantons)", 1, "canonical", "canonical_authority", "standard_textbook", "high"),
        ],
        "disambiguates_from": ["gloss_quantum_corrections_perturbative", "gloss_quantum_corrections_regime_changing"],
    },
]


def _disambig_to_sections(d: dict) -> dict:
    senses_lines = []
    for label, summary, where in d["senses"]:
        senses_lines.append(f"- **{label}** — {summary}  *(used in: {where})*")
    senses_block = "\n".join(senses_lines)
    return {
        "Disambiguation Notice":
            f"This page disambiguates the term **{d['title'].split(' (disambiguation)')[0]}** "
            f"as used in the wiki. Each sense is a different mathematical object. Use the "
            f"specific sense (via [[g:slug]] markup) in prose, not the bare phrase.",
        "Senses": senses_block,
        "Why this disambig exists": d["why"],
    }


def _sense_to_sections(s: dict) -> dict:
    return {
        "Definition": s["definition"],
        "Mathematical Form": s["math"],
        "Regime": s["regime"],
        "Distinguished From": s["distinguished_from"],
    }


def insert_entry(
    cur: sqlite3.Cursor,
    entry_id: str,
    title: str,
    entry_type: str,
    domain: str,
    sections: dict,
) -> bool:
    cur.execute("""
        INSERT OR IGNORE INTO entries (
            id, title, filename, entry_type, scale, domain, status,
            confidence, type_group, authoring_status, formality_tier
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entry_id, title, f"{entry_id}.md", entry_type, "—",
        domain, "glossary", "established", "GL", "complete", 2,
    ))
    if cur.rowcount == 0:
        return False
    for i, (sec_name, content) in enumerate(sections.items()):
        cur.execute("""
            INSERT OR IGNORE INTO sections
              (entry_id, section_name, section_order, content)
            VALUES (?, ?, ?, ?)
        """, (entry_id, sec_name, i, content))
    return True


def insert_anchor(
    cur: sqlite3.Cursor,
    entry_id: str,
    source: str,
    identifier: str,
    title: str,
    tier: int,
    stability: str,
    relationship: str,
    canonical_role: str | None,
    confidence: str,
) -> None:
    cur.execute("""
        INSERT OR IGNORE INTO external_anchors (
            entry_id, source, identifier, revision_id, title,
            tier, source_stability_class, relationship, canonical_role,
            verified_date, verified_by_session, confidence, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entry_id, source, identifier, None, title,
        tier, stability, relationship, canonical_role,
        TODAY, SESSION, confidence,
        f"Glossary seed 2026-05-04: anchor for defined-term entry {entry_id}.",
    ))


def insert_link(
    cur: sqlite3.Cursor,
    source_id: str,
    target_id: str,
    link_type: str,
    source_title: str = "",
    target_title: str = "",
    description: str = "",
) -> None:
    src_label = f"[{source_id}](entries/{source_id}.md)"
    tgt_label = f"[{target_id}](entries/{target_id}.md)"
    desc = description or (
        "Glossary disambiguates_from link: same name/symbol, different "
        "mathematical object. Inserted by glossary seed 2026-05-04."
    )
    cur.execute("""
        INSERT OR IGNORE INTO links
          (link_type, source_id, source_label, target_id, target_label,
           description, link_order, confidence_tier)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (link_type, source_id, src_label, target_id, tgt_label, desc, 0, "1"))


def main() -> None:
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")

    # Phase 1: ds_wiki.db inserts (entries, sections, links)
    src = sqlite3.connect(DS_WIKI_DB)
    sc = src.cursor()

    inserted_entries = 0
    skipped_entries = 0
    inserted_links = 0

    # Disambig pages
    for d in DISAMBIG:
        ok = insert_entry(
            sc, d["id"], d["title"], "disambiguation_page", d["domain"],
            _disambig_to_sections(d),
        )
        if ok:
            inserted_entries += 1
        else:
            skipped_entries += 1

    # Sense entries
    for s in SENSES:
        ok = insert_entry(
            sc, s["id"], s["title"], "defined_term", s["domain"],
            _sense_to_sections(s),
        )
        if ok:
            inserted_entries += 1
        else:
            skipped_entries += 1

    # Disambiguates-from links between senses
    for s in SENSES:
        for sibling in s.get("disambiguates_from", []):
            insert_link(sc, s["id"], sibling, "disambiguates from")
            inserted_links += 1

    src.commit()
    src.close()

    # Phase 2: wiki_history.db inserts (anchors)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    hcc = hc.cursor()
    inserted_anchors = 0
    for s in SENSES:
        for a in s.get("anchors", []):
            insert_anchor(hcc, s["id"], *a)
            if hcc.rowcount > 0:
                inserted_anchors += 1
    hc.commit()
    hc.close()

    # Phase 3: report
    print(f"Glossary seed migration {SESSION}")
    print(f"  Disambig pages defined:    {len(DISAMBIG)}")
    print(f"  Sense entries defined:     {len(SENSES)}")
    print(f"  Entries inserted:          {inserted_entries}")
    print(f"  Entries skipped (exists):  {skipped_entries}")
    print(f"  'disambiguates from' links inserted: {inserted_links}")
    print(f"  External anchors inserted: {inserted_anchors}")


if __name__ == "__main__":
    main()
