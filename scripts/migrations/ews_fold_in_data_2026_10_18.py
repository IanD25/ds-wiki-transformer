"""
Content for ews_fold_in_2026_10_18.py (audit_ref gsw-ews-fold-in-2026-10-18).

Early-warning-signal (EWS) / tipping-point literature, folded in as reference_law
entries EWS1-EWS10 to ground Questions Raised Log item QR-006. Mode A; no new
conjectures, no promotions.

Every equation, number and quotation below was checked against the source text on
2026-10-18; the access level per source (full text / preprint / abstract / secondary)
is in each anchor's notes and in docs/prior_art_reviews/EWS_FOLD_IN_2026_10.md.
Where only an abstract was read, the entry text is limited to what the abstract states.
"""

AUD = "gsw-ews-fold-in-2026-10-18"


def facets(cc, tags, archetype, dsens):
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
    TAGS.append((entry_id, path, primacy, confidence, f"EWS fold-in ({AUD}): {rationale}"))


# ===========================================================================
# EWS1 — Critical slowing down and the classical indicators
# Read: Scheffer et al. 2009 full text via its reprint as Ch. 2 of Dakos's 2011 Wageningen PhD thesis
# (edepot.wur.nl/168815; the Nature typeset version was not accessible). Dakos et al. 2012 full text.
# Ditlevsen & Johnsen 2010 author draft (25 May 2010) for the Ornstein-Uhlenbeck relations.
# ===========================================================================
_t = ["critical slowing down", "early-warning signals", "lag-1 autocorrelation", "variance", "return rate",
      "fold bifurcation", "dominant eigenvalue", "Ornstein-Uhlenbeck process", "skewness", "flickering",
      "rolling window", "Kendall tau"]
