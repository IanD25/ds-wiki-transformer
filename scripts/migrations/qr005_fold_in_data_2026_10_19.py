"""
Content for qr005_fold_in_2026_10_19.py (audit_ref gsw-qr005-fold-in-2026-10-19).

The experimental side of Questions Raised Log item QR-005 (is gravity quantum, or thermodynamic?):
the wiki held the thermodynamic derivations (GT01-GT07, GT10) but nothing on the tests that can
tell a quantum gravitational field from a classical or noisy one. The QR-005 literature map
(docs/prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md §G) proposed R1-R14;
this module folds in the priority six (R1-R6) as reference_law entries GT12-GT17. Mode A; no
conjectures, no Q-entries, no promotions, no calibration rows.

Reading rule (EWS / QR-004 precedent): each statement is limited to what was actually read.
Reading level per source is in each anchor's note: "this session" = read by the fold-in session
(PDF text extraction, passages located and read; or the arXiv/Crossref abstract); "QR-005 map
sub-agent" = reported by a sub-agent of the map session, not re-read here. Every DOI was checked on
Crossref on 2026-10-19.
"""

AUD = "gsw-qr005-fold-in-2026-10-19"
MAP = "docs/prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md"


def facets(cc, tags, archetype, dsens="D-sensitive"):
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
    TAGS.append((entry_id, path, primacy, confidence, f"QR-005 fold-in ({AUD}): {rationale}"))


DIM = ("Dimensional sensitivity: D-sensitive — the results are stated for Newtonian gravity in three spatial "
       "dimensions (the 1/r potential). This is the physical dimension of space, not the DS-internal Ω_D posit.")
SEEN = " Read by this session 2026-10-19"
CR = " DOI verified on Crossref 2026-10-19."

# ===========================================================================
# GT12 — Gravitationally mediated entanglement (BMV) and what it would show  [map R1]
# ===========================================================================
_t = ["gravitationally mediated entanglement", "BMV experiment", "entanglement witness", "LOCC",
      "local classical channel", "spin entanglement witness", "Feynman 1957 thought experiment",
      "quantum nature of gravity", "graviton inference", "mediator locality", "microdiamond interferometry",
      "tabletop quantum gravity"]
ENTRIES.append(dict(
    id="GT12", title="GT12: Gravitationally Mediated Entanglement (BMV) — What a Positive Witness Would Show",
    filename="GT12_gravitationally_mediated_entanglement.md",
    scale="quantum", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "If two masses, each held in a superposition of two places, become entangled through their gravitational "
         "interaction alone, then gravity is not acting as a local classical channel. The argument rests on a "
         "theorem of quantum information theory: local operations and classical communication (LOCC) cannot create "
         "entanglement. Bose et al. 2017 and Marletto & Vedral 2017 proposed the test, which revives Feynman's 1957 "
         "thought experiment. In the Bose et al. design, two microdiamonds of ~10⁻¹⁴ kg carry embedded spins that "
         "tag which of two positions, ~250 μm apart, each occupies. The diamonds fall side by side for τ ~ 2.5 s; the "
         "Newtonian interaction gives each pair of branches a different phase; the spins are then read out. The "
         "stated requirements against decoherence are a pressure of 10⁻¹⁵ Pa and an internal temperature of "
         "~0.15 K.\n\n"
         "What a positive result would show is debated.\n"
         "- **Agreed:** it rules out gravity as an LOCC channel. That covers pairwise classical channels (GT13), "
         "mean-field gravity (GT16) and Oppenheim's classical–quantum gravity (GT14, which Oppenheim et al. 2023 "
         "and Kryhin & Sudhir 2025 describe as non-entangling).\n"
         "- **Not settled:** whether it shows the field has quantum degrees of freedom, or that gravitons exist. "
         "Carney 2022: assuming unitarity and Lorentz invariance of the S-matrix, 'Newtonian entanglement' requires "
         "massless bosons universally coupled to mass, which could be spin-2 gravitons or, in principle, spin-0. "
         "Danielson, Satishchandran & Wald 2022: if a body's Newtonian field can mediate entanglement, the body can "
         "also entangle with on-shell gravitons. Galley, Giacomini & Selby 2022 prove a no-go theorem within "
         "generalised probabilistic theories, given their premises. Against: Fragkos, Kopp & Pikovski 2022 show the "
         "entanglement can equally be described by non-local processes, so 'it is not possible to draw conclusions "
         "about mediators'; Martín-Martínez & Perche 2023 show how it could be accounted for without quantum degrees "
         "of freedom of the gravitational field; Huggett, Linnemann & Schneider 2022 call the witness claim "
         "'equivocal'.\n"
         "- **Classical models that entangle:** Trillo & Navascués 2025 show that Diósi–Penrose dynamics (GT15) can "
         "entangle two masses closer than a critical distance, so a positive witness alone 'is not enough to "
         "validate quantum gravity'. Aziz & Howl 2025 (Nature) argue that classical gravity can transmit quantum "
         "information to quantum-field matter through local processes; several 2025–26 rebuttals dispute this "
         "(QR-005 map list; not read here).\n\n"
         "No such experiment has been done. The QR-005 map estimates the shortfalls at ~7.5 orders of magnitude in "
         "superposed mass and ~10 in the smallest source mass whose gravity has been measured (map §C)."),
        ("Mathematical Form",
         "Branch phases (Bose et al. 2017, Eq. 2), separation d, superposition size Δx, time τ:\n"
         "  φ ~ Gm₁m₂τ/ħd,   φ_RL ~ Gm₁m₂τ/ħ(d − Δx),   φ_LR ~ Gm₁m₂τ/ħ(d + Δx)\n"
         "  |Ψ(τ)⟩ ∝ |L⟩₁(|L⟩₂ + e^{iΔφ_LR}|R⟩₂) + |R⟩₁(e^{iΔφ_RL}|L⟩₂ + |R⟩₂),   Δφ_ij = φ_ij − φ\n"
         "  entangled unless the relative phases factorise\n\n"
         "Witness (spins read out after the interferometer closes):\n"
         "  W = |⟨σ_x⁽¹⁾ ⊗ σ_z⁽²⁾⟩ − ⟨σ_y⁽¹⁾ ⊗ σ_z⁽²⁾⟩| > 1  ⇒  entangled\n\n"
         "LOCC theorem: no entanglement measure increases under local operations and classical communication."),
        ("Constraint Category",
         "Informatic (In): a constraint on what kind of channel gravity can be. Because LOCC cannot create "
         "entanglement, an observed gravity-only entanglement forbids every account in which gravity acts as a "
         "local classical channel. It does not by itself fix the field's quantum degrees of freedom; that step needs "
         "further assumptions (locality of the mediator, or unitarity and Lorentz invariance)."),
        ("DS Cross-References",
         "GT13 (the pairwise classical channel, already excluded). GT14 (Oppenheim's classical–quantum gravity: "
         "non-entangling, so a positive witness would rule it out). GT15 (Diósi–Penrose collapse, which can entangle "
         "at short range). GT16 (mean-field semiclassical gravity, which cannot entangle). GT17 (the noise route: a "
         "test equivalent to the witness that needs no entanglement). GT01, GT10 (thermodynamic derivations of the "
         "field equations, which are silent on whether the field can carry quantum information). CM2 (the Newtonian "
         "potential that sets the phases). IT02 (entanglement of a pure state is the von Neumann entropy of a "
         "reduced state)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "The test is a yes/no decision: a witness crossing its separable-state threshold (W > 1) certifies "
         "entanglement. The physics behind it is a no-go theorem (LOCC cannot create entanglement); "
         "threshold-transition is the nearest archetype in the wiki's list.\n\n" + DIM),
        ("What The Math Says",
         "Put each of two tiny masses in two places at once, side by side. There are four combinations of where the "
         "two masses are, and in each the masses are a slightly different distance apart, so gravity gives each "
         "combination a slightly different phase. If gravity can do that coherently, the four combinations end up "
         "in a joint state that cannot be split into 'state of mass 1' times 'state of mass 2': the masses are "
         "entangled. Spins inside the masses record which branch each took, and comparing spin measurements on the "
         "two masses shows whether they became entangled. A go-between that can only pass classical messages can "
         "never do this, so a positive result would rule out gravity as such a go-between. Whether it would also "
         "prove gravitons is a separate argument that needs extra assumptions."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "threshold-transition"),
))
anchor("GT12", "10.1103/PhysRevLett.119.240401", "Bose et al. 2017 - Spin Entanglement Witness for Quantum Gravity (PRL 119:240401; arXiv:1707.06050)",
       "canonical_authority",
       "Progenitor of the experiment." + SEEN + " (arXiv v1 full text, passages): m ~ 10⁻¹⁴ kg; Δx ~ 250 μm; τ ~ 2.5 s; "
       "P = 10⁻¹⁵ Pa and 0.15 K; branch phases (Eq. 2); witness W = |⟨σx⊗σz⟩ − ⟨σy⊗σz⟩| > 1." + CR,
       role="progenitor")
