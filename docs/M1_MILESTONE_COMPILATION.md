# M1 Milestone Compilation — 2026-10-18 (pre-merge baseline)

> **Second milestone.** M0 (2026-04-08) set the condition for M1: at least one conjecture formally falsified. **P12 was falsified on 2026-07-25**, so the condition is met. This compilation is also the **pre-merge baseline** before the wiki is merged with the *Relatively Human* podcast; the matching embedding snapshot is `snap_20261018_190812` (milestone, never pruned).
>
> **Counting rule.** Every number below comes from the `claim_status_latest` view (latest calibration row per scientific entity) or `process_status_latest` (process records), in `wiki_history.db`. Raw calibration rows (89 across 13 audit refs) are *not* claim counts. Audit refs: M0 family, `gsw-cca-potts-sweep-phase-E-2026-04-20`, `gsw-maldacena-deep-research-2026-05-04`, the five scaling refs suffixed `-2026-05-04` (work done 2026-07-25), and `gsw-consistency-pass-2026-10-18` (+ `-h5-gate`).

---

## 1. What we believe right now

**47 scientific claims: 29 Speculative · 8 Supported · 7 Established · 3 Falsified.**

- **Established (7):** P21 (Chentsov's classical uniqueness theorem only; quantum case = Petz classification) · M6 (Fisher rank as a parameter-space diagnostic, nothing more) · BR04 (Ruppeiner = Fisher–Rao on the Gibbs family, Brody–Rivier 1995) · C1 (metabolic power-law scaling; curvature itself contested) · `matrix_spectrum_reduces_to_critical_exponents` · `curvature_direction_puzzle` (resolved: sum rule, not min rule) · `mmr_sustained_vs_peak_distinction`
- **Supported (8):** P5 (only as an application of Machta et al. 2013) · P18, P19, P20 (single-domain, US equities / AlphaEntropy) · CCA-1b magnitude · CCA-2 (2D and 3D tori only) · GT10 (linearized only) · STAT3
- **Falsified (3):** P12 · CCA-1 · CCA-1b L^d scaling
- **Speculative (29):** P1–P4, P6–P11, P13–P17, P22, P23, P14a, P14b, CCA-1c, H3, H5, X1, BR01, GT02, GT04, GT10_as_CCA_instance, CCA_brown_mechanism_question, fisher_gravity_chain

**Process records (8), not claims:** cca_terminology_rename, lambda_symbol_collision, scaling_framework_root_diagnosis (Established); cca_d_eff_naming, cca_eta_naming, endpoint_decision_revised, saberi_2024_prb_priority_read, saberi_external_reviewer (Speculative).

## 2. What the evidence is

- **P21** — `canonical_authority` Chentsov 1982, Amari 1985, Amari & Nagaoka 2000, Petz 1996, Ay–Jost–Lê–Schwachhöfer 2015. A theorem from the literature, not a project finding.
- **M6, P5** — Machta, Chachra, Transtrum & Sethna 2013 (`reframing_of` for P5); Quinn et al. 2023 caveat; Phase E (2026-04-20): at continuous T_c the observable reduces to standard critical exponents (Vinayak et al. 2014).
- **BR04** — Brody & Rivier 1995.
- **C1** — WBE 1997, White & Seymour 2003, Dodds–Rothman–Weitz 2001, and the 2026-07-25 replication record (Griebeler & Werner 2016 et al.) that downgraded curvature to contested.
- **GT10** — Jacobson 1995/2016, with the Casini–Galante–Myers 2016 scope caveat.
- **CCA-1b magnitude, CCA-2, STAT3, matrix_spectrum** — in-project Phase A–E Potts/Ising runs (540-run Phase E sweep) against Brown–Bossomaier–Barnett 2022, Vinayak 2014 and Borgs–Chayes 1996. Each rests on a **single test family**.
- **P18–P20** — one domain (US equities 2003–2025); internal constructions, needs-review.
- **P12 (Falsified)** — structural: β(λ) is a weighted average of d_f/(d_f+1) and 1, so it is ≤ 1 for every admissible input, and urban exponents ~1.15 cannot be reached. Falsified without new data.

## 3. What's still open

- **The merge.** Podcast claims mapped to wiki status in `docs/PODCAST_CROSSWALK_2026-10-18.md`; merge design not started.
- **P14a** — the only runnable scaling item (branching-ratio variance vs BMR/MMR exponent gap).
- **Scaling item ②** — does metabolic rate decompose into separate parallel fluxes at all? If not, H5's two-process reading has no referent.
- **CCA-1c / Brown mechanism question** — is d_eff_CCA's first-order jump just λ₁ ordering-mode collapse (textbook), or more?
- **Glossary markup** not applied (611 flags / 122 entries); CCA and λ renames not applied in body text.
- **P9** should move to the Q-series; **P6/P7 anchor notes** (818/819) need owner review.
- **Labels that look generous, flagged and unchanged:** `mmr_sustained_vs_peak_distinction` is Established on the strength of the owner's own argument, with no primary-literature anchor; the charter reserves Established for cited textbook results. `scaling_framework_root_diagnosis` (process) is Established although its "no mechanism" diagnosis was declared reversed on 2026-07-25 — and the 2026-10-18 gate found the identity supplies no mechanism after all.

## 4. What changed since M0

- **One label change among M0-calibrated entities:** P12, Speculative → **Falsified** (2026-07-25). The other 31 M0-calibrated claims keep their M0 label.
- **15 entities calibrated for the first time:** BR01, BR04, C1, GT02, GT04, GT10, H3, H5, M6, P14a, P14b, STAT3, X1, curvature_direction_puzzle, mmr_sustained_vs_peak_distinction.
- **Corrections without label changes (2026-10-18):** the source DB now mirrors calibration — three_state prefixes on all 23 conjectures, status banners on 14 claims, and conjecture_summary statuses updated. P17/P23/GT11/G12 wording on Amendola (5σ was a forecast) and Cadoni ("universal for regular BHs") corrected. The fabricated "Xiao et al. 2015" removed from H5, where it had survived. H5's two-process derivation reclassified as a re-derivation and a restatement of West et al. 2003. GT05 anchored; its source is free-energy, not entanglement. Errors shared with the podcast corrected: BIO3 (Frank 2009), IT05 and the M6→QM2 link (uncertainty principle), C2 (β = 1 ± 1/D_eff). The date erratum is recorded.

## 5. What we tried that didn't work (mandatory)

- **P12's cross-domain universality** — falsified by its own functional form. Its `would_kill` anticipated the wrong failure mode [over-extension-beyond-formula-range].
- **H5's "derivation found, diagnosis reversed"** (2026-07-25) — the identity is correct but textbook, and is West et al. 2003; it gave λ a meaning, not a mechanism. Escalation within one session.
- **Inverting β = D/(D+1), or 1 ± 1/D, on single exponents to read off dimensions** — C1's implied D_eff (two values above the embedding dimension), X1's d_f = 2.7, C2's urban D_eff ≈ 8 and ≈ 4.8. One parameter per data point; all retired or withdrawn.
- **CCA-1 (isotropy = criticality)** and **CCA-1b L^d scaling** — falsified by our own Phase C and D runs.
- **P6 (Fisher rank = Hausdorff dimension)** and **P7 (monotone D_eff)** — contradicted by our own Phase 1 tests: rank gives mixed integers on fractals, and the participation ratio failed monotonicity in every tested configuration.
- **Bianconi 2025 as an independent second route from Fisher information to gravity** — retracted; it uses quantum relative entropy.
- **"Xiao et al. 2015"** — a fabricated citation that passed several earlier reviews; it survived in H5 for a further 85 days after it was corrected in C1.
- **Treating the endpoint question as a choice** — [2/3, 3/4] was chosen, then declared "derivable"; it is neither settled nor derivable from the identity.
