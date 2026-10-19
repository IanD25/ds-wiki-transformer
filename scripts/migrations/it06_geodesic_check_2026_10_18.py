"""
IT06 geodesic check — 2026-10-18 (audit_ref gsw-it06-geodesic-check-2026-10-18). Mode A: corrections
only, no promotions.

WHY
---
The QR-004 corrections pass left IT06 out (docs/prior_art_reviews/QR004_CORRECTIONS_2026_10_18.md §4).
IT06 says minimum-dissipation paths are geodesics of the Fisher-Rao metric. Sivak & Crooks 2012 (read in
full) derive a friction-tensor metric zeta = k_BT tau∘I for slow driving; it is Fisher-Rao (times a
constant) only for constant relaxation time (Crooks 2007, read in full; Salamon & Berry 1983 via Deffner &
Bonança 2020). IT06 also writes Jarzynski and Crooks as the s_tot IFT with a substitution (both need
equilibrium starts and use the dissipated work; Seifert 2012 §§3.2, 4.3) and calls the IFT a proof of the
second law (Seifert 2012 §3.3.1 says it is not). X8, P21, BR04 and seven link descriptions lean on the
geodesic sentence. The Fisher-gravity chain does not. Pattern tags: vocabulary-stacking-analogy,
over-extension-beyond-formula-range. Proposed wording and reading record:
docs/prior_art_reviews/IT06_GEODESIC_CHECK_2026_10_18.md (items 1-21; item 22 is a docs banner).

WHAT THIS DOES
--------------
1. sections: dated CORRECTION banners appended after the wrong text, which stays unchanged.
2. conjectures.claim (P21): one banner appended.
3. links: descriptions prefixed "[Corrected 2026-10-18, <ref>] <new>. Previously: "<old>"". Types and
   endpoints unchanged.
4. wiki_history.db: one append-only calibration row for P21 (label unchanged: Established).

SAFETY
------
Dry run by default; --apply writes. Each (table, row, column) target gets exactly one composed write; a
duplicate target aborts. A target that already carries all its banners is skipped; one that carries the
audit_ref but not all its banners aborts as partially applied. Every check string (an exact quote of the
wrong text) must occur exactly once in a pending target. Post-write read-back verifies every value.

Run:  python3 scripts/migrations/it06_geodesic_check_2026_10_18.py
      python3 scripts/migrations/it06_geodesic_check_2026_10_18.py --apply
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-it06-geodesic-check-2026-10-18"
D = "2026-10-18"
REPORT = "docs/prior_art_reviews/IT06_GEODESIC_CHECK_2026_10_18.md"
LINK_PREFIX = f"[Corrected {D}, {AUDIT_REF}] "


def banner(body, tail="The text above is unchanged."):
    return f"\n\n> **CORRECTION {D} (`{AUDIT_REF}`).** {body} *{tail}*"


# Shared wording
FRICTION = ("In slow driving near equilibrium the mean excess work is W_ex ≈ ∫ λ̇ᵀ ζ(λ) λ̇ dt, where "
            "ζ_ij = β∫₀^∞⟨δX_j(0)δX_i(t)⟩_λ dt is the friction tensor, a Riemannian metric on control-parameter "
            "space; minimum-excess-work protocols are its geodesics, run at constant excess power (Sivak & Crooks "
            "2012, PRL 108:190602, Eqs. 12–13, p. 3). In general ζ is not the Fisher–Rao metric: ζ = k_BT τ∘I, the "
            "entry-by-entry product of an integral relaxation-time matrix and the Fisher information of the "
            "equilibrium family (Eq. 14). It reduces to the Fisher metric times a constant only when the relaxation "
            "time does not vary along the path (p. 4; for several parameters, one relaxation time common to all).")
JAR_CROOKS = ("Jarzynski and Crooks are not the Δs_tot fluctuation theorem with a substitution. All three are "
              "cases of one master identity ⟨e^{−R}⟩ = 1 whose R depends on the chosen end distribution (Seifert "
              "2012, Rep. Prog. Phys. 75:126001, Eq. 80): with the actual final distribution R = Δs_tot; with an "
              "equilibrium start at λ₀ and the equilibrium distribution at λ_t as reference, R = β(W − ΔF), the "
              "dissipated work. Jarzynski requires that equilibrium start (§3.2.1); Crooks, p̃(−W)/p(W) = "
              "e^{−β(W−ΔF)}, also requires the reverse process to start in equilibrium at λ_t (§3.2.3, Eq. 61). "
              "A detailed theorem for Δs_tot itself holds in a non-equilibrium steady state (Eq. 65), not in "
              "general. β(W − ΔF) equals Δs_tot only if the system has also relaxed to equilibrium at the end.")
P21_NOT_TESTED = ("η measures how straight a path is on the SPD manifold. P21, now Established only as "
                  "Chentsov's uniqueness theorem, makes no prediction about market paths, so these results neither "
                  "support nor contradict P21.")

# ─────────────────────────────────────────────────────────────────────────────
# Section banners — (entry_id, section_name) -> (check strings, banners)
# ─────────────────────────────────────────────────────────────────────────────
SECTION_OPS = {}


def sec(eid, name, checks, banners):
    key = (eid, name)
    if key in SECTION_OPS:
        raise SystemExit(f"ABORT — duplicate section target {key}")
    SECTION_OPS[key] = dict(checks=list(checks), banners=list(banners))


# 1. IT06 What It Claims
sec("IT06", "What It Claims",
    checks=["the Jarzynski equality and Crooks fluctuation theorem follow as special cases by setting s_tot = β(W − ΔF)",
            "This is the information-theoretic proof of the second law",
            "minimum-dissipation paths between thermodynamic states are geodesics on the Fisher-Rao manifold of "
            "probability distributions"],
    banners=[banner(
        "Three corrections. (a) The fluctuation theorem for Δs_tot holds for Markovian (Langevin or master-equation) "
        "dynamics, any initial distribution, driving and duration; its thermodynamic reading assumes the noise is "
        "not affected by the driving (Seifert 2012 §3.2.1, §3.3.1, Eq. 64). " + JAR_CROOKS + " (b) Within "
        "stochastic dynamics ⟨Δs_tot⟩ = D_KL(P_F‖P_R) ≥ 0 restates the second law as distinguishability of forward "
        "and reverse paths. It is not an independent proof: the irreversibility is built in through the "
        "stochastic dynamics (Seifert 2012 §3.3.1). (c) " + FRICTION + " That is the setting of the classical "
        "thermodynamic-length results: Salamon & Berry 1983 (endoreversible, mean relaxation time) and Crooks 2007 "
        "(PRL 99:100602; stepwise protocols with re-equilibration after each step). Even then the manifold is the "
        "family of equilibrium states indexed by the control parameters, not the space of all distributions. "
        "Outside linear response, exact optimal protocols jump at the start and end (Schmiedl & Seifert 2007; "
        "Seifert 2012 §7.1), which the geodesic picture misses. Seifert's 2012 review does not itself state the "
        "geodesic result.")])

# 2. IT06 Mathematical Form
sec("IT06", "Mathematical Form",
    checks=["Jarzynski:  s_tot = β(W − ΔF)", "Crooks:     P_F(s_tot = a) / P_R(s_tot = −a) = e^a",
            "where g_ij = Fisher-Rao metric on parameter space",
            "Equality: minimum-dissipation path is a geodesic on Fisher-Rao manifold"],
    banners=[banner(
        "Jarzynski (equilibrium start at λ₀): ⟨e^{−β(W−ΔF)}⟩ = 1, the master fluctuation theorem with "
        "R = β(W − ΔF), a different functional from Δs_tot (Seifert 2012 Eqs. 58–59, 80). Crooks (forward process "
        "starts in equilibrium at λ₀, reverse at λ_t): p̃(−W)/p(W) = e^{−β(W−ΔF)} (Eq. 61); a detailed theorem "
        "for Δs_tot holds in a steady state (Eq. 65), not in general. Thermodynamic geometry (slow driving, linear "
        "response): W_ex ≈ ∫₀^Δt λ̇ᵀ ζ(λ) λ̇ dt (no 1/τ prefactor when written with dλ/dt), ζ = k_BT τ∘I the "
        "friction tensor, L = ∫₀^Δt √(λ̇ᵀζλ̇) dt, and W_ex ≥ L²/Δt with equality only at constant excess power, "
        "i.e. a geodesic of ζ (Sivak & Crooks 2012, Eqs. 13–14, p. 3). W_ex is excess work; it equals dissipation "
        "once the system re-equilibrates at the end. Fisher special case (constant relaxation time τ_R): "
        "ζ = k_BT τ_R I, so W_ex ≥ k_BT τ_R L_I²/Δt with L_I the Fisher (thermodynamic) length. Stepwise form "
        "(N steps, re-equilibration after each; Crooks 2007 Eqs. 9–13): forward-plus-reverse hysteresis ≈ J/N ≥ "
        "L_I²/N in units of k_B; one direction about half that. Salamon & Berry 1983 (endoreversible): "
        "ΔE ≥ ε̄ℓ²/τ, Weinhold metric, ε̄ a mean lag time (via Deffner & Bonança 2020, EPL, Eq. 7).")])

# 3. IT06 Constraint Category
sec("IT06", "Constraint Category",
    checks=["all are consequences of D_KL ≥ 0 instantiated in different physical settings",
            "dissipation is minimised by following geodesics on the Fisher-Rao manifold"],
    banners=[banner(
        "D_KL ≥ 0 gives the mean inequalities (⟨Δs_tot⟩ ≥ 0, ⟨W⟩ ≥ ΔF). The Jarzynski and Crooks equalities are not "
        "consequences of D_KL ≥ 0; they come from the master identity ⟨e^{−R}⟩ = 1 (path-probability "
        "normalisation) with equilibrium initial states (Seifert 2012 §§3.2, 4.3). In slow driving, excess work is "
        "minimised along geodesics of the friction tensor ζ = k_BT τ∘I, which are Fisher–Rao (IT08) geodesics only "
        "when the relaxation time is constant (Sivak & Crooks 2012, Eq. 14, p. 4).")])

# 4. IT06 DS Cross-References
sec("IT06", "DS Cross-References",
    checks=["by setting s_tot = β(W − ΔF)", "⟨W_diss⟩ = D_KL(P_F||P_R) × k_BT",
            "detailed fluctuation symmetry P_F(a)/P_R(−a) = e^a",
            "minimum-dissipation non-equilibrium processes are geodesics on the Fisher-Rao manifold"],
    banners=[banner(
        "NE03: Jarzynski is the master fluctuation theorem with R = β(W − ΔF) for an equilibrium initial state; "
        "⟨W⟩ − ΔF = k_BT·D_KL(P_F‖P_R) holds when forward and reverse processes both start in equilibrium "
        "(Kawai, Parrondo & Van den Broeck 2007; Seifert 2012 §7.2, Eqs. 147–148). NE04: Crooks is a detailed "
        "theorem for the work, p̃(−W)/p(W) = e^{−β(W−ΔF)}, with equilibrium starts for both processes (Seifert "
        "2012 Eq. 61); the symmetry for Δs_tot holds in a steady state (Eq. 65). IT08: slow-driving optimal "
        "protocols are geodesics of the friction tensor ζ = k_BT τ∘I, which coincide with Fisher–Rao geodesics of "
        "the equilibrium family only for constant relaxation time (Sivak & Crooks 2012; Crooks 2007).")])

# 5. IT06 Mathematical Archetype
sec("IT06", "Mathematical Archetype",
    checks=["entropy production measures deviation from the geodesic path through the space of probability "
            "distributions"],
    banners=[banner(
        "Entropy production does not measure deviation from a geodesic: even an optimal (geodesic, constant-power) "
        "protocol produces W_ex = L²/Δt > 0, which vanishes only as Δt → ∞. The geometric layer is the "
        "slow-driving friction-tensor metric (Sivak & Crooks 2012), Fisher–Rao only for constant relaxation time.")])

# 6. IT06 What The Math Says
sec("IT06", "What The Math Says",
    checks=["Setting s_tot = β(W − ΔF) recovers the Jarzynski equality",
            "gives the Crooks relation P_F(a)/P_R(−a) = e^a",
            "The minimum-dissipation result follows from the Cramér-Rao bound applied to the Fisher-Rao metric"],
    banners=[banner(
        "Jarzynski and Crooks need equilibrium initial states and use the dissipated work β(W − ΔF), not Δs_tot "
        "(see What It Claims). The minimum-dissipation result does not come from the Cramér–Rao bound. It comes "
        "from linear response (excess power is a quadratic form λ̇ᵀζλ̇) plus the Cauchy–Schwarz inequality, which "
        "gives W_ex ≥ L²/Δt with equality at constant excess power (Sivak & Crooks 2012, p. 3; Crooks 2007, Eq. 9). "
        "It is a lower bound, reached by the geodesic of the friction tensor ζ, which is Fisher–Rao only for "
        "constant relaxation time.")])

# 7. IT06 Concept Tags
sec("IT06", "Concept Tags",
    checks=["• Fisher-Rao metric and minimum dissipation"],
    banners=[banner(
        "Read 'Fisher-Rao metric and minimum dissipation' as 'thermodynamic (friction-tensor) metric and minimum "
        "excess work in slow driving'; the metric is Fisher–Rao only for constant relaxation time (Sivak & Crooks "
        "2012).", tail="The tags above are unchanged.")])

# 13 + 14. X8 Geodesic Test
sec("X8", "Geodesic Test",
    checks=["instance of Seifert's minimum-dissipation result (IT06)",
            "(Seifert's bound: ⟨W_diss⟩ ≥ d_geodesic²/τ)",
            "P21 conditional (fast-shock limit): SUPPORTED.",
            "This is the adiabatic limit in thermodynamics.",
            "P21 irreversibility: CONFIRMED."],
    banners=[
        banner(
            "Test design. The bound is not Seifert's, and it does not apply here as written. The source form is "
            "W_ex ≥ L²/Δt (Sivak & Crooks 2012, p. 3), with L the length in the friction-tensor metric ζ = k_BT τ∘I, "
            "in units of √(energy × time). The Fisher form, W_ex ≥ k_BT τ_R L_I²/Δt, needs a constant relaxation time "
            "τ_R (p. 4); the endoreversible form is ΔE ≥ ε̄ℓ²/τ (Salamon & Berry 1983). Four mismatches. (1) Metric: "
            "the affine-invariant SPD distance is the Fisher–Rao distance of zero-mean Gaussians, not a friction "
            "metric, and has no relaxation-time factor. (2) Units: Σ = ∫v²/D_eff dt has units of D_eff per time, "
            "d_geo²/τ has units of 1/time, and the source bound is a work; nothing fixes the conversion. (3) Regime: "
            "the bound is a slow-driving result, valid when the protocol changes slower than the system relaxes "
            "(Sivak & Crooks, before Eq. 11); the fast episodes called near-geodesic below (duration < τ_relax) are "
            "where it does not hold. (4) Setting: a market has no externally driven control parameter and no "
            "equilibrium Gibbs family. Test 3 computed only η = d_geo/L_actual, never step 2, so no reported number "
            "depends on this bound. Note (Established, a mathematical identity): σ = v²/D_eff = (d(2√D_eff)/dt)², so "
            "by Cauchy–Schwarz, for any path, Σ ≥ 4(√D_end − √D_start)²/τ, with equality when √D_eff changes at a "
            "constant rate. This is the thermodynamic-length inequality for X8's own one-dimensional quadratic form; "
            "it follows from the proxy's definition and carries no thermodynamic content."),
        banner(
            "Test 3 interpretation. " + P21_NOT_TESTED + " η ≈ 0.50 is below the near-geodesic threshold of 0.8 in "
            "the project's own spec (docs/ALPHAENTROPY_GEODESIC_TEST_SPEC.md). Fast driving relative to relaxation "
            "is the far-from-quasi-static regime, where excess work is largest (W_ex ∝ 1/Δt), not a "
            "minimum-dissipation limit. The descent/recovery asymmetry (1.75×) is an empirical asymmetry in path "
            "straightness; no path probabilities were computed, so it is not a measurement of P_F ≠ P_R. The η "
            "values themselves stand."),
    ])

# 15. X8 DS Connections (banner after the table)
sec("X8", "DS Connections",
    checks=["If crisis paths minimize Σ, they are Fisher-Rao geodesics — key test for P21"],
    banners=[banner(
        "Geodesic-test row: Σ depends only on the scalar D_eff(t). Its minimisers at fixed duration are paths along "
        "which √D_eff changes at a constant rate (see Geodesic Test), so minimising Σ cannot select a geodesic on "
        "the SPD manifold. The test does not bear on P21.", tail="The table above is unchanged.")])

# 16. X8 Three Crisis Archetypes
sec("X8", "Three Crisis Archetypes",
    checks=["The thermodynamic analog is exact:",
            "Is optimal filtering inherently selecting the Fisher-Rao relaxation scale?"],
    banners=[banner(
        "The analogy holds in name only. In thermodynamics 'adiabatic' means no heat exchange; in the "
        "thermodynamic-length and slow-driving literature the near-reversible limit is slow driving relative to "
        "relaxation (Sivak & Crooks 2012; Deffner & Bonança 2020), so the 'adiabatic' (fast) regime here is the "
        "opposite of that limit. The Fisher metric contains no time scale; relaxation times enter only through the "
        "friction tensor ζ = k_BT τ∘I (Sivak & Crooks 2012, Eq. 14), so there is no 'Fisher–Rao relaxation scale' "
        "for the EWMA filter to select. The empirical scaling of η with duration/τ_relax stands as an observation "
        "about the estimator.")])

# 17. X8 Thermodynamic Connections
sec("X8", "Thermodynamic Connections",
    checks=["The proxy σ(t) = v²/D_eff is an", "approximation that captures the qualitative behavior"],
    banners=[banner(
        "IT06 paragraph: unverified. No derivation or test shows that Σ approximates D_KL(P_F‖P_R) of any model of "
        "returns (Overview: 'This has not been done'). Treat Σ as an analogy-motivated proxy only.")])

# 21. BR04
_BR04 = ("Geodesics of the Ruppeiner/Weinhold metric minimise dissipated availability only for slow, endoreversible "
         "processes with a given mean relaxation time (Salamon & Berry 1983, ΔE ≥ ε̄ℓ²/τ). For slow driving in "
         "general the optimal paths are geodesics of the friction tensor ζ = k_BT τ∘I, which is this metric times a "
         "constant only when the relaxation time is constant (Sivak & Crooks 2012).")
sec("BR04", "Constraint Category", checks=["the geodesics (optimal thermodynamic paths)"], banners=[banner(_BR04)])
sec("BR04", "Mathematical Archetype", checks=["geodesics are the most efficient thermodynamic processes"],
    banners=[banner(_BR04)])

# ─────────────────────────────────────────────────────────────────────────────
# 20. P21 — conjectures.claim
# ─────────────────────────────────────────────────────────────────────────────
CONJ_OPS = {
    "P21": dict(
        checks=["(4) non-equilibrium thermodynamics, where minimum-dissipation paths between states are geodesics on "
                "the Fisher-Rao manifold",
                "These are correctly covered by Chentsov uniqueness",
                "P21 holds conditionally in the fast-shock limit"],
        banners=[banner(
            "Instance (4) is mis-stated. The metric governing slow-driving dissipation is the friction tensor "
            "ζ = k_BT τ∘I (Sivak & Crooks 2012, PRL 108:190602, Eq. 14). It depends on the dynamics through the "
            "relaxation times, so Chentsov's theorem, which is about invariance under sufficient statistics, does "
            "not single it out. It equals the Fisher–Rao metric of the equilibrium family times a constant only for "
            "constant relaxation time (p. 4; Crooks 2007). Instance (4) is therefore withdrawn from the list of "
            "instances Chentsov covers; at most it is a special case of instance (1). The financial-market "
            "paragraphs do not test P21 (see X8 corrections). Label unchanged: Established, for the classical "
            "theorem only. Report: " + REPORT + ".")]),
}

# ─────────────────────────────────────────────────────────────────────────────
# Links — (id, source, target, must-contain, new text)
# ─────────────────────────────────────────────────────────────────────────────
LINK_FIXES = [
    (820, "IT06", "NE03", "by setting s_tot = β(W - ΔF)",
     "Jarzynski is a sister case of the same master fluctuation identity, with R = β(W − ΔF) and an equilibrium "
     "initial state (Seifert 2012 Eqs. 58–59, 80); IT06 is the general framework."),
    (821, "IT06", "NE04", "P_F(a)/P_R(-a) = e^a",
     "Crooks is the detailed fluctuation theorem for work, p̃(−W)/p(W) = e^{−β(W−ΔF)}, with forward and reverse "
     "processes started in equilibrium (Seifert 2012 Eq. 61); it is a special case of IT06's master identity."),
    (822, "IT06", "IT08", "geodesics on the Fisher-Rao manifold",
     "In slow driving, minimum-excess-work protocols are geodesics of the friction tensor ζ = k_BT τ∘I (Sivak & "
     "Crooks 2012). This equals the Fisher–Rao metric of the equilibrium family (IT08) times a constant only when "
     "the relaxation time is constant (Crooks 2007; Salamon & Berry 1983)."),
    (832, "IT06", "FL1", "with no physical assumptions",
     "The identity ⟨e^{−R}⟩ = 1 follows from normalisation of path probabilities. Reading R as entropy production "
     "needs physical assumptions: Markovian stochastic dynamics with the noise unaffected by the driving (Seifert "
     "2012 §3.2.1, §3.3.1)."),
    (977, "NE09", "IT06", "under separate review",
     "A core result of stochastic thermodynamics. (IT06's Fisher–Rao geodesic sentence was corrected 2026-10-18 "
     "under gsw-it06-geodesic-check-2026-10-18: the slow-driving metric is the friction tensor.)"),
    (825, "X8", "IT06", "approximates Seifert's D_KL",
     "Analogy only: Σ = ∫σ dt is not derived from path probabilities and is not shown to approximate Seifert's "
     "D_KL(P_F‖P_R) (X8 Overview)."),
    (828, "X8", "P21", "Σ_actual vs d_geodesic²/τ",
     "The geodesic test does not test P21. The 'Seifert bound' it used is mis-stated (see X8 Geodesic Test "
     "correction), and P21 is Established only as Chentsov's theorem, which predicts nothing about market paths. "
     "Test 3's η is a path-straightness measure."),
]

# ─────────────────────────────────────────────────────────────────────────────
# Calibration — append-only, label unchanged
# ─────────────────────────────────────────────────────────────────────────────
CALIBRATIONS = [(
    "P21", "conjecture", "Established", D, AUDIT_REF,
    "Classical Chentsov uniqueness + quantum Petz classification (unchanged); instance (4) withdrawn — slow-driving "
    "dissipation metric is the friction tensor (Sivak & Crooks 2012), Fisher–Rao only for constant relaxation time "
    "[vocabulary-stacking-analogy; over-extension-beyond-formula-range]",
    "IT06 geodesic check (owner-approved). Sivak & Crooks 2012 (PRL 108:190602, read in full): for slow driving the "
    "excess work is set by the friction tensor zeta = k_BT tau∘I (Eq. 14), whose geodesics are the "
    "minimum-excess-work protocols; it reduces to the Fisher information metric only when the relaxation time does "
    "not vary (p. 4), the setting of Salamon & Berry 1983 and Crooks 2007 (PRL 99:100602, read in full). The friction "
    "tensor depends on the dynamics, so Chentsov's theorem does not cover instance (4); the 2026-05-04 addendum's "
    "statement that it does is withdrawn. The X8 financial geodesic test does not test P21. Label unchanged: "
    "Established for the classical theorem only. Report: " + REPORT + "."),
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
    for cid in CONJ_OPS:
        once(("conjectures", cid, "claim"))
    for (lid, *_rest) in LINK_FIXES:
        once(("links", lid, "description"))


def plan_text(content, op, label):
    """Return new content, or None if already applied. Abort on partial state."""
    present = [b in content for b in op["banners"]]
    if all(present):
        return None
    if any(present) or AUDIT_REF in content:
        raise SystemExit(f"[{label}] ABORT — partially applied")
    for chk in op["checks"]:
        n = content.count(chk)
        if n != 1:
            raise SystemExit(f"[{label}] FAIL — check string count {n}: {chk[:70]!r}")
    return content + "".join(op["banners"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")
    check_targets()

    print("=" * 72); print("PHASE 1 — validation / dry run"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    sec_ops, conj_ops, link_ops, skipped = [], [], [], 0
    for (eid, name), op in SECTION_OPS.items():
        rows = cur.execute("SELECT id, content FROM sections WHERE entry_id=? AND section_name=?", (eid, name)).fetchall()
        if len(rows) != 1:
            raise SystemExit(f"[{eid}.{name}] ABORT — {len(rows)} sections found")
        new = plan_text(rows[0][1], op, f"{eid}.{name}")
        if new is None:
            skipped += 1; continue
        sec_ops.append((rows[0][0], f"{eid}.{name}", new))
        print(f"  [{eid}.{name}] plan — {len(op['banners'])} banner(s), {len(rows[0][1])} → {len(new)} chars")
    for cid, op in CONJ_OPS.items():
        row = cur.execute("SELECT claim FROM conjectures WHERE id=?", (cid,)).fetchone()
        if row is None:
            raise SystemExit(f"[{cid}.claim] ABORT — conjecture not found")
        new = plan_text(row[0], op, f"{cid}.claim")
        if new is None:
            skipped += 1; continue
        conj_ops.append((cid, new))
        print(f"  [{cid}.claim] plan — {len(op['banners'])} banner(s), {len(row[0])} → {len(new)} chars")
    for lid, s, t, must, new_text in LINK_FIXES:
        row = cur.execute("SELECT source_id, target_id, description FROM links WHERE id=?", (lid,)).fetchone()
        if row is None or (row[0], row[1]) != (s, t):
            raise SystemExit(f"[links {lid}] ABORT — unexpected row {row!r}")
        desc = row[2]
        if desc.startswith(LINK_PREFIX):
            skipped += 1; continue
        if AUDIT_REF in desc:
            raise SystemExit(f"[links {lid}] ABORT — audit_ref present without prefix")
        if desc.count(must) != 1:
            raise SystemExit(f"[links {lid}] FAIL — expected text count {desc.count(must)}: {must!r}")
        link_ops.append((lid, LINK_PREFIX + new_text + f' Previously: "{desc}"'))
        print(f"  [links {lid} {s}->{t}] plan")
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    pending_cal = [c for c in CALIBRATIONS if not hc.execute(
        "SELECT 1 FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
        (c[0], c[3], c[4])).fetchone()]
    hc.close()
    print(f"\n  {len(sec_ops)} section writes, {len(conj_ops)} conjecture writes, {len(link_ops)} link writes, "
          f"{len(pending_cal)} calibration rows; {skipped} targets already applied")

    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply."); return

    print("\n" + "=" * 72); print("PHASE 2 — apply"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    try:
        for sid, label, new in sec_ops:
            cur.execute("UPDATE sections SET content=? WHERE id=?", (new, sid))
            if cur.rowcount != 1: raise SystemExit(f"[{label}] rowcount {cur.rowcount}")
        for cid, new in conj_ops:
            cur.execute("UPDATE conjectures SET claim=? WHERE id=?", (new, cid))
            if cur.rowcount != 1: raise SystemExit(f"[{cid}] rowcount {cur.rowcount}")
        for lid, new in link_ops:
            cur.execute("UPDATE links SET description=? WHERE id=?", (new, lid))
            if cur.rowcount != 1: raise SystemExit(f"[links {lid}] rowcount {cur.rowcount}")
        conn.commit()
    except BaseException:
        conn.rollback(); conn.close(); raise
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for row in pending_cal:
        hc.execute("""INSERT OR IGNORE INTO confidence_calibration (entity_id, entity_type, confidence,
                      calibration_date, audit_ref, short_status, rationale) VALUES (?,?,?,?,?,?,?)""", row)
    hc.commit(); hc.close()
    print(f"  wrote {len(sec_ops)} sections, {len(conj_ops)} conjectures, {len(link_ops)} links, "
          f"{len(pending_cal)} calibration rows")

    print("\n" + "=" * 72); print("PHASE 3 — read-back verification"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    bad = [label for sid, label, new in sec_ops
           if cur.execute("SELECT content FROM sections WHERE id=?", (sid,)).fetchone()[0] != new]
    bad += [cid for cid, new in conj_ops
            if cur.execute("SELECT claim FROM conjectures WHERE id=?", (cid,)).fetchone()[0] != new]
    bad += [f"links:{lid}" for lid, new in link_ops
            if cur.execute("SELECT description FROM links WHERE id=?", (lid,)).fetchone()[0] != new]
    for (eid, name), op in SECTION_OPS.items():
        c = cur.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (eid, name)).fetchone()[0]
        if plan_text(c, op, f"{eid}.{name}") is not None:
            bad.append(f"not-applied:{eid}.{name}")
    for cid, op in CONJ_OPS.items():
        c = cur.execute("SELECT claim FROM conjectures WHERE id=?", (cid,)).fetchone()[0]
        if plan_text(c, op, f"{cid}.claim") is not None:
            bad.append(f"not-applied:{cid}.claim")
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for c in CALIBRATIONS:
        got = hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? "
                         "AND calibration_date=? AND audit_ref=?", (c[0], c[3], c[4])).fetchone()
        if got != (c[2], c[5]):
            bad.append(f"cal:{c[0]}")
    hc.close()
    if bad:
        raise SystemExit(f"Post-write drift: {bad}")
    print(f"  verified: {len(sec_ops)} sections, {len(conj_ops)} conjectures, {len(link_ops)} links, "
          f"{len(CALIBRATIONS)} calibration rows")


if __name__ == "__main__":
    main()