anchor("GT12", "10.1103/PhysRevLett.119.240402", "Marletto & Vedral 2017 - Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity (PRL 119:240402; arXiv:1707.06036)",
       "canonical_authority",
       "Co-progenitor: the information-theoretic argument that any system mediating entanglement must be quantum."
       + SEEN + " (abstract)." + CR, role="progenitor")
anchor("GT12", "10.1103/RevModPhys.97.015003", "Bose et al. 2025 - Massive quantum systems as interfaces of quantum mechanics and gravity (Rev. Mod. Phys. 97:015003; arXiv:2311.09218)",
       "canonical_authority",
       "The main current review. Metadata only (Crossref, arXiv); abstract read by a QR-005 map sub-agent; not read "
       "by this session." + CR, role="comprehensive_survey", confidence="medium")
anchor("GT12", "10.1103/PhysRevD.105.024029", "Carney 2022 - Newton, entanglement, and the graviton (PRD 105:024029; arXiv:2108.06320)",
       "cites", "Assuming S-matrix unitarity and Lorentz invariance, Newtonian entanglement requires massless bosons "
       "universally coupled to mass (spin 2 or, in principle, spin 0)." + SEEN + " (abstract)." + CR)
anchor("GT12", "10.1103/PhysRevD.105.086001", "Danielson, Satishchandran & Wald 2022 - Gravitationally mediated entanglement: Newtonian field versus gravitons (PRD 105:086001; arXiv:2112.10798)",
       "cites", "If the Newtonian field of a body can mediate entanglement, the body can also entangle with on-shell "
       "gravitons; no clear distinction between the two under the gedankenexperiment's protocols." + SEEN +
       " (abstract)." + CR)
anchor("GT12", "10.22331/q-2022-08-17-779", "Galley, Giacomini & Selby 2022 - A no-go theorem on the nature of the gravitational field beyond quantum theory (Quantum 6:779; arXiv:2012.01441)",
       "cites", "No-go theorem in the generalised-probabilistic-theories framework, given its premises (gravity "
       "mediates entanglement, among others)." + SEEN + " (abstract, partly)." + CR, confidence="medium")
anchor("GT12", "10.1116/5.0101334", "Fragkos, Kopp & Pikovski 2022 - On inference of quantization from gravitationally induced entanglement (AVS Quantum Sci. 4:045601; arXiv:2206.00558)",
       "open_in_literature", "Frames the inference as ambiguous: entanglement generation can equally be described by "
       "mediators or by non-local processes; 'not possible to draw conclusions about mediators'." + SEEN +
       " (abstract)." + CR)
anchor("GT12", "2205.09013", "Huggett, Linnemann & Schneider 2022 - Quantum Gravity in a Laboratory? (arXiv:2205.09013)",
       "open_in_literature", "Philosophy of physics: the positive claim of witness is 'equivocal'." + SEEN +
       " (arXiv abstract). Preprint; journal version not checked.", tier=3, stability="preprint-evolving",
       source="arxiv", confidence="medium")
anchor("GT12", "10.1103/PhysRevD.108.L101702", "Martín-Martínez & Perche 2023 - What gravity mediated entanglement can really tell us about quantum gravity (PRD 108:L101702; arXiv:2208.09489)",
       "cites", "Shows how BMV entanglement could be accounted for without quantum degrees of freedom of the "
       "gravitational field, and what assumptions are needed to read it as proof of quantum gravity." + SEEN +
       " (abstract)." + CR)
anchor("GT12", "10.1103/PhysRevLett.130.100202", "Christodoulou et al. 2023 - Locally mediated entanglement in linearized quantum gravity (PRL 130:100202; arXiv:2202.03368)",
       "cites", "Treats the effect in linearised quantum gravity with local mediation (the map reports a delayed "
       "entanglement signal as the sharp test)." + SEEN + " (abstract opening only)." + CR, confidence="medium")
anchor("GT12", "10.1103/PhysRevD.111.L121101", "Trillo & Navascués 2025 - Diósi-Penrose model of classical gravity predicts gravitationally induced entanglement (PRD 111:L121101; arXiv:2411.02287)",
       "cites", "DP dynamics can entangle two particles iff closer than a critical distance d_c ∝ the model's free "
       "parameter; 'GIE detection is not enough to validate quantum gravity'." + SEEN + " (abstract)." + CR)
