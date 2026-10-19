"""
QR-005 corrections — 2026-10-19 (audit_ref gsw-qr005-corrections-2026-10-19). Mode A: corrections
only, no promotions.

WHY
---
The QR-005 literature map (docs/prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md
§F) found 27 errors or needed qualifications in the wiki's gravity strand. Most share one shape: a
thermodynamic, entropic or induced derivation of gravity read as "gravity is not quantum / no
gravitons", although every such derivation uses ħ and is silent on whether the field is quantized —
new pattern tag `emergent-read-as-classical`. Seven are the existing `vocabulary-stacking-analogy`.
Three anchors were wrong (HB09 Wall 2009 DOI; two GT02 anchors crediting Dai & Stojkovic's papers to
Hossenfelder). Every item was re-checked against the live text and, for the load-bearing claims,
against primary sources read in this session (reading record and the owner's decisions:
docs/prior_art_reviews/QR005_CORRECTIONS_2026_10_19.md). The re-check found the Bianconi
misdescription (map item 16) in 10 further entries and 4 further links; they are corrected here too.

WHAT THIS DOES
--------------
1. sections: dated CORRECTION banners appended after the wrong text, which stays unchanged above
   them. GT03: exact duplicate paragraph and six duplicate concept-tag lines removed (hygiene).
2. links: descriptions prefixed "[Corrected 2026-10-19, <ref>] <new>. Previously: "<old>""
   (precedent consistency_pass_phase6_gt05). Types and endpoints unchanged.
3. wiki_history.db external_anchors: three wrong anchors corrected (notes record the original
   values); two anchors added (Hossenfelder 2017 PRD 95:124018 on GT02; Wall 2012 on HB09); notes
   appended to five anchors whose notes repeat a corrected claim.
4. wiki_history.db confidence_calibration: append-only rows, labels unchanged (owner-approved list).

SAFETY
------
Dry run by default; --apply writes. Every (table, row, column) target gets exactly one composed
write; a duplicate target aborts. Applied state is detected BEFORE find-strings are matched
(banners are stripped first, then every find must be absent and every replacement present); a
partially applied target aborts. Pending targets need every check string present and every
find-string exactly once. Post-write read-back verifies every value.

Run:  python3 scripts/migrations/qr005_corrections_2026_10_19.py
      python3 scripts/migrations/qr005_corrections_2026_10_19.py --apply
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-qr005-corrections-2026-10-19"
D = "2026-10-19"
REPORT = "docs/prior_art_reviews/QR005_CORRECTIONS_2026_10_19.md"
LINK_PREFIX = f"[Corrected {D}, {AUDIT_REF}] "
ERC = " Pattern tag: emergent-read-as-classical."
VSA = " Pattern tag: vocabulary-stacking-analogy."


def banner(body, tail="The text above is unchanged."):
    return f"\n\n> **CORRECTION {D} (`{AUDIT_REF}`).** {body} *{tail}*"


def parts(*ps):
    return " ".join(f"({i}) {p}" for i, p in enumerate(ps, 1))


# ─────────────────────────────────────────────────────────────────────────────
# Shared source strings (reading level recorded in each)
# ─────────────────────────────────────────────────────────────────────────────
J16 = "Jacobson 2016, PRL 116:201101 (arXiv:1505.04753 v4, full text read 2026-10-19)"
J95 = "Jacobson 1995, PRL 75:1260 (arXiv:gr-qc/9504004, full text read 2026-10-19)"
BIANCONI = ("Bianconi 2025 (PRD 111:066001; arXiv:2408.14391 v7, full text read 2026-10-19) uses no Fisher "
            "information metric, classical or quantum: the word 'Fisher' does not occur in the paper. Its action is "
            "the quantum relative entropy between the spacetime metric, treated as an operator, and a metric induced "
            "by matter fields (see GT04's correction).")
NOT_HOLO = ("Ryu–Takayanagi is not an input: Jacobson 2016 'proceeds directly in spacetime, making no use of "
            "holography'. The area term is his assumption that vacuum entanglement entropy has a finite, universal "
            "area density η; that this matches the Bekenstein–Hawking 1/4ħG is a consistency check. The holographic "
            "derivations (Faulkner et al. 2014: linearised Einstein equations within AdS/CFT) are parallel work, not "
            "an ingredient.")
NOT_LIMIT = ("Jacobson 2016 does not describe the 1995 result as a limit of the 2016 one, and neither derivation is "
             "classical. The 1995 derivation uses the Unruh temperature T = ħκ/2π and gives G = 1/(4ħη); the 2016 one "
             "uses the same Clausius relation at T = ħ/2π (its Eq. 16, which Jacobson calls 'just the usual Clausius "
             "relation'), now for vacuum entanglement in small causal diamonds. They are two semiclassical derivations "
             "in different settings, not a classical result and its quantum generalization (" + J95 + "; " + J16 + ").")
FIRST_LAW = ("The quantity involved is quantum relative entropy between states of quantum fields (IT04), not classical "
             "KL divergence (IT03). Its first-order variation around the reference state vanishes identically, for "
             "any state: this is the 'first law of entanglement' δS = (2π/ħ)δ⟨K⟩ (Jacobson 2016, Eq. 16), which holds "
             "whether or not the Einstein equation does. So 'δS_EE = 0 is equivalent to δD = 0' cannot be right; the "
             "Einstein equation comes from balancing the area variation against δ⟨K⟩. The vacuum is also not "
             "'maximally entangled': the hypothesis is that entanglement entropy is maximal at fixed volume. This is "
             "hop 3 of the Fisher–gravity chain (docs/CCA_GRAVITY_FINDINGS.md).")
NO_DS_SOURCE = ("No source makes this claim. Jacobson 2016 does not mention Padmanabhan, and it concerns small causal "
                "diamonds at a point, not the Hubble horizon; treat it as an internal analogy.")
TFD = ("The thermofield double has thermal (Boltzmann) weights e^{−βE_n/2}: it is maximally entangled only in the "
       "infinite-temperature limit β → 0. At finite temperature it is the purification of a thermal state, and its "
       "entanglement entropy equals the thermal entropy.")
RT_DIR = ("Wrong direction. The Ryu–Takayanagi area is 4G times the entanglement entropy, so less entanglement means a "
          "smaller minimal surface: the throat area shrinks while the wormhole gets longer. Van Raamsdonk: decreasing "
          "the entanglement 'effectively increases the proper distance between the corresponding spacetime regions, "
          "while decreasing the area separating the two regions' (Van Raamsdonk 2010, GRG 42:2323; arXiv:1005.3035, "
          "read 2026-10-19).")
BH_ENT = ("The entanglement entropy of quantum fields across a horizon is divergent: it depends on the cutoff and on the "
          "number of species, so it does not simply 'equal' A/4ℓ_P². It matches A/4G only once the divergence is "
          "absorbed into the renormalised G (Susskind & Uglum 1994; Jacobson 1994), fully only if gravity is wholly "
          "induced by matter (GT06; Speculative), and for spin-1 fields only after a horizon contact term is added "
          "(Kabat 1995, NPB 453:281; abstract read 2026-10-19). Whether black-hole entropy counts gravitational "
          "microstates or matter entanglement is open (Wald 2001; Carlip 2014).")
GSL_WALL = ("Wall's proofs of the GSL are semiclassical: quantum fields on a classical background, minimally coupled to "
            "general relativity. The 2012 proof rests on stated axioms (determinism, ultralocality, local Lorentz "
            "invariance, stability) checked for free fields and 1+1-dimensional CFTs, and uses the monotonicity of "
            "quantum relative entropy between states on the horizon algebra when restricted to later horizon slices "
            "(Wall 2012, PRD 85:104049; arXiv:1105.3445, abstract and §2.5 read 2026-10-19). That is not the "
            "non-negativity of a classical KL divergence between forward and reverse path distributions, which "
            "underlies the fluctuation theorems. The common thread is monotonicity of a relative entropy applied to "
            "different objects, so the fluctuation-theorem parallel is an analogy.")
GSL_PTR = "Only the fluctuation theorems rest on forward/reverse KL divergence; the GSL proofs do not (see What It Claims)."
HB01_SCOPE = ("The Bekenstein bound caps entropy relative to energy × size (S ≤ 2πER/ħc). It is not a cap per unit "
              "volume, and it contains no G: for fixed E it grows linearly with R.")
EGJ = ("Eling, Guedens & Jacobson 2006 (PRL 96:121301; gr-qc/0602001) and Chirco & Liberati 2010 (PRD 81:024016; "
       "arXiv:0909.4194), full text read 2026-10-19")

# (entry_id, section_name) -> dict(checks=[must-exist strings], replace=[(find, repl)], banners=[...])
SECTION_OPS = {}


def sec(eid, name, banners=(), replace=(), checks=()):
    op = SECTION_OPS.setdefault((eid, name), dict(checks=[], replace=[], banners=[]))
    op["checks"] += list(checks)
    op["replace"] += list(replace)
    op["banners"] += list(banners)


# ── C1, C3, C4, C5, C2 — GT10 ───────────────────────────────────────────────
C1 = ("Jacobson 2016 derives the semiclassical Einstein equation: quantum fields on a classical spacetime, with "
      "⟨T_ab⟩ as the source. It takes no position on whether gravitons exist. It leaves them out of the entanglement "
      "count only because the full Einstein tensor is already on the geometric side, so including graviton energy "
      "'would be double counting'. Temperature is not absent: the vacuum's modular Hamiltonian carries the "
      "temperature ħ/2π, and Jacobson calls δS = (2π/ħ)δ⟨K⟩ 'just the usual Clausius relation'. Newton's constant "
      "comes out as G = 1/(4ħη), so ħ is an input. Reading the result as 'not transmitted by gravitons' or 'no "
      "thermodynamics' goes beyond the paper (" + J16 + ")." + ERC)
sec("GT10", "What It Claims", checks=["No thermodynamic assumptions (heat, temperature, Clausius relation) are needed"],
    banners=[banner(C1)])
sec("GT10", "Constraint Category",
    checks=["No classical thermodynamic concepts (heat flux, temperature, Clausius relation) are invoked",
            "is promoted from a static holographic identity to a dynamical principle"],
    banners=[banner(parts(C1, NOT_HOLO))])
sec("GT10", "What The Math Says",
    checks=["This means gravity is not a fundamental force transmitted by gravitons",
            "No temperature, no heat, no thermodynamics — just entanglement structure"],
    banners=[banner(C1)])
C5 = ("'This IS the Einstein equation' needs its scope. Jacobson's result (his Eq. 26) is G_ab + Λg_ab = "
      "(2π/ħη)δ⟨T_ab⟩: the semiclassical equation, sourced by the expectation value of the stress tensor, for "
      "first-order variations of the local vacuum state in small diamonds, with Λ an undetermined constant. It holds "
      "exactly for conformal fields. For other fields it needs a conjecture about how entanglement varies (his Eq. "
      "21); Casini, Galante & Myers 2016 and Speranza 2016 show it can fail for some relevant operators, which v4 "
      "accommodates by letting the reference curvature depend on the ball size. Jacobson also flags coherent states, "
      "which carry energy without changing entanglement, as an open challenge.")
sec("GT10", "Mathematical Form",
    checks=["This IS the Einstein equation:", "GT10 is the quantum-informatic generalization of GT01"],
    banners=[banner(parts(C5, "Relationship to GT01: " + NOT_LIMIT))])
sec("GT10", "DS Cross-References",
    checks=["the 1995 result is the classical-thermodynamic limit",
            "that GT10 promotes from a static holographic identity",
            "equivalent to delta_D_KL = 0 around the maximally entangled vacuum state",
            "is the global version of GT10's local entanglement equilibrium"],
    banners=[banner(parts("GT01 clause: " + NOT_LIMIT, "HB07 clause: " + NOT_HOLO,
                          "IT03 clause: " + FIRST_LAW + VSA,
                          "GT03 clause: " + NO_DS_SOURCE))])

# ── C6, C7, C8 — GT01 ───────────────────────────────────────────────────────
sec("GT01", "What It Claims",
    checks=["it shows that gravity may not be a fundamental force but rather an emergent thermodynamic phenomenon"],
    banners=[banner(parts(
        "'Emergent' here means that Einstein's equation behaves like an equation of state; it does not mean that "
        "gravity is classical. Two of the four inputs are quantum: the Unruh temperature ħa/2πck_B and G = 1/(4ħη).",
        "Jacobson's own remark is narrower: it 'may be no more appropriate to canonically quantize the Einstein "
        "equation than it would be to quantize the wave equation for sound in air'. Sound is quantized (phonons are "
        "collective modes of quantum atoms), so the analogy leaves room for graviton-like collective quanta.",
        "The derivation needs local equilibrium: the horizon's expansion and shear are set to vanish at the point (" +
        J95 + ").") + ERC)])
sec("GT01", "Constraint Category",
    checks=["This is not an analogy: it is an exact mathematical derivation",
            "the geometric content (curvature) equals the thermodynamic content (entropy production)"],
    banners=[banner(parts(
        "'Exact' holds given four inputs, two of them quantum (ħ), plus local equilibrium.",
        "The derivation assumes no entropy production: expansion and shear vanish at the point. Curvature is matched "
        "to the entropy flux δQ/T, not to entropy production; production terms appear only out of equilibrium (GT07; "
        "Eling, Guedens & Jacobson 2006).") + ERC)])
sec("GT01", "What The Math Says", checks=["exactly as in the standard derivation from the Einstein-Hilbert action"],
    banners=[banner(
        "In the Einstein–Hilbert action Λ is a parameter put into the action. In Jacobson 1995 it is an arbitrary "
        "constant forced by local energy conservation and the Bianchi identity, and he writes that it 'remains as "
        "enigmatic as ever' (" + J95 + "). That is the structure of unimodular gravity: Alonso-Serrano & Liška 2020 "
        "(PRD 102:104056; abstract read 2026-10-19) argue that the thermodynamic route gives unimodular gravity rather "
        "than general relativity.")])
sec("GT01", "DS Cross-References",
    checks=["the Clausius relation δQ = TdS is a consequence of the second law applied locally",
            "Bianconi extends to quantum regime, using quantum relative entropy and Fisher information"],
    banners=[banner(parts(
        "TD3 clause: δQ = TdS is the reversible (equilibrium) equality; the second law gives only the inequality "
        "dS ≥ δQ/T. Jacobson calls δQ = TdS 'the fundamental relation' and requires local equilibrium; the "
        "non-equilibrium form is dS = δQ/T + d_iS (GT07).",
        "GT04 clause: " + BIANCONI))])

# ── C9–C12 — GT02 ───────────────────────────────────────────────────────────
VERLINDE_THEORY = parts(
    "ΔS = 2πk_B mcΔx/ħ is Verlinde's postulate, 'motivated by Bekenstein's' thought experiment; it is not the "
    "Bekenstein bound (HB01).",
    "G is defined, not derived: Verlinde introduces N = Ac³/Għ with 'a new constant G' and says one can 'regard this "
    "equation as the definition of G'. Newton's law is therefore largely an input.",
    "The 2011 paper never mentions gravitons. It argues that gravity is not a fundamental force and that, if so, "
    "closed strings (whose excitations include the graviton) must be emergent too; emergent quanta are not the same "
    "as no quanta (Verlinde 2011, JHEP 04:029; arXiv:1001.0785, full text read 2026-10-19).") + ERC
VERLINDE_STATUS = parts(
    "Attribution. JHEP 11 (2017) 007, 'Inconsistencies in Verlinde's emergent gravity', is by Dai & Stojkovic, not "
    "Hossenfelder (Crossref). It criticises Verlinde 2016's elastic-strain MOND derivation, and a reply disputes it "
    "(Yoon 2020, arXiv:2003.03198, not peer-reviewed). The solar-system conflict is from Hees, Famaey & Bertone 2017 "
    "(PRD 95:064019: perihelion advances off by seven orders of magnitude). Hossenfelder's own paper is 'Covariant "
    "version of Verlinde's emergent gravity' (PRD 95:124018; arXiv:1703.01415); Dai & Stojkovic's PRD 96:108501 "
    "(arXiv:1706.07854) comments on it: they correct a calculation error, recover de Sitter space, and find it "
    "unstable.",
    "Two theories. This entry is Verlinde 2011 (the entropic force). Brouwer et al. 2017, Dai & Stojkovic and "
    "Hossenfelder test or rework Verlinde 2016 ('Emergent gravity and the dark universe', SciPost Phys. 2:016, "
    "2017), a different theory.",
    "Brouwer et al. 2017 call their agreement 'only a first step': the prediction holds only for static, spherically "
    "symmetric, isolated mass distributions and assumes a ΛCDM background (abstract and §1 read 2026-10-19). Results "
    "the paragraph omits: Lelli, McGaugh & Schombert 2017 (fits only with low stellar mass-to-light ratios; the "
    "predicted residual correlation with radius is not seen); Hees et al. 2017 (above); Halenka & Miller 2020 (PRD "
    "102:084007: excluded at >5σ in clusters under nominal profile assumptions, but the authors conclude it cannot "
    "formally be ruled out once systematics are included); Brouwer et al. 2021 (A&A 650:A113: the lensing radial "
    "acceleration relation agrees, but early- and late-type galaxies differ by ≥6σ, which a gravity-only "
    "modification cannot explain). Abstracts read 2026-10-19.",
    "Kobakhidze 2011 uses ultra-cold-neutron data from Nesvizhevsky et al. 2002 (Nature 415:297, at the ILL; GRANIT "
    "is its successor). His argument is contested: Chaichian, Oksanen & Tureanu 2011 (PLB 702:419) find that "
    "entropic gravity does not necessarily contradict bound neutron states. It has since become a bound on "
    "entropic-force noise rather than a no-go (Schimmoller et al. 2021, PRR 3:033065: compatible with qBounce for "
    "σ ≳ 250). Abstracts read 2026-10-19.",
    "Visser 2011 needs a separate temperature and entropy for each pair of masses, a construction he calls "
    "'baroque' (not 'unphysical'), and states that his constraints do not directly affect Jacobson's or "
    "Padmanabhan's versions (full text read 2026-10-19).")
sec("GT02", "What It Claims",
    checks=["gravity is not mediated by a graviton", "the Bekenstein bound for information on holographic screens",
            "Hossenfelder & collaborators 2017 (JHEP 11, 007", "agreement WITHOUT free parameters"],
    banners=[banner("The theory. " + VERLINDE_THEORY), banner("The status paragraph. " + VERLINDE_STATUS)])
sec("GT02", "Mathematical Form", checks=["(Bekenstein, one bit per Compton wavelength)", "(bits on screen of area A)"],
    banners=[banner("ΔS = 2πk_B mcΔx/ħ is Verlinde's postulate, motivated by Bekenstein's thought experiment, not the "
                    "Bekenstein bound; N = Ac³/Għ is Verlinde's definition of G, so Newton's law is largely an input "
                    "(see What It Claims).")])
sec("GT02", "What The Math Says", checks=["from purely thermodynamic and holographic arguments"],
    banners=[banner("Not purely: G is put in by definition through N = Ac³/Għ, and ΔS is a postulate, not the "
                    "Bekenstein bound (see What It Claims).")])
sec("GT02", "DS Cross-References",
    checks=["the entropy change ΔS uses the Bekenstein bound to count bits",
            "Bianconi makes the framework quantum by using quantum relative entropy and Fisher information"],
    banners=[banner(parts("HB01 clause: Verlinde's ΔS is a postulate motivated by Bekenstein's thought experiment, "
                          "not the Bekenstein bound.", "GT04 clause: " + BIANCONI))])

# ── C13–C15 — GT03 ──────────────────────────────────────────────────────────
GT03_DUP = ("The monotonic approach to holographic equipartition (N_bulk → N_sur as the universe expands) is the "
            "cosmological analog of the Zamolodchikov c-theorem: just as the c-function counting UV degrees of freedom "
            "decreases monotonically under renormalisation group coarse-graining (c_UV ≥ c_IR), the bulk degrees of "
            "freedom N_bulk decrease relative to the boundary N_sur as the universe coarse-grains its way from early "
            "dense configurations to the present de Sitter epoch. Both are monotonicity/irreversibility theorems about "
            "degree-of-freedom counting under a coarse-graining flow — one along the RG scale, one along cosmic time.")
GT03_TAGS6 = ("\n• c-theorem analog\n• monotonic decrease of degrees of freedom\n• coarse-graining flow"
              "\n• RG-cosmology duality\n• RG irreversibility\n• UV-IR analogy")
NOT_HALT = ("Expansion does not halt at N_sur = N_bulk. Padmanabhan's V is the Hubble volume 4π/3H³, so dV/dt = 0 means "
            "only that the Hubble rate is constant. That is de Sitter space, which expands exponentially.")
CTHM = ("The c-theorem parallel is an analogy, not a theorem: no monotone c-function is constructed and nothing is "
        "proved for cosmic expansion." + VSA)
sec("GT03", "What It Claims", checks=["a state where N_sur = N_bulk and expansion halts"],
    replace=[(GT03_DUP + " " + GT03_DUP, GT03_DUP)],
    banners=[banner(parts(
        NOT_HALT + " The entry's own 'approaches de Sitter' says so. N_bulk is defined with a sign factor ε and is "
        "positive only in the accelerating phase. Substituting the definitions turns the equation into the standard "
        "Friedmann acceleration equation (his Eq. 6), and Padmanabhan himself warns that rewriting standard results in "
        "thermodynamic language 'is unnecessary and does not add to our insight' (Padmanabhan 2012, arXiv:1206.4916, "
        "full text read 2026-10-19).",
        CTHM, "Hygiene: the c-theorem paragraph appeared twice, verbatim; the second copy was removed."))])
sec("GT03", "Mathematical Form", checks=["This yields the Friedmann equation:"],
    banners=[banner("Padmanabhan's equation gives the Friedmann acceleration equation ä/a = −(4πL_P²/3)(ρ + 3p) "
                    "(his Eq. 6, flat case); the H² form follows only after integrating with energy conservation and a "
                    "late-time de Sitter boundary condition. N_bulk carries a sign factor ε and is positive only while "
                    "the expansion accelerates.")])
sec("GT03", "Constraint Category",
    checks=["connecting cosmological dynamics to the RG irreversibility proven by Zamolodchikov's c-theorem"],
    banners=[banner(CTHM)])
sec("GT03", "DS Cross-References", checks=["is the microscopic foundation for Padmanabhan's holographic equipartition"],
    banners=[banner(parts("RG04 clause: " + CTHM, "GT10 clause: " + NO_DS_SOURCE + VSA))])
sec("GT03", "Mathematical Archetype",
    checks=["the universe expands until N_sur = N_bulk", "This makes holographic equipartition the cosmological c-theorem"],
    banners=[banner(parts(NOT_HALT, CTHM))])
sec("GT03", "What The Math Says",
    checks=["When N-sur equals N-bulk, expansion halts", "The structural parallel to the Zamolodchikov c-theorem is exact"],
    banners=[banner(parts(NOT_HALT, "'Exact' is not supported. " + CTHM))])
sec("GT03", "Concept Tags", replace=[(GT03_TAGS6 + GT03_TAGS6, GT03_TAGS6)])

# ── C16 — GT04 and the Bianconi clauses elsewhere ───────────────────────────
GT04_MAIN = (
    "Checked against the full text (arXiv:2408.14391 v7, read 2026-10-19), Bianconi's paper does not contain most of "
    "what this entry says. The word 'Fisher' does not occur in it: there is no Fisher or Bures metric, classical or "
    "quantum, and no Hessian of a relative entropy. There is no optimal transport or gradient flow, and no network: "
    "the paper is a continuum, Lorentz-invariant field theory (an earlier, discrete version on higher-order networks "
    "is a separate paper). What it does: it treats the spacetime metric at each point as a quantum operator, an "
    "'effective density matrix'; it describes bosonic matter topologically (Dirac–Kähler: a 0-form, a 1-form and a "
    "2-form); and its action is the quantum relative entropy between the spacetime metric and the metric induced by "
    "the matter fields. The resulting modified Einstein equations reduce to Einstein's with zero cosmological constant "
    "at low coupling; an auxiliary 'G-field' gives a small positive emergent Λ. It is a classical field theory, and the "
    "author suggests that canonically quantizing it 'could bring new insights into quantum gravity'. So 'quantum "
    "relative entropy' here does not make gravity quantum. The 2026-05-04 disambiguation above was right that this is "
    "not the classical Fisher–Rao metric, but wrong to say the paper uses the quantum Fisher (Bures) metric: it uses "
    "neither." + VSA)
GT04_PTR = "There is no Fisher-metric step in the paper (see What It Claims)."
sec("GT04", "What It Claims", checks=["Bianconi's approach is network-native", "treats gravitational dynamics as optimal transport"],
    banners=[banner(GT04_MAIN)])
sec("GT04", "Mathematical Form", checks=["Gravity = curvature of the Fisher-Rao metric on quantum state space"],
    banners=[banner("Not in the paper. Bianconi's action is the quantum relative entropy between the spacetime metric "
                    "(treated as an operator) and the matter-induced metric; no Fisher metric appears (see What It "
                    "Claims).")])
sec("GT04", "Constraint Category", checks=["quantum relative entropy → Fisher metric → curvature → Einstein equations"],
    banners=[banner(GT04_PTR)])
sec("GT04", "DS Cross-References",
    checks=["the Fisher-Rao metric on quantum state space is the emergent spacetime metric in Bianconi's framework"],
    banners=[banner("IT05, IT08 and RG06 clauses: no Fisher metric or gradient flow appears in the paper. GT01 clause: "
                    "Jacobson's derivation is not classical (it uses T = ħκ/2π), and Bianconi does not use Fisher "
                    "information (see What It Claims).")])
sec("GT04", "Mathematical Archetype", checks=["an action built from the quantum Fisher information metric"],
    banners=[banner("The action is a relative entropy between two metrics, not a functional of a Fisher metric (see "
                    "What It Claims).")])
sec("GT04", "What The Math Says", checks=["The network structure allows discrete formulation"],
    banners=[banner("This describes a construction that is not in the paper: no Fisher metric, no curvature of state "
                    "space, no network (see What It Claims).")])
for eid, name, chk in [
        ("GT05", "DS Cross-References", "both use quantum information (entanglement, Fisher information) to derive gravity"),
        ("IT04", "What It Claims", "to gravitational dynamics in frameworks such as Bianconi's"),
        ("IT04", "DS Cross-References", "Bianconi's framework uses quantum relative entropy and its Fisher information"),
        ("IT08", "Constraint Category", "and gravity (Bianconi)"),
        ("IT08", "DS Cross-References", "derives gravitational dynamics from the Fisher-Rao geometry on quantum state space"),
        ("RG06", "What It Claims", "through Bianconi's framework, to gravitational dynamics"),
        ("RG06", "DS Cross-References", "both use the Fisher metric as the fundamental geometric object"),
        ("BR04", "DS Cross-References", "Bianconi's framework uses the Fisher metric on quantum states to derive gravity")]:
    sec(eid, name, checks=[chk], banners=[banner("Bianconi clause: " + BIANCONI + VSA)])
sec("BR04", "What It Claims", checks=["through Jacobson's and Bianconi's frameworks, in spacetime geometry"],
    banners=[banner("Neither framework puts a Fisher–Rao metric into spacetime geometry. Jacobson 1995 and 2016 use "
                    "horizon or entanglement entropy with the Unruh temperature, and no Fisher metric. " + BIANCONI + VSA)])

# ── C17 — GT06 ──────────────────────────────────────────────────────────────
sec("GT06", "Constraint Category", checks=["a thermodynamic/statistical effect of the underlying quantum degrees of freedom"],
    banners=[banner(
        "Induced gravity is a one-loop quantum effect (order ħ) of matter fields on a classical background, not a "
        "thermodynamic one: Visser 2002 (MPLA 17:977; gr-qc/0204062, read 2026-10-19) sets it up as quantizing the "
        "matter fields with 'the geometry considered as a classical background'. 'Established' fits the one-loop "
        "generation of an R term in the effective action; that gravity is wholly induced is Speculative." + ERC)])
sec("GT06", "Mathematical Form", checks=["∫ (dk/16π²)", "S_ent = (A/4G_ind) + finite terms"],
    banners=[banner(parts(
        "The formula is linear in the cutoff, which is wrong: the heat-kernel coefficient of R is quadratic in the "
        "cutoff κ (Visser 2002, Eq. 9: the a₁ term carries κ²), so 1/G_ind ∝ N_s κ² in natural units, with O(1), "
        "spin-dependent factors.",
        "S_ent = A/4G_ind holds for minimally coupled spin-0 and spin-½ fields; for spin 1 the black-hole entropy and "
        "the entanglement entropy differ by a contact term at the horizon (Kabat 1995, NPB 453:281; abstract read "
        "2026-10-19)."))])
sec("GT06", "What The Math Says", checks=["S-ent equals A over 4 G-ind plus finite corrections"],
    banners=[banner("The R coefficient is quadratic in the cutoff, not linear, and S_ent = A/4G_ind holds for spin 0 "
                    "and ½ but needs a horizon contact term for spin 1 (see Mathematical Form).")])

# ── C18 — GT07 ──────────────────────────────────────────────────────────────
GT07_MAIN = parts(
    "Eling, Guedens & Jacobson 2006 already contain both terms. In f(R) gravity the required entropy production comes "
    "from the expansion (θ²) and acts as a bulk viscosity 3ħαf/4π. In pure GR it is optional, allowed when the "
    "horizon shear is non-zero, and acts as a shear viscosity 1/16πG (η/s = ħ/4π), as for black-hole horizons. So "
    "'σ is produced by the shear' is right only for the optional GR term.",
    "Chirco & Liberati 2010 do not introduce the bulk viscosity: they cite EGJ for it. They identify the GR shear "
    "term with Hartle–Hawking tidal heating and generalise it to f(R).",
    "The Jarzynski, Crooks and Seifert parallels are analogies, not shared derivations.",
    "Notation: σ is used both for the shear tensor σ_μν and for entropy production; EGJ write the latter d_iS, with "
    "dS = δQ/T + d_iS (" + EGJ + ").") + VSA
sec("GT07", "What It Claims", checks=["giving spacetime an effective bulk viscosity", "σ is produced by the shear of null congruences"],
    banners=[banner(GT07_MAIN)])
sec("GT07", "Mathematical Form", checks=["internal entropy production rate (from horizon shear)"],
    banners=[banner("σ ≥ 0 (entropy production) and σ_μν (shear) are different quantities; EGJ write entropy production "
                    "as d_iS. In f(R) it comes from the expansion, not the shear. The 'analog structure' lines are "
                    "analogies (see What It Claims).")])
sec("GT07", "Constraint Category", checks=["is the gravitational counterpart of the dissipated work bound"],
    banners=[banner("The Jarzynski and Seifert parallels are analogies; no shared derivation is given (see What It "
                    "Claims)." + VSA)])
sec("GT07", "Mathematical Archetype", checks=["is structurally identical to the Jarzynski dissipated-work bound"],
    banners=[banner("Analogous, not structurally identical: no shared derivation is given (see What It Claims)." + VSA)])
sec("GT07", "What The Math Says",
    checks=["Chirco and Liberati (2010) showed this entropy production is a gravitational viscosity",
            "parallels the Jarzynski equality exactly"],
    banners=[banner("Two corrections. In f(R) the entropy production comes from the expansion and acts as a bulk "
                    "viscosity 3ħαf/4π, already in EGJ 2006; in GR the optional term is a shear viscosity 1/16πG, "
                    "which Chirco & Liberati identify with tidal heating. The Jarzynski parallel is an analogy, not "
                    "exact (see What It Claims).")])

# ── C19 — HB01 (+ GT11) ─────────────────────────────────────────────────────
sec("HB01", "What It Claims",
    checks=["there is a maximum number of bits per unit volume",
            "the bound arises from requiring that the system not form a black hole"],
    banners=[banner(parts(
        HB01_SCOPE + " A cap per unit area is the holographic bound S ≤ A/4ℓ_P² (HB03), a different, gravitational "
        "bound.",
        "'Requiring that the system not form a black hole' is the argument for the spherical (holographic) bound "
        "(Susskind 1995). Bekenstein's own argument applied the generalized second law to lowering a system into a "
        "black hole. Casini 2008 shows that a well-defined version, the positivity of a relative entropy, holds "
        "automatically in flat-space quantum field theory, with no gravity and no species problem (CQG 25:205021; "
        "arXiv:0804.2182, abstract and introduction read 2026-10-19)."))])
sec("HB01", "Constraint Category", checks=["It is the tightest universal bound on information density in physics"],
    banners=[banner("It is not a bound on information density. " + HB01_SCOPE)])
sec("HB01", "What The Math Says", checks=["Any attempt to pack more information into the region would cause gravitational collapse"],
    banners=[banner("Not as stated: the bound contains no G, and Casini 2008 shows a version holds in flat-space quantum "
                    "field theory without gravity. Collapse arguments motivate the holographic bound (HB03), not this "
                    "one (see What It Claims).")])
sec("GT11", "DS Cross-References", checks=["maximum information density S <= A/4"],
    banners=[banner("HB01 clause: S ≤ A/4 is the holographic bound (HB03), not the Bekenstein bound S ≤ 2πER/ħc "
                    "(HB01), and neither is a maximum information density.")])

# ── C20 — HB02, IT02 ────────────────────────────────────────────────────────
MICRO = ("Microstate counting reproduces A/4 only for special black holes. Strominger & Vafa 1996 count a class of "
         "five-dimensional extremal (BPS) black holes in string theory (PLB 379:99; abstract read 2026-10-19); extreme "
         "Kerr is reached only under the conjectural Kerr/CFT assumptions. No count derives A/4 for Schwarzschild or "
         "ordinary astrophysical Kerr, and loop quantum gravity calibrates the 1/4 through the Immirzi parameter.")
sec("HB02", "What It Claims",
    checks=["has been reproduced by string theory microstate counting (Strominger & Vafa, 1996)",
            "whose von Neumann entropy exactly equals A/4l_P²"],
    banners=[banner(parts(MICRO, BH_ENT))])
sec("HB02", "DS Cross-References",
    checks=["IT02 (Von Neumann Entropy — BH entropy equals the entanglement entropy of quantum fields across the horizon"],
    banners=[banner("IT02 clause: " + BH_ENT)])
sec("IT02", "What It Claims",
    checks=["equals the von Neumann entropy of the reduced density matrix obtained by tracing over the degrees of freedom behind the event horizon"],
    banners=[banner(BH_ENT)])
sec("IT02", "DS Cross-References", checks=["BH entropy equals entanglement entropy across the horizon"],
    banners=[banner("HB02 clause: " + BH_ENT)])

# ── C21 — HB03 ──────────────────────────────────────────────────────────────
HOLO_NOT_FROM_BEK = ("The holographic bound does not follow from the Bekenstein bound. It is motivated by the "
                     "generalized second law and gravitational-collapse arguments (Susskind 1995). The Bekenstein bound "
                     "contains no G and scales with E·R; E·R ~ R² holds only for a system at the edge of collapse "
                     "(R ~ GE/c⁴).")
sec("HB03", "What It Claims", checks=["can contain at most one bit per Planck area"],
    banners=[banner(parts(
        "S ≤ A/4ℓ_P² is in nats: 1/(4 ln 2) ≈ 0.36 bits per Planck area, not one bit. The entry's own figure, 1.4 × "
        "10⁶⁹ bits/m², already uses this.",
        "As a statement about 'any region of space' the spacelike bound fails in general (for example in cosmology "
        "and in collapsing regions) and is replaced by Bousso's covariant bound (1999)."))])
sec("HB03", "DS Cross-References", checks=["the holographic principle follows from the Bekenstein bound"],
    banners=[banner("HB01 clause: " + HOLO_NOT_FROM_BEK)])

# ── C22 — HB04 ──────────────────────────────────────────────────────────────
sec("HB04", "What It Claims", checks=["transferring information from behind the horizon to the exterior"],
    banners=[banner(
        "Hawking's calculation gives exactly thermal radiation that carries no information about what fell in; that "
        "is what makes the paradox, as the next sentence says. 'Transferring information from behind the horizon' is "
        "not what the calculation shows. Since 2019, semiclassical gravitational path-integral calculations that "
        "include 'islands' give a Page curve for the radiation's fine-grained entropy, consistent with unitarity "
        "(Almheiri, Hartman, Maldacena, Shaghoulian & Tajdini 2021, RMP 93:035002; arXiv:2006.06872, abstract and "
        "passages read 2026-10-19). They show how much information comes out, not how.")])

# ── C23, C24 — BR03, HB07, BR01 ─────────────────────────────────────────────
sec("BR03", "What It Claims",
    checks=["the Ryu-Takayanagi surface grows, corresponding to the wormhole throat stretching",
            "Starting from a thermofield double state (maximally entangled)"],
    banners=[banner(parts(RT_DIR, TFD))])
sec("BR03", "What The Math Says",
    checks=["As entanglement entropy decreases, the Ryu-Takayanagi surface area grows",
            "a maximally entangled state between two copies of a CFT"],
    banners=[banner(parts(RT_DIR + " This section gives both directions; 'the throat area shrinks' is the right one.",
                          TFD))])
sec("BR03", "DS Cross-References",
    checks=["the RT surface area grows as entanglement decreases",
            "the Fisher metric on quantum states generates the geometric structure"],
    banners=[banner(parts("HB07 clause: " + RT_DIR,
                          "GT04 clause: unsupported. " + BIANCONI + VSA))])
sec("HB07", "DS Cross-References", checks=["removing entanglement causes the minimal surface to grow"],
    banners=[banner("BR03 clause: " + RT_DIR)])
sec("BR01", "What The Math Says", checks=["is a maximally entangled state between two copies of a quantum system"],
    banners=[banner(TFD)])
sec("BR01", "Mathematical Archetype", checks=["the amount of each is conserved in the equivalence"],
    banners=[banner("'Conserved' has no content here: ER = EPR states no conserved quantity, so the conservation-law "
                    "archetype does not fit. The facet value is left for the archetype review.")])

# ── C25 — HB09 ──────────────────────────────────────────────────────────────
sec("HB09", "What It Claims",
    checks=["Both the GSL and the fluctuation theorems are consequences of the non-negativity of KL divergence"],
    banners=[banner(GSL_WALL + VSA)])
sec("HB09", "Mathematical Form", checks=["Both follow from D_KL(p_forward || p_reverse) ≥ 0."], banners=[banner(GSL_PTR)])
sec("HB09", "Constraint Category",
    checks=["are manifestations of the non-negativity of KL divergence between forward and time-reversed distributions"],
    banners=[banner(GSL_PTR)])
sec("HB09", "DS Cross-References", checks=["D_KL(p||q) ≥ 0 is the common information-theoretic root of both the GSL"],
    banners=[banner("IT03 clause: " + GSL_PTR)])
sec("HB09", "What The Math Says",
    checks=["Both the GSL and the Jarzynski/Crooks relations follow from the same mathematical fact"],
    banners=[banner(GSL_PTR)])

# ── C26 — IT05 ──────────────────────────────────────────────────────────────
sec("IT05", "What It Claims",
    checks=["connects statistical inference to general relativity (Ruppeiner geometry)", "and emergent gravity (Bianconi)"],
    banners=[banner(parts(
        "Ruppeiner geometry lives on thermodynamic state space (including black-hole thermodynamic parameters), not "
        "on spacetime: read 'connects statistical inference to thermodynamic geometry (Ruppeiner; BR04)'.",
        "Bianconi clause: " + BIANCONI) + VSA)])

# ── C27 — GT05 ──────────────────────────────────────────────────────────────
sec("GT05", "What The Math Says",
    checks=["Carney estimates that current technology is within an order of magnitude of the required sensitivity"],
    banners=[banner(
        "Not in the paper. Carney et al. 2025 say that the minimum force noise of their non-local model, about "
        "10⁻²⁴ N/√Hz for milligram masses at millimetre separation (with λ = 0; their Eq. 51), is 'nearly observable "
        "with modern ultra-sensitive force measurements' (PRX 15:031038; arXiv:2502.17575, read 2026-10-19). The "
        "QR-005 literature map estimates that current mm-scale gravity sensors are about 10⁹ times noisier (sensor "
        "figures from sub-agent readings of Westphal et al. 2021 and Fuchs et al. 2024, not checked here). λ = 0 is "
        "itself already excluded by atom interferometry, so the surviving models predict even less noise.")])

# ─────────────────────────────────────────────────────────────────────────────
# Link descriptions — (id, source, target, must-contain-in-old, new text)
# ─────────────────────────────────────────────────────────────────────────────
_BIAN_L = ("Bianconi 2025 contains no Fisher information metric, classical or quantum (full text read 2026-10-19); its "
           "action is the quantum relative entropy between the spacetime metric, treated as an operator, and a "
           "matter-induced metric.")
_BH_L = ("Horizon entanglement entropy is cutoff- and species-dependent; it matches A/4G only after renormalising G "
         "(Susskind & Uglum 1994), fully only if gravity is wholly induced (Speculative), and needs a contact term for "
         "spin 1 (Kabat 1995).")
_RT_L = ("Less entanglement means a smaller RT surface (throat area) and a longer wormhole (Van Raamsdonk 2010), not a "
         "growing surface.")
_PADMA_L = ("Internal analogy, not a published result: Jacobson 2016 does not mention Padmanabhan, and it concerns small "
            "causal diamonds at a point, not the Hubble horizon.")
LINK_FIXES = [
    (851, "GT10", "GT01", "classical limit of entanglement equilibrium",
     "Not a generalization or a classical limit: Jacobson 1995 and 2016 are two semiclassical derivations (both use "
     "T ∝ ħ and G = 1/4ħη) in different settings, local Rindler horizons and small causal diamonds."),
    (853, "GT10", "HB07", "promotes from a static holographic identity",
     "Jacobson 2016 makes 'no use of holography'; Ryu–Takayanagi is not an input. The area term is an assumed "
     "universal entanglement density η, matched to 1/4ħG as a consistency check."),
    (855, "GT10", "IT03", "equivalent to delta_D_KL = 0 at the vacuum state",
     "Weak link. The relevant quantity is quantum relative entropy (IT04), whose first-order variation vanishes "
     "identically (the first law of entanglement, δS = 2πδ⟨K⟩/ħ) whether or not the Einstein equation holds; the "
     "Einstein equation comes from balancing the area variation against it."),
    (852, "GT10", "GT03", "is the global version of Jacobson 2016", _PADMA_L),
    (866, "GT03", "GT10", "is the global version of Jacobson 2016", _PADMA_L),
    (742, "GT02", "HB01", "uses the Bekenstein bound to count information bits",
     "Verlinde's ΔS = 2πk_B mcΔx/ħ is a postulate motivated by Bekenstein's thought experiment, not an application of "
     "the Bekenstein bound."),
    (747, "GT04", "IT05", "becomes the spacetime metric", _BIAN_L),
    (748, "GT04", "GT01", "using Fisher information rather than the Clausius relation",
     _BIAN_L + " Jacobson 1995 is not classical either (it uses T = ħκ/2π)."),
    (706, "IT04", "GT04", "its Fisher information metric on quantum state space", _BIAN_L),
    (775, "RG06", "GT04", "Bianconi for gravity", _BIAN_L),
    (805, "BR04", "GT04", "Bianconi shows it generates gravitational dynamics", _BIAN_L),
    (713, "HB01", "INFO1", "nature has a maximum information density",
     "The Bekenstein bound caps entropy relative to energy × size (S ≤ 2πER/ħc), not per unit volume; Casini 2008 "
     "shows a version holds automatically in flat-space QFT."),
    (857, "GT11", "HB01", "Bekenstein bound sets maximum information density",
     "S ≤ A/4 is the holographic bound (HB03), not the Bekenstein bound (HB01), and neither is a maximum information "
     "density."),
    (715, "HB01", "HB03", "The Bekenstein bound implies holography",
     "The holographic bound is motivated by the GSL and collapse arguments (Susskind 1995), not derived from the "
     "Bekenstein bound, which contains no G; E·R ~ R² only at the edge of collapse."),
    (700, "IT02", "HB02", "Bekenstein-Hawking entropy equals the entanglement entropy", _BH_L),
    (716, "HB02", "IT02", "the gravitational and quantum information descriptions are identical", _BH_L),
    (754, "GT06", "HB02", "G is determined by S_ent = A/4G",
     "Both 1/G_ind and horizon entanglement entropy are cutoff-dependent; S_ent = A/4G_ind is a renormalisation "
     "statement, valid for spin 0 and ½ and needing a contact term for spin 1 (Kabat 1995)."),
    (800, "BR03", "HB07", "the RT minimal surface area grows", _RT_L),
    (812, "HB09", "IT03", "shared information-theoretic root",
     "Analogy only: the GSL proofs use monotonicity of quantum relative entropy on the horizon (Wall 2012), not a "
     "classical forward/reverse KL divergence."),
]

# ─────────────────────────────────────────────────────────────────────────────
# Anchors (wiki_history.db) — corrections keep the row; notes record the original values
# ─────────────────────────────────────────────────────────────────────────────
ANCHOR_UPDATES = [
    # (id, entry_id, expected_identifier, set{col: value}, note to append)
    (855, "GT02", "10.1007/JHEP11(2017)007",
     {"title": "Dai & Stojkovic 2017 - Inconsistencies in Verlinde's emergent gravity (JHEP 11 (2017) 007; arXiv:1710.00946)"},
     "Was titled 'Hossenfelder 2017 - Inconsistencies in Verlinde's emergent gravity'. Crossref: the authors are Dai & "
     "Stojkovic. The paper criticises Verlinde 2016 (emergent gravity and the dark universe), not GT02's Verlinde 2011; "
     "a reply disputes it (Yoon 2020, arXiv:2003.03198). The solar-system conflict in the original note is Hees et al. "
     "2017, not this paper."),
    (856, "GT02", "1706.07854",
     {"title": "Dai & Stojkovic 2017 - A note on a covariant version of Verlinde's emergent gravity (arXiv preprint of PRD 96:108501)"},
     "Was titled 'Hossenfelder 2017 - A covariant version of Verlinde's emergent gravity'. arXiv metadata: "
     "arXiv:1706.07854 is Dai & Stojkovic's comment, published as PRD 96:108501 (anchor 857). Hossenfelder's own paper "
     "is arXiv:1703.01415 / PRD 95:124018, added as its own anchor."),
    (422, "HB09", "10.1103/PhysRevD.80.124008",
     {"identifier": "10.1088/1126-6708/2009/06/021",
      "title": "Wall 2009 - Ten proofs of the generalized second law (JHEP 06 (2009) 021; arXiv:0901.3865)",
      "canonical_role": "comprehensive_survey"},
     "Corrected identifier: the row carried doi:10.1103/PhysRevD.80.124008, which Crossref resolves to Guica, Hartman, "
     "Song & Strominger 2009, 'The Kerr/CFT correspondence', not Wall. Wall's paper is JHEP 06 (2009) 021 (Crossref "
     "checked 2026-10-19), not PRD 80, 124008 as the original note says. Role changed progenitor -> "
     "comprehensive_survey: it surveys proofs; Bekenstein 1973 (anchor 421) is the progenitor."),
]
ANCHOR_NOTES = [
    (837, "GT04", "10.1103/PhysRevD.111.066001",
     "Full text read (arXiv v7): the paper contains no Fisher or Bures metric, classical or quantum; the word 'Fisher' "
     "does not occur. The action is the quantum relative entropy between the spacetime metric (as an operator) and the "
     "matter-induced metric. The 'Hessian = Bures / quantum Fisher' statement above was an inference, not the paper's."),
    (388, "GT10", "10.1103/PhysRevLett.116.201101",
     "Full text read (arXiv v4): 'making no use of holography' — the derivation does not assume a holographic context; "
     "it is semiclassical, for first-order variations of the local vacuum state (exact for conformal fields, modulo a "
     "conjecture otherwise), and takes no position on gravitons."),
    (852, "GT02", "10.1093/mnras/stw3192",
     "Tests Verlinde 2016, not GT02's Verlinde 2011. Abstract: 'only a first step'; valid only for static, spherically "
     "symmetric, isolated lenses; ΛCDM background assumed."),
    (853, "GT02", "10.1103/PhysRevD.83.021502",
     "Contested: Chaichian, Oksanen & Tureanu 2011 (PLB 702:419) find no necessary contradiction; Schimmoller et al. "
     "2021 (PRR 3:033065) turn it into a noise bound (σ ≳ 250). The data are Nesvizhevsky et al. 2002 (ILL)."),
    (854, "GT02", "10.1007/JHEP10(2011)140",
     "Full text read: Visser calls the construction 'baroque' (not 'unphysical') and states his constraints do not "
     "directly affect Jacobson's or Padmanabhan's versions."),
]
ANCHOR_INSERTS = [
    dict(entry_id="GT02", source="doi", identifier="10.1103/PhysRevD.95.124018",
         title="Hossenfelder 2017 - Covariant version of Verlinde's emergent gravity (PRD 95:124018; arXiv:1703.01415)",
         tier=1, stability="active-literature", relationship="adjacent_concept", role=None, confidence="high",
         notes="Hossenfelder's own paper, previously mis-credited in two GT02 anchors (855, 856). A covariant Lagrangian "
               "for Verlinde 2016, not GT02's Verlinde 2011. Metadata checked on Crossref and arXiv 2026-10-19; body not "
               "read."),
    dict(entry_id="HB09", source="doi", identifier="10.1103/PhysRevD.85.104049",
         title="Wall 2012 - Proof of the generalized second law for rapidly changing fields and arbitrary horizon slices (PRD 85:104049; arXiv:1105.3445)",
         tier=1, stability="canonical", relationship="cites", role=None, confidence="high",
         notes="Abstract and §2.5 read 2026-10-19: semiclassical GSL proof for quantum fields minimally coupled to GR; "
               "axioms verified for free fields and 1+1 CFTs; uses monotonicity of quantum relative entropy on the "
               "horizon algebra. Crossref checked."),
]

# ─────────────────────────────────────────────────────────────────────────────
# Calibration — append-only, labels unchanged (owner approval required)
# ─────────────────────────────────────────────────────────────────────────────
CALIBRATIONS = [
    ("fisher_gravity_chain", "structural_observation", "Speculative", D, AUDIT_REF,
     "Speculative (unchanged) — three of the four hop descriptions are wrong as written: hop 2 misnames the Hessian "
     "identity as Cramér–Rao, hop 3 rests on an identity independent of Einstein's equation, hop 4's 'classical limit' "
     "is not in Jacobson 2016 [vocabulary-stacking-analogy; emergent-read-as-classical]",
     "QR-005 corrections pass. Hop 3 (IT03 → GT10): the first-order variation of relative entropy around the vacuum "
     "vanishes identically for any state (the first law of entanglement, Jacobson 2016 Eq. 16, read in full), so the "
     "claimed equivalence δS_EE = 0 ⇔ δD_KL = 0 is false and the KL link carries no Einstein content; the quantity is "
     "also quantum relative entropy, not classical KL. Hop 4 (GT10 → GT01): Jacobson 2016 calls its Eq. 16 'just the "
     "usual Clausius relation' at T = ħ/2π; both 1995 and 2016 are semiclassical, and neither is a limit of the other. "
     "Hop 2: Fisher = Hessian of KL is correct, but it is not the Cramér–Rao bound. The label stays Speculative because "
     "the chain is already recorded as a conceptual analogy (M0; 2026-05-04), not a theorem chain; this row records "
     "that even the analogy's hop 3 is vacuous. Report: " + REPORT + "."),
    ("GT04", "entry", "Speculative", D, AUDIT_REF,
     "Speculative (unchanged) — the paper uses no Fisher metric, classical or quantum; the 2026-05-04 'Bures' reading "
     "was an inference [vocabulary-stacking-analogy]",
     "QR-005 corrections pass, Bianconi 2025 full text read (arXiv:2408.14391 v7). The action is the quantum relative "
     "entropy between the spacetime metric, treated as an operator, and the metric induced by topological (Dirac–Kähler) "
     "matter fields; the word 'Fisher' does not occur; no network, optimal transport or gradient flow; a continuum "
     "classical field theory whose canonical quantization the author leaves open. The 2026-05-04 row was right that "
     "this is not classical Fisher–Rao, wrong that the Hessian is the Bures metric. Report: " + REPORT + "."),
    ("GT02", "entry", "Speculative", D, AUDIT_REF,
     "Speculative (unchanged) — attribution corrected (JHEP 11 (2017) 007 is Dai & Stojkovic); critiques of Verlinde "
     "2016 separated from Verlinde 2011; Halenka & Miller 2020 not a clean exclusion",
     "QR-005 corrections pass. The 2026-05-04 row credits 'Hossenfelder 2017 (JHEP 11, 007)'; Crossref gives Dai & "
     "Stojkovic, and the solar-system constraint is Hees, Famaey & Bertone 2017. Brouwer 2017, Dai & Stojkovic and "
     "Hossenfelder concern Verlinde 2016, a different theory from GT02's Verlinde 2011. Halenka & Miller 2020: >5σ "
     "only under nominal profile assumptions; the authors conclude emergent gravity cannot formally be ruled out on "
     "cluster scales once systematics are included. Report: " + REPORT + "."),
    ("GT10", "entry", "Supported", D, AUDIT_REF,
     "Supported (unchanged) — semiclassical; first-order variations of the local vacuum state; no holography; silent "
     "on gravitons [emergent-read-as-classical]",
     "QR-005 corrections pass, Jacobson 2016 read in full (arXiv v4). 'Linearized only' (2026-05-04) is better stated "
     "as: first-order variations of the local vacuum state in small causal diamonds, with ⟨T_ab⟩ as source; the paper "
     "notes the full nonlinear Einstein tensor sits on the geometric side. It uses no holography, takes T = ħ/2π and "
     "G = 1/4ħη, and leaves gravitons out only to avoid double counting. Exact for conformal fields; otherwise modulo "
     "a conjecture that can fail for some relevant operators (CGM 2016). Report: " + REPORT + "."),
]


# ─────────────────────────────────────────────────────────────────────────────
def check_targets():
    seen = set()
    def once(k):
        if k in seen:
            raise SystemExit(f"ABORT — duplicate target {k}")
        seen.add(k)
    for (eid, name) in SECTION_OPS:
        once(("sections", eid, name, "content"))
    for (lid, *_rest) in LINK_FIXES:
        once(("links", lid, "description"))
    for (aid, *_rest) in ANCHOR_UPDATES + ANCHOR_NOTES:
        once(("external_anchors", aid))
    for a in ANCHOR_INSERTS:
        once(("external_anchors", a["entry_id"], a["identifier"]))
    for c in CALIBRATIONS:
        once(("confidence_calibration", c[0], c[3], c[4]))


def plan_section(content, op, label):
    """Return new content, or None if already applied. Abort on partial state."""
    banners = op["banners"]
    stripped = content
    for b in banners:
        stripped = stripped.replace(b, "")
    present = [b in content for b in banners]
    applied = all(present) and all(f not in stripped and r in stripped for f, r in op["replace"])
    if applied:
        return None
    if any(present) or (AUDIT_REF in content):
        raise SystemExit(f"[{label}] ABORT — partially applied")
    new = content
    for find, repl in op["replace"]:
        n = new.count(find)
        if n != 1:
            raise SystemExit(f"[{label}] FAIL — find count {n}: {find[:70]!r}")
        new = new.replace(find, repl, 1)
    for chk in op["checks"]:
        if chk not in content:
            raise SystemExit(f"[{label}] FAIL — check string missing: {chk[:70]!r}")
    return new + "".join(banners)


def note_suffix(note):
    return f" | [Corrected {D}, {AUDIT_REF}] {note}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")
    check_targets()

    print("=" * 72); print("PHASE 1 — validation / dry run"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    sec_ops, skipped = [], 0
    for (eid, name), op in SECTION_OPS.items():
        row = cur.execute("SELECT id, content FROM sections WHERE entry_id=? AND section_name=?", (eid, name)).fetchone()
        if row is None:
            raise SystemExit(f"[{eid}.{name}] ABORT — section not found")
        new = plan_section(row[1], op, f"{eid}.{name}")
        if new is None:
            skipped += 1; continue
        sec_ops.append((row[0], f"{eid}.{name}", new))
        print(f"  [{eid}.{name}] plan — {len(op['replace'])} replace, {len(op['banners'])} banner(s), "
              f"{len(row[1])} → {len(new)} chars")
    link_ops = []
    for lid, s, t, must, new_text in LINK_FIXES:
        row = cur.execute("SELECT source_id, target_id, description FROM links WHERE id=?", (lid,)).fetchone()
        if row is None or (row[0], row[1]) != (s, t):
            raise SystemExit(f"[links {lid}] ABORT — unexpected row {row!r}")
        desc = row[2]
        if desc.startswith(LINK_PREFIX):
            skipped += 1; continue
        if must not in desc:
            raise SystemExit(f"[links {lid}] FAIL — expected text missing: {must!r}")
        link_ops.append((lid, LINK_PREFIX + new_text + f' Previously: "{desc}"'))
        print(f"  [links {lid} {s}->{t}] plan")
    conn.close()

    hc = sqlite3.connect(WIKI_HISTORY_DB)
    anc_ops = []
    for aid, eid, ident, sets, note in ANCHOR_UPDATES + [(a, e, i, {}, n) for a, e, i, n in ANCHOR_NOTES]:
        row = hc.execute("SELECT entry_id, identifier, notes FROM external_anchors WHERE id=?", (aid,)).fetchone()
        if row is None or row[0] != eid:
            raise SystemExit(f"[anchor {aid}] ABORT — unexpected row {row!r}")
        if AUDIT_REF in (row[2] or ""):
            if row[1] != sets.get("identifier", ident):
                raise SystemExit(f"[anchor {aid}] ABORT — note applied but identifier {row[1]!r}")
            skipped += 1; continue
        if row[1] != ident:
            raise SystemExit(f"[anchor {aid}] ABORT — identifier {row[1]!r}, expected {ident!r}")
        new_sets = dict(sets); new_sets["notes"] = (row[2] or "") + note_suffix(note)
        anc_ops.append((aid, new_sets)); print(f"  [anchor {aid} {eid}] plan — {', '.join(new_sets)}")
    anc_ins = [a for a in ANCHOR_INSERTS if not hc.execute(
        "SELECT 1 FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND relationship=?",
        (a["entry_id"], a["source"], a["identifier"], a["relationship"])).fetchone()]
    for a in anc_ins:
        print(f"  [anchor + {a['entry_id']} {a['identifier']}] plan")
    pending_cal = [c for c in CALIBRATIONS if not hc.execute(
        "SELECT 1 FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
        (c[0], c[3], c[4])).fetchone()]
    for c in pending_cal:
        prev = hc.execute("SELECT confidence FROM claim_status_latest WHERE entity_id=?", (c[0],)).fetchone()
        if prev is None or prev[0] != c[2]:
            raise SystemExit(f"[calibration {c[0]}] ABORT — latest label {prev!r}, row would change it to {c[2]!r}")
    hc.close()
    print(f"\n  {len(sec_ops)} section writes, {len(link_ops)} link writes, {len(anc_ops)} anchor updates, "
          f"{len(anc_ins)} anchor inserts, {len(pending_cal)} calibration rows; {skipped} targets already applied")

    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply."); return

    print("\n" + "=" * 72); print("PHASE 2 — apply"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    try:
        for sid, label, new in sec_ops:
            cur.execute("UPDATE sections SET content=? WHERE id=?", (new, sid))
            if cur.rowcount != 1: raise SystemExit(f"[{label}] rowcount {cur.rowcount}")
        for lid, new in link_ops:
            cur.execute("UPDATE links SET description=? WHERE id=?", (new, lid))
            if cur.rowcount != 1: raise SystemExit(f"[links {lid}] rowcount {cur.rowcount}")
        conn.commit()
    except BaseException:
        conn.rollback(); conn.close(); raise
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        for aid, sets in anc_ops:
            cols = ", ".join(f"{k}=?" for k in sets)
            n = hc.execute(f"UPDATE external_anchors SET {cols} WHERE id=?", (*sets.values(), aid)).rowcount
            if n != 1: raise SystemExit(f"[anchor {aid}] rowcount {n}")
        for a in anc_ins:
            hc.execute("""INSERT INTO external_anchors (entry_id, source, identifier, revision_id, title, tier,
                          source_stability_class, relationship, canonical_role, verified_date, verified_by_session,
                          confidence, notes) VALUES (?,?,?,NULL,?,?,?,?,?,?,?,?,?)""",
                       (a["entry_id"], a["source"], a["identifier"], a["title"], a["tier"], a["stability"],
                        a["relationship"], a["role"], D, AUDIT_REF, a["confidence"], a["notes"]))
        for row in pending_cal:
            hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date,
                          audit_ref, short_status, rationale) VALUES (?,?,?,?,?,?,?)""", row)
        hc.commit()
    except BaseException:
        hc.rollback(); hc.close(); raise
    hc.close()
    print(f"  wrote {len(sec_ops)} sections, {len(link_ops)} links, {len(anc_ops)} anchor updates, "
          f"{len(anc_ins)} anchor inserts, {len(pending_cal)} calibration rows")

    print("\n" + "=" * 72); print("PHASE 3 — read-back verification"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    bad = [label for sid, label, new in sec_ops
           if cur.execute("SELECT content FROM sections WHERE id=?", (sid,)).fetchone()[0] != new]
    bad += [f"links:{lid}" for lid, new in link_ops
            if cur.execute("SELECT description FROM links WHERE id=?", (lid,)).fetchone()[0] != new]
    for (eid, name), op in SECTION_OPS.items():
        c = cur.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (eid, name)).fetchone()[0]
        if plan_section(c, op, f"{eid}.{name}") is not None:
            bad.append(f"not-applied:{eid}.{name}")
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for aid, sets in anc_ops:
        got = hc.execute(f"SELECT {', '.join(sets)} FROM external_anchors WHERE id=?", (aid,)).fetchone()
        if tuple(got) != tuple(sets.values()):
            bad.append(f"anchor:{aid}")
    for a in ANCHOR_INSERTS:
        if hc.execute("SELECT COUNT(*) FROM external_anchors WHERE entry_id=? AND source=? AND identifier=? AND "
                      "relationship=?", (a["entry_id"], a["source"], a["identifier"], a["relationship"])).fetchone()[0] != 1:
            bad.append(f"anchor+:{a['identifier']}")
    for c in CALIBRATIONS:
        got = hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? "
                         "AND calibration_date=? AND audit_ref=?", (c[0], c[3], c[4])).fetchone()
        if got != (c[2], c[5]):
            bad.append(f"cal:{c[0]}")
    hc.close()
    if bad:
        raise SystemExit(f"Post-write drift: {bad}")
    print(f"  verified: {len(sec_ops)} sections, {len(link_ops)} links, {len(anc_ops)} anchor updates, "
          f"{len(ANCHOR_INSERTS)} anchor inserts, {len(CALIBRATIONS)} calibration rows; all {len(SECTION_OPS)} "
          f"section targets read as applied")


if __name__ == "__main__":
    main()
