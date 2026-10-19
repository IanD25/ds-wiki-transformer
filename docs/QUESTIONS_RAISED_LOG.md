# Questions Raised Log

> **What this is.** A running intake log of open scientific questions that the wiki's compiled knowledge raises — questions to ask the world, not answers we claim. Started 2026-10-18 after the pre-merge consistency pass, when the project returned to its original purpose: compile real science, map the connections, and look for good questions.
>
> **What this is not.** Not conjectures (P-series) and not yet open-question entries (Q-series in `ds_wiki.db`). Nothing here asserts that a question is new. Most will turn out to be well-known open problems, and that is fine: placing ourselves correctly in an existing conversation is the point.

## How the log works

**IDs** use the prefix `QR-` so they never collide with the wiki's Q-series (Q1–Q5) or P-series.

**Status ladder** (a question moves down it; nothing skips a step):

1. **Raised** — written down, with why the wiki's map suggests it.
2. **Literature-mapped** — the field's current state found and read from primary sources: who works on it, what is settled, what is not.
3. **Gated** — both gates in [`QUESTION_GATES.md`](QUESTION_GATES.md) have run, in order, with the report in `prior_art_reviews/`:
   - **Gate 1, prior art** (`memory/feedback_prior_art_gate.md`), with one verdict:
     - `open-in-literature` — a recognised open problem; record it as such, citing who frames it.
     - `answered` — the literature already settles it; fold the answer in as reference entries.
     - `narrow-angle-provisional` — the field asks it, but the wiki's cross-domain view adds a specific sub-question nobody seems to ask. Provisional until a second, primary-source search fails to find it.
   - **Gate 2, worth asking** — runs whenever Gate 1 is not `answered`. Five tests (triviality, absence, obvious or erroneous, expert view, should it be asked), then **PROCEED**, **RE-SCOPE**, **FOLD** or **DROP**, each with a reason tag. A PROCEED stays provisional until a second, independent search fails to explain the absence.
4. **Filed** (optional) — becomes a Q-series entry in `ds_wiki.db`, anchored `open_in_literature`. Only a question with a Gate 2 PROCEED can be filed.

**Parked** (any stage) — set aside by owner decision, with a date, a reason and a resume condition. Nothing is lost: the entry stays as written and picks up where it stopped.

**Rules.** Literature cited below is a *starting point* unless marked verified. No question becomes a wiki entity without the gate. Each entry names the wiki entities involved and the gaps in the wiki's own coverage, because a question sitting on an empty patch of the map needs grounding (Mode A) before any exploration (Mode B).

---

## QR-006 · Can information measures warn of tipping points earlier, or more reliably, than classical indicators? — **PRIORITY**

- **Question.** Do information-theoretic measures (transfer entropy and information flow, mutual information, Fisher-information indices, entropy rates, complexity measures, correlation-matrix concentration) give earlier or more reliable warning of critical transitions in real systems — ecosystems, climate, medicine, markets — than rising variance and autocorrelation (critical slowing down)?
- **Why the wiki raises it.** It is the honest descendant of the CCA thread. CCA found that correlation-matrix observables discriminate first-order from continuous transitions, using different signatures from Brown–Bossomaier–Barnett's transfer entropy (STAT3, CCA-1c, Phase E). It is also the subject of the podcast's S1E2 *Tipping Points*. It is the owner's top real-world question.
- **Wiki holdings.** STAT3, CCA-1c, X0_FIM_Regimes, M3 (Preisach hysteresis), D2 (Feigenbaum), STAT6 (Brown 2022), and, since the 2026-10-18 EWS fold-in ([report](prior_art_reviews/EWS_FOLD_IN_2026_10.md)), **EWS1–EWS10**:
  - EWS1 critical slowing down and the classical indicators; EWS2 the lake and yeast experiments.
  - EWS3 B-, N- and R-tipping and transitions without warning; EWS4 false alarms and limits of detection.
  - EWS5 Barnett 2013's information-flow peak; EWS6 the ecological Fisher Information index.
  - EWS7 covariance-eigenvalue and dominant-mode indicators; EWS8 the Weinans 2021 benchmark.
  - EWS9 Bury 2021 deep learning with ROC; EWS10 spatial permutation entropy.
  - **Remaining gap:** biological criticality (QR-002), and the unread sources listed in the report (Fath 2003, Kritzman 2011, Prokopenko 2011).
- **Starting literature (not yet verified this session):** Scheffer et al. 2009 (*Nature* 461:53); Dakos et al. 2012 (*PLoS ONE*); Boettiger & Hastings 2012; Ditlevsen & Johnsen 2010; Barnett et al. 2013 (*PRL* 111:177203); Brown, Bossomaier & Barnett 2022; Fath, Cabezas & Pawlowski 2003 (Fisher information for regime shifts); Chen et al. 2012 (dynamical network biomarkers); Bury et al. 2021 (*PNAS*).
- **What would decide it.** Head-to-head comparisons on the same data: lead time and false-alarm rate of each indicator, across transition types (fold, noise-induced, rate-induced), on systems where the transition is known.
- **Possible prior art inside the wiki to check:** X0's "Fisher-information regime" classification against the ecological Fisher Information index; CCA's correlation-concentration signal against dynamical network biomarkers.
- **Status:** **Literature-mapped (partial)**, 2026-10-18 — [`prior_art_reviews/QR-006_EWS_LITERATURE_MAP_2026_10_18.md`](prior_art_reviews/QR-006_EWS_LITERATURE_MAP_2026_10_18.md). Compiled by a research agent; several key sources not yet read. QR-006 stays the umbrella question and is not itself gated: as posed ("any measure, any real system") it is too broad to decide. Its testable form is **QR-006b** below, which is gated.
- **What the field currently says (provisional):**
  - **Unproven.** Information-theoretic indicators have all been *proposed* as earlier or better warnings, but head-to-head tests on the same data are rare, mostly on models, small, and scored differently. The one multi-indicator benchmark that included one (Weinans et al. 2021, 13 indicators) found no overall winner; mutual information was among the least robust to noise.
  - **No study found** compares transfer entropy against autocorrelation or variance on lead time or ROC.
  - The only systematic ROC win over the classical signals is deep learning (Bury et al. 2021), which is not information-theoretic.
  - Classical signals are well grounded for slow approaches to a bifurcation (whole-lake and yeast experiments). They fail for noise- and rate-induced tipping, give false alarms on trends, did not appear before epileptic seizures, and only partly before market crashes. They do not distinguish abrupt from continuous transitions.
  - Information flow peaks on the *disordered* side of a transition, and for first-order transitions only in finite systems (Barnett 2013; Brown 2022). There is no test yet on real time series.