anchor("GT12", "10.1038/s41586-025-09595-7", "Aziz & Howl 2025 - Classical theories of gravity produce entanglement (Nature 646:813; arXiv:2510.19714)",
       "cites", "Claims classical gravity coupled to quantum-field matter can generate entanglement through local "
       "processes. Contested: the QR-005 map lists at least seven 2025-26 rebuttals (not read here)." + SEEN +
       " (abstract)." + CR, confidence="medium")
tag("GT12", "physics.modern.quantum_mechanics", "primary", "entanglement of massive superpositions")
tag("GT12", "information_theory.quantum_info", "secondary", "LOCC cannot create entanglement")
tag("GT12", "physics.cosmology", "secondary", "the quantum nature of gravity (GT-series convention)")
LINKS += [
    ("GT12", "CM2", "tests", "1", "The branch phases are set by the Newtonian potential Gm₁m₂/d between the branches."),
    ("GT12", "IT02", "derives from", "1", "Entanglement of a pure two-body state is the von Neumann entropy of either "
     "reduced state; the witness certifies that it is non-zero."),
    ("GT12", "GT01", "disambiguates from", "1", "A thermodynamic derivation of Einstein's equation is silent on whether "
     "the field can carry quantum information; the entanglement test is what could tell."),
    ("GT12", "GT10", "disambiguates from", "1", "Jacobson 2016 is semiclassical and takes no position on gravitons; it "
     "makes no prediction for the entanglement test."),
    ("GT12", "GT13", "generalizes", "1", "A positive witness would rule out every LOCC account of gravity, not only "
     "the pairwise channel already excluded."),
    ("GT12", "GT14", "tests", "1", "Oppenheim's classical-quantum gravity is described as non-entangling, so a "
     "positive witness would rule it out."),
    ("GT12", "GT16", "tests", "1", "Mean-field (Schrödinger-Newton) gravity cannot entangle two masses."),
    ("GT12", "GT15", "tensions with", "1", "Diósi-Penrose dynamics can entangle masses closer than a critical "
     "distance (Trillo & Navascués 2025), so a positive witness alone does not establish quantum gravity."),
]

# ===========================================================================
# GT13 — Gravity is not a pairwise local classical channel  [map R2]
# ===========================================================================
_t = ["classical channel gravity", "Kafri-Taylor-Milburn model", "gravitational decoherence",
      "continuous measurement and feedback", "atom interferometry", "minimum decoherence rate",
      "non-entangling gravity", "Newtonian force from classical information"]
ENTRIES.append(dict(
    id="GT13", title="GT13: Gravity Is Not a Pairwise Local Classical Channel (Kafri–Taylor–Milburn; Altamirano et al. 2018)",
    filename="GT13_not_pairwise_classical_channel.md",
    scale="quantum", domain="physics · information", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Kafri, Taylor & Milburn 2014 modelled the gravitational interaction between two masses as a classical "
         "measurement channel: each mass's position is continuously measured and the result is fed back as a force. "
         "The model reproduces the Newtonian force on average, cannot create entanglement, and forces a minimum "
         "decoherence (and heating) rate of the order of the gravitationally induced coupling.\n\n"
         "Altamirano, Corona-Ugalde, Mann & Zych 2018 applied the model pairwise between each atom in an "
         "interferometer and the Earth. Existing single-atom interference with large spatial superpositions "
         "(for example a 10 m rubidium fountain with 0.54 m separation) shows visibilities larger than the model "
         "allows, by factors from ~2.5 to ~10¹⁸ across the experiments, even if the predicted rate is cut tenfold "
         "(their C = 0.1) to allow for corrections to the path separation. So if gravity reduces to pairwise Newtonian interactions at low energy, "
         "that interaction cannot come from exchanging classical information alone.\n\n"
         "SCOPE: this excludes the *pairwise local* classical-channel framework. It does not exclude gravity-related "
         "collapse (GT15), which the same experiments do not constrain, nor non-pairwise classical models such as "
         "Oppenheim's (GT14)."),
        ("Mathematical Form",
         "KTM channel: weak continuous measurement of each position + classical feedback force\n"
         "  ⇒ mean force = Newtonian; entangling power = 0\n"
         "  ⇒ decoherence rate Γ_KTM ≥ Γ_min ~ gravitationally induced coupling (same order as the normal-mode splitting)\n"
         "Test (Altamirano et al. 2018), schematically: predicted visibility V_KTM ~ exp(−Γ_min τ) vs measured V_obs;\n"
         "  V_obs / V_KTM ≈ 2.5 … 10¹⁸ across interferometry experiments  ⇒  pairwise classical channel excluded"),
        ("Constraint Category",
         "Informatic (In): the excluded hypothesis is information-theoretic — that the Newtonian interaction conveys "
         "only classical information between pairs of masses. The data exclude it through its required minimum "
         "decoherence, not through any statement about gravitons."),
        ("DS Cross-References",
         "GT12 (the entanglement witness would exclude every LOCC model, not only this one). GT15 (Diósi–Penrose "
         "collapse is not constrained by these experiments). GT17 (minimum-noise theorems for non-entangling "
         "gravity generalise the KTM idea; Kafri & Taylor 2013 is by two of the same authors). CM2 (the Newtonian "
         "force the channel reproduces on average)."),
        ("Mathematical Archetype",
         "Mathematical archetype: exponential-decay\n\n"
         "A classical channel forces interference visibility to decay at a minimum rate; the test compares that "
         "minimum decay with the visibilities actually measured.\n\n" + DIM),
        ("What The Math Says",
         "Suppose gravity worked like a pair of observers who keep measuring where each mass is and then push the "
         "other mass accordingly. On average that reproduces Newton's attraction. But measuring a mass's position "
         "destroys its quantum interference, so such gravity would wash out the interference of any atom held in "
         "two places at once, at a minimum rate set by the strength of gravity. Atom interferometers have kept atoms "
         "in two places half a metre apart with much more interference than this model allows. So gravity between "
         "pairs of particles is not this kind of classical measure-and-push channel."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "exponential-decay"),
))
anchor("GT13", "10.1088/1361-6382/aac72f", "Altamirano, Corona-Ugalde, Mann & Zych 2018 - Gravity is not a pairwise local classical channel (CQG 35:145005; arXiv:1612.07735)",
       "canonical_authority",
       "Progenitor of the exclusion." + SEEN + " (arXiv v2: abstract, Table I, Sec. II–III passages): visibilities "
       "exceed the KTM prediction by ~2.5 to ~10¹⁸ even with the rate cut tenfold (C = 0.1); the experiments do not "
       "constrain the Diósi–Penrose model." + CR, role="progenitor")
