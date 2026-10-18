# QR-006 literature map — information-theoretic vs classical early-warning signals (2026-10-18)

> **Provenance (2026-10-18).** Literature map for Questions Raised Log entry **QR-006**, compiled by a read-only research agent. Read status is given per source in §H; several key sources (Barnett 2013, Fath 2003, Dakos 2012, Ditlevsen & Johnsen 2010) were **not read**. The main session has **not** re-verified these readings first-hand. The two derivations in §C2 and §G (Fisher Information index ≈ pooled-variance proxy; CCA's participation-ratio jump ≈ order-parameter jump through S(k=0)) are the agent's own and are **Speculative** until checked. Treat this as a starting map, not a gate verdict. **Corrections from the early-warning fold-in session's full-text reading (2026-10-18):** (a) Tirabassi & Masoller 2023's main text reports an entropy minimum before the transition in **5 of 6** satellite transects; the "6 of 6 vs 4 of 6" figure below was not found in the paper. (b) Bury et al. 2021's 268 test series are **not a single packaged benchmark**: they are spread across GitHub simulation scripts, PANGAEA and NOAA. (c) Barnett et al. 2013's transfer-entropy peak is in an equilibrium temperature sweep; any lead in time is only suggested.

Mode A (curation / grounding). Read-only. Confidence tags: **Established / Supported / Speculative**.
**Note on quotes:** I could not supply 1–2 verbatim quotes per source because a copyright constraint in this session allows only one short quote per response. I paraphrased instead and gave the location (section or line) so you can check each claim against the source. The one quote I used is in §D.

---

## (A) Answer in one paragraph

**No, not in any established way.** Critical slowing down (CSD) is the classical early-warning signal, read off as rising lag-1 autocorrelation (AC1) and rising variance. It is well grounded in theory for local bifurcations (fold, transcritical, Hopf), and it has been confirmed in controlled experiments. It fails, or gives false alarms, in documented ways. Every information-theoretic family has been *proposed* as an early or better warning: transfer entropy / information flow, mutual information, the ecological "Fisher Information index", permutation entropy, complexity measures, and correlation-matrix eigenvalue measures. Real head-to-head tests on the same data are **rare, mostly done on models, small, and inconsistent in their metrics**. The one multi-indicator benchmark I found that included an information-theoretic indicator (Weinans et al. 2021) found no overall winner. In it, mutual information was among the *least* robust to measurement noise and high dimension. The claims that Fisher information or information dissipation give a "leading indicator" come mostly from the method's own authors, on one or a few events, without ROC or null-model error rates. The only family with a systematic ROC win over AC1 and variance is deep learning (Bury et al. 2021), which is not information-theoretic. **Supported:** information-theoretic indicators are at best complementary to CSD. "Earlier or more reliable" is unproven.

---

## (B) Classical EWS: what works, what fails

**Theory (Established).** As the dominant eigenvalue of the linearised dynamics approaches zero, perturbations decay more slowly. Memory then rises (AC1) and shocks accumulate (variance). Scheffer et al. 2009 (*Nature* 461:53, full text read) set this out for the fold and note that it also applies to transcritical and Hopf bifurcations (Box 1–3; lines ~42–60, 366, 531 of the extracted text). They also warn that variance can in principle *fall* if slowing down reduces the system's ability to track forcing (around line 166).

**Experimental confirmation (Supported).**
- **Carpenter et al. 2011** (*Science* 332:1079; preprint full text read). Top predators were added to Peter Lake over three years, with an unmanipulated reference lake. Warning statistics appeared more than a year before the food-web transition was complete. The authors caution that warnings may fail if the system is forced too fast (preprint lines ~325–330).
- **Dai et al. 2012** (*Science* 336:1175; abstract only). Yeast populations with an Allee effect and a fold bifurcation recovered more slowly, and their fluctuations grew larger and lasted longer, as the collapse point approached.

**Climate applications (contested).**
- **Boers 2021** (*Nat. Clim. Change* 11:680; abstract via repository) reports significant EWS in eight AMOC fingerprint indices. Chen & Tung (Matters Arising, arXiv:2312.13568; abstract only) dispute the proxies.
- **Ditlevsen & Ditlevsen 2023** (*Nat. Commun.* 14:4254; full text paywall-redirected, so press and abstract only) fit variance and AC1 of a 1870–2020 SST fingerprint to a saddle-node model. They estimate collapse around 2025–2095 at 95% confidence, cannot distinguish partial from full collapse, and are widely questioned.

**Known failures (Established as categories).**
1. **No-warning transitions.** Scheffer 2009 itself lists three causes (lines 797–822): a rare extreme event moving the system between stable states without an approach to the threshold; a fast, permanent change in external conditions; and too-short records.
   - Ashwin et al. 2012 (*Phil. Trans. A* 370:1166; abstract only) formalise B-, N- and R-tipping (bifurcation-, noise- and rate-induced). R-tipping needs neither a bifurcation nor noise.
   - Ditlevsen & Johnsen 2010 (*GRL* 37, doi:10.1029/2010GL044486; not retrieved, known through citing papers): the absence of rising variance and inconclusive AC1 before Dansgaard–Oeschger events implies noise-induced tipping.
   - Hastings & Wysham 2010 (*Ecol. Lett.* 13:464; abstract via index): nonlinear models with environmental variability and no smooth potential can shift with no warning.
2. **False positives and selection bias.**
   - Boettiger & Hastings 2012 (*J. R. Soc. Interface*; arXiv:1204.6231, abstract read): error rates of common indicators are rarely reported and can be severe even under favourable assumptions.
   - Boettiger & Hastings, "prosecutor's fallacy" (arXiv:1210.1204; abstract only): choosing systems because they already tipped inflates apparent skill.
   - Jäger & Füllsack 2019 (*PLoS ONE* 14:e0211072; read via PMC): exponential, logistic and logarithmic trends produce rising SD and AC1 without any transition. Detrending removes this.
3. **Domain failures.**
   - Medicine: Wilkat, Rings & Lehnertz 2019 (*Chaos*, doi:10.1063/1.5122759; abstract and press) found no CSD before 105 seizures in 28 patients when tested against surrogates. Dynamics *sped up* instead.
   - Finance: Guttal et al. 2016 (*PLoS ONE* 11:e0144198; abstract) found rising variance but **no rising AC1** before major crashes over about a century of indices. They read crashes as stochastic transitions, not bifurcations.
4. **Methodological sensitivity.** Dakos et al. 2012 (*PLoS ONE* 7:e41010; bibliographic only, not read) is the standard methods paper. Results depend on the detrending bandwidth, window size and sampling. Ditlevsen & Ditlevsen 2026 (arXiv:2609.01164; abstract) show that observing variables not aligned with the critical direction can hide EWS until late. So absence of EWS is not evidence of safety.

---

## (C) Information-theoretic EWS by family

**C1. Information flow / transfer entropy.**
- **Claimed:** Barnett, Lizier, Harré, Seth & Bossomaier 2013 (*PRL* 111:177203; full text not read, commentary page read). Global transfer entropy (GTE) in the 2D Glauber Ising model peaks strictly on the *disordered* side of T_c, while mutual information peaks at T_c. They propose "TE has peaked and is falling while MI still rises" as a warning signal. The commentary itself says real-world applicability is untested. A Rényi follow-up (PRE 90:063308) reports pairwise TE also peaks on the disordered side.
- **First-order case:** Brown, Bossomaier & Barnett 2022 (*Sci. Rep.* 12:15145, doi:10.1038/s41598-022-17359-w; PMC full text read via summary). GTE also peaks on the disordered side for first-order Potts q = 5, 7, 10 in **finite systems only**. The peak converges to T_c as q and L grow, and for q > 7 GTE becomes discontinuous at T_c. They call this the first demonstration of early warning of a first-order transition. **There is no empirical data and no comparison with susceptibility, AC1 or variance.**
- **Tested empirically:** Quax, Kandhai & Sloot 2013 (*Sci. Rep.* 3:1898; PMC read via summary). Their "information dissipation length" (mutual information decaying across instruments in swap rates) rose before Lehman: the first clear warning came about 118 trading days ahead in USD and about 67 in EUR. AR(1) CSD gave no clear sustained signal. This is **one event**, with threshold-based warnings and no ROC.
- **Status:** Speculative as a practical EWS. The "early warning" is a peak in control-parameter space at equilibrium, not shown as lead time in a driven time series.

**C2. Fisher Information index (Cabezas / Fath / Pawlowski school).**
- **Lineage:** Fath, Cabezas & Pawlowski 2003 (*J. Theor. Biol.* 222:517; bibliographic only); Mayer, Pawlowski & Cabezas 2006 (*Ecol. Model.*; not retrieved); Karunanithi et al. 2008 (*Ecol. Soc.* 13; abstract via index).
- **The "sustainable regimes hypothesis"** (AIChE 2006 proceedings; abstract) says a regime is stable when FI is constant in time, and that a change in FI signals a regime shift.
- **Construction** (Spanbauer et al. 2014, *PLoS ONE* 9:e108936; **full text read**, Methods lines ~355–390). Split the multivariate series into windows of about 8–10 points. Set a "size of states" per variable from the standard deviation of the quietest window. Bin points into indistinguishable states, build p(s) by counting, and compute a shift-invariant FI per window.
- **Claims:**
  - Eason, Garmestani & Cabezas 2014 (*Clean Technol. Environ. Policy* 16:773; first page read) say variance, skewness, kurtosis and CSD fire only once a shift is "well underway", and that FI is a leading indicator.
  - Spanbauer 2014 compared FI with univariate variance, skewness, kurtosis and AC1 on a Foy Lake diatom record (109 species, about 800 steps). Univariate indicators were weak and inconsistent across species (lines 172–196). FI showed about 2,000 years of instability before the shift at ~1.3 ka. This is qualitative, one record, no significance test, and the authors overlap with the method's developers.
- **Critique:** Burnett 2019 (UNL PhD dissertation; abstract read). Under resampling, a "velocity" measure was more robust to data loss than FI or the Variance Index. Regime-detection metrics were "inconsistent, not generalizable" and not validated probabilistically. I found no published critique in a peer-reviewed journal.
- **Triviality check (my derivation, not found in literature; Supported as mathematics).** Shift-invariant (location) Fisher information of a Gaussian density is 1/σ². So when the windowed occupancy density broadens, FI falls. A declining FI index is therefore largely a **dispersion or variance proxy** after binning, plus some sensitivity to multimodality from flickering. This would explain why it "leads" univariate variance in multispecies data: it pools all variables, not because it uses information geometry.

**C3. Permutation entropy, sample entropy, complexity.**
- Tirabassi & Masoller 2023 (*PNAS* 120:e2215667120; full text via summary, power analysis in the SI not seen). Spatial PE against spatial correlation (Moran's I): PE was **worse** in one vegetation model and **better** in another. On satellite transects, PE rose before tipping in 6 of 6 and correlation in 4 of 6. They call the two complementary.
- A laser-threshold experiment (arXiv:2508.01000; abstract via search) has PE starting to fall well before the intensity rises.
- Dakos & Soler-Toscano 2017 (*Ecol. Complexity* 32:144; not read) on algorithmic complexity.
- **Status:** Speculative to Supported as complementary. Small studies.

**C4. Correlation-network / eigenvalue measures.**
- **Dominant eigenvalue of the dynamics:** Held & Kleinen 2004 (*GRL* 31:L23207; abstract via index), "degenerate fingerprinting": track the smallest decay rate of the dynamics. This is CSD itself in multivariate form.
- **Covariance-matrix eigenvalues:**
  - Brock & Carpenter 2006 (*Ecol. Soc.*; cited by Chen 2019, not read).
  - Chen, O'Dea, Drake & Epureanu 2019 (*Sci. Rep.* 9:2572; PMC read via summary) use the largest covariance eigenvalue **and its share of the eigenvalue norm**. These rose more sharply near the bifurcation than spatial variance or skewness, and stayed flat in a model with no bifurcation.
- **Dynamical network biomarkers (DNB):** Chen, Liu, Liu, Li & Aihara 2012 (*Sci. Rep.* 2:342; PMC read via summary). Near a bifurcation the dominant mode's variance diverges. A subgroup's internal correlations go to ±1, its correlations with the rest fall, and its SDs rise. The composite index was tested on three disease microarray datasets, against fold-change and random gene selection, **not against AC1 or variance**.
- **Finance:** Kritzman, Li, Page & Rigobon 2011 (*J. Portfolio Mgmt*; secondary only) define the "absorption ratio", the fraction of variance in the top eigenvectors, as a warning of market fragility.
- **Participation ratio / effective rank:** I found no paper using the participation ratio or effective rank of a correlation matrix as a named EWS. The closest are the explained-variance share and λ_max/‖λ‖, which are monotonically related to the same concentration.

**C5. Machine learning (benchmark only).** Bury et al. 2021 (*PNAS* 118:e2106140118; PMC read via summary). A CNN-LSTM trained on fold, transcritical and Hopf normal forms beat AC1 and variance on ROC in 6 of 8 comparisons. On paleoclimate records it roughly tied AC1. Exact AUC values are only in the figures. Dablander & Bury 2022 (PNAS letter) show that preprocessing strongly affects results. Dylewsky et al. 2022/23 (arXiv:2206.00060) extend this to spatial / Ising-like data.

---

## (D) Head-to-head evidence

Same data, information-theoretic indicator against variance / AC1 (or ML):

| Study | Indicators | Data | Metric | Result |
|---|---|---|---|---|
| Weinans et al. 2021, *Sci. Rep.* 11:9148 (PMC read via summary) | 13 multivariate indicators, incl. **mutual information**, explained variance, max covariance, MAF, degenerate fingerprinting, average AC / variance | 4D and 20D models, 6 data-degradation scenarios | Kendall τ against the bifurcation parameter (no ROC) | No overall winner. Average variance was best under reduced resolution. **MI was the most affected by measurement noise and failed in 20D** |
| Tirabassi & Masoller 2023 | spatial PE vs Moran's I | 2 models + satellite transects | power (SI) | mixed: PE better in 1 model and in the transects, worse in the other model |
| Quax et al. 2013 | information dissipation length vs AR(1) | Lehman swap rates | thresholded lead time | IDL led by about 3–6 months. n = 1 event |
| Spanbauer et al. 2014 | FI vs variance, skewness, kurtosis, AC1 | 1 paleo record | visual | FI flagged instability earlier. No statistics |
| Eason et al. 2014 | FI vs variance etc. | models + real systems | (not read) | FI "leading" (authors' claim) |
| Bury et al. 2021 | DL vs AC1 and variance | 268 empirical + model series | ROC | DL better in 6 of 8 comparisons |

Weinans et al. state the no-winner finding directly: "there is not one method outperforming the others" (abstract).

**Plain statement (Supported):** I found **no** study that compares transfer entropy against AC1 or variance on lead time or ROC, and **no** common-benchmark ROC study of permutation entropy, Fisher information or DNB against CSD. A July 2026 preprint (Ngueuleweu, arXiv:2607.11935; abstract only) claims a Kalman-estimated elasticity leads AR(1) by 14–24 months in NASA AIRS data. It is not information-theoretic and not yet reviewed.

---

## (E) First-order vs continuous

- **Dynamical systems view (Established).** CSD *does* apply to the fold, which is the classic hysteretic, "first-order-like" tipping point. The eigenvalue still goes to zero at the saddle-node, as in Scheffer 2009 Box 1. CSD fails when escape happens *before* the fold, through noise-induced or rate-induced tipping (Ashwin 2012, Ditlevsen & Johnsen 2010). In statistical-physics terms, that is nucleation out of a metastable state rather than reaching the spinodal.
- **Statistical-physics framing.** Hagstrom & Levin (arXiv:2110.12287; abstract only) name the paradox: CSD belongs to second-order transitions, yet real tipping looks first-order. They resolve it through spinodal instabilities, which do show precursors.
- **Non-catastrophic transitions show the same signals.** Kéfi et al. 2013 (*Oikos* 122:641; abstract) show the same EWS before non-catastrophic (continuous) transitions. So **CSD does not discriminate transition type**; it measures increasing sensitivity to perturbations.
- **Where information flow peaks.**
  - Ising (continuous): on the disordered side, above T_c (Barnett 2013).
  - First-order Potts: also on the disordered side, but only at finite L, and it converges to T_c as the transition sharpens (Brown 2022).
  - So "early" means *approached from the high-temperature (disordered) side* in a finite system. There is no evidence it gives any lead when approached from the ordered side, or in the thermodynamic limit for strongly first-order transitions.
- **Indicator choice by type.** I found no systematic literature result saying which indicators work for abrupt versus continuous transitions, beyond: CSD works for local bifurcations and is blind to N- and R-tipping, and flickering, skewness and bimodality are suggested for near-fold noisy systems.

---

## (F) Open sub-questions a researcher could take on

1. **Do information-theoretic indicators add ROC skill over AC1 and variance on a common benchmark?** Run PE, TE, MI, the Cabezas FI and the participation ratio on Bury 2021's public set of 268 transition and null series. Use identical windows and detrending, and report AUC with a surrogate null. *Decides it:* AUC differences with confidence intervals.
2. **Is the Cabezas FI index redundant with pooled variance?** Compute FI alongside the multivariate total variance and 1/σ² on models where variance is known to *fall* before transition (for example, time-delay systems). If FI tracks 1/variance, it is redundant there.
3. **Does the GTE peak give lead time in *time*, not just in T?** Slowly ramp T downward in Glauber Ising and Potts (q = 2, 10). Compute windowed GTE, AC1 and variance, and compare the first significant alarm. Then try a real slow-forcing record, such as the Peter Lake data.
4. **Does participation-ratio collapse add anything beyond explained variance or λ_max share?** Use Weinans 2021's degradation scenarios. Measure incremental Kendall τ or AUC with PR conditioned on λ₁/Σλ.
5. **Does any indicator beat chance for noise-induced, fold-like events?** Test on seizure iEEG (Wilkat dataset), crash indices (Guttal), and Dansgaard–Oeschger events in NGRIP. A negative result would be informative.

---

## (G) Relation to the wiki: prior-art verdicts (provisional)

**X0_FIM_Regimes vs the Fisher Information index (C2): ADJACENT.**
- **Shared:** the vocabulary and the idea that "Fisher information classifies stable regimes versus transitions".
- **Narrow difference:** Cabezas FI is a *scalar* shift-invariant FI of a binned, windowed state-occupancy density along a time trajectory. X0 reads the *singular-value spectrum* of a matrix built from a spatial correlation kernel. These are different mathematical objects.
- **Restatements inside X0 (my assessment):**
  - X0's three regimes (exponential correlations, critical/power-law, flat/ordered) restate the standard disordered / critical / ordered phase classification.
  - Prokopenko et al. 2011 (*PRE* 84:041116; abstract via index: FIM elements diverge or peak at second-order transitions) is the closer prior art for "FIM detects criticality".
  - X0's finance case ("one hub carries the information load", MAG7 concentration) is the absorption-ratio idea (Kritzman 2011), so it is **ADJACENT to RESTATEMENT** for that application.

**CCA participation-ratio collapse vs DNB / dominant-eigenvalue (C4).**
- **Generic use of correlation-matrix concentration as a transition signal: RESTATEMENT.** Concentration of covariance onto one dominant mode near a bifurcation is the multivariate form of CSD. It is in Chen 2012 (DNB), Brock & Carpenter 2006, Chen 2019 (λ_max share), Weinans 2021 (explained variance) and Kritzman 2011. A participation ratio near 1 is that concentration.
- **CCA's specific use: ADJACENT.**
  - **Narrow difference:** CCA uses the PR of an *equilibrium spatial* correlation matrix swept in temperature to *classify transition order*, not to forecast in a time series. I found no prior art for that classification use (NO PRIOR ART FOUND, provisional).
- **Triviality warning (my derivation; Speculative until checked against `scripts/cca_observables.py`).** On a periodic lattice the correlation matrix is circulant, so its eigenvalues are the structure factor S(k) (Established). If χ_ij = ⟨qδ⟩−1 keeps the disconnected order-parameter term, then in the ordered phase S(0) ≈ N·m², which gives PR = O(1). In the disordered phase S(k) is smooth, which gives PR = O(N). At a first-order T_c, m jumps, so PR jumps. The observed jump at q = 10, L = 32 from about 1.5 to about 370 (N = 1024) fits this O(1)→O(N) pattern. **The d_eff_CCA jump may be the order-parameter discontinuity seen through S(k = 0).** That is the "λ₁ ordering-mode collapse" already flagged in CLAUDE.md, and it is likely a 5-minute re-derivation, not new content.

---

## (H) Sources and read status

| Source | Read status |
|---|---|
| Scheffer et al. 2009, *Nature* 461:53, doi:10.1038/nature08227 | **Full text** (pdftotext) |
| Carpenter et al. 2011, *Science* 332:1079, doi:10.1126/science.1203672 | **Full preprint** |
| Spanbauer et al. 2014, *PLoS ONE* 9:e108936 | **Full text** |
| Eason, Garmestani, Cabezas 2014, *CTEP* 16:773, doi:10.1007/s10098-013-0687-2 | Abstract + page 1 only |
| Weinans et al. 2021, *Sci. Rep.* 11:9148, doi:10.1038/s41598-021-87839-y | Full text via fetch summary |
| Brown, Bossomaier, Barnett 2022, *Sci. Rep.* 12:15145 (PMC9452544) | Full text via fetch summary |
| Bury et al. 2021, *PNAS* 118:e2106140118 (PMC8488604) | Full text via fetch summary (no AUC numbers) |
| Chen et al. 2012, *Sci. Rep.* 2:342 (PMC3314989) | Full text via fetch summary (equations as images) |
| Chen, O'Dea, Drake, Epureanu 2019, *Sci. Rep.* 9:2572 | Full text via fetch summary |
| Quax, Kandhai, Sloot 2013, *Sci. Rep.* 3:1898 (PMC3667490) | Full text via fetch summary |
| Tirabassi & Masoller 2023, *PNAS* 120:e2215667120 (PMC9910486) | Full text via summary (SI not seen) |
| Jäger & Füllsack 2019, *PLoS ONE* 14:e0211072 | Full text via summary |
| Barnett et al. 2013, *PRL* 111:177203 | **Not read**; Sussex commentary page read |
| Boettiger & Hastings 2012 (arXiv:1204.6231); 2012/13 (arXiv:1210.1204) | Abstracts |
| Burnett 2019, UNL dissertation (natresdiss/299) | Abstract |
| Boers 2021, *Nat. Clim. Change* 11:680; Chen & Tung (arXiv:2312.13568) | Abstract / snippet |
| Ditlevsen & Ditlevsen 2023, *Nat. Commun.* 14:4254 | Paywall redirect; press + abstract only |
| Ditlevsen & Ditlevsen 2026 (arXiv:2609.01164); Ngueuleweu 2026 (arXiv:2607.11935) | Abstracts |
| Ashwin et al. 2012, *Phil. Trans. A* 370:1166 | Abstract |
| Hastings & Wysham 2010, *Ecol. Lett.* 13:464 | Abstract via index |
| Dai et al. 2012, *Science* 336:1175 | Abstract via secondary sources |
| Wilkat et al. 2019, *Chaos*; Guttal et al. 2016, *PLoS ONE* | Abstract / press |
| Kéfi et al. 2013, *Oikos* 122:641; Hagstrom & Levin (arXiv:2110.12287) | Abstracts |
| Prokopenko et al. 2011, *PRE* 84:041116; Held & Kleinen 2004, *GRL* 31:L23207 | Abstract via index |
| Fath et al. 2003 *JTB* 222:517; Karunanithi 2008; Mayer 2006; Dakos 2012 *PLoS ONE*; Dakos & Soler-Toscano 2017; Ditlevsen & Johnsen 2010; Lenton 2011; Scheffer 2012; Kritzman 2011; Brock & Carpenter 2006 | **Bibliographic or secondary only; not read** |

Local PDF copies were kept in the research session scratchpad only (not in the repo).
