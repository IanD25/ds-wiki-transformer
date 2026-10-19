"""
Content for qr010_fold_in_2026_10_19.py (audit_ref gsw-qr010-fold-in-2026-10-19).

Questions Raised Log item QR-010 (why does modern machine learning escape the complexity tax, and where
doesn't it?) sits on a patch of the wiki with almost no machine-learning content (map §G). The QR-010
literature map (docs/prior_art_reviews/QR-010_ML_COMPLEXITY_MAP_2026_10_19.md §H) proposed ML1-ML10;
the owner approved ML1, ML2 and ML5 (2026-10-19). IDs keep the map's labels, so ML3, ML4 and ML6-ML10
stay reserved for the map's other candidates. ML1 supersedes QR-009's proposed R5, which was never
written. Mode A; no conjectures, no Q-entries, no promotions, no calibration rows.

Reading rule (QR-004 / QR-005 precedent): each statement is limited to what was actually read.
Reading level per source is in each anchor's note:
  - "read by the QR-010 main session" = the main session located the passage or number in the primary text
    (PDF text extraction) or read the arXiv / Crossref abstract, as stated;
  - "QR-010 map sub-agent" = reported by a sub-agent of the map session, not re-read by the main session.
Every DOI was checked on Crossref on 2026-10-19; every arXiv id was resolved through the arXiv API.

ML2 -> IT09 is deliberately not in this file: QR-010 S7 found no source joining MacKay's count to the
sloppy-models Fisher spectrum, so no link is made (docs/prior_art_reviews/QR-010_GATES_2026_10_19.md).
"""

AUD = "gsw-qr010-fold-in-2026-10-19"
MAP = "docs/prior_art_reviews/QR-010_ML_COMPLEXITY_MAP_2026_10_19.md"


def facets(cc, tags, archetype, dsens="D-invariant"):
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
    TAGS.append((entry_id, path, primacy, confidence, f"QR-010 fold-in ({AUD}): {rationale}"))


DIM = ("Dimensional sensitivity: D-invariant. The 'dimensions' here are counts of parameters, features or "
       "samples, not physical dimensions of space, and nothing depends on the DS-internal Ω_D posit.")
MS = " Read by the QR-010 main session 2026-10-19"
SA = " QR-010 map sub-agent reading"
CR = " DOI verified on Crossref 2026-10-19."
AX = " arXiv record resolved 2026-10-19."

# ===========================================================================
# ML1 — Double descent, benign and tempered overfitting  [map ML1; supersedes QR-009 R5]
# ===========================================================================
_t = ["double descent", "benign overfitting", "tempered overfitting", "interpolation threshold",
      "minimum-norm interpolant", "ridgeless regression", "bias-variance trade-off", "effective rank",
      "label noise", "early stopping", "effective number of parameters", "peaking phenomenon",
      "over-parameterisation", "complexity tax"]
