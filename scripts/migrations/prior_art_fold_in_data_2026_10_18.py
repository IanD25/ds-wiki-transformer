"""
Content for prior_art_fold_in_2026_10_18.py (audit_ref gsw-prior-art-fold-in-2026-10-18).

Every equation and quotation below was checked against the primary source on
2026-10-18; the access level per source is in each anchor's notes and in
docs/prior_art_reviews/PRIOR_ART_FOLD_IN_2026_10.md. Where only an abstract was
read, the entry text is limited to what the abstract states.
"""

AUD = "gsw-prior-art-fold-in-2026-10-18"


def facets(cc, tags, archetype, dsens):
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


def anchor(entry_id, source, identifier, title, relationship, notes, role=None, tier=1,
           stability="canonical", confidence="high"):
    ANCHORS.append(dict(entry_id=entry_id, source=source, identifier=identifier, title=title,
                        relationship=relationship, role=role, tier=tier, stability=stability,
                        confidence=confidence, notes=notes))


def tag(entry_id, path, primacy, rationale, confidence="high"):
    TAGS.append((entry_id, path, primacy, confidence, f"Prior-art fold-in ({AUD}): {rationale}"))


# ===========================================================================
# BIO16 — Frank 2009 (source 11)
# Read: full text, journal reprint (stevefrank.org) + arXiv:0901.3742; Eqs. 5, 14, 17 and quotes checked on the page.
# ===========================================================================
_t = ["Fisher's fundamental theorem", "Fisher information", "additive genetic variance", "natural selection",
      "Price equation", "reformulation not mechanism", "least-squares average effects", "information about the environment"]
ENTRIES.append(dict(
    id="BIO16", title="BIO16: Natural Selection and Fisher Information (Frank 2009)",
    filename="BIO16_frank_selection_fisher_information.md",
    scale="population", domain="biology · information", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Frank (2009, *J. Evol. Biol.* 22:231–244) shows that the variances in Fisher's fundamental theorem of natural "
         "selection are Fisher information. With p_y the frequency of type y and ṗ_y its rate of change, the total "
         "variance in fitness is P = Σ p_y (ṗ_y/p_y)² — the Fisher information in the population's frequency changes "
         "(Eq. 5). The part captured by the hereditary particles is G = Σ p_y g_y², the additive genetic variance (Eq. 14). "
         "The fundamental theorem, ṁ_f = ṁ_G = G (Eq. 17), then reads in his words: \"the rate of change in fitness caused "
         "by natural selection is equal to the Fisher information about the environment captured by the hereditary "
         "particles.\" He states the novelty precisely: \"The new result here is that these traditional measures of "
         "variance are measures of Fisher information.\"\n\n"
         "\"Maximizes\" in the title has a narrow meaning. The average effects of the hereditary particles are the "
         "least-squares regression of observed fitness on genotype, and so they maximize G for the value of P fixed by "
         "observation (p. 243). It is not a dynamical principle that drives selection.\n\n"
         "SCOPE: a re-expression of Fisher's theorem (BIO3), not a mechanism and not a new prediction. Frank says so: "
         "\"it remains unclear whether the link between Fisher information and the evolutionary dynamics of natural "
         "selection is just an interesting analogy or represents a deeper insight\" (p. 232). The wiki previously stated "
         "this reformulation, uncited, as an identity (BIO3; corrected 2026-10-18)."),
        ("Mathematical Form",
         "Total Fisher information in frequency change (Eq. 5):\n"
         "  P = Σ_y p_y (ṗ_y / p_y)² = Σ_y p_y a_y²      (P = total variance in fitness)\n\n"
         "Captured by hereditary particles (Eq. 14):\n"
         "  G = Σ_y p_y g_y² = g · g                    (G = additive genetic variance)\n"
         "  P = G + E                                    (E = information lost; environmental variance)\n\n"
         "Fundamental theorem (Eq. 17):\n"
         "  ṁ_f = ṁ_G = G\n\n"
         "Standard Fisher information for comparison (IT05): I(θ) = E[(∂ log p(y|θ)/∂θ)²]"),
        ("Constraint Category",
         "Informatic (In): the result identifies the variance terms of selection theory with Fisher information, so the "
         "Cramér–Rao reading of variance carries over. It adds no constraint on evolutionary dynamics beyond Fisher's "
         "theorem itself."),
        ("DS Cross-References",
         "BIO3 (Natural Selection — Fisher's Fundamental Theorem; BIO16 is a re-expression of that theorem, and BIO3's "
         "2026-10-18 correction cites this paper). IT05 (Fisher Information — the classical quantity used throughout; "
         "no quantum or geometric extension is involved). M6 (Fisher Information Rank — not the quantity in Frank's "
         "argument; any link is an analogy only)."),
        ("Mathematical Archetype",
         "Mathematical archetype: optimization-principle\n\n"
         "The optimization is a least-squares projection: choosing the average effects g as close as possible to the "
         "observed fitness fluctuations a maximizes the captured Fisher information G at fixed total P. The archetype "
         "label describes that projection, not a principle governing evolution."),
        ("What The Math Says",
         "Take a population whose type frequencies p sub y change at rates p-dot sub y. The quantity P, the sum over "
         "types of p sub y times the square of p-dot over p, is both the variance in fitness and the Fisher information "
         "that the frequency change carries about the environment. Fitting fitness to the hereditary particles by least "
         "squares splits P into a captured part G and a residual part E. G is the additive genetic variance. Fisher's "
         "fundamental theorem says the partial change in mean fitness due to selection equals G. So the theorem can be "
         "read as: selection changes fitness at a rate equal to the Fisher information captured by heredity. Nothing in "
         "this changes what the theorem predicts."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "optimization-principle", "D-invariant"),
))
anchor("BIO16", "doi", "10.1111/j.1420-9101.2008.01647.x",
       "Frank 2009 - Natural selection maximizes Fisher information (J. Evol. Biol. 22:231-244)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18: journal reprint (stevefrank.org/reprints-pdf/09JEBftns.pdf) and arXiv:0901.3742. "
       "Eqs. 5, 14, 17 and the quotes in BIO16 checked against the page images. Frank calls the link possibly 'just an interesting analogy'.",
       role="progenitor", stability="active-literature")
tag("BIO16", "biology.evolution", "primary", "selection theory (Fisher's fundamental theorem)")
tag("BIO16", "information_theory", "secondary", "Fisher information re-expression")
LINKS += [
    ("BIO16", "BIO3", "derives from", "1.5",
     "Frank 2009 re-expresses Fisher's fundamental theorem: the additive genetic variance G in dW/dt = Var_A(w) is the Fisher "
     "information captured by the hereditary particles (Eq. 17). A reformulation, not a mechanism; BIO3's 2026-10-18 correction rests on it."),
    ("BIO16", "IT05", "derives from", "2",
     "Uses the classical Fisher information of the type-frequency distribution; P = sum p_y (pdot_y/p_y)^2 (Eq. 5)."),
]

# ===========================================================================
# IT11 — Quantum Fisher information / quantum Cramér–Rao bound (source 12)
# Read: full text (scanned PRL, york.ac.uk copy); Eqs. 11-15, 28, 32-33, Bures relation, credits checked on page images.
# ===========================================================================
_t = ["quantum Fisher information", "quantum Cramér-Rao bound", "symmetric logarithmic derivative", "Bures metric",
      "statistical distance", "Fubini-Study metric", "quantum metrology", "Mandelstam-Tamm uncertainty", "Helstrom", "Holevo"]
ENTRIES.append(dict(
    id="IT11", title="IT11: Quantum Fisher Information and the Quantum Cramér–Rao Bound (Braunstein–Caves 1994)",
    filename="IT11_quantum_fisher_information.md",
    scale="quantum", domain="information · physics", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "To estimate a parameter X encoded in a density operator ρ̂(X), one performs some quantum measurement {Ê(ξ)}. "
         "Its outcome probabilities p(ξ|X) = tr(Ê(ξ)ρ̂(X)) have an ordinary Fisher information F(X), and after N "
         "repetitions the classical Cramér–Rao bound gives N⟨(δX)²⟩ ≥ 1/F(X) (Braunstein & Caves 1994, *PRL* 72:3439, "
         "Eqs. 11–13). Maximizing F over all quantum measurements gives a measurement-independent quantity — now called "
         "the quantum Fisher information — and the bound becomes the quantum Cramér–Rao bound.\n\n"
         "Braunstein & Caves define the maximum as a line element on density operators, ds²_DO = dX² max F(X) (Eq. 14). "
         "They show it equals tr(dρ̂ R⁻¹(dρ̂)), where R(Ô) = ½(ρ̂Ô + Ôρ̂) (Eqs. 15, 28); R⁻¹(ρ̂′) is what Helstrom and Holevo "
         "called the symmetric logarithmic derivative. They show the bound is achievable, that the metric reduces to "
         "the Fubini–Study metric on pure states, and that it is the Bures metric: [d_Bures]² = ¼ ds²_DO.\n\n"
         "PRIORITY: the quantum bound itself is older. Braunstein & Caves write \"Both Helstrom [10] and Holevo [6] have "
         "derived the bound\" (Helstrom 1976; Holevo 1982). Their contribution is separating the classical and quantum "
         "optimizations, proving achievability, and the statistical-distance geometry. The paper does not use the term "
         "\"quantum Fisher information\".\n\n"
         "UNCERTAINTY RELATIONS: combining the bounds gives N⟨(δX)²⟩ (ds²_DO/dX²) ≥ 1 (Eq. 32), which they call \"a "
         "Mandelstam-Tamm uncertainty principle\" for X and its generator ĥ, more stringent than the standard form for "
         "mixed states. This is the estimation route to parameter–generator (time–energy type) uncertainty relations. It "
         "does not derive the Heisenberg–Robertson ΔxΔp relation, which follows from the commutator (see IT05's "
         "2026-10-18 correction)."),
        ("Mathematical Form",
         "Classical Cramér–Rao, N measurements (Eq. 13):\n"
         "  N⟨(δX)²⟩_X ≥ 1/F(X) + N⟨δX⟩²_X ≥ 1/F(X)\n"
         "  F(X) = ∫dξ p(ξ|X) (∂ ln p(ξ|X)/∂X)²,   p(ξ|X) = tr(Ê(ξ)ρ̂(X))\n\n"
         "Quantum metric (Eqs. 14, 15, 28):\n"
         "  ds²_DO = dX² max_{Ê(ξ)} F(X) = tr(dρ̂ R⁻¹_ρ̂(dρ̂)),   R_ρ̂(Ô) = ½(ρ̂Ô + Ôρ̂)\n\n"
         "Bures relation (p. 3442):  [d_Bures(ρ̂, ρ̂+dρ̂)]² = ¼ ds²_DO\n"
         "Pure states:  ds²_DO = 4⟨dψ⊥|dψ⊥⟩ = ds²_PS  (Fubini–Study)\n\n"
         "Parameter uncertainty principle (Eq. 32):  N⟨(δX)²⟩_X (ds²_DO/dX²) ≥ 1\n"
         "  with ds²_DO/dX² ≤ Σ_j (dp_j/dX)²/p_j + 4⟨(Δĥ)²⟩_X  (Eq. 33)"),
        ("Constraint Category",
         "Informatic-Geometric (In-Gm): a lower bound on the precision of any estimate of a parameter encoded in a "
         "quantum state, expressed through a Riemannian metric (Bures) on density operators. It is the quantum "
         "counterpart of IT05's Cramér–Rao bound and sets the standard limits of quantum metrology."),
        ("DS Cross-References",
         "IT05 (Fisher Information — IT11's quantity is IT05's classical Fisher information maximized over all quantum "
         "measurements). IT08 (Fisher-Rao Metric — the Bures/SLD metric is a quantum counterpart; on commuting families it "
         "reduces to the classical metric). QM2 (Heisenberg Uncertainty Principle — Eq. 32 is a Mandelstam–Tamm-type "
         "parameter–generator relation, not a derivation of ΔxΔp ≥ ħ/2). P21 (Fisher-Rao Metric Universality — on the "
         "quantum side there is no unique monotone metric (Petz); the SLD/Bures metric is one member of the family)."),
        ("Mathematical Archetype",
         "Mathematical archetype: optimization-principle\n\n"
         "Two nested optimizations: over estimators, which gives the classical Cramér–Rao bound, then over quantum "
         "measurements, which gives the quantum Fisher information. The resulting maximum defines a distance between "
         "neighbouring quantum states by how well any measurement can tell them apart."),
        ("What The Math Says",
         "Any measurement turns a quantum state into a probability distribution over outcomes, and that distribution has "
         "a Fisher information about the parameter X. The best measurement gives the largest Fisher information, and that "
         "largest value defines the squared distance per unit X between neighbouring states. N repetitions can then "
         "estimate X with variance no smaller than one over N times that value. Written with the symmetrized product R, "
         "the distance is the trace of d-rho times R-inverse of d-rho. A quarter of it is the squared Bures distance, and "
         "on pure states it is the Fubini–Study metric. Bounding the distance by the variance of the generator h gives a "
         "Mandelstam–Tamm-type uncertainty relation between the parameter and h."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In-Gm", _t, "optimization-principle", "D-invariant"),
))
anchor("IT11", "doi", "10.1103/PhysRevLett.72.3439",
       "Braunstein & Caves 1994 - Statistical distance and the geometry of quantum states (PRL 72:3439-3443)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 (scanned PRL, www-users.york.ac.uk/~sb54/papers/bc94.pdf; no text layer — "
       "Eqs. 11-15, 28, 32-33, the Bures relation and the Helstrom/Holevo credit checked on page images). The bound is credited "
       "by the authors to Helstrom 1976 and Holevo 1982 (not anchored here; not read).",
       role="progenitor")
