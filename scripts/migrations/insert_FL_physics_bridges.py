"""
Build incoming links from physics/information theory entries TO the FL
formal logic layer. Currently FL has 86 outgoing links but ZERO incoming
links from non-FL entries.

These bridges connect the formal logic foundation to the physics content,
enabling the Phase 3/4 paper validation pipeline to trace physical claims
back to their logical structure.

Each link says: "this physics result has this formal logical structure."
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB


LINKS = [
    # -----------------------------------------------------------------------
    # IT03 (KL Divergence) → FL1 (Deductive Validity) + FL9 (Tautological Entailment)
    # D_KL >= 0 is a theorem of probability theory — its validity is deductive.
    # The proof follows from Jensen's inequality applied to the convexity of -log.
    # -----------------------------------------------------------------------
    ("IT03", "FL1", "couples to", "1.5",
     "D_KL(p||q) >= 0 is a deductively valid theorem: given the axioms of "
     "probability theory, no counterexample exists. The proof via Jensen's "
     "inequality is a deductive chain from convexity of -log(x)."),
    ("IT03", "FL9", "couples to", "1.5",
     "D_KL >= 0 is a tautological entailment of the probability axioms: every "
     "assignment of probability distributions satisfying the axioms makes the "
     "inequality true. This is why irreversibility is mathematical, not physical."),

    # -----------------------------------------------------------------------
    # NE04 (Crooks Fluctuation Theorem) → FL14 (Reductio / Conditional Proof)
    # The Crooks derivation uses conditional proof structure: assume detailed
    # balance, derive the ratio P_F/P_R = exp(beta * delta_S).
    # -----------------------------------------------------------------------
    ("NE04", "FL14", "couples to", "1.5",
     "The Crooks fluctuation theorem is derived by conditional proof: assume "
     "microscopic reversibility (detailed balance), then derive "
     "P_F(W)/P_R(-W) = exp(beta(W-delta_F)) as a conditional consequence. "
     "The logical structure is: if detailed balance, then the fluctuation "
     "symmetry holds."),

    # -----------------------------------------------------------------------
    # IT06 (Seifert Stochastic Thermodynamics) → FL1 (Deductive Validity) + FL13 (Modus Ponens)
    # The integral fluctuation theorem <e^{-s_tot}> = 1 is an exact identity.
    # The second law follows from it by modus ponens + Jensen's inequality.
    # -----------------------------------------------------------------------
    ("IT06", "FL1", "couples to", "1.5",
     "The integral fluctuation theorem <e^{-s_tot}> = 1 is deductively valid "
     "for any stochastic dynamics — it follows from the normalization of "
     "probability distributions, with no physical assumptions."),
    ("IT06", "FL13", "couples to", "1.5",
     "The second law follows from the integral fluctuation theorem by modus "
     "ponens: (1) <e^{-s_tot}> = 1 [premise], (2) Jensen's inequality: "
     "e^{-<x>} <= <e^{-x}> [premise], therefore (3) <s_tot> >= 0 [conclusion]. "
     "This is a two-step deductive chain."),

    # -----------------------------------------------------------------------
    # INFO4 (DPI / Mutual Information) → FL9 (Tautological Entailment)
    # The DPI I(X;Z) <= I(X;Y) for X->Y->Z is a tautological entailment of
    # the Markov chain definition.
    # -----------------------------------------------------------------------
    ("INFO4", "FL9", "couples to", "1.5",
     "The Data Processing Inequality I(X;Z) <= I(X;Y) for X->Y->Z is "
     "tautologically entailed by the definition of Markov chains: the "
     "conditional independence X _|_ Z | Y makes the inequality true under "
     "every probability assignment satisfying the Markov property."),

    # -----------------------------------------------------------------------
    # HB09 (GSL) → FL2 (Soundness) + FL16 (Quantificational Logic)
    # The GSL is a universally quantified claim: FOR ALL processes,
    # dS_total/dt >= 0. Its soundness depends on the premises (Bekenstein-
    # Hawking entropy, quantum field theory on curved spacetime).
    # -----------------------------------------------------------------------
    ("HB09", "FL2", "couples to", "1.5",
     "The Generalised Second Law is a sound argument if its premises are true: "
     "(1) S_BH = A/4l_P^2 (Bekenstein-Hawking), (2) quantum fields on curved "
     "spacetime are unitary. The GSL's validity is deductive given these premises; "
     "its soundness depends on their empirical truth."),
    ("HB09", "FL16", "couples to", "1.5",
     "The GSL is a universally quantified claim: for all processes involving "
     "black holes, dS_total/dt >= 0. This is a first-order logical structure "
     "(universal quantifier over processes) whose scope covers all black hole "
     "interactions."),

    # -----------------------------------------------------------------------
    # TD3 (Second Law) → FL1 (Deductive Validity) + FL3 (Logical Form)
    # The second law has different logical forms depending on formulation:
    # Clausius (no spontaneous heat flow), Kelvin (no perfect engine),
    # statistical (S increases with overwhelming probability).
    # -----------------------------------------------------------------------
    ("TD3", "FL1", "couples to", "1.5",
     "The statistical formulation of the Second Law (entropy increases with "
     "overwhelming probability for macroscopic systems) is deductively valid "
     "given the assumption of equal a priori probability of microstates. "
     "The Clausius and Kelvin formulations are logically equivalent."),
    ("TD3", "FL3", "couples to", "1.5",
     "The Second Law has three logically equivalent formulations (Clausius, "
     "Kelvin, statistical) with different surface forms but identical logical "
     "structure. The equivalence is proven by showing each implies the others "
     "— a demonstration that logical form, not topic, determines validity."),

    # -----------------------------------------------------------------------
    # GT07 (Chirco Non-Eq Spacetime Thermo) → FL14 (Conditional Proof)
    # Chirco's extension is a conditional: IF modified gravity (f(R)),
    # THEN entropy production sigma > 0 on the horizon.
    # -----------------------------------------------------------------------
    ("GT07", "FL14", "couples to", "1.5",
     "The non-equilibrium extension of Jacobson's derivation is a conditional "
     "proof: assume f(R) gravity (departure from Einstein GR), then derive "
     "entropy production sigma >= 0 on the horizon as a necessary consequence. "
     "Setting sigma = 0 recovers Jacobson's original conditional proof of GR."),

    # -----------------------------------------------------------------------
    # NE03 (Jarzynski) → FL13 (Modus Ponens)
    # Jarzynski follows from Crooks by exponential averaging — a modus ponens
    # step from the Crooks ratio.
    # -----------------------------------------------------------------------
    ("NE03", "FL13", "couples to", "1.5",
     "The Jarzynski equality follows from the Crooks fluctuation theorem by "
     "modus ponens: (1) P_F(W)/P_R(-W) = exp(beta(W-delta_F)) [Crooks], "
     "(2) integrate both sides over W [valid operation], therefore "
     "(3) <e^{-beta*W}> = e^{-beta*delta_F} [Jarzynski]. Each step is a "
     "deductively valid inference."),

    # -----------------------------------------------------------------------
    # RG04 (c-theorem) → FL1 (Deductive Validity) + FL16 (QL / universal quantifier)
    # The c-theorem is a proven theorem in 2D QFT: FOR ALL 2D QFTs,
    # c_UV >= c_IR. Zamolodchikov's proof is deductive.
    # -----------------------------------------------------------------------
    ("RG04", "FL1", "couples to", "1.5",
     "The Zamolodchikov c-theorem is a deductively valid theorem in 2D QFT: "
     "given unitarity, Lorentz invariance, and the existence of a "
     "stress-energy tensor, dc/dt <= 0 follows by construction from "
     "two-point correlation functions. The proof is explicit and deductive."),
    ("RG04", "FL16", "couples to", "1.5",
     "The c-theorem is universally quantified: for all 2D quantum field "
     "theories satisfying unitarity and Lorentz invariance, c_UV >= c_IR. "
     "This is a first-order statement whose scope is the class of unitary "
     "Lorentz-invariant 2D QFTs."),
]


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    labels = {r[0]: r[1] for r in cur.execute("SELECT id, title FROM entries")}

    inserted = 0
    for src, tgt, lt, tier, desc in LINKS:
        src_label = labels.get(src, src)
        tgt_label = labels.get(tgt, tgt)
        cur.execute(
            "INSERT OR IGNORE INTO links "
            "(link_type, source_id, source_label, target_id, target_label, "
            "description, link_order, confidence_tier) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (lt, src, src_label, tgt, tgt_label, desc, 0, tier)
        )
        if cur.rowcount > 0:
            print(f"  {src} -> {tgt} ({lt})")
            inserted += 1
        else:
            print(f"  SKIP (exists): {src} -> {tgt}")

    conn.commit()
    conn.close()
    print(f"\nInserted {inserted} FL<-physics bridge links.")


if __name__ == "__main__":
    print(f"Building FL<-physics bridges in:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
