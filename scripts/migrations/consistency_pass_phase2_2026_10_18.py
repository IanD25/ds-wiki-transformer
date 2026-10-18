"""
Consistency pass, Phase 2 — bring ds_wiki.db in line with the calibration record
— 2026-10-18 (audit_ref gsw-consistency-pass-2026-10-18). Mode A: no promotions.

WHY
---
The calibration table (wiki_history.db.confidence_calibration) holds the real,
post-M0 statuses. ds_wiki.db still showed pre-M0 state: conjectures.three_state
read "All States", "States 1→2→3", "State 2"…; only P12 had been touched
(2026-07-25). The claim text of P2, P5, P7, P8, P11, P21 never mentioned the
M0 findings. P17 and P23 still carried part of the Amendola/Cadoni wording that
M0's Fifth Addendum (2026-04-08) flagged as wrong.

WHAT THIS DOES
--------------
1. three_state, all 23 conjectures: PREFIX with the current label + pointer +
   pattern tag(s), then " | was: " + the stored value kept verbatim (P12's
   existing 2026-07-25 suffix included). Labels and pointers are taken from the
   latest calibration row per conjecture; tags from feedback_diagnostic_labels.
2. Status banner PREPENDED to the claim of P2, P5, P7, P8, P11, P21 (as
   directed) and of P6, P10, P12, P13, P15, P18, P19, P20 — the conjectures
   whose latest calibration contradicts the stored claim. Criteria used:
   (a) calibration finds the claim false or partially false (P12, P7);
   (b) contradicted by this project's own tests (P6, P7);
   (c) the claim asserts a derivation / uniqueness / superiority / provenance
       the calibration denies (P8 "uniquely predicted", P10 "better explained",
       P13 "derived from geometry alone", P15 "Landauer-class", P2/P5/P11
       restatements, P21 "common foundation");
   (d) the claim's scope exceeds the calibrated scope (P11 urban, P18–P20
       single-domain).
   Not bannered (calibration says untested/unproven, which a conjecture already
   implies): P1, P3, P4, P9, P14, P16, P22. P17/P23 get correction banners (3).
3. P17 / P23: apply the outstanding Fifth-Addendum rewording (Cadoni
   "generic" → "universal for regular BHs", 7 authors, own KS prefers k = 3;
   P23 "5σ rejection of k = 3" → ~3σ tension, 5σ was a forecast; P17's
   "LVK O4" line relabelled — Amendola 2024 uses GWTC-3, not O4). Original
   wording quoted in an appended dated banner, per the C1 precedent.
5. (owner-approved 2026-10-18) conjecture_summary.status: same prefix format as
   three_state ("<label> | was: <original>") on the 20 rows that exist; P18–P20
   have no summary row and none is created.
6. (owner-approved 2026-10-18) external_anchors ids 818 (P6) and 819 (P7), both
   `contradicts` Machta 2013: their notes appear swapped — each describes the
   other conjecture's claim — and P7's `contradicts` relationship is doubtful.
   A dated correction sentence is APPENDED to each note; original note text and
   the relationship field are unchanged.
4. Calibration: append-only. Rows ONLY for P17 and P23 (a correction is
   recorded; labels unchanged). No other label changes in this phase.

SAFETY
------
Dry run by default; --apply writes. Aborts on duplicate (table, row, column)
targets — each column gets exactly one composed write (the B2a lesson).
Idempotent: re-running after apply detects applied edits and skips them.
Post-write read-back verifies every written value.

Run:  python3 scripts/migrations/consistency_pass_phase2_2026_10_18.py
      python3 scripts/migrations/consistency_pass_phase2_2026_10_18.py --apply
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-consistency-pass-2026-10-18"
CAL_DATE = "2026-10-18"
SEP = " | was: "

# ─────────────────────────────────────────────────────────────────────────────
# 1. three_state prefixes (label — pointer [pattern tags] (calibration refs))
#    "run 2026-07-25" marks audit_refs whose "-2026-05-04" suffix is a session
#    label (see the 2026-10-18 date erratum in SESSION_HANDOVER_2026-05-04.md).
# ─────────────────────────────────────────────────────────────────────────────
THREE_STATE = {
    "P1": "Speculative — heterodox alternative to metric expansion with no unique prediction; null_hypothesis Hubble 1929 + Planck 2018 [heterodox-alternative-without-unique-prediction] (M0 2026-04-08)",
    "P2": "Speculative — restatement of West–Brown–Enquist 1997 in D_eff vocabulary; reframing_of WBE 1997 [restatement-in-new-vocabulary; untestable-without-owner-data] (M0 2026-04-08)",
    "P3": "Speculative — one operator with a free exponent per quantity; over/under-constraint audit never performed; null_hypothesis Adelberger et al. 2003 [over-parameterized-unification] (M0 2026-04-08)",
    "P4": "Speculative — refresh-rate reading not experimentally distinguished from the kinetic speed-limit reading; null_hypothesis Lehninger [heterodox-alternative-without-unique-prediction] (M0 2026-04-08)",
    "P5": "Supported as application — restatement of Machta et al. 2013 sloppy models; reframing_of Machta–Chachra–Transtrum–Sethna 2013 [restatement-in-new-vocabulary] (M0 2026-04-08; refined Phase E 2026-04-20)",
    "P6": "Speculative — contradicted by own Phase 1 tests: gap-based Fisher rank does not converge to the Hausdorff dimension, only the participation ratio does [contradicted-by-own-tests] (M0 2026-04-08; unchanged Phase E 2026-04-20)",
    "P7": "Speculative, partially falsified by own Phase 1 tests — the participation ratio fails monotonicity under every tested coarse-graining configuration; only gap-based rank on lattices under block-spin passes [contradicted-by-own-tests] (M0 2026-04-08)",
    "P8": "Speculative — restatement of Gefen–Mandelbrot–Aharony 1980 (exponents on fractal substrates) and Janke–Johnston–Kenna 2004 (FIM distinguishes transition order); reframing_of both [restatement-in-new-vocabulary] (M0 2026-04-08)",
    "P9": "Speculative — monitoring gate on quantum-complexity literature filed as a conjecture; belongs in the Q-series (not moved in this pass) [monitoring-gate-mislabeled-as-conjecture] (M0 2026-04-08)",
    "P10": "Speculative — running-ℏ / GUP reading is one of several consistent with hadron radii, no unique prediction; null_hypothesis Pohl et al. 2010 [heterodox-alternative-without-unique-prediction] (M0 2026-04-08)",
    "P11": "Speculative, scope bounded — reframing of Bettencourt et al. 2007 urban scaling; the D/(D+1) form is bounded ≤ 1, so it can fit sublinear infrastructure exponents only, not superlinear socioeconomic ones (~1.15); reframing_of Bettencourt et al. 2007 [restatement-in-new-vocabulary; untestable-without-owner-data] (M0 2026-04-08; gsw-scaling-corrections, run 2026-07-25)",
    "P12": "Falsified by structural bound — β(λ) ≤ 1 for every d_f and every λ in [0,1], so urban exponents ~1.15 are unreachable; biological half blocked, not falsified; null_hypothesis Newman 2005 [over-extension-beyond-formula-range; conditional-claim-with-unsatisfiable-antecedent] (gsw-scaling-queue, run 2026-07-25)",
    "P13": "Speculative — owner-acknowledged ansatz, not derived from geometry as the claim states; internal_construction (needs-review) [ansatz-without-derivation] (M0 2026-04-08)",
    "P14": "Speculative — needs vascular data not available at the required resolution; split into P14a (λ-free empirical core, runnable now) and P14b (Δλ mechanism, blocked) [untestable-without-owner-data] (M0 2026-04-08; gsw-scaling-queue, run 2026-07-25)",
    "P15": "Speculative — owner-acknowledged ansatz; financial-market evidence is analogy; its Landauer motivation is void under the λ definition resolved 2026-07-25; internal_construction (needs-review) [ansatz-without-derivation] (M0 2026-04-08; H3 gsw-kolokotrones-research, run 2026-07-25)",
    "P16": "Speculative — blocked at specification, not measurement: no biological learning problem has a specified model with a computable RLCT; Q4 is the real item [untestable-without-owner-data] (gsw-scaling-queue, run 2026-07-25)",
    "P17": "Speculative, high risk — owner-constructed D_eff = k bridge on the contested Farrah et al. 2023 result; GW ~3σ tension (Amendola et al. 2024, GWTC-3), Gaia BH and JWST AGN tensions; DESI DR2 2.8–4.2σ, not 5σ (M0 2026-04-08; M0 deep research 2026-04-08; gsw-maldacena 2026-05-04; prose corrected 2026-10-18)",
    "P18": "Supported as single-domain observation — US equities 2003–2025 only, not a general structural claim; internal_construction (needs-review) [single-domain-overgeneralization risk] (M0 2026-04-08)",
    "P19": "Supported as single-domain observation — US equities and the participation-ratio proxy only, not a cross-domain claim; internal_construction (needs-review) [single-domain-overgeneralization risk] (M0 2026-04-08)",
    "P20": "Supported as single-domain empirical fit — 19 AlphaEntropy A/B variants, ρ estimated qualitatively; not a theoretical principle; internal_construction (needs-review) [single-domain-overgeneralization risk] (M0 2026-04-08)",
    "P21": "Established for the classical theorem only — Chentsov uniqueness (canonical_authority Chentsov 1982, Amari 1985, Ay–Jost–Lê–Schwachhöfer 2015); the quantum case is Petz 1996's classification, with no single canonical metric; the cross-domain 'common foundation' step is not established (M0 2026-04-08; gsw-maldacena 2026-05-04)",
    "P22": "Speculative — individual lockout mechanisms are established; the trichotomy as an exhaustive classification is unproven; MBL thermodynamic-limit status open (M0 2026-04-08)",
    "P23": "Speculative, high risk — inherits the P17/GT11 tensions (Amendola/Cadoni figures corrected); no first-principles derivation links Bekenstein saturation to cosmological coupling [ansatz-without-derivation] (M0 2026-04-08; M0 deep research 2026-04-08; prose corrected 2026-10-18)",
}

# ─────────────────────────────────────────────────────────────────────────────
# 2. Claim banners (prepended; original claim follows unchanged)
# ─────────────────────────────────────────────────────────────────────────────
def banner(label, body):
    return (f"> **CURRENT STATUS — banner added {CAL_DATE} (`{AUDIT_REF}`).** "
            f"Label: **{label}**. {body} "
            f"*The claim as originally stated follows, unchanged.*\n\n")

BANNERS = {
    "P2": banner("Speculative (M0 2026-04-08)",
        "Reason: the functional form α = D_eff/(D_eff+1) is West, Brown & Enquist 1997; the 'tracks D_eff' framing is owner-constructed and adds no independent content [restatement-in-new-vocabulary]. A test needs vascular micro-CT data that does not exist at the required resolution [untestable-without-owner-data]. Related correction: C1's implied-D_eff column — what this formula yields when inverted on observed exponents — was retired on 2026-07-25 because two of its values exceed the embedding dimension. Anchor: `reframing_of` West, Brown & Enquist 1997, *Science* 276:122 (doi:10.1126/science.276.5309.122)."),
    "P5": banner("Supported as application (M0 2026-04-08; refined Phase E 2026-04-20)",
        "Reason: 'Fisher Information rank = effective dimensionality' restates the Sethna-group sloppy-models result [restatement-in-new-vocabulary]; validation on tori, random graphs and random geometric graphs counts as application to new model classes, not as discovery. Quinn et al. 2023 caveat: Ising at its microscopic parameterisation is not sloppy — sloppiness appears only under coarse-graining. Phase E (2026-04-20): at a continuous transition (2D Potts q = 2) the equivalence is a re-expression of standard critical exponents (Vinayak et al. 2014), not a new observable. Anchor: `reframing_of` Machta, Chachra, Transtrum & Sethna 2013, *Science* 342:604 (doi:10.1126/science.1238723)."),
    "P6": banner("Speculative (M0 2026-04-08; unchanged Phase E 2026-04-20)",
        "Reason: this project's own Phase 1 tests show gap-based Fisher rank does NOT converge to the Hausdorff dimension on fractals — it returns mixed integers. Agreement appears only for the participation ratio, which is a different observable [contradicted-by-own-tests]. The 'two independent routes' via Fisher Information Rank is therefore not supported as stated; the claim needs reformulating as a participation-ratio claim, or retiring. C1's retired implied-D_eff column (2026-07-25) lists P6 as affected."),
    "P7": banner("Speculative — partially falsified (M0 2026-04-08)",
        "Reason: the participation ratio failed monotonicity under coarse-graining in every tested configuration. Only gap-based rank on lattices under block-spin coarse-graining behaved monotonically, so 'under any valid coarse-graining operation' is contradicted by this project's own tests [contradicted-by-own-tests]. Needs reformulation restricted to the rank observable on the tested substrates, or retirement. Anchored reference: Machta, Chachra, Transtrum & Sethna 2013 (parameter-space compression under coarse-graining; doi:10.1126/science.1238723)."),
    "P8": banner("Speculative (M0 2026-04-08)",
        "Reason: critical exponents that vary with a non-integer substrate dimension are the established result of Gefen, Mandelbrot & Aharony 1980, *PRL* 45:855 ('Critical phenomena on fractal lattices'); that FIM structure distinguishes transition order is Janke, Johnston & Kenna 2004, *Physica A* 336:181 [restatement-in-new-vocabulary]. Rediscovery within that lineage, not a novel claim. Two further corrections: (i) Gefen–Mandelbrot–Aharony found the critical properties depend on the fractal dimension AND on topological factors — ramification, connectivity, lacunarity — with T_c = 0 and T_c > 0 systems at the same dimension, so 'as a function of D_eff' alone is narrower than the progenitor allows; (ii) 'uniquely predicted by Fisher Rank' is unsupported — the dependence comes from the substrate, not from a Fisher-rank construction. Anchors: `reframing_of` Gefen–Mandelbrot–Aharony 1980 (doi:10.1103/PhysRevLett.45.855) and Janke–Johnston–Kenna 2004 (doi:10.1016/j.physa.2004.01.023)."),
    "P10": banner("Speculative (M0 2026-04-08)",
        "Reason: 'better explained … than by standard QCD alone' is not supported — the GUP / running-ℏ reading is one of several consistent with existing hadron data and has generated no unique prediction [heterodox-alternative-without-unique-prediction]. Anchors: `null_hypothesis` Pohl et al. 2010, *Nature* 466:213 (doi:10.1038/nature09250); Peskin & Schroeder."),
    "P11": banner("Speculative, scope bounded (M0 2026-04-08; gsw-scaling-corrections, run 2026-07-25)",
        "Reason: the empirical regularity is Bettencourt, Lobo, Helbing, Kühnert & West 2007; the spectral-dimension mechanism is owner-constructed and untested [restatement-in-new-vocabulary; untestable-without-owner-data]. The D/(D+1) form, and β(λ) built on it, is bounded above by 1, so it cannot express superlinear urban socioeconomic exponents (~1.15); only sublinear infrastructure exponents (~0.80–0.85) fall in range. Anchor: `reframing_of` Bettencourt et al. 2007, *PNAS* 104:7301 (doi:10.1073/pnas.0610172104)."),
    "P12": banner("Falsified by structural bound (gsw-scaling-queue, run 2026-07-25)",
        "Reason: β(λ) is a weighted average of d_f/(d_f+1) and 1, so it is bounded above by 1 for every d_f and every λ in [0,1]. Urban socioeconomic exponents ~1.15 lie outside its range as a property of the formula, so 'regardless of domain' is false without any new data. The biological half is blocked (λ has no independent measurement), not falsified [over-extension-beyond-formula-range; conditional-claim-with-unsatisfiable-antecedent]. Anchor: `null_hypothesis` Newman 2005. Kept as a labelled falsification per the no-deletions rule."),
    "P13": banner("Speculative (M0 2026-04-08)",
        "Reason: contrary to 'derived from geometry alone', the (d_f−1)/(d_f+1) form is an owner-acknowledged ansatz with no first-principles derivation (see Q3) [ansatz-without-derivation]; flagged internal_construction (needs-review). Also: 'phase coherence' is the pre-2026-07-25 reading of λ; under H5's resolved definition λ is the fractional contribution of one process to total metabolic rate, and this bound has not been restated for that definition."),
    "P15": banner("Speculative (M0 2026-04-08)",
        "Reason: owner-acknowledged ansatz (see Q5) [ansatz-without-derivation]; the AlphaEntropy financial-market results are analogy, not a test of this formula. Its 'Landauer-class' motivation — a cost of maintaining phase coherence — no longer applies: under the definition resolved 2026-07-25 (H3, H5), λ is the fractional contribution of one process to total metabolic rate, not a synchronisation an organism maintains. Any surviving P15 needs a different rationale."),
    "P18": banner("Supported as single-domain observation (M0 2026-04-08)",
        "Reason: the floor is observed in US equities 2003–2025 only. The structural reading — that regulation imposes a coherence floor on 'regulated market systems' generally — is not supported until replicated on non-US markets, power grids or telecom [single-domain-overgeneralization]. internal_construction (AlphaEntropy-derived, needs-review)."),
    "P19": banner("Supported as single-domain observation (M0 2026-04-08)",
        "Reason: tested on US equities with the participation-ratio proxy only; the 4:1 recovery-to-crisis threshold comes from one dataset. 'In Tier 3 domains (economics, ecology, social systems)' exceeds that scope [single-domain-overgeneralization]. internal_construction (AlphaEntropy-derived, needs-review)."),
    "P20": banner("Supported as single-domain empirical fit (M0 2026-04-08)",
        "Reason: the formula was fitted to 19 A/B variants in one financial system, with ρ estimated qualitatively rather than measured. It is not supported as a principle for 'Tier 3 domains' generally [single-domain-overgeneralization]. internal_construction (AlphaEntropy-derived, needs-review)."),
    "P21": banner("Established — for the classical uniqueness theorem only (M0 2026-04-08; sharpened gsw-maldacena 2026-05-04)",
        "Reason: Chentsov's theorem — the Fisher–Rao metric is, up to scale, the unique Riemannian metric invariant under sufficient statistics (Markov morphisms) — is a proven result (Chentsov 1972/1982; Amari 1985; extended to general statistical manifolds by Ay, Jost, Lê & Schwachhöfer 2015). It is canonical mathematics, not this project's discovery, and 'unique … on any space of probability distributions' holds only with that invariance condition. The quantum case is a classification, not a uniqueness result: Petz 1996 gives a family of monotone metrics (Bures smallest, RLD largest, BKM, Wigner–Yanase) that agree only in the commutative limit, so there is no single canonical quantum Fisher metric. The conjecture's further step — that thermodynamics, RG flow and gravity 'share a common information-geometric foundation' because of Chentsov — is NOT established. Instance (3) uses quantum relative entropy (the Bures/Petz family, via Bianconi 2025 in GT04), not classical Fisher–Rao, so Chentsov's theorem does not cover it [vocabulary-stacking-analogy — see fisher_gravity_chain, Speculative]. Instance (1) (Ruppeiner = Fisher–Rao on the Gibbs family; Brody & Rivier 1995) is established; instances (2) and (4) are uncalibrated. Anchors: `canonical_authority` Chentsov 1982; Amari 1985; Amari & Nagaoka 2000; Petz 1996; Ay–Jost–Lê–Schwachhöfer 2015 (arXiv:1306.1465)."),
}

# ─────────────────────────────────────────────────────────────────────────────
# 3. P17 / P23 Fifth-Addendum rewording (find → replace, then dated banner)
# ─────────────────────────────────────────────────────────────────────────────
CADONI_FULL = ("Cadoni, Sanna, Pitzalis, Banerjee, Murgia, Hazra & Branchesi 2023 "
               "(JCAP 11, 007; arXiv:2306.11588)")

REWORD = [
    ("P17", "critical_gaps", [(
        "7. CADONI k = 1 PREDICTION: Cadoni et al. (JCAP, 2023) showed generic nonsingular GR interiors give k = 1, not k = 3.",
        f"7. CADONI k = 1 PREDICTION: {CADONI_FULL} show k = 1 is the universal leading-order cosmological-coupling prediction for spherically-symmetric regular (nonsingular) BHs in GR; horizonless compact objects add a subleading model-dependent term. Their own KS analysis of the Farrah–Croker elliptical-galaxy sample prefers k = 3 over k = 1, which they read as possible evidence that astrophysical BHs are non-GR objects, not as support for the Farrah–Croker scenario; they conclude regular GR BHs are unlikely to be the source of dark energy.",
    )],
     f"\n\n> **CORRECTION {CAL_DATE} (`{AUDIT_REF}`; applies M0 Fifth Addendum, Finding 2).** "
     "Item 7 previously read: \"Cadoni et al. (JCAP, 2023) showed generic nonsingular GR interiors give k = 1, not k = 3.\" "
     "The paper says 'universal' (for spherically-symmetric objects), k = 1 is the only contribution for regular BHs specifically, "
     "it has seven authors, and its own elliptical-sample analysis prefers k = 3. Original wording recorded here per the no-deletions rule."),

    ("P17", "phase1_results", [(
        "- LVK O4: k < 2.1 (standard), k < 1.1 (CCBH-corrected) at 2 sigma.",
        "- GWTC-3 (LVK O1–O3, via Amendola et al. 2024 — not O4): k < 2.1 (PLPP, log-uniform delay-time prior) and k < 1.1 (PLPP with Ghodla 2023's corrected delay time) at 2σ.",
    ), (
        "- Cadoni et al.: generic nonsingular GR gives k = 1, not k = 3.",
        "- Cadoni et al. 2023 (seven authors): k = 1 is universal at leading order for regular (nonsingular) GR BHs; their own KS analysis of the Farrah sample prefers k = 3, which they read as possible non-GR behaviour.",
    )],
     f"\n\n> **CORRECTION {CAL_DATE} (`{AUDIT_REF}`; applies M0 Fifth Addendum, Findings 1–2).** "
     "Two CHALLENGING lines corrected. (1) Previously \"LVK O4: k < 2.1 (standard), k < 1.1 (CCBH-corrected) at 2 sigma.\" "
     "Those limits are Amendola, Rodrigues, Kumar & Quartin 2024's GWTC-3 results; the paper does not use O4. "
     "(2) Previously \"Cadoni et al.: generic nonsingular GR gives k = 1, not k = 3.\" The paper says 'universal' for regular BHs, "
     "and its authors' own sample analysis prefers k = 3. Original wording recorded here per the no-deletions rule."),

    ("P23", "claim", [(
        r"including GW 5$\sigma$ rejection of $k = 3$, Gaia BH constraints, and Cadoni $k = 1$ prediction",
        r"including ~3$\sigma$ GW merger-rate tension with $k = 3$ (Amendola et al. 2024, GWTC-3; their $5\sigma$ figure is a forecast for ~250 further events), Gaia BH constraints, and the Cadoni et al. 2023 $k = 1$ prediction for regular BHs",
    )],
     f"\n\n> **CORRECTION {CAL_DATE} (`{AUDIT_REF}`; applies M0 Fifth Addendum, Findings 1–2).** "
     "This paragraph previously cited \"GW 5$\\sigma$ rejection of $k = 3$\" and \"Cadoni $k = 1$ prediction\". "
     "Current GWTC-3 data give 2σ upper limits k < 2.1 — about 3σ tension with k = 3, not a rejection; the >5σ figure is Amendola et al.'s forecast. "
     "Cadoni et al.'s k = 1 is the universal leading-order result for regular GR BHs. Original wording recorded here per the no-deletions rule."),

    ("P23", "would_kill", [(
        "(currently reject k = 3 at 5 sigma but k = 1 still viable — Amendola et al. MNRAS 528, 2024)",
        "(current GWTC-3 data give 2σ upper limits k < 2.1 — ~3σ tension with k = 3, not a rejection; Amendola et al.'s >5σ figure is a forecast for ~250 further events; k = 1 still viable — Amendola, Rodrigues, Kumar & Quartin, MNRAS 528, 2377, 2024)",
    )],
     f"\n\n> **CORRECTION {CAL_DATE} (`{AUDIT_REF}`; applies M0 Fifth Addendum, Finding 1).** "
     "Item 4 previously read \"(currently reject k = 3 at 5 sigma but k = 1 still viable — Amendola et al. MNRAS 528, 2024)\". "
     "The 5σ figure is the paper's forecast, not its current-data result. Original wording recorded here per the no-deletions rule."),

    ("P23", "critical_gaps", [(
        "Cadoni k = 1 for generic nonsingular objects (Cadoni 2023)",
        "Cadoni et al. 2023's k = 1, universal at leading order for regular (nonsingular) GR BHs, with their own sample analysis preferring k = 3",
    ), (
        "3. CADONI k = 1 vs k = 3: Generic nonsingular GR interiors give k = 1 (Cadoni et al. JCAP 2023).",
        f"3. CADONI k = 1 vs k = 3: Regular (nonsingular) GR BHs give k = 1 at leading order — 'universal' for spherically-symmetric objects ({CADONI_FULL}); horizonless compact objects add a model-dependent term, and the authors' own KS analysis of the Farrah sample prefers k = 3.",
    )],
     f"\n\n> **CORRECTION {CAL_DATE} (`{AUDIT_REF}`; applies M0 Fifth Addendum, Finding 2).** "
     "Items 1 and 3 previously read \"Cadoni k = 1 for generic nonsingular objects (Cadoni 2023)\" and "
     "\"Generic nonsingular GR interiors give k = 1 (Cadoni et al. JCAP 2023).\" The paper says 'universal' for regular BHs; "
     "horizonless objects add a term, and its own sample analysis prefers k = 3. Original wording recorded here per the no-deletions rule."),
]

# ─────────────────────────────────────────────────────────────────────────────
# 4. Calibration rows — corrections recorded, labels unchanged
# ─────────────────────────────────────────────────────────────────────────────
CALIBRATIONS = [
    ("P17", "conjecture", "Speculative", CAL_DATE, AUDIT_REF,
     "Prose corrected: Cadoni wording + GWTC-3 (not O4) relabel, per M0 Fifth Addendum",
     "Correction recorded, label unchanged (Speculative, high risk). Applied the outstanding M0 Fifth Addendum rewording to ds_wiki.db: "
     "critical_gaps item 7 and one phase1_results line now state Cadoni et al. 2023 correctly (7 authors; k = 1 'universal' at leading order for "
     "regular GR BHs; their own KS analysis prefers k = 3). The phase1_results line 'LVK O4: k < 2.1, k < 1.1' was relabelled — these are "
     "Amendola et al. 2024 GWTC-3 (O1–O3) limits; the paper does not use O4. The Amendola 5σ-forecast correction was already applied 2026-05-04. "
     "Original wording preserved in dated banners. Closes the P17 prose item left open in the gsw-maldacena-deep-research-2026-05-04 row."),
    ("P23", "conjecture", "Speculative", CAL_DATE, AUDIT_REF,
     "Prose corrected: '5σ rejection of k=3' and Cadoni 'generic' removed, per M0 Fifth Addendum",
     "Correction recorded, label unchanged (Speculative, high risk). claim and would_kill still stated 'GW 5σ rejection of k = 3' as current fact; "
     "corrected to ~3σ tension from GWTC-3 2σ upper limits (k < 2.1), with the >5σ figure identified as Amendola et al. 2024's forecast. "
     "critical_gaps items 1 and 3 corrected from 'generic nonsingular' to Cadoni et al. 2023's 'universal for regular BHs', noting their "
     "own sample analysis prefers k = 3. Original wording preserved in dated banners."),
]


ANCHOR_NOTE_FIXES = {
    818: (" CORRECTION 2026-10-18 (gsw-consistency-pass-2026-10-18): this note appears to describe P7's claim "
          "(monotonic d_eff decrease under coarse-graining), not P6's; P6 is the fractal-dimension / Fisher-rank "
          "convergence claim, contradicted by this project's own Phase 1 tests (gap-based rank does not converge to "
          "the Hausdorff dimension). The notes on anchors 818 (P6) and 819 (P7) look swapped. Original text kept above; "
          "relationship unchanged pending owner review."),
    819: (" CORRECTION 2026-10-18 (gsw-consistency-pass-2026-10-18): this note appears to describe P6's claim "
          "(fractal dimension converging with Fisher rank), not P7's; P7 is the monotonic-decrease-under-coarse-graining "
          "claim. The relationship is also doubtful: Machta 2013's parameter-space compression points the SAME way P7 "
          "claims — P7 failed on the participation ratio in this project's own tests, not against Machta. Candidate "
          "relationship adjacent_concept; owner review needed. Original text kept above; relationship unchanged."),
}


def fetch(cur, cid, col):
    row = cur.execute(f"SELECT {col} FROM conjectures WHERE id=?", (cid,)).fetchone()
    if row is None:
        raise SystemExit(f"Row not found: conjectures {cid}")
    return row[0] or ""


def plan(cur):
    ops, seen = [], set()

    def add(label, cid, col, new, current):
        target = ("conjectures", cid, col)
        if target in seen:
            raise SystemExit(f"[{label}] ABORT — duplicate target {target}")
        seen.add(target)
        if new == current:
            print(f"  [{label}] OK — already applied, skipping")
            return
        ops.append((label, cid, col, new))

    # three_state
    ids = [r[0] for r in cur.execute("SELECT id FROM conjectures ORDER BY conjecture_order")]
    missing = set(ids) ^ set(THREE_STATE)
    if missing:
        raise SystemExit(f"ABORT — three_state map does not cover exactly the 23 conjectures: {missing}")
    for cid in ids:
        cur_v = fetch(cur, cid, "three_state")
        prefix = THREE_STATE[cid] + SEP
        if cur_v.startswith(prefix):
            add(f"{cid}.three_state", cid, "three_state", cur_v, cur_v); continue
        if SEP in cur_v:
            raise SystemExit(f"[{cid}.three_state] ABORT — already carries a different ' | was: ' prefix")
        add(f"{cid}.three_state", cid, "three_state", prefix + cur_v, cur_v)
        print(f"  [{cid}.three_state] plan — prefix (+{len(prefix)}) | was: {cur_v[:40]!r}")

    # Columns touched by both a banner and a reword are composed into one write.
    composed = {}
    for cid, col, pairs, suffix in REWORD:
        composed[(cid, col)] = (pairs, suffix)

    for cid, ban in BANNERS.items():
        cur_v = fetch(cur, cid, "claim")
        pairs, suffix = composed.pop((cid, "claim"), ([], ""))
        if cur_v.startswith(ban):
            add(f"{cid}.claim", cid, "claim", cur_v, cur_v); continue
        new = cur_v
        for find, repl in pairs:
            if new.count(find) != 1:
                raise SystemExit(f"[{cid}.claim] FAIL — anchor count {new.count(find)}: {find[:70]!r}")
            new = new.replace(find, repl, 1)
        new = ban + new + suffix
        add(f"{cid}.claim", cid, "claim", new, cur_v)
        print(f"  [{cid}.claim] plan — banner (+{len(ban)})" + (f", {len(pairs)} replace(s) + suffix" if pairs else ""))

    for (cid, col), (pairs, suffix) in composed.items():
        cur_v = fetch(cur, cid, col)
        # Applied suffix first: the correction banner quotes the original
        # wording, so the find-strings legitimately reappear inside it.
        if cur_v.endswith(suffix):
            add(f"{cid}.{col}", cid, col, cur_v, cur_v); continue
        new = cur_v
        for find, repl in pairs:
            if new.count(find) != 1:
                raise SystemExit(f"[{cid}.{col}] FAIL — anchor count {new.count(find)}: {find[:70]!r}")
            new = new.replace(find, repl, 1)
        new = new + suffix
        add(f"{cid}.{col}", cid, col, new, cur_v)
        print(f"  [{cid}.{col}] plan — {len(pairs)} replace(s) + correction banner (+{len(suffix)})")
    return ops


def plan_summary(cur):
    ops = []
    for cid, status in cur.execute("SELECT id, status FROM conjecture_summary ORDER BY rowid").fetchall():
        prefix = THREE_STATE[cid] + SEP
        if (status or "").startswith(prefix):
            print(f"  [{cid}.summary] OK — already applied, skipping"); continue
        if SEP in (status or ""):
            raise SystemExit(f"[{cid}.summary] ABORT — different ' | was: ' prefix present")
        ops.append((cid, prefix + (status or "")))
        print(f"  [{cid}.summary] plan — prefix | was: {(status or '')[:40]!r}")
    return ops


def plan_anchor_notes(hcur):
    ops = []
    for aid, suffix in ANCHOR_NOTE_FIXES.items():
        row = hcur.execute("SELECT entry_id, relationship, notes FROM external_anchors WHERE id=?", (aid,)).fetchone()
        if row is None or row[1] != "contradicts" or row[0] not in ("P6", "P7"):
            raise SystemExit(f"[anchor {aid}] ABORT — unexpected row {row!r}")
        if (row[2] or "").endswith(suffix):
            print(f"  [anchor {aid}] OK — already applied, skipping"); continue
        ops.append((aid, (row[2] or "") + suffix))
        print(f"  [anchor {aid}] plan — append correction (+{len(suffix)})")
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")

    print("=" * 72); print("PHASE 1 — validation / dry run"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    ops = plan(cur)
    sum_ops = plan_summary(cur)
    conn.close()
    hc0 = sqlite3.connect(WIKI_HISTORY_DB)
    note_ops = plan_anchor_notes(hc0.cursor())
    hc0.close()

    hc = sqlite3.connect(WIKI_HISTORY_DB)
    pending_cal = [c for c in CALIBRATIONS if not hc.execute(
        "SELECT 1 FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
        (c[0], c[3], c[4])).fetchone()]
    hc.close()
    print(f"\n  {len(ops)} conjecture writes + {len(sum_ops)} summary writes planned; "
          f"{len(note_ops)} anchor-note appends; {len(pending_cal)} calibration rows to append")

    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply."); return

    print("\n" + "=" * 72); print("PHASE 2 — apply"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    for label, cid, col, new in ops:
        cur.execute(f"UPDATE conjectures SET {col}=? WHERE id=?", (new, cid))
        if cur.rowcount != 1:
            conn.rollback(); conn.close(); raise SystemExit(f"[{label}] hit {cur.rowcount} rows; rolled back")
    for cid, new in sum_ops:
        cur.execute("UPDATE conjecture_summary SET status=? WHERE id=?", (new, cid))
        if cur.rowcount != 1:
            conn.rollback(); conn.close(); raise SystemExit(f"[{cid}.summary] hit {cur.rowcount} rows; rolled back")
    conn.commit(); conn.close()
    print(f"  wrote {len(ops)} conjecture values + {len(sum_ops)} summary values")

    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for row in pending_cal:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence,
                      calibration_date, audit_ref, short_status, rationale) VALUES (?,?,?,?,?,?,?)""", row)
    for aid, new in note_ops:
        hcur = hc.execute("UPDATE external_anchors SET notes=? WHERE id=?", (new, aid))
        if hcur.rowcount != 1:
            hc.rollback(); hc.close(); raise SystemExit(f"[anchor {aid}] hit {hcur.rowcount} rows; rolled back")
    hc.commit(); hc.close()
    print(f"  appended {len(pending_cal)} calibration rows; {len(note_ops)} anchor notes corrected")

    print("\n" + "=" * 72); print("PHASE 3 — read-back verification"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    bad = [label for label, cid, col, new in ops if fetch(cur, cid, col) != new]
    bad += [f"{cid}.summary" for cid, new in sum_ops
            if cur.execute("SELECT status FROM conjecture_summary WHERE id=?", (cid,)).fetchone()[0] != new]
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for c in CALIBRATIONS:
        got = hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                         (c[0], c[3], c[4])).fetchone()
        if got != (c[2], c[5]):
            bad.append(f"cal:{c[0]}")
    bad += [f"anchor:{aid}" for aid, new in note_ops
            if hc.execute("SELECT notes FROM external_anchors WHERE id=?", (aid,)).fetchone()[0] != new]
    hc.close()
    if bad:
        raise SystemExit(f"Post-write drift: {bad}")
    print(f"  verified: {len(ops)} conjecture + {len(sum_ops)} summary writes, {len(note_ops)} anchor notes, "
          f"{len(CALIBRATIONS)} calibration rows")


if __name__ == "__main__":
    main()