tag("IT11", "information_theory.quantum_info", "primary", "quantum estimation theory")
tag("IT11", "physics.modern.quantum_mechanics", "secondary", "density operators, uncertainty relations")
tag("IT11", "statistics_probability.inference", "secondary", "Cramér–Rao bound")
LINKS += [
    ("IT11", "IT05", "generalizes", "1.5",
     "Quantum Fisher information is IT05's classical Fisher information maximized over all quantum measurements "
     "(Braunstein-Caves 1994 Eq. 14); for a fixed measurement IT05 applies unchanged."),
    ("IT11", "QM2", "couples to", "2",
     "Braunstein-Caves Eq. 32 is an uncertainty principle for estimating a parameter X, which they identify as Mandelstam-Tamm "
     "type (X vs its generator h). It does not derive Heisenberg-Robertson Delta-x Delta-p, which follows from the commutator."),
    ("IT11", "IT08", "couples to", "2",
     "The quantum (SLD) metric ds^2_DO is four times the squared Bures distance and reduces to Fubini-Study on pure states; "
     "it is the quantum counterpart of the Fisher-Rao metric, one member of Petz's family of monotone metrics."),
]

# ===========================================================================
# URB1 — Bettencourt 2013 (source 5)
# Read: full text + SM (colorado.edu reprint); assumptions, Table 1, δ = H/[D(D+H)], 7/6 and the dissipation contrast checked.
# ===========================================================================
_t = ["urban scaling", "Bettencourt 2013", "settlement scaling theory", "superlinear socioeconomic scaling",
      "sublinear infrastructure", "network fractal dimension H", "delta = H/[D(D+H)]", "mixing population", "cities vs organisms"]
ENTRIES.append(dict(
    id="URB1", title="URB1: The Origins of Scaling in Cities (Bettencourt 2013)",
    filename="URB1_bettencourt_origins_of_urban_scaling.md",
    scale="population", domain="networks", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Bettencourt (2013, *Science* 340:1438–1441) derives the exponents of urban scaling (C2) from \"four simple "
         "assumptions\": (1) a mixing population — citizens can explore the city given their resources, with path geometry "
         "of fractal dimension H; (2) incremental network growth — infrastructure connects people as they join; (3) bounded "
         "human effort — the social-output parameter G is independent of city size N; (4) socioeconomic outputs proportional "
         "to local social interactions, Y = GN²/A_n.\n\n"
         "In D spatial dimensions the theory gives land area A ∝ N^α with α = D/(D+H), infrastructure network volume "
         "A_n ∝ N^{1−δ}, and socioeconomic rates Y ∝ N^{1+δ}, with δ = H/[D(D+H)]. For cities, D = 2 and H ≃ 1, so α ≃ 2/3, "
         "δ ≃ 1/6, and the predicted exponents are 7/6 (socioeconomic, and network power dissipation) and 5/6 (network "
         "volume). Network length scales with α, not 1 − δ. Fits in the paper: gross metropolitan product β = 1.126 ± 0.023 "
         "(363 US MSAs), road lane miles 0.849 ± 0.038 (415 urban areas).\n\n"
         "Author-stated limits: agglomeration effects vanish as H → 0; H ≤ 2 bounds δ ≤ 1/4; the theory concerns whole "
         "cities, not intra-urban profiles. The paper contrasts cities with organisms: transport dissipation scales "
         "superlinearly with population, so cities differ from systems \"thought to have evolved to minimize energy "
         "dissipation\" such as organisms (citing West, Brown & Enquist; BIO12).\n\n"
         "CONTESTED: whether the empirical exponents are robust. Arcaute et al. 2015 (J. R. Soc. Interface) find exponents "
         "fluctuate with city-boundary definitions; Leitão et al. 2016 (R. Soc. Open Sci.) find β ≠ 1 inferences depend on "
         "how fluctuations are modelled; Shalizi 2011 (arXiv:1102.4101) argues the data cannot separate power laws from "
         "other forms. (Critiques read at abstract level only.)\n\n"
         "WIKI RELEVANCE: C2's withdrawn \"β = 1 ± 1/D_eff\" and P11's \"urban scaling tracks network dimension\" restate "
         "this theory. Note that δ is H/[D(D+H)], not 1/D; P11's D/(D+1) form cannot reach any exponent above 1, so this "
         "paper falsifies P11 (closed 2026-10-18)."),
        ("Mathematical Form",
         "Assumption 4:  Y = G N² / A_n\n\n"
         "Predictions (Table 1; general D, H → cities D = 2, H = 1):\n"
         "  Land area           A   ∝ N^α,      α = D/(D+H)          → 2/3\n"
         "  Network volume      A_n ∝ N^{1−δ}                         → 5/6\n"
         "  Network length      L_n ∝ N^α                             → 2/3\n"
         "  Interactions/capita I_i ∝ N^δ,     δ = H/[D(D+H)]       → 1/6\n"
         "  Socioeconomic rates Y   ∝ N^{1+δ}                         → 7/6\n"
         "  Network dissipation W   ∝ N^{1+δ}                         → 7/6\n\n"
         "Limits:  H → 0 ⇒ δ → 0 (no agglomeration);  H ≤ 2 ⇒ δ ≤ 1/4"),
        ("Constraint Category",
         "Geometric (Ge): exponents are fixed by the spatial dimension D of the city and the fractal dimension H of "
         "movement paths, through the balance between interaction benefits and transport costs on a hierarchical network."),
        ("DS Cross-References",
         "C2 (Urban Scaling — the empirical regularity this theory explains; C2's withdrawn β = 1 ± 1/D_eff re-expressed it). "
         "P11 (Urban Scaling Tracks Network Spectral Dimension — restates the question this paper answers, with a D/(D+1) "
         "form that cannot give superlinear exponents). BIO12 (West–Brown–Enquist — the hierarchical-network sums are "
         "parallel, but Bettencourt stresses that cities do not minimize dissipation)."),
        ("Mathematical Archetype",
         "Mathematical archetype: power-law-scaling\n\n"
         "City-wide quantities scale as powers of population, with exponents that are rational functions of D and H. "
         "The theory predicts the exponents from a balance condition rather than fitting them."),
        ("What The Math Says",
         "People in a city of N inhabitants interact at a rate set by population density over the network area. Land "
         "area grows as N to the power D over D plus H, because people must be able to reach the whole city. The "
         "network grows incrementally, so its volume grows as N to the power one minus delta, where delta equals H over "
         "D times D plus H. Social output is G times N squared over the network area, so it grows as N to the power one "
         "plus delta. With D equal to two and H equal to one, delta is one sixth: socioeconomic outputs scale as seven "
         "sixths and infrastructure volume as five sixths. Energy lost in transport also scales as seven sixths, so "
         "cities do not minimize dissipation as organisms are thought to."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Ge", _t, "power-law-scaling", "D-sensitive"),
))
anchor("URB1", "doi", "10.1126/science.1235823", "Bettencourt 2013 - The origins of scaling in cities (Science 340:1438-1441)",
       "canonical_authority",
       "Primary source. Full text and Supplementary Materials read 2026-10-18 (colorado.edu reprint of the AAAS PDF). Four assumptions, "
       "Table 1, delta = H/[D(D+H)] ~ 1/6 and the organisms contrast checked first-hand. Critiques (Arcaute 2015, Leitao 2016, Shalizi 2011) "
       "read at abstract level only.", role="progenitor")
tag("URB1", "networks_systems.complex_systems", "primary", "urban systems as interaction networks")
tag("URB1", "networks_systems", "secondary", "infrastructure networks")
LINKS += [
    ("URB1", "C2", "predicts for", "1.5",
     "Bettencourt 2013 derives C2's exponents: socioeconomic beta = 1 + delta = 7/6, network volume 1 - delta = 5/6, land area 2/3, "
     "with delta = H/[D(D+H)] (D = 2, H = 1). C2's withdrawn 'beta = 1 +/- 1/D_eff' re-expressed this with a free parameter."),
    ("P11", "URB1", "tensions with", "1.5",
     "P11 asks whether urban exponents track infrastructure-network dimension; Bettencourt 2013 already answers it, with exponents "
     "set by spatial dimension D and path dimension H. P11's D/(D+1) form disagrees with that theory and cannot give exponents above 1. "
     "P11 closed as Falsified 2026-10-18 (gsw-prior-art-fold-in-2026-10-18)."),
    ("URB1", "BIO12", "analogous to", "2",
     "Both sum quantities over a hierarchical branching network (Bettencourt Eqs. 1-3; WBE Eqs. 4, 6). The physics differs: WBE "
     "minimizes dissipation, while Bettencourt finds urban dissipation scales superlinearly (1 + delta)."),
]