anchor("GT13", "10.1088/1367-2630/16/6/065020", "Kafri, Taylor & Milburn 2014 - A classical channel model for gravitational decoherence (NJP 16:065020; arXiv:1401.0946)",
       "cites", "The model: gravity as a classical measurement channel; equivalent to a Diósi model; cannot create "
       "entanglement; decoherence rate of the order of the gravitational normal-mode splitting." + SEEN +
       " (abstract)." + CR)
tag("GT13", "physics.modern.quantum_mechanics", "primary", "atom-interferometry decoherence bound")
tag("GT13", "information_theory.quantum_info", "secondary", "classical channels cannot entangle")
tag("GT13", "physics.cosmology", "secondary", "gravity (GT-series convention)")
LINKS += [
    ("GT13", "CM2", "tests", "1", "The KTM channel reproduces Newton's attraction on average; atom interferometry "
     "excludes the minimum decoherence it would bring."),
    ("GT13", "GT15", "disambiguates from", "1", "The experiments that exclude the pairwise classical channel do not "
     "constrain Diósi-Penrose collapse (Altamirano et al. 2018)."),
]

# ===========================================================================
# GT14 — Classical-quantum (postquantum) gravity and the trade-off  [map R3]
# ===========================================================================
_t = ["classical-quantum gravity", "postquantum classical gravity", "Oppenheim", "decoherence-diffusion trade-off",
      "spacetime diffusion", "D2 diffusion coefficient", "stochastic metric", "completely positive hybrid dynamics",
      "torsion balance bound", "matter-wave interferometry bound", "non-entangling gravity"]
ENTRIES.append(dict(
    id="GT14", title="GT14: Classical–Quantum (Postquantum) Gravity and the Decoherence–Diffusion Trade-off (Oppenheim)",
    filename="GT14_classical_quantum_gravity.md",
    scale="quantum", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Oppenheim 2023 (PRX) constructs a theory in which spacetime stays classical while matter is quantum. The "
         "coupling is linear in the density matrix, completely positive and trace-preserving, and reduces to general "
         "relativity in the classical limit, so it avoids the pathologies of the expectation-value semiclassical "
         "theory (GT16). The price is that the theory must be fundamentally stochastic: both the metric and the "
         "quantum matter diffuse.\n\n"
         "Oppenheim, Sparaciari, Šoda & Weller-Davies 2023 (Nat. Commun.) prove that this is generic for any such "
         "classical–quantum dynamics: the decoherence it induces on quantum matter (rate set by D₀) and the "
         "diffusion of the classical field (coefficient D₂) obey a trade-off, roughly D₂ ≳ (coupling)²/D₀. Less "
         "decoherence forces more diffusion, so the theory is squeezed from both sides: precision mass and "
         "acceleration measurements bound D₂ from above, and coherence times in matter-wave interferometry bound it "
         "from below.\n\n"
         "**The windows** (S5 reconciled 2026-10-19 against the published texts):\n"
         "- Ultra-local continuous kernel ('noise everywhere'): **excluded** (torsion balances give D₂ ≤ 10⁻⁴¹; "
         "interferometry needs D₂ ≥ 10⁻⁹ kg² s m⁻³ in the published version, 10⁻²⁴ in arXiv v1).\n"
         "- Ultra-local discrete kernel: 10⁻¹ ≥ (l_P³/m_P)D₂ ≥ 10⁻²⁵ in the original (24 orders open). With "
         "Janse et al. 2024's review of modern force-noise experiments on Earth, the upper bound falls to 10⁻¹⁶, "
         "leaving **~9 orders**.\n"
         "- Non-local kernel (Diósi–Penrose form, GT15): 10⁻⁹ ≥ l_P²D₂ ≥ 10⁻³⁵ kg² s m⁻¹ in the published version "
         "(26 orders; arXiv v1 had 10⁻⁴⁰ and 31 orders). Janse et al. lower the upper bound to 10⁻²⁴, leaving "
         "**~11 orders**.\n"
         "- Janse et al. note that atom interferometry would push the discrete model's upper bound below its lower "
         "bound, and LISA Pathfinder would gain ~19 orders, but they are 'unsure' whether those experiments apply. "
         "Their text quotes '26 and 24 orders' remaining with the two model labels swapped relative to the "
         "published Oppenheim et al. figures.\n\n"
         "Oppenheim et al. and Kryhin & Sudhir 2025 describe the gravitational fluctuations as able to mediate "
         "classical correlations but not entanglement, so a positive entanglement witness (GT12) would rule the "
         "theory out. The QR-005 map flags that some Markovian hybrid models can entangle (Angeli & Carlesso 2025; "
         "not read here), so this should be checked kernel by kernel."),
        ("Mathematical Form",
         "Decoherence–diffusion trade-off (Oppenheim et al. 2023): positivity of the classical–quantum dynamics "
         "requires\n  2D₂ ⪰ D₁ D₀⁻¹ D₁ᵀ   (roughly D₂ ≳ coupling² / D₀)\n\n"
         "Experimental squeeze (published Nat. Commun. figures; N_λ, M_λ, V_λ from fullerene interferometry):\n"
         "  ultra-local continuous:  10⁻⁴¹ ≥ D₂ ≥ 10⁻⁹ kg² s m⁻³          → excluded\n"
         "  ultra-local discrete:    10⁻¹ ≥ (l_P³/m_P) D₂ ≥ 10⁻²⁵            → 24 orders open\n"
         "  non-local (DP kernel):   10⁻⁹ ≥ l_P² D₂ ≥ 10⁻³⁵ kg² s m⁻¹       → 26 orders open\n"
         "Janse et al. 2024 (direct acceleration-noise data on Earth only):\n"
         "  10⁻¹⁶ ≥ (l_P³/m_P) D₂ ≥ 10⁻²⁵   (~9 orders);   10⁻²⁴ ≥ l_P² D₂ ≥ 10⁻³⁵   (~11 orders)"),
        ("Constraint Category",
         "Informatic-Geometric (In-Gm): a positivity (complete-positivity) constraint on how a classical geometry "
         "can couple to quantum matter. It ties an information-theoretic quantity (decoherence of matter) to a "
         "geometric one (diffusion of the metric). That makes classical gravity testable without the entanglement "
         "experiment."),
        ("DS Cross-References",
         "GT16 (expectation-value semiclassical gravity, whose pathologies this theory avoids). GT15 (the non-local "
         "kernel that saturates the trade-off has the Diósi–Penrose form). GT12 (a positive entanglement witness "
         "would rule the theory out). GT17 (minimum-noise thresholds; Fabiano et al. 2026 test their general "
         "threshold on these models). GV1 (the theory reduces to general relativity in the classical limit)."),
        ("Mathematical Archetype",
         "Mathematical archetype: diffusion-equation\n\n"
         "The classical field obeys stochastic (diffusive) dynamics whose diffusion coefficient D₂ is bounded below "
         "by the inverse of the decoherence coefficient. Experiments bound D₂ from both sides.\n\n" + DIM),
        ("What The Math Says",
         "Suppose spacetime really is classical and only matter is quantum. For the two to interact consistently, "
         "gravity has to 'look' at matter, and looking destroys quantum superpositions, so matter decoheres. The "
         "theorem says that the less matter decoheres, the more the gravitational field must jitter randomly. So "
         "experiments can corner the idea from both sides: long-lived superpositions in interferometers demand a lot "
         "of jitter, while precise weighing experiments show there is not much jitter. One version of the theory "
         "(jitter everywhere) is already ruled out; two others survive in windows of roughly 9 and 11 orders of "
         "magnitude if only the most direct experiments are counted."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In-Gm", _t, "diffusion-equation"),
))
anchor("GT14", "10.1103/PhysRevX.13.041040", "Oppenheim 2023 - A Postquantum Theory of Classical Gravity? (PRX 13:041040; arXiv:1811.03116)",
       "canonical_authority",
       "Progenitor: classical gravity coupled to quantum fields, linear in the density matrix, completely positive, "
       "reducing to GR; fundamentally stochastic." + SEEN + " (arXiv v3 abstract)." + CR, role="progenitor")