- **Provisional verdicts on the wiki's own work:**
  - **X0** vs the ecological Fisher Information index: ADJACENT (different mathematical objects). X0's three regimes restate the textbook disordered / critical / ordered phases, and its finance case is close to the "absorption ratio" (Kritzman 2011).
  - **CCA**: using correlation-matrix concentration as a warning signal is a RESTATEMENT (dynamical network biomarkers, eigenvalue-share indicators). Using the participation ratio to *classify transition order* has no prior art found yet (provisional).
  - **Triviality warning:** the agent derives that CCA's first-order jump may simply be the order-parameter jump seen through S(k=0). That is the CCA-1c reduction test, still unrun.
- **Open sub-questions** (from the map; each with deciding data):
  1. **Do information indicators add ROC skill over autocorrelation and variance?** Test on a common benchmark, such as Bury et al. 2021's public set of 268 transition and null series.
  2. **Is the Fisher Information index a pooled-variance proxy?**
  3. **Does a transfer-entropy peak give lead *time* in a slowly driven system,** not just a peak in temperature?
  4. **Does participation-ratio collapse add anything beyond the eigenvalue share?**
  5. **Does any indicator beat chance for noise-induced tipping** (seizures, crashes, Dansgaard–Oeschger events)?
- **Next:**
  - **(a) Mode A:** read the unread key sources (Barnett 2013, Fath 2003, Dakos 2012, Ditlevsen & Johnsen 2010), then fold the early-warning literature into the wiki. That fills the coverage gap below.
  - **(b) Gate:** run the prior-art gate on sub-question 1. If it comes back open, it is a concrete project on public data that could answer the owner's question directly.
  - **(c)** Run the CCA-1c reduction test, which the triviality warning feeds.
  - *Update:* (a) is done (EWS fold-in). (b) is done for the re-scoped form, QR-006b, below. (c) is still unrun; it now feeds QR-007.

### QR-006b · Regime-stratified benchmark: do information indicators beat the classical and the regime-appropriate indicators where critical slowing down's assumptions fail?

- **Question** (baselines widened 2026-10-18, owner-approved). On a common labelled benchmark of transition series and matched no-transition series, scored at matched false-alarm rates, does any information-theoretic indicator beat **all** of the following, measured by ROC-AUC or by lead time at fixed specificity?
  - lag-1 autocorrelation and variance;
  - their rank-based versions (rank AC1, a robust spread measure);
  - the regime-appropriate non-information indicators: skewness, kurtosis and bimodality; RAD (Harris et al. 2024); the α-stable scale factor (Layritz et al. 2025); drift–diffusion–jump or Langevin estimates.

  In particular, does it do so where the linear-Gaussian approximation fails: non-Gaussian or multiplicative noise, strong nonlinearity near the fold, and noise- or rate-induced tipping? Results are reported per regime and against chance.