# ===========================================================================
# IT09 — Sloppy models / parameter-space compression (source 6)
# Read: Machta 2013 published full text (Yale copy) + arXiv SM; Transtrum 2015 arXiv v1; Quinn 2023 arXiv v2.
# ===========================================================================
_t = ["sloppy models", "parameter space compression", "Fisher information matrix eigenvalues", "stiff and sloppy directions",
      "hyperribbon", "model manifold", "relevant and irrelevant directions", "renormalization group", "coarse-graining",
      "reparameterization dependence"]
ENTRIES.append(dict(
    id="IT09", title="IT09: Sloppy Models and Parameter-Space Compression (Machta et al. 2013)",
    filename="IT09_sloppy_models_parameter_space_compression.md",
    scale="cross-scale", domain="information · physics", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Many multiparameter models are \"sloppy\": the eigenvalues of their Fisher information matrix (FIM) are spread "
         "roughly evenly on a log scale over many decades, so a few stiff parameter combinations control behaviour and the "
         "rest barely matter (Transtrum et al. 2015, *J. Chem. Phys.* 143:010901). Machta, Chachra, Transtrum & Sethna "
         "(2013, *Science* 342:604–607) trace this to coarse-graining. In a hopping (diffusion) model and in the 2D Ising "
         "model, the FIM at the microscopic scale is not sloppy: \"neither the diffusion model nor the Ising model are "
         "sloppy at their microscopic scales.\" When observables are coarsened — several time steps, or a decimated "
         "subset of sites — the eigenvalues of irrelevant directions shrink according to their renormalization-group "
         "exponents, while relevant directions keep their precision: \"relevant variables are exactly those for which "
         "spatial coarsening preserves measurement precision.\" The stiff directions are the parameters of the emergent "
         "theory (drift and diffusion; the Ising h and t).\n\n"
         "Scope of the Ising example: 13 global, translation-invariant couplings (12 neighbour couplings plus the field) "
         "on a 64 × 64 lattice at T_c only; no per-site fields, no temperature sweep, no first-order transitions.\n\n"
         "CAVEATS from the same group: FIM eigenvalues depend on parameterization — \"the FIM can be transformed into any "
         "positive definite matrix by a simple linear transformation of parameters\" (Transtrum 2015, arXiv v1). Quinn, "
         "Abbott, Transtrum, Machta & Sethna (2023, *Rep. Prog. Phys.* 86:035901) prove the hyperribbon bounds only for "
         "smooth nonlinear least-squares models; for probabilistic models such as Ising the hierarchy is observed, not "
         "proven. Sloppiness is not the same as non-identifiability (Chis et al. 2016, abstract).\n\n"
         "WIKI RELEVANCE: M6 (Fisher Information Rank) and P5 (FIM rank = D_eff) apply this programme to new model "
         "classes. For an exponential family the FIM is the covariance of the conjugate observables, so a model with "
         "per-site fields has the connected correlation matrix as its FIM."),
        ("Mathematical Form",
         "FIM (Machta 2013 Eq. 1):  g_μν = −Σ_x P_θ(x) ∂² log P_θ(x) / ∂θ^μ ∂θ^ν,   ds² = g_μν δθ^μ δθ^ν\n\n"
         "Exponential family (Ising):  g_μν = ∂_μ∂_ν log Z = ⟨Φ_μ Φ_ν⟩ − ⟨Φ_μ⟩⟨Φ_ν⟩\n\n"
         "Hopping model, n-th eigenvalue after time τ:  λ_n ∼ τ² (Dτ/a²)^{−n−1/2}\n\n"
         "Irrelevant directions under coarse-graining by b (Quinn 2023 Eq. 16):\n"
         "  d log(ds²)/db = −D + 2y_i      (y_i < 0, the RG exponent)\n"
         "Relevant directions: the metric does not contract.\n\n"
         "Sloppy spectrum: log λ_i roughly uniformly spaced over many decades."),
        ("Constraint Category",
         "Informatic-Geometric (In-Gm): the FIM eigen-structure sets which parameter combinations data can constrain. "
         "Coarse-graining compresses parameter space onto the few relevant directions, which is why effective theories "
         "with few parameters predict well."),
        ("DS Cross-References",
         "IT05 (Fisher Information — the FIM is the object studied). IT08 (Fisher-Rao Metric — ds² is the Fisher-Rao "
         "line element; the model manifold is its embedding). RG01 (Wilson's Renormalisation Group — irrelevant directions "
         "shrink at rates set by RG exponents). M6 (Fisher Information Rank — an application of this programme; Machta "
         "2013 is its canonical anchor). P5 (FIM rank = D_eff — Supported only as an application of this work). STAT5 "
         "(correlation-matrix spectra at criticality — the per-site-field FIM is a correlation matrix)."),
        ("Mathematical Archetype",
         "Mathematical archetype: dimensional-scaling\n\n"
         "Under coarse-graining by a factor b, each FIM eigenvalue scales as a power of b set by the dimension D and the "
         "RG exponent of its direction. Relevant directions survive, and irrelevant ones shrink geometrically."),
        ("What The Math Says",
         "The Fisher information matrix measures how distinguishable two nearby parameter settings are from data. For "
         "many models its eigenvalues fall off geometrically, so only a few combinations of parameters matter. For a "
         "hopping model or the Ising model observed at the finest scale this is not true: every parameter is visible. "
         "Observe only coarse features — after many time steps, or on a decimated lattice — and the eigenvalues of the "
         "irrelevant directions fall at rates fixed by their renormalization-group exponents, while the relevant ones "
         "stay. What remains is the few-parameter emergent theory. The eigenvalues themselves depend on how the "
         "parameters are chosen, so statistics built from them inherit that choice."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In-Gm", _t, "dimensional-scaling", "D-sensitive"),
))
anchor("IT09", "doi", "10.1126/science.1238723",
       "Machta, Chachra, Transtrum & Sethna 2013 - Parameter space compression underlies emergent theories and predictive models (Science 342:604-607)",
       "canonical_authority",
       "Primary source. Published full text read 2026-10-18 (machtagroup.yale.edu copy) plus arXiv:1303.6738 SM. Quotes checked first-hand. "
       "An erratum exists (Science 342:931) - not read. The arXiv and published texts differ; quote the published one.", role="progenitor")
anchor("IT09", "doi", "10.1063/1.4923066",
       "Transtrum, Machta, Brown, Daniels, Myers & Sethna 2015 - Perspective: Sloppiness and emergent theories in physics, biology, and beyond (J. Chem. Phys. 143:010901)",
       "cites",
       "Full text of arXiv:1501.07668 v1 read 2026-10-18 (journal wording not checked). DOI verified on Crossref 2026-10-18. NOTE: anchor id 100 "
       "(P5) carries 10.1063/1.4918623, which Crossref resolves to Beechem et al., Rev. Sci. Instrum. 86:041101 - a wrong DOI.")
anchor("IT09", "doi", "10.1088/1361-6633/aca6f8",
       "Quinn, Abbott, Transtrum, Machta & Sethna 2023 - Information geometry for multiparameter models: new perspectives on the origin of simplicity (Rep. Prog. Phys. 86:035901)",
       "canonical_authority",
       "Review. Full text of arXiv:2111.07176 v2 read 2026-10-18; published version not read. Hyperribbon bounds proven only for "
       "nonlinear least-squares models.", role="comprehensive_survey")
tag("IT09", "statistics_probability.inference", "primary", "parameter identifiability and model reduction")
tag("IT09", "information_theory", "secondary", "Fisher information geometry")
tag("IT09", "physics.modern.statistical_mechanics", "secondary", "renormalization group, Ising model")
LINKS += [
    ("P5", "IT09", "derives from", "1.5",
     "P5's 'Fisher information rank = effective dimensionality' is an application of the sloppy-models programme (Machta et al. 2013); "
     "Supported only as such. Caveat from the same group: FIM eigenvalues are not invariant under reparameterization (Transtrum 2015)."),
    ("M6", "IT09", "derives from", "1.5",
     "Fisher Information Rank as a parameter-space diagnostic is the Machta et al. 2013 construction (M6's canonical anchor). Any "
     "eigenvalue statistic, including a participation ratio, depends on the parameterization chosen."),
    ("IT09", "IT05", "derives from", "1.5",
     "The object studied is the Fisher information matrix g_mu,nu = -E[d^2 log P / d theta d theta] (Machta 2013 Eq. 1)."),
    ("IT09", "RG01", "couples to", "2",
     "Under coarse-graining, FIM eigenvalues of irrelevant directions shrink at rates set by their RG exponents "
     "(d log ds^2/db = -D + 2y_i, Quinn 2023 Eq. 16); relevant directions keep their precision."),
]

# ===========================================================================
# STAT4 — Gefen, Mandelbrot & Aharony 1980 (source 7)
# Read: full text (4-page scan, Wayback copy of Mandelbrot's Yale archive); abstract, R_min rule, gasket and Koch results checked on the page.
# ===========================================================================
_t = ["critical phenomena on fractals", "fractal lattices", "order of ramification", "connectivity", "lacunarity",
      "Sierpinski gasket", "Sierpinski carpet", "Koch curves", "lower critical dimension", "Ising model", "renormalization group"]