ENTRIES.append(dict(
    id="ML1", title="ML1: Double Descent, Benign and Tempered Overfitting — When Fitting the Noise Is Cheap",
    filename="ML1_double_descent_benign_tempered_overfitting.md",
    scale="cross-scale", domain="computer science · statistics", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Classical bias–variance reasoning says out-of-sample error rises as the number of fitted parameters p "
         "approaches the number of observations n. For least squares on random isotropic features the variance term "
         "is σ²γ/(1−γ) with γ = p/n < 1, which diverges at the interpolation threshold p = n (Hastie, Montanari, "
         "Rosset & Tibshirani 2022). Past that threshold the minimum-norm interpolant's risk can fall again as p "
         "keeps growing: 'double descent'.\n\n"
         "**History.** Learning-curve peaks of the minimum-norm ('pseudo-inverse') solution were shown in experiments "
         "by Vallet, Cailton & Refregier 1989 and derived by Opper et al. 1990 in statistical-physics models of "
         "learning (both via Loog et al. 2020). Belkin, Hsu, Ma & Mandal 2019 named the 'double descent' curve and "
         "extended it to random-feature models, two-layer networks and random forests.\n\n"
         "**What is proven (linear and kernel models).**\n"
         "- **Benign overfitting** (Bartlett, Long, Lugosi & Tsigler 2020): the minimum-norm interpolant in linear "
         "regression predicts well if and only if the data covariance has many low-variance directions, measured by "
         "'effective ranks' of the covariance tail that are large compared with n. The noise is then absorbed by many "
         "unimportant directions.\n"
         "- **The peak is an under-regularisation effect** in isotropic linear models: optimally tuned ℓ2 "
         "regularisation gives test performance that is monotone in both sample size and model size (Nakkiran, "
         "Venkat, Kakade & Ma 2021).\n"
         "- **Low signal-to-noise brings the classical trade-off back**: in Hastie et al.'s isotropic model, least "
         "squares beats predicting zero only when γ < SNR/(SNR + 1).\n\n"
         "**What is empirical (deep networks).**\n"
         "- Nakkiran et al. ('Deep double descent', ICLR 2020; J. Stat. Mech. 2021) report model-wise, epoch-wise and "
         "sample-wise double descent in ResNets, CNNs and Transformers. It is strongest with label noise; in a critical "
         "range of model sizes more data can hurt. Their hypothesis that the peak sits where an 'effective model "
         "complexity' equals n is stated as a conjecture.\n"
         "- **Tempered, not benign.** Mallinar et al. 2022 classify overfitting as benign (test risk → Bayes risk), "
         "tempered (finite excess risk) or catastrophic. Kernel ridge regression with power-law spectra, including "
         "ReLU neural tangent kernels, is tempered (proven). Deep networks trained to interpolation are tempered, "
         "while those stopped early are benign (empirical). Interpolating deep nets therefore pay a finite cost for "
         "label noise: the tax is reduced, not removed.\n"
         "- **The U-curve returns on an effective parameter count.** Curth, Jeffares & van der Schaar 2023 show that "
         "for linear regression with random features, trees and boosting, the second descent sits where the raw "
         "parameter count switches between different complexity axes. Plotted against an effective number of "
         "parameters evaluated on unseen inputs, the curves fold back into conventional U-shapes. Deep networks were "
         "not tested.\n\n"
         "Status: the linear and kernel results are proven and the double-descent phenomenon has been reproduced by "
         "several groups; the deep-network statements are empirical."),
        ("Mathematical Form",
         "Isotropic least squares, γ = p/n < 1 (Hastie et al. 2022):\n"
         "  variance term  R_var = σ² · γ / (1 − γ)   → ∞ as γ → 1\n"
         "  least squares beats the zero predictor only if γ < SNR / (SNR + 1)\n\n"
         "Minimum-norm interpolant (p > n):\n"
         "  β̂ = X⁺y = lim_{λ→0⁺} (XᵀX + λI)⁻¹ Xᵀy\n\n"
         "Effective ranks of the covariance tail (Bartlett et al. 2020, Definition 3), eigenvalues λ₁ ≥ λ₂ ≥ …:\n"
         "  r_k(Σ) = Σ_{i>k} λ_i / λ_{k+1},    R_k(Σ) = (Σ_{i>k} λ_i)² / Σ_{i>k} λ_i²\n"
         "  with k* = min{k ≥ 0 : r_k(Σ) ≥ b n}: if k* ≥ n/c₁ the excess risk is bounded below by a constant "
         "(not benign); benign requires k*/n → 0 and large tail ranks relative to n\n\n"
         "Overfitting taxonomy with label noise, as n → ∞ (Mallinar et al. 2022):\n"
         "  benign: R → R_Bayes;  tempered: R → R_Bayes + finite excess;  catastrophic: R → ∞"),
        ("Constraint Category",
         "Informatic (In): a statistical constraint on the out-of-sample error of a fitted model as a function of the "
         "ratio of parameters to samples, the spectrum of the data and the signal-to-noise ratio. It says when "
         "interpolating noisy training data is harmless, when it costs a finite amount, and when regularisation still "
         "wins."),
        ("DS Cross-References",
         "ML2 (implicit regularisation: the minimum-norm choice that makes interpolation benign is one instance of "
         "the bias gradient training supplies). ML5 (how out-of-sample error is measured, and when the measurement is "
         "itself biased). QR-009 map §B1 (the per-parameter variance cost; mechanism M1, estimation variance) and "
         "QR-010 map §B2, §F. Disambiguation: Bartlett et al.'s R_k has the algebraic form of a participation ratio, "
         "but of the tail of the data covariance spectrum; it is not the participation ratio of a Fisher information "
         "spectrum used in the wiki's retired effective-dimension thread (see the glossary)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "The behaviour changes at the interpolation threshold p = n, where the variance of least squares diverges; "
         "on either side the risk curve has a different shape.\n\n" + DIM),
        ("What The Math Says",
         "Give a model more adjustable knobs and, at first, it fits the real pattern better. Then, as the number of "
         "knobs approaches the number of data points, it is forced to bend itself to fit every accident in the data, "
         "and its predictions get worse: the classical overfitting peak. Keep adding knobs past that point and "
         "something surprising can happen: there are now many ways to fit the data exactly, and if the training "
         "procedure picks the simplest one, the accidents get spread thinly over many unimportant directions where "
         "they do little harm, so predictions improve again. This only works under conditions: a strong enough signal "
         "and data with many weak directions. In deep networks trained to fit noisy labels perfectly, the harm does "
         "not vanish; it shrinks to a steady, finite cost. Count the knobs the data actually pin down, rather than "
         "all the knobs, and the familiar U-shaped curve comes back."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "threshold-transition"),
))
anchor("ML1", "10.1073/pnas.1903070116", "Belkin, Hsu, Ma & Mandal 2019 - Reconciling modern machine-learning practice and the classical bias-variance trade-off (PNAS 116:15849; arXiv:1812.11118)",
       "canonical_authority",
       "Named the double-descent curve and extended it to random features, two-layer nets and random forests (the "
       "1989-90 prehistory is recorded via Loog et al. 2020). Abstract read by the QR-009 main session; QR-009 map "
       "sub-agent full text." + CR, role="progenitor")
