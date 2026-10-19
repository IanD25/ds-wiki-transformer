"""
QR-004 corrections — 2026-10-18 (audit_ref gsw-qr004-corrections-2026-10-18). Mode A: corrections
only, no promotions.

WHY
---
The QR-004 literature map (docs/prior_art_reviews/QR-004_THERMO_LIMITS_LITERATURE_MAP_2026_10_18.md
§F) found 28 errors or needed qualifications. Most share one shape: Landauer's erasure bound applied
to operations that are not erasures (copying, encoding, spikes, comparisons, synchronisation) —
pattern tag `landauer-scope-overreach`. Each item was re-checked against the live text; the
load-bearing claims were checked against primary sources read in this session. Proposed wording,
reading record and the owner's decisions: docs/prior_art_reviews/QR004_CORRECTIONS_2026_10_18.md
(owner approved 2026-10-18: list C1-C28, groups A and B, treatment A2, TD3 facet, P15 row).
IT06 is deliberately left out (separate follow-up).

WHAT THIS DOES
--------------
1. sections: dated CORRECTION banners appended after the wrong text, which stays unchanged above
   them. Group A (boilerplate in 21 Mathematical Archetype sections, treatment A2): three phrases
   replaced in place, each paragraph marked; B5 alone carries the full original wording. INFO4:
   exact duplicate sentence and six duplicate concept-tag lines removed (hygiene, no content lost).
2. links / entry_connections: descriptions prefixed "[Corrected 2026-10-18, <ref>] <new>.
   Previously: "<old>"" (precedent consistency_pass_phase6_gt05). Types and endpoints unchanged.
3. entry_properties: dimensional_sensitivity D-sensitive -> D-invariant for B5, E2, TD3 (the
   original value is recorded in each entry's banner and here).
4. wiki_history.db: one append-only calibration row for P15 (label unchanged: Speculative).

SAFETY
------
Dry run by default; --apply writes. Every (table, row, column) target gets exactly one composed
write; a duplicate target aborts. Applied state is detected BEFORE find-strings are matched (the
B5 banner quotes the original boilerplate, so the find-strings legitimately reappear inside it):
banners are stripped first, then every find must be absent and every replacement present. A
partially applied target aborts. Pending targets need every find-string exactly once. Post-write
read-back verifies every value.

Run:  python3 scripts/migrations/qr004_corrections_2026_10_18.py
      python3 scripts/migrations/qr004_corrections_2026_10_18.py --apply
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-qr004-corrections-2026-10-18"
D = "2026-10-18"
REPORT = "docs/prior_art_reviews/QR004_CORRECTIONS_2026_10_18.md"
LINK_PREFIX = f"[Corrected {D}, {AUDIT_REF}] "


def banner(body, tail="The text above is unchanged."):
    return f"\n\n> **CORRECTION {D} (`{AUDIT_REF}`).** {body} *{tail}*"


B_TAIL = "The 'Dimensional sensitivity' line above is unchanged."


# ─────────────────────────────────────────────────────────────────────────────
# Group A — archetype boilerplate (21 entries), treatment A2
# ─────────────────────────────────────────────────────────────────────────────
A_ENTRIES = ["Ax1", "B5", "E2", "EM11", "ES6", "F1", "F2", "F5", "G3", "KC3", "KC5", "M1", "Q3", "Q5",
             "QM2", "T6", "T9", "TD3", "TD4", "TD8", "TD13"]
S1 = ("Thermodynamic bounds cannot be violated by any mechanism, no matter how clever, because they follow "
      "from entropy, energy conservation, and the statistics of distinguishable states.")
N1 = ("Second-law (mean) bounds such as Carnot and Landauer have no known violation once every reservoir, and any "
      "information the system holds, is counted. Fluctuation bounds such as the thermodynamic uncertainty relation "
      "hold only within stated model classes (continuous-time jump or overdamped dynamics in a steady state with "
      "time-independent driving) and have explicit counterexamples outside them: inertial dynamics, time-dependent "
      "driving, magnetic fields, quantum transport and discrete time (Horowitz & Gingrich 2020; Pietzonka 2022).")
S2 = ("The bound value itself is often D-sensitive: Carnot is D-invariant; Landauer and Heisenberg involve k_BT and ℏ, "
      "both acted on by Ω_D.")
N2 = ("Carnot and Landauer are D-invariant: Landauer's bound counts distinguishable states, not degrees of freedom, so "
      "it does not depend on spatial dimension (Landauer 1961). That Ω_D acts on k_B and ℏ is a DS-internal posit (see "
      "OmD, an internal construction), not part of these reference laws.")
S3 = "Ashby regulatory variety (V_controller ≥ V_system − V_channel)"
N3 = "Ashby regulatory variety (V_outcome ≥ V_disturbance − V_regulator)"


def a_marker(eid):
    where = "in the note below" if eid == "B5" else "in B5's Mathematical Archetype"
    return (f" *(Corrected {D}, `{AUDIT_REF}`: three phrases in this paragraph; original wording kept {where}.)*")


A_B5_BANNER = banner(
    "The thermodynamic-bound boilerplate paragraph above appears in 21 entries (" + ", ".join(A_ENTRIES) + "). "
    "Three phrases were corrected in place in all of them, and the original wording is kept here once. "
    f"(1) Was: \"{S1}\" Absolute 'no mechanism' holds for second-law mean bounds; fluctuation bounds such as the TUR "
    "have stated scopes and known counterexamples (Horowitz & Gingrich 2020, Nat. Phys. 16:15; Pietzonka 2022, PRL "
    "128:130606 — an inertial pendulum-clock model breaks the TUR). "
    f"(2) Was: \"{S2}\" Landauer's derivation counts states, so its bound does not depend on dimension; the Ω_D "
    "action on constants is a DS-internal posit. "
    f"(3) Was: \"{S3}\" Ashby's law is V_O ≥ V_D − V_R (Ashby 1956, S.11/8): the subtracted term is the regulator's "
    "variety and the bounded term the variety of outcomes; there is no 'channel' term. "
    f"Report: `{REPORT}`.", "The rest of the paragraph above is unchanged.")

# ─────────────────────────────────────────────────────────────────────────────
# Group B — dimensional_sensitivity facet (B5, E2, TD3)
# ─────────────────────────────────────────────────────────────────────────────
B_BANNERS = {
    "B5": banner("Landauer's derivation counts states and allows any number of degrees of freedom per state, so the "
                 "kT ln 2 per bit floor does not depend on spatial dimension (Landauer 1961; Bennett 2003). The "
                 "dimensional_sensitivity facet is changed from D-sensitive to D-invariant, which also matches B5's own "
                 "What's Conjectured section.", B_TAIL),
    "E2": banner("E2 was tagged D-sensitive only through B5 (the 'Applied to this entry' line calls the Landauer floor "
                 "'a D-sensitive bound'). B5 is D-invariant, so E2's dimensional_sensitivity facet is changed from "
                 "D-sensitive to D-invariant.", B_TAIL),
    "TD3": banner("ΔS ≥ 0 has the same form in any dimension. What depends on dimension is the entropy of particular "
                  "systems (through their density of states), not the law. The dimensional_sensitivity facet is "
                  "changed from D-sensitive to D-invariant.", B_TAIL),
}
PROPERTIES = [("B5", "D-sensitive", "D-invariant"), ("E2", "D-sensitive", "D-invariant"),
              ("TD3", "D-sensitive", "D-invariant")]

# ─────────────────────────────────────────────────────────────────────────────
# Individual corrections (C1-C28) — section banners
# ─────────────────────────────────────────────────────────────────────────────
ZHANG = ("Zhang, Cao, Ouyang & Tu 2020 (Nat. Phys. 16:95, doi:10.1038/s41567-019-0701-7)")
SYNC_NOT_ERASURE = ("Synchronization is not an erasure: keeping oscillators in step is continuous dissipation against "
                    "noise, and the published minimum cost diverges, rather than vanishes, at full synchrony (" + ZHANG +
                    "; see Q5's correction). The motivation is also void under H3's 2026-07-25 definition of λ.")
LAUGHLIN = "Laughlin, de Ruyter van Steveninck & Anderson 1998 (Nat. Neurosci. 1:36, doi:10.1038/236)"

# (entry_id, section_name) -> dict(checks=[must-exist strings], replace=[(find, repl)], banners=[...])
SECTION_OPS = {}


def sec(eid, name, banners=(), replace=(), checks=()):
    key = (eid, name)
    op = SECTION_OPS.setdefault(key, dict(checks=[], replace=[], banners=[]))
    op["checks"] += list(checks)
    op["replace"] += list(replace)
    op["banners"] += list(banners)


# Group A + B composition
for eid in A_ENTRIES:
    sec(eid, "Mathematical Archetype",
        replace=[(S3, N3), (S1, N1), (S2, N2 + a_marker(eid))])
sec("B5", "Mathematical Archetype", banners=[A_B5_BANNER, B_BANNERS["B5"]])
sec("E2", "Mathematical Archetype", banners=[B_BANNERS["E2"]])
sec("TD3", "Mathematical Archetype", banners=[B_BANNERS["TD3"]])

# C1 TD2
sec("TD2", "DS Cross-References", checks=["a first-law consequence for information"], banners=[banner(
    "Landauer's bound is a second-law result, not a first-law one. The first law only does the bookkeeping: when the "
    "memory's energy is unchanged, the work put in leaves as heat. The kT ln 2 minimum comes from the entropy count "
    "(Landauer 1961; Bennett 2003, Stud. Hist. Phil. Mod. Phys. 34:501, which calls the principle a consequence or "
    "restatement of the second law).")])
# C2 EM11
sec("EM11", "DS Cross-References", checks=["even reversible computation produces Joule-like dissipation"], banners=[banner(
    "Wrong. Logically reversible computation has no Landauer floor: it can in principle run at zero cost, or at a cost "
    "per step that vanishes as it is run more slowly (Bennett 1982; Bennett 2003). Real devices dissipate because they "
    "run at finite speed; that excess falls off as 1/τ with cycle time τ and depends on the protocol (Proesmans, Ehrich "
    "& Bechhoefer 2020, PRL 125:100602). In Jun, Gavrilov & Bechhoefer 2014 (PRL 113:190601) a matched operation that "
    "erased nothing cost 0.05 ± 0.03 kT, against 0.71 ± 0.03 kT for a full erasure. kT ln 2 is the price of erasing a "
    "bit, not of computing.")])
# C3 + C26 NE06 DS Cross-References
sec("NE06", "DS Cross-References",
    checks=["copying one bit costs at least kT ln 2", "organisms maximise entropy production"], banners=[banner(
    "Two corrections. (1) The B5 clause: copying is not erasure. Copying onto a blank register is logically reversible "
    "and has no minimum dissipation in principle (Bennett 1982; Bennett 2003, whose own example is DNA → RNA "
    "transcription). What cannot be avoided is free energy of kT × I, where I is the mutual information between copy "
    "and template in nats. For a copy that persists after it separates from its template, that free energy must be "
    "supplied up front and is stored in the correlation; it is dissipated only if the correlation is later lost without "
    "being used (Ouldridge, Govern & ten Wolde 2017, PRX 7:021004; Ouldridge & ten Wolde 2017, PRL 118:158103). "
    "(2) The TD3 and NE02 clauses: England derives a lower bound on heat production. He does not claim that organisms "
    "maximise entropy production, and the bound is not a maximum-entropy-production (MEPP) result. Kolchinsky 2024 "
    "(arXiv:2404.01130) argues there is no universal link between dissipation and replicator growth rate.")])
# C4 BIO5 DS Cross-References
sec("BIO5", "DS Cross-References",
    checks=["transcription and translation are irreversible information operations with thermodynamic cost"],
    banners=[banner(
    "Template copying is not inherently logically irreversible: transcription can be treated as a logically reversible "
    "copy, driven mainly by removal of the pyrophosphate product (Bennett 1982; Bennett 2003). The free energy cells "
    "actually spend per nucleotide or amino acid pays for speed, direction and accuracy (Andrieux & Gaspard 2008, PNAS "
    "105:9516; Sartori & Pigolotti 2015, PRX 5:041039), not for a Landauer erasure. The only Landauer-type cost is on "
    "correlations discarded without use (see NE06's correction).")])
# C5 BIO5 fidelity
sec("BIO5", "Mathematical Form", checks=["error rate ~10⁻⁹ per base per replication (with proofreading)"], banners=[banner(
    "~10⁻⁹ hides three stages: base selection by the polymerase (~10⁻⁴–10⁻⁵ per base), exonuclease proofreading "
    "(~10⁻² of those errors survive) and mismatch repair. The measured whole-genome rate for E. coli is 2.2 × 10⁻¹⁰ "
    "mutations per nucleotide per generation in wild type, and ~3.3 × 10⁻⁸ without mismatch repair (mutL deletion) "
    "(Lee, Popodi, Tang & Foster 2012, PNAS 109:E2774, Table 1). That is a rate per generation after all repair, not the "
    "polymerase's own error rate. Stage figures: Bębenek & Ziuzia-Graczyk 2018, Curr. Genet. 64:985.")])
sec("BIO5", "What The Math Says", checks=["approximately 10 to the minus 9 per base"], banners=[banner(
    "The 10⁻⁹ figure and the per-division arithmetic built on it are qualified in the Mathematical Form correction "
    "(three error-correction stages; E. coli measured at 2.2 × 10⁻¹⁰ per nucleotide per generation, Lee et al. 2012).")])
# C6 + C7 + C8a INFO4 DS Cross-References
_RG04 = ("RG04 (Zamolodchikov c-theorem — the c-theorem is the field-theoretic instance of the DPI: RG coarse-graining "
         "is a Markov chain step, and the c-function counting effective degrees of freedom decreases monotonically under "
         "it, exactly as I(X;Z) ≤ I(X;Y). Information loss under coarse-graining IS RG irreversibility).")
sec("INFO4", "DS Cross-References",
    checks=["the DPI explains why reverse translation protein→DNA cannot occur", "ΔI × kT ln 2"],
    replace=[(_RG04 + " " + _RG04, _RG04)],
    banners=[banner(
    "Three corrections. (1) The BIO5 clause is overstated. The DPI bounds how much information about a source survives "
    "along a Markov chain. It does not forbid a mechanism that writes some (non-unique) coding sequence for a given "
    "protein: degeneracy means the original DNA could not be recovered, not that reverse translation is impossible. The "
    "Central Dogma is an empirical claim about which transfers occur (Crick 1970). (2) The B5 clause: 'ΔI × kT ln 2' "
    "is a lower bound ('at least'), not a fixed cost, and only for information actually erased or correlations "
    "discarded without use (Sagawa & Ueda 2009, PRL 102:250602; Ouldridge, Govern & ten Wolde 2017). (3) Hygiene: the "
    "RG04 sentence appeared twice, verbatim; the second copy was removed. On the RG04 claim itself see the What It "
    "Claims correction.")])
# C8b INFO4 Concept Tags dedup
_TAGS6 = ("\n• coarse-graining\n• degrees of freedom reduction\n• RG irreversibility\n• c-theorem foundation"
          "\n• UV-IR monotonicity\n• RG flow analog")
sec("INFO4", "Concept Tags", replace=[(_TAGS6 + _TAGS6, _TAGS6)])
# C9 INFO4 What It Claims
sec("INFO4", "What It Claims",
    checks=["The DPI therefore provides the information-theoretic proof that RG flow is irreversible"], banners=[banner(
    "Overstated. The DPI does not prove that RG flow is irreversible. Zamolodchikov's 1986 proof rests on unitarity "
    "(reflection positivity), rotation invariance and stress-tensor conservation; the entropic proof (Casini & Huerta "
    "2004, arXiv:hep-th/0405111) rests on strong subadditivity of quantum entanglement entropy plus Poincaré symmetry. "
    "The DPI comparison is an analogy: both are monotonicity statements under coarse-graining, but an RG step has not "
    "been shown to be a Markov channel on a probability distribution in the DPI's sense. The same overstatement recurs "
    "in this entry's other sections and in RG04 (not corrected in this pass).")])
# C10 B5 Why It Matters Here
sec("B5", "Why It Matters Here",
    checks=["every neural spike, every enzymatic decision that discards information",
            r"$A \cdot k_B T \ln 2 / 4\ell_P^2$"], banners=[banner(
    "(1) The floor applies only to information actually erased. A spike is signalling, not erasure, and measured neural "
    "costs are far higher: about 10⁴ ATP per bit at a chemical synapse and 10⁶–10⁷ ATP per bit for graded or spiking "
    "signals in blowfly retina, roughly 3 × 10⁵ – 3 × 10⁸ times kT ln 2 at ~20 kT per ATP (" + LAUGHLIN + "). "
    "(2) The holographic bound S ≤ A/4ℓ_P² is in units of k_B (nats), so the corresponding erasure-cost bound is "
    "kT·A/4ℓ_P², without the ln 2; the holographic bound does not fix T.")])
# C11 B5 What's Established
sec("B5", "What's Established", checks=["measuring dissipation approaching the $k_B T \\ln 2$ limit"], banners=[banner(
    "Bérut et al. reached kT ln 2 only in the limit of slow cycles, by extrapolation, and with incomplete erasure. The "
    "precision test is Jun, Gavrilov & Bechhoefer 2014 (PRL 113:190601): full erasure costs 0.71 ± 0.03 kT (an "
    "asymptotic value from a 1/τ fit; ln 2 ≈ 0.69), while a matched protocol that erases nothing costs 0.05 ± 0.03 kT.")])
# C12 B5 What The Math Says
sec("B5", "What The Math Says", checks=["Reversible computation (quantum computing in principle) can avoid this cost entirely."],
    banners=[banner(
    "In principle only (Bennett 1982; Bennett 2003). In practice, preparing ancilla bits, disposing of garbage bits, "
    "running at finite speed and resetting error-correction syndromes all erase information and pay the bound. Quantum "
    "computing is not the same thing as reversible computing here.")])
# C13 B5 Key Connections (H3, G3, F5 rows) + G3 Key Connections (same holographic row)
sec("B5", "Key Connections",
    checks=["Synchronization maintenance is a Landauer-class erasure cost",
            "Holographic entropy bound times $k_B T \\ln 2$ gives total erasure cost",
            "Sets minimum energy cost of biological information processing"], banners=[banner(
    "Three rows corrected. H3: synchronization is not an erasure; its published minimum cost diverges, rather than "
    "vanishes, at full synchrony (" + ZHANG + "; see Q5). G3: the holographic bound is in nats, so the factor is kT, not "
    "kT ln 2 (see Why It Matters Here). F5: no bearing on the oxygen corridor, whose edges are set by CcO kinetics and "
    "ROS balance, many orders of magnitude above any Landauer cost.")])
sec("G3", "Key Connections", checks=["Holographic entropy times $k_B T \\ln 2$ gives total erasure cost"], banners=[banner(
    "The holographic bound S ≤ A/4ℓ_P² is in units of k_B (nats), so the erasure-cost bound is kT·A/4ℓ_P², without the "
    "ln 2 (see B5's Why It Matters Here correction).")])
# C14 Q5
sec("Q5", "Current Status", checks=["has not been published"], banners=[banner(
    "The literature has an answer, and it contradicts this ansatz in form. " + ZHANG + " compute the free-energy cost "
    "of synchronizing coupled biochemical oscillators. Below a critical dissipation there is no synchrony at all, and "
    "under their optimal design the minimum excess dissipation diverges as 1/(1−r) as the Kuramoto order parameter "
    "r → 1 (their Eq. 15). The ansatz here makes the cost vanish at full coherence. A single oscillator's coherence also "
    "costs free energy (Cao, Wang, Ouyang & Tu 2015), bounded by the driving affinity and the number of states in the "
    "cycle (Barato & Seifert 2017, proved by Ohga, Ito & Kolchinsky 2023). None of this is Landauer erasure: it is "
    "continuous dissipation to stay out of equilibrium. Zhang's analysis is mean-field, with no dependence on dimension "
    "or d_f. Caveat: under the 2026-07-25 redefinition λ is no longer a coherence (H3), so this compares only against "
    "the original 'phase coherence' reading. Pattern tag: landauer-scope-overreach.")])
sec("Q5", "Nearest Existing Literature", checks=["Acebrón, J.A. et al. (2005)"], banners=[
    f"\n\n*Added {D} (`{AUDIT_REF}`) — the published answers, which contradict the ansatz in form (see Current Status):*\n"
    "- Zhang, D., Cao, Y., Ouyang, Q. & Tu, Y. (2020). The energy cost and optimal design for synchronization of coupled "
    "molecular oscillators. *Nature Physics*, 16, 95–100. [Minimum dissipation diverges as 1/(1−r); no synchrony below "
    "a critical dissipation; mean-field]\n"
    "- Cao, Y., Wang, H., Ouyang, Q. & Tu, Y. (2015). The free-energy cost of accurate biochemical oscillations. "
    "*Nature Physics*, 11, 772–778. [Single-oscillator coherence costs free energy]\n"
    "- Barato, A.C. & Seifert, U. (2017). Coherence of biochemical oscillations is bounded by driving force and network "
    "topology. *Physical Review E*, 95, 062409. [Bound proved by Ohga, Ito & Kolchinsky 2023, PRL 131:077101]"])
sec("Q5", "DS Connections", checks=["Synchronization cost is a Landauer-class erasure"], banners=[banner(
    "Synchronization is not an erasure; the published minimum cost diverges at full synchrony (" + ZHANG +
    "; see Current Status).")])
# C15 B5 Phase Coherence Cost, H3 What It Says, H3 Key Connections
sec("B5", "Phase Coherence Cost (Tier 3 ‡_p)",
    checks=["Re-synchronizing desynchronized subsystems requires erasing their phase differences"],
    banners=[banner(SYNC_NOT_ERASURE)])
sec("H3", "What It Says", checks=["which is a Landauer-class irreversible operation (see B5)"],
    banners=[banner("On the physics of the 'Landauer-class' cost in the second paragraph: " + SYNC_NOT_ERASURE)])
sec("H3", "Key Connections", checks=["Synchronization cost is a Landauer-class information erasure cost"],
    banners=[banner("B5 row: " + SYNC_NOT_ERASURE)])
# C16 D1, X6
sec("D1", "Key Connections", checks=["Neural encoding pays Landauer cost per bit of stimulus resolution"], banners=[banner(
    "B5 row: encoding is not erasure, so Landauer does not price it. The measured metabolic cost of neural information "
    "is about 10⁴–10⁷ ATP per bit, set mainly by ion pumping (" + LAUGHLIN + ").")])
sec("X6", "DS Connections", checks=["Neural Landauer cost per spike; synchronization cost via H3"], banners=[banner(
    "B5 row: a spike is signalling, not erasure, so Landauer does not price it; the measured metabolic cost of neural "
    "information is about 10⁴–10⁷ ATP per bit (" + LAUGHLIN + "). The H3 synchronization cost is retired (see Q5).")])
# C17 INFO1
_INFO1_FIX = ("The axioms are misstated. Additivity for independent variables does not single out Shannon entropy: every "
              "Rényi entropy has it too (Rényi 1961). Shannon's 1948 uniqueness theorem uses continuity, growth with n "
              "for equally likely outcomes, and the grouping (chain-rule) property H(X,Y) = H(X) + H(Y|X). Khinchin "
              "1957 uses continuity, maximum at the uniform distribution, invariance under adding zero-probability "
              "outcomes, and the same chain rule.")
sec("INFO1", "What It Claims", checks=["continuity, symmetry, and additivity for independent variables"],
    banners=[banner(_INFO1_FIX)])
sec("INFO1", "Constraint Category", checks=["(3) H(X,Y) = H(X) + H(Y) for independent X,Y"],
    banners=[banner(_INFO1_FIX)])
# C18 F1
sec("F1", "Formula", checks=[r"V_{\text{controller}} \geq V_{\text{system}} - V_{\text{channel}}"], banners=[banner(
    "Ashby's own form (An Introduction to Cybernetics, 1956, S.11/8): with varieties measured logarithmically, "
    "V_outcomes ≥ V_disturbances − V_regulator, or H(E) ≥ H(D) − H(R). The formula above is this rearranged, with the "
    "outcome variety mislabelled 'channel'.")])
sec("F1", "What's Established", checks=["It follows directly from Shannon's channel coding theorem"], banners=[banner(
    "Ashby derives the law by counting and from elementary entropy inequalities (S.11/5–11/8), then notes that one form "
    "of it stands in exact relation to Shannon's Theorem 10 (noise removable by a correction channel is limited by that "
    "channel's capacity). It is not a consequence of the channel coding theorem. The rigorous control-theory version "
    "is Touchette & Lloyd 2000 (PRL 84:1156; not read in this pass).")])
sec("F1", "Why It Matters Here", checks=["requiring at least four filtering layers — and five are observed"],
    banners=[banner("The 'four layers needed, five observed' argument is internal DS 2.0 content, not part of Ashby's "
                    "law, and is unsourced here.")])
sec("F1", "Key Connections", checks=["Variety regulation has an energy cost: $k_B T \\ln 2$ per bit of disturbance suppressed"],
    banners=[banner(
    "B5 row: there is no established 'kT ln 2 per bit suppressed' cost. The formal route from regulation to "
    "thermodynamics is feedback thermodynamics (Sagawa & Ueda 2009, 2010), where the cost depends on what is measured "
    "and what is erased; the link is a heuristic.")])
# C19, C20 INFO5
sec("INFO5", "Mathematical Archetype", checks=["Irreversible operations (like lossy compression) increase K relative to the original"],
    banners=[banner(
    "Wrong direction. The inequality just stated, K(f(x)) ≤ K(x) + K(f) + O(1), means computable processing cannot "
    "raise K by more than the program's own complexity; lossy compression typically lowers K (Li & Vitányi).")])
sec("INFO5", "DS Cross-References", checks=["the minimum energy to erase the description of x is K(x) × kT ln 2 joules"],
    banners=[banner(
    "This is Zurek's 1989 proposal (PRA 40:4731), not an established theorem: it holds for deterministic computation, "
    "up to additive constants, and K is uncomputable, so no process can be guaranteed to reach it. Kolchinsky 2023 (PRE "
    "108:034101) shows the cost can be paid in heat, noise or protocol complexity.")])
# C21 IT03
sec("IT03", "DS Cross-References", checks=["which equals kT times the KL divergence between the initial and erased states"],
    banners=[banner(
    "Direction matters: D(erased‖initial) = ln 2, but D(initial‖erased) is infinite. The general statement is "
    "W ≥ ΔF_eq + kT[D(ρ_final‖ρ_eq) − D(ρ_initial‖ρ_eq)] (Esposito & Van den Broeck 2011, EPL 95:40004). For erasure in "
    "a symmetric double well, ΔF_eq = 0, the initial state is the equilibrium one, and D(ρ_final‖ρ_eq) = ln 2.")])
# C22 CS11
sec("CS11", "DS Cross-References", checks=["each comparison is an irreversible information operation"], banners=[banner(
    "Right size, wrong reason. Comparisons can be done reversibly (any computation can be made logically reversible if "
    "its input is kept; Bennett 1982, 2003), so they carry no Landauer cost one by one. What cannot be avoided is "
    "discarding the input order: erasing log₂(n!) bits costs kT ln(n!) ≈ kT n ln n, and nothing at all if the "
    "permutation is kept. (Derived from Landauer and Bennett; no primary source on sorting.)")])
# C23 E2
sec("E2", "Why It Matters Here", checks=["the Landauer limit would be reached around 2080", "State-of-art (2025)"],
    banners=[banner(
    "Unsourced. Koomey, Berard, Sanchez & Wong 2011 (IEEE Ann. Hist. Comput. 33(3):46) never mention Landauer and "
    "project no year; they cite Feynman's estimate that a 10¹¹-fold improvement on 1985 technology was theoretically "
    "possible. The 2080 date and the 2025 row have no source and should be treated as unsourced. (Secondary sources "
    "extrapolate the 1.57-year doubling to the Landauer scale around 2048–2050, and the doubling time lengthened after "
    "about 2000; search summary only.) Also, joules per operation is not joules per erased bit: a logically reversible "
    "operation erases nothing, so Landauer is a floor only for irreversible logic.")])
sec("E2", "What's Contested", checks=["The extrapolation to 2080"], banners=[banner(
    "The 2080 extrapolation is unsourced; see the Why It Matters Here correction.")])
# C24 TD3
sec("TD3", "DS Cross-References", checks=["consistent with maximum work extraction occurring at equilibrium"],
    banners=[banner(
    "Physics correction. No work can be extracted from a system at thermodynamic equilibrium. Maximum power is reached "
    "away from equilibrium; in linear response the efficiency at maximum power is half the Carnot efficiency (Van den "
    "Broeck 2005, PRL 95:190602; Schmiedl & Seifert 2008, EPL 83:30005). The AlphaEntropy passage is an analogy: "
    "'equilibrium' here is a label for a dep/capex ratio near 1, not a thermodynamic state.")])
# C25 NE06 Mathematical Form + What The Math Says
sec("NE06", "Mathematical Form", checks=["⟨ΔS_total⟩ ≥ −Δs_int + log(n_rep/n_init)"], banners=[banner(
    "Misquoted. England's inequality (arXiv:1209.1179 v1, Eq. 6) is β⟨ΔQ⟩ + ln π(→I|II) + ΔS_int ≥ 0: the heat "
    "released, plus the internal entropy change, is bounded below by how improbable it is for the replication to run "
    "backwards (π(→I|II) is the probability of returning from the replicated state II to the initial state I). There is "
    "no replication-ratio term; England notes the result is a precise statement of the second law. The published "
    "version (J. Chem. Phys. 139:121923, 2013) recasts it for replicators in terms of growth rate, internal entropy "
    "and durability. Checked against the arXiv v1 full text, not the published version.")])
sec("NE06", "What The Math Says", checks=["the logarithm of the replication ratio n-rep over n-init"], banners=[banner(
    "The bound described here is misquoted; see the Mathematical Form correction (England's Eq. 6 has no "
    "replication-ratio term).")])
# C27 F5 (A2 replacements already composed above)
sec("F5", "Mathematical Archetype", checks=["lower edge from quantum tunneling rates, upper edge from thermal denaturation"],
    banners=[banner(
    "The 'Applied to this entry' line contradicts F5's own text, which gives ATP failure (low PO₂) and oxidative damage "
    "(high PO₂) as the corridor edges, not tunnelling rates and thermal denaturation.")])
# C28 MATH4
sec("MATH4", "DS Cross-References", checks=["Landauer gives the thermodynamic cost of logical operations"],
    banners=[banner(
    "Of logically irreversible operations only; logically reversible operations have no Landauer floor (Bennett 1982; "
    "Bennett 2003).")])

# ─────────────────────────────────────────────────────────────────────────────
# Link descriptions — (table, id, source, target, must-contain-in-old, new text)
# ─────────────────────────────────────────────────────────────────────────────
_SYNC1 = ("Synchronization is not an erasure; its published minimum cost diverges, rather than vanishes, at full "
          "synchrony (Zhang et al. 2020, Nat. Phys. 16:95; see Q5).")
_HOLO1 = "The holographic bound is in nats, so the total erasure-cost bound is kT·A/4ℓ_P², without the ln 2."
_F5_1 = ("No bearing on the oxygen corridor, whose edges are set by CcO kinetics and ROS balance, many orders of "
         "magnitude above any Landauer cost.")
_NEURAL = ("Neural encoding has a metabolic cost of about 10⁴–10⁷ ATP per bit (Laughlin et al. 1998), far above and "
           "unrelated to Landauer's erasure floor: encoding is not erasure.")
_ASHBY = ("No established 'kT ln 2 per bit suppressed' cost; the formal route from regulation to thermodynamics is "
          "feedback thermodynamics (Sagawa & Ueda), where the cost depends on what is measured and erased. Heuristic link.")
LINK_FIXES = [
    ("links", 228, "B5", "TD2", "also follows from the first law",
     "The kT ln 2 floor comes from the second law (TD3, link 227), not the first; the first law contributes only the "
     "bookkeeping (work in = heat out when the memory's energy is unchanged)."),
    ("links", 793, "NE06", "B5", "organisational entropy of the replica",
     "Copying is not erasure: a persistent copy needs free energy of at least kT × (copy–template mutual information), "
     "stored in the correlation and dissipated only if it is lost unused (Ouldridge et al. 2017; Bennett 1982)."),
    ("links", 259, "BIO5", "B5", "thermodynamically irreversible information operation",
     "Template copying is not inherently logically irreversible (Bennett 1982, 2003); the free energy spent pays for "
     "speed, direction and accuracy, not for a Landauer erasure."),
    ("links", 328, "INFO4", "BIO5", "information-theoretic proof that protein→DNA reverse translation is impossible",
     "The DPI bounds information about a source along a Markov chain; it does not forbid writing a (non-unique) coding "
     "sequence for a protein. The Central Dogma is an empirical claim (Crick 1970)."),
    ("links", 41, "B5", "F5", "Sets minimum energy cost of biological information processing", _F5_1),
    ("links", 42, "B5", "G3", "gives total erasure cost", _HOLO1),
    ("links", 71, "H3", "B5", "Landauer-class information erasure cost", _SYNC1),
    ("links", 45, "D1", "B5", "Neural encoding pays Landauer cost", _NEURAL),
    ("links", 47, "F1", "B5", "per bit of disturbance suppressed", _ASHBY),
    ("links", 332, "INFO5", "B5", "K(x) × kT ln 2", "Zurek's 1989 proposal, not an established theorem (deterministic "
     "computation, up to constants; K is uncomputable). Kolchinsky 2023: the cost can be paid in heat, noise or "
     "protocol complexity."),
    ("links", 371, "CS11", "B5", "minimum thermodynamic cost of sorting",
     "Comparisons can be done reversibly, so they carry no Landauer cost one by one; the unavoidable cost is discarding "
     "the input order, kT ln(n!) ≈ kT n ln n, and zero if the permutation is kept."),
    ("entry_connections", 35, "B5", "G3", "total erasure cost", _HOLO1),
    ("entry_connections", 94, "G3", "B5", "total erasure cost", _HOLO1),
    ("entry_connections", 37, "B5", "F5", "Sets minimum energy cost of biological information processing", _F5_1),
    ("entry_connections", 38, "B5", "H3", "Landauer-class erasure cost", _SYNC1),
    ("entry_connections", 111, "H3", "B5", "Landauer-class information erasure cost", _SYNC1),
    ("entry_connections", 167, "Q5", "B5", "Landauer-class erasure", _SYNC1),
    ("entry_connections", 56, "D1", "B5", "Neural encoding pays Landauer cost", _NEURAL),
    ("entry_connections", 228, "X6", "B5", "Neural Landauer cost per spike",
     _NEURAL + " The H3 synchronization cost is retired (see Q5)."),
    ("entry_connections", 69, "F1", "B5", "per bit of disturbance suppressed", _ASHBY),
]
LINK_COLS = {"links": ("source_id", "target_id"), "entry_connections": ("entry_id", "target_id")}

# ─────────────────────────────────────────────────────────────────────────────
# Calibration — append-only, label unchanged
# ─────────────────────────────────────────────────────────────────────────────
CALIBRATIONS = [(
    "P15", "conjecture", "Speculative", D, AUDIT_REF,
    "Speculative (unchanged) — the published synchronization-cost result contradicts the (1−λ)² form under the original "
    "phase-coherence reading [landauer-scope-overreach; ansatz-without-derivation]",
    "QR-004 corrections pass (owner-approved 2026-10-18). Zhang, Cao, Ouyang & Tu 2020 (Nat. Phys. 16:95) give the "
    "free-energy cost of synchronizing coupled biochemical oscillators: no synchrony below a critical dissipation, and "
    "under the optimal design the minimum excess dissipation diverges as 1/(1−r) as the Kuramoto order parameter r → 1 "
    "(Eq. 15; mean-field, no dimension or d_f dependence). P15's motivating cost (Q5) vanishes at full coherence, the "
    "opposite form. Synchronization is continuous dissipation, not Landauer erasure. Label unchanged because under "
    "H3's 2026-07-25 definition λ is not a coherence, so the result does not test P15 as now defined; P15 already "
    "needs a different rationale. Report: " + REPORT + "."),
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
    for (table, lid, *_rest) in LINK_FIXES:
        once((table, lid, "description"))
    for (eid, _, _) in PROPERTIES:
        once(("entry_properties", eid, "dimensional_sensitivity"))


def plan_section(content, op, label):
    """Return new content, or None if already applied. Abort on partial state."""
    banners = op["banners"]
    stripped = content
    for b in banners:
        stripped = stripped.replace(b, "")
    present = [b in content for b in banners]
    applied = (all(present) and all(f not in stripped and r in stripped for f, r in op["replace"]))
    if applied:
        return None
    if any(present) or (AUDIT_REF in content):
        raise SystemExit(f"[{label}] ABORT — partially applied")
    new = content
    for find, repl in op["replace"]:
        n = new.count(find)
        if n != 1:
            raise SystemExit(f"[{label}] FAIL — find count {n}: {find[:70]!r}")
        new = new.replace(find, repl, 1)
    for chk in op["checks"]:
        if chk not in content:
            raise SystemExit(f"[{label}] FAIL — check string missing: {chk[:70]!r}")
    return new + "".join(banners)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")
    check_targets()

    print("=" * 72); print("PHASE 1 — validation / dry run"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    sec_ops, skipped = [], 0
    for (eid, name), op in SECTION_OPS.items():
        row = cur.execute("SELECT id, content FROM sections WHERE entry_id=? AND section_name=?", (eid, name)).fetchone()
        if row is None:
            raise SystemExit(f"[{eid}.{name}] ABORT — section not found")
        new = plan_section(row[1], op, f"{eid}.{name}")
        if new is None:
            skipped += 1; continue
        sec_ops.append((row[0], f"{eid}.{name}", new))
        print(f"  [{eid}.{name}] plan — {len(op['replace'])} replace, {len(op['banners'])} banner(s), "
              f"{len(row[1])} → {len(new)} chars")
    link_ops = []
    for table, lid, s, t, must, new_text in LINK_FIXES:
        sc, tc = LINK_COLS[table]
        row = cur.execute(f"SELECT {sc}, {tc}, description FROM {table} WHERE id=?", (lid,)).fetchone()
        if row is None or (row[0], row[1]) != (s, t):
            raise SystemExit(f"[{table} {lid}] ABORT — unexpected row {row!r}")
        desc = row[2]
        if desc.startswith(LINK_PREFIX):
            skipped += 1; continue
        if must not in desc:
            raise SystemExit(f"[{table} {lid}] FAIL — expected text missing: {must!r}")
        link_ops.append((table, lid, LINK_PREFIX + new_text + f' Previously: "{desc}"'))
        print(f"  [{table} {lid} {s}->{t}] plan")
    prop_ops = []
    for eid, old, new in PROPERTIES:
        rows = cur.execute("SELECT id, property_value FROM entry_properties WHERE entry_id=? "
                           "AND property_name='dimensional_sensitivity'", (eid,)).fetchall()
        if len(rows) != 1:
            raise SystemExit(f"[{eid}.dimensional_sensitivity] ABORT — {len(rows)} rows")
        if rows[0][1] == new:
            skipped += 1; continue
        if rows[0][1] != old:
            raise SystemExit(f"[{eid}.dimensional_sensitivity] ABORT — value {rows[0][1]!r}")
        prop_ops.append((rows[0][0], eid, new)); print(f"  [{eid}.dimensional_sensitivity] plan {old} → {new}")
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    pending_cal = [c for c in CALIBRATIONS if not hc.execute(
        "SELECT 1 FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
        (c[0], c[3], c[4])).fetchone()]
    hc.close()
    print(f"\n  {len(sec_ops)} section writes, {len(link_ops)} link writes, {len(prop_ops)} property writes, "
          f"{len(pending_cal)} calibration rows; {skipped} targets already applied")

    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply."); return

    print("\n" + "=" * 72); print("PHASE 2 — apply"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    try:
        for sid, label, new in sec_ops:
            cur.execute("UPDATE sections SET content=? WHERE id=?", (new, sid))
            if cur.rowcount != 1: raise SystemExit(f"[{label}] rowcount {cur.rowcount}")
        for table, lid, new in link_ops:
            cur.execute(f"UPDATE {table} SET description=? WHERE id=?", (new, lid))
            if cur.rowcount != 1: raise SystemExit(f"[{table} {lid}] rowcount {cur.rowcount}")
        for pid, eid, new in prop_ops:
            cur.execute("UPDATE entry_properties SET property_value=? WHERE id=?", (new, pid))
            if cur.rowcount != 1: raise SystemExit(f"[{eid} prop] rowcount {cur.rowcount}")
        conn.commit()
    except BaseException:
        conn.rollback(); conn.close(); raise
    conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for row in pending_cal:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date,
                      audit_ref, short_status, rationale) VALUES (?,?,?,?,?,?,?)""", row)
    hc.commit(); hc.close()
    print(f"  wrote {len(sec_ops)} sections, {len(link_ops)} links, {len(prop_ops)} properties, "
          f"{len(pending_cal)} calibration rows")

    print("\n" + "=" * 72); print("PHASE 3 — read-back verification"); print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB); cur = conn.cursor()
    bad = [label for sid, label, new in sec_ops
           if cur.execute("SELECT content FROM sections WHERE id=?", (sid,)).fetchone()[0] != new]
    bad += [f"{t}:{lid}" for t, lid, new in link_ops
            if cur.execute(f"SELECT description FROM {t} WHERE id=?", (lid,)).fetchone()[0] != new]
    bad += [f"prop:{eid}" for pid, eid, new in prop_ops
            if cur.execute("SELECT property_value FROM entry_properties WHERE id=?", (pid,)).fetchone()[0] != new]
    # every planned target now reads as applied
    for (eid, name), op in SECTION_OPS.items():
        c = cur.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (eid, name)).fetchone()[0]
        if plan_section(c, op, f"{eid}.{name}") is not None:
            bad.append(f"not-applied:{eid}.{name}")
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
    print(f"  verified: {len(sec_ops)} sections, {len(link_ops)} links, {len(prop_ops)} properties, "
          f"{len(CALIBRATIONS)} calibration rows; all {len(SECTION_OPS)} section targets read as applied")


if __name__ == "__main__":
    main()