ENTRIES.append(dict(
    id="STAT4", title="STAT4: Critical Phenomena on Fractal Lattices (Gefen–Mandelbrot–Aharony 1980)",
    filename="STAT4_critical_phenomena_fractal_lattices.md",
    scale="cross-scale", domain="physics · mathematics", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "Gefen, Mandelbrot & Aharony (1980, *PRL* 45:855–858) applied renormalization-group methods to Ising spins on "
         "self-similar fractal lattices. Abstract: the critical properties \"vary with the (noninteger) fractal "
         "dimensionality D, but also with several topological factors: ramification, connectivity, lacunarity, etc. For "
         "any D ≥ 1, there exist systems with both T_c = 0, and T_c > 0; hence a lower critical dimensionality is not "
         "defined.\"\n\n"
         "Main results. (1) \"Ising systems with given D have T_c = 0 if the minimum order of ramification, R_min, is "
         "finite, and T_c > 0 if R_min is infinite\" — stated as a general rule from exactly solved examples. (2) The "
         "Sierpiński gasket (D = ln3/ln2 ≈ 1.585, finitely ramified) has an exact recursion with no finite-temperature "
         "fixed point: T_c = 0, ν = ∞, and the correlation length grows as an exponential of an exponential of the coupling. "
         "(3) Same D, different exponents: a nonbranching Koch curve with D = ln3/ln2 gives y = 1/ν = D, while the gasket "
         "with the same D gives y = 0. (4) Different D, same exponent: branching Koch curves with D = ln5/ln3, ln7/ln3 and "
         "2 all give y = ln2/ln3 ≈ 0.63. (5) Sierpiński carpets (infinitely ramified) have T_c > 0; their T_c and ν, "
         "computed with approximate Migdal–Kadanoff recursions, depend on D, on the connectivity Q and on lacunarity.\n\n"
         "The paper contrasts fractals with ε-expansions in non-integer d, which it calls purely formal continuations "
         "that assume translational invariance; it reports no ε-expansion results. Follow-up: Gefen, Aharony & "
         "Mandelbrot, J. Phys. A 16:1267 (1983), 17:435 (1984, with Shapir), 17:1277 (1984) — not read.\n\n"
         "WIKI RELEVANCE: P8 (critical exponents interpolate continuously as a function of D_eff) restates the question "
         "this paper answered in 1980, and the answer — D alone does not determine the exponents — falsifies P8 (closed "
         "2026-10-18). T5's planned test "
         "(Ising exponents on the Sierpiński gasket) has no finite-temperature transition to measure."),
        ("Mathematical Form",
         "Ramification rule: R_min finite ⇒ T_c = 0;  R_min infinite ⇒ T_c > 0\n\n"
         "Sierpiński gasket (D = ln3/ln2), exact recursion (Eq. 1):\n"
         "  e^{4K′} = (e^{12K} + 3e^{4K} + 4) / (e^{8K} + 4e^{4K} + 3)\n"
         "  near T = 0:  y = 0, ν = ∞,  ξ ∝ exp[4 exp(4K)]\n\n"
         "Nonbranching Koch curves (R = 2):  x′ = x^N  ⇒  y = 1/ν = ln N / ln b = D\n"
         "Branching Koch curves, D = ln5/ln3, ln7/ln3, 2:  y = ln2/ln3 ≈ 0.63 for all\n\n"
         "Sierpiński carpets:  D = ln(b² − l²)/ln b,  Q = ln(b − l)/ln b,  T_c > 0"),
        ("Constraint Category",
         "Geometric (Ge): the substrate's geometry and topology — fractal dimension, order of ramification, "
         "connectivity, lacunarity — together set whether a transition exists and its exponents. Dimension alone is not "
         "sufficient."),
        ("DS Cross-References",
         "P8 (Continuous Critical Exponent Interpolation on Fractional-D Substrates — restates the question and is "
         "falsified by this paper's answer; closed 2026-10-18). T5 (Critical Exponent–Dimension Sensitivity — its gasket protocol meets T_c = 0). Gate G5 "
         "(critical exponent interpolation). RG03 (Kadanoff Block Spin — the decimation method used). A2 (Richardson "
         "Effect — fractal dimension as a measured quantity)."),
        ("Mathematical Archetype",
         "Mathematical archetype: recursive-self-similarity\n\n"
         "Self-similar lattices admit exact decimation: the recursion relation for the coupling closes on itself at each "
         "scale, and its fixed points give T_c and the exponents. Topology enters through which bonds must be cut to "
         "isolate a region."),
        ("What The Math Says",
         "Put Ising spins on a fractal and renormalize by tracing out sites scale by scale. On the Sierpiński gasket the "
         "recursion for the coupling K has no fixed point at finite temperature: the system orders only at zero "
         "temperature, and the correlation length grows faster than any power. This happens whenever a finite number of "
         "bonds can isolate an arbitrarily large piece of the lattice. On carpets, where no finite cut suffices, a "
         "finite-temperature transition exists. Two lattices with the same fractal dimension can have different "
         "exponents, and lattices with different dimensions can share one. Exponents are therefore not a function of "
         "dimension alone."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Ge", _t, "recursive-self-similarity", "D-sensitive"),
))
anchor("STAT4", "doi", "10.1103/PhysRevLett.45.855",
       "Gefen, Mandelbrot & Aharony 1980 - Critical Phenomena on Fractal Lattices (PRL 45:855-858)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 as a 4-page image scan (Wayback copy of users.math.yale.edu/mandelbrot/web_pdfs/"
       "088criticalPhenomena.pdf; live server TLS expired). Abstract, ramification rule, gasket recursion and Koch results checked on "
       "the page images. Carpet values come from approximate Migdal-Kadanoff recursions.", role="progenitor")
tag("STAT4", "physics.modern.statistical_mechanics", "primary", "critical phenomena, renormalization group")
tag("STAT4", "mathematics.geometry_topology", "secondary", "fractal geometry and ramification")
LINKS += [
    ("P8", "STAT4", "derives from", "1.5",
     "P8's 'critical exponents vary continuously with non-integer D_eff' restates the question Gefen-Mandelbrot-Aharony 1980 answered: "
     "exponents depend on fractal dimension AND topology (ramification, connectivity, lacunarity), so D alone does not fix them. "
     "P8 closed as Falsified 2026-10-18 (gsw-prior-art-fold-in-2026-10-18)."),
    ("STAT4", "T5", "constrains", "1.5",
     "T5 plans Ising exponents on the Sierpinski gasket (D ~ 1.585). The gasket is finitely ramified, so T_c = 0 and nu = infinity "
     "(Gefen 1980 Eq. 1): there is no finite-temperature transition to measure. Same-D lattices give different exponents."),
    ("STAT4", "G5", "tests", "1.5",
     "Evidence against exponent interpolation as a function of dimension alone: same D gives y = D (Koch) or y = 0 (gasket); "
     "D = ln5/ln3, ln7/ln3 and 2 all give y = ln2/ln3."),
    ("STAT4", "RG03", "derives from", "2",
     "Results obtained by exact decimation (block-spin) renormalization on self-similar lattices."),
]

# ===========================================================================
# IT10 — Janke, Johnston & Kenna 2004 (source 8)
# Read: full text, arXiv:cond-mat/0401092; abstract, Eq. 12, conclusion checked first-hand.
# ===========================================================================
_t = ["information geometry", "scalar curvature", "Fisher-Rao metric", "phase transitions", "hyperscaling",
      "correlation volume", "spherical model", "planar random graphs", "1D Potts", "Lee-Yang edge"]
ENTRIES.append(dict(
    id="IT10", title="IT10: Information Geometry of Phase Transitions (Janke–Johnston–Kenna 2004)",
    filename="IT10_information_geometry_phase_transitions.md",
    scale="cross-scale", domain="information · physics", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Janke, Johnston & Kenna (2004, *Physica A* 336:181–186) put the Fisher–Rao metric on the parameter space (β, h) "
         "of solvable statistical-mechanical models and study its scalar curvature R. For these models the metric is the "
         "Hessian of the reduced free energy, G_ij = ∂_i∂_j f (Eq. 6). Abstract: \"A non-interacting model has a flat "
         "geometry (R = 0), while R diverges at the critical point of an interacting one.\" Under a standard scaling "
         "ansatz with hyperscaling, R ∼ ξ^d ∼ |β − β_c|^{α−2} (Eq. 12): the curvature scales as the correlation volume.\n\n"
         "Models: the 1D q-state Potts model, the 3D spherical model, and the Ising model on planar random graphs "
         "(2D gravity); earlier work covered 1D Ising and Bethe-lattice/mean-field models. Not the square-lattice 2D Ising "
         "model.\n\n"
         "Their own negative results: R is not positive definite in general (1D Potts), and \"the naively expected scaling "
         "behaviour (12) fails in both the three-dimensional spherical model and in the Ising model on planar random "
         "graphs\", where R ∼ |β − β_c|^{−2} because α < 0. R also diverges on the Lee–Yang edge with exponent σ = 1/2.\n\n"
         "WHAT IT DOES NOT CLAIM: the paper says nothing about first-order versus continuous transitions, and does not "
         "cite Ruppeiner. The wiki's earlier attribution to this paper of the finding that Fisher-information structure "
         "\"distinguishes transition order\" (P8's M0 status line) has no support in the text.\n\n"
         "STATUS: contested (Tier 2 †) until independently reproduced — a single short study, partly a summary of the "
         "authors' earlier papers (owner decision 2026-10-18; wiki_meta defines Established as independently reproduced)."),
        ("Mathematical Form",
         "Fisher metric (Eq. 5):  G_ij(θ) = −E[∂² ln p(x|θ) / ∂θ_i ∂θ_j]\n"
         "Stat-mech case (Eq. 6):  G_ij = ∂_i ∂_j f,   ∂_i = (∂/∂β, ∂/∂h),  f = reduced free energy per site\n\n"
         "Scalar curvature (Eq. 7):  R = −(1/2G²) × (a 3 × 3 determinant of second and third derivatives of f),   G = det(G_ij)\n\n"
         "With hyperscaling νd = 2 − α (Eq. 12):  R ∼ ξ^d ∼ |β − β_c|^{α−2}\n"
         "Fails for α < 0 (Eq. 18):  R ∼ |β − β_c|^{−2}  (3D spherical model; Ising on planar random graphs)\n"
         "Lee–Yang edge (Eq. 16):  R ∼ (z − z₀(y))^{−1/2}"),
        ("Constraint Category",
         "Informatic-Geometric (In-Gm): the curvature of the information metric on parameter space tracks interaction "
         "strength and diverges at critical points, scaling as the correlation volume when hyperscaling holds and α > 0."),
        ("DS Cross-References",
         "IT08 (Fisher-Rao Metric — the metric whose curvature is computed). BR04 (Ruppeiner Metric — the parallel "
         "thermodynamic programme; the 'curvature ∝ correlation volume' idea is Ruppeiner's, though this paper does not "
         "cite it). P8 (critical-exponent interpolation — cited this paper as prior art in M0 for a claim the paper does "
         "not make). IT05 (Fisher Information)."),
        ("Mathematical Archetype",
         "Mathematical archetype: power-law-scaling\n\n"
         "Near a continuous transition the scalar curvature diverges as a power of the distance to criticality, with an "
         "exponent fixed by α through hyperscaling, and with a different exponent when α is negative."),
        ("What The Math Says",
         "Treat temperature and field as coordinates and measure distances between models with the Fisher metric, which "
         "here is the matrix of second derivatives of the free energy. A non-interacting model gives a flat space. An "
         "interacting model gives curvature that blows up at the critical point. If hyperscaling holds, the curvature "
         "grows like the correlation length to the power d, or like the reduced temperature to the power alpha minus two. "
         "When alpha is negative, as in the three-dimensional spherical model, the regular part of the free energy "
         "dominates and the curvature grows as the reduced temperature to the power minus two instead."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In-Gm", _t, "power-law-scaling", "D-sensitive"),
))
anchor("IT10", "doi", "10.1016/j.physa.2004.01.023",
       "Janke, Johnston & Kenna 2004 - Information geometry and phase transitions (Physica A 336:181-186)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 via arXiv:cond-mat/0401092 (Elsevier version not compared). Abstract, Eq. 12 and the "
       "conclusion checked first-hand; no mention of first-order transitions or of Ruppeiner.", role="progenitor")
tag("IT10", "physics.modern.statistical_mechanics", "primary", "phase transitions in solvable models")
tag("IT10", "mathematics.geometry_topology.differential_geometry", "secondary", "scalar curvature of a metric")
tag("IT10", "information_theory", "secondary", "Fisher-Rao information geometry")
LINKS += [
    ("P8", "IT10", "couples to", "2",
     "M0 cited Janke-Johnston-Kenna 2004 as prior art for 'FIM distinguishes transition order'; the paper does not address transition "
     "order. Its relevant result is curvature R ~ xi^d ~ |beta - beta_c|^(alpha-2) under hyperscaling, failing for alpha < 0."),
    ("IT10", "IT08", "derives from", "1.5",
     "Computes the scalar curvature of the Fisher-Rao metric on (beta, h), which for these models is the Hessian of the reduced free energy."),
    ("IT10", "BR04", "couples to", "2",
     "Parallel programme: Ruppeiner's thermodynamic metric and its 'curvature ~ correlation volume' reading. JJK 2004 do not cite Ruppeiner, "
     "and they show the scaling fails when alpha < 0."),
]