ENTRIES.append(dict(
    id="EWS1", title="EWS1: Critical Slowing Down and Classical Early-Warning Signals (Scheffer et al. 2009; Dakos et al. 2012)",
    filename="EWS1_critical_slowing_down.md",
    scale="cross-scale", domain="networks · biology · earth sciences", status="established", confidence="Tier 1",
    sections=[
        ("What It Claims",
         "Near a local bifurcation such as a fold, the dominant eigenvalue of the linearised dynamics around the "
         "equilibrium goes to zero, so the system recovers ever more slowly from small perturbations: critical slowing "
         "down. Scheffer et al. (2009, *Nature* 461:53–59) review the theory and evidence. They note it can be proven "
         "for any continuous model approaching a fold (Wissel 1984), that slowing down typically starts far from the "
         "bifurcation, and that it also signals the Hopf bifurcation. Under stochastic forcing it shows up as three "
         "early-warning signals: slower recovery from perturbations, increased autocorrelation and increased variance. "
         "Flickering between states and rising skewness are added signals near a fold with strong noise.\n\n"
         "Caveats in the review itself: in principle slowing down can make the system track fluctuations less well, "
         "so variance can fall (Berglund & Gentz 2006), although in models it usually rises. False negatives arise "
         "when a shift is caused by a rare extreme event or a fast, permanent change of conditions rather than a "
         "gradual approach, when records are too short, or when the perturbation regime changes over time.\n\n"
         "Dakos et al. (2012, *PLoS ONE* 7:e41010) is the standard methods paper. It applies metric-based indicators "
         "(lag-1 autocorrelation, AR(1) coefficient, return rate, detrended fluctuation analysis, spectral measures, "
         "standard deviation, coefficient of variation, skewness, kurtosis, conditional heteroskedasticity, the BDS "
         "test) and model-based ones (time-varying AR(p), drift–diffusion–jump models, threshold AR(p), potential "
         "analysis) to two simulated harvesting time series, one slowing down and one flickering. Trends are scored "
         "by Kendall's τ within rolling windows, with sensitivity analysis over window size and detrending bandwidth "
         "and significance tested against surrogate (ARMA-fitted) series. They found \"no single best indicator\", "
         "that every method needed data-specific treatment, and that warnings apply only if conditions move the "
         "system slowly towards a bifurcation, not when forcing is faster than the system's response.\n\n"
         "SCOPE: the theory is local-bifurcation theory with weak noise. It says nothing about noise- or rate-induced "
         "tipping (EWS3), and slowing down is not specific to catastrophic shifts (EWS4, Kéfi et al. 2013)."),
        ("Mathematical Form",
         "Lag-1 autocorrelation and AR(1) fit (Dakos et al. 2012):\n"
         "  ρ₁ = E[(z_t − μ)(z_{t+1} − μ)] / σ²_z\n"
         "  z_{t+1} = a₁ z_t + ε_t,  ε_t Gaussian white noise;  ρ₁ and a₁ are equivalent\n"
         "  return rate = 1/a₁  (also written 1 − a₁)\n\n"
         "Linearised one-variable picture (Ditlevsen & Johnsen 2010, author draft):\n"
         "  ẋ = −∂ₓU_μ(x) + σ η  →  near a minimum  ẋ = −α_μ x + σ η   (Ornstein–Uhlenbeck)\n"
         "  ⟨x²⟩ = σ² / (2 α_μ)            (fluctuation–dissipation)\n"
         "  c(t) = ⟨x²⟩ exp(−α_μ |t|),  correlation time T = 1/α_μ\n"
         "  ⟨x²⟩ / T = σ²/2                (constant)\n"
         "  approaching the fold, α_μ → 0, so variance and correlation time diverge together"),
        ("Constraint Category",
         "Dynamical (Di): the warning signals are consequences of the local stability of an equilibrium. They "
         "constrain what a time series should look like before a local bifurcation under weak noise, not whether a "
         "transition will occur."),
        ("DS Cross-References",
         "NE05 (Fluctuation–Dissipation Theorem — the variance relation ⟨x²⟩ = σ²/2α). EWS2 (experimental tests). "
         "EWS3 (transitions without warning). EWS4 (false alarms and limits). EWS7 (multivariate form: the dominant "
         "covariance mode). EWS8, EWS9, EWS10 (comparisons against autocorrelation and variance). M3 (Preisach "
         "hysteresis — its Type IV paired saddle-nodes are the fold geometry these signals target)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "As a control parameter approaches a bifurcation, the leading decay rate goes to zero. Variance and "
         "autocorrelation time diverge together, in fixed ratio for the linear Ornstein–Uhlenbeck case."),
        ("What The Math Says",
         "Picture a ball in a valley being jostled by noise. As conditions change, the valley flattens before it "
         "disappears. In a flat valley the ball takes longer to roll back after each knock, so successive positions "
         "are more alike (higher lag-1 autocorrelation) and the ball wanders further (higher variance). For the "
         "simplest linear model the variance is the noise strength squared over twice the restoring rate, and the "
         "correlation time is one over the restoring rate, so both blow up as the restoring rate goes to zero, and "
         "their ratio stays fixed. These signals are generic, but only for a slow approach to a local bifurcation; "
         "methods need careful detrending, window choice and significance testing."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Di", _t, "threshold-transition", "D-invariant"),
))
anchor("EWS1", "10.1038/nature08227",
       "Scheffer et al. 2009 - Early-warning signals for critical transitions (Nature 461:53-59)",
       "canonical_authority",
       "Review. Full text read 2026-10-18 via its reprint as Chapter 2 ('Early-warning signals for critical transitions: "
       "A review') of V. Dakos's 2011 Wageningen PhD thesis (edepot.wur.nl/168815); the Nature typeset version was not "
       "accessible. Fold/Hopf slowing down, three signals, the variance-can-fall caveat and the false-negative causes "
       "checked on that text. DOI verified on Crossref.",
       role="comprehensive_survey", stability="canonical")
anchor("EWS1", "10.1371/journal.pone.0041010",
       "Dakos et al. 2012 - Methods for detecting early warnings of critical transitions in time series (PLoS ONE 7:e41010)",
       "cites",
       "Methods paper. Full text read 2026-10-18 (PLoS PDF): Table 1 indicator list, AR(1)/rho_1 definitions, Kendall tau, "
       "surrogate testing, Discussion quotes. DOI verified on Crossref.",
       stability="canonical")
anchor("EWS1", "10.1029/2010GL044486",
       "Ditlevsen & Johnsen 2010 - Tipping points: Early warning and wishful thinking (GRL 37)",
       "cites",
       "Cited here for the Ornstein-Uhlenbeck relations <x^2> = sigma^2/(2 alpha), T = 1/alpha, <x^2>/T = sigma^2/2. "
       "Read 2026-10-18 from the authors' draft dated 25 May 2010 (gfy.ku.dk/~pditlev); the version of record was not "
       "accessible. DOI verified on Crossref.", confidence="medium")
tag("EWS1", "networks_systems.dynamical_systems", "primary", "bifurcation theory of critical slowing down")
tag("EWS1", "statistics_probability.stochastic_processes", "secondary", "Ornstein-Uhlenbeck / AR(1) time-series indicators")
tag("EWS1", "biology.ecology", "secondary", "developed and applied mainly for ecological regime shifts")
LINKS += [
    ("EWS1", "NE05", "derives from", "1.5",
     "The variance signal is the fluctuation-dissipation relation for an Ornstein-Uhlenbeck process: <x^2> = sigma^2/(2 alpha), "
     "which diverges as the restoring rate alpha goes to zero at a fold (Ditlevsen & Johnsen 2010 invoke the FDT explicitly)."),
]

# ===========================================================================
# EWS2 — Experimental confirmation
# Read: Carpenter et al. 2011 author preprint (Cary Institute); Dai et al. 2012 abstract only.
# ===========================================================================
_t = ["whole-lake experiment", "food-web regime shift", "largemouth bass", "reference ecosystem", "yeast",
      "population collapse", "critical slowing down", "replicated experiment", "experimental bifurcation diagram"]
ENTRIES.append(dict(
    id="EWS2", title="EWS2: Experimental Tests of Early-Warning Signals (Carpenter et al. 2011; Dai et al. 2012)",
    filename="EWS2_ews_experiments.md",
    scale="population", domain="biology · networks", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Two independent experiments observed the signals of critical slowing down (EWS1) before a transition that "
         "the experimenters induced.\n\n"
         "Whole lake (Carpenter et al. 2011, *Science* 332:1079–1082). Top predators (largemouth bass) were added to a "
         "lake dominated by planktivorous fish over three summers (2008–2010); a nearby lake dominated by adult bass "
         "was left unmanipulated as a reference. In the abstract's words, warning signals were evident in the "
         "manipulated lake \"more than a year before the food web transition was complete\". The indicators were "
         "high variance and coefficient of variation, return rates near zero, lag-1 autocorrelations near one, high "
         "skewness, and a shift of spectral power to low frequencies, all relative to the reference lake. The authors "
         "note that early warnings may fail when a system is forced too fast.\n\n"
         "Yeast (Dai et al. 2012, *Science* 336:1175–1177; abstract only). Replicate laboratory populations of "
         "*Saccharomyces cerevisiae* were used to observe critical slowing down directly before population collapse; "
         "the authors mapped the bifurcation diagram experimentally. Near the tipping point populations became more vulnerable to disturbance, and "
         "fluctuations of population density grew in size and duration, as the theory predicts.\n\n"
         "SCOPE: both are slow, deliberate approaches to a known threshold — the case where the theory should work. "
         "They do not test noise- or rate-induced transitions, false-alarm rates, or information-theoretic indicators."),
        ("Mathematical Form",
         "No new mathematics. Both test the EWS1 predictions:\n"
         "  as the control parameter approaches the threshold,  return rate → 0,  lag-1 autocorrelation → 1,\n"
         "  variance ↑  (Carpenter et al. compare against a simultaneously monitored reference lake)"),
        ("Constraint Category",
         "Dynamical (Di): empirical confirmation that the local-bifurcation signals appear in real, noisy biological "
         "systems driven slowly towards a threshold."),
        ("DS Cross-References",
         "EWS1 (the predictions tested). EWS4 (why experiments with replicates or a reference system avoid the "
         "selection bias of historical case studies)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "An experimentally imposed slow drift of a control parameter towards a fold-type threshold, with the "
         "predicted slowing down observed before the transition."),
        ("What The Math Says",
         "If the theory of critical slowing down is right, you should see it when you push a real system slowly "
         "towards a known threshold and watch. In a lake whose food web was slowly destabilised by adding predators, "
         "the plankton record became more variable and more sluggish more than a year before the food web finished "
         "flipping, while an untouched neighbouring lake showed no such change. In replicate yeast populations near "
         "their collapse point, populations recovered more slowly and fluctuated more. These are the favourable "
         "cases; they show the signals are real, not that they are reliable in general."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Di", _t, "threshold-transition", "D-invariant"),
))
anchor("EWS2", "10.1126/science.1203672",
       "Carpenter et al. 2011 - Early warnings of regime shifts: a whole-ecosystem experiment (Science 332:1079-1082)",
       "canonical_authority",
       "Primary source. Read 2026-10-18 from the authors' preprint (caryinstitute.org reprints, line-numbered) plus the "
       "Europe PMC abstract; the 'more than a year before' quote is from the abstract. Design (2008-2010, largemouth bass, "
       "reference lake) and indicator list checked in the preprint. DOI verified on Crossref.",
       role="progenitor", stability="canonical")
anchor("EWS2", "10.1126/science.1219805",
       "Dai, Vorselen, Korolev & Gore 2012 - Generic indicators for loss of resilience before a tipping point leading to population collapse (Science 336:1175-1177)",
       "cites",
       "Abstract only (Europe PMC / PubMed 22654061), read 2026-10-18. EWS2's yeast paragraph is limited to the abstract. "
       "DOI verified on Crossref.", confidence="medium")
tag("EWS2", "biology.ecology", "primary", "whole-lake and laboratory-population experiments")
tag("EWS2", "networks_systems.dynamical_systems", "secondary", "tests of bifurcation-theory predictions")
LINKS += [
    ("EWS2", "EWS1", "tests", "1",
     "Two independent experiments (whole lake, yeast) observed the predicted rising variance/autocorrelation and slower "
     "recovery before an induced transition. Favourable cases: slow approach to a known threshold."),
]

# ===========================================================================
# EWS3 — Tipping types and transitions without warning
# Read: Ashwin et al. 2012 arXiv:1103.0169v5 (abstract + definitions); Hastings & Wysham 2010 abstract;
# Ditlevsen & Johnsen 2010 author draft (25 May 2010), full.
# ===========================================================================
_t = ["B-tipping", "N-tipping", "R-tipping", "rate-induced tipping", "noise-induced transition",
      "Dansgaard-Oeschger events", "NGRIP ice core", "non-smooth potential", "no early warning", "energy balance model"]
ENTRIES.append(dict(
    id="EWS3", title="EWS3: Tipping-Point Types and Transitions Without Warning (Ashwin et al. 2012; Hastings & Wysham 2010; Ditlevsen & Johnsen 2010)",
    filename="EWS3_tipping_types_no_warning.md",
    scale="cross-scale", domain="networks · earth sciences · biology", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "Not every abrupt transition is the slow approach to a bifurcation that critical slowing down (EWS1) assumes.\n\n"
         "Ashwin, Wieczorek, Vitolo & Cox (2012, *Phil. Trans. R. Soc. A* 370:1166–1184) separate three mechanisms. "
         "B-tipping is associated with a bifurcation of the quasi-static system. N-tipping is induced by noise. "
         "R-tipping (rate-dependent) happens when a parameter changes fast enough that the system fails to track a "
         "moving attractor; it \"need not be associated with either bifurcations or noise\" (abstract). They show all "
         "three in a simple global energy-balance climate model.\n\n"
         "Hastings & Wysham (2010, *Ecol. Lett.* 13:464–472; abstract only) argue that nonlinearity combined with "
         "environmental variability gives many ecological models no smooth potential, so a class of systems will shift "
         "with no forewarning. They illustrate this numerically under slowly changing conditions.\n\n"
         "Ditlevsen & Johnsen (2010, *GRL* 37; read from the authors' May 2010 draft) make two points. First, near a "
         "bifurcation variance and autocorrelation time are linked (⟨x²⟩/T = σ²/2 in the linear limit), so a rise in "
         "only one of them is not a sign of an approaching tipping point. Second, in high-resolution (about annual) NGRIP "
         "isotope records of 17 Dansgaard–Oeschger events, none showed a significant rise in variance or "
         "autocorrelation before the jump. They conclude the events were most probably noise-induced, with very "
         "limited predictability. That conclusion is an inference from one record type (single study).\n\n"
         "SCOPE: these results bound where EWS1 can work. They do not say transitions are unpredictable in general."),
        ("Mathematical Form",
         "Langevin picture used by Ditlevsen & Johnsen (author draft):\n"
         "  ẋ = −∂ₓU_μ(x) + σ η,   test potential U_μ(x) = x⁴/4 − x²/2 − μx,  fold at μ₀ = −2√3/9\n"
         "  B-tipping: μ(t) drifts to μ₀ — variance and autocorrelation rise before the jump\n"
         "  N-tipping: μ fixed, a large fluctuation crosses the barrier — no rise\n\n"
         "R-tipping (Ashwin et al. 2012, as stated in the abstract): a sufficiently rapid change of an input or "
         "parameter makes the system move away from a branch of attractors that, at each frozen parameter value, is "
         "still stable."),
        ("Constraint Category",
         "Dynamical (Di): a classification of transition mechanisms, of which only bifurcation-induced tipping under "
         "slow forcing carries the generic critical-slowing-down signature."),
        ("DS Cross-References",
         "EWS1 (the signals these mechanisms evade). EWS4 (false alarms — the complementary failure mode). M3 (Preisach "
         "hysteresis — its Type VI is labelled 'R-tipping'; this entry is the canonical source of that term)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "Three routes across a threshold: the threshold moves to the system (B), noise carries the system over a "
         "barrier (N), or the system cannot keep up with a moving stable state (R)."),
        ("What The Math Says",
         "There are three ways to fall off a cliff. The ground can crumble under you as conditions slowly change "
         "(B-tipping): this is the case critical slowing down warns about. A gust can knock you over the edge while "
         "the ground is still solid (N-tipping): nothing slows down first. Or the safe path can move faster than you "
         "can walk (R-tipping): the path never disappears, you just fail to follow it. Ice-core records of the abrupt "
         "glacial-era warmings show no rise in variance or autocorrelation before the jumps, which suggests they were "
         "of the noise-driven kind."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Di", _t, "threshold-transition", "D-invariant"),
))
anchor("EWS3", "10.1098/rsta.2011.0306",
       "Ashwin, Wieczorek, Vitolo & Cox 2012 - Tipping points in open systems: bifurcation, noise-induced and rate-dependent examples in the climate system (Phil. Trans. R. Soc. A 370:1166-1184)",
       "canonical_authority",
       "Primary source for the B-/N-/R-tipping taxonomy. Read 2026-10-18: abstract (Europe PMC) and arXiv:1103.0169v5 "
       "front matter; the body's formal definitions were not transcribed. DOI verified on Crossref.",
       role="progenitor", stability="canonical")
anchor("EWS3", "10.1111/j.1461-0248.2010.01439.x",
       "Hastings & Wysham 2010 - Regime shifts in ecological systems can occur with no warning (Ecol. Lett. 13:464-472)",
       "cites",
       "Abstract only (Europe PMC / PubMed 20148928), read 2026-10-18. DOI verified on Crossref.", confidence="medium")
anchor("EWS3", "10.1029/2010GL044486",
       "Ditlevsen & Johnsen 2010 - Tipping points: Early warning and wishful thinking (GRL 37)",
       "cites",
       "Read 2026-10-18 in full from the authors' draft dated 25 May 2010 (gfy.ku.dk/~pditlev/papers/bifurcation_detection_short.pdf), "
       "not the version of record: OU relations, double-well test, 17 DO events from NGRIP, conclusion. DOI verified on Crossref.",
       confidence="medium")
tag("EWS3", "networks_systems.dynamical_systems", "primary", "bifurcation / noise / rate-induced tipping taxonomy")
tag("EWS3", "earth_sciences.climate", "secondary", "climate tipping, Dansgaard-Oeschger events")
tag("EWS3", "biology.ecology", "secondary", "ecological regime shifts without warning")
LINKS += [
    ("EWS3", "EWS1", "constrains", "1.5",
     "Bounds where critical slowing down applies: N-tipping and R-tipping need not show it (Ashwin et al. 2012); systems "
     "without smooth potentials may shift with no warning (Hastings & Wysham 2010); DO events show none (Ditlevsen & Johnsen 2010)."),
    ("EWS3", "M3", "constrains", "2",
     "M3's Type VI hysteresis is labelled 'R-tipping' without a citation. Ashwin et al. 2012 is the canonical definition: "
     "loss of tracking of a moving attractor under fast parameter change, with no bifurcation or noise required. "
     "M3's use (rate-dependent damage) should be checked against it."),
]

# ===========================================================================
# EWS4 — False alarms and limits of detection
# Read: Boettiger & Hastings 2012 (JRSI) arXiv:1204.6231 abstract + methods skim; Boettiger & Hastings 2012 (PRSB)
# arXiv:1210.1204 abstract + set-up; Jäger & Füllsack 2019 full text (PMC); Kéfi et al. 2013 full text (copy hosted at UCF).
# ===========================================================================
_t = ["false positive", "false negative", "receiver operating characteristic", "prosecutor's fallacy",
      "selection bias", "detrending", "trend artefact", "model-based indicator", "non-catastrophic transition",
      "transcritical bifurcation", "Hopf bifurcation", "loss of stability"]
ENTRIES.append(dict(
    id="EWS4", title="EWS4: False Alarms and Limits of Early-Warning Detection (Boettiger & Hastings 2012; Jäger & Füllsack 2019; Kéfi et al. 2013)",
    filename="EWS4_ews_false_alarms_limits.md",
    scale="cross-scale", domain="statistics · networks · biology", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "A rising indicator is not evidence of an approaching tipping point unless its error rates are known.\n\n"
         "Error rates (Boettiger & Hastings 2012, *J. R. Soc. Interface* 9:2527–2539). Proposed early-warning methods "
         "\"hardly ever characterize their expected error rates\" (abstract). They give a model-based (likelihood) "
         "approach that quantifies the trade-off between false alarms and missed warnings with receiver operating "
         "characteristic (ROC) curves. They find these error rates \"can be quite severe for common indicators even "
         "under favourable assumptions\", and that a model-based indicator can do better.\n\n"
         "Selection bias (Boettiger & Hastings 2012, *Proc. R. Soc. B* 279:4734–4739, \"the prosecutor's fallacy\"). "
         "Choosing systems to study because they are known to have tipped biases the analysis. In simulated "
         "populations that collapsed purely by chance, common warning statistics gave an elevated rate of false "
         "positives. Experiments with replicates avoid this pitfall entirely (abstract).\n\n"
         "Trend artefacts (Jäger & Füllsack 2019, *PLoS ONE* 14:e0211072). Of 22 generic growth and decay systems "
         "with no critical transition, 11 showed a clear simultaneous rise in standard deviation and lag-1 "
         "autocorrelation: quadratic, exponential and logistic growth with absolute noise, and quadratic, logarithmic, "
         "trigonometric and logistic decay with absolute or relative noise. Scaling did not remove these false "
         "positives; detrending (local linear, global polynomial or moving average) removed all of them.\n\n"
         "Non-specificity (Kéfi et al. 2013, *Oikos* 122:641–648). Critical slowing down also precedes "
         "non-catastrophic transitions (transcritical and Hopf bifurcations, and sharp responses with no bifurcation). "
         "It indicates increasing sensitivity to perturbations, not specifically a catastrophic shift: \"indicators "
         "specific to catastrophic shifts are still lacking\" (abstract)."),
        ("Mathematical Form",
         "Detection as classification (Boettiger & Hastings 2012):\n"
         "  for a decision threshold on an indicator statistic, false-positive rate vs true-positive rate → ROC curve\n"
         "  error rates must be estimated against null (no-transition) simulations, not only on systems that tipped\n\n"
         "Bayes form of the selection bias (Boettiger & Hastings 2012b):\n"
         "  P(signal | no approach to a bifurcation) small does not imply P(no approach | signal) small"),
        ("Constraint Category",
         "Informatic (In): statistical limits on inferring an approaching transition from one realisation of a "
         "time series."),
        ("DS Cross-References",
         "EWS1 (the indicators whose error rates are at issue). EWS3 (missed warnings from N- and R-tipping). EWS9 "
         "(Bury et al. 2021, which reports ROC curves against null series). MATH1 (Bayes' theorem — the logic of the "
         "prosecutor's fallacy)."),
        ("Mathematical Archetype",
         "Mathematical archetype: statistical-distribution\n\n"
         "Warning performance is a pair of error rates estimated from the distribution of an indicator under "
         "transition and null scenarios."),
        ("What The Math Says",
         "A smoke alarm is only useful if you know how often it goes off without a fire and how often it stays quiet "
         "during one. Early-warning indicators were mostly reported without either number. When the numbers are "
         "computed they can be poor. Studying only systems that already collapsed makes the alarm look better than "
         "it is. Any steady trend in the data can make variance and autocorrelation rise with no tipping point in "
         "sight, until the trend is removed. And slowing down warns that a system is getting fragile, not that it is "
         "about to jump to a different state."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "statistical-distribution", "D-invariant"),
))
anchor("EWS4", "10.1098/rsif.2012.0125",
       "Boettiger & Hastings 2012 - Quantifying limits to detection of early warning for critical transitions (J. R. Soc. Interface 9:2527-2539)",
       "canonical_authority",
       "Primary source. Read 2026-10-18: abstract (Europe PMC) and arXiv:1204.6231v1 (ROC / likelihood approach confirmed in "
       "the methods; full results not transcribed). Quotes in EWS4 are from the abstract. DOI verified on Crossref.",
       role="progenitor")
anchor("EWS4", "10.1098/rspb.2012.2085",
       "Boettiger & Hastings 2012 - Early warning signals and the prosecutor's fallacy (Proc. R. Soc. B 279:4734-4739)",
       "cites",
       "Abstract (Semantic Scholar) and arXiv:1210.1204v1 set-up read 2026-10-18. Simulation counts not transcribed "
       "(the preprint gives several). DOI verified on Crossref.", confidence="medium")
anchor("EWS4", "10.1371/journal.pone.0211072",
       "Jäger & Füllsack 2019 - Systematically false positives in early warning signal analysis (PLoS ONE 14:e0211072)",
       "cites",
       "Full text read 2026-10-18 (PMC6364907): 11 of 22 systems, the system list, scaling vs detrending result. "
       "DOI verified on Crossref.")
anchor("EWS4", "10.1111/j.1600-0706.2012.20838.x",
       "Kéfi, Dakos, Scheffer, Van Nes & Rietkerk 2013 - Early warning signals also precede non-catastrophic transitions (Oikos 122:641-648)",
       "cites",
       "Read 2026-10-18 from a copy hosted at sciences.ucf.edu (journal typeset PDF, (c) 2012 the authors / Oikos): abstract, "
       "synthesis box, model list (fold, transcritical, Hopf, no-bifurcation). Crossref gives issued year 2012 (online); "
       "print volume is 2013. DOI verified on Crossref.")
tag("EWS4", "statistics_probability.inference", "primary", "false-alarm / missed-detection error rates of EWS")
tag("EWS4", "networks_systems.dynamical_systems", "secondary", "bifurcation types that share the slowing-down signature")
LINKS += [
    ("EWS4", "EWS1", "constrains", "1.5",
     "Classical indicators have unreported and sometimes severe error rates (Boettiger & Hastings 2012), are inflated by "
     "selecting systems that tipped (prosecutor's fallacy), rise under plain trends unless detrended (Jäger & Füllsack 2019), "
     "and are not specific to catastrophic shifts (Kéfi et al. 2013)."),
    ("EWS4", "MATH1", "derives from", "2",
     "The prosecutor's fallacy is the confusion of P(signal | no transition) with P(no transition | signal); Bayes' theorem."),
]

# ===========================================================================
# EWS5 — Information flow peaks on the disordered side (Barnett et al. 2013)
# Read: full text, authors' version dated 13 Sep 2013 (users.sussex.ac.uk/~lionelb); supplementary material downloaded
# but its derivations were not checked.
# ===========================================================================
_t = ["transfer entropy", "global transfer entropy", "multi-information", "kinetic Ising model", "Glauber dynamics",
      "disordered phase", "information flow", "mutual information peak", "early warning conjecture", "equilibrium temperature sweep"]
ENTRIES.append(dict(
    id="EWS5", title="EWS5: Information Flow Peaks on the Disordered Side of a Phase Transition (Barnett et al. 2013)",
    filename="EWS5_information_flow_disordered_peak.md",
    scale="cross-scale", domain="physics · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Barnett, Lizier, Harré, Seth & Bossomaier (2013, *PRL* 111:177203) compare static and dynamic dependency "
         "measures across the transition of the 2D ferromagnetic Ising model with Glauber dynamics (periodic "
         "boundaries; simulations at L = 512, 100 temperatures, 200 runs each). Pairwise mutual information, the "
         "global multi-information and pairwise transfer entropy all peak at T_c. Global transfer entropy T_gl — the "
         "average information flow from the whole system to a single site — peaks strictly on the disordered side, "
         "at T = 2.354 ± 0.003 against T_c ≈ 2.269. At L = 64, 128 and 256 the position of the maximum did not change "
         "at the temperature resolution used.\n\n"
         "They conjecture this is universal for a class of complex dynamical systems. They suggest a possible "
         "warning: if T_gl, estimated over time windows short compared with the change in the order parameter, peaks "
         "while the multi-information keeps rising, the system may be approaching criticality from the disordered "
         "side. They name financial crashes and some epileptic seizures as candidate applications, and state that "
         "further research is needed \"both in complex dynamical models and on real-world data\".\n\n"
         "SCOPE (read from the paper): the result is a peak in temperature, measured at equilibrium at each "
         "temperature. No time series was driven through the transition and no lead time was measured; the warning "
         "use is a proposal. The measures are lag-1 and short-range (ℓ = 1 history). The authors do not claim an "
         "analytic expression for either transfer-entropy measure. The first-order extension is STAT6 (Brown, "
         "Bossomaier & Barnett 2022). Single study: contested until independently reproduced."),
        ("Mathematical Form",
         "Transfer entropy (Schreiber 2000):  T_{Y→X} = I( X(t) : Y^{(ℓ)}(t) | X^{(ℓ)}(t) )\n"
         "Pairwise MI:          I_pw = (1/2N) Σ_⟨i,j⟩ I(S_i : S_j)\n"
         "Multi-information:    I_gl = Σ_i H(S_i) − H(S)\n"
         "Pairwise TE (ℓ = 1):  T_pw = (1/2N) Σ_⟨i,j⟩ T_{S_j→S_i}\n"
         "Global TE (ℓ = 1):    T_gl = (1/N) Σ_i T_{S→S_i}\n\n"
         "Glauber flip probability:  P_i(s) = [1 + e^{βΔH_i(s)}]⁻¹,  ΔH_i(s) = 2 s_i Σ_{j∈ν(i)} s_j\n"
         "2D Ising:  β_c = ½ log(1 + √2),  T_c ≈ 2.269;   reported argmax_T T_gl = 2.354 ± 0.003 (L = 512)"),
        ("Constraint Category",
         "Informatic (In): a claim about where an information-flow observable peaks relative to an equilibrium phase "
         "transition."),
        ("DS Cross-References",
         "STAT6 (Brown, Bossomaier & Barnett 2022 — the first-order Potts extension, built on this paper). INFO4 "
         "(Mutual Information — transfer entropy is a conditional mutual information). EWS1 (the classical signals "
         "the proposed warning would compete with; no comparison is made here). STAT3 / X0_FIM_Regimes (CCA and X0 "
         "context, via STAT6)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "A dynamic, past-conditioned dependency measure peaks off-critical (disordered side) while static "
         "dependency measures peak at the critical point."),
        ("What The Math Says",
         "Measure how much the spins of a magnet depend on each other, in two ways. The static way (mutual "
         "information) asks how much knowing one spin tells you about another at the same moment; it peaks exactly "
         "at the critical temperature. The dynamic way (global transfer entropy) asks how much the whole lattice's "
         "previous state tells you about a spin's next flip, beyond what its own past tells you. In simulations it "
         "peaks a little above the critical temperature, on the disordered side. So a system cooling slowly towards "
         "the transition might show the dynamic measure peaking and turning down while the static one is still "
         "rising — a possible warning. That last step was proposed, not tested."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "threshold-transition", "D-sensitive"),
))
anchor("EWS5", "10.1103/PhysRevLett.111.177203",
       "Barnett, Lizier, Harré, Seth & Bossomaier 2013 - Information flow in a kinetic Ising model peaks in the disordered phase (PRL 111:177203)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 from the authors' version dated 13 Sep 2013 (users.sussex.ac.uk/~lionelb, "
       "Ising_TE_PRL.pdf): abstract, Eqs. 1-13, T_gl maximum 2.354 +/- 0.003, L = 64-512 check, the time-window warning "
       "proposal and 'further research' sentence. Supplementary material downloaded, derivations not checked. "
       "DOI verified on Crossref.",
       role="progenitor")