anchor("ML1", "10.1073/pnas.1907378117", "Bartlett, Long, Lugosi & Tsigler 2020 - Benign overfitting in linear regression (PNAS 117:30063; arXiv:1906.11300)",
       "canonical_authority",
       "Effective ranks r_k, R_k (Definition 3); Theorem 4 lower bound; benign iff many low-variance directions."
       + SA + " (Definition 3, Theorem 4, full text)." + CR, role="progenitor")
anchor("ML1", "10.1214/21-AOS2133", "Hastie, Montanari, Rosset & Tibshirani 2022 - Surprises in high-dimensional ridgeless least squares interpolation (Ann. Statist. 50:949; arXiv:1903.08560)",
       "canonical_authority",
       "σ²γ/(1−γ) variance for isotropic least squares (Thm 1); least squares beats the zero predictor only for "
       "γ < SNR/(SNR+1). QR-009 map sub-agent full text (§1-2)." + CR, role="progenitor")
anchor("ML1", "10.1017/S0962492921000027", "Bartlett, Montanari & Rakhlin 2021 - Deep learning: a statistical viewpoint (Acta Numerica 30:87-201; arXiv:2103.09177)",
       "canonical_authority",
       "Survey; calls its three principles (interpolation by gradient methods, implicit regularisation, benign "
       "overfitting) a conjecture for deep nets." + SA + " (abstract only); not read by the main session." + CR,
       role="comprehensive_survey", confidence="medium")
anchor("ML1", "10.1073/pnas.2001875117", "Loog, Viering, Mey, Krijthe & Tax 2020 - A brief prehistory of double descent (PNAS 117:10625)",
       "cites", "Prehistory: Vallet, Cailton & Refregier 1989 (experiments, pseudo-inverse learning curves); Opper "
       "et al. 1990 (theory, peak at n/N = 1); Duin 2000." + SA + " (whole letter)." + CR)
anchor("ML1", "10.1088/1742-5468/ac3a74", "Nakkiran, Kaplun, Bansal, Yang, Barak & Sutskever 2021 - Deep double descent: where bigger models and more data hurt (J. Stat. Mech. 2021:124003; ICLR 2020; arXiv:1912.02292)",
       "cites", "Model-, epoch- and sample-wise double descent; strongest with label noise; EMC hypothesis is a "
       "conjecture." + SA + " (§1-2)." + CR)
anchor("ML1", "2003.01897", "Nakkiran, Venkat, Kakade & Ma 2021 - Optimal Regularization Can Mitigate Double Descent (ICLR 2021; arXiv:2003.01897)",
       "cites", "Optimally tuned ℓ2 regularisation gives monotone test performance for certain isotropic linear "
       "models." + MS + " (arXiv abstract)." + AX, source="arxiv")
anchor("ML1", "2207.06569", "Mallinar, Simon, Abedsoltan, Pandit, Belkin & Nakkiran 2022 - Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting (arXiv:2207.06569; NeurIPS 2022 per map sub-agent, venue not verified)",
       "cites", "Interpolating deep nets are tempered, early-stopped ones benign; KRR with power-law spectra (incl. "
       "ReLU NTK) tempered." + MS + " (arXiv abstract)." + AX, source="arxiv", confidence="medium")
anchor("ML1", "2310.18988", "Curth, Jeffares & van der Schaar 2023 - A U-turn on Double Descent: Rethinking Parameter Counting in Statistical Learning (NeurIPS 2023; arXiv:2310.18988)",
       "reframing_of", "On an effective number of parameters measured on unseen inputs, double-descent curves of "
       "linear regression, trees and boosting 'fold back' into convex shapes; deep nets not tested." + MS +
       " (arXiv abstract); Definition 1" + SA + "." + AX, source="arxiv")
tag("ML1", "computer_science.ml", "primary", "generalisation of over-parameterised models")
tag("ML1", "statistics_probability.inference", "secondary", "bias-variance trade-off, minimum-norm least squares")
LINKS += [
    ("ML1", "ML2", "couples to", "1", "The minimum-norm interpolant that makes overfitting benign in linear "
     "regression is the implicit bias of gradient descent from zero initialisation; ML2 records that bias and the "
     "effective-complexity measures."),
    ("ML1", "gloss_participation_ratio", "disambiguates from", "1", "Bartlett et al.'s effective rank R_k has the "
     "algebraic form of a participation ratio, but of the tail of the data covariance spectrum, not of a Fisher "
     "information spectrum. Different objects."),
]

# ===========================================================================
# ML2 — Implicit regularisation and effective complexity  [map ML2]
# ===========================================================================
_t = ["implicit regularisation", "implicit bias of gradient descent", "max-margin convergence",
      "effective complexity", "effective number of parameters", "effective dimensionality (Maddox)",
      "random-label experiment", "PAC-Bayes bound", "compression bound", "non-vacuous generalisation bound",
      "simplicity bias", "flat minima", "uniform convergence", "soft inductive bias", "over-parameterisation"]