# ===========================================================================
# STAT5 — Correlation-matrix spectra at criticality (source 9): Vinayak et al. 2014 + Borgs & Chayes 1996
# Read: Vinayak full text arXiv:1403.7218 v2 (Eq. 5 checked first-hand); Borgs-Chayes arXiv:adap-org/9411001 intro + Thm 3.5 (agent; proofs not read).
# ===========================================================================
_t = ["correlation matrix spectrum", "critical point", "rank-ordered eigenvalue law", "Zipf law", "2D Ising",
      "Potts covariance matrix", "Fortuin-Kasteleyn clusters", "random cluster representation", "correlation length duality"]
ENTRIES.append(dict(
    id="STAT5", title="STAT5: Correlation-Matrix Spectra at Criticality (Vinayak et al. 2014; Borgs–Chayes 1996)",
    filename="STAT5_correlation_matrix_spectra_criticality.md",
    scale="cross-scale", domain="physics · mathematics", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "VINAYAK, PROSEN, BUČA & SELIGMAN (2014, *EPL* 108:20006). For a translation-invariant lattice whose spatial "
         "correlations decay as a power law, C_nm ≈ c/|n − m|^θ, the eigenvalues of the N × N correlation matrix are the "
         "Fourier transform of the correlation function. Ranked in decreasing order they follow λ_j ≈ c_d / j^ζ with "
         "ζ = (d − θ)/d (Eq. 5). For the 2D Ising model at T_c, θ = 1/4 and ζ = 7/8. Simulations (Metropolis, L = 192, "
         "correlation matrix estimated from spin time series) give ζ = 0.8504, short of 0.875 and size-dependent. A random "
         "quarter of the sites still gives a power law (ζ = 0.838). At high temperature the spectrum matches "
         "Marčenko–Pastur. The authors call the result \"not entirely surprising\"; the abstract's \"prove\" is a continuum "
         "estimate. The paper states the law in θ, the correlation-decay exponent; θ = d − 2 + η, so θ equals the "
         "anomalous dimension η only in d = 2. It gives a rank law, not an eigenvalue-density exponent.\n\n"
         "BORGS & CHAYES (1996, *J. Stat. Phys.* 82:1235–1297). The q × q covariance matrix of a Potts pair over colours m, n, "
         "G^{mn}(x − y), is written exactly in terms of Fortuin–Kasteleyn random-cluster connectivities. In an ordered phase "
         "it has eigenvalue 0, one simple eigenvalue and one (q − 2)-fold eigenvalue — distinct correlation functions in "
         "different symmetry channels. In d = 2 a duality relation links them: ξ^{(2)}_wir(β) = ½ ξ_free(β*). In the "
         "disordered phase the matrix \"contains no more information than the standard two-point function\". This is a "
         "colour-space matrix for a fixed pair of sites, not the N × N site–site matrix; the paper says nothing about "
         "site–site spectra.\n\n"
         "WIKI RELEVANCE: CCA's FIM with per-site fields is the connected site–site correlation matrix (IT09). At a "
         "continuous transition its spectral tail is therefore fixed by known critical exponents (Vinayak), which is the "
         "basis of the M0/Phase E finding that CCA's ι at continuous T_c re-expresses standard exponents."),
        ("Mathematical Form",
         "Vinayak et al. 2014:\n"
         "  C_{n,m} ≈ c / |n − m|^θ,   1 ≪ |n − m| ≪ L          (Eq. 1; 2D Ising at T_c: θ = 1/4)\n"
         "  λ^{(k)} ≈ c′_d / |k|^{d−θ}                           (Eq. 4)\n"
         "  λ_j ≈ c_d / j^ζ,   ζ = (d − θ)/d,   1 ≪ j ≪ N = L^d    (Eq. 5; 2D Ising: ζ = 7/8; measured 0.8504 at L = 192)\n\n"
         "Borgs & Chayes 1996:\n"
         "  G^{mn}(x − y) = ⟨qδ(σ_x, m) qδ(σ_y, n)⟩ − ⟨qδ(σ_x, m)⟩⟨qδ(σ_y, n)⟩\n"
         "  disordered: G^{mn}_free = (qδ(m,n) − 1) τ_free(x − y)     (τ_free = FK connectivity)\n"
         "  ordered eigenvalues: G^{(1)}_wir = qτ^fin_wir + q(q−1)C_wir;  G^{(2)}_wir = qτ^fin_wir  ((q−2)-fold)\n"
         "  d = 2:  ξ^{(2)}_wir(β) = ½ ξ_free(β*)  for β ≥ β_o"),
        ("Constraint Category",
         "Informatic (In): at a continuous transition the eigen-structure of correlation matrices is fixed by the "
         "critical exponents, so spectral observables carry no information beyond them; in the Potts case the cluster "
         "representation fixes the colour-channel correlations."),
        ("DS Cross-References",
         "STAT3 (CCA class — Vinayak and Borgs–Chayes are among its cited prior art). gloss_anomalous_dimension_cca_isotropy_iota "
         "(CCA's ι, the Zipf-tail slope of the FIM spectrum — at continuous T_c it corresponds to Vinayak's ζ). "
         "gloss_anomalous_dimension_critical (standard η). IT09 (sloppy models — the per-site-field FIM is a covariance matrix). "
         "M6 (Fisher Information Rank)."),
        ("Mathematical Archetype",
         "Mathematical archetype: power-law-scaling\n\n"
         "A power-law correlation function on a periodic lattice gives power-law eigenvalues, because the eigenvalues are "
         "its Fourier transform; the rank exponent follows from the decay exponent and the dimension."),
        ("What The Math Says",
         "On a periodic lattice the correlation matrix depends only on the separation between sites, so its eigenvectors "
         "are plane waves and its eigenvalues are the Fourier transform of the correlation function. If correlations fall "
         "off as distance to the power minus theta, the eigenvalue at wavevector k grows as one over k to the power d "
         "minus theta. Counting eigenvalues from the top, the j-th one falls as j to the power minus zeta, with zeta "
         "equal to d minus theta over d — seven eighths for the 2D Ising model at its critical point. Separately, the "
         "Potts colour-covariance matrix for two sites splits into channels whose correlation functions are cluster "
         "connectivities in the Fortuin–Kasteleyn representation."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "power-law-scaling", "D-sensitive"),
))
anchor("STAT5", "doi", "10.1209/0295-5075/108/20006",
       "Vinayak, Prosen, Buca & Seligman 2014 - Spectral analysis of finite-time correlation matrices near equilibrium phase transitions (EPL 108:20006)",
       "canonical_authority",
       "Primary source. Full text of arXiv:1403.7218 v2 read 2026-10-18 (EPL version not compared). Eq. 5 and zeta = 7/8, 0.8504 checked "
       "first-hand. The paper states the law in theta (correlation decay), not eta, and gives a rank law, not a density exponent.",
       role="progenitor", stability="active-literature")
anchor("STAT5", "doi", "10.1007/BF02183383",
       "Borgs & Chayes 1996 - The covariance matrix of the Potts model: a random cluster analysis (J. Stat. Phys. 82:1235-1297)",
       "canonical_authority",
       "arXiv:adap-org/9411001 read 2026-10-18: abstract, introduction and Theorem 3.5 (by research agent; proofs not read). The matrix is "
       "q x q over colours for a fixed site pair, not the N x N site-site matrix. DOI verified on Crossref.", role="progenitor",
       confidence="medium")
tag("STAT5", "physics.modern.statistical_mechanics", "primary", "critical correlations, Potts/Ising models")
tag("STAT5", "mathematics.probability_measure", "secondary", "random-cluster measures, correlation-matrix spectra")
LINKS += [
    ("STAT5", "gloss_anomalous_dimension_cca_isotropy_iota", "predicts for", "1.5",
     "CCA's iota is the Zipf-tail slope of the per-site-field FIM spectrum, i.e. of the connected correlation matrix. At a continuous "
     "transition Vinayak et al. 2014 give lambda_j ~ j^-zeta, zeta = (d - theta)/d (7/8 for 2D Ising), so iota there re-expresses theta."),
    ("STAT5", "STAT3", "couples to", "2",
     "Prior art cited by STAT3. Vinayak: correlation-matrix rank law at 2D Ising T_c (no Potts, no first-order, no temperature sweep). "
     "Borgs-Chayes: q x q Potts colour covariance via FK clusters - not the site-site matrix CCA uses."),
]

# ===========================================================================
# STAT6 — Brown, Bossomaier & Barnett 2022 (source 10)
# Read: full text, published (PMC9452544) + arXiv:1810.09607 v3; key findings checked first-hand on arXiv text.
# ===========================================================================
_t = ["global transfer entropy", "information flow", "first-order phase transition", "Potts model", "Glauber dynamics",
      "early warning", "cluster interface length", "disordered-side peak"]
ENTRIES.append(dict(
    id="STAT6", title="STAT6: Global Transfer Entropy at First-Order Transitions (Brown–Bossomaier–Barnett 2022)",
    filename="STAT6_global_transfer_entropy_phase_transitions.md",
    scale="cross-scale", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Brown, Bossomaier & Barnett (2022, *Sci. Rep.* 12:15145) measure global transfer entropy (GTE) — the average "
         "information flow from each site's neighbourhood to the site, G = (1/N) Σ_i T_{s→s_i}, a lag-1 conditional mutual "
         "information under Glauber dynamics — across the transition of the 2D q-state Potts model for q = 5, 7, 10 "
         "(L = 32, 64, 128). Earlier work (Barnett et al. 2013, PRL) found that GTE peaks on the disordered side of the "
         "continuous Ising transition. Here the peak is also on the disordered side at finite size for these first-order "
         "transitions. As the transition becomes more strongly first order the peak moves towards T_c, and they argue "
         "that in the thermodynamic limit \"G becomes discontinuous at the transition temperature, T_c, peaking at T_c^+.\"\n\n"
         "Mechanism (stated as a conjecture in the published text): information flows only across boundaries between "
         "same-state (geometric) spin clusters, so G ∝ Σ_c p(c) L_c, with L_c the average interface length of clusters of "
         "size c. The average interface length, computed for q = 2, 5, 7, 10, tracks the GTE peak locations "
         "qualitatively, which they offer as a single framework for both transition orders.\n\n"
         "Caveats: strong finite-size effects (L ≤ 128); the early-warning effect \"holds most strongly for finite-size "
         "systems\"; one estimator shows a spurious ordered peak; the mechanism match is by peak location, without a fit.\n\n"
         "WIKI RELEVANCE: the main prior art for CCA-1c (do FIM-spectrum curve shapes distinguish first-order from "
         "continuous Potts transitions?). Differences: GTE is dynamical and multi-site; CCA's observables are equal-time "
         "two-point. \"Hybrid two-point + multi-point\" is the wiki's description, not the authors'. GTE was computed for "
         "q = 5, 7, 10; q = 2 enters only through earlier Ising work and the interface-length figure.\n\n"
         "STATUS: contested (Tier 2 †) until independently reproduced — a single numerical study at L ≤ 128 "
         "(owner decision 2026-10-18; wiki_meta defines Established as independently reproduced)."),
        ("Mathematical Form",
         "Transfer entropy (lag 1):  T_{Y→X} = I(X_t ; Y_{t−1} | X_{t−1}) = H(X_t | X_{t−1}) − H(X_t | X_{t−1}, Y_{t−1})\n"
         "Global transfer entropy:   G = (1/N) Σ_i T_{s→s_i}   (s = the site's neighbourhood)\n"
         "  G ≥ 0, with G = 0 iff each site, conditioned on its past, is independent of its neighbours\n\n"
         "Potts model:  H = −J Σ_⟨ij⟩ δ(s_i, s_j),   T_c = 1 / ln(1 + √q)\n\n"
         "Interface conjecture:  G ∝ Σ_c p(c) L_c"),
        ("Constraint Category",
         "Informatic (In): information flow between sites is bounded by the length of interfaces between unlike states, "
         "which links an information-theoretic observable to cluster geometry at both transition orders."),
        ("DS Cross-References",
         "STAT3 (CCA class — Brown et al. is the prior art for CCA-1c's question and supplies a mechanism CCA lacks). "
         "X0_FIM_Regimes (three-state classification — claims a first-order vs continuous signature from FIM structure). "
         "INFO4 (Mutual Information — transfer entropy is a conditional mutual information). STAT5 (correlation-matrix "
         "spectra — the equal-time two-point counterpart)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "An information-flow observable peaks near a phase transition; at a strongly first-order transition it is "
         "argued to become discontinuous at T_c in the thermodynamic limit."),
        ("What The Math Says",
         "For each lattice site, ask how much the neighbours' previous states tell you about the site's next state beyond "
         "what its own previous state tells you, and average over sites. Deep in the ordered phase neighbours agree and "
         "nothing flows; deep in the disordered phase correlations are short. In between, the measure peaks — on the "
         "disordered side at finite size, both for the continuous Ising transition and for first-order Potts "
         "transitions. The authors attribute this to flow along the boundaries of same-colour clusters, whose total length "
         "peaks in the same place."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "threshold-transition", "D-sensitive"),
))
anchor("STAT6", "doi", "10.1038/s41598-022-17359-w",
       "Brown, Bossomaier & Barnett 2022 - Information flow in first-order Potts model phase transition (Sci. Rep. 12:15145)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18: published version (PMC9452544) by research agent; arXiv:1810.09607 v3 first-hand. "
       "GTE computed for q = 5, 7, 10 only; interface mechanism labelled a conjecture in the published text.",
       role="progenitor", stability="active-literature")
