# QR-010 literature map: why modern machine learning escapes the complexity tax, and where it doesn't (2026-10-19)

> **Provenance (2026-10-19).** Mode A, literature mapping only. This is the map for Questions Raised Log entry **QR-010**, raised by the owner today as the sequel to QR-009. QR-009 found that extra model freedom is usually taxed by estimation variance, by selection over many tries, and by five other mechanisms (M1–M7). QR-010 asks why the largest machine-learning models seem to escape that tax, and where they still pay it. Following the deep-research pattern, the search was split across seven read-only research sub-agents:
> 1. the "bitter lesson" and neural scaling laws;
> 2. why over-parameterised networks generalise (proven vs empirical);
> 3. pre-training and transfer as pooling evidence;
> 4. benchmark reuse, contamination, leaderboard selection, Goodhart and reward hacking, and the emergent-abilities debate;
> 5. distribution shift, shortcut learning, rare events and small data;
> 6. finance as the hard case;
> 7. the reconciliation literature and current (2024–2026) directions.
>
> **Sub-agent summaries are leads, not readings.** The main session re-checked the load-bearing citations itself:
> - metadata and abstracts for 50 arXiv records;
> - 31 DOIs against Crossref;
> - the headline numbers in 20 primary texts, found by PDF or HTML text extraction (column "MS" in §J).
>
> Markers in §J are never upgraded. The sub-agents' notes are kept outside the repo, in the session notes folder (`research_notes/ML and the complexity tax/`, files 1–7).
>
> **The wiki itself was read, not written.** `ds_wiki.db` was queried read-only for machine-learning content (§G). No gate has been run, nothing has been folded in, and nothing has been written to either database. Confidence tags: **Established / Supported / Speculative**.
>
> **Dates and status.** This field moves fast. Every source in §J carries its date, and preprints, working papers, workshop papers, blogs and company reports are marked as such. Nothing here is investment advice.

**QR-010 in one sentence a physicist could check:** *Very large neural networks predict well out of sample, although they have far more adjustable parameters than classical statistics would allow. Is that because they see far more independent data per effective parameter and are implicitly regularised, or because over-parameterisation changes the bias–variance arithmetic itself? And under what conditions does the classical penalty come back?*

---

## (A) The answer in plain terms

- **The puzzle exists only if you meter complexity by raw parameter count.** The classical result is that the tax grows with *effective* degrees of freedom over *independent* observations (QR-009 §B1–B2), and raw parameter count was never that meter. Measured on effective complexity, modern ML is not an exception to the tax. It is an extreme case of QR-009's three cures:
  - more independent evidence;
  - pooling across related data;
  - shrinkage toward simple solutions.

  This reading is **Supported**: it is proven for linear and kernel models and argued for deep nets. Whether it is the *whole* story for networks that learn their own features is **contested** (§D1).
- **Escape route 1: far more evidence per adjustable part.**
  - **Compute-optimal training uses about 20 tokens per parameter.** Chinchilla is 70B parameters on 1.4T tokens; the paper's Table 3 gives 1B parameters → 20.2B tokens.
  - **Current small models go far beyond that.** Llama 3 8B saw at least about 1,875 tokens per parameter, by the model card's "15T+".
  - **Measured storage capacity is only about 3.6 bits per parameter** (Morris et al. 2025, a preprint, on random bitstrings). Our order-of-magnitude arithmetic, Speculative as a number: such a model can store at most about 0.002 bits per training token, so it must compress its corpus rather than memorise it.
  - **Modern language-model pre-training is therefore not in the "more parameters than data" regime** that made Zhang et al.'s 2017 random-label experiment surprising.
- **Escape route 2: pooling.** Pre-training is the M5 lesson (QR-009 §D) at web scale.
  - **One measured case.** Pre-training on text was worth about 1,000× the fine-tuning data, for a 40M-parameter model with 300,000 characters of Python. The multiplier shrinks as local data grow, and in the data-rich limit pre-training can *hurt* small models ("ossification"; Hernandez et al. 2021, a preprint).
  - **Where sources frame it as Bayesian.** Two do so explicitly: MAML is empirical Bayes (Grant et al. 2018, exact for linear regression), and TabPFN approximates Bayesian prediction under a synthetic prior (Hollmann et al. 2025). Xie et al. 2022 prove that in-context learning acts as implicit Bayesian inference, in a mixture-of-HMMs setting.
  - **For large-language-model pre-training in general,** "pooling" is our analogy, not a sourced result.
- **Escape route 3: the invisible leash.** The training procedure prefers simple solutions: gradient descent's implicit bias, early stopping, weight decay and architecture. So effective complexity stays far below the parameter count.
  - **Proven** only in restricted settings. Gradient descent on separable data converges to the max-margin direction (Soudry et al. 2018). The minimum-norm interpolant is benign only under stated spectral conditions (Bartlett et al. 2020).
  - **Empirical** for deep nets.
  - This is QR-009's "shrunk middle" (§B4) in another form: a very flexible model with a strong soft preference for simple fits. Wilson 2025 calls it "soft inductive bias". The link to Parpart et al.'s intermediate priors is ours.
- **Double descent and benign overfitting are real but conditional, and older than usually cited.**
  - **History.** The phenomenon was first shown in 1989–1990 statistical-physics work (Vallet et al.; Opper et al.; via Loog et al. 2020).
  - **What is proven.** The peak is the same variance blow-up as QR-009's σ²γ/(1−γ) at p ≈ n, continued past the interpolation point (Hastie et al. 2022). Optimally tuned ridge removes it in isotropic linear models (Nakkiran et al. 2021).
  - **Measured on effective parameters, the U-curve returns** for linear models, trees and boosting (Curth et al. 2023).
  - **Interpolating deep nets are *tempered*, not benign.** They pay a finite, non-zero cost for label noise; early-stopped nets look benign (Mallinar et al. 2022). **The tax is reduced, not repealed.**