anchor("GT14", "10.1038/s41467-023-43348-2", "Oppenheim, Sparaciari, Šoda & Weller-Davies 2023 - Gravitationally induced decoherence vs space-time diffusion: testing the quantum nature of gravity (Nat. Commun. 14:7910; arXiv:2203.01982)",
       "canonical_authority",
       "The trade-off theorem and the experimental squeeze." + SEEN + ": published version (nature.com, open access) "
       "for Eqs. 44–47 and the bounds, and arXiv v1 full text. The published lower bounds differ from v1 (V_λ ~ "
       "10⁻³⁷ m³ and N_λ; continuous D₂ ≥ 10⁻⁹, non-local l_P²D₂ ≥ 10⁻³⁵); the discrete window is unchanged."
       + CR, role="progenitor")
anchor("GT14", "10.1103/PhysRevResearch.6.033076", "Janse et al. 2024 - Current experimental upper bounds on spacetime diffusion (PRR 6:033076; arXiv:2403.08912)",
       "cites",
       "Upper bounds ≥ 15 orders lower than Oppenheim et al.'s; conservative windows 10⁻¹⁶ ≥ (l_P³/m_P)D₂ ≥ 10⁻²⁵ and "
       "10⁻²⁴ ≥ l_P²D₂ ≥ 10⁻³⁵; atom interferometry and LISA Pathfinder would go further, but the authors are "
       "unsure they apply." + SEEN + " (arXiv v1 full text; published abstract identical)." + CR)
anchor("GT14", "10.22331/q-2024-12-16-1565", "Layton, Oppenheim & Weller-Davies 2024 - A healthier semi-classical dynamics (Quantum 8:1565; arXiv:2208.11722)",
       "cites", "Linear, completely positive classical–quantum dynamics is forced to be stochastic when back-reaction "
       "is non-zero; avoids the pathologies of expectation-value laws." + SEEN + " (abstract)." + CR)
anchor("GT14", "10.1103/PhysRevLett.134.061501", "Kryhin & Sudhir 2025 - Distinguishable consequence of classical gravity on quantum matter (PRL 134:061501; arXiv:2309.09105)",
       "cites", "Classical gravity must fluctuate; fluctuations mediate classical correlations but not entanglement; "
       "a characteristic phase response in cross-correlations distinguishes it." + SEEN + " (abstract)." + CR)
tag("GT14", "physics.modern.quantum_mechanics", "primary", "hybrid classical–quantum dynamics")
tag("GT14", "physics.cosmology", "secondary", "classical spacetime (GT-series convention)")
tag("GT14", "statistics_probability.stochastic_processes", "secondary", "stochastic metric diffusion")
LINKS += [
    ("GT14", "GV1", "generalizes", "1", "Classical-quantum gravity reduces to general relativity in the classical "
     "limit while adding a stochastic (diffusive) metric."),
    ("GT14", "GT16", "tensions with", "1", "Linear, completely positive classical-quantum coupling avoids the "
     "pathologies of expectation-value (mean-field) semiclassical gravity."),
    ("GT14", "GT15", "couples to", "1", "The non-local kernel saturating the decoherence-diffusion trade-off has the "
     "Diósi-Penrose form (Oppenheim et al. 2023)."),
]

# ===========================================================================
# GT15 — Diósi–Penrose collapse and underground bounds  [map R4]
# ===========================================================================
_t = ["Diósi-Penrose model", "gravity-related collapse", "objective reduction", "spontaneous radiation",
      "underground X-ray search", "R0 cut-off", "germanium detector", "XENONnT", "Majorana Demonstrator",
      "collapse models"]