ENTRIES.append(dict(
    id="ML2", title="ML2: Implicit Regularisation and Effective Complexity in Over-Parameterised Models",
    filename="ML2_implicit_regularisation_effective_complexity.md",
    scale="cross-scale", domain="computer science · statistics · information", status="contested",
    confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "A network with far more parameters than training examples can memorise anything, yet trained on real data "
         "it generalises. The explanation on record is that what matters is not the raw parameter count but the "
         "effective complexity of the solution the training procedure actually picks.\n\n"
         "**The capacity is real** (Zhang, Bengio, Hardt, Recht & Vinyals, ICLR 2017; CACM 2021). A CIFAR-10 "
         "Inception network trained on randomly shuffled labels reached 100% training accuracy and 9.78% test "
         "accuracy (chance). The same network trained on the true labels, with augmentation and weight decay, reached "
         "89.05% test accuracy. Random labels took only 'a small constant factor' longer to fit. Complexity measures "
         "that depend only on the hypothesis class (VC dimension, Rademacher complexity) therefore cannot explain "
         "why such networks generalise; measures that depend on the data and the training algorithm are not ruled "
         "out.\n\n"
         "**Implicit bias, proven in restricted settings.**\n"
         "- Gradient descent on linearly separable data with logistic-type loss converges in direction to the "
         "maximum-margin (hard-margin SVM) solution, only logarithmically fast (Soudry, Hoffer, Nacson, Gunasekar & "
         "Srebro 2018). This is offered as a reason why training past zero training error can help.\n"
         "- The minimum-norm interpolant is the λ → 0⁺ limit of ridge regression (ML1): 'fit exactly, choosing the "
         "smallest solution' is shrinkage in its weakest form.\n"
         "- For matrix factorisation, convergence to minimum nuclear norm is a conjecture (Gunasekar et al. 2017, by "
         "its own abstract; map sub-agent reading).\n"
         "- Stochastic-gradient noise is not necessary: full-batch training matched SGD on CIFAR-10 when explicit "
         "regularisation, gradient clipping and longer training replaced it (Geiping et al. 2022; one dataset).\n\n"
         "**Effective complexity: several measures, not one quantity.**\n"
         "- MacKay's 1992 effective number of well-determined parameters, revived by Maddox, Benton & Wilson 2020 as "
         "N_eff = Σ λ_i/(λ_i + z) over the eigenvalues of the training-loss Hessian. They report it tracks double "
         "descent (preprint).\n"
         "- Classical effective degrees of freedom, Σ Cov(ŷ_i, y_i)/σ² (QR-009 map §B2).\n"
         "- Compression and PAC-Bayes bounds. Dziugaite & Roy 2017 gave the first non-vacuous bound for a deep "
         "(stochastic) network: 16-22% on a binary MNIST task. Lotfi et al. 2024 gave the first non-vacuous bounds "
         "for pretrained language models, for compressed models: a top-1 error bound of 96.41% against ≈ 99.99% for "
         "random guessing; the uncompressed model's bound is vacuous. Such bounds show that a simple description "
         "consistent with the data exists; they do not certify the deployed model.\n"
         "- Simplicity bias: from an algorithmic-information probability–complexity bound, Valle-Pérez, Camargo & "
         "Louis 2019 argue the parameter–function map of many networks is exponentially biased towards simple "
         "functions.\n"
         "These measures agree in direction (effective complexity far below the parameter count) and have no common "
         "numerical scale.\n\n"
         "**Flatness is a correlate, not a cause.** For ReLU networks, rescaling symmetries give equivalent models "
         "with arbitrarily sharper minima (Dinh, Pascanu, Bengio & Bengio 2017).\n\n"
         "**Why the entry is contested.** Wilson 2025 (ICML position paper) argues soft inductive biases plus PAC-Bayes "
         "and countable-hypothesis bounds already characterise benign overfitting, double descent and the success of "
         "over-parameterisation, while conceding that representation learning is distinctive. Nagarajan & Kolter 2019 "
         "show that bounds built on uniform convergence can grow with the training-set size and are provably vacuous "
         "for some over-parameterised models trained by gradient descent. That rules out a proof technique, not an "
         "effective-complexity explanation, but whether effective complexity fully explains networks that learn their "
         "own features remains open in the literature (QR-010 map §D1)."),
        ("Mathematical Form",
         "Effective dimensionality (Maddox, Benton & Wilson 2020, Definition 2.2; after MacKay 1992):\n"
         "  N_eff(A, z) = Σ_{i=1}^{k} λ_i / (λ_i + z),   A = Hessian of the training loss, z > 0\n"
         "  directions with λ_i ≫ z count ≈ 1 (determined by the data); λ_i ≪ z count ≈ 0\n\n"
         "Classical effective degrees of freedom:\n"
         "  df(ŷ) = σ⁻² Σ_i Cov(ŷ_i, y_i) = tr(S)  for a linear smoother ŷ = S y\n\n"
         "Max-margin limit (Soudry et al. 2018), separable data, logistic loss, gradient descent:\n"
         "  w(t)/‖w(t)‖ → ŵ/‖ŵ‖,   ŵ = argmin ‖w‖ subject to y_n wᵀx_n ≥ 1,   convergence rate ∝ 1/log t\n\n"
         "Generic shape of the bounds (constants differ by paper):\n"
         "  PAC-Bayes:  E_Q[L] ≤ E_Q[L̂] + O( √( (KL(Q‖P) + ln(1/δ)) / n ) )\n"
         "  compression / Occam:  L ≤ L̂ + O( √( (K ln 2 + ln(1/δ)) / n ) ),  K = description length in bits"),
        ("Constraint Category",
         "Informatic (In): a constraint on generalisation set by the description length or prior mass of the solution "
         "a training procedure selects, rather than by the size of the hypothesis class."),
        ("DS Cross-References",
         "CS10 (No Free Lunch: a learner beats random guessing only by exploiting structure, i.e. through an inductive "
         "bias matched to the problem; ML2 records which biases gradient training supplies). INFO5 (Kolmogorov "
         "complexity: the compression bounds and Valle-Pérez et al.'s simplicity-bias argument are description-length "
         "and algorithmic-information arguments). ML1 (benign interpolation as the minimum-norm case). ML5 (measured "
         "generalisation is only as good as the test set). Disambiguation: Maddox et al.'s 'effective "
         "dimensionality' is a soft count of Hessian eigenvalues; it is not the participation-ratio 'effective "
         "dimension' of the wiki's retired D_eff thread, nor Mattingly's d_eff (see the glossary). Any link to IT09 "
         "(sloppy models) was considered under QR-010 sub-question S7 and not made: see "
         "docs/prior_art_reviews/QR-010_GATES_2026_10_19.md."),
        ("Mathematical Archetype",
         "Mathematical archetype: optimization-principle\n\n"
         "Among the many parameter settings that fit the training data, the training procedure selects one that "
         "extremises an implicit criterion (minimum norm, maximum margin, short description).\n\n" + DIM),
        ("What The Math Says",
         "The same network that can memorise random nonsense perfectly will, on real data, settle on a simple "
         "explanation. The training method itself prefers simple solutions: started small and nudged downhill, it "
         "finds the smallest or widest-margin fit before any contorted one. So the right measure of a trained model's "
         "complexity is how much of it the data actually pin down, or how short a description of it can be, not how "
         "many knobs it has. Several ways of counting this exist and they agree that the number is far below the "
         "knob count, but they are different counts. Whether this fully explains deep learning, or only explains it "
         "in simplified settings, is still argued."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "optimization-principle"),
))
anchor("ML2", "1611.03530", "Zhang, Bengio, Hardt, Recht & Vinyals 2017 - Understanding deep learning requires rethinking generalization (ICLR 2017; arXiv:1611.03530)",
       "canonical_authority",
       "Random-label experiment: 100% train / 9.78% test on random labels vs 89.05% test on true labels (Table 1); "
       "'a small constant factor' longer; ImageNet 95.20%." + MS + " (full text, Table 1 and §1-2)." + AX,
       role="progenitor", source="arxiv")