- **Why the baselines were widened.** Where critical slowing down's assumptions fail, the field's own replacements are distributional and model-based, not information-theoretic. In Harris et al. 2024's screen under unknown noise amplitude, information features beat AC1 but no information feature reached the top 100; distribution-shape features won (second-search report §7). Against AC1 and variance alone, a "yes" could not tell an information gain from a distributional one. *Original wording (2026-10-18, superseded):* "…does any information-theoretic indicator beat lag-1 autocorrelation and variance…".
- **Why re-scoped.** In the linear-Gaussian regime where critical slowing down holds, the information measures are functions of the autocovariance (lag-1 MI = −½ log(1 − ρ²); transfer entropy = Granger causality; Gaussian ordinal-pattern probabilities are fixed by the autocorrelations). There they can at best match autocorrelation and variance. That half of QR-006's sub-question 1 is a re-derivation and was folded.
- **Gate report:** [`prior_art_reviews/QR-006_BENCHMARK_GATES_2026_10_18.md`](prior_art_reviews/QR-006_BENCHMARK_GATES_2026_10_18.md) (first use of Gate 2).
- **Gate 1:** the generic benchmark is `open-in-literature` — Dakos et al. 2024 (*Earth Syst. Dyn.* 15:1117, §4.3.1) name the gap; the closest study, Weinans et al. 2021, used one model family, Kendall τ rather than ROC, and only mutual information. The regime-stratified version is `narrow-angle-provisional` (no prior art found).
- **Gate 2:** **FOLD** the linear-Gaussian equivalence (`trivial-from-known-result`). **RE-SCOPE → PROCEED (provisional)** on the regime-stratified form. The absence is partly explained by data-hungriness (e, Weinans 2021) and by labelled benchmarks existing only since 2021 (f, Bury et al.).
- **Design conditions** (from Gate 2 test 3): indicators, windows, detrending and thresholds fixed in advance; identical preprocessing for every indicator; matched null series; every indicator scored against chance as well as against autocorrelation and variance, because in noise- and rate-induced tipping nothing may beat chance.
- **Status:** **Gated — PROCEED with named gaps**, 2026-10-18 (was "still provisional, narrowed" after the second, independent search, [report](prior_art_reviews/QR-006b_SECOND_SEARCH_2026_10_18.md)). Not overturned: no study found runs the regime-stratified, matched-false-alarm benchmark. Partial answers turned up under other vocabulary: seizure-prediction ROC comparisons found no univariate nonlinear advantage over linear measures (Mormann 2005, abstract), and a feature screen under unknown noise found distribution-shape features winning (Harris et al. 2024, *PRX*). Baselines widened accordingly (owner-approved 2026-10-18; see the question above). The Gaussian-copula sub-case folds (`trivial-from-known-result`). Harris 2024 Table S1 has since been read (report §7). Under unknown noise amplitude, 244 information features beat AC1, but none reaches the top 100; distribution-shape features win, which backs the baseline re-scope. **Readings closed 2026-10-18 (report §8): PROCEED with named gaps.** Eason 2014 was read in full (owner-supplied UNL copy) and is clean: single runs, scored by rank correlation between indicator curves and by eye, with no nulls or false-alarm rates. FI tracks −variance (ρ = −0.98), as the 1/σ² identity predicts. Dakos & Soler-Toscano 2017 (search summary) and Mormann 2005 (abstract) could not be obtained; both are named gaps in the pre-registration.
- **Provisional until:** ~~(1) a second, independent search fails to find the study~~ — done 2026-10-18, not overturned. Still open: Dakos & Soler-Toscano 2017 (full text), Mormann et al. 2005 (full text: measure list and per-measure ROC), Eason et al. 2014 (results). ~~Harris et al. 2024 Supplemental Table S1~~: read 2026-10-18, not the study (report §7). If these come back clean, PROCEED is confirmed on the re-scoped form; if one contains the study, that regime FOLDs (`found-under-other-vocabulary`). *Update 2026-10-18:* ~~Eason et al. 2014~~: read in full, clean (report §8.2). Dakos & Soler-Toscano 2017 and Mormann et al. 2005: unobtainable this session (closed; no repository copy), so they stand as **named gaps**, not as conditions. Re-open the verdict if either is read later: Dakos could touch the bifurcation, flickering and possibly N/R strata; Mormann only the empirical stratum and the prior.
- **Next:** ~~read the three open items; then a pre-registered benchmark design~~ — done 2026-10-18: [`experiments/QR006B_BENCHMARK_PREREGISTRATION.md`](experiments/QR006B_BENCHMARK_PREREGISTRATION.md). It sets out 10 strata (3 controls, 6 tests, 1 descriptive empirical), 6 information indicators against 12 baselines, matched nulls, prediction ROC, lead time at 5% false-alarm rate, actionable lead time and in-progress detection scored separately, Holm-controlled decision rules, and controls opened first. Estimated cost ≈ 90–100 CPU-hours. ~~Next is the pilot, then the freeze commit~~ — done 2026-10-18: pipeline built (`scripts/qr006b/`); pilot passed ([`experiments/QR006B_PILOT_REPORT_2026_10_18.md`](experiments/QR006B_PILOT_REPORT_2026_10_18.md); results discarded, no test-stratum comparison computed); protocol frozen (tag `qr006b-prereg-frozen`; amendments A1–A22 in its §12). Owner decisions on the two control-design risks (pilot report §6) are logged as protocol deviations D1–D2, made before any confirmatory data existed. D1: the decisive score in the slow-ramp strata uses the record up to 80% of the way to the tip. D2: the C0g mutual-information tolerance becomes ±0.05. **Next: the confirmatory run, owner to start** (≈ 49 CPU-hours / ≈ 5.5 h for the decisive part; ≈ 220 / ≈ 24 h with all sensitivity analyses).

## QR-007 · Can correlation-matrix observables classify a transition's order? — **MERGED into QR-008** (2026-10-18)

> **Merged 2026-10-18 (owner decision).** The equilibrium form folded (status below). The only remaining form, reading a transition's order from data taken *before* it, is the "order" part of QR-008's stage 1, so it now lives there. The entry is kept unchanged below as the record.