tag("STAT6", "physics.modern.statistical_mechanics", "primary", "first-order Potts transitions")
tag("STAT6", "information_theory.shannon", "secondary", "transfer entropy")
LINKS += [
    ("STAT6", "STAT3", "analogous to", "1.5",
     "Brown et al. 2022 distinguish first-order from continuous Potts transitions with an information observable (GTE) and give a "
     "cluster-interface mechanism - the prior art for CCA-1c. GTE is dynamical and multi-site; CCA's d_eff/iota are equal-time two-point."),
    ("STAT6", "X0_FIM_Regimes", "analogous to", "2",
     "X0 claims a first-order vs continuous signature from FIM structure; Brown et al. report one from transfer entropy with a stated "
     "mechanism (G ~ sum_c p(c) L_c, a conjecture)."),
    ("STAT6", "INFO4", "derives from", "2",
     "Transfer entropy is a conditional mutual information, T = I(X_t ; Y_t-1 | X_t-1)."),
]

# ===========================================================================
# BIO12 — West, Brown & Enquist 1997 (source 1)
# Read: full text (Science reprint copy); Eq. 5, assumptions, p. 126 D/(D+1) and Table 1 checked (agent on page images; Eq. 5 context,
# assumptions and p. 126 first-hand). WBE 1999 (Science 284:1677) full text first-hand.
# ===========================================================================
_t = ["West-Brown-Enquist model", "WBE", "fractal distribution network", "quarter-power scaling", "Kleiber's law",
      "space-filling branching", "area-preserving branching", "terminal units", "impedance matching", "a = D/(D+1)",
      "finite-size corrections"]
ENTRIES.append(dict(
    id="BIO12", title="BIO12: West–Brown–Enquist Fractal Network Model of Allometric Scaling (1997)",
    filename="BIO12_west_brown_enquist_network_model.md",
    scale="organismal", domain="biology · physics", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "West, Brown & Enquist (1997, *Science* 276:122–126) derive quarter-power allometric scaling from the geometry of "
         "resource-distribution networks. Their three assumptions: a space-filling, fractal-like branching network supplies "
         "the whole body; the final branch (capillary) is a size-invariant unit; and the energy needed to distribute "
         "resources is minimized. For a self-similar network with branching ratio n, radius ratio β = r_{k+1}/r_k and length "
         "ratio γ = l_{k+1}/l_k, metabolic rate B ∝ M^a with a = −ln n / ln(γβ²) (Eq. 5). Space filling gives γ = n^{−1/3}; "
         "area-preserving branching gives β = n^{−1/2}; so a = 3/4. The authors stress the result is \"essentially a "
         "geometric one, strictly applying only to systems that exhibit area-preserving branching\". Pure Poiseuille "
         "(cubic-law) branching, β = n^{−1/3}, gives a = 1; area preservation in large vessels comes from impedance matching "
         "of the pulsatile flow. The model predicts a family of quarter powers (Table 1): aorta radius 3/8, circulation "
         "time 1/4, heart rate −1/4, capillary number 3/4.\n\n"
         "Dimension: \"Because the fractal network must still fill the entire D-dimensional volume, our result generalizes "
         "to a = D/(D + 1). Organisms are three-dimensional, which explains the 3 in the numerator\" (p. 126; restated in "
         "WBE 1999, *Science* 284:1677). D here is the dimension of the space the network fills, not a measured fractal "
         "dimension of the vascular tree.\n\n"
         "CONTESTED as the explanation of metabolic scaling. The authors call it an \"idealized zeroth-order "
         "approximation\". Savage, Deeds & Fontana (2008, *PLoS Comput. Biol.*, abstract) find that 3/4 holds only in the "
         "limit of infinite network size and that the model predicts about 0.81 over the mammal range. Dodds, Rothman & "
         "Weitz 2001 and Kozłowski & Konarzewski 2004 dispute the derivation (not read this pass); Glazier (BIO14) and C1's "
         "replication record dispute a universal 3/4. Maino et al. (BIO15) derive the same finite-size equation from DEB "
         "assumptions.\n\n"
         "WIKI RELEVANCE: P2's α = D_eff/(D_eff + 1) is WBE's a = D/(D+1) with D renamed; reading D as a measured vascular "
         "dimension is the wiki's reinterpretation, not WBE's. H5 claims WBE as its λ = 1 case."),
        ("Mathematical Form",
         "Allometry (Eq. 1):  Y = Y₀ M^b;   metabolic rate B ∝ M^a\n"
         "Self-similar network:  β = r_{k+1}/r_k,  γ = l_{k+1}/l_k,  N_k = n^k\n"
         "Exponent (Eq. 5):  a = −ln n / ln(γβ²)\n"
         "  space filling:     γ = n^{−1/3}\n"
         "  area preserving:   β = n^{−1/2}   ⇒  a = 3/4\n"
         "  Poiseuille (cubic): β = n^{−1/3}  ⇒  a = 1\n"
         "Generalization (p. 126):  a = D/(D + 1)\n"
         "Table 1 (predicted):  aorta radius 3/8;  circulation time 1/4;  heart rate −1/4;  capillary number 3/4;  B 3/4"),
        ("Constraint Category",
         "Geometric (Ge): the exponent follows from how a space-filling hierarchical network with invariant terminal units "
         "fills a D-dimensional body, with flow physics (impedance matching vs Poiseuille) choosing the radius scaling."),
        ("DS Cross-References",
         "C1 (Metabolic Scaling — WBE is C1's axiomatic-foundation anchor and the 3/4 explanation C1's replication record "
         "contests). P2 (Metabolic Exponent Tracks Vascular D_eff — restates a = D/(D+1); folded 2026-10-18). H5 (β(λ) — "
         "claims WBE as its λ = 1 case). X1 (Vascular/Metabolic instantiation). FM4 (Poiseuille's Law — the r⁴ resistance "
         "used in Eq. 6; pure Poiseuille branching gives a = 1). BIO13, BIO14, BIO15 (rival or corrective accounts)."),
        ("Mathematical Archetype",
         "Mathematical archetype: dimensional-scaling\n\n"
         "The exponent is a rational function of the dimension of the filled space, a = D/(D+1): the network adds an "
         "effective extra dimension, so metabolic rate scales as a volume in D + 1 dimensions measured in D."),
        ("What The Math Says",
         "Branch a tube n ways at each level, shrinking radii by beta and lengths by gamma. Requiring the tubes to fill the "
         "body makes gamma equal to n to the minus one third. Requiring the cross-sectional area to be preserved at each "
         "branch, which avoids reflecting the pressure wave, makes beta equal to n to the minus one half. Fixing the size "
         "of the capillaries and summing the blood volume over all levels gives metabolic rate proportional to mass to "
         "the power minus log n over log of gamma times beta squared, which is three quarters. In D dimensions it is D "
         "over D plus one. If instead branching follows Poiseuille's cube law, the exponent is one."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Ge", _t, "dimensional-scaling", "D-sensitive"),
))
anchor("BIO12", "doi", "10.1126/science.276.5309.122",
       "West, Brown & Enquist 1997 - A General Model for the Origin of Allometric Scaling Laws in Biology (Science 276:122-126)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 (Science reprint copy, umdberg.pbworks.com). Eq. 5, assumptions and Table 1 checked on page "
       "images by research agent; the p. 126 'a = D/(D+1)' and '3 in the numerator' passage checked first-hand.", role="progenitor")
anchor("BIO12", "doi", "10.1126/science.284.5420.1677",
       "West, Brown & Enquist 1999 - The Fourth Dimension of Life: Fractal Geometry and Allometric Scaling of Organisms (Science 284:1677-1679)",
       "cites",
       "Full text read first-hand 2026-10-18 (pdodds.w3.uvm.edu copy): 'In D dimensions ... generalizes to give a ~ B ~ M^(D/(D+1))'.")
anchor("BIO12", "doi", "10.1371/journal.pcbi.1000171",
       "Savage, Deeds & Fontana 2008 - Sizing up allometric scaling theory (PLoS Comput. Biol. 4:e1000171)",
       "cites",
       "Abstract only (read by research agent 2026-10-18): 3/4 holds only in the infinite-size limit; about 0.81 predicted over the mammal range.",
       stability="active-literature", confidence="medium")