tag("EWS5", "physics.modern.statistical_mechanics", "primary", "kinetic Ising model across its phase transition")
tag("EWS5", "information_theory.shannon", "secondary", "transfer entropy / mutual information measures")
LINKS += [
    ("STAT6", "EWS5", "derives from", "1.5",
     "Brown, Bossomaier & Barnett 2022 extend Barnett et al. 2013's disordered-side global-transfer-entropy peak from the "
     "continuous Ising transition to first-order Potts transitions (q = 5, 7, 10)."),
    ("EWS5", "INFO4", "derives from", "2",
     "Transfer entropy is a conditional mutual information, T_{Y->X} = I(X(t) : Y^(l)(t) | X^(l)(t)); the paper compares it "
     "with pairwise MI and the multi-information."),
    ("EWS5", "EWS1", "predicts for", "2",
     "Proposes a warning (T_gl peaking while multi-information still rises) that would compete with critical slowing down "
     "for approaches from the disordered side. Proposal only: no driven time series, lead time or comparison with "
     "autocorrelation/variance in the paper."),
]

# ===========================================================================
# EWS6 — The ecological "Fisher Information" index
# Read: Fath, Cabezas & Pawlowski 2003 NOT read (paywalled); Karunanithi, Cabezas, Frieden & Pawlowski 2008 full text
# (Ecol. Soc., incl. equation images 1, 4, 5); Spanbauer et al. 2014 full text (PMC); Burnett 2019 dissertation abstract.
# ===========================================================================
_t = ["Fisher information index", "sustainable regimes hypothesis", "dynamic order", "size of states",
      "shift-invariant Fisher information", "probability amplitude", "regime shift", "paleoecology", "diatoms",
      "Foy Lake", "variance proxy", "Cabezas"]
