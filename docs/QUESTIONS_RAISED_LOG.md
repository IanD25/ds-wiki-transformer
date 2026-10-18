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
- **Status:** **Gated — PROCEED (still provisional, narrowed)**, 2026-10-18, after the second, independent search ([report](prior_art_reviews/QR-006b_SECOND_SEARCH_2026_10_18.md)). Not overturned: no study found runs the regime-stratified, matched-false-alarm benchmark. Partial answers turned up under other vocabulary: seizure-prediction ROC comparisons found no univariate nonlinear advantage over linear measures (Mormann 2005, abstract), and a feature screen under unknown noise found distribution-shape features winning (Harris et al. 2024, *PRX*). Baselines widened accordingly (owner-approved 2026-10-18; see the question above). The Gaussian-copula sub-case folds (`trivial-from-known-result`). Harris 2024 Table S1 has since been read (report §7). Under unknown noise amplitude, 244 information features beat AC1, but none reaches the top 100; distribution-shape features win, which backs the baseline re-scope. Confirm PROCEED on the re-scoped form once three unread items come back clean: Dakos & Soler-Toscano 2017, Mormann 2005 and Eason 2014, in full.
- **Provisional until:** ~~(1) a second, independent search fails to find the study~~ — done 2026-10-18, not overturned. Still open: Dakos & Soler-Toscano 2017 (full text), Mormann et al. 2005 (full text: measure list and per-measure ROC), Eason et al. 2014 (results). ~~Harris et al. 2024 Supplemental Table S1~~: read 2026-10-18, not the study (report §7). If these come back clean, PROCEED is confirmed on the re-scoped form; if one contains the study, that regime FOLDs (`found-under-other-vocabulary`).
- **Next:** read the three open items; then a pre-registered benchmark design on the Bury et al. 2021 scripts and records (CC BY-NC-SA 4.0) and the Weinans model family.

## QR-007 · Can correlation-matrix observables classify a transition's order?

- **Question.** Can observables of the connected correlation matrix (participation ratio, eigenvalue concentration) tell a first-order transition from a continuous one, on data where the order is known — and do they carry anything beyond the order-parameter jump and existing order-discrimination methods?
- **Why the wiki raises it.** It is CCA's distinct angle, split out of QR-006 by the QR-006b gate report: as a *warning* signal, correlation-matrix concentration is a restatement (dynamical network biomarkers, eigenvalue-share indicators), and the participation ratio is a second-order statistic with no special standing in QR-006b. Classifying transition *order* is a separate question.
- **Wiki holdings.** CCA-1c, STAT3, STAT6 (Brown 2022), EWS3 (transitions without warning), EWS7 (covariance-eigenvalue indicators), M3 (hysteresis).
- **Starting literature (not yet verified this session):** Brown, Bossomaier & Barnett 2022 (*Sci. Rep.*; transfer entropy across Potts q = 5, 7, 10); the standard finite-size methods for telling first-order from continuous transitions — the energy cumulant (Challa, Landau & Binder 1986, *PRB* 34:1841) and the free-energy-barrier method (Lee & Kosterlitz 1990, *PRL* 65:137). These are the baselines any new discriminator has to beat. (Janke, Johnston & Kenna 2004, sometimes cited here, does not address transition order.)
- **Triviality warning (carried over).** CCA's first-order jump may simply be the order-parameter jump seen through S(k = 0). The CCA-1c reduction test, still unrun, decides that; if it reduces, QR-007 folds.
- **What would decide it.** The reduction test, then a comparison against standard order-discrimination methods on Potts q = 2, 5, 7, 10.
- **Status:** Raised, 2026-10-18. Not gated.

## QR-001 · Why is nature describable with so few parameters?

- **Question.** Is there a measurable, domain-general signature of when a complex system — biological, ecological, economic — admits a low-dimensional effective description, and when it does not?
- **Why the wiki raises it.** It is the honest descendant of "effective dimensionality as the hidden variable" (Ax2, P5–P7). The map puts RG, information geometry and sloppy models side by side.
- **Wiki holdings.** RG01, RG04, M4 (Mori–Zwanzig), M6, IT03, IT05, P5, P7; sloppy models arriving via the fold-in (Machta 2013). Coverage is good.
- **Starting literature:** Machta, Chachra, Transtrum & Sethna 2013 (*Science* 342:604; anchored); Transtrum et al. 2015 (*J. Chem. Phys.* 143:010901); Quinn et al. 2023 (*Rep. Prog. Phys.*).
- **What would decide it.** A predictor of compressibility, such as the eigenvalue-spectrum shape of the Fisher information, tested on model classes from different fields before fitting.
- **Status:** Raised.