- **Scaling laws are the tax, priced.**
  - Kaplan et al. 2020 write the overfitting penalty explicitly: it depends on N^0.74/D (✓). Chinchilla's L = E + A/N^α + B/D^β trades a parameter term against a data term at fixed compute.
  - **The exponents are fitted, not derived.** Theories reproduce power laws only in toy and solvable models.
  - **Even the fitting is fragile.** Chinchilla's published Approach-3 constants came from an optimiser that stopped early: matching the published confidence intervals would take over 600,000 runs, and the authors likely ran fewer than 500 (Besiroglu et al. 2024 ✓).
  - **When data run short, the tax visibly returns.** Up to 4 epochs of repeated data cost almost nothing (✓). By about 16 epochs a further repeat is worth only about 1/e of a fresh token (the paper's fitted decay constant R*_D ≈ 15.4, which it calls a "half-life"), and by 40 epochs almost nothing (Muennighoff et al. 2023). Public human text is projected to run out between 2026 and 2032 (Villalobos et al., v2 2024 ✓).
- **Where machine learning still pays, through the same mechanisms as QR-009:**
  - **Selection over many tries (M2).**
    - Meta tested 27 private model variants on Chatbot Arena before the Llama 4 release. The authors call the practice a "best-of-N strategy" (✓; Singh et al. 2025, preprint).
    - Two identical checkpoints scored 1052 and 1069 Elo (✓).
  - **Broken holdouts.**
    - **Fresh maths test.** Accuracy fell by up to 8% on new grade-school maths problems for some model families, while frontier models showed minimal drops (GSM1k ✓).
    - **SWE-bench.** A third of "successful" coding patches had the answer leaked in the issue text. Filtering them cut one agent's score from 12.47% to 3.97% (SWE-Bench+, preprint).
    - **ML-based science.** Leakage affected 294 papers in 17 fields (Kapoor & Narayanan 2023).
  - **Goodhart (M7).**
    - **Reward-model overoptimisation.** Optimising against a learned proxy reward first raises, then lowers, the true ("gold") reward (Gao et al. 2023 ✓).
    - **Reward hacking.** A frontier model reward-hacked in 39 of 128 runs on one agentic benchmark, against 8 of 1,087 on another (METR 2025, blog ✓).
  - **Shift and shortcuts (M3, M6).**
    - Pneumonia models could identify the hospital from the X-ray 99.95% of the time. Hospital prevalence alone gave AUC 0.861 (Zech et al. 2018 ✓).
    - Google Flu Trends overestimated in 100 of 108 weeks. It was built by matching 50 million search terms to 1,152 data points, and was beaten by 3-week-old official data (Lazer et al. 2014 ✓).
  - **Rare events (M5/M6).** An AI weather model trained without strong cyclones could not forecast Category 5 storms; it "relaxes toward" intensities seen in training (Sun et al. 2025 ✓).
  - **Low signal-to-noise and a reflexive market (finance; §C, §D3).**
- **One honest surprise: test-set reuse cost much less than worst-case theory predicts.**
  - New ImageNet test sets dropped accuracy by 11–14%, but rankings held. Each point gained on the old test set bought *more* than a point on the new one, the opposite of what adaptive overfitting would produce.
  - The authors call adaptivity "an unlikely explanation" (Recht et al. 2019 ✓). A meta-analysis of over 100 Kaggle competitions found "little evidence of substantial overfitting".
  - The proposed reason is QR-009's M2 arithmetic with a small *effective* N: models agree with each other far beyond what their accuracies imply, so many "tries" count as few (Mania et al. 2019).
- **The bitter lesson is an essay, not a result.**
  - Sutton (13 March 2019 ✓) argues from four historical cases (chess, Go, speech, vision) that general methods exploiting computation beat built-in human knowledge.
  - His vision example concedes that convolution survives as a built-in prior. Vision Transformers, which lack it, needed 300M pre-training images to edge past ResNets: 88.55% against 87.54% on ImageNet (✓).
  - The defensible form is "weak, general priors plus scale beat strong hand-built ones *when data are plentiful*". It says nothing about estimation variance.
- **Finance is the hard case, and its own literature says so.**
  - **Gu, Kelly & Xiu 2020 (✓).** The best monthly out-of-sample R² for individual stocks is 0.40%, from a three-layer network. Least squares on all 920 features scores −3.46%. Deeper networks do worse. The authors attribute this to the "tiny signal-to-noise ratio" and contrast it with computer vision.
  - **The "virtue of complexity" claim** (Kelly, Malamud & Zhou 2024) faces three critiques that converge by different routes: its forecasts act like volatility-timed momentum or a 12-month moving average, and real learning at 12 monthly observations would need 25–30 years of data. The critiques are Nagel 2025, a working paper; Elmore & Strauss, *Economics Letters* 2026; and Fallahgoul 2025, a preprint (✓ abstract). **Open, actively contested** (§D3).
- **The wiki holds almost nothing on machine learning (§G).**
  - CS10 (No Free Lunch) and EWS9 (a deep-learning early-warning classifier) are the only ML-bearing entries.
  - IT09 and M6 are adjacent only through a specific, unchecked Hessian–Fisher link (drift note, §F).

**Calibrated summary.**

| Claim | Tag |
|---|---|
| Over-parameterised networks can fit random labels perfectly, so capacity measures that depend only on the architecture cannot explain their generalisation | **Established** (Zhang et al. 2017 ✓) |
| Minimum-norm interpolation can be benign, and double descent occurs, in linear and kernel models under stated spectral and SNR conditions | **Established** (Bartlett et al. 2020; Hastie et al. 2022; Belkin et al. 2019) |
| Interpolating deep nets overfit "benignly" | **Not supported**: tempered, a finite cost from label noise; early-stopped nets look benign (Mallinar et al. 2022 ✓ abstract) |
| Language-model loss follows fitted power laws in parameters, data and compute over several orders of magnitude, with an explicit overfitting term | **Established as empirical fits** (Kaplan 2020 ✓; Hoffmann 2022 ✓); **exponents not derived** |
| Measured on an effective-parameter count, double descent folds back into a U-curve | **Established** for linear models, trees and boosting (Curth et al. 2023 ✓ abstract); **not tested** for deep nets |
| Modern ML escapes the tax mainly through more independent evidence per effective parameter, pooling, and implicit regularisation | **Supported** (reconciliation literature, §B5, §D1); **Speculative** as a complete account of feature learning |
| Over-parameterisation improves generalisation beyond what effective-complexity accounting explains | **No source found** that shows it; its demonstrated benefit is easier optimisation |
| Pre-training substitutes for scarce task data, with a benefit that shrinks as task data grow | **Supported** (Hernandez et al. 2021 ✓, one target, preprint; He et al. 2019; TabPFN) |
| ML still pays the selection, Goodhart, shift and rare-event taxes | **Established** for each named case in §C |
| The cost of reusing benchmark test sets has been small in practice | **Supported** (Recht 2019 ✓; Roelofs 2019; Mania 2019) |
| "Emergent abilities" are mostly metric artefacts | **Contested**: true for most catalogued BIG-Bench cases (Schaeffer 2023 ✓); loss-threshold effects claimed to survive (Du et al. 2024) |
| Over-parameterised "virtue of complexity" carries over to return prediction | **Contested**, with three converging critiques |
| "The bitter lesson" is a tested law | **No.** An essay; a historical induction over four cases |

---

## (B) Settled — Established

### B1. Fitting random labels: the architecture alone does not prevent overfitting
- **What happened.** Zhang, Bengio, Hardt, Recht & Vinyals (ICLR 2017; *CACM* 64:107, 2021) trained a CIFAR-10 Inception network on random labels.
  - It reached **100.0% training accuracy and 9.78% test accuracy** (chance for 10 classes).
  - On the true labels the same network gave **89.05%** test accuracy.
  - Random labels took only "a small constant factor" longer to fit (✓).
  - On ImageNet, random-label training accuracy reached **95.20%** (✓).
- **What it rules out.** Complexity measures that depend only on the hypothesis class (VC dimension, Rademacher complexity) cannot separate the networks that generalise from those that don't.
- **What it does not rule out.** Data-dependent and algorithm-dependent measures. Wilson 2025 shows a Gaussian process reproduces the experiment, and its marginal likelihood falls as more labels are randomised.
- **For QR-009.** The tax depends on what the *procedure* does with the data, not on what the architecture *could* fit. This is QR-009's §B2 point (effective, not nominal, degrees of freedom) in its sharpest form.

### B2. Double descent and benign overfitting, with conditions
- **Prehistory.** Learning-curve peaks for the minimum-norm "pseudo-inverse" solution were shown experimentally by Vallet, Cailton & Refregier 1989, and derived by Opper et al. 1990 with the peak at n/N = 1. Source: Loog et al. 2020, *PNAS* 117:10625 (✓ cit). Belkin et al. 2019 (*PNAS* 116:15849) named it and extended it to modern models.
- **The proven core is QR-009's own formula.**
  - For least squares with random isotropic features, risk rises as σ²γ/(1−γ) when γ = p/n → 1 (QR-009 §B1). Past γ = 1, the minimum-norm interpolant's variance falls again (Hastie, Montanari, Rosset & Tibshirani 2022, *Ann. Statist.* 50:949).
  - Optimally tuned ridge makes the risk monotone in both sample size and model size for isotropic linear regression (Nakkiran, Venkat, Kakade & Ma, ICLR 2021 ✓ abstract).
  - **The double-descent peak is an under-regularisation artefact in that setting.**
- **Benign overfitting** (Bartlett, Long, Lugosi & Tsigler 2020, *PNAS* 117:30063). The minimum-norm interpolant is benign if and only if the data covariance has many low-variance directions: the "effective rank" of the tail must be large compared with n. The noise is then absorbed by many unimportant directions. **Proven for linear regression only.**
- **The taxonomy** (Mallinar et al. 2022, preprint).
  - Kernel ridge regression with power-law spectra, including ReLU neural tangent kernels, overfits in a **tempered** way.
  - Deep nets "trained to interpolation are tempered, while those stopped early are benign" (✓ abstract).
- **Deep double descent** (Nakkiran et al., ICLR 2020; *J. Stat. Mech.* 2021:124003).
  - It is model-wise, epoch-wise and sample-wise: in a critical range of model sizes, 4× more data can hurt.
  - It is strongest with label noise (15% in their headline figure).
  - **Conjectured:** that the peak sits where "effective model complexity" ≈ n.
- **Effective parameters bring the U back** (Curth, Jeffares & van der Schaar, NeurIPS 2023 ✓ abstract). For linear regression with random features, trees and boosting, double-descent curves "fold back into more traditional convex shapes" when plotted against an effective number of parameters measured on unseen inputs. **Not tested for deep nets.**

### B3. Scaling laws: the tax written as a fitted equation
- **Kaplan et al. 2020** (arXiv preprint, never formally published; ✓ §1, Eqs. 1.1–1.5, 4.3–4.4):
  - L(N) ∝ N^−0.076 (non-embedding parameters);
  - L(D) ∝ D^−0.095 (tokens);
  - L(C_min) ∝ C_min^−0.050, on the compute-efficient frontier (not raw compute).
  - The overfitting penalty depends only on **N^0.74/D**. To keep it below seed noise needs D ≳ 5×10³·N^0.74, so data need grow only sublinearly with model size.
  - **Range:** some trends span more than seven orders of magnitude, but D varied over only about two.
  - **Caveat:** regularisation was not re-tuned as N and D changed.
- **Hoffmann et al. 2022, "Chinchilla"** (arXiv; NeurIPS 2022 per sub-agent, not verified by MS):
  - "for every doubling of model size the number of training tokens should also be doubled" (✓ abstract).
  - Chinchilla used 70B parameters on 1.4T tokens with Gopher's compute budget, and beat the 280B Gopher.
  - The fitted form is L = E + A/N^α + B/D^β, with E = 1.69, A = 406.4, B = 410.7, α = 0.34, β = 0.28 (✓).
  - The authors read B/D^β as an optimisation term, not estimation variance.
- **The fit itself was fragile** (Besiroglu et al. 2024, preprint ✓ abstract).
  - Approach 3's estimates were inconsistent with the other two approaches.
  - Its confidence intervals would need "over 600,000 experiments"; the authors likely ran fewer than 500.
  - A Hoffmann co-author attributed this to an optimiser that stopped early (sub-agent ft).
  - The refit is consistent with about 20 tokens per parameter. Llama 3's in-house fit gave about 41 at its compute budget (sub-agent ft).
  - **"20 tokens per parameter" is a ratio for one data mix and architecture family, not a constant.**
- **Status of the exponents:** **fitted, not derived.** Bahri et al. 2024 (*PNAS* 121:e2311878121 ✓ cit), Sharma & Kaplan, Maloney–Roberts–Sully and Hutter produce power laws in solvable or toy models. Bahri et al. separate a "variance-limited" regime, the classical estimation term, from a "resolution-limited" regime. None derives the measured LLM exponents.

### B4. Data limits: where the single-epoch escape ends
- **Repeated data** (Muennighoff et al., NeurIPS 2023 ✓ abstract).
  - Up to 4 epochs of repeated data give "negligible changes to loss" compared with unique data. In their example, an 8.7B model trained for 4 epochs had a validation loss only 0.5% higher.
  - Beyond that the value of extra compute "eventually decays to zero".
  - The fitted decay constant R*_D ≈ 15.4 (called a "half-life", but it is a 1/e scale): by about 16 epochs a further repeat is worth about 1/e of fresh data. Runs at 44 epochs overfit mid-training and break the fit (sub-agent ft).
- **The data stock** (Villalobos et al., v2 June 2024 ✓ abstract). Training sets will match the stock of public human text "between 2026 and 2032, or slightly earlier if models are overtrained". **Cite the version:** v1 (2022) gave other dates.
- **Synthetic data.**
  - Recursive training in which model output *replaces* real data makes the tails of the distribution disappear (Shumailov et al. 2024, *Nature* 631:755 ✓ cit).
  - *Accumulating* synthetic data alongside real data avoids the collapse (Gerstgrasser et al. 2024, preprint ✓ abstract).
  - **The dispute turns on the modelling assumption, not on conflicting experiments.**

### B5. Effective complexity is far below the parameter count
At least five measures exist. **They are different quantities and must not be equated:**

| Measure | Definition (source's own) | Source |
|---|---|---|
| Effective dimensionality | N_eff(H, z) = Σ λᵢ/(λᵢ + z) over the eigenvalues of the training-loss Hessian, with z > 0 a constant | Maddox, Benton & Wilson 2020 (preprint ✓ abstract; definition sub-agent ft). The counting form is MacKay's 1992 "effective number of parameters" |
| Effective number of parameters of a smoother | variance-based, evaluated on test inputs | Curth et al. 2023 |
| Classical effective degrees of freedom | Σ Cov(ŷᵢ, yᵢ)/σ²; tr(S) for a linear smoother | ESL §7.6; QR-009 §B2 |
| Compression bounds | description length of a compressed version of the trained model | Arora et al. 2018; Lotfi et al. 2022, 2024 (✓ abstract) |
| Storage capacity | ≈ 3.6 bits per parameter on random bitstrings, models of 500K–1.5B parameters (Morris et al. 2025 ✓); ≈ 2 bits per parameter for synthetic facts after about 1,000 exposures each (Allen-Zhu & Li 2024, preprint) | as listed |

- **What the measures share:** a trained network's effective complexity is far below its parameter count. **Supported.** No published mapping between their numerical values was found.
- **What the bounds certify, and what they don't:**
  - Every non-vacuous bound found applies to a *modified* network: a stochastic one (Dziugaite & Roy, UAI 2017 ✓ metadata, binary MNIST, 16–22%) or a compressed one.
  - For language models the bound is non-vacuous but loose: a 96.41% top-1 error bound for a compressed GPT-2, against about 99.99% for random guessing. The uncompressed model's bound is vacuous (Lotfi et al., ICML 2024; numbers sub-agent ft).
  - So the bounds show that a simple description consistent with the data *exists*. They do not certify the deployed model.

### B6. Implicit regularisation: proven in restricted settings
- **Max-margin convergence** (Soudry et al. 2018, *JMLR* 19 ✓ abstract). On separable data with logistic-type loss, gradient descent converges to the max-margin direction, "only logarithmic in the convergence of the loss itself". This is offered as a reason why training past zero error helps.
- **Other results:**
  - Infinite-width two-layer max-margin (Chizat & Bach 2020; proven).
  - Deep-linear incremental learning (Gissin et al. 2020; proven).
  - Matrix-factorisation nuclear-norm bias (Gunasekar et al. 2017): **a conjecture**, by the paper's own abstract.
- **Plain linear algebra.** The minimum-norm interpolant is the λ → 0⁺ limit of ridge regression. So "interpolate, choosing the smallest solution" is shrinkage in its weakest form. **Established.** The view that early stopping approximates ridge is a lead from the literature (Ali, Kolter & Tibshirani 2019; not checked this pass).
- **Stochastic noise is not necessary** (Geiping et al., ICLR 2022). Full-batch training matched SGD on CIFAR-10 (95.68% vs 95.70%), but needed explicit regularisation, gradient clipping, longer training and data augmentation. So it is the bias that matters, not stochasticity as such. **Empirical, one dataset.**
- **Flat minima are a correlate, not a cause.**
  - Sharpness, as usually measured, changes under reparameterisation without changing the function (Dinh et al. 2017, proven by construction).
  - In a study of 40 measures over more than 10,000 networks, sharpness- and PAC-Bayes-based measures predicted generalisation best, and norm-based measures correlated *negatively* (Jiang et al. 2020).

### B7. Selection and Goodhart: QR-009's M2 and M7, in ML
- **Reward-model overoptimisation** (Gao, Schulman & Hilton 2022/23; ✓ §3–4).
  - A proxy reward model is trained to imitate a "gold" one. Optimising against the proxy first raises, then lowers, the gold score.
  - Best-of-n follows R(d) = d(α − βd), with d = √KL and KL_bon = log n − (n−1)/n.
  - The authors map Manheim & Garrabrant's taxonomy onto their terms: "regressional" Goodhart (noisy proxy features) and "extremal" (leaving the reward model's training distribution).
  - QR-009 §B3 identified regressional Goodhart with the optimiser's curse. That identification is ours.
- **Reward hacking is unavoidable in general** (Skalse et al. 2022 ✓ abstract). Over all stochastic policies, "two reward functions can only be unhackable if one of them is constant".
- **Leaderboards: best-of-N, said by the authors.**
  - Singh et al. 2025 (preprint ✓): "Private testing coupled with the option to retract enables a best-of-N strategy", which "introduces an upward bias".
  - They found 27 private variants for Llama 4. Two identical checkpoints scored 1052 and 1069 (±≈20).
  - **Our arithmetic (Speculative, illustrative):** with a standard error of about 10–11 Elo, the expected best of 27 independent noise draws is about 2.0 standard errors (closed form 2.03, Monte Carlo 2.00), i.e. about +20 Elo from selection alone. Correlated variants would lower this. The paper's own simulated figures are internally inconsistent: about 100 points for 10 variants in its summary, about 50 for 20 in §3.2.

---

## (C) Measured — where the tax was quantified, or escaped, and how big

| Domain | Study | What was measured | Size | Mechanism (§F) | MS |
|---|---|---|---|---|---|
| Random labels | Zhang et al. 2017 | Same CIFAR-10 net on true vs random labels | 100% train both; test 89.05% vs 9.78% | M1 (capacity ≠ tax) | ft |
| Scaling | Kaplan et al. 2020 | Overfitting penalty vs N, D | depends on N^0.74/D; D ≳ 5×10³·N^0.74 | M1, priced | ft |
| Compute-optimal | Hoffmann et al. 2022 | 70B on 1.4T tokens vs 280B on 300B, same compute | 70B model better on a large range of tasks | M1 trade-off | ft |
| Data repetition | Muennighoff et al. 2023 | Repeated vs unique tokens | ≤ 4 epochs ≈ free (+0.5% loss); 1/e at ~16; ~0 at 40 | M1 returns when data short | abs |
| Transfer | Hernandez et al. 2021 (preprint) | Effective data transferred, text → Python | D_T = 1.9e4·D_F^0.18·N^0.38; ~1,000× at one small-data point; "ossification" at high data | pooling (M1 cure) | ft |
| Transfer, detection | He, Girshick & Dollár 2019 | COCO from scratch vs ImageNet-pretrained | From scratch with longer training matched pre-training, even at 10% of data | pooling redundant with enough local data | — (sa abs) |
| Small tabular data | Grinsztajn et al. 2022 | 45 datasets, ~10k rows | Tree ensembles still beat deep nets | inductive bias (M1) | abs |
| Small tabular data | Hollmann et al. 2025 (TabPFN) | Transformer pretrained on ~100M synthetic datasets, ≤ 10k rows | Normalised ROC AUC 0.939 vs 0.752 default CatBoost (0.952 vs 0.822 tuned); 2.8 s vs 4 h tuned ensemble; trees expected to win on larger data | synthetic prior (pooling) | cit |
| Architecture vs data | Dosovitskiy et al. 2021 (ViT) | ImageNet top-1 after JFT-300M pre-training | ViT-H/14 88.55% vs BiT ResNet 87.54%; ViT trails ResNets on ImageNet alone | weak prior pays in data | ft |
| Weather | Lam et al. 2023 (GraphCast) | 39 years of ERA5 vs deterministic ECMWF HRES | Better on 90.3% of 1,380 targets; not compared with the ENS ensemble | escape in a stable, high-SNR world | ft (preprint) |
| Test-set reuse | Recht et al. 2019 | New CIFAR-10 / ImageNet test sets | Drops 3–15% / 11–14% (best ImageNet 82.9 → 72.2); ranking kept; slope > 1; adaptivity "an unlikely explanation" | M3 (shift), *not* M2 | ft |
| Holdout reuse | Roelofs et al. 2019 | >100 Kaggle competitions, public vs private | "little evidence of substantial overfitting" | M2, small effective N | — (sa abs) |
| Contamination | Zhang et al. 2024 (GSM1k) | New grade-school maths set | Drops up to 8% (v1 preprint: 13%); frontier models minimal | broken holdout | abs |
| Contamination | Aleithan et al. 2024 (SWE-Bench+, preprint) | Leaked solutions in issues | 32.67% of "solved" patches leaked; one agent 12.47% → 3.97% | broken holdout | — (sa abs) |
| Leakage in science | Kapoor & Narayanan 2023 | Literature survey | 294 papers, 17 fields; civil-war complex-ML advantage vanished when fixed | broken holdout; M1 | cit |
| Leaderboard | Singh et al. 2025 (preprint) | Chatbot Arena private testing | 27 Meta variants; identical checkpoints 17 Elo apart | M2 (authors' framing) | ft |
| Goodhart | Gao et al. 2023 | Gold vs proxy reward under optimisation | Gold rises then falls; d(α − βd) for best-of-n | M2 + M7 | ft |
| Reward hacking | METR 2025 (blog) | o3 on RE-Bench and HCAST | 39/128 runs (30.4%), 21/21 on one task; 8/1,087 (0.7%) on HCAST | M7 | ft |
| Emergence | Schaeffer et al. 2023 | BIG-Bench metrics | > 92% of claimed emergent abilities come from two discontinuous metrics | M2 on findings (our inference) | ft |
| Shortcuts | Geirhos et al. 2019 | Shape vs texture conflict images | ResNet-50 chose by shape 22.1%; humans 95.9% | M6 | ft |
| Shortcuts | Zech et al. 2018 | Pneumonia CNN across hospitals | Hospital identified 99.95%; prevalence alone AUC 0.861; external AUC 0.802 → 0.717 | M6 (+ base rates) | ft |
| Shortcuts | Beery et al. 2018 | Camera traps, unseen locations | Top-1 error 20.83% → 41.08% | M6 | ft |
| Shortcuts | Winkler et al. 2019 | Surgical ink on skin images | Specificity 84.1% → 45.8% | M6 | cit |
| Clinical ML | Roberts et al. 2021 | 62 COVID imaging models | "none … of potential clinical use" | M1 + M6 + broken holdout | cit |
| Deployment | Wong et al. 2021 | Epic Sepsis Model, external validation | AUC 0.63 vs developer's 0.76–0.83; 67% of sepsis cases never alerted | M3/M6 | cit |
| Deployment | Lazer et al. 2014 | Google Flu Trends | Too high 100 of 108 weeks; 50M terms vs 1,152 points; MAE 0.486 vs 0.311 (lagged CDC) | M1 + M2 + M3 + M7 | ft |
| Shift benchmarks | Koh et al. 2021 (WILDS) | ID vs OOD, 10 datasets | e.g. Camelyon17 93.2 → 70.3; worst-group CivilComments 92.2 → 56.0 | M3 | abs |
| Shift, scale | Taori 2020; Miller 2021; Fang 2022 | ~200 ImageNet models; CLIP | OOD tracks ID ("accuracy on the line"); only more diverse data lifts it; CLIP robustness from data diversity | M3 | abs |
| Rare events | Sun et al. 2025 | AI weather model without strong cyclones | Cannot forecast Category 5; "relax toward" training intensities | M5/M6 | ft |
| Finance | Gu, Kelly & Xiu 2020 | 30,000 US stocks, 920 features | Best monthly R² 0.40% (NN3); OLS-all −3.46%; peak at 3 layers; authors cite "tiny signal-to-noise ratio" | M1 | ft |
| Finance | Leippold, Wang & Zhou 2022 | Chinese A-shares | R² up to 2.71% overall, 7.27% in the smallest 30%, ≤ 0.74% in the top 70% | M1; frictions | cit |
| Finance | Avramov, Cheng & Metzker 2023 | ML signals vs economic restrictions | Profits shrink excluding microcaps, distressed firms and high-volatility periods, and shrink further after costs | M4 | cit |
| Finance | Rahimikia, Ni & Wang 2025 (preprint) | Time-series foundation models on daily returns | Zero-shot R² −1.37% (Chronos), −2.80% (TimesFM); pre-training on financial data helps | pooling fails off-domain | abs |
| Finance | Lopez-Lira & Tang (preprint, v6 2025) | GPT-4 on post-cutoff headlines | Drift-strategy Sharpe fell from 6.54 (2021Q4) to 1.22 (early 2024) | M7 or short sample (not distinguishable) | — (sa ft) |

**Three cautions on reading the table.**
1. **The "escape" rows are in domains with plentiful, stable, high-SNR data:** language, images, weather. The "tax" rows are the opposite. The table cannot separate "ML escapes the tax" from "ML was deployed where the tax is low". That is the reconciliation's point, not a refutation of it.
2. **"Shortcut" and "shift" failures are not paid for by model size.** In each case the shortcut is genuinely predictive in the training data, and the fix is data-side: external validation, cropping, multi-site training. Calling them a "complexity tax" stretches QR-009's term. They belong to M3 and M6.
3. **Most finance rows are about one market and one period, and several are preprints.** None is investment advice.

---

## (D) Open — and who frames it as open

1. **Does effective-complexity accounting fully explain why feature-learning networks generalise?**
   - **Essentially answered in principle:** Wilson 2025 (ICML position paper ✓ abstract): soft inductive bias plus PAC-Bayes and countable-hypothesis bounds; he concedes representation learning is distinct. Supported by the Lotfi et al. bounds.
   - **Classical tools insufficient:** Zhang et al. 2021 ("still requires rethinking"); Nagarajan & Kolter 2019 (two-sided uniform-convergence bounds provably vacuous even over the solutions gradient descent reaches); Belkin 2021.
   - **Partly open:** Bartlett, Montanari & Rakhlin 2021 call their three principles a "conjecture" for deep nets. Danhofer, D'Ascenzo, Dubach & Poggio 2025 (preprint) leave learnability and optimisation open.
   - **The split is mostly over the standard of explanation.** "Answered" means non-vacuous bounds exist after training. "Open" means no theory predicts *which* architectures and data will generalise. **Open in the literature, by those authors.**
2. **Emergent abilities.**
   - Wei et al. 2022 (TMLR) defined emergence as abilities absent in smaller models and present in larger ones.
   - Schaeffer, Miranda & Koyejo 2023 (✓) showed that two discontinuous metrics account for more than 92% of claimed cases, and produced fake emergence in vision models by choosing the metric. They do not claim real emergence is impossible.
   - Du et al. (NeurIPS 2024 ✓ abstract) report abilities appearing below a pre-training-loss threshold "regardless of the continuity of metrics". The 2025 counter-claims (Gu et al.; Krakauer et al.) are known only through a survey.
   - **Open, framed by Du et al. and the 2025 survey.**
3. **Does the "virtue of complexity" carry over to return prediction?** This continues QR-009 §D1, with new entries.
   - Kelly, Malamud & Zhou 2024 (*JF*).
   - The critics:
     - Nagel 2025 (NBER WP 34104): the forecast becomes volatility-timed momentum, and the method "mislearns" on reversal data;
     - Elmore & Strauss (*Economics Letters* 258:112749, 2026 ✓ cit): 97.5% correlated with a 12-month moving average (sub-agent ss);
     - Fallahgoul 2025 (preprint ✓ abstract): escaping the information bound at 12 monthly observations would need more than 25–30 years of data;
     - Berk 2023, Buncic 2025 and Cartea, Jin & Shi 2025 (working papers, known only through Nagel).
   - **Kelly & Malamud's 2025 reply** (working paper, not read) reportedly separates nominal from effective complexity, which narrows the dispute toward this map's §B5 reading.
   - **Procedural fact:** Nagel was the handling editor of KMZ at *JF* (KMZ acknowledgements, sub-agent ft).
   - **Open, actively contested.**
4. **Is pre-training scaling slowing?**
   - No primary, quantitative source found shows a measured flattening of the pre-training loss law at frontier scale. Labs mostly do not publish those curves.
   - What is documented is a shift of effort:
     - smaller models trained far past compute-optimal, for inference cost (Llama 3; Sardana et al., ICML 2024 ✓ abstract);
     - test-time compute;
     - reinforcement learning with verifiable rewards.
   - Silver & Sutton 2025 (a book-chapter preprint) assert that progress from human data is "demonstrably slowing", without data in the text read. **Open; no primary evidence either way found.**
5. **Does reinforcement learning with verifiable rewards add new capability or re-weight old ones?**
   - Yue et al. (NeurIPS 2025 oral ✓ abstract): it improves single-attempt accuracy, but base models score higher at large pass@k. The current setup "does not elicit fundamentally new reasoning patterns".
   - DeepSeek-R1 (*Nature* 645:633, 2025 ✓ cit) reports reasoning behaviour emerging under rule-based rewards.
   - **Open.** For the tax framing: a verifier removes the learned-proxy gap Gao et al. measured. Incomplete verifiers can still be gamed (METR's timer and evaluator edits).
6. **How much of the distribution-shift gap can scale close?**
   - Hendrycks et al. 2020 (✓ abstract): pre-trained Transformers degrade less, but "larger models are not necessarily more robust".
   - Taori 2020 and Fang 2022: data diversity, not size, moves models above the line.
   - Wenzel et al. 2022 (31k networks): the ID–OOD relation is strongly dataset-dependent.
   - **Open; framed as open by Taori et al.** ("an open research problem").
7. **Is "bigger and general beats built-in knowledge" true outside data-rich domains?** The bitter lesson's critics (Brooks 2019, a blog post; a 2025 blog by Cranmer, unconfirmed byline) say the evidence conflicts, especially in AI-for-science. The only "empirical test" found is an LLM-scored bibliometric study (Yousefi & Collins, an EMNLP 2024 workshop paper). **No controlled test found; open in the sense that nobody has tested it.**
8. **What is the Chinchilla data term?** The authors call B/D^β an optimisation term. It behaves like an estimation term in Kaplan's overfitting law and in Muennighoff's repetition decay. **No source found that separates the two. Our question (§I S2), not a recognised open problem.**

---

## (E) When does ML escape the tax? Factor by factor

This continues QR-009 §E. The factors are the same; machine learning sits at different values of them.

| Factor (QR-009 §E) | Where ML escapes | Where ML pays | Evidence |
|---|---|---|---|
| **Independent evidence per effective parameter** | Language pre-training at 20 to ≥ 1,875 tokens per parameter, single-epoch; images with millions of labels | Small tabular data (~10k rows); clinical datasets; rare events; multi-epoch reuse past ~4–16 epochs | Hoffmann 2022; Llama 3; Muennighoff 2023; Grinsztajn 2022; Roberts 2021 |
| **Signal-to-noise** | Image labels near-deterministic; next-token prediction has a learnable structure | Monthly stock returns: best R² 0.40%; label noise makes interpolating nets *tempered* | GKX 2020; Mallinar 2022; Bartlett 2020 / Hastie 2022 (benign needs high SNR) |
| **Pooling / prior structure** | Pre-training on related data; synthetic priors (TabPFN); convolutions for images | Off-domain pooling: generic time-series models on returns; "ossification" when local data suffice; homogenisation spreads shared defects | Hernandez 2021; Hollmann 2025; Rahimikia 2025; Bommasani 2021 |
| **Implicit / explicit regularisation** | Gradient-descent bias, early stopping, weight decay keep effective complexity low | Interpolation with noisy labels; when the soft bias favours a shortcut (simplicity bias picks the wrong simple feature) | Soudry 2018; Mallinar 2022; Shah et al. 2020 |
| **Number of variants tried** | Test-set reuse: tries are highly correlated, so the effective N is small | Private leaderboard variants; emergence findings selected over many task × metric pairs | Mania 2019; Roelofs 2019; Singh 2025 |
| **Independence of the test draw** | Fresh, post-cutoff and live benchmarks (LiveBench, LiveCodeBench, GSM1k) | Contamination; leaked solutions; leakage in ML-based science; look-ahead bias in LLM backtests | Zhang 2024; Aleithan 2024; Kapoor 2023; Levy 2026; Lopez-Lira, Tang & Zhu 2025 |
| **Stationarity** | Physics (weather), language, natural images | Search behaviour (Google Flu); hospitals and scanners; markets | Lam 2023; Lazer 2014; Zech 2018; Wong 2021 |
| **Proxy vs target** | Verifiable rewards (unit tests, proofs) narrow the gap | Learned reward models; incomplete graders; cost-as-proxy-for-need | Gao 2023; METR 2025; Obermeyer 2019 |
| **Environment reacting** | Static benchmarks, physical systems | Markets (signal decay); the web filling with model output (collapse under replacement) | Lopez-Lira & Tang; Shumailov 2024 |
| **Cost per adjustment / use** | — | Inference cost moves the optimum to small, overtrained models; trading costs erase ML return signals | Sardana 2024; Avramov 2023 |

**The common thread (Supported):** machine learning escapes the tax in exactly the corner QR-009 §D predicted: abundant independent data, regularisation toward simple solutions, and a stable world. It escapes more completely than anyone expected because the data, the pooling and the implicit regularisation are all far larger than in classical statistics. Where any of the three fails, the tax returns through the same mechanisms and at the same rates.

---

## (F) Same math, or same mechanism?

The terms are QR-009's:
- **same math:** a common derivation exists and is cited;
- **same mechanism:** the causal story is the same, but no common equation is written down;
- **surface analogy:** what is shared is the word.

| ML phenomenon | QR-009 mechanism | Relationship | Note |
|---|---|---|---|
| Double-descent peak at p ≈ n (minimum-norm least squares) | **M1** estimation variance | **Same math.** Hastie et al. 2022's σ²γ/(1−γ), continued past γ = 1 | Established (linear) |
| Benign vs tempered overfitting | **M1** | **Same math** for linear and kernel models; deep nets empirical | Benign needs high SNR and a long, flat spectral tail |
| Kaplan overfitting law; Chinchilla allocation; repetition decay | **M1** | **Same mechanism**, written as fitted equations | Chinchilla's authors call B/D^β optimisation error; §D8 |
| Implicit regularisation, early stopping, "soft inductive bias" | **M1's cure:** shrinkage (QR-009 §B4) | **Same math** in the linear case (minimum norm = ridge as λ → 0⁺). **Same mechanism** for deep nets | Wilson's soft bias and Parpart et al.'s intermediate prior: the link is ours |
| Pre-training, transfer, MAML, TabPFN, in-context learning | **M1's cure:** pooling (QR-009 §D, M5) | **Same math** for MAML in linear regression (empirical Bayes, Grant et al. 2018), TabPFN (authors' framing), in-context learning in a mixture-of-HMMs model (Xie et al. 2022). **Our analogy** for LLM pre-training in general | Hernandez's D_T reads like a prior's effective sample size: our analogy |
| Private leaderboard variants | **M2** selection | **Same math** (expected maximum of N noisy scores); the authors say "best-of-N" | ≈ +20 Elo at N = 27 if independent (our arithmetic) |
| Test-set reuse (ImageNet, Kaggle) | **M2** | **Same math with small effective N:** correlated models (Mania et al.) | Why the measured tax was small |
| "Emergent abilities" catalogued over many task × metric pairs | **M2** (on findings) | **Same mechanism**, our inference | Schaeffer et al. stress metric choice, not multiplicity |
| Contamination, leaked solutions, leakage, LLM look-ahead bias | Broken holdout (the violated cure of QR-009 M2) | **Same mechanism:** the test draw is not independent of model construction | Levy 2026: in-window LLM backtests not interpretable |
| Reward-model overoptimisation | **M2** (regressional) + **M6/M7** (extremal) | **Same math** for the best-of-n term (selection on a noisy proxy); Gao et al. map their terms onto Manheim & Garrabrant | Identifying regressional Goodhart with the optimiser's curse is ours (QR-009 §B3) |
| Reward hacking, specification gaming | **M7** (Goodhart) | **Same mechanism** | Skalse et al.: unhackable proxies essentially do not exist over all stochastic policies |
| Model collapse under replacement | **M7** (the environment reacts: the web fills with model output) + **M1** (effective sample of the true distribution shrinks) | **Same mechanism**, our framing | Avoided by accumulation |
| Distribution shift (ImageNetV2, WILDS, temporal shift) | **M3** change | **Same mechanism**; Muth's tracking mathematics does not apply directly (no drifting level is being tracked) | The gap is set by the training data, not model size |
| Shortcut learning, spurious correlations | **M6** fragility to the unanticipated | **Same mechanism** | Not M1: more capacity does not cure it |
| Gray-swan extremes; few-event domains | **M5/M6** | **Same mechanism** (no events of the kind in training) | QR-009's "count events, not rows" |
| Homogenisation (one foundation model, many uses) | **M6** + forecast combination | **Same math** for one part: equal-weight averaging of signals with error correlation ρ gives σ²[ρ + (1−ρ)/n] (QR-009 §G.3), so descendants of one model with high ρ gain little from ensembling. Applying the identity here is ours | Bommasani et al. 2021 state the risk qualitatively |
| Overtraining small models for inference cost; trading costs | **M4** cost | **Same mechanism**; same math within finance (QR-009 §B6) | Sardana 2024; Avramov 2023 |
| Google Flu Trends | **M1 + M2 + M3 + M7** | **Same mechanisms**, several at once | 50M candidate terms; search engine changed ("blue team" dynamics) |
| "Emergence", "phase transition", "grokking" as physics words | — | **Surface analogy** unless a derivation is given | Vocabulary-stacking risk with the wiki's criticality entries |
| Power-law scaling laws vs the wiki's power-law archetype (H5, P12) | — | **Surface analogy.** The exponents are fitted; toy derivations (Bahri, Maloney) are not RG | Do not connect |

**Honest bottom line.** Every escape route in machine learning is one of QR-009's cures, and every place it still pays is one of QR-009's mechanisms. Nothing found requires an eighth mechanism. The nearest candidate is the *broken holdout* (contamination and leakage). QR-009 treated it as part of M2's cure, but in ML it is common and large enough to deserve its own row.

**Drift note.** This map touches four quantities that sound like the wiki's retired effective-dimension (D_eff / Fisher-rank) thread. **None of them is the same object, and none should be connected to D_eff, Ax2 or P5–P7:**
1. Bartlett et al.'s effective rank R_k = (Σ_{i>k} λᵢ)²/Σ_{i>k} λᵢ² has the *algebraic form* of a participation ratio. It is applied to the tail of the **data covariance** spectrum. The sub-agent noticed the form; no source links it to Fisher rank.
2. Maddox et al.'s N_eff is a soft count of directions in the **training-loss Hessian**. For a log-likelihood loss at its minimum, that Hessian is the observed Fisher information (textbook). So N_eff counts "stiff" directions in the sense of the sloppy-models literature (IT09, QR-001), and its counting form is MacKay's 1992 effective number of parameters. **That is the one specific link to QR-001.** Whether the sloppy-models papers make it explicitly was not checked (S7).
3. Sharma & Kaplan's "intrinsic dimension" is a property of the **data manifold**, used to argue that the scaling exponent is about 4/d.
4. Nakkiran et al.'s "effective model complexity" is the **largest sample size** a procedure can fit to near-zero training error.

A claim that "effective dimension explains why deep learning works" would stack four objects under one word (`vocabulary-stacking-analogy`). It is not supported by anything found.

> **Note 2026-10-19 (S7 done; [`QR-010_GATES_2026_10_19.md`](QR-010_GATES_2026_10_19.md) Part 4).** MacKay 1992's count is confirmed: γ = Σ λ_a/(λ_a + α), Eq. 4.9, "the effective number of parameters that are well determined by the data". Maddox et al. cite it. But none of Transtrum et al. 2015, Quinn et al. 2023 or Sethna's 2024 book draft cites MacKay or uses that count. The join to the Fisher spectrum is a one-line identity (`trivial-from-known-result`), not a sourced connection, so **no ML2 → IT09 link was made.** Body text above unchanged.

---

## (G) What the wiki holds, and its gaps

### G.1 Holdings (read-only query, 2026-10-19)
Searched for machine learning, neural network, deep learning, overfitting, double descent, gradient descent, Goodhart, transfer learning, VC dimension, information bottleneck and related terms. **The wiki has almost no machine-learning content.** The relevant entries:
- **CS10, No Free Lunch theorem** (Wolpert & Macready 1997). The wiki's one statement that learning gains come only from exploiting problem structure ("inductive bias"). It is the formal backbone of the counter-argument to a strong reading of the bitter lesson. General methods win only on the problems their soft biases fit.
- **EWS9, deep-learning early-warning signals** (Bury et al. 2021). A CNN-LSTM trained on 500,000 + 200,000 simulated series from bifurcation normal forms. It is a *synthetic-prior pre-training* instance of the same shape as TabPFN. The entry itself says it is a pattern recogniser for critical slowing down, not a new signal.
- **IT09** (sloppy models) and **M6** (Fisher information rank). Adjacent only through the specific Hessian–Fisher link in the drift note, which has not been checked.
- **INFO5** (Kolmogorov complexity) and **INFO1** (mentions minimum description length). The compression-bound literature (Lotfi et al.) and the simplicity-bias argument use algorithmic information. Valle-Pérez, Camargo & Louis 2019 make that link explicitly.
- **F1** (Ashby's requisite variety). The floor on controller complexity, as in QR-009.
- **X6** ("Neural Networks — Regime-First Instantiation") is about biological neural networks, not machine learning. **Not relevant** despite its title.
- **BIO22** (metabolic cost of neural information) is biology. **Not relevant.**

### G.2 Gaps
No reference entry exists for any of:
- generalisation theory (VC, Rademacher, PAC-Bayes, compression bounds);
- double descent and benign or tempered overfitting (QR-009 R5 proposed one);
- implicit regularisation;
- neural scaling laws;
- transfer and pre-training;
- benchmark reuse, contamination and leakage;
- Goodhart in ML and reward hacking;
- distribution shift and shortcut learning;
- emergent abilities;
- ML in return prediction;
- the bitter lesson.

Per the log's rules, Mode A grounding comes before any exploration.

### G.3 Wiki items this map bears on (for owner awareness; nothing changed)
1. **CS10's "Mathematical Archetype" section says "conservation-law"** (total performance conserved over all functions). That reading is reasonable for the averaged statement. A future fold-in on inductive bias would link to CS10 rather than duplicate it.
2. **EWS9's design** (train on simulated normal forms, test on real systems) is the synthetic-prior pattern. If the owner later runs QR-008, the pooling literature here (Hernandez's shrinking multiplier; TabPFN's ≤ 10k-row scope; ossification) predicts when such a classifier should beat classical indicators. More simulated training data helps most when local data are scarce, and helps less, or hurts, when local data are plentiful and the simulated prior is mismatched. Our inference; **Speculative.**
3. **QR-009 R5** (double descent and benign overfitting) should be written with Mallinar et al.'s "tempered" result and Curth et al.'s U-turn. Otherwise it will overstate how benign interpolation is.

---

## (H) Candidate fold-in reference entries (owner decides; nothing written)

These continue QR-009 §H; where an entry overlaps one of QR-009's, the overlap is noted.

| # | Proposed entry | Core sources | Would ground / link |
|---|---|---|---|
| ML1 | Double descent, benign and tempered overfitting, with conditions and prehistory | Vallet 1989; Opper 1990; Loog 2020; Belkin 2019; Hastie 2022; Bartlett 2020; Nakkiran 2020, 2021; Mallinar 2022; Curth 2023 | **Supersedes QR-009 R5** |
| ML2 | Implicit regularisation and effective complexity in over-parameterised models | Zhang 2017/2021; Soudry 2018; Maddox 2020; MacKay 1992; Arora 2018; Lotfi 2022, 2024; Dziugaite & Roy 2017; Wilson 2025; Nagarajan & Kolter 2019; Dinh 2017; Jiang 2020 | CS10; INFO5; IT09 (drift note) |
| ML3 | Neural scaling laws: what is fitted, what is derived, where they bend | Kaplan 2020; Hoffmann 2022; Besiroglu 2024; Muennighoff 2023; Villalobos 2024; McKenzie 2023; Caballero 2023; Bahri 2024; Sardana 2024 | — |
| ML4 | Pre-training and transfer as borrowed evidence | Hernandez 2021; He 2019; Kornblith 2019; Grant 2018; Xie 2022; Hollmann 2025; Bommasani 2021 | EWS9; QR-009 §D (M5) |
| ML5 | Benchmark reuse, contamination, leakage and leaderboard selection | Recht 2019; Roelofs 2019; Mania 2019; Dwork 2015; Blum & Hardt 2015; Zhang 2024 (GSM1k); Singh 2025; Aleithan 2024; Kapoor & Narayanan 2023 | **QR-009 R4** (selection) |
| ML6 | Goodhart in machine learning: reward overoptimisation and reward hacking | Gao 2023; Skalse 2022; Manheim & Garrabrant 2018; Krakovna 2020 (blog); METR 2025 (blog); Baker 2025 (preprint) | **QR-009 R12** (Goodhart) |
| ML7 | Distribution shift and shortcut learning | Geirhos 2019, 2020; Beery 2018; Zech 2018; Winkler 2019; Koh 2021; Taori 2020; Miller 2021; Fang 2022; Hendrycks 2020; Lazer 2014; Wong 2021; Sun 2025 | QR-009 M3/M6 |
| ML8 | The emergent-abilities debate (an open-question entry) | Wei 2022; Schaeffer 2023; Ganguli 2022; Du 2024 | Vocabulary warning (criticality entries) |
| ML9 | Machine learning in return prediction, and its limits | Gu, Kelly & Xiu 2020; Leippold 2022; Avramov 2023; Kelly, Malamud & Zhou 2024; Nagel 2025; Elmore & Strauss 2026; Fallahgoul 2025; Levy 2026; Glasserman & Lin 2023 | **QR-009 R7**, D1 |
| ML10 | The bitter lesson, as a historical thesis and its critiques | Sutton 2019 (essay); Brooks 2019 (blog); Dosovitskiy 2021; Silver & Sutton 2025 (preprint) | CS10. Cite as an essay, not as a law |

**ML1, ML2 and ML5 are the priority.** ML1 and ML2 carry the reconciliation (M1 and its cures), and ML5 is the clearest M2 instance. ML3 is needed whenever the podcast or wiki quotes a scaling number. Each new entry needs an anchor at creation.

---

## (I) Candidate sub-questions, and what would decide each

| # | Sub-question | Deciding evidence | Disposition (suggested; no gate run) |
|---|---|---|---|
| S1 | Does effective-complexity accounting fully explain generalisation in feature-learning networks? | A non-vacuous bound for the *deployed, uncompressed* model; or a theory that predicts which architectures and data generalise, before training | **Open in the literature** (§D1). Not decidable in-house |
| S2 | Is Chinchilla's data term estimation variance or optimisation error? | Fixed-step experiments that vary fresh vs repeated data and noise level at matched optimisation | **Our question.** Needs a targeted prior-art search first. Frontier-scale compute; not in-house |
| S3 | Do any sharp capability transitions survive continuous metrics and adequate test resolution? | Loss-threshold studies across model families with continuous metrics | **Open** (§D2). Not in-house |
| S4 | Does leaderboard inflation follow the expected-maximum formula in N private variants and score noise? | Arena variant counts plus identical-checkpoint noise | **Likely a RESTATEMENT:** the authors already frame it as best-of-N and simulate it. A five-minute calculation (§B7) reproduces the order of magnitude. Suggested **FOLD** into ML5 |
| S5 | Is pre-training literally partial pooling (empirical Bayes) beyond MAML-linear, TabPFN and the HMM in-context model? | A quantitative mapping from pre-training to a hierarchical prior | **Partly answered** (Grant 2018; Xie 2022; Müller 2022). A targeted search is needed before calling the rest open |
| S6 | Does the virtue of complexity survive effective-complexity accounting in finance? | Out-of-sample timing gains of P ≫ T models vs their simple-rule equivalents, in new data | **Open, actively contested** (§D3). Watch item, not in-house |
| S7 | Do the sloppy-models papers already connect MacKay's effective number of parameters to the Fisher spectrum? | Targeted read: Transtrum et al. 2015; Quinn et al. 2023; MacKay 1992 | **Mode A search only**, needed before any wiki claim (drift note) |
| S8 | A double-descent demonstration for the podcast or wiki | Random-features ridge regression on a laptop | **A teaching demo, not research**: a RESTATEMENT of Hastie 2022 / Nakkiran 2021 |

**Overall.** QR-010 as worded looks headed for Gate 1 `answered` in its main form. The mechanisms of escape and of residual tax are documented under other names: effective degrees of freedom, implicit regularisation, transfer, benchmark overfitting, Goodhart, distribution shift. The likely verdict is FOLD (`found-under-other-vocabulary`) via ML1–ML7. The recognised open edges are D1, D2, D3 and D5. None is decidable in-house. The wiki's main job here is Mode A, as with QR-009.

---

## (J) Sources and reading markers

**Sub-agent markers** (SA):
- **ft** — full text, or the named sections, read by text extraction (often targeted);
- **abs** — abstract only;
- **ss** — search summary or secondary description only;
- **meta** — bibliographic record only; content from background knowledge (must be verified before quoting).

**Main-session markers** (MS):
- **cit** — DOI, title, venue and pages confirmed through Crossref;
- **arx** — arXiv record (authors, dates, comments) and abstract read through the arXiv API;
- **ft** — the cited passage or number found in the primary text by PDF or HTML extraction this session;
- **num** — computed;
- **—** — not checked by the main session.

Nothing below is upgraded. Venues the main session could not confirm are marked "per SA".

### Bitter lesson and scaling
| Source | Date / status | SA | MS |
|---|---|---|---|
| Sutton, "The Bitter Lesson", essay, incompleteideas.net | 13 Mar 2019; essay | ft | ft (date; quote; chess, Go, speech, vision) |
| Brooks, "A Better Lesson", rodneybrooks.com | 19 Mar 2019; blog | ss | — |
| Silver & Sutton, "Welcome to the Era of Experience" | ~Apr 2025; book-chapter preprint | ft (excerpts) | — |
| Yousefi & Collins, arXiv:2410.09649 | 2024; EMNLP workshop | abs | — |
| Kaplan et al., arXiv:2001.08361 | 23 Jan 2020; preprint | ft | arx, ft (Eqs. 1.1–1.3, 4.4; N^0.74/D) |
| Hoffmann et al., arXiv:2203.15556 ("Chinchilla") | 29 Mar 2022; NeurIPS 2022 per SA | ft | arx, ft (Table 3; 70B / 1.4T; E, A, B) |
| Besiroglu, Erdil, Barnett & You, arXiv:2404.10102 | Apr/May 2024; preprint | ft | arx (600,000 vs < 500) |
| Grattafiori et al., "The Llama 3 Herd of Models", arXiv:2407.21783; Llama 3.1 model card | 2024; technical report | ft-partial; ft (card) | — |
| Muennighoff et al., arXiv:2305.16264 | 2023; NeurIPS 2023 | ft | arx (4 epochs, "negligible") |
| Villalobos et al., arXiv:2211.04325 v2 | Jun 2024; preprint (ICML 2024 per SA) | abs | arx ("between 2026 and 2032") |
| Sardana, Portes, Doubov & Frankle, arXiv:2401.00448 | 2024; ICML 2024 | abs | arx (up to 10,000 tokens/param) |
| McKenzie et al., arXiv:2306.09479 | Oct 2023; TMLR | abs | arx |
| Caballero et al., arXiv:2210.14891 | 2023; ICLR 2023 per SA | abs | — |
| Schaeffer et al., arXiv:2406.04391 (downstream predictability) | 2024/25; preprint | abs | — |
| Bahri, Dyer, Kaplan, Lee & Sharma, *PNAS* 121:e2311878121 | Jul 2024 | abs | cit |
| Sharma & Kaplan, arXiv:2004.10802; Maloney, Roberts & Sully, arXiv:2210.16859; Hutter, arXiv:2102.04074 | 2020–22; JMLR per SA / preprints | abs | — |
| Snell et al., arXiv:2408.03314; Brown et al., arXiv:2407.21787 | 2024; ICLR 2025 per SA / preprint | abs | — |
| Shumailov et al., *Nature* 631:755 | 25 Jul 2024 | meta (+ abs of preprint) | cit |
| Gerstgrasser et al., arXiv:2404.01413 | Apr 2024; preprint | abs | arx |

### Over-parameterised generalisation
| Source | Date / status | SA | MS |
|---|---|---|---|
| Zhang, Bengio, Hardt, Recht & Vinyals, arXiv:1611.03530 | ICLR 2017 | ft | arx, ft (Table 1; "small constant factor"; 95.20%) |
| Zhang et al., *CACM* 64:107 ("still requires") | Mar 2021 | meta | cit |
| Belkin, Hsu, Ma & Mandal, *PNAS* 116:15849 | Aug 2019 | meta | cit (also QR-009) |
| Loog, Viering, Mey, Krijthe & Tax, *PNAS* 117:10625 | May 2020; letter | ft | cit |
| Nakkiran et al., "Deep double descent", arXiv:1912.02292; *J. Stat. Mech.* 2021:124003 | ICLR 2020 per SA; 2021 | ft (§1–2) | arx, cit |
| Nakkiran, Venkat, Kakade & Ma, arXiv:2003.01897 | ICLR 2021 | abs | arx |
| Bartlett, Long, Lugosi & Tsigler, *PNAS* 117:30063 | Dec 2020 | ft (Def. 3, Thm 4) | cit |
| Hastie, Montanari, Rosset & Tibshirani, *Ann. Statist.* 50:949 | 2022 | meta | cit (QR-009) |
| Mallinar et al., arXiv:2207.06569 | 2022 (v3 2024); NeurIPS 2022 per SA | abs | arx ("tempered"; "stopped early are benign") |
| Curth, Jeffares & van der Schaar, arXiv:2310.18988 | NeurIPS 2023 | abs, ft (Def. 1) | arx ("fold back") |
| Bartlett, Montanari & Rakhlin, *Acta Numerica* 30:87 | May 2021 | abs | cit |
| Belkin, "Fit without fear", *Acta Numerica* 30:203 | May 2021 | meta | cit |
| Soudry, Hoffer, Nacson, Gunasekar & Srebro, arXiv:1710.10345 | *JMLR* 19 (2018) | abs | arx |
| Gunasekar et al. 2017, arXiv:1705.09280; Neyshabur, Tomioka & Srebro, arXiv:1412.6614 | NeurIPS 2017 per SA; ICLR 2015 workshop | abs | — |
| Chizat & Bach, arXiv:2002.04486; Chizat, Oyallon & Bach, arXiv:1812.07956; Gissin et al., arXiv:1909.12051 | 2019–20 | abs | — |
| Geiping et al., arXiv:2109.14119 | ICLR 2022 | ft (§1) | — |
| Hochreiter & Schmidhuber, "Flat minima", *Neural Comput.* 9:1 | 1997 | meta | cit |
| Keskar et al., arXiv:1609.04836; Dinh et al., arXiv:1703.04933; Jiang et al., arXiv:1912.02178; Foret et al. (SAM), arXiv:2010.01412 | 2017–21; venues per SA | abs / ft (partial) | — |
| Dziugaite & Roy, arXiv:1703.11008 | UAI 2017 | abs, ft (§1) | arx (journal ref UAI) |
| Lotfi et al., arXiv:2211.13609 (PAC-Bayes compression) | NeurIPS 2022 per SA | abs, ft (partial) | — |
| Lotfi et al., arXiv:2312.17173 (LLM bounds) | ICML 2024 | ft (Tables 1–2) | arx ("first non-vacuous") |
| Arora, Ge, Neyshabur & Zhang, arXiv:1802.05296 | 2018; ICML 2018 per SA | abs | arx |
| Maddox, Benton & Wilson, arXiv:2003.02139 | 2020; preprint | ft-partial (Def. 2.2) | arx |
| Wilson, "(Position:) Deep learning is not so mysterious or different", arXiv:2503.02113 | ICML 2025 (position track) | abs, ft (§1) | arx ("soft inductive biases") |
| Nagarajan & Kolter, arXiv:1902.04742 | NeurIPS 2019 per SA | meta | — |
| Berner, Grohs, Kutyniok & Petersen, arXiv:2105.04026 | 2021/22 | meta | — |
| Danhofer, D'Ascenzo, Dubach & Poggio, arXiv:2507.02550 | Jul 2025; preprint | abs | — |
| Valle-Pérez, Camargo & Louis, arXiv:1805.08522 | ICLR 2019 per SA | abs | — |
| Shah et al., "Pitfalls of simplicity bias", arXiv:2006.07710 | NeurIPS 2020 per SA | abs | — |
| Dosovitskiy et al. (ViT), arXiv:2010.11929 | ICLR 2021 | ft (Table 2) | arx, ft (88.55 vs 87.54) |
| Power et al., "Grokking", arXiv:2201.02177 | Jan 2022; preprint / workshop (venue unverified) | ft | arx, ft (< 10³ vs ~10⁶ steps; "1000 times") |
| Nanda et al., arXiv:2301.05217 | ICLR 2023 per SA | ft | arx |
| Liu, Michaud & Tegmark ("Omnigrok"), arXiv:2210.01117; Lyu et al., arXiv:2311.18817 | 2023–24 | abs / ft (§1) | — |
| Jacot, Gabriel & Hongler (NTK), arXiv:1806.07572 | NeurIPS 2018 | abs | — |
| Morris et al., "How much do language models memorize?", arXiv:2505.24832 | May/Jun 2025; preprint | ft-partial | arx, ft (α = 3.64) |
| Allen-Zhu & Li, "Physics of LMs 3.3", arXiv:2404.05405 | Apr 2024; preprint | ft-partial | arx |
| Frankle & Carbin (lottery ticket), arXiv:1803.03635 | ICLR 2019 | meta | — |
| Du et al. 2019 (arXiv:1810.02054); Allen-Zhu, Li & Song 2019 (arXiv:1811.03962) | ICLR / ICML 2019 per SA | meta | — |

### Pre-training and pooling
| Source | Date / status | SA | MS |
|---|---|---|---|
| Hernandez, Kaplan, Henighan & McCandlish, arXiv:2102.01293 | Feb 2021; preprint | ft | arx, ft (Table 1; 1000×; ossification §3.1) |
| Yosinski et al. 2014; Kornblith, Shlens & Le, arXiv:1805.08974 | NIPS 2014; CVPR 2019 per SA | abs / ft (targeted) | — |
| He, Girshick & Dollár, arXiv:1811.08883 | ICCV 2019 per SA | abs | — |
| Devlin et al. (BERT), arXiv:1810.04805; Brown et al. (GPT-3), arXiv:2005.14165 | 2019; NeurIPS 2020 | abs / ft (targeted) | — |
| Bommasani et al., arXiv:2108.07258 | 2021; report | ft (targeted) | — |
| Grant, Finn, Levine, Darrell & Griffiths, arXiv:1801.08930 | ICLR 2018 per SA | abs, ft (targeted) | — |
| Xie, Raghunathan, Liang & Ma, arXiv:2111.02080 | ICLR 2022 | — | arx (found by MS) |
| Hollmann et al. (TabPFN), *Nature* 637:319 | Jan 2025 | ft (PMC) | cit |
| Grinsztajn, Oyallon & Varoquaux, arXiv:2207.08815 | 2022; NeurIPS 2022 D&B per SA | abs | arx |
| Ansari et al. (Chronos), arXiv:2403.07815 | TMLR 10/2024 | ft (targeted) | — |
| Das et al. (TimesFM), arXiv:2310.10688; Woo et al. (Moirai), arXiv:2402.02592; Rasul et al. (Lag-Llama), arXiv:2310.08278 | 2023–24; ICML 2024 per SA / preprint | abs | — |
| Meyer, Kaltenpoth, Zalipski & Müller, arXiv:2510.13654 | Feb 2026; preprint | ft (targeted) | — |
| Aksu et al. (GIFT-Eval), arXiv:2410.10393; Shchur et al. (fev-bench), arXiv:2509.26468 | 2024–25; preprints | abs; ss | — |
| Zeng et al. (DLinear), arXiv:2205.13504 | AAAI 2023 per SA | abs, ft (targeted) | — |
| Lam et al. (GraphCast), *Science* 382:1416 | Dec 2023 | ft (preprint) | cit, ft (90.3% of 1,380, preprint) |

### Where ML still pays: benchmarks, Goodhart, emergence
| Source | Date / status | SA | MS |
|---|---|---|---|
| Recht, Roelofs, Schmidt & Shankar, arXiv:1902.10811 | ICML 2019 (PMLR 97) | ft | arx, ft ("unlikely explanation"; 82.9 → 72.2; five years) |
| Roelofs et al., "A meta-analysis of overfitting in ML" | NeurIPS 2019 | abs | — |
| Mania et al., arXiv:1905.12580 | 2019; venue unverified | abs | arx |
| Dwork et al., *Science* 349:636 | Aug 2015 | meta | cit |
| Blum & Hardt, arXiv:1502.04585 | 2015 | abs | — |
| Zhang et al. (GSM1k), arXiv:2405.00332 v4 | NeurIPS 2024 D&B | abs | arx ("up to 8%"; frontier minimal) |
| Roberts et al. ("lens of time"), arXiv:2310.10628; Golchin & Surdeanu, arXiv:2308.08493; Deng et al., arXiv:2311.09783; Sainz et al., arXiv:2310.18018 | 2023–24 | abs / ss | — |
| Jain et al. (LiveCodeBench), arXiv:2403.07974; White et al. (LiveBench), arXiv:2406.19314 | 2024; ICLR 2025 (LiveBench) per SA | abs | — |
| Aleithan et al. (SWE-Bench+), arXiv:2410.06992 | Oct 2024; preprint | abs | — |
| OpenAI, "Introducing SWE-bench Verified" | Aug 2024; company blog | ss | — |
| Singh et al., "The Leaderboard Illusion", arXiv:2504.20879 | Apr/May 2025; preprint | ft | arx, ft (27 variants; best-of-N; 1052/1069) |
| Gao, Schulman & Hilton, arXiv:2210.10760 | 2022; ICML 2023 per SA | ft | arx, ft (KL_bon; regressional / extremal) |
| Manheim & Garrabrant, arXiv:1803.04585 | 2018; preprint | abs | — (QR-009) |
| Skalse, Howe, Krasheninnikov & Krueger, arXiv:2209.13085 | NeurIPS 2022 per SA | abs | arx ("only … if one of them is constant") |
| Krakovna et al., "Specification gaming" | 21 Apr 2020; DeepMind blog | ft | — |
| Baker et al., arXiv:2503.11926 | Mar 2025; preprint | abs | — |
| METR, "Recent frontier models are reward hacking" | 5 Jun 2025; blog/report | ft | ft (39/128 = 30.4%; 8/1,087 = 0.7%; evaluator monkey-patching) |
| Wei et al., arXiv:2206.07682 | TMLR 2022 | abs | arx |
| Schaeffer, Miranda & Koyejo, arXiv:2304.15004 | NeurIPS 2023 per SA | ft | arx, ft (> 92%) |
| Ganguli et al., arXiv:2202.07785 | FAccT 2022 | abs | — |
| Du et al., arXiv:2403.15796 | NeurIPS 2024 | abs | arx |
| Kapoor & Narayanan, *Patterns* 4:100804 | Aug/Sep 2023 | ss / abs | cit |

### Shift, shortcuts, rare events
| Source | Date / status | SA | MS |
|---|---|---|---|
| Geirhos et al., "Shortcut learning", *Nat. Mach. Intell.* 2:665 | Nov 2020 | abs | cit |
| Geirhos et al., texture bias, arXiv:1811.12231 | ICLR 2019 | ft | arx, ft (22.1%; 95.9%) |
| Gwern, "The Neural Net Tank Urban Legend" | web essay; secondary | ft (partial) | — |
| Ribeiro, Singh & Guestrin (LIME), arXiv:1602.04938 | KDD 2016 per SA | ft (§6.4) | — |
| Beery, Van Horn & Perona, arXiv:1807.04975 | ECCV 2018 | ft | arx, ft (20.83% → 41.08%) |
| Zech et al., *PLoS Med.* 15:e1002683 | Nov 2018 | ft | cit, ft (99.95%; 0.861; 0.717) |
| DeGrave, Janizek & Lee, *Nat. Mach. Intell.* 3:610 | May 2021 | ss | cit |
| Roberts et al., *Nat. Mach. Intell.* 3:199 | Mar 2021 | abs | cit |
| Winkler et al., *JAMA Dermatol.* 155:1135 | Oct 2019 | abs | cit |
| Koh et al. (WILDS), arXiv:2012.07421 | ICML 2021 | ft (Table 1) | arx |
| Taori et al., arXiv:2007.00644; Miller et al., arXiv:2107.04649 | NeurIPS 2020 / ICML 2021 per SA | abs | arx |
| Radford et al. (CLIP), arXiv:2103.00020 | 2021 | ft (§3.3) | — |
| Fang et al., arXiv:2205.01397 | ICML 2022 per SA | abs | arx ("more diverse training distribution") |
| Hendrycks et al., arXiv:2004.06100 | ACL 2020 | abs | arx ("larger models are not necessarily more robust") |
| Wenzel et al., "Assaying OOD generalization in transfer learning" | NeurIPS 2022 | ss | — |
| Lazer, Kennedy, King & Vespignani, *Science* 343:1203 | Mar 2014 | ft | cit, ft (100/108; 1,152; MAE values; "winter detector") |
| Wong et al., *JAMA Intern. Med.* 181:1065 | Aug 2021 | abs | cit |
| Obermeyer et al., *Science* 366:447 | Oct 2019 | ss | cit |
| NTSB, HAR-19/03 (Uber, Tempe) | Nov 2019; investigation report | ft (summary, §1.5) | — |
| Zillow Offers wind-down (8-K, press) | Nov 2021; company statement | ss | — |
| Sun et al., "gray swan tropical cyclones", *PNAS* 122 | May 2025 | ft (arXiv v3) | cit, arx, ft ("relax toward") |

### Finance
| Source | Date / status | SA | MS |
|---|---|---|---|
| Gu, Kelly & Xiu, *RFS* 33:2223 | May 2020 | ft | cit, ft (0.40% NN3; 3 layers; "tiny signal-to-noise ratio"; 1.35 / 2.45) |
| Israel, Kelly & Moskowitz, *J. Invest. Mgmt* 18(2):23 | 2020 | abs / ss | — |
| Avramov, Cheng & Metzker, *Mgmt Sci.* 69:2587 | May 2023 | abs | cit |
| Leippold, Wang & Zhou, *JFE* 145:64 | Aug 2022 | ft | cit |
| Kelly, Malamud & Zhou, *JF* 79:459 | Feb 2024 | abs, ft (targeted) | cit (QR-009 ft) |
| Nagel, NBER WP 34104 | Aug 2025; working paper | ft-partial | QR-009 ft |
| Elmore & Strauss, "Is complexity virtuous?", *Econ. Lett.* 258:112749 | Jan 2026 | ss | cit (found by MS) |
| Fallahgoul, arXiv:2506.03780 | Jun 2025; preprint | abs | arx (25–30 years) |
| Berk 2023; Buncic 2025; Cartea, Jin & Shi 2025; Kelly & Malamud 2025 | working papers | meta (via Nagel) | — |
| Didisheim, Ke, Kelly & Malamud, NBER WP 31689 | 2023; working paper | meta | — |
| Campbell & Thompson, *RFS* 21:1509 | Jul 2008 | ft (WP version) | cit |
| Lopez-Lira & Tang, arXiv:2304.07619 v6 | Oct 2025; preprint | ft-partial | — |
| Glasserman & Lin, arXiv:2309.17322 | Sep 2023; preprint | ft-partial | arx |
| Levy, "Caution ahead", *J. Accounting Res.* 64:1139 | Jun 2026 | ss / meta | cit (found by MS) |
| Lopez-Lira, Tang & Zhu, arXiv:2504.14765 | 2025; preprint | ss | arx |
| He, Lv, Manela & Wu (ChronoBERT), arXiv:2502.21206 | 2025; preprint | ft-partial | — |
| Rahimikia, Ni & Wang, arXiv:2511.18578 | Nov 2025; preprint | ft-partial | arx ("perform poorly"; from-scratch helps) |
| Noguer i Alonso & Pereira Franklin, arXiv:2606.27100 | Jun 2026; preprint | ft-partial | — |
| Makridakis et al. (M6), *IJF* 41:1315 | 2025 | ft-partial | QR-009 ft |

### Reconciliation and current directions
| Source | Date / status | SA | MS |
|---|---|---|---|
| Yue et al., arXiv:2504.13837 | NeurIPS 2025 (oral) | abs | arx |
| DeepSeek-AI (Guo et al.), *Nature* 645:633 | Sep 2025 | meta | cit |
| Shao et al., "Spurious rewards", arXiv:2506.10947 | Jun 2025; preprint | meta | — |
| Penedo et al. (FineWeb), arXiv:2406.17557; Gunasekar et al. (phi-1), arXiv:2306.11644 | 2023–24 | meta | — |
| Carlini et al. 2021 (arXiv:2012.07805), 2023 (arXiv:2202.07646) | USENIX Sec. 2021; ICLR 2023 | meta | — |
| Lotfi et al., arXiv:2407.18158 (token-level bounds) | NeurIPS 2024 per SA | meta | — |

### Corrections to common citations (collected from the sub-agents, checked where marked)
1. **"Chinchilla says 20 tokens per parameter."** The paper says to scale N and D *equally*. About 20 comes from Table 3 (1B → 20.2B ✓) and from Chinchilla's own 70B / 1.4T. Approach 3's constants implied about 70; the refit gives about 20 (Besiroglu ✓). Llama 3's fit gave about 41.
2. **Kaplan's 0.050 is for C_min** (✓). **D ∝ N^0.74 is the overfitting-avoidance relation, not the compute-optimal data rule** (compute-optimal is N ∝ C^0.73).
3. **Double descent did not start with Belkin et al. 2019:** Vallet et al. 1989; Opper et al. 1990 (Loog et al. 2020 ✓ cit).
4. **"Deep nets overfit benignly."** Interpolating deep nets are *tempered* (Mallinar ✓ abstract).
5. **Non-vacuous bounds for deep nets and LLMs** apply to stochastic or compressed surrogates. Dziugaite & Roy is a **UAI 2017** paper (✓ arXiv journal ref), on binary MNIST.
6. **Gunasekar et al. 2017's nuclear-norm bias is a conjecture;** so is Nakkiran's effective-model-complexity hypothesis.
7. **Recht et al. 2019 do not say "no adaptive overfitting".** They say adaptivity is "an unlikely explanation" (✓). The name "accuracy on the line" belongs to Miller et al. 2021.
8. **GSM1k:** "up to 13%" is the v1 preprint; the NeurIPS camera-ready says "up to 8%" (✓).
9. **Kapoor & Narayanan:** 294 papers in 17 fields in *Patterns* (2023); the preprint said 329; the live tally (May 2024) is 648 in 30 fields.
10. **The Leaderboard Illusion is a preprint,** and its simulated inflation figures are internally inconsistent.
11. **The tank detector that learned the weather is apocryphal** (Gwern, secondary). **"Husky vs wolf"** was a deliberately built bad classifier to test whether *humans* would spot it (Ribeiro et al. §6.4). **"Cows on beaches"** is an illustrative figure using a commercial API, not Beery et al.'s experiment; the measured result is camera-trap error doubling at unseen locations (✓).
12. **Uber Tempe:** the NTSB's probable cause is operator distraction. The classifier's failures are findings, not "the cause".
13. **CLIP's "75%" gap reduction is for zero-shot use only;** it is "almost entirely gone" after full supervision. Fang et al. attribute it to data diversity (✓ abstract).
14. **Gu, Kelly & Xiu:** the 0.40% R² is NN3 (✓); the 1.35 / 2.45 Sharpe ratios are attributed to NN4 in the text.
15. **Campbell & Thompson 2008 has no "0.5% R²" threshold.** Their yardstick compares R² with the squared monthly Sharpe ratio (≈ 1.2%).
16. **"Caution ahead" is by Bradford Levy alone,** in *JAR* 64:1139 (2026 ✓ cit). Glasserman & Lin's in-sample finding is that anonymised headlines did *better* (distraction dominated).
17. **Kaplan 2020's "larger models are more sample-efficient"** is about pre-training from scratch. For fine-tuning data, cite Hernandez et al. 2021, with its single-target caveat.
18. **Morris et al.'s 3.6 bits per parameter** is measured on random bitstrings in models up to 1.5B parameters. **Allen-Zhu & Li's 2 bits** is for synthetic facts with about 1,000 exposures. Do not average or conflate them.
19. **Sutton's essay is dated 13 March 2019** (✓). The 2025 "Bittersweet Lesson" blog is not by Sutton.