- **Question.** Can observables of the connected correlation matrix (participation ratio, eigenvalue concentration) tell a first-order transition from a continuous one, on data where the order is known — and do they carry anything beyond the order-parameter jump and existing order-discrimination methods?
- **Why the wiki raises it.** It is CCA's distinct angle, split out of QR-006 by the QR-006b gate report: as a *warning* signal, correlation-matrix concentration is a restatement (dynamical network biomarkers, eigenvalue-share indicators), and the participation ratio is a second-order statistic with no special standing in QR-006b. Classifying transition *order* is a separate question.
- **Wiki holdings.** CCA-1c, STAT3, STAT6 (Brown 2022), EWS3 (transitions without warning), EWS7 (covariance-eigenvalue indicators), M3 (hysteresis).
- **Starting literature (not yet verified this session):** Brown, Bossomaier & Barnett 2022 (*Sci. Rep.*; transfer entropy across Potts q = 5, 7, 10); the standard finite-size methods for telling first-order from continuous transitions — the energy cumulant (Challa, Landau & Binder 1986, *PRB* 34:1841) and the free-energy-barrier method (Lee & Kosterlitz 1990, *PRL* 65:137). These are the baselines any new discriminator has to beat. (Janke, Johnston & Kenna 2004, sometimes cited here, does not address transition order.)
- **Triviality warning (carried over).** CCA's first-order jump may simply be the order-parameter jump seen through S(k = 0). The CCA-1c reduction test, still unrun, decides that; if it reduces, QR-007 folds.
- **What would decide it.** The reduction test, then a comparison against standard order-discrimination methods on Potts q = 2, 5, 7, 10.
- **Two settings, not one (2026-10-18 discussion).** CCA-1c was scored on an *equilibrium* temperature sweep, across the transition. For use as a warning (QR-008) the order must be read from data taken *before* the transition, which CCA has never been tested on. In a driven system the outcome also depends on noise against barrier height. At low noise, with hysteresis, the jump happens at the spinodal. The spinodal is a fold bifurcation, so critical slowing down does precede it (the lake experiments, EWS2). At high noise or large system size, the jump comes earlier through nucleation, with little or no slowing down. *Established* (standard nucleation and bifurcation theory).
- **Status:** Raised, 2026-10-18. **FOLD (equilibrium setting), 2026-10-18** — tag `trivial-from-known-result`. The CCA-1c reduction test reduces (`experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md`). Since tr χ = N(q − 1) is fixed, d_eff = 1/[f₁² + (1 − f₁)²/d_bulk], with the top-mode share f₁ ≈ ⟨M²⟩. The first-order jump is the order-parameter jump seen through S(k = 0). With λ₁ removed, the spectrum's participation ratio falls rather than jumps. Not gated: no question remains to gate. The pre-transition / driven setting (QR-008, problem 1) is untouched by this test. **Merged into QR-008, 2026-10-18.**

## QR-008 · Classify, then measure: can a transition's type be identified first, and the best indicators for that type then used?

- **Question.** Can a two-stage early-warning tool work? Stage 1 identifies the kind of transition approaching:
  - bifurcation type (fold, Hopf, transcritical);
  - mechanism (bifurcation-, noise- or rate-induced tipping);
  - first-order or continuous.

  Stage 2 then applies the indicators that QR-006b's benchmark finds best for that type. Does the pair beat a single classifier or a single indicator at matched false-alarm rates?