ENTRIES.append(dict(
    id="GT15", title="GT15: Diósi–Penrose Gravity-Related Collapse and Its Underground Bounds",
    filename="GT15_diosi_penrose_collapse.md",
    scale="quantum", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Diósi (1987, 1989) and Penrose (1996) proposed that a superposition of different mass distributions "
         "collapses on its own, at a rate set by the gravitational self-energy of the difference between the "
         "branches: roughly one over ħ divided by that energy. The collapse is random, so it also shakes the "
         "particles. Charged particles that are shaken radiate, so the model predicts a faint, spontaneous X-ray "
         "glow from ordinary matter. A cut-off length R₀ (the effective size of each nucleus's mass distribution) "
         "is needed to keep the rate finite.\n\n"
         "Underground searches find no such glow:\n"
         "- Donadi et al. 2021 (Gran Sasso, germanium): R₀ > 0.54 × 10⁻¹⁰ m with probability 0.95. Penrose's natural "
         "value for germanium is 0.05 × 10⁻¹⁰ m, so **the parameter-free version is ruled out**.\n"
         "- Majorana Demonstrator (Arnquist et al. 2022; revised arXiv v5, 2023): R₀ > 2.54 × 10⁻¹⁰ m at 95% CL.\n"
         "- XENONnT (Aprile et al. 2026): R₀ > 4.9 × 10⁻¹⁰ m at 90% CL, > 4.5 × 10⁻¹⁰ m at 95% CL, about five times "
         "the Majorana limit.\n\n"
         "These bounds apply to the Markovian (white-noise) model; dissipative and coloured-noise variants evade "
         "them (QR-005 map). Trillo & Navascués 2025 show that DP dynamics can entangle two masses closer than a "
         "critical distance proportional to the free parameter, so the model also makes a prediction for the "
         "entanglement test (GT12)."),
        ("Mathematical Form",
         "Collapse rate (Penrose estimate): τ ≈ ħ / E_Δ,   E_Δ = gravitational self-energy of the difference between "
         "the two branches' mass distributions\n"
         "Diósi master equation: dρ/dt = −(i/ħ)[H, ρ] − (G/2ħ) ∫∫ d³x d³y [μ(x), [μ(y), ρ]] / |x − y|,\n"
         "  with μ the mass-density operator smeared over R₀\n"
         "Bounds on R₀ (Markovian model):\n"
         "  Donadi 2021: R₀ > 0.54 × 10⁻¹⁰ m (p = 0.95)   vs Penrose's 0.05 × 10⁻¹⁰ m (Ge)\n"
         "  Majorana 2022/23: R₀ > 2.54 × 10⁻¹⁰ m (95% CL)\n"
         "  XENONnT 2026: R₀ > 4.9 × 10⁻¹⁰ m (90% CL); > 4.5 × 10⁻¹⁰ m (95% CL)"),
        ("Constraint Category",
         "Informatic-Geometric (In-Gm): a proposed link between the geometry that each branch would source and the "
         "loss of quantum coherence. Collapse destroys superpositions (informatic), at a rate set by gravitational "
         "self-energy (geometric). The radiation it predicts makes it testable without any interferometer."),
        ("DS Cross-References",
         "GT16 (Schrödinger–Newton gravity has the same Diósi–Penrose roots, but does not describe collapse; "
         "Bahrami et al. 2014). GT14 (the Diósi–Penrose form is the non-local kernel saturating Oppenheim's "
         "trade-off). GT12 (DP can entangle at short range). GT13 (the classical-channel exclusions do not constrain "
         "DP). QM1 (collapse modifies Schrödinger evolution). CM2 (the Newtonian self-energy that sets the rate)."),
        ("Mathematical Archetype",
         "Mathematical archetype: exponential-decay\n\n"
         "Superpositions of different mass distributions lose coherence at a rate E_Δ/ħ; the accompanying random "
         "kicks produce a radiation rate that underground detectors bound.\n\n" + DIM),
        ("What The Math Says",
         "Penrose's idea: if a lump of matter is in two places at once, spacetime would have to be bent in two "
         "different ways at once, and nature does not tolerate that for long. The heavier the lump and the more "
         "different the two places, the faster the superposition snaps to one place. The snapping is random, so it "
         "jiggles charged particles, and jiggled charges emit faint X-rays. Very quiet detectors deep underground "
         "see no such X-rays, which rules out Penrose's own version of the idea. A version with an adjustable size "
         "parameter survives only if that size is at least about a hundred times Penrose's natural value."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In-Gm", _t, "exponential-decay"),
))
anchor("GT15", "10.1103/PhysRevA.40.1165", "Diósi 1989 - Models for universal reduction of macroscopic quantum fluctuations (PRA 40:1165)",
       "canonical_authority", "Progenitor (the master equation). Not read by this session; the QR-005 map lists it "
       "as a core source." + CR, role="progenitor", stability="canonical", confidence="medium")
anchor("GT15", "10.1007/BF02105068", "Penrose 1996 - On Gravity's role in Quantum State Reduction (GRG 28:581)",
       "canonical_authority", "Progenitor (gravity-related reduction, τ ≈ ħ/E_Δ). Not read by this session." + CR,
       role="progenitor", stability="canonical", confidence="medium")
anchor("GT15", "10.1038/s41567-020-1008-4", "Donadi et al. 2021 - Underground test of gravity-related wave function collapse (Nat. Phys. 17:74; arXiv:2111.13490)",
       "cites", "R₀ > 0.54 × 10⁻¹⁰ m (probability 0.95) vs Penrose's 0.05 × 10⁻¹⁰ m for Ge; 'rules out the natural "
       "parameter-free version'." + SEEN + " (full text, results and Fig. 5)." + CR)
anchor("GT15", "10.1103/PhysRevLett.129.080401", "Arnquist et al. (Majorana) 2022 - Search for Spontaneous Radiation from Wave Function Collapse in the Majorana Demonstrator (PRL 129:080401; arXiv:2202.01343)",
       "cites", "R_DP > (2.54 ± 0.03) × 10⁻¹⁰ m at 95% CL, from arXiv v5 (June 2023), which post-dates the published "
       "erratum (PRL 130:239902, per the QR-005 map; erratum not read)." + SEEN + " (arXiv v5 text)." + CR)
anchor("GT15", "10.1103/2jm3-4976", "Aprile et al. (XENONnT) 2026 - Challenging Spontaneous Quantum Collapse with the XENONnT Dark Matter Detector (PRL 136:120201; arXiv:2506.05507)",
       "cites", "R₀ > 4.9 × 10⁻¹⁰ m (90% CL), 4.5 × 10⁻¹⁰ m (95% CL); ~5× the Majorana limit; also first exclusion of "
       "the GRW values in CSL." + SEEN + " (arXiv v2 full text, results)." + CR)
anchor("GT15", "10.1103/PhysRevD.111.L121101", "Trillo & Navascués 2025 - Diósi-Penrose model of classical gravity predicts gravitationally induced entanglement (PRD 111:L121101; arXiv:2411.02287)",
       "cites", "DP can entangle two particles iff closer than d_c ∝ its free parameter." + SEEN + " (abstract)." + CR)
tag("GT15", "physics.modern.quantum_mechanics", "primary", "collapse models")
tag("GT15", "physics.cosmology", "secondary", "gravity-related reduction (GT-series convention)")
LINKS += [
    ("GT15", "QM1", "tensions with", "1", "Gravity-related collapse adds a non-unitary, stochastic term to "
     "Schrödinger evolution."),
    ("GT15", "CM2", "derives from", "1", "The collapse rate is set by the Newtonian gravitational self-energy of the "
     "difference between the branches' mass distributions."),
    ("GT15", "GT16", "couples to", "1", "Same Diósi-Penrose roots; Bahrami et al. 2014 show the Schrödinger-Newton "
     "equation itself does not describe collapse."),
]

# ===========================================================================
# GT16 — Fundamentally semiclassical (Schrödinger–Newton) gravity  [map R5]
# ===========================================================================
_t = ["semiclassical gravity", "Schrödinger-Newton equation", "Møller-Rosenfeld equation", "mean-field gravity",
      "superluminal signalling", "Page-Geilker experiment", "nonlinear Schrödinger equation",
      "Tilloy-Diósi model", "optomechanical test"]
