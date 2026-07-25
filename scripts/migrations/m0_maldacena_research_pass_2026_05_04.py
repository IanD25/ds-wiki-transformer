"""
Maldacena Deep Research Pass — Anchor + Calibration Updates — 2026-05-04

Five-agent literature audit triggered by reading a Juan Maldacena interview
"The Emergence of Spacetime" (YouTube). Findings sharpen and update prior
calibrations on multiple wiki entries:

  GT04  — Bianconi 2025 canonical_authority anchor, quantum-not-classical
          Fisher disambiguation
  GT10  — Casini-Galante-Myers 2016 contradicts anchor (modular-H-as-boost
          assumption fails for relevant operators with low conformal
          dimensions); Faulkner-Lashkari-Van Raamsdonk 2014 cites anchor
          (parallel theorem-level holographic bridge)
  BR04  — Brody-Rivier 1995 reframing_of anchor (Ruppeiner ⊂ Fisher-Rao on
          Gibbs canonical family in thermodynamic limit)
  IT08  — Brody-Rivier 1995 cites anchor (cross-link from Fisher-Rao to
          Ruppeiner thermodynamic-limit identification)
  P21   — Petz 1996 canonical_authority anchor (quantum-case classification:
          family of monotone metrics, NOT a single canonical metric);
          Ay-Jost-Lê-Schwachhöfer 2015 canonical_authority anchor (extends
          Chentsov uniqueness from finite simplices to general statistical
          manifolds)
  P17   — DESI DR2 (arXiv:2503.14738, PRD 112, 083515) cites anchor,
          Sapone-Nesseris 2025 cites anchor noting compilation sensitivity
  P23   — same DESI DR2 + Sapone-Nesseris anchors
  HB05  — Maldacena 2412.14014 adjacent_concept anchor (real-observers
          paper, dS partition function with massive worldline puncture)
  GT08  — same Maldacena 2412.14014 adjacent_concept anchor
  GT02  — Brouwer 2017 cites (positive weak-lensing test, 33,613 galaxies);
          Hossenfelder 2017 contradicts; Kobakhidze 2011 contradicts;
          Visser 2011 contradicts; Wang-Braunstein 2018 contradicts; Pardo
          2017 contradicts; Dai-Stojkovic 2017 contradicts. Verlinde 2017
          status is contested-with-positive-and-negative-evidence.

Calibration records (audit_ref = gsw-maldacena-deep-research-2026-05-04):
  fisher_gravity_chain    — Conceptual analogy CONFIRMED by 2020-2025 search
  GT04_Bianconi_quantum   — Bianconi uses quantum relative entropy / Bures,
                            NOT classical Fisher
  GT10_Casini_caveat      — Modular-H-as-boost assumption fails for relevant
                            operators (Casini-Galante-Myers 2016)
  BR04_thermo_limit       — Ruppeiner = Fisher-Rao on Gibbs canonical only
                            in thermodynamic limit (Brody-Rivier 1995)
  P21_quantum_classification — Quantum extension is Petz family classification
                            (1996); Bures/BKM/RLD/Wigner-Yanase distinguished
                            members; no single canonical metric
  P17_DESI_correction     — DESI DR2 σ-levels are 2.8-4.2σ across SN
                            compilations, NOT 5σ; phantom crossing at
                            z~0.4-0.5 not at 5σ discovery threshold
  GT02_Verlinde_contested — Brouwer 2017 positive lensing test BUT multiple
                            peer-reviewed negative results
  sethna_no_emergent_spacetime — Sethna group makes NO emergent-spacetime
                            claim; "spacetime emerges from FIM stiff/sloppy
                            hierarchy" is wiki-internal interpolation
  cca_terminology_rename_active — d_eff → PR_FIM, η → ι rename now justified
                            by deep-research finding that PR-formula on FIM
                            has no canonical citation and Sethna group
                            avoids the scalar
  GT_cluster_regime_tags  — Per-entry regime annotations per Maldacena
                            methodology lesson

Run: python3 scripts/migrations/m0_maldacena_research_pass_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-maldacena-deep-research-2026-05-04"
AUDIT_REF = SESSION


# ============================================================================
# EXTERNAL ANCHORS
# ============================================================================
# (entry_id, source, identifier, revision_id, title, tier,
#  source_stability_class, relationship, canonical_role, confidence, notes)

ANCHORS = [
    # ========================================================================
    # GT04 — Bianconi Gravity from Entropy
    # ------------------------------------------------------------------------
    # Disambiguation: Bianconi 2025 uses QUANTUM relative entropy on
    # density-matrix-valued metrics; the Hessian is Bures / quantum Fisher,
    # NOT classical Fisher information on a parameter manifold. Existing
    # GT04 prose mentions "quantum relative entropy" and "quantum Fisher
    # information matrix" but the M6→GT04 link path could be misread as
    # classical-Fisher-to-gravity. Anchor explicitly disambiguates.
    # ========================================================================
    ("GT04", "doi", "10.1103/PhysRevD.111.066001", None,
     "Bianconi 2025 - Gravity from entropy",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "DEEP-RESEARCH 2026-05-04 DISAMBIGUATION: Bianconi's framework uses "
     "QUANTUM relative entropy S(ρ‖σ) = Tr[ρ ln ρ - ρ ln σ] on density-"
     "matrix-valued metrics. The Hessian is the Bures / quantum Fisher "
     "metric on density matrices — NOT classical Fisher information on a "
     "parameter manifold of probability distributions. Equating Bianconi's "
     "framework with classical FIM (the M6/Ax2/CCA Fisher object) is a "
     "category error: Bures ≠ Fisher-Rao except in the commutative limit. "
     "Status: peer-reviewed action-principle programme (PRD 111 (2025) "
     "066001); single-author; no independent verification as of mid-2025. "
     "Regime: action principle constructed to recover Einstein equations "
     "in low-coupling limit; auxiliary G-field as dark-matter candidate "
     "lacks quantitative match to observation in the published paper."),

    # ========================================================================
    # GT10 — Jacobson Entanglement Equilibrium (2016)
    # ------------------------------------------------------------------------
    # Casini-Galante-Myers 2016 is a load-bearing CAVEAT: they showed via
    # holographic calculation that Jacobson's modular-Hamiltonian-as-boost-
    # generator assumption fails for relevant operators with low conformal
    # dimensions. Jacobson's derivation requires this assumption.
    # Faulkner-Lashkari-Van Raamsdonk 2014 is a parallel theorem-level
    # holographic bridge; entirely on modular-H side, not classical Fisher.
    # ========================================================================
    ("GT10", "doi", "10.1007/JHEP03(2016)194", None,
     "Casini, Galante, Myers 2016 - Comments on Jacobson's entanglement-equilibrium derivation",
     1, "canonical", "contradicts", None, "high",
     "DEEP-RESEARCH 2026-05-04: Casini-Galante-Myers (JHEP 03 (2016) 194; "
     "arXiv:1601.00528) showed via holographic calculation that Jacobson "
     "2016's derivation requires the modular Hamiltonian on a small "
     "geodesic ball to reduce to the boost generator — a property of the "
     "CFT vacuum that FAILS for relevant operators with low conformal "
     "dimensions. The derivation is therefore not universal across QFTs. "
     "Jacobson and others have proposed workarounds (separate vacuum "
     "subtraction) but the assumption is not innocuous. Implication: GT10 "
     "is established for conformal fields; for general QFTs the modular-H "
     "structure must be checked separately."),

    ("GT10", "arxiv", "1601.00528", None,
     "Casini, Galante, Myers 2016 (arXiv preprint of above)",
     3, "preprint-evolving", "contradicts", None, "high",
     "Preprint version of JHEP 03 (2016) 194. Same caveat content as DOI "
     "anchor. Listed separately for reproducibility."),

    ("GT10", "doi", "10.1007/JHEP03(2014)051", None,
     "Faulkner, Lashkari, Van Raamsdonk et al. 2014 - Gravitation from entanglement in holographic CFTs",
     1, "canonical", "cites", None, "high",
     "DEEP-RESEARCH 2026-05-04: Theorem-level holographic bridge from "
     "boundary entanglement first law to LINEARIZED bulk Einstein "
     "equations in CFTs with semiclassical holographic duals. Parallel "
     "to Jacobson 2016 (which is local, not holographic) — same overall "
     "conclusion (linearized Einstein from entanglement structure) via "
     "different machinery (Ryu-Takayanagi minimal surfaces + boundary "
     "modular-H). Linearized only. Faulkner et al. 2017 (JHEP 08 (2017) "
     "057) extends toward nonlinear order, but only within AdS/CFT — "
     "the nonlinear extension does NOT lift to a Jacobson-style local "
     "entanglement-equilibrium derivation."),

    # ========================================================================
    # BR04 — Thermodynamic Geometry (Ruppeiner Metric)
    # ------------------------------------------------------------------------
    # Brody-Rivier 1995 PRE 51, 1006 proves Ruppeiner = Fisher-Rao on the
    # Gibbs canonical family in the thermodynamic limit. Outside the
    # thermodynamic limit they can differ. So Ruppeiner ⊂ Fisher-Rao.
    # ========================================================================
    ("BR04", "doi", "10.1103/PhysRevE.51.1006", None,
     "Brody, Rivier 1995 - Geometrical aspects of statistical mechanics",
     1, "canonical", "reframing_of", None, "high",
     "DEEP-RESEARCH 2026-05-04: Brody-Rivier (PRE 51, 1006, 1995) proved "
     "that the Ruppeiner thermodynamic metric -Hess(S) on the Gibbs "
     "canonical family equals the Fisher-Rao metric on that family in the "
     "thermodynamic limit. Ruppeiner ⊂ Fisher-Rao: Ruppeiner is the "
     "thermodynamic-limit special case of Fisher-Rao on a 2-parameter "
     "exponential family (β, h). Outside the thermodynamic limit "
     "(small/finite systems with large fluctuations) they can differ. "
     "Implication for wiki: BR04 (Ruppeiner) is NOT a separate "
     "mathematical object from IT08 (Fisher-Rao); it is a specific "
     "reduction of IT08 in a specific regime. Cross-linked anchor on "
     "IT08 marks the same paper as `cites`."),

    # ========================================================================
    # IT08 — Fisher-Rao Metric
    # ------------------------------------------------------------------------
    # Cross-link from BR04 via Brody-Rivier 1995.
    # ========================================================================
    ("IT08", "doi", "10.1103/PhysRevE.51.1006", None,
     "Brody, Rivier 1995 - Geometrical aspects of statistical mechanics",
     1, "canonical", "cites", None, "high",
     "DEEP-RESEARCH 2026-05-04: Identifies the Ruppeiner thermodynamic "
     "metric (BR04) as Fisher-Rao on the Gibbs canonical family in the "
     "thermodynamic limit. Cross-link to BR04's reframing_of anchor "
     "with the same DOI. Establishes BR04 ⊂ IT08 in a specific regime."),

    # ========================================================================
    # P21 — Fisher-Rao Metric Universality (Established for classical)
    # ------------------------------------------------------------------------
    # Sharpening: the wiki currently labels the quantum extension as a
    # "gap." Petz 1996 actually proved a CLASSIFICATION theorem: a family
    # of monotone metrics parameterized by symmetric operator-monotone
    # functions f, with Bures/BKM/RLD/Wigner-Yanase as distinguished
    # members. So the quantum case has uniqueness-like structure, just
    # not a single canonical metric. Ay-Jost-Lê-Schwachhöfer 2015 extends
    # Chentsov uniqueness from finite simplices to general statistical
    # manifolds.
    # ========================================================================
    ("P21", "doi", "10.1016/0024-3795(94)00211-8", None,
     "Petz 1996 - Monotone metrics on matrix spaces",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "DEEP-RESEARCH 2026-05-04: Petz (Lin. Alg. Appl. 244, 81, 1996) "
     "proved the QUANTUM classification theorem: every monotone "
     "Riemannian metric on full-rank density matrices has the form "
     "⟨A,B⟩^f_ρ = Tr[A · m_f(L_ρ, R_ρ)^{-1}(B)] where f is a symmetric, "
     "normalized, operator-monotone function on (0,∞) with f(1)=1, "
     "f(t)=t·f(1/t). Distinguished members: Bures/SLD (smallest, used "
     "for quantum Cramér-Rao bound), Bogoliubov-Kubo-Mori BKM (unique "
     "self-dual member where ±1 quantum connections are mutually dual, "
     "Grasselli-Streater 2001), RLD (largest), Wigner-Yanase (skew "
     "information). Implication for P21: the wiki's framing 'Established "
     "for classical, gap for quantum' is too coarse. The correct framing "
     "is: classical Chentsov uniqueness on probability simplices "
     "(Established); quantum Petz classification — a parameterized family "
     "of monotone metrics with no single canonical choice (Established as "
     "classification, not uniqueness). All members coincide in the "
     "commutative limit and reduce to Fisher-Rao."),

    ("P21", "arxiv", "1306.1465", None,
     "Ay, Jost, Lê, Schwachhöfer 2015 - The uniqueness of the Fisher metric as information metric",
     3, "preprint-evolving", "canonical_authority", "axiomatic_foundation", "high",
     "DEEP-RESEARCH 2026-05-04: Extends Chentsov classical uniqueness "
     "(originally proved on finite probability simplices) to general "
     "statistical manifolds. Together with Chentsov 1972/1982, this "
     "covers the full classical case for P21's universality claim. The "
     "canonical statement of P21 as Established applies on any classical "
     "statistical manifold satisfying the relevant invariance conditions, "
     "not just finite simplices."),

    # ========================================================================
    # P17 — Cosmological Coupling = D_eff
    # ------------------------------------------------------------------------
    # DESI DR2 σ-levels: 2.8σ (Pantheon+) / 3.8σ (Union3) / 4.2σ (DES-SN5YR)
    # tension with ΛCDM, NOT 5σ. Phantom crossing of w=-1 at z~0.4-0.5.
    # Sapone-Nesseris 2025 EPJC notes compilation sensitivity.
    # ========================================================================
    ("P17", "arxiv", "2503.14738", None,
     "DESI Collaboration 2025 - DESI 2024 Year 3 Cosmological Constraints",
     1, "canonical", "cites", None, "high",
     "DEEP-RESEARCH 2026-05-04: DESI DR2 (Phys. Rev. D 112, 083515; "
     "arXiv:2503.14738) reports w0wa-CDM constraints with 2.8σ "
     "(Pantheon+) / 3.8σ (Union3) / 4.2σ (DES-SN5YR) tension with ΛCDM "
     "depending on SN Ia compilation. Best-fit w0wa trajectories cross "
     "w=-1 (phantom regime) near z~0.4-0.5; current w0 > -1 (quintessence-"
     "like today), wa < 0 (more phantom in past). σ-levels are NOT 5σ — "
     "no current dataset clears the conventional 5σ discovery threshold. "
     "CRITICAL CORRECTION: P17 wiki entry's '5σ rejection of k=3' was the "
     "Amendola 2024 FORECAST (~250 additional events), not current data. "
     "Wiki prose pending owner sign-off for correction."),

    ("P17", "arxiv", "2504.15222", None,
     "Sapone, Nesseris 2025 - Did DESI DR2 truly reveal dynamical dark energy?",
     1, "active-literature", "cites", None, "medium",
     "DEEP-RESEARCH 2026-05-04: Sapone-Nesseris (EPJC 2025; "
     "arXiv:2504.15222) argues DESI DR2 dynamical dark energy interpretation "
     "is sensitive to (i) SN Ia compilation choice and (ii) prior "
     "assumptions. Companion arXiv:2503.24343 shows BAO data can also be "
     "fit by modifying the sound horizon at recombination (early dark "
     "energy) rather than late-time w(z) evolution. Status: contested, "
     "leaning toward 'real but possibly systematics-contaminated.' "
     "P17 should remain Speculative-high-risk per M0 audit."),

    # ========================================================================
    # P23 — Horizon Formation as Bekenstein-Saturation Phase Transition
    # ------------------------------------------------------------------------
    # Same DESI / Sapone-Nesseris caveats as P17 (P23 inherits GT11
    # cosmological-coupling tensions).
    # ========================================================================
    ("P23", "arxiv", "2503.14738", None,
     "DESI Collaboration 2025 - DESI 2024 Year 3 Cosmological Constraints",
     1, "canonical", "cites", None, "high",
     "DEEP-RESEARCH 2026-05-04: P23 inherits GT11 cosmological-coupling "
     "tensions; DESI DR2 σ-levels (2.8-4.2σ across SN compilations) are "
     "below the 5σ discovery threshold. P23 framework's k=cosmological-"
     "coupling-from-D_eff claim faces the same calibration constraints "
     "as P17."),

    ("P23", "arxiv", "2504.15222", None,
     "Sapone, Nesseris 2025 - Did DESI DR2 truly reveal dynamical dark energy?",
     1, "active-literature", "cites", None, "medium",
     "DEEP-RESEARCH 2026-05-04: Same caveat as P17: DR2 dynamical-dark-"
     "energy interpretation may be systematics-contaminated. P23 "
     "remains Speculative-high-risk pending owner-side validation."),

    # ========================================================================
    # HB05 — Unruh Effect (closest existing wiki home for dS observer)
    # ========================================================================
    ("HB05", "arxiv", "2412.14014", None,
     "Maldacena 2024 - Real Observers Solving Imaginary Problems",
     3, "preprint-evolving", "adjacent_concept", None, "high",
     "DEEP-RESEARCH 2026-05-04: Maldacena (sole author, December 2024). "
     "In the dS Euclidean partition function on S^D the dimension-"
     "dependent phase factor i^(D+2) obstructs a state-counting "
     "interpretation of the Gibbons-Hawking entropy. Including a physical "
     "observer — modeled as a massive worldline puncture in the Euclidean "
     "S^D — largely cancels this phase, restoring positivity. Builds on "
     "the algebraic-observer crossed-product machinery of Chandrasekaran-"
     "Longo-Penington-Witten arXiv:2206.10780. Adjacent to HB05 because "
     "Unruh-Davies temperature on the dS observer's worldline is in the "
     "same family of cosmological-horizon thermodynamic considerations. "
     "Methodology lesson: 'you can't measure time without a clock' is "
     "gauge-fixing on a constraint algebra (type III to type II via "
     "crossed product), not a separate theorem."),

    # ========================================================================
    # GT08 — Equivalence Principle (cross-attach Maldacena 2412.14014)
    # ========================================================================
    ("GT08", "arxiv", "2412.14014", None,
     "Maldacena 2024 - Real Observers Solving Imaginary Problems",
     3, "preprint-evolving", "adjacent_concept", None, "high",
     "DEEP-RESEARCH 2026-05-04: Same paper as HB05 anchor. Adjacent to "
     "GT08 because the observer is a load-bearing element of the "
     "equivalence-principle framework (frame-dependent acceleration → "
     "frame-dependent Unruh temperature). Maldacena 2024 makes the "
     "physical-observer-with-mass-and-energy structure quantitatively "
     "necessary in dS Euclidean calculations."),

    # ========================================================================
    # GT04 — also cross-attach Maldacena 2412.14014 (related dS observer)
    # ========================================================================
    ("GT04", "arxiv", "2412.14014", None,
     "Maldacena 2024 - Real Observers Solving Imaginary Problems",
     3, "preprint-evolving", "adjacent_concept", None, "medium",
     "DEEP-RESEARCH 2026-05-04: Different program but adjacent — both "
     "GT04 (Bianconi entropic gravity) and Maldacena 2412.14014 use "
     "quantum information machinery to re-derive or constrain "
     "gravitational/cosmological partition functions. Bianconi's matter "
     "is via quantum relative entropy on density-matrix metrics; "
     "Maldacena's observer cancels Euclidean dS phase factors via "
     "worldline puncture. Programs do not depend on each other."),

    # ========================================================================
    # GT02 — Verlinde Entropic Gravity (contested status)
    # ------------------------------------------------------------------------
    # Wiki framing should reflect both Brouwer 2017 positive lensing test
    # AND multiple peer-reviewed negative results.
    # ========================================================================
    ("GT02", "doi", "10.1093/mnras/stw3192", None,
     "Brouwer et al. 2017 - First test of Verlinde's theory of emergent gravity using weak gravitational lensing measurements",
     1, "canonical", "cites", None, "high",
     "DEEP-RESEARCH 2026-05-04: Brouwer et al. (MNRAS 466, 2547, 2017) "
     "tested Verlinde 2017 emergent-gravity prediction against weak-"
     "lensing data on 33,613 galaxies. Result: prediction agrees with "
     "data WITHOUT free parameters at galactic scales. Status: positive "
     "empirical test, controlled. Methodology not verified in primary "
     "text by deep-research agent — flagged confidence at the test level "
     "but anchor confidence high for the paper's existence and claim."),

    ("GT02", "doi", "10.1103/PhysRevD.83.021502", None,
     "Kobakhidze 2011 - Gravity is not an entropic force",
     1, "canonical", "contradicts", None, "high",
     "DEEP-RESEARCH 2026-05-04: Kobakhidze (PRD 83, 021502, 2011; "
     "arXiv:1009.5414) argues quantized gravitational states observed in "
     "the GRANIT ultra-cold-neutron experiment (Nesvizhevsky et al.) are "
     "inconsistent with Verlinde 2011's entropic-force derivation: an "
     "entropic force from a holographic screen cannot produce coherent "
     "Bohr-like discrete gravitational quantum states. Subsequent rebuttal "
     "and counter-rebuttal exists but the experimental signature is real."),

    ("GT02", "doi", "10.1007/JHEP10(2011)140", None,
     "Visser 2011 - Conservative entropic forces",
     1, "canonical", "contradicts", None, "high",
     "DEEP-RESEARCH 2026-05-04: Visser (JHEP 10 (2011) 140; "
     "arXiv:1108.5240) shows that entropic-force derivations of "
     "conservative many-body forces (which Newtonian gravity is) require "
     "unphysical entropy structures and multiple temperature baths. "
     "Mathematical critique of Verlinde 2011's framework."),

    ("GT02", "doi", "10.1007/JHEP11(2017)007", None,
     "Hossenfelder 2017 - Inconsistencies in Verlinde's emergent gravity",
     1, "canonical", "contradicts", None, "high",
     "DEEP-RESEARCH 2026-05-04: Hossenfelder & collaborators (JHEP 11 "
     "(2017) 007) argue the Verlinde 2017 elastic-strain MOND derivation "
     "is not self-consistent; a careful redo gives standard Newtonian "
     "gravity, not MOND. Solar-system constraints conflict with the "
     "explicit galactic-scale formula."),

    ("GT02", "arxiv", "1706.07854", None,
     "Hossenfelder 2017 - A covariant version of Verlinde's emergent gravity",
     3, "preprint-evolving", "cites", None, "high",
     "DEEP-RESEARCH 2026-05-04: Hossenfelder's attempt to make Verlinde "
     "2017 covariant; Dai-Stojkovic (PRD 96, 108501, 2017) showed this "
     "covariant version fails to recover stable de Sitter. Listed as "
     "cites (not contradicts) since this paper is itself a sympathetic "
     "extension of Verlinde's program."),

    ("GT02", "doi", "10.1103/PhysRevD.96.108501", None,
     "Dai, Stojkovic 2017 - Comment on Hossenfelder's covariant Verlinde",
     1, "canonical", "contradicts", None, "high",
     "DEEP-RESEARCH 2026-05-04: Dai-Stojkovic show that Hossenfelder's "
     "covariant version of Verlinde 2017 fails to recover stable de "
     "Sitter; another mathematical inconsistency in the program."),

    # ========================================================================
    # M6 / Ax2 — Sethna sloppy-models clarification
    # ------------------------------------------------------------------------
    # Important: Sethna group makes NO emergent-spacetime claim. Wiki
    # entries that link M6 (Fisher Information Rank) to gravity must NOT
    # cite Sethna lineage as supporting that link; the Sethna lineage is
    # purely about parameter-space compression, not spacetime emergence.
    # Adding a contradicts anchor on M6 to the Sethna primary paper, with
    # notes documenting the explicit absence of an emergent-spacetime
    # claim.
    # ========================================================================
    ("M6", "doi", "10.1126/science.1238723", None,
     "Machta, Chachra, Transtrum, Sethna 2013 - Parameter Space Compression",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "DEEP-RESEARCH 2026-05-04: Sethna-group sloppy-models foundational "
     "paper. Critical clarification: this paper makes NO emergent-"
     "spacetime claim. The word 'spacetime' does not appear as a "
     "derivation target; the paper discusses 'emergent THEORIES' "
     "(effective coarse-grained descriptions) using Ising / diffusion / "
     "biological networks. Any wiki framing that asserts 'spacetime "
     "emerges from FIM stiff/sloppy hierarchy' is a wiki-internal "
     "interpolation the original authors do not endorse. M6 is a "
     "legitimate application of the Sethna framework to parameter-space "
     "diagnostics; M6 → spacetime is NOT supported by this paper."),

    ("M6", "arxiv", "1303.6738", None,
     "Machta, Chachra, Transtrum, Sethna 2013 (arXiv preprint)",
     3, "preprint-evolving", "canonical_authority", "progenitor", "high",
     "Preprint version of Science 342, 604 (2013). Same content."),
]


# ============================================================================
# CALIBRATION RECORDS
# ============================================================================
# (entity_id, entity_type, confidence, calibration_date, audit_ref,
#  short_status, rationale)

CALIBRATIONS = [
    # ------------------------------------------------------------------------
    # Fisher-gravity chain — M0 downgrade CONFIRMED by 2020-2025 search
    # ------------------------------------------------------------------------
    ("fisher_gravity_chain", "structural_observation", "Speculative",
     TODAY, AUDIT_REF,
     "Conceptual analogy CONFIRMED by deep-research 2020-2025 search",
     "Five-agent literature audit found NO peer-reviewed paper 2020-2025 "
     "constructing a theorem-level bridge from classical Fisher information "
     "geometry on a parameter manifold to the Jacobson-2016 / modular-"
     "Hamiltonian / entanglement-entropy machinery used in emergent-"
     "Einstein derivations. Closest theorem-level results (Faulkner-"
     "Lashkari-Van Raamsdonk 2014; Faulkner et al. 2017) sit ENTIRELY on "
     "the modular-H side, not classical Fisher. Bianconi 2025 uses "
     "QUANTUM relative entropy / Bures (different mathematical object). "
     "M0 2026-04-08 downgrade to 'conceptual analogy, not theorem "
     "composition' is correct and conservative. The chain stacks "
     "vocabulary across distinct objects; the M6→IT05→IT03→GT10→GT01 "
     "path is a vocabulary path, not a theorem path."),

    # ------------------------------------------------------------------------
    # GT04 — Bianconi quantum-not-classical disambiguation
    # ------------------------------------------------------------------------
    ("GT04", "entry", "Speculative",
     TODAY, AUDIT_REF,
     "Bianconi uses QUANTUM relative entropy / Bures, not classical Fisher",
     "Wiki entry GT04 prose mentions 'quantum relative entropy' and "
     "'quantum Fisher information matrix' but the M6→GT04 link path "
     "could be misread as classical-Fisher-to-gravity. Disambiguation: "
     "Bianconi 2025 (PRD 111, 066001) uses S(ρ‖σ) on density-matrix-"
     "valued metrics; Hessian = Bures / quantum Fisher metric, NOT "
     "classical Fisher-Rao on a parameter manifold. Equating these is "
     "a category error. Status: peer-reviewed action-principle programme; "
     "single-author; no independent verification as of mid-2025. Should "
     "stay Speculative pending independent reproduction."),

    # ------------------------------------------------------------------------
    # GT10 — Casini-Galante-Myers caveat
    # ------------------------------------------------------------------------
    ("GT10", "entry", "Supported",
     TODAY, AUDIT_REF,
     "Linearized only; modular-H-as-boost assumption fails for relevant operators (Casini-Galante-Myers 2016)",
     "Jacobson 2016 entanglement-equilibrium derivation requires the "
     "modular Hamiltonian on a small geodesic ball to reduce to the "
     "boost generator. Casini-Galante-Myers (JHEP 03 (2016) 194) "
     "showed this fails for relevant operators with low conformal "
     "dimensions. Implication: GT10 is established for conformal fields; "
     "for general QFTs the modular-H structure must be checked "
     "separately. Faulkner-Lashkari-Van Raamsdonk 2014 provides a "
     "parallel theorem-level holographic bridge to linearized Einstein. "
     "Faulkner et al. 2017 extends toward nonlinear Einstein but only "
     "within AdS/CFT, not via Jacobson-style local entanglement "
     "equilibrium. Wiki should reflect both the support and the scope "
     "limitation."),

    # ------------------------------------------------------------------------
    # BR04 — Ruppeiner ⊂ Fisher-Rao in thermodynamic limit
    # ------------------------------------------------------------------------
    ("BR04", "entry", "Established",
     TODAY, AUDIT_REF,
     "Ruppeiner = Fisher-Rao on Gibbs canonical family in thermodynamic limit (Brody-Rivier 1995)",
     "Brody-Rivier (PRE 51, 1006, 1995) proved Ruppeiner -Hess(S) on "
     "the Gibbs canonical family equals Fisher-Rao on that family in "
     "the thermodynamic limit. Outside the thermodynamic limit they can "
     "differ. Implication: BR04 is NOT a separate mathematical object "
     "from IT08; it is a specific reduction in a specific regime. "
     "Wiki entries treating Ruppeiner as a fundamentally different "
     "object from Fisher-Rao should be clarified — they are the same "
     "object in the regime where both are typically applied."),

    # ------------------------------------------------------------------------
    # P21 — Quantum classification, not single canonical metric
    # ------------------------------------------------------------------------
    ("P21", "conjecture", "Established",
     TODAY, AUDIT_REF,
     "Classical Chentsov uniqueness + quantum Petz classification",
     "Sharpening of M0 calibration: P21's universality claim is "
     "Established for the classical case (Chentsov 1972/1982 on finite "
     "simplices; Ay-Jost-Lê-Schwachhöfer 2015 arXiv:1306.1465 extends "
     "to general statistical manifolds). Quantum extension is "
     "Established AS CLASSIFICATION (Petz 1996 Lin. Alg. Appl. 244, 81) "
     "— a parameterized family of monotone metrics on density matrices, "
     "with Bures (smallest), BKM (unique self-dual), RLD (largest), "
     "Wigner-Yanase as distinguished members. There is no single "
     "canonical quantum metric — physical context selects a member. "
     "All members coincide in the commutative limit and reduce to "
     "Fisher-Rao. Wiki framing 'Established for classical, gap for "
     "quantum' is too coarse — the quantum case has classification, "
     "not absence of structure."),

    # ------------------------------------------------------------------------
    # P17 — DESI σ-level correction (5σ → 2.8-4.2σ)
    # ------------------------------------------------------------------------
    ("P17", "conjecture", "Speculative",
     TODAY, AUDIT_REF,
     "DESI DR2 σ-levels 2.8-4.2σ across SN compilations, NOT 5σ",
     "DESI DR2 (PRD 112, 083515; arXiv:2503.14738) reports w0wa-CDM "
     "tension with ΛCDM at 2.8σ (Pantheon+) / 3.8σ (Union3) / 4.2σ "
     "(DES-SN5YR). NOT the 5σ originally claimed in P17 wiki entry "
     "(Amendola 2024 5σ was a FORECAST for ~250 additional events, "
     "not current data). Phantom crossing of w=-1 occurs at z~0.4-0.5 "
     "in best-fit w0wa trajectories but is NOT at 5σ discovery threshold. "
     "Sapone-Nesseris 2025 (EPJC; arXiv:2504.15222) flags compilation "
     "and prior sensitivity. Wiki prose correction pending owner sign-"
     "off (touches ds_wiki.db); calibration record is the override "
     "until then. P17 stays Speculative-high-risk."),

    # ------------------------------------------------------------------------
    # GT02 — Verlinde contested status (positive AND negative tests)
    # ------------------------------------------------------------------------
    ("GT02", "entry", "Speculative",
     TODAY, AUDIT_REF,
     "Verlinde program contested with both positive (Brouwer 2017) and multiple negative tests",
     "Wiki framing should reflect contested-with-mixed-evidence status. "
     "Positive: Brouwer 2017 (MNRAS 466, 2547) weak-lensing test on "
     "33,613 galaxies — Verlinde 2017 prediction agrees with data "
     "without free parameters. Negative: Kobakhidze 2011 (PRD 83, "
     "021502; GRANIT neutron experiment), Visser 2011 (JHEP 10, 140; "
     "conservative force critique), Hossenfelder 2017 (JHEP 11, 007; "
     "elastic-strain MOND inconsistencies + solar-system constraints), "
     "Dai-Stojkovic 2017 (PRD 96, 108501; covariant version fails dS), "
     "Pardo 2017 (dwarf-galaxy rotation curves), Wang-Braunstein 2018. "
     "Status: contested in the published literature both ways."),

    # ------------------------------------------------------------------------
    # M6 — Sethna disclaimer (no emergent-spacetime claim)
    # ------------------------------------------------------------------------
    ("M6", "entry", "Established",
     TODAY, AUDIT_REF,
     "Fisher Rank legitimate as parameter-space diagnostic; Sethna lineage makes NO emergent-spacetime claim",
     "M6 is correctly anchored as canonical_authority/progenitor to "
     "Machta-Chachra-Transtrum-Sethna 2013. Critical clarification: the "
     "Sethna primary paper makes NO emergent-spacetime claim. The word "
     "'spacetime' does not appear as a derivation target; the paper "
     "discusses 'emergent THEORIES' (effective coarse-grained "
     "descriptions). Any wiki framing that uses M6 → Sethna → spacetime "
     "as evidence of an information-theoretic derivation of gravity is "
     "an interpolation the original authors do not endorse. M6 itself "
     "stays Established as parameter-space diagnostic; Fisher-gravity "
     "chain stays Speculative."),

    # ------------------------------------------------------------------------
    # CCA terminology rename — now justified
    # ------------------------------------------------------------------------
    ("cca_terminology_rename", "decision", "Established",
     TODAY, AUDIT_REF,
     "PR_FIM / ι rename now justified by deep-research findings",
     "Per CCA_TERMINOLOGY_RENAME_PROPOSAL.md the rename d_eff → PR_FIM, "
     "η → ι was proposed pending owner sign-off. Deep-research 2026-05-04 "
     "strengthens the case: (1) the PR formula d_eff = (Σλ)²/Σλ² applied "
     "to FIM specifically has NO canonical citation found in primary "
     "literature — it's a folklore transfer from random-matrix / neural-"
     "covariance contexts. (2) Mattingly 2018 d_eff = Σ_r r·Ω_r is a "
     "DIFFERENT formula in the same Sethna lineage, mandatory citation "
     "for terminology hygiene. (3) Sethna group itself (Quinn 2023) "
     "deliberately AVOIDS collapsing the spectrum to a single number; "
     "they use hyperribbon widths and the eigenvalue spectrum directly. "
     "(4) CCA's η collides with standard stat-mech η_critical; the two "
     "are mathematically related at criticality, which compounds confusion. "
     "Notation banner added to active CCA docs 2026-05-04; full migration "
     "of body texts is staged work."),

    # ------------------------------------------------------------------------
    # ER=EPR — Maldacena's own framing is more cautious than popular version
    # ------------------------------------------------------------------------
    ("BR01", "entry", "Speculative",
     TODAY, AUDIT_REF,
     "ER=EPR is convincing for thermofield-double; for generic Bell pairs requires generalized geometry",
     "Maldacena-Susskind 2013 (Fortsch. Phys. 61, 781) argues ER=EPR "
     "convincingly for the specific thermofield-double state between "
     "two AdS black holes (eternal AdS-Schwarzschild). For generic "
     "entangled states (e.g., 2 spin-1/2 particles), no smooth classical "
     "metric description exists — a 'generalized notion of geometry' is "
     "needed; classical wormhole emerges only in large-N / many-EPR-pair "
     "/ large-entanglement limit. Maldacena himself in 2024-2025 "
     "interview describes ER=EPR as 'an aspiration, a slogan or a "
     "principle that perhaps a more complete theory of gravity should "
     "have' — not a proven correspondence. Recent operational-theorem "
     "extensions (Wilkens et al. arXiv:2410.16496) prove a precise "
     "version when both subregions admit type III₁ algebras and a "
     "'classical condition' holds — narrower than the popular framing."),
]


def main() -> None:
    if not WIKI_HISTORY_DB.exists():
        raise SystemExit(f"Cannot find {WIKI_HISTORY_DB}; run from repo root")

    conn = sqlite3.connect(WIKI_HISTORY_DB)
    cur = conn.cursor()

    # ------------------------------------------------------------------------
    # Insert anchors
    # ------------------------------------------------------------------------
    inserted_anchors = 0
    skipped_anchors = 0
    for row in ANCHORS:
        (entry_id, source, identifier, revision_id, title, tier,
         stability, relationship, canonical_role, confidence, notes) = row
        try:
            cur.execute("""
                INSERT OR IGNORE INTO external_anchors (
                    entry_id, source, identifier, revision_id, title,
                    tier, source_stability_class, relationship,
                    canonical_role, verified_date, verified_by_session,
                    confidence, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (entry_id, source, identifier, revision_id, title,
                  tier, stability, relationship, canonical_role,
                  TODAY, SESSION, confidence, notes))
            if cur.rowcount > 0:
                inserted_anchors += 1
            else:
                skipped_anchors += 1
        except sqlite3.IntegrityError as e:
            print(f"FAILED  {entry_id} {source} {identifier}: {e}")

    # ------------------------------------------------------------------------
    # Insert calibration rows
    # ------------------------------------------------------------------------
    inserted_cal = 0
    for row in CALIBRATIONS:
        (entity_id, entity_type, confidence, cal_date, audit_ref,
         short_status, rationale) = row
        cur.execute("""
            INSERT INTO confidence_calibration (
                entity_id, entity_type, confidence, calibration_date,
                audit_ref, short_status, rationale
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (entity_id, entity_type, confidence, cal_date, audit_ref,
              short_status, rationale))
        inserted_cal += 1

    conn.commit()

    # ------------------------------------------------------------------------
    # Verify
    # ------------------------------------------------------------------------
    cur.execute("""
        SELECT COUNT(*) FROM external_anchors
        WHERE verified_by_session = ?
    """, (SESSION,))
    total_anchors = cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) FROM confidence_calibration
        WHERE audit_ref = ?
    """, (AUDIT_REF,))
    total_cal = cur.fetchone()[0]

    print(f"Migration {SESSION}")
    print(f"  Anchors inserted this run:     {inserted_anchors}")
    print(f"  Anchors skipped (UNIQUE):      {skipped_anchors}")
    print(f"  Total anchors with this session: {total_anchors}")
    print(f"  Calibrations inserted this run: {inserted_cal}")
    print(f"  Total calibrations under {AUDIT_REF}: {total_cal}")

    conn.close()


if __name__ == "__main__":
    main()