ENTRIES.append(dict(
    id="EWS6", title="EWS6: The Ecological Fisher Information Index for Regime Shifts (Fath, Cabezas & Pawlowski 2003)",
    filename="EWS6_fisher_information_index.md",
    scale="cross-scale", domain="biology · information · earth sciences", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "A group around H. Cabezas at the U.S. EPA (with Fath, Pawlowski, Mayer, Karunanithi and colleagues) uses a "
         "Fisher information computed from a system's trajectory as an index of \"dynamic order\". The form was "
         "introduced by Fath, Cabezas & Pawlowski (2003, *J. Theor. Biol.* 222:517–530; not read this pass). "
         "Karunanithi, Cabezas, Frieden & Pawlowski (2008, *Ecol. Soc.* 13(1):22) give the derivation and the "
         "time-windowed estimator now in use. Take the parameter to be the ergodic mean ⟨y⟩, write s = y − ⟨y⟩, and "
         "assume the fluctuations are independent of the mean. Then the parameter drops out and I depends only on the "
         "density p(s) of the fluctuations. The authors note this independence becomes an approximation near a "
         "transition, where fluctuations grow and become asymmetric. Earlier work computed I from first and second "
         "time derivatives of the series; the 2008 method instead bins points within each time window into states "
         "whose size is set by an uncertainty per variable, and computes I from the binned distribution.\n\n"
         "The \"sustainable regimes hypothesis\" (as stated by Karunanithi et al.): a regime has a time-averaged "
         "Fisher information that does not change; steadily declining FI signals loss of dynamic order; and the "
         "shift between regimes is marked by a steep drop in FI.\n\n"
         "Application. Spanbauer et al. (2014, *PLoS ONE* 9:e108936) applied the index to 109 diatom species in a "
         "Foy Lake (Montana) sediment record, with windows of 10 time steps and the size of states set from each "
         "species' standard deviation in the least variable window. Univariate indicators (variance, skewness, "
         "kurtosis, autocorrelation) were weak and inconsistent across species. Mean FI declined steadily over a "
         "~2 kyr period of instability before the shift, which they read as a warning. One record, assessed visually, "
         "with no significance test or null model.\n\n"
         "Critique. A 2019 University of Nebraska–Lincoln PhD dissertation (J. L. Burnett, *Regime detection measures "
         "for the practical ecologist*; abstract only) found a proposed 'velocity' measure more robust to data loss "
         "than Fisher Information or the Variance Index, and called the regime-detection metrics inconsistent, not "
         "generalizable and not validated with probabilistic measures of certainty.\n\n"
         "IDENTITY CHECK (standard result): the quantity in Eq. 4 is the location (shift-invariant) Fisher information "
         "of p(s). For a Gaussian p(s) of variance σ² it equals 1/σ², so for near-Gaussian fluctuations a falling FI "
         "index is the same signal as rising variance. Whether the binned, multivariate estimator adds anything beyond "
         "pooled dispersion has not been tested (QR-006 sub-question 2). Contested: claims of a leading indicator rest "
         "largely on the developers' own case studies."),
        ("Mathematical Form",
         "Fisher information about the ergodic mean (Karunanithi et al. 2008, Eqs. 4–5; Eq. 4 attributed there to "
         "Fath et al. 2003):\n"
         "  I = ∫ ds (1/p(s)) [dp(s)/ds]²\n"
         "  I = 4 ∫ ds [dq(s)/ds]²,   q²(s) ≡ p(s)\n\n"
         "Standard identity (location family, IT05):  p(s) = N(0, σ²)  ⇒  I = 1/σ²\n\n"
         "Estimator (Karunanithi et al. 2008; Spanbauer et al. 2014): split the n-variable series into overlapping "
         "windows; two points are the same state if |x_i(t_a) − x_i(t_b)| ≤ size-of-states_i for every variable i; "
         "count points per state → p(s); compute I per window from the discrete form in Karunanithi et al. 2008 (not "
         "transcribed here)."),
        ("Constraint Category",
         "Informatic (In): a summary statistic of the occupancy distribution of a trajectory, proposed as an index of "
         "regime stability."),
        ("DS Cross-References",
         "IT05 (Fisher Information — the location-family form used here). EWS1 (variance, the signal this index "
         "reduces to for Gaussian fluctuations). X0_FIM_Regimes (shares the words 'Fisher information' and 'regime', "
         "but X0 reads the spectrum of a matrix built from a spatial correlation kernel — a different object). BIO16 "
         "(Frank's Fisher information in selection theory — also a different object)."),
        ("Mathematical Archetype",
         "Mathematical archetype: statistical-distribution\n\n"
         "A functional of the empirical distribution of states visited within a time window, tracked from window to "
         "window."),
        ("What The Math Says",
         "Within each stretch of time, count how often the system revisits nearly the same state. If it keeps "
         "returning to the same few states, the distribution is sharp and this Fisher information is high (\"orderly\"). "
         "If it wanders over many states, the distribution is flat and the number is low. A regime is supposed to "
         "keep the number steady, and a shift is supposed to show up as a drop. For a bell-shaped spread the number "
         "is exactly one over the variance, so a drop is the same as variance rising — the classical warning seen "
         "through a different formula. Whether the multi-species, binned version captures anything more is unproven."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "statistical-distribution", "D-invariant"),
))
anchor("EWS6", "10.1016/S0022-5193(03)00067-5",
       "Fath, Cabezas & Pawlowski 2003 - Regime changes in ecological systems: an information theory approach (J. Theor. Biol. 222:517-530)",
       "canonical_authority",
       "Progenitor of the index. NOT READ: paywalled (ScienceDirect 403), no open copy found 2026-10-18; no abstract retrieved. "
       "Bibliographic record verified on Crossref. Its content enters EWS6 only through Karunanithi et al. 2008, which states "
       "that Fath et al. 2003 derived Eq. 4 and computed I from first and second time derivatives.",
       role="progenitor", confidence="medium")