ENTRIES.append(dict(
    id="GT16", title="GT16: Fundamentally Semiclassical (Schrödinger–Newton) Gravity",
    filename="GT16_semiclassical_schrodinger_newton.md",
    scale="quantum", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "If gravity is fundamentally classical and is sourced by the *expectation value* of quantum matter "
         "(G_ab = 8πG⟨T_ab⟩), then in the weak-field, non-relativistic limit the Schrödinger equation picks up a "
         "nonlinear, non-local self-gravity term: the Schrödinger–Newton equation (Diósi 1984; Penrose 1996). With "
         "quantized gravity the Schrödinger equation stays linear (Bahrami, Großardt, Donadi & Bassi 2014).\n\n"
         "Problems and status:\n"
         "- The Schrödinger–Newton equation does not describe wave-function collapse, although it was first "
         "proposed for that purpose (Bahrami et al.).\n"
         "- Combined with the standard collapse postulate, fundamentally semiclassical gravity allows superluminal "
         "signalling; a consistent version needs a suitable prescription for collapse (Bahrami et al.). Tilloy & "
         "Diósi 2016 build one by sourcing gravity from spontaneously localised matter; it recovers the Newtonian "
         "pair potential up to a short-distance cut-off and predicts an extra gravitational decoherence term.\n"
         "- Page & Geilker 1981 is often cited as experimental evidence against semiclassical gravity. Bahrami et al. "
         "note that its 'superposition' was prepared by a classical procedure, so it tests only a no-collapse "
         "interpretation of semiclassical gravity.\n"
         "- Yang et al. 2013 predict that for a macroscopic object in a harmonic trap, the quantum uncertainty "
         "evolves at a frequency different from the classical one, observable with optomechanics; for several "
         "objects, quantum uncertainty cannot be transferred between them by gravity.\n\n"
         "So mean-field gravity is excluded on consistency grounds in its simplest form, not by experiment. It "
         "cannot entangle masses (GT12)."),
        ("Mathematical Form",
         "Semiclassical (Møller–Rosenfeld) field equation:  G_ab = 8πG ⟨ψ| T̂_ab |ψ⟩\n"
         "Newtonian limit, one particle (Schrödinger–Newton):\n"
         "  iħ ∂ψ(t,r)/∂t = [ −ħ²∇²/2m − Gm² ∫ |ψ(t,r′)|² / |r − r′| d³r′ ] ψ(t,r)\n"
         "  nonlinear and non-local in ψ (contrast: linear Schrödinger equation under quantized gravity)"),
        ("Constraint Category",
         "Informatic-Geometric (In-Gm): the classical geometry responds to the averaged quantum state, so geometric "
         "dynamics depend nonlinearly on the wave function. The nonlinearity is the source of both the predicted "
         "self-gravity effects and the consistency problems (signalling, the need for a collapse rule)."),
        ("DS Cross-References",
         "QM1 (Schrödinger equation — made nonlinear here). GV1 (the semiclassical Einstein equation with ⟨T_ab⟩ as "
         "source). GT14 (Oppenheim's classical–quantum gravity, built to avoid these pathologies). GT15 (gravity-"
         "related collapse, a candidate collapse rule). GT12 (mean-field gravity cannot entangle masses). GT10 "
         "(Jacobson 2016 also derives a semiclassical equation with ⟨T_ab⟩, as an equilibrium condition, not as a "
         "claim that gravity is fundamentally classical)."),
        ("Mathematical Archetype",
         "Mathematical archetype: coupled-field-equations\n\n"
         "The wave function sources a classical potential that in turn enters the wave function's own evolution, so "
         "the matter and gravity equations are solved together, self-consistently.\n\n" + DIM),
        ("What The Math Says",
         "Suppose gravity stays classical and simply responds to where matter is on average. A particle spread over "
         "two places would then be pulled by its own averaged mass, sitting halfway between the two places. That "
         "makes the quantum rules nonlinear: the particle's motion now depends on its own wave function. That causes "
         "trouble. Combined with the usual rule that a measurement collapses the wave function, it would let you "
         "signal faster than light. So the simplest version of 'classical gravity sourced by quantum matter' does "
         "not hold together, and consistent versions need a specific collapse rule or a stochastic coupling."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In-Gm", _t, "coupled-field-equations"),
))
anchor("GT16", "10.1088/1367-2630/16/11/115007", "Bahrami, Großardt, Donadi & Bassi 2014 - The Schrödinger–Newton equation and its foundations (NJP 16:115007; arXiv:1407.4370)",
       "canonical_authority",
       "Survey of fundamentally semiclassical gravity in the Newtonian limit: the SN equation; it does not describe "
       "collapse; with standard collapse it allows superluminal signalling; Page–Geilker tests only a no-collapse "
       "interpretation." + SEEN + " (abstract and the Page–Geilker passage)." + CR,
       role="comprehensive_survey")
anchor("GT16", "10.1103/PhysRevLett.47.979", "Page & Geilker 1981 - Indirect Evidence for Quantum Gravity (PRL 47:979)",
       "cites", "Often cited against semiclassical gravity. Not read by this session; its scope as stated by Bahrami "
       "et al. 2014." + CR, stability="canonical", confidence="medium")
anchor("GT16", "10.1103/PhysRevLett.110.170401", "Yang, Miao, Lee, Helou & Chen 2013 - Macroscopic Quantum Mechanics in a Classical Spacetime (PRL 110:170401; arXiv:1210.0457)",
       "cites", "Optomechanical signature of the many-particle SN equation; quantum uncertainty not transferable "
       "between gravitating objects." + SEEN + " (abstract)." + CR)
anchor("GT16", "10.1103/PhysRevD.93.024026", "Tilloy & Diósi 2016 - Sourcing semiclassical gravity from spontaneously localized quantum matter (PRD 93:024026; arXiv:1509.08705)",
       "cites", "A consistent stochastic semiclassical gravity in the Newtonian limit via spontaneous localisation; "
       "Newtonian pair potential up to a cut-off; extra decoherence." + SEEN + " (abstract)." + CR)
tag("GT16", "physics.modern.quantum_mechanics", "primary", "nonlinear Schrödinger–Newton dynamics")
tag("GT16", "physics.cosmology", "secondary", "semiclassical gravity (GT-series convention)")
LINKS += [
    ("GT16", "QM1", "tensions with", "1", "Sourcing gravity by ⟨T_ab⟩ makes the Schrödinger equation nonlinear "
     "(Schrödinger-Newton); with quantized gravity it stays linear."),
    ("GT16", "GV1", "derives from", "1", "The Møller-Rosenfeld semiclassical equation G_ab = 8πG⟨T_ab⟩ in the "
     "Newtonian limit."),
    ("GT16", "CM2", "derives from", "1", "The self-gravity term is the Newtonian potential of the wave function's own "
     "mass density."),
]

# ===========================================================================
# GT17 — Minimum noise of non-entangling gravity; entanglement-free tests  [map R6]
# ===========================================================================
_t = ["noise inequality", "minimum gravitational noise", "non-entangling gravity", "LOCC inequality",
      "entanglement-free test", "torsion pendulum", "force noise threshold", "LISA Pathfinder",
      "quantum nature of gravity", "Galilean invariance"]