anchor("ML2", "10.1145/3446776", "Zhang, Bengio, Hardt, Recht & Vinyals 2021 - Understanding deep learning (still) requires rethinking generalization (Commun. ACM 64:107-115)",
       "cites", "Republication with commentary; the '(still)' marks the authors' view in 2021. Bibliographic record "
       "only; text not read." + CR, confidence="medium")
anchor("ML2", "1710.10345", "Soudry, Hoffer, Nacson, Gunasekar & Srebro 2018 - The Implicit Bias of Gradient Descent on Separable Data (JMLR 19; arXiv:1710.10345)",
       "canonical_authority",
       "Proven: gradient descent converges in direction to the max-margin solution, logarithmically slowly." + MS +
       " (arXiv abstract)." + AX, role="progenitor", source="arxiv")
anchor("ML2", "10.1162/neco.1992.4.3.415", "MacKay 1992 - Bayesian Interpolation (Neural Comput. 4:415-447)",
       "canonical_authority",
       "Origin of the effective number of well-determined parameters that Maddox et al. 2020 cite as 'MacKay "
       "1992a' for effective dimensionality (citation located by the main session in Maddox et al.'s text)." + CR +
       " MacKay's own text: see the QR-010 gate report (S7).", role="progenitor", confidence="medium")
anchor("ML2", "2003.02139", "Maddox, Benton & Wilson 2020 - Rethinking Parameter Counting in Deep Models: Effective Dimensionality Revisited (arXiv:2003.02139)",
       "cites", "N_eff(A, z) = Σ λ_i/(λ_i + z) over Hessian eigenvalues (Definition 2.2); cites MacKay 1992a and Gull "
       "1989." + MS + " (Definition 2.2 and citations located in the PDF text)." + AX + " Preprint; no venue on arXiv.",
       source="arxiv", tier=3, stability="preprint-evolving", confidence="medium")
anchor("ML2", "1703.11008", "Dziugaite & Roy 2017 - Computing Nonvacuous Generalization Bounds for Deep (Stochastic) Neural Networks with Many More Parameters than Training Data (UAI 2017; arXiv:1703.11008)",
       "cites", "First non-vacuous PAC-Bayes bound for a deep stochastic network, binary MNIST, 16-22%." + SA +
       " (abstract, §1); venue from the arXiv journal reference." + AX, source="arxiv")