## QR-002 · Are living systems poised at criticality, and what tunes them there?

- **Question.** Is the apparent criticality of neural, genetic and collective biological systems real, and if so is it selected, self-organised, or an artefact of how the data are analysed?
- **Why the wiki raises it.** It descends from the regimes and three-state thread (H1, X0). Criticality entries link to biology mainly through information theory.
- **Wiki holdings.** C3, STAT3, the criticality glossary page. **Gap:** almost no biological-criticality entries.
- **Starting literature:** Mora & Bialek 2011 (*J. Stat. Phys.*); Muñoz 2018 (*Rev. Mod. Phys.* 90:031001).
- **What would decide it.** Criticality tests that survive known artefacts (subsampling, thresholding, latent common drivers); evidence of a tuning mechanism.
- **Status:** Raised.

## QR-003 · What sets biological and urban scaling exponents, and why is there no universal one?

- **Question.** The network-delivery theories (WBE for organisms, Bettencourt for cities), Dynamic Energy Budget theory and Glazier's metabolic-level boundaries predict different exponents and different dependence on dimension. Can they be tested against each other across organisms, cities and engineered networks, where the embedding dimension and network type differ?
- **Why the wiki raises it.** It descends from P2, P11 and P12; C1 and C2 sit side by side on the map.
- **Wiki holdings.** C1, C2, H5, X1, and soon WBE 1997, the allometric-cascade debate, metabolic-level boundaries, DEB and Bettencourt 2013 as reference entries (fold-in in progress). Coverage will be good.
- **Starting literature:** West, Brown & Enquist 1997; Bettencourt 2013 (verified 2026-10-18: δ = H/[D(D+H)] ≈ 1/6); Glazier 2010; Kooijman (DEB); Kolokotrones 2010 and its replication record (in C1).
- **What would decide it.** Each theory's prediction for a system it was not built for (WBE for a planar network, Bettencourt for a 3-D one), checked against data.
- **Status:** Raised.

## QR-004 · How close do living systems run to the thermodynamic limits of information processing?

- **Question.** Do cells, organisms and ecosystems operate near Landauer and thermodynamic-uncertainty bounds when sensing, signalling and regulating, and what does running near those bounds buy them?
- **Why the wiki raises it.** It is the real version of P15's retired "cost of coherence". It runs through the map's biggest genuine hubs (Second Law TD3, Shannon INFO1, Landauer B5) into biology.
- **Wiki holdings.** TD3, INFO1, INFO2, INFO4, INFO5, B5, BIO5, F1, F5. Coverage is good on the physics side, thinner on the measured biology.
- **Starting literature:** Bérut et al. 2012 (Landauer test); Barato & Seifert 2015 (*PRL* 114:158101); Lan et al. 2012 (*Nat. Phys.* 8:422, energy–speed–accuracy in sensory adaptation).
- **What would decide it.** Measured dissipation versus precision for specific biochemical networks, compared with the bound.
- **Status:** Raised.

## QR-005 · Is gravity quantum, or thermodynamic?

- **Question.** Will tabletop experiments show gravity carrying quantum information (mediating entanglement), or the decoherence and force noise that entropic and thermodynamic models predict?
- **Why the wiki raises it.** It is the testable form of the Fisher–gravity and entropic-gravity strand, and of the owner's information-first worldview.
- **Wiki holdings.** GT01, GT02, GT05 (corrected 2026-10-18), GT10, HB02, BR01. Coverage is good.
- **Starting literature:** Bose et al. 2017 (*PRL* 119:240401); Marletto & Vedral 2017 (*PRL* 119:240402); Carney, Karydas, Scharnhorst, Singh & Taylor 2025 (*PRX* 15:031038, **verified 2026-10-18**: free-energy models, with S_FF(0) force noise and decoherence signatures; the non-local λ = 0 model is already excluded).
- **What would decide it.** A gravitational-entanglement witness, or the absence of predicted excess decoherence and force noise, at the relevant mass and separation scales.
- **Status:** Raised.

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