tag("BIO12", "biology.physiology", "primary", "metabolic scaling, cardiovascular networks")
tag("BIO12", "networks_systems", "secondary", "hierarchical branching networks")
LINKS += [
    ("P2", "BIO12", "derives from", "1.5",
     "P2's alpha = D_eff/(D_eff + 1) is WBE's a = D/(D+1) (WBE 1997 p. 126; WBE 1999) with D renamed. In WBE, D is the dimension of the "
     "space the network fills; reading it as a measured vascular dimension is P2's own move. P2 folded 2026-10-18."),
    ("BIO12", "C1", "predicts for", "1.5",
     "WBE predicts B ~ M^(3/4) from space-filling, area-preserving branching with invariant capillaries; C1's replication record contests "
     "a universal 3/4, and finite-size WBE gives ~0.81 over mammals (Savage et al. 2008)."),
    ("H5", "BIO12", "generalizes", "2",
     "H5's own claim (Speculative): beta(lambda = 1) = d_f/(d_f+1) recovers WBE. WBE's D is the embedding dimension, not d_f."),
    ("X1", "BIO12", "derives from", "2",
     "X1's vascular mapping uses WBE's network model and its D/(D+1) exponent."),
    ("FM4", "BIO12", "implements", "2",
     "Poiseuille resistance R_k = 8 mu l_k / (pi r_k^4) enters WBE Eq. 6; pure Poiseuille (cubic-law) branching would give a = 1, not 3/4."),
]

# ===========================================================================
# BIO13 — Allometric cascade debate (source 2): Darveau et al. 2002; West et al. 2003; Banavar et al. 2003; Darveau reply 2003
# Read: all full text (agent); West 2003 published wording first-hand; arXiv:physics/0211058 first-hand in the 2026-10-18 H5 gate.
# ===========================================================================
_t = ["allometric cascade", "multiple-causes model", "control coefficients", "metabolic control analysis",
      "exponent sum rule", "b = sum c_i b_i", "dimensional homogeneity", "parallel vs series processes", "elasticity of a sum"]
ENTRIES.append(dict(
    id="BIO13", title="BIO13: Allometric Cascade and the Exponent Sum Rule (Darveau 2002; West et al. 2003)",
    filename="BIO13_allometric_cascade_sum_rule.md",
    scale="organismal", domain="biology", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "PROPOSAL. Darveau, Suarez, Andrews & Hochachka (2002, *Nature* 417:166–170) proposed a \"multiple-causes model of "
         "allometry\": MR = a Σ c_i M^{b_i} (Eq. 2), where b_i is the scaling exponent of process i and c_i its control "
         "coefficient, the c_i summing to 1 \"by definition\". With literature control coefficients they obtained b ≈ 0.76 "
         "for basal and 0.82–0.92 for maximal metabolic rate.\n\n"
         "CORRECTION. West, Savage, Gillooly, Enquist, Woodruff & Brown (2003, *Nature* 421:713) showed Eq. 2 violates "
         "dimensional homogeneity — for basal rate it gives b ≈ 0.76 with mass in kilograms and 1.08 in picograms. With "
         "c_i ≡ ∂lnB/∂lnB_i the standard sum rules give Σc_i = 1 and \"b = Σc_i b_i, the equations that Darveau et al. "
         "should have used\"; these are \"very general, requiring no assumptions about how B and B_i scale, or whether the "
         "B_i are connected in parallel or in series.\" For a parallel sum B = ΣB_i the weights are the shares, c_i = B_i/B "
         "(explicit in the preprint, arXiv:physics/0211058), which vary with mass, and the model is \"simply a consistency "
         "check on the conservation of energy … and so must be trivially correct.\" They also argue most of the processes "
         "act in series, not in parallel, so adding them double counts.\n\n"
         "Banavar, Damuth, Maritan & Rinaldo (2003, *Nature* 421:713–714) independently called the model \"flawed and … "
         "meaningless\": \"it does not follow that an effective exponent is simply a weighted average of the individual "
         "exponents.\" Darveau et al.'s reply (*Nature* 421:714) conceded that the equation \"does not distinguish between\" "
         "parallel demand and series supply processes and proposed MR₀Σc_i(M/M₀)^{b_i}; Banavar et al. note that M₀ is "
         "arbitrary across 20 orders of magnitude.\n\n"
         "STATUS: Eq. 2 as published is wrong, which its authors partly concede. The corrected identity — the log–log slope "
         "of a sum is the share-weighted mean of the component slopes — is exact bookkeeping (the elasticity-of-a-sum rule) "
         "and carries no mechanism. H5's two-process \"derivation\" is this identity (H5 prior-art gate, 2026-10-18)."),
        ("Mathematical Form",
         "Darveau et al. 2002, Eq. 2 (incorrect):  MR = a Σ_i c_i M^{b_i},   Σ c_i = 1, c_i constant\n\n"
         "West et al. 2003 (general):\n"
         "  c_i ≡ ∂ln B / ∂ln B_i,   Σ c_i = 1,   Σ c_i ε_i = 0,   ε_i = b − b_i\n"
         "  b(M) ≡ d ln B / d ln M = Σ c_i b_i\n"
         "Parallel sum B = Σ B_i:  c_i = B_i / B = (a_i/a) M^{−ε_i}   (mass-dependent)\n\n"
         "Two processes, B = αM^p + βM^q:  b = p·f + q·(1 − f),  f = αM^p / B"),
        ("Constraint Category",
         "Thermodynamic (Th): an energy-budget identity — the whole-organism exponent is the flux-weighted average of "
         "component exponents. It constrains bookkeeping, not mechanism."),
        ("DS Cross-References",
         "H5 (β(λ) — its two-process identity is West et al.'s sum rule; λ = B_i/B is their c_i). C1 (Metabolic Scaling). "
         "BIO12 (WBE — the single-network account the cascade was offered against). BIO14 (Glazier — criticised the cascade "
         "in 2005). BIO15 (DEB — a mechanistic two-term flux sum)."),
        ("Mathematical Archetype",
         "Mathematical archetype: linear-proportionality\n\n"
         "The exponent of a sum is a linear combination of component exponents with weights equal to each component's "
         "share. The weights move with mass, which is why fixed weights (Darveau's Eq. 2) fail."),
        ("What The Math Says",
         "Write total metabolic rate as a sum of processes, each scaling with mass at its own power. The slope of log rate "
         "against log mass is then the average of the component slopes, weighted by each process's current share of the "
         "total. Because the shares change with mass, the weights cannot be fixed constants. Fixing them, as the 2002 "
         "equation did, makes the answer depend on the units of mass. The correct version is one line of calculus and "
         "true for any positive terms, so it says nothing about which processes there are or why they scale as they do."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th", _t, "linear-proportionality", "D-invariant"),
))
anchor("BIO13", "doi", "10.1038/417166a",
       "Darveau, Suarez, Andrews & Hochachka 2002 - Allometric cascade as a unifying principle of body mass effects on metabolism (Nature 417:166-170)",
       "canonical_authority",
       "Primary source of the cascade proposal. Full text read 2026-10-18 by research agent (pdodds.w3.uvm.edu copy); Eq. 2 checked on page image.",
       role="progenitor")
anchor("BIO13", "doi", "10.1038/421713a",
       "West, Savage, Gillooly, Enquist, Woodruff & Brown 2003 - Why does metabolic rate scale with body size? (Nature 421:713)",
       "cites",
       "Published text read first-hand 2026-10-18 (pdodds.w3.uvm.edu copy of Nature 421:713-714); preprint arXiv:physics/0211058 read in the "
       "2026-10-18 H5 gate. c_i = B_i/B is explicit only in the preprint; '0.78 in g' is preprint-only.")
anchor("BIO13", "doi", "10.1038/421713b",
       "Banavar, Damuth, Maritan & Rinaldo 2003 - Allometric cascades (Nature 421:713-714)",
       "cites",
       "Full text read 2026-10-18 (same two-page PDF as West et al. 2003); 'weighted average' quote checked first-hand.")
anchor("BIO13", "doi", "10.1038/421714a",
       "Darveau, Suarez, Andrews & Hochachka 2003 - Reply (Nature 421:714)",
       "cites",
       "Full text read 2026-10-18 (same two-page PDF); concession that Eq. 2 'does not distinguish between' parallel and series processes.")
tag("BIO13", "biology.physiology", "primary", "metabolic scaling, metabolic control analysis")
LINKS += [
    ("H5", "BIO13", "derives from", "1.5",
     "H5's two-process identity d ln B/d ln M = p f + q (1 - f) is West et al. 2003's correction b = sum c_i b_i with c_i = B_i/B "
     "(RESTATEMENT; H5 prior-art gate 2026-10-18). H5 stays Speculative: the identity is bookkeeping, the choice of processes is not."),
    ("BIO13", "BIO12", "tensions with", "2",
     "The cascade was offered as a multiple-causes alternative to WBE's single network; West et al. reply that the parallel-sum version "
     "is a trivially correct energy-conservation check and so cannot conflict with WBE."),
]

# ===========================================================================
# BIO14 — Glazier's metabolic-level boundaries hypothesis (source 3)
# Read: Glazier 2005 full text, Glazier 2010 full text (agent; Eqs. 2-3 and abstract wording checked first-hand).
# ===========================================================================
_t = ["metabolic-level boundaries hypothesis", "MLBH", "Glazier", "surface-area limits", "volume limits",
      "metabolic level", "activity level", "no universal 3/4 law", "U-shaped b vs L"]
ENTRIES.append(dict(
    id="BIO14", title="BIO14: Metabolic-Level Boundaries Hypothesis (Glazier 2005, 2010)",
    filename="BIO14_metabolic_level_boundaries_hypothesis.md",
    scale="organismal", domain="biology", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Glazier (2005, *Biol. Rev.* 80:611–662; 2010, *Biol. Rev.* 85:111–138) argues that there is no universal 3/4 "
         "law. The metabolic scaling exponent b lies between two boundary constraints: surface-area limits on fluxes of "
         "resources, wastes and heat (∝ M^{2/3}) and volume limits on power production (∝ M¹). Which constraint dominates "
         "depends on metabolic level L. In resting organisms b falls as L rises — near 1 in dormant organisms, near 2/3 in "
         "cold-exposed endotherms; in active organisms b rises with L and approaches 1 in maximal bursts, because muscle "
         "power scales with muscle mass. Overall b versus L is \"approximately U-shaped\", and the slope \"should vary "
         "mostly between 2/3 and 1\" (2010 abstract). Glazier presents the hypothesis as \"an extension of Kooijman's (2000) "
         "boundary approach\" (2005, p. 632; see BIO15).\n\n"
         "The 2010 paper writes the exponent as a weighted mix: b = f(L) = 1·p + (2/3)(1 − p) = (p + 2)/3 (Eq. 2), \"where p "
         "and 1 − p are the proportions of influence of the volume and surface-area boundary constraints\". No functional "
         "form for p(L) is given; Glazier calls for \"a quantitative, mechanistic theory\" of how the constraints interact "
         "(2010, p. 125).\n\n"
         "CONTESTED. Glazier calls it \"obviously oversimplified\" with observed exceptions (2005); slope–intercept "
         "autocorrelation can confound b–L relations (2010, p. 119); 2/3 and 1 are not strict bounds (2005 lists other "
         "boundary slopes, and the 3/4 internal-surface boundary is itself disputed).\n\n"
         "WIKI RELEVANCE: H5's β(λ) = λ·d_f/(d_f+1) + (1 − λ)·1 has the same form as Glazier's Eq. 2: with d_f = 2 and "
         "λ = 1 − p it is identical, and both read the weight as activity-dependent. Glazier published it in 2010."),
        ("Mathematical Form",
         "Boundaries:  surface-area limit  R ∝ M^{2/3};   volume limit  R ∝ M¹\n\n"
         "Glazier 2010, Eqs. 2–3:\n"
         "  b = f(L) = 1·(p) + (2/3)(1 − p) = (p + 2)/3\n"
         "  R = a M^{f(L)} = a M^{(p+2)/3}\n"
         "  p = 1 (minimal inactive, maximal active):  b = 1\n"
         "  p = 0 (maximal inactive):                  b = 2/3\n\n"
         "Predicted pattern: resting b decreasing in L; active b increasing in L; overall U-shaped."),
        ("Constraint Category",
         "Geometric (Ge): the exponent is bracketed by surface-area (2/3) and volume (1) scaling, with metabolic level "
         "setting which geometric limit binds."),
        ("DS Cross-References",
         "C1 (Metabolic Scaling — Glazier's reviews are part of the 'no universal exponent' consensus C1 cites). H5 (β(λ) "
         "— same interpolation form, earlier). BIO12 (WBE — Glazier disputes its universal 3/4). BIO15 (DEB — the boundary "
         "approach MLBH extends). BIO13 (cascade — criticised by Glazier 2005)."),
        ("Mathematical Archetype",
         "Mathematical archetype: power-law-scaling\n\n"
         "Metabolic rate is a power of mass whose exponent is interpolated between the surface and volume exponents by an "
         "activity-dependent weight."),
        ("What The Math Says",
         "Metabolism is limited either by surfaces, which scale as mass to the two-thirds, or by volume, which scales as "
         "mass to the first power. Let p be the share of influence of the volume limit. Then the exponent is p times one "
         "plus one minus p times two thirds, which is p plus two over three. Resting animals with high metabolic level are "
         "surface-limited and sit near two thirds; dormant animals and animals at full exertion are volume-limited and sit "
         "near one. The hypothesis does not say how p depends on metabolic level."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Ge", _t, "power-law-scaling", "D-sensitive"),
))
anchor("BIO14", "doi", "10.1017/S1464793105006834",
       "Glazier 2005 - Beyond the '3/4-power law': variation in the intra- and interspecific scaling of metabolic rate in animals (Biol. Rev. 80:611-662)",
       "canonical_authority",
       "Primary source (MLBH first stated, p. 632). Full text read 2026-10-18 by research agent (pdodds.w3.uvm.edu copy).", role="progenitor")