anchor("EWS6", "10.5751/ES-02318-130122",
       "Karunanithi, Cabezas, Frieden & Pawlowski 2008 - Detection and assessment of ecosystem regime shifts from Fisher information (Ecol. Soc. 13(1):22)",
       "cites",
       "Full text read 2026-10-18 (ecologyandsociety.org HTML; Eqs. 1, 4, 5 read from the equation images): derivation, "
       "independence-from-mean assumption and its caveat, sustainable regimes hypothesis, windowed binning estimator. "
       "DOI verified on Crossref.")
anchor("EWS6", "10.1371/journal.pone.0108936",
       "Spanbauer et al. 2014 - Prolonged instability prior to a regime shift (PLoS ONE 9:e108936)",
       "cites",
       "Full text read 2026-10-18 (PMC4184814): 109 species, 10-step windows, size of states from the least variable window, "
       "~2 kyr instability, univariate indicators weak. Eq. 2 is an image not transcribed. DOI verified on Crossref.")
tag("EWS6", "biology.ecology", "primary", "regime-shift index from ecological time series")
tag("EWS6", "statistics_probability.inference", "secondary", "location Fisher information of an empirical density")
tag("EWS6", "earth_sciences.climate", "secondary", "paleoecological / climate-driven regime shift application")
LINKS += [
    ("EWS6", "IT05", "derives from", "1.5",
     "I = integral (1/p)(dp/ds)^2 ds is the Fisher information of a location family p(s - theta); for a Gaussian it is 1/sigma^2."),
    ("EWS6", "EWS1", "couples to", "2",
     "Shares the variance: for near-Gaussian fluctuations a falling FI index (I = 1/sigma^2) is the rising-variance signal. "
     "Whether the binned multivariate estimator adds anything beyond pooled dispersion is untested (QR-006 sub-question 2)."),
    ("EWS6", "X0_FIM_Regimes", "disambiguates from", "1",
     "Both speak of 'Fisher information' and 'regimes', but the index is a scalar location FI of a windowed occupancy density "
     "along a trajectory, while X0 reads the singular-value spectrum of a matrix built from a spatial correlation kernel. "
     "Different mathematical objects; do not treat as the same method."),
    ("EWS6", "BIO16", "disambiguates from", "2",
     "Two Fisher-information uses in biology: Frank's (BIO16) is the FI of type-frequency change in selection theory; this "
     "index is the location FI of a state-occupancy density. Different objects."),
]

# ===========================================================================
# EWS7 — Covariance-eigenvalue and dominant-mode indicators
# Read: Brock & Carpenter 2006 full text (Ecol. Soc. HTML); Chen et al. 2019 full text (PMC); Chen et al. 2012 full text
# (PMC); Held & Kleinen 2004 abstract via an index (EarthRef), not the paper; Kritzman et al. 2011 secondary sources only.
# ===========================================================================
_t = ["covariance matrix", "largest eigenvalue", "eigenvalue share", "principal component", "degenerate fingerprinting",
      "dynamical network biomarker", "absorption ratio", "multivariate early warning", "dominant mode",
      "codimension-one bifurcation", "systemic risk", "participation ratio"]