ENTRIES.append(dict(
    id="GT17", title="GT17: Minimum Noise of Non-Entangling Gravity; Entanglement-Free Tests",
    filename="GT17_minimum_noise_nonentangling_gravity.md",
    scale="quantum", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Any gravity that cannot create entanglement must add a minimum amount of noise. So a measurement of "
         "gravitating masses that comes out quieter than that floor would show that gravity is entangling, without "
         "making or detecting entanglement.\n\n"
         "- Kafri & Taylor 2013 (preprint): if a force cannot convey entanglement, a local noise inequality holds, "
         "and noise measurements can verify entanglement generation, for example by gravity between torsional "
         "oscillators.\n"
         "- Lami, Pedernales & Plenio 2024 (PRX): an efficiently computable 'LOCC inequality' bounds how well local "
         "operations and classical communication can simulate a given evolution. Applied to harmonic oscillators in "
         "coherent states interacting by Newtonian gravity, such as torsion pendula, a violation would establish the "
         "non-classicality of gravity. The test needs neither large delocalised states nor entanglement detection.\n"
         "- Fabiano, Fujita, Matsumura & Carney 2026 (preprint): they classify all models of non-quantized gravity "
         "that are Galilean invariant, time-local and reproduce Newton's interaction on average, and show that "
         "every non-entangling one must inject a quantifiable minimum noise. For masses 1 mm apart the threshold is "
         "roughly S_aa ≈ 10⁻¹⁸ m s⁻²/√Hz, about 1000 times below the LISA Pathfinder level. They test it on "
         "Oppenheim's classical–quantum models (GT14).\n\n"
         "The QR-005 map estimates that mm-scale ground-based gravity measurements are about 10⁹ above this "
         "threshold (sub-agent readings of Westphal et al. 2021 and Fuchs et al. 2024; not checked here). The "
         "threshold's generality rests on one group's preprint so far."),
        ("Mathematical Form",
         "Non-entangling (LOCC) gravity ⇒ added force/acceleration noise ≥ S_min (model-class theorem)\n"
         "Fabiano et al. 2026: for two masses at d ≈ 1 mm,  √S_aa,min ≈ 10⁻¹⁸ m s⁻² / √Hz\n"
         "  measured noise < S_min  ⇒  gravity is entangling\n"
         "Lami et al. 2024: F_LOCC ≤ F_max (computable upper bound on the LOCC simulation fidelity of U);\n"
         "  observed fidelity > F_max  ⇒  the gravitational evolution is not LOCC"),
        ("Constraint Category",
         "Informatic (In): the entanglement-or-noise dichotomy is an information-theoretic constraint. A channel that "
         "cannot convey entanglement must leave a noise signature, so a sufficiently quiet measurement does the work "
         "of an entanglement witness."),
        ("DS Cross-References",
         "GT12 (the entanglement witness this replaces). GT13 (the classical-channel model whose minimum decoherence "
         "is the simplest case). GT14 (Oppenheim's models, on which Fabiano et al. test their threshold). GT05 "
         "(Carney et al. 2025's free-energy models predict force noise; their λ = 0 case is already excluded). CM2 "
         "(Newton's interaction, reproduced on average by every model in the class)."),
        ("Mathematical Archetype",
         "Mathematical archetype: thermodynamic-bound\n\n"
         "A floor below which no model in a stated class can go: here a floor on noise, not a thermodynamic "
         "quantity. 'thermodynamic-bound' is the nearest bound-type archetype in the wiki's list.\n\n" + DIM),
        ("What The Math Says",
         "If gravity cannot link two masses quantum mechanically, it can only pass along classical information, and "
         "doing that consistently leaves a trace: a minimum amount of random jitter in how the masses move. So "
         "instead of building the very hard two-places-at-once experiment, one could measure gravitating masses very "
         "quietly. If they jitter less than the minimum, gravity must be able to entangle. The required quietness "
         "for masses a millimetre apart is about a thousand times below what the LISA Pathfinder satellite achieved, "
         "and far below current ground-based measurements of gravity between small masses."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "thermodynamic-bound"),
))
anchor("GT17", "10.1103/PhysRevX.14.021022", "Lami, Pedernales & Plenio 2024 - Testing the Quantumness of Gravity without Entanglement (PRX 14:021022; arXiv:2302.03075)",
       "canonical_authority",
       "Progenitor of the peer-reviewed entanglement-free test: a computable LOCC inequality; coherent states of "
       "oscillators (torsion pendula); no delocalisation, no entanglement detection." + SEEN + " (abstract and "
       "introduction passages)." + CR, role="progenitor")
anchor("GT17", "1311.4558", "Kafri & Taylor 2013 - A noise inequality for classical forces (arXiv:1311.4558)",
       "cites", "Noise measurements can verify entanglement generation; applied to gravity between torsional "
       "oscillators." + SEEN + " (abstract). Preprint; no journal version found.", tier=3,
       stability="preprint-evolving", source="arxiv", confidence="medium")
anchor("GT17", "2603.26075", "Fabiano, Fujita, Matsumura & Carney 2026 - Minimal noise in non-quantized gravity (arXiv:2603.26075)",
       "cites", "Classification of Galilean-invariant, time-local, Newton-on-average non-quantized models; every "
       "non-entangling one injects a minimum noise; ~10⁻¹⁸ m s⁻²/√Hz at 1 mm, ~1000× below LISA Pathfinder." + SEEN +
       " (arXiv v2 abstract and introduction). Preprint, not peer-reviewed.", tier=3, stability="preprint-evolving",
       source="arxiv", confidence="medium")
tag("GT17", "physics.modern.quantum_mechanics", "primary", "noise floors for non-entangling interactions")
tag("GT17", "information_theory.quantum_info", "secondary", "LOCC inequalities")
tag("GT17", "physics.cosmology", "secondary", "gravity (GT-series convention)")
LINKS += [
    ("GT17", "GT05", "constrains", "1", "Carney et al. 2025's free-energy models are noisy by construction; their "
     "λ = 0 case is excluded, and the minimum-noise threshold bounds the rest of the class."),
    ("GT17", "GT14", "constrains", "1", "Fabiano et al. 2026 test their general minimum-noise threshold on "
     "Oppenheim's classical-quantum gravity models."),
    ("GT17", "GT12", "couples to", "1", "Noise below the non-entangling threshold is equivalent to demonstrating "
     "gravitational entanglement, without making or detecting it."),
    ("GT17", "GT13", "generalizes", "1", "The KTM channel's minimum decoherence is one instance of the general "
     "minimum-noise requirement for non-entangling gravity."),
]