anchor("BIO14", "doi", "10.1111/j.1469-185X.2009.00095.x",
       "Glazier 2010 - A unifying explanation for diverse metabolic scaling in animals and plants (Biol. Rev. 85:111-138)",
       "cites",
       "Full text read 2026-10-18 (Wayback copy of an LMU teaching PDF); abstract wording and Eqs. 2-3 checked first-hand.")
tag("BIO14", "biology.physiology", "primary", "metabolic scaling and activity level")
tag("BIO14", "biology.ecology", "secondary", "comparative scaling across animals and plants")
LINKS += [
    ("BIO14", "C1", "predicts for", "1.5",
     "MLBH: the metabolic exponent varies mostly between 2/3 and 1 with metabolic level (resting b falls with L, active b rises toward 1); "
     "no universal 3/4."),
    ("H5", "BIO14", "analogous to", "1.5",
     "Same mathematical form, same domain, earlier: Glazier 2010 Eq. 2, b = 1 p + (2/3)(1 - p), is H5's beta(lambda) with d_f = 2 and "
     "lambda = 1 - p, with the same activity-level reading. Glazier gives no p(L), as H5 gives no lambda mechanism."),
    ("BIO14", "BIO12", "tensions with", "1.5",
     "Glazier argues there is no universal 3/4-power law; WBE derives 3/4 from network geometry."),
    ("BIO14", "BIO15", "derives from", "2",
     "Glazier presents the MLBH as 'an extension of Kooijman's (2000) boundary approach' (2005, p. 632)."),
]

# ===========================================================================
# BIO15 — Dynamic Energy Budget theory (source 4)
# Read: Sousa, Domingos & Kooijman 2008 full text (PMC HTML; appendix with proofs not read); Maino et al. 2014 published abstract
# + July 2012 manuscript full text (not the version of record); Kooijman 2010 book NOT read.
# ===========================================================================
_t = ["Dynamic Energy Budget theory", "DEB", "Kooijman", "reserve and structure", "isomorph", "surface-area assimilation",
      "volume-linked maintenance", "reserve mobilisation", "metabolic scaling", "intra- vs interspecific scaling"]
ENTRIES.append(dict(
    id="BIO15", title="BIO15: Dynamic Energy Budget Theory and Metabolic Scaling (Kooijman)",
    filename="BIO15_dynamic_energy_budget_theory.md",
    scale="organismal", domain="biology", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Dynamic Energy Budget (DEB) theory (Kooijman; 3rd ed. 2010) models an organism as reserve plus structure. In the "
         "standard model the organism is an isomorph, with surface area ∝ V^{2/3}. Assimilation is proportional to surface "
         "area, ṗ_A = {ṗ_Am} V^{2/3} f(X), because \"mass and energy transport are proportional to surface areas\"; "
         "maintenance is proportional to structural volume, ṗ_M = ([ṗ_M] + {ṗ_T}/L) V, with a surface-linked term for "
         "heating or osmosis (Sousa, Domingos & Kooijman 2008, *Phil. Trans. R. Soc. B* 363:2453). Respiration therefore "
         "mixes surface- and volume-proportional terms. Sousa et al. state that oxygen consumption of fasting animals "
         "scales as w^α with α ∈ [0.66, 1] within a species, and α ∈ [0.5, 1] across species' fully grown adults "
         "(propositions; proofs in an appendix not read here).\n\n"
         "Interspecific scaling (Maino, Kearney, Nisbet & Kooijman 2014, *J. Anim. Ecol.* 83:20). Through reserve "
         "mobilisation they derive, for adults, mass as M = C₀Ḃ + C₁Ḃ^{4/3}, which their manuscript calls \"precisely "
         "the equation\" derivable from the finite-size WBE model; Ḃ ∝ M^{3/4} only as mass → ∞. Consequence: \"mechanistic "
         "theories based on completely different principles can be used to derive the same equations\", so fits to scaling "
         "data cannot separate DEB from WBE. The published abstract: the DEB mechanism \"does not necessarily contradict\" "
         "transport-based models and explains intra- versus interspecific differences. (Quotes from a July 2012 manuscript "
         "except where marked as the published abstract.)\n\n"
         "CONTESTED as an explanation of metabolic scaling: DEB and WBE fit the same data on different assumptions. DEB "
         "itself is a long-developed general theory of metabolic organisation; this entry concerns its scaling account.\n\n"
         "WIKI RELEVANCE: DEB supplies named processes (surface-linked assimilation, volume-linked maintenance) for the "
         "two-term sums that H5 and Ballesteros et al. 2018 take as given."),
        ("Mathematical Form",
         "Sousa, Domingos & Kooijman 2008:\n"
         "  assimilation:  ṗ_A = {ṗ_Am} V^{2/3} f(X)\n"
         "  maintenance:   ṗ_M = [ṗ_M]* V,   [ṗ_M]* = [ṗ_M] + {ṗ_T}/L,   L = V^{1/3}\n"
         "  respiration of fasting animals ∝ w^α:  α ∈ [0.66, 1] (intraspecific),  α ∈ [0.5, 1] (interspecific)\n\n"
         "Maino et al. (manuscript), adults at ultimate size:\n"
         "  ṗ_M = V[ṗ_M],   ṗ_C = v̇E / V^{1/3},   E_m = V_m^{4/3} [ṗ_M]/v̇\n"
         "  M = C₀Ḃ + C₁Ḃ^{4/3}   ⇒   Ḃ ∝ M^{3/4} only as M → ∞"),
        ("Constraint Category",
         "Thermodynamic (Th): conservation of energy and mass across reserve and structure, with transport across surfaces "
         "and maintenance by volume; the scaling exponent emerges from the balance of these fluxes."),
        ("DS Cross-References",
         "C1 (Metabolic Scaling). H5 (β(λ) — DEB names the two processes H5's two-term identity leaves open). BIO12 (WBE — "
         "the same finite-size equation from different assumptions). BIO14 (MLBH — extends Kooijman's boundary approach). "
         "BIO13 (cascade — the bookkeeping identity any flux sum obeys)."),
        ("Mathematical Archetype",
         "Mathematical archetype: conservation-law\n\n"
         "Energy budgets close: assimilation, mobilisation, maintenance and growth must balance. Scaling relations follow "
         "from which fluxes scale with surface and which with volume, not from a postulated exponent."),
        ("What The Math Says",
         "An organism takes in food across surfaces, so assimilation scales as volume to the two-thirds. It pays "
         "maintenance on its structure, so maintenance scales as volume. Respiration mixes the two, so its apparent "
         "exponent sits between two thirds and one depending on growth and reserve. Across species, setting reserve "
         "mobilisation equal to maintenance at ultimate size gives mass as a sum of metabolic rate and metabolic rate to "
         "the four-thirds — the same form the network model gives — so the three-quarter law appears only for very large "
         "masses."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Th", _t, "conservation-law", "D-sensitive"),
))
anchor("BIO15", "doi", "10.1098/rstb.2007.2230",
       "Sousa, Domingos & Kooijman 2008 - From empirical patterns to theory: a formal metabolic theory of life (Phil. Trans. R. Soc. B 363:2453-2464)",
       "canonical_authority",
       "Formal statement of DEB theory by its originator's group. Full text (PMC2606805 HTML) read 2026-10-18 by research agent; the "
       "supplementary appendix with proofs not read. Used in place of Kooijman's book (ISBN 9780521131919), which was not read and is not "
       "anchored. TODO: add Kooijman 2010 (Dynamic Energy Budget Theory for Metabolic Organisation, 3rd ed., CUP) as the "
       "progenitor anchor once it has been read (owner decision 2026-10-18).", role="comprehensive_survey")
anchor("BIO15", "doi", "10.1111/1365-2656.12085",
       "Maino, Kearney, Nisbet & Kooijman 2014 - Reconciling theories for metabolic scaling (J. Anim. Ecol. 83:20-29)",
       "cites",
       "Published abstract read 2026-10-18; full text of a July 2012 manuscript (bio.vu.nl/thb/research/bib/MainKear2013.pdf) read - not the "
       "version of record. Equations and quotes in BIO15 are from the manuscript.", confidence="medium")
tag("BIO15", "biology.physiology", "primary", "metabolic organisation and energy budgets")
tag("BIO15", "biology.ecology", "secondary", "life-history and interspecific comparisons")
LINKS += [
    ("BIO15", "C1", "predicts for", "1.5",
     "DEB: respiration mixes surface (V^2/3) and volume (V) fluxes, giving alpha in [0.66, 1] within species (Sousa et al. 2008); across "
     "species M = C0 B + C1 B^(4/3), so 3/4 only as M -> infinity (Maino et al., manuscript)."),
    ("H5", "BIO15", "couples to", "2",
     "H5's two-process identity takes a sum of two power laws as given; DEB names the processes (surface-linked assimilation, "
     "volume-linked maintenance). Ballesteros et al. 2018, H5's special case, credits DEB for the isometric + allometric sum."),
    ("BIO15", "BIO12", "tensions with", "1.5",
     "Competing explanations that reach the same finite-size equation from different assumptions (reserve dynamics vs transport network); "
     "Maino et al. conclude fits to scaling data cannot distinguish them."),
]