anchor("ML2", "2312.17173", "Lotfi, Finzi, Kuang, Rudner, Goldblum & Wilson 2024 - Non-Vacuous Generalization Bounds for Large Language Models (ICML 2024; arXiv:2312.17173)",
       "cites", "First non-vacuous bounds for pretrained LLMs, for compressed (SubLoRA) models; top-1 error bound "
       "96.41%." + MS + " (arXiv abstract);" + SA + " (Tables 1-2)." + AX, source="arxiv")
anchor("ML2", "1805.08522", "Valle-Pérez, Camargo & Louis 2019 - Deep learning generalizes because the parameter-function map is biased towards simple functions (ICLR 2019; arXiv:1805.08522)",
       "cites", "Algorithmic-information probability-complexity bound; exponential bias towards simple functions."
       + MS + " (arXiv abstract)." + AX, source="arxiv")
anchor("ML2", "1703.04933", "Dinh, Pascanu, Bengio & Bengio 2017 - Sharp Minima Can Generalize For Deep Nets (arXiv:1703.04933; ICML 2017 per map sub-agent)",
       "cites", "Flatness notions are not reparameterisation-invariant for ReLU nets." + MS + " (arXiv abstract)." + AX,
       source="arxiv", confidence="medium")
anchor("ML2", "2109.14119", "Geiping, Goldblum, Pope, Moeller & Goldstein 2022 - Stochastic Training is Not Necessary for Generalization (ICLR 2022; arXiv:2109.14119)",
       "cites", "Full-batch training matches SGD on CIFAR-10 with explicit regularisation." + MS + " (arXiv abstract);"
       " 95.68% vs 95.70%" + SA + "." + AX, source="arxiv")
anchor("ML2", "2503.02113", "Wilson 2025 - Position: Deep Learning is Not So Mysterious or Different (ICML 2025; arXiv:2503.02113)",
       "open_in_literature", "Argues soft inductive biases plus PAC-Bayes and countable-hypothesis bounds characterise "
       "benign overfitting and double descent; concedes representation learning is distinctive." + MS +
       " (arXiv abstract)." + AX, source="arxiv")
anchor("ML2", "1902.04742", "Nagarajan & Kolter 2019 - Uniform convergence may be unable to explain generalization in deep learning (arXiv:1902.04742; NeurIPS 2019 per map sub-agent)",
       "open_in_literature", "Uniform-convergence bounds can increase with n and are provably vacuous for some "
       "over-parameterised models trained by gradient descent." + MS + " (arXiv abstract)." + AX,
       source="arxiv", confidence="medium")
tag("ML2", "computer_science.ml", "primary", "generalisation theory of over-parameterised models")
tag("ML2", "statistics_probability.bayesian", "secondary", "MacKay effective parameters; PAC-Bayes")
tag("ML2", "information_theory.kolmogorov_complexity", "secondary", "compression bounds; simplicity bias")
LINKS += [
    ("ML2", "CS10", "couples to", "1", "No Free Lunch says generalisation beyond random guessing must come from an "
     "inductive bias matched to the problem; ML2 records the biases gradient training supplies (minimum norm, "
     "maximum margin, short description)."),
    ("ML2", "INFO5", "derives from", "2", "Compression (Occam) bounds and the simplicity-bias argument of "
     "Valle-Pérez et al. 2019 are description-length / algorithmic-information arguments."),
    ("ML2", "gloss_effective_dimension", "disambiguates from", "1", "Maddox et al.'s 'effective dimensionality' is a "
     "soft count Σ λ/(λ+z) of training-loss Hessian eigenvalues (after MacKay 1992); it is not the participation "
     "ratio of a Fisher spectrum (the retired D_eff object) nor Mattingly's d_eff."),
]

# ===========================================================================
# ML5 — Benchmark reuse, contamination, leakage and leaderboard selection  [map ML5]
# ===========================================================================
_t = ["test-set reuse", "adaptive overfitting", "reusable holdout", "adaptive data analysis",
      "benchmark contamination", "data leakage", "leaderboard", "best-of-N selection", "selection bias",
      "distribution gap", "model similarity", "GSM1k", "SWE-bench", "Chatbot Arena", "reproducibility"]