- **Why the wiki raises it.** The owner's synthesis (2026-10-18). It joins QR-007 (can one measure classify the type?) to QR-006b (which indicator works for which type?), and descends from the earlier D_eff / CCA transition-classification work. QR-007 was merged into it the same day.
- **Carried over from QR-007 (merged 2026-10-18).**
  - *The wiki's own candidate is gone.* CCA's equilibrium order discriminator folded: the d_eff jump is the order-parameter jump read through λ₁ (CCA-1c Retired; `experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md`). The wiki has no measure of its own for reading order before a transition.
  - *Equilibrium baselines,* for any order discriminator that is scored across the transition: the energy cumulant (Challa, Landau & Binder 1986) and the free-energy-barrier method (Lee & Kosterlitz 1990). Not verified this session.
  - *Driven systems behave differently* (QR-007's "two settings" note). At low noise, with hysteresis, a first-order jump happens at the spinodal, which is a fold bifurcation, so slowing down precedes it. At high noise or large system size, it comes earlier by nucleation, with little warning. So "first-order or continuous" is partly a question of noise against barrier height, not only of the system. *Established.*
- **Prior art already in the wiki (stage 1).** EWS9: Bury et al. 2021 (*PNAS*) train a classifier that warns of a transition and predicts its bifurcation type (fold, Hopf, transcritical or none) ahead of time. Successor work extends this to more bifurcation types (from memory, not checked). Fitting the drift and diffusion of a Langevin model also reconstructs the stability landscape, which amounts to classification. Stage 1 is therefore prior art for bifurcation type.
- **Possibly open (provisional, no search run):** classifying the *mechanism* (B / N / R) and the *order* ahead of time; and using the predicted type to choose which indicators to trust.
- **Problems it must survive:**
  1. **Pre-transition data.** Stage 1 must work before the transition. CCA was only ever scored across one, and that result folded (above).
  2. **Types that leave no trace.** Noise- and rate-induced tipping can give no warning (EWS3), and the classical signals also precede smooth, non-catastrophic transitions (Kéfi et al. 2013, from memory). A classifier cannot sort what leaves nothing in the data.
  3. **Errors compound, and stage 1 may already be the warning.** A misclassified type picks the wrong indicators, and Bury's classifier warns and classifies in one step. The two-stage design earns its place only if stage-2 indicators add skill beyond the classifier's own output, which is testable.
- **Scoring requirement 1: actionable lead time.** Score the warning time *minus the response time of the intended intervention*, not warning time alone. A few seconds is useless for policy and enough for an automated controller.
- **Scoring requirement 2: prediction and detection kept apart.**
  - *Prediction* means warning before the transition begins, from slowing down or other precursors. It is limited by record length in units of the system's recovery time, not by sampling rate: once the sampling interval is shorter than the recovery time, extra samples are largely redundant. *Established* (effective sample size ≈ record length / recovery time).
  - *In-progress detection* means catching a transition already under way: a nucleating patch, or an escape trajectory leaving the basin. High sampling rate and spatial coverage help here. Lead time is short, about the duration of the escape, but can be enough for an automated response.
  - Score and report the two separately. The seizure field draws this line explicitly: prediction (minutes to hours ahead) mostly failed, while onset detection (seconds) is in clinical use in responsive neurostimulation. Other fast-detection practice: deep-learning disruption predictors in fusion plasmas, tens to hundreds of milliseconds ahead (Kates-Harbeck et al. 2019, *Nature*); grid protection on phasor measurements; thermoacoustic onset control. *All from memory, not verified this session.*
- **Depends on:** QR-006b's benchmark (stage 2 is its type-by-indicator table). Whether type can be read before the transition, formerly QR-007, is now this entry's own stage-1 question.
- **Status:** Raised, 2026-10-18. Not gated; gate after QR-006b's benchmark exists.

## QR-001 · Why is nature describable with so few parameters?

- **Question.** Is there a measurable, domain-general signature of when a complex system — biological, ecological, economic — admits a low-dimensional effective description, and when it does not?
- **Why the wiki raises it.** It is the honest descendant of "effective dimensionality as the hidden variable" (Ax2, P5–P7). The map puts RG, information geometry and sloppy models side by side.
- **Wiki holdings.** RG01, RG04, M4 (Mori–Zwanzig), M6, IT03, IT05, P5, P7; sloppy models arriving via the fold-in (Machta 2013). Coverage is good.
- **Starting literature:** Machta, Chachra, Transtrum & Sethna 2013 (*Science* 342:604; anchored); Transtrum et al. 2015 (*J. Chem. Phys.* 143:010901); Quinn et al. 2023 (*Rep. Prog. Phys.*).
- **What would decide it.** A predictor of compressibility, such as the eigenvalue-spectrum shape of the Fisher information, tested on model classes from different fields before fitting.
- **Status:** Raised. **Parked 2026-10-18** (owner) until QR-006b and QR-004 are finished. Reason: the established answer is the sloppy-models programme already in the wiki (Machta 2013; Transtrum 2015), and mapping it would mostly fold the wiki's own versions (P5–P7); nothing decidable by us.

## QR-002 · Are living systems poised at criticality, and what tunes them there?

- **Question.** Is the apparent criticality of neural, genetic and collective biological systems real, and if so is it selected, self-organised, or an artefact of how the data are analysed?
- **Why the wiki raises it.** It descends from the regimes and three-state thread (H1, X0). Criticality entries link to biology mainly through information theory.
- **Wiki holdings.** C3, STAT3, the criticality glossary page. **Gap:** almost no biological-criticality entries.
- **The wiki's own candidate answer: STAT3** (Constrained Critical Attractor class; **Speculative**, downgraded 2026-10-18). Its answer to "what tunes them there?" is that nothing does: a non-local constraint the system cannot break holds it at criticality. Its core members, self-organised criticality (Bak–Tang–Wiesenfeld 1987) and neural criticality (Beggs & Plenz 2003), are this question's subject. Its own contribution is narrower than it claims. "No tuning needed" is already the defining idea of self-organised criticality, so what STAT3 adds is the wider grouping (Riemann zeros, critical magnets, black-hole horizons) and the "constraint" framing. Its "no prior literature unifies these" claim has never been gated.
- **Shared work.** QR-002's literature mapping is also STAT3's prior-art gate: one reading, starting with Muñoz 2018 (which, from memory, reviews the proposed self-tuning mechanisms), settles both.
- **Starting literature:** Mora & Bialek 2011 (*J. Stat. Phys.*); Muñoz 2018 (*Rev. Mod. Phys.* 90:031001).
- **What would decide it.** Criticality tests that survive known artefacts (subsampling, thresholding, latent common drivers); evidence of a tuning mechanism.
- **Status:** Raised. **Parked 2026-10-18** (owner) until QR-006b and QR-004 are finished. Reason: a large, contested field with almost no wiki coverage; its main payoff here would be settling STAT3, which is already Speculative and a classification rather than a testable claim. If wanted later, one review (Muñoz 2018) settles STAT3's novelty claim.

## QR-003 · What sets biological and urban scaling exponents, and why is there no universal one?

- **Question.** The network-delivery theories (WBE for organisms, Bettencourt for cities), Dynamic Energy Budget theory and Glazier's metabolic-level boundaries predict different exponents and different dependence on dimension. Can they be tested against each other across organisms, cities and engineered networks, where the embedding dimension and network type differ?
- **Why the wiki raises it.** It descends from P2, P11 and P12; C1 and C2 sit side by side on the map.
- **Wiki holdings.** C1, C2, H5, X1, and soon WBE 1997, the allometric-cascade debate, metabolic-level boundaries, DEB and Bettencourt 2013 as reference entries (fold-in in progress). Coverage will be good.
- **Starting literature:** West, Brown & Enquist 1997; Bettencourt 2013 (verified 2026-10-18: δ = H/[D(D+H)] ≈ 1/6); Glazier 2010; Kooijman (DEB); Kolokotrones 2010 and its replication record (in C1).
- **What would decide it.** Each theory's prediction for a system it was not built for (WBE for a planar network, Bettencourt for a 3-D one), checked against data.
- **Status:** Raised. **Parked 2026-10-18** (owner) until QR-006b and QR-004 are finished. Reason: the wiki's own scaling claims have mostly folded or been falsified; the open cross-theory test is a large project. P14a stays runnable separately.

## QR-004 · How close do living systems run to the thermodynamic limits of information processing?

- **Question.** Do cells, organisms and ecosystems operate near Landauer and thermodynamic-uncertainty bounds when sensing, signalling and regulating, and what does running near those bounds buy them?
- **Why the wiki raises it.** It is the real version of P15's retired "cost of coherence". It runs through the map's biggest genuine hubs (Second Law TD3, Shannon INFO1, Landauer B5) into biology.
- **Wiki holdings.** TD3, INFO1, INFO2, INFO4, INFO5, B5, BIO5, F1, F5, plus adjacent IT06, NE03–NE06 and BIO10. **Corrected 2026-10-18** (`gsw-qr004-corrections-2026-10-18`, owner-approved; [report](prior_art_reviews/QR004_CORRECTIONS_2026_10_18.md)): the map's §F errors were applied as dated banners across 59 sections, 20 link descriptions and 3 facet values; tag `landauer-scope-overreach`; IT06 left for a separate check. **Folded in 2026-10-18** (`gsw-qr004-fold-in-2026-10-18`; [report](prior_art_reviews/QR004_FOLD_IN_2026_10_18.md)): 13 reference entries close the gaps listed below:
  - NE07 Bennett reversibility;
  - NE08 generalised and finite-time Landauer;
  - NE09 TUR;
  - NE10 cost of oscillation and synchronization;
  - BIO17 kinetic proofreading;
  - BIO18 speed over accuracy;
  - BIO19 copying;
  - BIO20 Berg–Purcell;
  - BIO21 cost of adaptation;
  - BIO22 neural cost per bit;
  - BIO23 cellular efficiency and the open question;
  - BIO24 motors;
  - BIO25 information-limited chemotaxis.
- **Gaps.** No TUR; no kinetic proofreading (Hopfield); no Bennett reversible computation as its own result; no sensing limits (Berg–Purcell); no cost of oscillation or synchronization; no motor energetics; no measured energy-per-bit figures (Laughlin, Kempes). Map §G proposes 13 reference entries (R1–R13), owner's call.
- **Starting literature:** Bérut et al. 2012 (Landauer test); Barato & Seifert 2015 (*PRL* 114:158101); Lan et al. 2012 (*Nat. Phys.* 8:422, energy–speed–accuracy in sensory adaptation).
- **What would decide it.** Measured dissipation versus precision for specific biochemical networks, compared with the bound.
- **Status:** **Literature-mapped (partial)** 2026-10-18: [`prior_art_reviews/QR-004_THERMO_LIMITS_LITERATURE_MAP_2026_10_18.md`](prior_art_reviews/QR-004_THERMO_LIMITS_LITERATURE_MAP_2026_10_18.md). It is partial because several primary texts were read at abstract level only. Headline:
  - **The first half is answered.** Cells sit far above Landauer: about 10× for translation, up to ~10⁸× for neural signalling. The field knows why: most processes are not erasures, and speed and accuracy cost energy.
  - **Against the bounds that do apply** (TUR, proofreading, sensing), several machines sit within about 2–6× (kinesin, *E. coli* adaptation, T7 polymerase); others are far (ribosome, chaperones, clocks).
  - **The second half is open in the literature.** "What does running near the bound buy?" is framed as open by Yang et al. 2021; the evidence so far says machines are tuned for speed.
  - **P15/Q5's "cost of coherence" has a published answer** (Zhang et al. 2020): cost diverges as synchrony becomes perfect, the reverse of the retired ansatz.
  - **Sub-questions closed out 2026-10-18** (owner decision; S1–S7 as defined in map §H). This is a disposition, not a formal gate run, except where stated:
    - **S1–S3 — answered, folded.** S1: how far cells sit from Landauer, and why. S2: whether proofreaders sit on their error–cost bound. S3: what coherence and synchronization cost. The literature map plus the fold-in's primary-source readings act as the Gate-1 search, verdict `answered`. The answers are now reference entries: NE07, NE08, BIO22, BIO23 (S1); BIO17, BIO18 (S2); NE10 (S3).
    - **S4–S5 — open in the literature; recorded, not pursued.** S4: a sensing or regulation process compared with the TUR using *measured* dissipation. S5: whether surplus dissipation buys fitness (KaiC). Framed as open by Yang et al. 2021 and Horowitz & Gingrich 2020; S5 is Zhang et al. 2020's untested prediction. Deciding either needs wet-lab measurement we cannot make; Gate 2 not run.
    - **S7 — dropped.** Landauer or TUR results at organism or ecosystem scale. The map's reason: the bounds need conditions (a defined Markov model with identifiable currents and a bath) that ecosystems do not meet, and maximum-entropy-production-style claims have failed (`ill-posed`; `expert-avoided-for-known-reason`). Gate 2 not formally run.
    - **S6 — still open:** does the synchronization-cost threshold depend on topology or spatial dimension, beyond Zhang's mean-field model? See Next.
- **Next.** Owner decisions, in order:
  1. *Done 2026-10-18:* §F corrections applied and all 13 §G entries folded in. Hopfield 1974, Lan 2012 and Terauchi 2007 were re-read in full and Laughlin 1998 at abstract level. IT06 follow-up done 2026-10-18 (`gsw-it06-geodesic-check-2026-10-18`, commit 6aaece6; [report](prior_art_reviews/IT06_GEODESIC_CHECK_2026_10_18.md)): the slow-driving dissipation metric is the friction tensor, Fisher–Rao only for constant relaxation time; X8's bound mis-stated; P21 instance (4) withdrawn, label unchanged; the Fisher–gravity chain does not depend on IT06.
  2. **Only S6 remains — skipped for now (owner, 2026-10-18).** If resumed: run both gates on it (`QUESTION_GATES.md`) only if the owner wants it pursued. It is the one sub-question that may be both unasked and decidable in-house (simulate thermodynamically consistent stochastic oscillators on lattices or networks of varying dimension). Prior art to check first: Kuramoto-on-lattices results (lower critical dimension; Hong, Chaté, Park & Tang 2005/2007), Chudak, Esposito & Ptaszyński 2026, and Burnet et al. 2026. **Drift warning:** it revives the wiki's d_f thread, where the owner's prior is strongest. Without S6, QR-004 is complete for the wiki's purposes; treat it as closed unless S6 is resumed.
  3. ~~S1–S3 fold; S4–S5 record; S7 DROP~~ — done 2026-10-18 (see Status).

## QR-005 · Is gravity quantum, or thermodynamic?

- **Question.** Will tabletop experiments show gravity carrying quantum information (mediating entanglement), or the decoherence and force noise that entropic and thermodynamic models predict?
- **Why the wiki raises it.** It is the testable form of the Fisher–gravity and entropic-gravity strand, and of the owner's information-first worldview.
- **Wiki holdings.** The thermodynamic and holographic side is well covered: GT01–GT08, GT10, HB01–HB10, BR01–BR05, plus IT02–IT05 on the Fisher–gravity chain. GT05 was corrected 2026-10-18. The map (§F) found 27 errors or needed qualifications in these entries, none applied (proposed tag `emergent-read-as-classical`). Examples:
  - GT10 says gravity is "not transmitted by gravitons";
  - GT10→IT03 "δS_EE = 0 ⇔ δD_KL = 0";
  - GT01's Λ "exactly as in Einstein–Hilbert";
  - GT03's "expansion halts";
  - GT04's Bianconi description;
  - HB01's "bits per unit volume";
  - HB02's "exactly entanglement entropy";
  - the BR03/HB07 RT-surface contradiction;
  - three wrong anchors (two on GT02, one on HB09).
- **Gaps.** The experimental side of the question is empty. The wiki has no entry on:
  - gravitationally mediated entanglement (BMV) or its interpretation debate;
  - the classical-channel model and its exclusion;
  - Oppenheim's classical-quantum gravity;
  - Diósi–Penrose collapse and its underground bounds;
  - semiclassical (Schrödinger–Newton) gravity;
  - the minimum-noise theorems;
  - quantum matter in external gravity;
  - the mass gap;
  - graviton detectability;
  - the scope of microstate counting;
  - the Page curve;
  - Verlinde 2016 as its own theory.

  Map §G proposes 14 reference entries (R1–R14), owner's call.
- **Starting literature:** Bose et al. 2017 (*PRL* 119:240401); Marletto & Vedral 2017 (*PRL* 119:240402); Carney, Karydas, Scharnhorst, Singh & Taylor 2025 (*PRX* 15:031038, **verified 2026-10-18**: free-energy models, with S_FF(0) force noise and decoherence signatures; the non-local λ = 0 model is already excluded).
- **What would decide it.** A gravitational-entanglement witness, or the absence of predicted excess decoherence and force noise, at the relevant mass and separation scales.
- **Status:** **Literature-mapped (partial)** 2026-10-18; un-parked 2026-10-18 at owner's request. Map: [`prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md`](prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md). Primer for the owner: [`primers/QR-005_GRAVITY_PRIMER.md`](primers/QR-005_GRAVITY_PRIMER.md). It is partial because most sources were read at abstract level and several numbers are flagged unresolved (map §I). Headline:
  - **"Quantum vs thermodynamic" is largely a false dichotomy.** Every thermodynamic derivation of gravity, like black-hole thermodynamics, rests on ħ-dependent quantum inputs. It concerns the field equations and is silent on whether the field is quantized. The live rivals to quantum gravity are *classical or noisy* gravity and collapse models.
  - **Already excluded:** the pairwise classical channel (Altamirano et al. 2018); parameter-free Diósi–Penrose (Donadi et al. 2021; now R₀ > 4.5 × 10⁻¹⁰ m, XENONnT 2026); Oppenheim's "noise everywhere" kernel; Carney et al.'s non-local λ = 0 model.
  - **Open in the literature:** what a positive entanglement witness would prove. It rules out LOCC-type classical gravity, but proving gravitons needs extra assumptions; framed by Bose et al. *RMP* 2025, Huggett et al. 2022 and Fragkos et al. 2022. Classical entanglement claims (Trillo & Navascués 2025; Aziz & Howl 2025) are contested.
  - **Not decidable by us.** The mass gap is ~7.5 orders of magnitude in superposed mass and ~10 in measured source mass, and the noise route is ~9 orders short. No published timeline exists.
  - Flagged: the question closest to the owner's own gravity strand, where an aesthetic prior can stand in for evidence (primer §(e)).
- **Next.** Owner decisions, in order:
  1. Whether to apply map §F (27 corrections; tag `emergent-read-as-classical`), including the three anchor fixes.
  2. Whether to fold in §G entries, R1–R6 first. Before R3, do the small Mode A reconciliation S5: the Janse 2024 and Oppenheim 2023 windows disagree.
  3. Whether to run the gates. Gate 1 looks headed for `open-in-literature` for the question as worded, and `answered` for its thermodynamic half (S1). S7 is a DROP candidate.

  Nothing is runnable in-house beyond the S5 bookkeeping.

---

## Coverage gaps the log has surfaced

- **Tipping points and early-warning signals (QR-006):** largely filled 2026-10-18 by EWS1–EWS10 (critical slowing down, tipping types, false alarms, information-flow, Fisher-index, eigenvalue, deep-learning and permutation-entropy indicators). Still thin: Fath et al. 2003 and Kritzman et al. 2011 (anchored, not read), and Prokopenko et al. 2011 (abstract only; a lead for IT10).
- **Criticality in biology (QR-002):** almost no entries.

## Changelog

- **2026-10-18** — Log started with QR-001 to QR-006, drawn from the big-picture review after the consistency pass. QR-006 marked priority by the owner; literature mapping launched.
- **2026-10-18** — QR-006 literature-mapped (partial); map saved under `docs/prior_art_reviews/`. Headline: information-theoretic early warning is unproven against the classical signals; the decisive test (a common-benchmark ROC comparison) appears not to have been done.
- **2026-10-18** — QR-006 coverage gap filled: EWS fold-in added EWS1–EWS10 (audit_ref `gsw-ews-fold-in-2026-10-18`; report `prior_art_reviews/EWS_FOLD_IN_2026_10.md`). Changed only QR-006's "Wiki holdings" line and the coverage-gaps bullet.
- **2026-10-18** — Gate 2 (worth-asking, `QUESTION_GATES.md`) added to the status ladder. QR-006b added: the re-scoped, regime-stratified benchmark, gated PROCEED (provisional); the linear-Gaussian half folded. QR-007 (transition-order classification by correlation-matrix observables) split out of QR-006 and raised.
- **2026-10-18** — QR-006b second, independent prior-art search (`prior_art_reviews/QR-006b_SECOND_SEARCH_2026_10_18.md`). The *Entropy* 28:628 review was read in full and is not prior art. Verdict: PROCEED still provisional, narrowed: not overturned; baseline re-scope recommended; Gaussian-copula sub-case folded; four unread items listed. Only QR-006b's status line changed.
- **2026-10-18** — Harris et al. 2024 Supplemental Table S1 read (arXiv ancillary file; report §7). Not the QR-006b study. It supports the baseline re-scope: under unknown noise amplitude no information feature reaches the top 100, and distribution-shape features win. Open items now three.
- **2026-10-18** — QR-006b baselines widened (owner-approved): an information indicator must now beat AC1 and variance, their rank-based versions, and the regime-appropriate distributional and model-based indicators. Original wording kept in the entry.
- **2026-10-18** — QR-008 raised (classify, then measure; owner's synthesis), with two scoring requirements: actionable lead time, and prediction scored separately from in-progress detection. QR-007 gains a note separating the equilibrium setting from the driven one (spinodal vs nucleation).
- **2026-10-18** — QR-007 folded for the equilibrium setting: the CCA-1c λ₁ reduction test reduces (`experiments/CCA1C_LAMBDA1_REDUCTION_TEST_2026_10_18.md`; audit_ref `gsw-cca1c-lambda1-reduction-2026-10-18`). Only QR-007's status line changed (tag `trivial-from-known-result`).
- **2026-10-18** — QR-007 merged into QR-008 (owner): the equilibrium form had folded, and the pre-transition form is QR-008's stage 1. QR-002 gains STAT3 as the wiki's own candidate answer (STAT3 downgraded to Speculative the same day, audit_ref `gsw-stat3-downgrade-2026-10-18`); QR-002's literature mapping doubles as STAT3's prior-art gate.
- **2026-10-18** — Owner review of the open questions. Active: QR-006b (readings, then benchmark design) and QR-004 (literature mapping). QR-008 waits on QR-006b. Parked until those two finish: QR-001, QR-002, QR-003, QR-005 (reasons in each entry). "Parked" added to the status ladder.
- **2026-10-18** — QR-004 literature-mapped (partial); map saved as `prior_art_reviews/QR-004_THERMO_LIMITS_LITERATURE_MAP_2026_10_18.md`. Headline: cells sit far above Landauer, and the field already knows why. Several machines sit within a few-fold of the TUR and process-specific bounds; what that closeness buys is open in the literature. Found 28 wiki errors or needed qualifications, none applied (proposed tag `landauer-scope-overreach`). Only QR-004's holdings, gaps, status and next lines changed. No gates run; no DB writes.
- **2026-10-18** — QR-006b readings closed (second-search report §8): **PROCEED with named gaps**. Eason 2014 clean (full text); Dakos & Soler-Toscano 2017 and Mormann 2005 unobtainable, named gaps. Pre-registered benchmark design written (`experiments/QR006B_BENCHMARK_PREREGISTRATION.md`); nothing run. Only QR-006b's status, "Provisional until" and "Next" lines changed.
- **2026-10-18** — QR-004: map §F corrections applied (`gsw-qr004-corrections-2026-10-18`; tag `landauer-scope-overreach`; IT06 deferred) and 13 reference entries folded in (NE07–NE10, BIO17–BIO25; `gsw-qr004-fold-in-2026-10-18`), both owner-approved. Status unchanged. Only QR-004's holdings and next lines changed.
- **2026-10-18** — QR-006b pilot run and protocol frozen (`experiments/QR006B_PILOT_REPORT_2026_10_18.md`; tag `qr006b-prereg-frozen`). The pilot passed; its results are discarded. The confirmatory run has not started. Only QR-006b's "Next" line changed.
- **2026-10-18** — QR-004 sub-questions closed out (owner): S1–S3 answered and folded into NE07–NE10/BIO17–BIO23; S4–S5 recorded as open-in-literature, not pursued (need wet-lab data); S7 dropped. Only S6 remains, pending an owner decision to gate it. Only QR-004's status and next lines changed.
- **2026-10-18** — QR-006b post-freeze deviations D1 (early-cut decisive score) and D2 (C0g MI tolerance), owner-approved, before any confirmatory data. Only QR-006b's "Next" line changed.
- **2026-10-18** — QR-005 un-parked at the owner's request and literature-mapped (partial): map `prior_art_reviews/QR-005_GRAVITY_QUANTUM_VS_THERMO_MAP_2026_10_18.md`, primer `primers/QR-005_GRAVITY_PRIMER.md`. Headline:
  - "quantum vs thermodynamic" is largely a false dichotomy: thermodynamic derivations use quantum inputs and are silent on quantization;
  - the testable rivals are classical or noisy gravity and collapse models, several already excluded;
  - what an entanglement witness would prove is open in the literature;
  - the experiments are 7.5–10 orders of magnitude away.

  Found 27 wiki errors or needed qualifications, none applied (proposed tag `emergent-read-as-classical`). Only QR-005's holdings, gaps, status and next lines changed. No gates run; no DB writes.