ENTRIES.append(dict(
    id="EWS7", title="EWS7: Covariance-Eigenvalue and Dominant-Mode Early-Warning Indicators (Held & Kleinen 2004; Brock & Carpenter 2006; Chen et al. 2012, 2019)",
    filename="EWS7_covariance_eigenvalue_indicators.md",
    scale="cross-scale", domain="networks · biology · finance", status="established", confidence="Tier 2",
    sections=[
        ("What It Claims",
         "In many variables, critical slowing down concentrates fluctuations onto the one slow direction: the "
         "eigenvector of the Jacobian whose eigenvalue goes to zero. Several groups turned this into indicators.\n\n"
         "Degenerate fingerprinting (Held & Kleinen 2004, *GRL* 31; abstract via an index only). Estimate the "
         "system's smallest decay rate and follow its trend, as the diagnostic most directly linked to distance from a "
         "bifurcation; demonstrated on the North Atlantic overturning circulation in the CLIMBER-2 model. Weinans et "
         "al. 2021 describe the method as the autocorrelation of the data projected on the first principal component.\n\n"
         "Largest covariance eigenvalue (Brock & Carpenter 2006, *Ecol. Soc.* 11(2):9). In a spatial model of "
         "pollutant and ecosystem-service variables, the indicator for each time step is the largest eigenvalue of "
         "the covariance matrix. It is strongly affected by the spatial unit nearest a critical point and only "
         "lightly by units that are merely noisy, so it rises before the regime shift without knowledge of the "
         "mechanism.\n\n"
         "Eigenvalue share (Chen, O'Dea, Drake & Epureanu 2019, *Sci. Rep.* 9:2572). For a linear stochastic system "
         "near a codimension-one bifurcation they prove that the largest covariance eigenvalue increases and becomes "
         "dominant over the others. They propose two indicators: σ₁, and its share of the eigenvalue norm. The "
         "eigenvector of σ₁ locates the regions most vulnerable to the transition.\n\n"
         "Dynamical network biomarkers (Chen, Liu, Liu, Li & Aihara 2012, *Sci. Rep.* 2:342). Before a critical "
         "transition a dominant group of variables appears in which (i) average within-group correlations rise "
         "sharply in absolute value, (ii) correlations with the rest fall, and (iii) standard deviations rise. They "
         "combine these into a composite index and apply it to microarray data of three diseases.\n\n"
         "Finance (Kritzman, Li, Page & Rigobon 2011, *J. Portfolio Mgmt* 37(4):112; not read — secondary sources "
         "only). The 'absorption ratio' is the fraction of total variance explained by a fixed number of leading "
         "eigenvectors, proposed as a measure of systemic risk.\n\n"
         "SCOPE: the theory (Chen et al. 2019) is linear and local; the applications are single-group demonstrations. "
         "These indicators are the multivariate form of EWS1, not a different mechanism. A participation ratio "
         "(Σσ)²/Σσ² falling towards 1 measures the same concentration."),
        ("Mathematical Form",
         "Covariance eigenvalues σ₁ ≥ σ₂ ≥ … ≥ σ_N of the windowed multivariate series (Chen et al. 2019):\n"
         "  indicator 1:  σ₁\n"
         "  indicator 2:  σ₁ / √(σ₁² + … + σ_N²)\n"
         "  near a codimension-one bifurcation the dominant Jacobian eigenvalue → 0 and σ₁ comes to dominate\n\n"
         "Related concentration measures (for comparison, not from these papers):\n"
         "  explained-variance share  Σ_{i≤k} σ_i / Σ_i σ_i   (the absorption ratio's form)\n"
         "  participation ratio       PR = (Σ_i σ_i)² / Σ_i σ_i²   (PR → 1 as one mode dominates)\n\n"
         "DNB conditions (Chen et al. 2012): within-group |PCC| ↑,  group-to-rest |PCC| ↓,  within-group SD ↑"),
        ("Constraint Category",
         "Dynamical (Di): the multivariate statement of critical slowing down — the slow mode's variance grows and "
         "dominates the covariance spectrum."),
        ("DS Cross-References",
         "EWS1 (the univariate case). EWS8 (Weinans et al. 2021 benchmark these against each other). STAT5 "
         "(correlation-matrix spectra at an equilibrium critical point — the static counterpart). STAT3 / CCA "
         "(d_eff as a participation ratio of correlation-matrix eigenvalues; using its collapse as a warning signal "
         "restates this entry). X0_FIM_Regimes (X0's 'one dominant direction' and its finance concentration case are "
         "this concentration idea)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "Approaching a bifurcation, one eigenvalue of the covariance matrix grows and comes to dominate the "
         "spectrum."),
        ("What The Math Says",
         "Watch many variables at once, such as species, genes or stock prices. When a system nears a tipping point, "
         "one combination of variables becomes very slow to recover and soaks up most of the fluctuation. In the "
         "covariance matrix of the data this shows up as one eigenvalue growing and dwarfing the rest, and its "
         "eigenvector points at the parts of the system most at risk. The biomarker version looks for a cluster of "
         "variables that suddenly move together, fluctuate more, and decouple from everything else. All of these are "
         "critical slowing down seen in many dimensions."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("Di", _t, "threshold-transition", "D-invariant"),
))
anchor("EWS7", "10.5751/ES-01777-110209",
       "Brock & Carpenter 2006 - Variance as a leading indicator of regime shift in ecosystem services (Ecol. Soc. 11(2):9)",
       "canonical_authority",
       "Primary source for the largest-covariance-eigenvalue indicator. Full text read 2026-10-18 (ecologyandsociety.org HTML; "
       "Appendix 1 not read). DOI verified on Crossref.",
       role="progenitor")
anchor("EWS7", "10.1038/s41598-019-38961-5",
       "Chen, O'Dea, Drake & Epureanu 2019 - Eigenvalues of the covariance matrix as early warning signals for critical transitions in ecological systems (Sci. Rep. 9:2572)",
       "cites",
       "Full text read 2026-10-18 (PMC6385210): both indicators incl. sigma_1/sqrt(sum sigma_i^2), codimension-one result "
       "(proof in the SI, not read), refs to Brock & Carpenter 2006 as prior. DOI verified on Crossref.")
anchor("EWS7", "10.1038/srep00342",
       "Chen, Liu, Liu, Li & Aihara 2012 - Detecting early-warning signals for sudden deterioration of complex diseases by dynamical network biomarkers (Sci. Rep. 2:342)",
       "cites",
       "Full text read 2026-10-18 (PMC3314989): the three DNB conditions, composite index (formula is an image, not "
       "transcribed), three microarray datasets. DOI verified on Crossref.")
anchor("EWS7", "10.1029/2004GL020972",
       "Held & Kleinen 2004 - Detection of climate system bifurcations by degenerate fingerprinting (GRL 31)",
       "cites",
       "Paper NOT read (Wiley 403). Abstract text read via the EarthRef reference index, 2026-10-18: smallest decay rate and "
       "its trend; CLIMBER-2 thermohaline circulation. DOI verified on Crossref.", confidence="medium")
anchor("EWS7", "10.3905/jpm.2011.37.4.112",
       "Kritzman, Li, Page & Rigobon 2011 - Principal components as a measure of systemic risk (J. Portfolio Mgmt 37(4):112-126)",
       "cites",
       "Paper NOT read (paywalled; SSRN 403). Absorption-ratio definition known only from secondary sources (2026-10-18); "
       "the number of eigenvectors used is not verified. DOI verified on Crossref.", confidence="low")
tag("EWS7", "networks_systems.dynamical_systems", "primary", "multivariate critical slowing down")
tag("EWS7", "statistics_probability.stochastic_processes", "secondary", "covariance spectra of linear stochastic systems")
tag("EWS7", "biology.molecular", "secondary", "dynamical network biomarkers from gene-expression data")
LINKS += [
    ("EWS7", "EWS1", "generalizes", "1.5",
     "Univariate rising variance is the one-variable case of the dominant covariance mode growing near a codimension-one "
     "bifurcation (Chen et al. 2019)."),
    ("EWS7", "STAT5", "analogous to", "2",
     "Both read the eigenvalues of a correlation/covariance matrix near a transition: STAT5 at an equilibrium critical point "
     "(rank law), EWS7 in a time series approaching a bifurcation (dominant-mode growth)."),
    ("EWS7", "STAT3", "analogous to", "2",
     "CCA's d_eff is a participation ratio of correlation-matrix eigenvalues; using its collapse as a warning signal "
     "restates the dominant-eigenvalue indicators here (QR-006 map: RESTATEMENT). CCA's use to classify transition order "
     "from an equilibrium temperature sweep is not addressed by these papers."),
    ("EWS7", "X0_FIM_Regimes", "analogous to", "2",
     "X0's 'one dominant direction' signature and its finance concentration case match the covariance-concentration idea; "
     "the finance case is close to the absorption ratio (Kritzman et al. 2011). X0's label is unchanged (owner decision pending)."),
]

# ===========================================================================
# EWS8 — Multivariate indicator benchmark (Weinans et al. 2021)
# Read: full text (PMC8080839).
# ===========================================================================
_t = ["multivariate indicators", "benchmark", "plant-pollinator model", "mutual information", "measurement noise",
      "data resolution", "Kendall tau", "min/max autocorrelation factor", "explained variance", "no single best indicator"]
ENTRIES.append(dict(
    id="EWS8", title="EWS8: Benchmark of Multivariate Resilience Indicators (Weinans et al. 2021)",
    filename="EWS8_multivariate_indicator_benchmark.md",
    scale="cross-scale", domain="networks · biology · information", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Weinans, Quax, van Nes & van de Leemput (2021, *Sci. Rep.* 11:9148) compare multivariate indicators of "
         "resilience loss on a plant–pollinator model with a known transition. The model has a 4-dimensional version "
         "and two 20-dimensional versions (full and partial network collapse). The indicators include averages of "
         "univariate autocorrelation and variance, mutual information, degenerate fingerprinting, explained variance "
         "of a PCA, the maximum covariance eigenvalue, the eigenvalue of a min/max autocorrelation factor (MAF) "
         "analysis, and cross-correlations. Six scenarios degrade the data or the system: shorter series (10,000 → "
         "1,000 points), lower resolution, measurement noise, multiplicative noise, unobserved variables, and "
         "reactivity. Performance is the Kendall τ of each indicator's trend towards the transition — a trend "
         "strength, not an ROC or a false-alarm rate.\n\n"
         "Main result, in the abstract's words: \"there is not one method outperforming the others\"; the best choice "
         "depends on the scenario, and the paper gives guidelines. With reduced resolution, autocorrelation-based "
         "indicators did poorly and variance-based ones held up. Mutual information was the indicator most strongly "
         "affected by measurement noise. The authors explain why: for a bivariate normal distribution lag-1 mutual "
         "information is a fixed function of lag-1 autocorrelation, so the difference in performance comes from "
         "estimation. MI needs more data, increasingly so in high dimension, and they conclude it \"might not be the "
         "most practical choice\" unless degrees of freedom can be reduced or data are plentiful.\n\n"
         "LINEAR-GAUSSIAN EQUIVALENCE (recorded here; the transfer-entropy part is not from Weinans et al.). For "
         "Gaussian data the information measures are functions of the classical statistics. Lag-1 mutual information "
         "is −½ log(1 − ρ²) (above). For jointly Gaussian processes, Granger causality equals twice the transfer "
         "entropy (Barnett, Barrett & Seth 2009, *PRL* 103:238701, Eq. 13). The location Fisher information of a "
         "Gaussian fluctuation density is 1/σ² (EWS6). An information-theoretic indicator can therefore add warning "
         "skill over autocorrelation and variance only through non-Gaussian or nonlinear structure, or through "
         "different estimation behaviour.\n\n"
         "SCOPE: one model family and one group's implementation; trend strength rather than error rates. Single "
         "study: contested until reproduced."),
        ("Mathematical Form",
         "Gaussian identity quoted by Weinans et al. (bivariate normal, lag-1 autocorrelation ρ):\n"
         "  MI = −½ log(1 − ρ²)\n"
         "  so lag-1 MI is a monotone function of ρ for Gaussian data and carries no extra information about slowing down\n\n"
         "Granger causality vs transfer entropy, jointly Gaussian processes (Barnett, Barrett & Seth 2009, Eqs. 12–13):\n"
         "  T_{Y→X|Z} = ½ ln( |Σ(X | X⁻ ⊕ Z⁻)| / |Σ(X | X⁻ ⊕ Y⁻ ⊕ Z⁻)| ),   F_{Y→X|Z} = 2 T_{Y→X|Z}\n\n"
         "Performance score:  Kendall τ between the indicator and the control parameter (or time) on the approach"),
        ("Constraint Category",
         "Informatic (In): a comparative estimate of which indicators keep their signal under realistic data "
         "limitations."),
        ("DS Cross-References",
         "EWS1 and EWS7 (the indicators compared). INFO4 (Mutual Information — the one information-theoretic "
         "indicator in the benchmark). EWS9 (a different benchmark design: ROC against null series)."),
        ("Mathematical Archetype",
         "Mathematical archetype: statistical-distribution\n\n"
         "Indicator performance as the rank correlation of an estimated statistic with distance to the transition, "
         "under controlled data degradation."),
        ("What The Math Says",
         "Simulate a pollination network that you know will collapse, then make its data worse in realistic ways — "
         "shorter, coarser, noisier, with some species unobserved — and see which warning statistics still trend "
         "upward. No single statistic wins everywhere. Mutual information, the one information-theoretic measure "
         "tested, suffers most from noise. That is no surprise: for bell-shaped data it is just a transformed "
         "autocorrelation, but it costs much more data to estimate."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "statistical-distribution", "D-sensitive"),
))
anchor("EWS8", "10.1038/s41598-021-87839-y",
       "Weinans, Quax, van Nes & van de Leemput 2021 - Evaluating the performance of multivariate indicators of resilience loss (Sci. Rep. 11:9148)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 (PMC8080839): model versions, six scenarios, Kendall tau scoring, "
       "abstract quote, MI = -1/2 log(1 - rho^2) (from the TeX source), MI conclusions. Figures not inspected. "
       "DOI verified on Crossref.",
       role="progenitor")
anchor("EWS8", "10.1103/PhysRevLett.103.238701",
       "Barnett, Barrett & Seth 2009 - Granger causality and transfer entropy are equivalent for Gaussian variables (PRL 103:238701)",
       "cites",
       "Cited for the linear-Gaussian equivalence F = 2T (Eq. 13), recorded in EWS8 at the parent session's request. Read "
       "2026-10-18 from arXiv:0910.4514v2 (Eqs. 8, 10-13 and the estimation caveat); version of record not read. "
       "DOI verified on Crossref.", confidence="medium")
tag("EWS8", "networks_systems.dynamical_systems", "primary", "benchmark of multivariate critical-slowing-down indicators")
tag("EWS8", "biology.ecology", "secondary", "plant-pollinator network model")
tag("EWS8", "information_theory.shannon", "secondary", "mutual-information indicator")
LINKS += [
    ("EWS8", "EWS7", "tests", "1.5",
     "Benchmarks explained variance, maximum covariance, MAF eigenvalue and degenerate fingerprinting under six data/system "
     "scenarios (Kendall tau); no indicator wins everywhere."),
    ("EWS8", "EWS1", "tests", "1.5",
     "Average autocorrelation and variance were among the best under short series; variance-based indicators held up under "
     "reduced resolution where autocorrelation-based ones failed."),
    ("EWS8", "INFO4", "tests", "2",
     "Lag-1 mutual information as a warning indicator: for Gaussian data MI = -1/2 log(1 - rho^2), a function of "
     "autocorrelation; it was the indicator most affected by measurement noise."),
]

# ===========================================================================
# EWS9 — Deep-learning EWS (Bury et al. 2021)
# Read: full text (PMC8488604); AUC values are in figures, not inspected.
# ===========================================================================
_t = ["deep learning", "CNN-LSTM", "normal forms", "fold bifurcation", "Hopf bifurcation", "transcritical bifurcation",
      "ROC curve", "AUC", "null time series", "thermoacoustic instability", "paleoclimate", "sapropel anoxia"]
ENTRIES.append(dict(
    id="EWS9", title="EWS9: Deep-Learning Early-Warning Signals Benchmarked by ROC (Bury et al. 2021)",
    filename="EWS9_deep_learning_ews.md",
    scale="cross-scale", domain="computer science · networks · earth sciences", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Bury, Sujith, Pavithran, Scheffer, Lenton, Anand & Bauch (2021, *PNAS* 118:e2106140118) train a CNN-LSTM "
         "classifier on simulated pre-transition series from randomly generated two-dimensional polynomial models "
         "passing through fold, Hopf or transcritical bifurcations, plus neutral (no-transition) series. There are two "
         "training sets: 500,000 series of length 500 and 200,000 of length 1,500. The classifier outputs a "
         "probability for each of the four outcomes, so it also predicts the type of bifurcation ahead.\n\n"
         "Out-of-sample tests used three model systems (a harvesting fold model, a consumer–resource model with Hopf "
         "and transcritical bifurcations, a five-variable disease–vaccine-opinion model) and three empirical datasets "
         "(paleoclimate transitions, thermoacoustic instability in a Rijke tube, sediment records of Mediterranean "
         "anoxia), each previously argued to show slowing down before a transition. ROC curves for predicting any "
         "transition were compared with lag-1 autocorrelation and variance across eight comparisons, using the last "
         "20% of each pre-transition series (the fourth quintile is in the SI). The classifier \"strongly outperforms\" "
         "the classical indicators in six. On paleoclimate it performs about as well as lag-1 autocorrelation (both "
         "beat variance). In the epidemic variable of the disease model all three are little better than random. The "
         "abstract counts 268 empirical and model series.\n\n"
         "SCOPE: trained and tested only on local bifurcations (critical slowing down present). It is not "
         "information-theoretic. A published comment, Dablander & Bury 2022 (*PNAS* 119, \"Deep learning for tipping "
         "points: Preprocessing matters\"), concerns preprocessing; it was not read. Code and the thermoacoustic data "
         "are on GitHub (ThomasMBury/deep-early-warnings-pnas); the geochemical and paleoclimate data are in public "
         "repositories (PANGAEA; NOAA World Data Center). So the test set is reproducible, but it is assembled from "
         "several sources, not a single packaged benchmark. Single study: contested until reproduced."),
        ("Mathematical Form",
         "Normal forms (Bury et al. 2021, Eqs. 1–3; bifurcation at μ = 0):\n"
         "  fold:          ẋ = μ − x²\n"
         "  Hopf:          ẋ = μx − y − x(x² + y²),   ẏ = x + μy − y(x² + y²)\n"
         "  transcritical: ẋ = μx − x²\n"
         "Training models: two-dimensional systems with third-order polynomial right-hand sides\n"
         "Classifier output: P(fold), P(Hopf), P(transcritical), P(neutral) for a series\n"
         "Score: ROC / AUC for 'any transition' vs neutral; for lag-1 AC and variance the discrimination threshold is "
         "the Kendall τ of the indicator trend (after Lowess detrending), for the classifier its probability"),
        ("Constraint Category",
         "Informatic (In): a learned classifier whose performance is stated as sensitivity and specificity against "
         "null series."),
        ("DS Cross-References",
         "EWS1 (the baselines: lag-1 autocorrelation and variance). EWS4 (the call for error rates this design "
         "answers). EWS3 (non-local and noise- or rate-induced transitions are outside its training). EWS8 (a "
         "trend-strength benchmark, for contrast)."),
        ("Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "Classification of a pre-transition time series by the normal form of the bifurcation it approaches."),
        ("What The Math Says",
         "Near a tipping point many different systems behave like a handful of simple textbook equations. So train a "
         "neural network on hundreds of thousands of simulated series from those equations and ask it, for a new "
         "series, whether a transition is coming and of which kind. Scored the way a medical test is scored — hits "
         "against false alarms on series where nothing happens — it beat rising autocorrelation and variance in six "
         "of eight comparisons and tied in the others. It is a pattern recogniser for critical slowing down, not a "
         "new signal."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "threshold-transition", "D-invariant"),
))
anchor("EWS9", "10.1073/pnas.2106140118",
       "Bury et al. 2021 - Deep learning for early warning signals of tipping points (PNAS 118:e2106140118)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 (PMC8488604): training sets, test systems, ROC comparison text "
       "('strongly outperforms ... in six'), data availability. AUC values are in Fig. 2 and were not read; SI not read. "
       "The Dablander & Bury 2022 comment is named from the PMC header only. DOI verified on Crossref.",
       role="progenitor")
tag("EWS9", "computer_science.ml", "primary", "deep-learning classifier for early warning")
tag("EWS9", "networks_systems.dynamical_systems", "secondary", "bifurcation normal forms as training data")
tag("EWS9", "earth_sciences.climate", "secondary", "paleoclimate and sediment test data")
LINKS += [
    ("EWS9", "EWS1", "tests", "1.5",
     "ROC comparison against lag-1 autocorrelation and variance on six systems: the classifier was better in 6 of 8 "
     "comparisons, comparable in the other 2."),
    ("EWS9", "EWS4", "tests", "2",
     "Reports sensitivity/specificity against null (no-transition) series, the evaluation Boettiger & Hastings 2012 called for."),
]

# ===========================================================================
# EWS10 — Spatial permutation entropy (Tirabassi & Masoller 2023)
# Read: full text (PMC9910486); SI (power analysis) not read.
# ===========================================================================
_t = ["permutation entropy", "ordinal patterns", "spatial early warning", "Moran's I", "spatial correlation",
      "vegetation tipping", "forest-savanna transition", "semiarid ecosystems", "MODIS tree cover", "Serengeti-Mara"]
ENTRIES.append(dict(
    id="EWS10", title="EWS10: Spatial Permutation Entropy as an Early-Warning Indicator (Tirabassi & Masoller 2023)",
    filename="EWS10_spatial_permutation_entropy.md",
    scale="cross-scale", domain="information · biology · earth sciences", status="contested", confidence="Tier 2 †",
    sections=[
        ("What It Claims",
         "Tirabassi & Masoller (2023, *PNAS* 120:e2215667120; published online 2022) compute permutation entropy (PE) "
         "from the probabilities of two-dimensional ordinal patterns in a spatial vegetation field, and compare it "
         "with spatial correlation (Moran's I) as an indicator of an approaching transition to an arid state. A "
         "spatial indicator needs no time series. Data: a high-resolution binarised Serengeti–Mara transect (30 m), "
         "six MODIS tree-cover transects (250 m) in Central Africa and South America showing bistability, and two "
         "vegetation models (LPF, LFCA).\n\n"
         "In both models PE decreases before the transition to desert while spatial correlation increases. In the "
         "satellite transects PE reaches a minimum at or near the start of the bistability region in five of the six "
         "transects. For the arid-to-vegetated direction both indicators behave inconsistently across transects. "
         "Their power analysis (in the SI, not read) finds PE outperforms spatial correlation for the LFCA model and "
         "the transects and underperforms for the LPF model. In the abstract's words, performance \"can be better, "
         "similar or worse than the spatial correlation\", and they propose PE as an additional indicator.\n\n"
         "SCOPE: spatial snapshots along a rainfall gradient (space-for-time), not a forecast in time. Single study: "
         "contested until reproduced."),
        ("Mathematical Form",
         "Permutation entropy of ordinal patterns π with empirical probabilities p(π):\n"
         "  PE = −Σ_π p(π) log p(π)   (Shannon entropy of the pattern distribution; here 2D patterns in a spatial field)\n"
         "Reference indicator: Moran's I spatial autocorrelation of the field u_ij"),
        ("Constraint Category",
         "Informatic (In): an entropy of local spatial order patterns, proposed as a complement to spatial "
         "correlation."),
        ("DS Cross-References",
         "INFO1 (Shannon Entropy — PE is the Shannon entropy of the ordinal-pattern distribution). EWS1 (spatial "
         "correlation is the spatial analogue of rising autocorrelation). EWS8, EWS9 (other comparisons with "
         "classical indicators)."),
        ("Mathematical Archetype",
         "Mathematical archetype: statistical-distribution\n\n"
         "An entropy of the distribution of local ordinal patterns, tracked along a driver gradient."),
        ("What The Math Says",
         "Look at a satellite map of tree cover and slide a small square over it. At each position, record only the "
         "ranking of the pixel values — which is highest, which is lowest — and count how often each ranking pattern "
         "appears. The entropy of those counts is the permutation entropy. Moving along a rainfall gradient towards "
         "the point where forest gives way to grassland, this entropy tends to fall to a minimum before the switch, "
         "while ordinary spatial correlation rises. Sometimes it is the better warning, sometimes the worse."),
        ("Concept Tags", bullets(_t)),
    ],
    properties=facets("In", _t, "statistical-distribution", "D-sensitive"),
))
anchor("EWS10", "10.1073/pnas.2215667120",
       "Tirabassi & Masoller 2023 - Entropy-based early detection of critical transitions in spatial vegetation fields (PNAS 120:e2215667120)",
       "canonical_authority",
       "Primary source. Full text read 2026-10-18 (PMC9910486): data, model results, 'five of the six transects' minimum, "
       "power-comparison sentence, abstract quote. The SI power analysis was not read. Crossref issued year 2022 (online); "
       "print volume 120 (2023). DOI verified on Crossref.",
       role="progenitor")
tag("EWS10", "information_theory.shannon", "primary", "permutation (ordinal-pattern) entropy")
tag("EWS10", "biology.ecology", "secondary", "vegetation tipping in semiarid ecosystems")
tag("EWS10", "earth_sciences.climate", "secondary", "rainfall-driven forest-savanna transitions")
LINKS += [
    ("EWS10", "INFO1", "derives from", "2",
     "Permutation entropy is the Shannon entropy of the empirical distribution of ordinal patterns."),
    ("EWS10", "EWS1", "tests", "2",
     "Compares spatial permutation entropy with spatial correlation (Moran's I), the spatial form of the slowing-down "
     "signal: better, similar or worse depending on system and data."),
]