ENTRIES.append(dict(
    id="ML5", title="ML5: Benchmark Reuse, Contamination, Leakage and Leaderboard Selection — When the Test Set Stops Being a Fresh Draw",
    filename="ML5_benchmark_reuse_contamination_leaderboards.md",
    scale="cross-scale", domain="computer science · statistics", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "A held-out test score estimates out-of-sample performance only if the test set is an independent draw that "
         "no modelling choice has touched. Machine learning breaks that condition in three ways, and the measured "
         "costs differ.\n\n"
         "**1. Adaptive reuse of a public test set.** Worst-case theory says repeated, adaptive queries can overfit a "
         "reused holdout; Dwork et al. 2015 give a reusable-holdout method based on differential privacy, and Blum & "
         "Hardt 2015 a leaderboard mechanism ('the Ladder'). Measured in practice, the cost was small:\n"
         "- Recht, Roelofs, Schmidt & Shankar 2019 rebuilt CIFAR-10 and ImageNet test sets following the original "
         "procedures. Accuracy fell by 3-15% (CIFAR-10) and 11-14% (ImageNet); the best ImageNet model fell from "
         "82.9% to 72.2% top-1, about five years of progress. But gains on the old test sets translated into larger "
         "gains on the new ones (ImageNet: acc_new ≈ 1.11·acc_orig − 20.2%), and the authors call adaptivity 'an "
         "unlikely explanation'. They attribute the drop to slightly harder images, a distribution gap.\n"
         "- A meta-analysis of over a hundred Kaggle competitions found 'little evidence of substantial overfitting' "
         "of the public leaderboard (Roelofs et al. 2019, NeurIPS; map sub-agent abstract reading).\n"
         "- The proposed reason: models agree in their predictions far beyond what their accuracies imply, and that "
         "similarity provably mitigates overuse (Mania et al. 2019). In selection terms, many tries count as few "
         "independent ones.\n"
         "These three studies share authors, so they are not fully independent.\n\n"
         "**2. Selection over many private variants.** Singh et al. 2025 (preprint) report that undisclosed private "
         "testing on Chatbot Arena, with the option to retract scores, 'enables a best-of-N strategy' that 'introduces "
         "an upward bias'. Meta tested 27 private variants before the Llama 4 release. Two identical model "
         "checkpoints scored 1052 and 1069. Under independent noise the expected best of N scores sits about 2.0 "
         "standard errors above its mean at N = 27 (the QR-009 §B3 formula; correlated variants give less).\n\n"
         "**3. Contamination and leakage: the test set is not independent of the model.**\n"
         "- GSM1k (Zhang et al. 2024): on 1,000 new grade-school maths problems built to match GSM8k, accuracy fell by "
         "up to 8%, with several model families showing systematic overfitting across almost all sizes, and a positive "
         "relationship (Spearman's r² = 0.36) between a model's probability of generating GSM8k examples and its "
         "gap. Many frontier models showed minimal signs of overfitting. (The v1 preprint said 'up to 13%'.)\n"
         "- SWE-Bench+ (Aleithan et al. 2024, preprint): 32.67% of SWE-Agent + GPT-4's successful patches had the "
         "solution in the issue report or comments, and 31.08% passed because of weak tests; filtering the problematic "
         "issues lowered its resolution rate from 12.47% to 3.97%.\n"
         "- Leakage in ML-based science (Kapoor & Narayanan): the 2022 preprint found errors in 17 fields affecting "
         "329 papers (the published Patterns 2023 version gives 294, per the map sub-agent). In civil-war prediction, "
         "the claimed advantage of complex ML models over logistic regression did not survive correction of "
         "leakage.\n\n"
         "**Why contested.** The 'reuse costs little' finding rests on one group's studies; the leaderboard figures are "
         "from a preprint whose own simulated inflation numbers are internally inconsistent; contamination effects "
         "vary widely between model families."),
        ("Mathematical Form",
         "Decomposition of a test-set drop (Recht et al. 2019), loss L, original test set S, population D, new test "
         "set S′ drawn from D′:\n"
         "  L_S − L_S′ = (L_S − L_D) [adaptivity gap] + (L_D − L_D′) [distribution gap] + (L_D′ − L_S′) [generalisation gap]\n\n"
         "Best of N independent noisy scores (extreme-value approximation; γ_E = Euler–Mascheroni constant):\n"
         "  E[max_{i≤N} Z_i] ≈ (1 − γ_E) Φ⁻¹(1 − 1/N) + γ_E Φ⁻¹(1 − 1/(N e))  ≤ √(2 ln N)\n"
         "  = 1.57, 2.03, 2.28 standard errors at N = 10, 27, 50 (closed form; Monte Carlo 1.54, 2.00, 2.25)\n\n"
         "Linear trend of new vs original accuracy (Recht et al. 2019):\n"
         "  CIFAR-10: acc_new = 1.69·acc_orig − 72.7%;   ImageNet top-1: acc_new = 1.11·acc_orig − 20.2%"),
        ("Constraint Category",
         "Informatic (In): a constraint on what a test score can certify. It is an unbiased estimate of out-of-sample "
         "performance only for a test draw independent of every modelling, selection and training choice; adaptive "
         "reuse, selection over variants and contamination each bias it upward by an amount set by noise, the "
         "effective number of tries and the overlap."),
        ("DS Cross-References",
         "EWS4 (error rates and selection bias in early-warning evaluation: the same lesson that an evaluation is "
         "valid only if its error rates and its selection are accounted for). EWS9 (a deep classifier scored by ROC "
         "on systems it was not trained on; its scores are interpretable to the extent the test systems were "
         "untouched by model choices). ML1, ML2 (what the test score is meant to measure). QR-009 map §B3 "
         "(selection over many tries, mechanism M2) and QR-010 map §B7, §F (the 'broken holdout' row)."),
        ("Mathematical Archetype",
         "Mathematical archetype: statistical-distribution\n\n"
         "The upward bias from picking the best of many noisy scores is a property of the distribution of the "
         "maximum (extreme-value statistics).\n\n" + DIM),
        ("What The Math Says",
         "A test score is only an honest guess at future performance if the test questions were never used to make "
         "any decision about the model. Machine learning bends that rule in three ways. Reusing the same public test "
         "for years turned out to cost surprisingly little, because the models people tried were so similar that "
         "thousands of attempts counted as few. Quietly testing many private versions and publishing only the best one "
         "is different: the winner looks better than it is purely by luck, by about two noise-widths when 27 versions "
         "are tried. And when the test questions, or their answers, leak into what the model was trained on, the "
         "score stops measuring anything new; fresh test sets built after the fact show how much the old scores were "
         "inflated, which varies a lot from model to model."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "statistical-distribution"),
))
anchor("ML5", "1902.10811", "Recht, Roelofs, Schmidt & Shankar 2019 - Do ImageNet Classifiers Generalize to ImageNet? (ICML 2019, PMLR 97:5389; arXiv:1902.10811)",
       "canonical_authority",
       "Drops 3-15% / 11-14%; 82.9 -> 72.2 top-1; 'five years of progress'; acc_new = 1.11·acc_orig − 20.2%; "
       "'Adaptivity is therefore an unlikely explanation'; gap decomposition." + MS + " (full text, passages and "
       "Table)." + AX, role="progenitor", source="arxiv")
anchor("ML5", "10.1126/science.aaa9375", "Dwork, Feldman, Hardt, Pitassi, Reingold & Roth 2015 - The reusable holdout: Preserving validity in adaptive data analysis (Science 349:636-638)",
       "canonical_authority",
       "Worst-case theory of adaptive holdout reuse and a differential-privacy remedy. Main session read the abstract "
       "of the companion arXiv:1506.02629 ('Generalization in Adaptive Data Analysis and Holdout Reuse'), not the "
       "Science text." + CR, role="progenitor", confidence="medium")
anchor("ML5", "1502.04585", "Blum & Hardt 2015 - The Ladder: A Reliable Leaderboard for Machine Learning Competitions (arXiv:1502.04585)",
       "cites", "Leaderboards can be overfit by repeated adaptive submission; a mechanism with guarantees." + MS +
       " (arXiv abstract)." + AX + " Venue not checked.", source="arxiv", tier=3, stability="preprint-evolving",
       confidence="medium")
anchor("ML5", "1905.12580", "Mania, Miller, Schmidt, Hardt & Recht 2019 - Model Similarity Mitigates Test Set Overuse (arXiv:1905.12580)",
       "cites", "ImageNet models agree well beyond their accuracy levels; similarity provably mitigates overfitting."
       + MS + " (arXiv abstract)." + AX + " Venue not verified.", source="arxiv", tier=3,
       stability="preprint-evolving", confidence="medium")
anchor("ML5", "2405.00332", "Zhang et al. 2024 - A Careful Examination of Large Language Model Performance on Grade School Arithmetic (GSM1k; NeurIPS 2024 Datasets & Benchmarks; arXiv:2405.00332)",
       "cites", "Drops up to 8% (v4 camera-ready; v1 said 13%); Spearman r² = 0.36; frontier models minimal." + MS +
       " (arXiv v4 abstract)." + AX, source="arxiv")
anchor("ML5", "2504.20879", "Singh et al. 2025 - The Leaderboard Illusion (arXiv:2504.20879)",
       "cites", "'enables a best-of-N strategy'; 'upward bias'; 27 Meta variants; identical checkpoints 1052 vs 1069."
       + MS + " (full text passages)." + AX + " Preprint, not peer-reviewed; simulated inflation figures internally "
       "inconsistent (≈100 points for 10 variants vs ≈50 for 20).", source="arxiv", tier=3,
       stability="preprint-evolving", confidence="medium")
anchor("ML5", "2410.06992", "Aleithan et al. 2024 - SWE-Bench+: Enhanced Coding Benchmark for LLMs (arXiv:2410.06992)",
       "cites", "32.67% of successful patches had leaked solutions; 31.08% weak tests; 12.47% -> 3.97%." + MS +
       " (arXiv abstract)." + AX + " Preprint.", source="arxiv", tier=3, stability="preprint-evolving",
       confidence="medium")
anchor("ML5", "10.1016/j.patter.2023.100804", "Kapoor & Narayanan 2023 - Leakage and the reproducibility crisis in machine-learning-based science (Patterns 4:100804; arXiv:2207.07048)",
       "cites", "Preprint abstract (read by the main session): 17 fields, 329 papers; civil-war prediction case. The "
       "published version's 294 papers is" + SA + " only." + CR)
tag("ML5", "computer_science.ml", "primary", "evaluation of machine-learning models")
tag("ML5", "statistics_probability.inference", "secondary", "adaptive data analysis, selection bias")
LINKS += [
    ("ML5", "EWS4", "couples to", "2", "Both concern how evaluation choices inflate apparent predictive skill: "
     "EWS4's error rates and selection on outcome; ML5's adaptive reuse, best-of-N selection and contamination. "
     "Distinct mechanisms; the shared variable is the estimated error rate."),
    ("ML5", "EWS9", "constrains", "2", "EWS9 scores a deep classifier by ROC on systems outside its training set; "
     "ML5 sets the conditions (an untouched, independent test draw; every variant counted) under which such scores "
     "measure out-of-sample skill."),
]
