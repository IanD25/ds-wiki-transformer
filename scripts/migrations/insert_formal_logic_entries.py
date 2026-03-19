"""
Formal Logic (FL) Entry Series — 22 entries
Inserts FL1–FL22 into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Batch 1 (FL1–FL7):  Foundations + PL Basics
Batch 2 (FL8–FL14): PL Metatheory + Natural Deduction
Batch 3 (FL15–FL22): QL + Metatheory + Extensions
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── BATCH 1: FOUNDATIONS + PL BASICS ─────────────────────────────────────

{
    "id": "FL1",
    "title": "Deductive Validity",
    "filename": "FL1_deductive_validity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "An argument is deductively valid if and only if there is no possible situation in which all premises are true and the conclusion is false. Validity is a purely formal property: it concerns the structure of inference, not the subject matter or factual truth of the claims involved. A valid argument transmits truth from premises to conclusion necessarily — if the premises hold, the conclusion cannot fail to hold. Validity does not require that the premises actually be true."),
        ("Mathematical Form", 1, "P₁, ..., Pₙ ⊨ C iff every valuation v satisfying all Pᵢ also satisfies C. Equivalently: the set {P₁, ..., Pₙ, ¬C} is unsatisfiable — no valuation makes all premises true and the conclusion false simultaneously. In propositional logic this is decidable by truth table; in first-order logic it is semidecidable."),
        ("Constraint Category", 2, "Informatic (In): deductive validity is a truth-preservation constraint — it guarantees that truth cannot be lost in passing from premises to conclusion. The constraint is modal: no possible world, model, or valuation constitutes a counterexample. This places validity among universal conservation laws: whatever logical structure the premises commit you to, the conclusion inherits unconditionally."),
        ("DS Cross-References", 3, "MATH4 (Gödel's Incompleteness Theorems): validity is precisely what incompleteness constrains — some true statements escape the reach of valid derivation from any consistent axiom set. FL5 (Propositional Logic): in PL, validity is fully decidable by truth table exhaustion, making it the tractable base case. FL3 (Logical Form and Topic Neutrality): validity is defined entirely by the form of the argument — substituting non-logical vocabulary preserves or destroys validity only through structural changes."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nValidity is the logical analog of a conservation principle: truth is the conserved quantity, and valid inference is the process that guarantees its conservation. Just as energy cannot be created or destroyed in a closed system, truth cannot be destroyed in a valid argument — if it enters via the premises, it must exit via the conclusion."),
        ("What The Math Says", 5, "The semantic definition ⊨ captures validity as a universal quantification over all models or valuations. For propositional logic, this quantification is finite and exhaustive — a truth table with 2ⁿ rows for n atomic variables settles the question mechanically. For first-order logic, the space of models is infinite, so validity is not decidable in general, though it is semidecidable: a proof will eventually be found if one exists, but no algorithm terminates on all invalid arguments. The equivalence of P₁,...,Pₙ ⊨ C with the unsatisfiability of {P₁,...,Pₙ, ¬C} transforms validity checking into satisfiability checking — the basis of modern SAT solving and automated theorem proving."),
        ("Concept Tags", 6, "• deductive validity\n• truth preservation\n• semantic entailment\n• models and valuations\n• logical necessity\n• formal inference\n• unsatisfiability\n• propositional logic\n• first-order logic\n• conservation of truth"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "deductive validity, truth preservation, semantic entailment, models and valuations, logical necessity, formal inference, unsatisfiability, propositional logic, first-order logic, conservation of truth", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("couples to", "FL1", "Deductive Validity", "MATH4", "Gödel's Incompleteness Theorems", "Gödel's incompleteness theorems directly constrain the reach of deductive validity: in any sufficiently expressive consistent formal system, there exist true statements for which no valid derivation from the axioms exists. Validity defines the boundary of what formal proof can accomplish; incompleteness shows that boundary is strictly inside the boundary of truth."),
        ("derives from", "FL1", "Deductive Validity", "FL3", "Logical Form and Topic Neutrality", "Validity and logical form are co-defined: an argument is valid because of its form, and logical form is precisely the structure that determines validity. Topic neutrality confirms that validity is structural, not material — swapping non-logical vocabulary cannot affect whether the argument is valid."),
        ("implements", "FL1", "Deductive Validity", "FL5", "Propositional Logic (PL)", "Propositional logic is the simplest formal system in which deductive validity is defined and fully decidable. PL provides the truth-table semantics that makes validity checkable by exhaustive enumeration, grounding the abstract definition in a concrete, tractable calculus."),
    ],
},

{
    "id": "FL2",
    "title": "Soundness of Arguments",
    "filename": "FL2_soundness_of_arguments.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "An argument is sound if and only if it is both deductively valid and all of its premises are actually true. Soundness is the stronger standard: validity guarantees truth transmission conditionally, but soundness guarantees that the conclusion is in fact true. A sound argument cannot have a false conclusion. Soundness thus combines formal correctness with material truth, making it the criterion by which valid reasoning establishes genuine knowledge rather than merely hypothetical entailment."),
        ("Mathematical Form", 1, "Sound(arg) iff Valid(arg) ∧ True(P₁) ∧ True(P₂) ∧ ... ∧ True(Pₙ). Since Valid(arg) means P₁,...,Pₙ ⊨ C, and all Pᵢ are true, it follows that True(C). Soundness is a conjunction: formal structure plus material content. Neither condition alone suffices."),
        ("Constraint Category", 2, "Informatic (In): soundness is a joint constraint — a structural constraint (validity) composed with an empirical constraint (truth of premises). The structural constraint is verifiable by logic alone; the material constraint requires knowledge of the world or of the axiomatic system in use. In formal systems, metatheoretic soundness asserts that the proof system does not prove falsehoods — a distinct, stronger sense addressed in FL15."),
        ("DS Cross-References", 3, "FL1 (Deductive Validity): soundness requires validity as the formal component. FL3 (Logical Form and Topic Neutrality): while validity is purely formal, soundness is not — the truth of premises is a matter of content, illustrating the form/content distinction. FL15 (Metatheoretic Soundness): the same word 'soundness' applies to proof systems (no false theorems are provable), which is a structurally analogous conservation claim at a different level."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nSoundness extends the truth-conservation guarantee of validity by adding the requirement that truth actually enters the system through the premises. Validity conserves truth if present; soundness ensures it is present. The combination is a closed conservation chain: truth in (true premises) + no loss (validity) = truth out (true conclusion)."),
        ("What The Math Says", 5, "Sound(arg) iff Valid(arg) ∧ ⋀ᵢ True(Pᵢ) encodes a two-stage guarantee. First, validity is checked formally — can the conclusion fail given the premises? Second, the premises are checked materially — do they actually obtain? If both hold, the conclusion must be true. This architecture reveals why invalid arguments with true premises prove nothing, and why valid arguments with false premises can reach false conclusions. The only leak-proof path to a guaranteed-true conclusion runs through both gates simultaneously."),
        ("Concept Tags", 6, "• soundness\n• deductive validity\n• true premises\n• guaranteed true conclusion\n• material truth\n• formal correctness\n• argument evaluation\n• knowledge from argument\n• metatheory\n• logic and epistemology"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "soundness, deductive validity, true premises, guaranteed true conclusion, material truth, formal correctness, argument evaluation, knowledge from argument, metatheory, logic and epistemology", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL2", "Soundness of Arguments", "FL1", "Deductive Validity", "Soundness is definitionally built on validity: a sound argument must first be valid. Without validity, true premises cannot guarantee a true conclusion; without true premises, validity produces only conditional entailment. Soundness is the conjunction that closes the gap between formal and material correctness."),
        ("analogous to", "FL2", "Soundness of Arguments", "FL15", "PL Metatheory (Soundness and Completeness)", "Both uses of 'soundness' express a conservation principle: argument soundness says no valid argument from true premises reaches a false conclusion; metatheoretic soundness says no proof system derives a false formula. The structural parallel is exact — truth enters the system and the system guarantees not to corrupt it — but the domains differ."),
        ("couples to", "FL2", "Soundness of Arguments", "FL3", "Logical Form and Topic Neutrality", "Soundness and logical form operate at different levels: logical form determines validity (topic-neutral); truth of premises determines whether the valid form actually produces a true conclusion (topic-specific). Soundness is where formal and material intersect."),
    ],
},

{
    "id": "FL3",
    "title": "Logical Form and Topic Neutrality",
    "filename": "FL3_logical_form_topic_neutrality.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "The validity of a deductive argument depends solely on its logical form — the pattern of logical constants and structural relations — and not on the specific subject matter of its non-logical terms. Replacing non-logical vocabulary with variables preserves validity or invalidity. Logic is therefore domain-independent: the same inferential forms are valid in mathematics, physics, biology, and everyday reasoning alike. This topic neutrality distinguishes logic from any particular science."),
        ("Mathematical Form", 1, "Schematize an argument by replacing each non-logical term with a variable of appropriate type (propositional, individual, predicate). A form Φ is logically valid iff every uniform substitution instance is valid — iff every interpretation of the variables satisfying the premises satisfies the conclusion. Invalid forms admit at least one substitution instance with true premises and false conclusion."),
        ("Constraint Category", 2, "Informatic (In): topic neutrality is a universality constraint — logical validity is invariant under domain substitution. Logical laws function as domain-free conservation laws: they hold in any universe of discourse, under any interpretation of non-logical terms. A statement is a logical truth iff it is true under all interpretations, not just the intended one."),
        ("DS Cross-References", 3, "Foundational to FL1 (Deductive Validity): validity is defined by form, making FL3 the conceptual basis for FL1's semantic definition. Enables FL4 (Counterexample Method): a single substitution instance with true premises and false conclusion refutes the whole form. Connects to CS1 (Church-Turing Thesis): Church-Turing achieves a similar universality — a model-independent characterization of computation that parallels logic's substrate-independence."),
        ("Mathematical Archetype", 4, "Mathematical archetype: symmetry-conservation\n\nTopic neutrality is a symmetry of logical form under substitution of non-logical vocabulary: the validity-value is conserved across this substitution group. Just as physical laws conserve quantities under symmetry transformations, logical validity is conserved under all uniform substitutions of non-logical terms."),
        ("What The Math Says", 5, "The schematization operation strips an argument of its specific content and reveals the underlying inferential skeleton. When we replace 'Socrates' with x, 'is mortal' with P, and 'is human' with Q, the argument becomes the universally valid schema ∀x(Qx→Px), Qa ⊨ Pa. The substitution group is all interpretations of individual constants and predicates over any non-empty domain. Tarski's definition of logical truth as truth-in-all-models is the mathematical codification: a logical truth holds because of form alone, not because of how the world happens to be."),
        ("Concept Tags", 6, "• logical form\n• topic neutrality\n• schematization\n• substitution invariance\n• domain independence\n• logical constants\n• model theory\n• logical truth\n• universality of logic\n• Tarski semantics"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "logical form, topic neutrality, schematization, substitution invariance, domain independence, logical constants, model theory, logical truth, universality of logic, Tarski semantics", 0),
        ("DS Facets", "mathematical_archetype", "symmetry-conservation", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL3", "Logical Form and Topic Neutrality", "FL1", "Deductive Validity", "Validity is defined as holding across all interpretations of non-logical terms — which is precisely the statement that validity depends on form alone. FL3 provides the philosophical and mathematical basis for FL1's universal quantification over valuations or models."),
        ("implements", "FL3", "Logical Form and Topic Neutrality", "FL4", "The Counterexample Method", "The counterexample method exploits topic neutrality directly: to show an argument form is invalid, it suffices to find one substitution instance where premises are true and conclusion is false. Topic neutrality guarantees that this one instance is sufficient to refute the general form."),
        ("analogous to", "FL3", "Logical Form and Topic Neutrality", "CS1", "Church-Turing Thesis", "Both assert domain-independence: logical validity holds across all interpretations of non-logical vocabulary, while computability holds across all physically realizable computational models. In both cases, a formal notion is shown to be substrate-independent, yielding a universal characterization."),
    ],
},

{
    "id": "FL4",
    "title": "The Counterexample Method",
    "filename": "FL4_counterexample_method.md",
    "entry_type": "method",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "The counterexample method demonstrates that an argument form is invalid by exhibiting a single interpretation in which all premises are true and the conclusion is false. Because validity requires truth-preservation across all interpretations, a single failure refutes the universal claim. The method is constructive: it produces explicit evidence of invalidity. One counterexample suffices."),
        ("Mathematical Form", 1, "To show P₁,...,Pₙ ⊭ C: exhibit a valuation v (for PL) or a model M (for QL) such that v(Pᵢ)=T for all i and v(C)=F. For propositional logic: find a truth-table row with all premises true and conclusion false. For predicate logic: specify a domain D with interpretations of predicates and constants such that all Pᵢ evaluate to true and C to false."),
        ("Constraint Category", 2, "Informatic (In): the counterexample method is a falsification procedure operating on the universal claim that every interpretation satisfying the premises satisfies the conclusion. It exploits the logical principle that a universal statement is refuted by a single counterinstance. Existence of a counterexample is equivalent to satisfiability of {P₁,...,Pₙ, ¬C}."),
        ("DS Cross-References", 3, "Implements FL1 (Deductive Validity): the method tests the definition directly by searching for the valuation or model that would make validity fail. Uses FL3 (Topic Neutrality): topic neutrality makes the method possible — a single substitution instance suffices because validity does not depend on the domain chosen. Connects to FL6 (Truth-Functionality): propositional counterexamples are truth-value assignments determined by the valuation framework."),
        ("Mathematical Archetype", 4, "Mathematical archetype: optimization-principle\n\nThe counterexample method minimizes the cost of establishing invalidity: instead of checking all interpretations, it searches for the single cheapest witness to failure. The method implements the asymmetry between verification (must check all cases) and falsification (one case suffices)."),
        ("What The Math Says", 5, "For propositional logic, the counterexample search is equivalent to satisfiability of a Boolean formula — specifically P₁ ∧ ... ∧ Pₙ ∧ ¬C. SAT solvers implement this at scale. For predicate logic, the search requires model construction: specifying a universe of discourse and an interpretation function. Löwenheim-Skolem guarantees that if a satisfiable first-order sentence has any model, it has a countable model. The compactness theorem implies that if every finite subset of {P₁,...,Pₙ,¬C} is satisfiable, the whole set is — meaning infinitely many premises can sometimes be defeated by finite counterexamples."),
        ("Concept Tags", 6, "• counterexample\n• invalidity\n• falsification\n• truth-value assignment\n• model construction\n• SAT solving\n• propositional logic\n• predicate logic\n• Löwenheim-Skolem\n• falsifiability"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "counterexample, invalidity, falsification, truth-value assignment, model construction, SAT solving, propositional logic, predicate logic, Löwenheim-Skolem, falsifiability", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "FL4", "The Counterexample Method", "FL1", "Deductive Validity", "The counterexample method implements the negation of the validity definition: FL1 defines validity as no interpretation making premises true and conclusion false; FL4 operationalizes invalidity by constructing exactly such an interpretation."),
        ("derives from", "FL4", "The Counterexample Method", "FL3", "Logical Form and Topic Neutrality", "The counterexample method works because of topic neutrality: since validity requires holding for all substitutions, any single substitution that fails constitutes a refutation of the form."),
        ("derives from", "FL4", "The Counterexample Method", "FL6", "Truth-Functionality and Valuations", "Propositional counterexamples are constructed by specifying truth-value assignments to atoms and computing compound values by truth-functionality. FL6 guarantees this computation is deterministic and complete."),
    ],
},

{
    "id": "FL5",
    "title": "Propositional Logic (PL)",
    "filename": "FL5_propositional_logic.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Propositional logic is the truth-functional calculus over atomic propositions connected by the logical connectives ¬, ∧, ∨, →, ↔. It is the foundational fragment of formal logic: decidable, sound, and complete. Every formula has a determinate truth value under any valuation of its atomic components, and every tautology is provable. PL captures the Boolean structure of reasoning and serves as the base layer on which all richer logics are built."),
        ("Mathematical Form", 1, "Syntax: atoms p, q, r ∈ Atoms; formulas built by ¬A, A∧B, A∨B, A→B, A↔B. Semantics: valuation v: Atoms→{T,F} extended to all formulas by truth tables. A formula A is a tautology iff v(A)=T for all v. Decidability: truth-table method runs in O(2ⁿ) for n atoms. Satisfiability is NP-complete (Cook-Levin)."),
        ("Constraint Category", 2, "Informatic (In): propositional logic is a maximal decidable fragment — it captures the full Boolean structure of truth-functional reasoning while remaining algorithmically tractable. Every question about propositional entailment is in principle mechanically resolvable. This decidability distinguishes PL sharply from first-order logic, where entailment is only semidecidable."),
        ("DS Cross-References", 3, "FL6 (Truth-Functionality): PL is the canonical truth-functional logic; FL6 articulates the semantic principle that makes PL work. FL7 (Expressive Adequacy): which connective sets express all PL truth functions — a question arising within PL. FL16 (Quantificational Logic): predicate logic extends PL by adding quantifiers ∀ and ∃, inheriting PL's connectives while losing decidability. CS4 (Cook-Levin): propositional satisfiability (SAT) is the canonical NP-complete problem."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nPropositional logic enforces the conservation of Boolean truth values through the connective operations: the truth value of a compound formula is fully determined by and conserved from the truth values of its components via truth-table rules. No information about truth values is created or destroyed in the composition process."),
        ("What The Math Says", 5, "The completeness theorem for PL (Post 1921) states that every tautology is provable in any sound proof system for PL, and every provable formula is a tautology. Proof-theoretic and semantic notions of logical truth coincide exactly — a harmony that breaks down in first-order logic (Gödel: syntactically complete systems are impossible for arithmetic). The compactness theorem for PL follows from König's lemma: if every finite subset of a set Γ of formulas is satisfiable, then Γ itself is satisfiable."),
        ("Concept Tags", 6, "• propositional logic\n• truth-functional calculus\n• Boolean algebra\n• decidability\n• completeness\n• satisfiability\n• tautology\n• truth tables\n• logical connectives\n• NP-completeness"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "propositional logic, truth-functional calculus, Boolean algebra, decidability, completeness, satisfiability, tautology, truth tables, logical connectives, NP-completeness", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL5", "Propositional Logic (PL)", "FL6", "Truth-Functionality and Valuations", "PL is grounded in truth-functionality: its semantics is entirely defined by truth-table rules for the connectives. Without truth-functionality, valuations could not be extended from atoms to complex formulas, and PL's decidability would be unavailable."),
        ("generalizes", "FL16", "Quantificational Logic (First-Order)", "FL5", "Propositional Logic (PL)", "Predicate logic extends propositional logic by adding quantifiers ∀ and ∃ and a domain of individuals. PL is the base layer: all connective apparatus is inherited by QL, and every propositional tautology remains a theorem of QL. The extension is conservative."),
        ("analogous to", "FL5", "Propositional Logic (PL)", "CS4", "Cook-Levin Theorem — NP-Completeness", "Propositional satisfiability (SAT) is the canonical NP-complete problem (Cook 1971). The complexity of PL reasoning — polynomial to verify, exponential to decide in the worst case — is the foundational result linking propositional logic to computational complexity theory."),
    ],
},

{
    "id": "FL6",
    "title": "Truth-Functionality and Valuations",
    "filename": "FL6_truth_functionality_valuations.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "A logical connective is truth-functional if and only if the truth value of the compound formula it forms is determined entirely by the truth values of its immediate components — with no dependence on meanings, modal status, or epistemic properties. A valuation is a function from atomic propositions to {T,F} that extends to all compound formulas by applying the truth-table rules for each connective. This compositional determination enables mechanical evaluation and is the basis for decidability of propositional logic."),
        ("Mathematical Form", 1, "v: Atoms→{T,F} extended compositionally: v(¬A)=T iff v(A)=F. v(A∧B)=T iff v(A)=T and v(B)=T. v(A∨B)=T iff v(A)=T or v(B)=T. v(A→B)=F iff v(A)=T and v(B)=F. v(A↔B)=T iff v(A)=v(B). Each binary connective defines a function {T,F}²→{T,F}; there are exactly 2⁴=16 such functions."),
        ("Constraint Category", 2, "Informatic (In): truth-functionality is a compositionality constraint — the semantic value of a compound is a function of and only of the semantic values of its parts. This is the Boolean special case of the Fregean principle of compositionality. It rules out connectives whose output depends on the manner, context, or reason for the truth of their inputs."),
        ("DS Cross-References", 3, "Foundational to FL5 (Propositional Logic): truth-functionality constitutes PL — without it, truth-table evaluation and decidability would be unavailable. Foundational to FL7 (Expressive Adequacy): functional completeness of a connective set only makes sense given truth-functional connectives. Connects to INFO1 (Shannon Entropy): valuations are complete Boolean state descriptions — a valuation over n atoms specifies one of 2ⁿ possible states, the exact state space over which Shannon entropy is computed."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nTruth-functionality enforces the conservation of semantic determination: the truth value of a compound formula is conserved from — fully determined by — the truth values of its components, with no injection of new semantic content at the connective step. The composition of truth-functions is itself a truth-function."),
        ("What The Math Says", 5, "The 16 binary truth-functional connectives correspond to the 16 Boolean functions {T,F}²→{T,F}. Post's lattice theorem classifies all sets of Boolean functions by closure under composition, identifying which sets are functionally complete. The connection to Shannon information is precise: a valuation over n atoms specifies one of 2ⁿ equally possible Boolean states; Shannon entropy H = −∑pᵢ log pᵢ measures uncertainty over this state space. Perfect knowledge (a single true valuation) gives H=0; maximum uncertainty gives H=n bits."),
        ("Concept Tags", 6, "• truth-functionality\n• valuation\n• Boolean functions\n• compositionality\n• truth tables\n• semantic determination\n• propositional semantics\n• functional completeness\n• intensional vs extensional\n• Boolean information"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "truth-functionality, valuation, Boolean functions, compositionality, truth tables, semantic determination, propositional semantics, functional completeness, intensional vs extensional, Boolean information", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "FL6", "Truth-Functionality and Valuations", "FL5", "Propositional Logic (PL)", "Truth-functionality is the constitutive semantic principle of PL: FL5 is the system in which all connectives are truth-functional, and FL6 articulates the rule that makes FL5's semantics work."),
        ("derives from", "FL7", "Expressive Adequacy", "FL6", "Truth-Functionality and Valuations", "Expressive adequacy asks whether a given set of truth-functions can generate all others by composition. This question is posed entirely within the truth-functional framework FL6 establishes."),
        ("analogous to", "FL6", "Truth-Functionality and Valuations", "INFO1", "Shannon Entropy", "Valuations and Shannon entropy inhabit the same Boolean state space. A valuation over n atoms picks out one of 2ⁿ Boolean states; Shannon entropy measures uncertainty over the same state space. The formal connection runs through Boolean algebras and discrete information theory."),
    ],
},

{
    "id": "FL7",
    "title": "Expressive Adequacy",
    "filename": "FL7_expressive_adequacy.md",
    "entry_type": "theorem",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "A set of Boolean connectives is expressively adequate (functionally complete) if and only if every truth function can be defined by a formula using only connectives from that set. The standard sets {¬,∧} and {¬,∨} are each adequate; NAND (Sheffer stroke ↑) and NOR (↓) are each individually adequate, each constituting a single-connective complete basis. Expressive adequacy characterizes the minimal logical resources required to express all possible Boolean conditions."),
        ("Mathematical Form", 1, "There are 2^(2^n) distinct n-ary truth functions. A set S of connectives is adequate iff every n-ary truth function is representable as a composition of connectives from S. Post's completeness theorem (1941): S is adequate iff S is not contained in any of the five maximal clones (T₀, T₁, S, M, D — preserving false, preserving true, self-dual, monotone, affine respectively)."),
        ("Constraint Category", 2, "Informatic (In): expressive adequacy is a completeness constraint on representational capacity — an adequate set of connectives leaves no Boolean condition unexpressible. Post's lattice classifies all clones of Boolean functions, giving a complete map of expressibility. Inadequacy means the language has a representational gap."),
        ("DS Cross-References", 3, "Arises within FL5 (Propositional Logic): expressive adequacy asks which subsets of PL's connectives suffice to express all of PL's expressible conditions. Grounded in FL6 (Truth-Functionality): functional completeness only makes sense for truth-functional connectives. Connects to CS1 (Church-Turing Thesis): functional completeness of a Boolean basis parallels computational completeness of a universal Turing machine — minimal operations suffice to simulate the entire class."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nExpressive adequacy asserts the conservation of representational power across a change of basis: switching from the full connective set to an adequate subset loses no expressible Boolean condition. The adequacy threshold is a phase boundary — adequate sets are above it, inadequate sets below."),
        ("What The Math Says", 5, "Post's completeness theorem provides the definitive analysis. The five maximal clones — functions preserving 0, preserving 1, self-dual, monotone, and linear over GF(2) — are the only obstacles to functional completeness. NAND is adequate because it is not monotone (NAND(1,1)=0), not self-dual, not linear, and does not preserve either constant. The result connects to circuit complexity — adequate bases correspond to universal gate sets, and circuit depth depends on the choice of basis. In quantum computing, the Solovay-Kitaev theorem characterizes universal gate sets for unitary operators."),
        ("Concept Tags", 6, "• expressive adequacy\n• functional completeness\n• Post's completeness theorem\n• Boolean clones\n• NAND\n• NOR\n• Sheffer stroke\n• universal gate set\n• Post's lattice\n• circuit complexity"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "expressive adequacy, functional completeness, Post's completeness theorem, Boolean clones, NAND, NOR, Sheffer stroke, universal gate set, Post's lattice, circuit complexity", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL7", "Expressive Adequacy", "FL5", "Propositional Logic (PL)", "Expressive adequacy is a theorem about PL's connective vocabulary: it asks which subsets suffice to express all Boolean conditions PL can express. FL5 is the containing system; FL7 characterizes its redundancy structure."),
        ("derives from", "FL7", "Expressive Adequacy", "FL6", "Truth-Functionality and Valuations", "Post's theorem is stated within the truth-functional framework: truth functions as {T,F}ⁿ→{T,F}, and completeness as closure under composition. Without FL6's framework, the notion of an adequate connective set would be undefined."),
        ("analogous to", "FL7", "Expressive Adequacy", "CS1", "Church-Turing Thesis", "Functional completeness of a Boolean connective set parallels computational completeness: a minimal set of operations suffices to simulate all operations in the class. NAND's individual adequacy is the Boolean analog of the universality of the universal Turing machine."),
    ],
},

# ── BATCH 2: PL METATHEORY + NATURAL DEDUCTION ───────────────────────────

{
    "id": "FL8",
    "title": "Tautology and Contradiction",
    "filename": "FL8_tautology_and_contradiction.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "A propositional formula is a tautology if and only if it is true under every possible truth-value assignment to its atomic variables. A contradiction is false under every such assignment. A contingency is neither. Tautologies are necessarily true by logical form alone, independent of empirical content. Whether any PL formula is a tautology is decidable: enumerate all 2^n valuations via truth table and verify."),
        ("Mathematical Form", 1, "⊨ A means: for every valuation v, v(A) = T. A is a contradiction iff ⊨ ¬A. A is a contingency iff neither ⊨ A nor ⊨ ¬A. Classical examples: ⊨ (A ∨ ¬A) (excluded middle), ⊨ (A → A). Contradictions: A ∧ ¬A. Decision: O(2^n) truth-table rows for n atoms."),
        ("Constraint Category", 2, "Informatic (In): tautologies represent the zero-information boundary — true regardless of how the world is. Contradictions represent maximal inconsistency — rule out every possible state. Between them, contingencies carry genuine content. This trichotomy partitions all propositional formulas and underpins logical necessity versus contingency."),
        ("DS Cross-References", 3, "FL9 (Tautological Entailment) defines entailment via tautologies: A1,...,An ⊨ B iff (A1 ∧ … ∧ An) → B is a tautology. FL5 (PL) identifies tautologies as exactly the theorems derivable from PL axioms. MATH4 (Gödel) highlights PL's exceptionality: in richer logics, truth outruns provability, but in PL the two coincide."),
        ("Mathematical Archetype", 4, "Mathematical archetype: threshold-transition\n\nThe tautology/contingency/contradiction trichotomy defines sharp boundaries — a formula either clears the tautology threshold (true everywhere) or falls below. No gradation within classical PL. This mirrors threshold phenomena where a system transitions discontinuously between qualitatively distinct regimes."),
        ("What The Math Says", 5, "The truth-table decision procedure is complete and sound: a formula receives T in every row if and only if it is a tautology. The procedure is co-NP-complete — verifying a non-tautology requires only one falsifying row, but confirming a tautology requires exhaustive enumeration. The structural duality between tautologies and contradictions (A is a tautology iff ¬A is a contradiction) means every tautology checker doubles as a contradiction checker under negation."),
        ("Concept Tags", 6, "• tautology\n• contradiction\n• contingency\n• truth-value assignment\n• semantic necessity\n• propositional logic\n• truth table\n• decidability\n• logical form\n• classical logic"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "tautology, contradiction, contingency, truth-value assignment, semantic necessity, propositional logic, truth table, decidability, logical form, classical logic", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL8", "Tautology and Contradiction", "FL9", "Tautological Entailment", "Tautological entailment is defined via tautologies: A1,...,An ⊨ B iff (A1 ∧ … ∧ An) → B is a tautology. FL9 inherits the decidability and threshold structure of FL8's tautology concept."),
        ("couples to", "FL8", "Tautology and Contradiction", "FL5", "Propositional Logic (PL)", "Tautologies are exactly the theorems of PL — coupling FL8's semantic all-valuations-true criterion with FL5's syntactic derivability relation via the soundness/completeness metatheorem."),
        ("analogous to", "FL8", "Tautology and Contradiction", "MATH4", "Gödel's Incompleteness Theorems", "In PL, every tautology is provable and vice versa — truth and proof coincide. Gödel shows this fails in systems encoding arithmetic: there exist true unprovable sentences. PL's tautology decidability is an instructive contrast for understanding incompleteness."),
    ],
},

{
    "id": "FL9",
    "title": "Tautological Entailment",
    "filename": "FL9_tautological_entailment.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "A set of propositional formulas {A1, …, An} tautologically entails B if and only if every truth-value assignment making all Ai true also makes B true. Written A1, …, An ⊨ B. This is semantic consequence in propositional logic — the formal foundation of deductive reasoning. Tautological entailment is decidable by truth table and captures the notion that the truth of premises forces the truth of the conclusion by logical form alone."),
        ("Mathematical Form", 1, "A1, …, An ⊨ B iff for every valuation v: if v(A1)=T and … and v(An)=T, then v(B)=T. Equivalently: ⊨ (A1 ∧ … ∧ An) → B. Special case: ∅ ⊨ B iff ⊨ B (B is a tautology). Decision: 2^k rows where k is the number of distinct atoms. Monotonicity: if Γ ⊨ B then Γ∪Δ ⊨ B."),
        ("Constraint Category", 2, "Informatic (In): tautological entailment is a truth-preservation constraint — truth is conserved from premises to conclusion under every valuation. No counter-model exists. This conservation structure makes deductive inference non-ampliative: the conclusion is already implicit in the premises."),
        ("DS Cross-References", 3, "FL1 (Validity) specializes entailment to the argument form: an argument is valid iff its premises tautologically entail its conclusion. FL8 (Tautologies) provides the equivalent reformulation: entailment reduces to tautologyhood of a conditional. FL15 (Soundness and Completeness) establishes the syntactic counterpart: ⊨ and ⊢ coincide in PL."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nTautological entailment is a strict truth-conservation law. Wherever the premises hold, the conclusion holds — no truth is lost and no falsehood is introduced. The semantic consequence relation is the logical analogue of a physical invariant."),
        ("What The Math Says", 5, "The reduction of entailment to tautology — A1,...,An ⊨ B iff ⊨ (A1 ∧ … ∧ An) → B — collapses the semantic consequence apparatus to a single decidable predicate. Monotonicity holds: adding premises never destroys entailment. Compactness holds: if Γ ⊨ B then some finite subset suffices. These structural properties distinguish classical entailment from non-monotonic and relevance-based consequence relations."),
        ("Concept Tags", 6, "• tautological entailment\n• semantic consequence\n• truth preservation\n• valuation\n• propositional logic\n• logical implication\n• decidability\n• monotonicity\n• compactness\n• deductive inference"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "tautological entailment, semantic consequence, truth preservation, valuation, propositional logic, logical implication, decidability, monotonicity, compactness, deductive inference", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL9", "Tautological Entailment", "FL1", "Deductive Validity", "Validity of an argument is exactly tautological entailment restricted to the finitely-premised form. FL1's criterion is a special application of FL9's semantic consequence relation."),
        ("couples to", "FL9", "Tautological Entailment", "FL8", "Tautology and Contradiction", "A1,...,An ⊨ B iff (A1 ∧ … ∧ An) → B is a tautology. Entailment and tautologyhood form a mutually defining pair at the semantic core of PL."),
        ("analogous to", "FL9", "Tautological Entailment", "FL15", "PL Metatheory (Soundness and Completeness)", "Soundness and completeness assert that ⊨ and ⊢ coincide in PL. FL15 validates proof systems as reliable instruments for computing the entailment relation defined in FL9."),
    ],
},

{
    "id": "FL10",
    "title": "The Material Conditional",
    "filename": "FL10_the_material_conditional.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "The material conditional A→B is false if and only if A is true and B is false; it is true in all other cases. This is the weakest truth-functional interpretation of 'if-then': it captures only the minimum logical content. A false antecedent makes any conditional vacuously true, producing the paradoxes of material implication. Despite these divergences from natural language, the material conditional is retained because it supports essential proof techniques and mathematical reasoning."),
        ("Mathematical Form", 1, "v(A→B) = F iff v(A)=T and v(B)=F; T otherwise. Equivalently: A→B ≡ ¬A ∨ B. Contrapositive: A→B ≡ ¬B→¬A. Truth table: TT→T, TF→F, FT→T, FF→T. Exportation: (A ∧ B)→C ≡ A→(B→C)."),
        ("Constraint Category", 2, "Informatic (In): the material conditional is a minimal-commitment conditional — it rules out only the one combination (true antecedent, false consequent) that would make 'if A then B' demonstrably false. This minimality makes the conditional maximally permissive while encoding the core logical asymmetry."),
        ("DS Cross-References", 3, "FL6 (Truth-Functionality): the conditional is defined solely by its truth table — v(A→B) depends only on v(A) and v(B). FL11 (Explosion): from A ∧ ¬A, the formula A→B is vacuously satisfied, enabling derivation of any B. FL22 (Intuitionistic Logic): rejects the classical equivalence A→B ≡ ¬A ∨ B because it rests on excluded middle."),
        ("Mathematical Archetype", 4, "Mathematical archetype: threshold-transition\n\nThe material conditional has a single critical threshold — v(A)=T, v(B)=F — that triggers falsehood. All other input combinations yield truth. This asymmetric one-failure-mode structure is a threshold phenomenon."),
        ("What The Math Says", 5, "The equivalence A→B ≡ ¬A ∨ B means every conditional in PL can be rewritten in terms of negation and disjunction — the conditional introduces no new expressive power beyond {¬, ∨}. This reduction enables normal-form transformations (CNF/DNF), resolution proofs, and satisfiability algorithms on minimal connective bases. The exportation law (A ∧ B)→C ≡ A→(B→C) is the propositional analogue of currying in lambda calculus, reflecting the Curry-Howard correspondence between material implication and function types."),
        ("Concept Tags", 6, "• material conditional\n• truth function\n• vacuous truth\n• antecedent\n• consequent\n• paradoxes of material implication\n• propositional logic\n• contrapositive\n• logical connective\n• exportation"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "material conditional, truth function, vacuous truth, antecedent, consequent, paradoxes of material implication, propositional logic, contrapositive, logical connective, exportation", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL10", "The Material Conditional", "FL6", "Truth-Functionality and Valuations", "The material conditional is defined as a truth function: its value is determined entirely by the values of its components. FL6 establishes the framework that legitimizes this definition."),
        ("couples to", "FL10", "The Material Conditional", "FL11", "Explosion and Absurdity (Ex Falso Quodlibet)", "Explosion depends on the material conditional: from A ∧ ¬A, A→B is vacuously true, and combined with A this yields B. The vacuous-truth behavior is precisely what paraconsistent logics target."),
        ("analogous to", "FL10", "The Material Conditional", "FL22", "Intuitionistic and Non-Classical Logics", "Intuitionistic logic replaces the classical conditional with a constructive one: A→B holds only if there is a method transforming any proof of A into a proof of B. This rejects A→B ≡ ¬A ∨ B."),
    ],
},

{
    "id": "FL11",
    "title": "Explosion and Absurdity (Ex Falso Quodlibet)",
    "filename": "FL11_explosion_and_absurdity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "From a contradiction — a formula and its negation both assumed true — any formula whatsoever can be derived. This is Ex Falso Quodlibet: a single inconsistency trivializes an entire formal system, making every formula a theorem. Classical and intuitionistic logic both accept explosion. Paraconsistent logics reject it, allowing localized inconsistencies without global collapse. Explosion is why consistency is the minimum requirement for any useful formal system."),
        ("Mathematical Form", 1, "A, ¬A ⊨ B for any formula B. Proof: (1) from A, derive A∨B by ∨-introduction; (2) from ¬A and A∨B, derive B by disjunctive syllogism. Also: ⊥ → B is a theorem for any B, where ⊥ denotes the canonical contradiction."),
        ("Constraint Category", 2, "Informatic (In): explosion is a catastrophic amplification constraint — inconsistency is not local damage but global annihilation of discriminating power. A system that proves both A and ¬A proves everything and distinguishes nothing. This is the logical analogue of maximum entropy: zero structure, no useful distinctions remaining."),
        ("DS Cross-References", 3, "FL14 (RAA) uses contradiction constructively: assume ¬A, derive contradiction, thereby prove A — harnessing explosion's premise without triggering its conclusion by discharging the assumption. MATH4 (Gödel): an inconsistent system proves everything via explosion, making consistency the precondition for meaningful formal reasoning. FL22 (Non-Classical Logics): paraconsistent logics reject explosion by restricting disjunctive syllogism or revising negation."),
        ("Mathematical Archetype", 4, "Mathematical archetype: threshold-transition\n\nExplosion is a catastrophic threshold — the moment a system crosses from consistent to inconsistent, it transitions discontinuously from well-behaved to trivial. Below the threshold, the system discriminates true from false; at the threshold, all discriminating power is lost. The inconsistency threshold is a point of no return in classical logic."),
        ("What The Math Says", 5, "The proof via disjunctive syllogism — from A, infer A∨B; from ¬A and A∨B, infer B — uses only two widely-accepted rules. Paraconsistent logics must reject at least one: disjunctive syllogism, ∨-introduction in the context of negation, or classical negation semantics. The relevant logic tradition rejects that A∨B is relevant to ¬A; the dialethic tradition accepts true contradictions without accepting all consequences. The existence of alternatives demonstrates that explosion is a feature of classical negation, not a logical necessity."),
        ("Concept Tags", 6, "• explosion\n• ex falso quodlibet\n• contradiction\n• inconsistency\n• paraconsistent logic\n• disjunctive syllogism\n• classical logic\n• trivialization\n• absurdity\n• formal system collapse"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "explosion, ex falso quodlibet, contradiction, inconsistency, paraconsistent logic, disjunctive syllogism, classical logic, trivialization, absurdity, formal system collapse", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("couples to", "FL11", "Explosion and Absurdity (Ex Falso Quodlibet)", "FL14", "Reductio ad Absurdum and Conditional Proof", "RAA is a controlled use of explosion: a subproof assumes ¬A, derives a contradiction, then discharges ¬A to conclude A. RAA channels explosion's destructive power into a constructive conclusion by confining the contradiction within a closed subproof scope."),
        ("analogous to", "FL11", "Explosion and Absurdity (Ex Falso Quodlibet)", "MATH4", "Gödel's Incompleteness Theorems", "Gödel's second theorem shows a consistent system cannot prove its own consistency. The reason consistency matters is explosion: inconsistency trivially proves every formula. MATH4 and FL11 define the stakes — Gödel shows we cannot fully secure consistency from within; FL11 shows what happens if it fails."),
        ("couples to", "FL11", "Explosion and Absurdity (Ex Falso Quodlibet)", "FL22", "Intuitionistic and Non-Classical Logics", "Paraconsistent logics are defined by rejecting explosion. They accept that A and ¬A can coexist locally without all formulas becoming derivable. FL22's alternatives show explosion is a consequence of classical negation, not inevitable."),
    ],
},

{
    "id": "FL12",
    "title": "Natural Deduction (Fitch System)",
    "filename": "FL12_natural_deduction_fitch_system.md",
    "entry_type": "method",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Natural deduction is a proof system where reasoning proceeds through structured step-by-step sequences, each justified by an inference rule, with vertical scope lines tracking active assumptions. The Fitch-style presentation uses indentation and horizontal bars to mark subproof boundaries. No axioms are required: every proof begins from assumptions that can be discharged. Each logical connective has introduction and elimination rules, making the system modular."),
        ("Mathematical Form", 1, "A proof is a numbered sequence of lines. Each line contains: (i) a formula, (ii) a justification citing a rule name and line numbers, (iii) a scope depth determined by active indentation. Subproofs begin with an assumption line under a new scope bar. Core rules: ∧I, ∧E, ∨I, ∨E, →I (CP), →E (MP), ¬I (RAA), ¬E, ↔I, ↔E, Reit."),
        ("Constraint Category", 2, "Informatic (In): natural deduction is an optimization-principle method — it provides the most direct path from assumptions to conclusion by mirroring the structure of the target formula. A proof of A∧B naturally has two subgoals (prove A, prove B); a proof of A→B uses a CP subproof. The method encodes the logical structure of the conclusion in the proof architecture."),
        ("DS Cross-References", 3, "FL13 (Modus Ponens and Core Rules) defines the rules that populate proofs. FL14 (RAA and Conditional Proof) provides the two subproof strategies. FL15 (Soundness and Completeness) guarantees the system is truth-preserving and derives every PL tautology, validating it as a faithful instrument for tautological entailment."),
        ("Mathematical Archetype", 4, "Mathematical archetype: optimization-principle\n\nThe Fitch system is designed so the shortest proof corresponds to the most direct logical path — introduction rules build toward the goal; elimination rules decompose premises. The subproof mechanism localizes assumptions, preventing global contamination, analogous to local variable scoping."),
        ("What The Math Says", 5, "Natural deduction was introduced by Gentzen (1935) as a formalization of how mathematicians actually reason. The key metatheoretic result is the normalization theorem: every proof can be reduced to normal form with no detour inferences (no formula introduced and immediately eliminated). Normal proofs correspond to cut-free proofs in sequent calculus. The Curry-Howard correspondence maps natural deduction proofs to typed lambda calculus terms — proofs are programs, propositions are types."),
        ("Concept Tags", 6, "• natural deduction\n• Fitch system\n• subproof\n• scope line\n• assumption discharge\n• introduction rule\n• elimination rule\n• proof system\n• normalization\n• Curry-Howard correspondence"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "natural deduction, Fitch system, subproof, scope line, assumption discharge, introduction rule, elimination rule, proof system, normalization, Curry-Howard correspondence", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "FL12", "Natural Deduction (Fitch System)", "FL13", "Modus Ponens and Core Inference Rules", "The Fitch system is the proof-mechanical framework; FL13's rules are its operational content. The scope lines define where rules apply; the rules determine what can be written at each line."),
        ("implements", "FL12", "Natural Deduction (Fitch System)", "FL14", "Reductio ad Absurdum and Conditional Proof", "RAA and CP are the two subproof strategies that give natural deduction its power for negation and conditionals. The Fitch subproof mechanism is precisely the syntactic structure designed to host these strategies."),
        ("couples to", "FL12", "Natural Deduction (Fitch System)", "FL15", "PL Metatheory (Soundness and Completeness)", "Soundness ensures every Fitch proof preserves truth; completeness ensures every valid argument has a Fitch proof. Together, FL15 validates FL12 as a complete and reliable instrument for the semantic consequence relation."),
    ],
},

{
    "id": "FL13",
    "title": "Modus Ponens and Core Inference Rules",
    "filename": "FL13_modus_ponens_core_rules.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Modus ponens is the fundamental inference rule: from A and A→B, derive B. It is the elimination rule for the conditional. Beyond modus ponens, the core rule set includes conjunction introduction/elimination, disjunction introduction/elimination, biconditional introduction/elimination, and reiteration. Each rule is locally truth-preserving: applying any rule to true premises always yields a true conclusion."),
        ("Mathematical Form", 1, "→E (MP): A, A→B / B. ∧I: A, B / A∧B. ∧E: A∧B / A; A∧B / B. ∨I: A / A∨B. ∨E: A∨B, [A]⊢C, [B]⊢C / C. ↔I: [A]⊢B, [B]⊢A / A↔B. ↔E: A↔B, A / B. Reit: A / A (copies accessible formula into current scope)."),
        ("Constraint Category", 2, "Informatic (In): each core rule is a local conservation law — truth is preserved from inputs to output at every single inference step. This locality means proof checking is modular: verifying each line individually against its cited rule suffices. The conservation property accumulates over chains, guaranteeing any formula derived from true assumptions is itself true."),
        ("DS Cross-References", 3, "FL12 (Natural Deduction) provides the proof framework within which these rules operate. FL1 (Validity) is justified by the fact that each rule preserves truth. FL6 (Truth-Functionality) grounds each rule in its corresponding truth table: ∧E is valid because v(A∧B)=T implies v(A)=T, and so on."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nEach inference rule is a local truth-conservation law — truth flows from premises to conclusion without loss. The entire proof system is then a global conservation law by induction: truth conserved at every step means truth conserved across any finite proof."),
        ("What The Math Says", 5, "Modus ponens is the unique rule needed, together with a suitable axiom set, to derive all of classical PL (Hilbert-style completeness). In natural deduction, no axioms are needed but the rule set expands. The disjunction elimination rule (∨E) is the most complex: it requires two subproofs showing B follows from each disjunct, then concludes B from A∨B. This case-split is the formal analogue of proof by cases. The full rule set plus FL14's RAA and CP is functionally complete."),
        ("Concept Tags", 6, "• modus ponens\n• inference rule\n• arrow elimination\n• conjunction introduction\n• disjunction elimination\n• truth preservation\n• natural deduction\n• proof step\n• rule schema\n• case analysis"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "modus ponens, inference rule, arrow elimination, conjunction introduction, disjunction elimination, truth preservation, natural deduction, proof step, rule schema, case analysis", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("couples to", "FL13", "Modus Ponens and Core Inference Rules", "FL12", "Natural Deduction (Fitch System)", "The rules and the Fitch framework are mutually constitutive: rules define what moves are legal, the framework defines how moves are recorded and scoped."),
        ("derives from", "FL13", "Modus Ponens and Core Inference Rules", "FL1", "Deductive Validity", "The local truth-preservation of each rule is the mechanism by which FL1's validity is implemented in a proof system."),
        ("derives from", "FL13", "Modus Ponens and Core Inference Rules", "FL6", "Truth-Functionality and Valuations", "Every core rule is a direct read-off from the truth table of the connective it governs. ∧E is valid because v(A∧B)=T forces v(A)=T. →E is valid because v(A)=T and v(A→B)=T forces v(B)=T."),
    ],
},

{
    "id": "FL14",
    "title": "Reductio ad Absurdum and Conditional Proof",
    "filename": "FL14_reductio_conditional_proof.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Reductio ad absurdum (RAA) temporarily assumes the negation of the desired conclusion, derives a contradiction, and thereby establishes the conclusion. Conditional proof (CP) temporarily assumes the antecedent, derives the consequent, and thereby establishes the conditional. Both operate through subproofs: temporary assumptions are introduced, exploited, and discharged at the subproof's close, contributing a new formula to the enclosing proof."),
        ("Mathematical Form", 1, "RAA: open subproof assuming ¬A; derive ⊥ (or any B ∧ ¬B); close subproof; conclude A. CP: open subproof assuming A; derive B; close subproof; conclude A→B. In Fitch notation, the subproof is indented under a scope bar. Discharge means the assumption no longer appears in the undischarged assumption set of the enclosing context."),
        ("Constraint Category", 2, "Informatic (In): RAA and CP are assumption-discharge constraints governing the lifecycle of temporary assumptions. An assumption introduced in a subproof cannot be exported directly — it must be discharged via the closing rule. This prevents assumption leakage and makes subproof-based reasoning safe and modular."),
        ("DS Cross-References", 3, "FL12 (Fitch System) provides the syntactic subproof mechanism within which RAA and CP operate. FL11 (Explosion) motivates RAA: the strategy works because a contradiction is maximally destructive, and RAA channels that power constructively by containing it within a subproof. FL13 (Core Rules) supplies the inference steps used within subproofs."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nBoth RAA and CP conserve truth at the subproof level. CP: if A is assumed and B derived, then A→B is true unconditionally. RAA: if assuming ¬A leads to contradiction, then ¬A is false, so A is true. No truth-loss occurs when moving from subproof to enclosing context."),
        ("What The Math Says", 5, "Together, RAA and CP are sufficient to derive every classically valid formula when combined with FL13's core rules. CP is →-introduction; RAA is ¬-introduction. Without these, the rule set cannot introduce conditional or negation formulas from scratch. PL completeness (FL15) depends on having both. In intuitionistic logic, RAA is restricted: one may derive ¬¬A but not A directly, reflecting the constructive constraint that a proof of A must provide a witness."),
        ("Concept Tags", 6, "• reductio ad absurdum\n• conditional proof\n• assumption discharge\n• subproof\n• negation introduction\n• conditional introduction\n• proof by contradiction\n• Fitch system\n• classical logic\n• proof strategy"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "reductio ad absurdum, conditional proof, assumption discharge, subproof, negation introduction, conditional introduction, proof by contradiction, Fitch system, classical logic, proof strategy", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "FL14", "Reductio ad Absurdum and Conditional Proof", "FL12", "Natural Deduction (Fitch System)", "RAA and CP are the two subproof-closing rules that complete the Fitch rule set. The scope bars and assumption lines are designed specifically to support these strategies."),
        ("couples to", "FL14", "Reductio ad Absurdum and Conditional Proof", "FL11", "Explosion and Absurdity (Ex Falso Quodlibet)", "RAA is a controlled use of explosion: the contradiction is confined within a subproof and converted into a constructive conclusion before it escapes."),
        ("derives from", "FL14", "Reductio ad Absurdum and Conditional Proof", "FL13", "Modus Ponens and Core Inference Rules", "Within every RAA or CP subproof, the derivation proceeds by applying FL13's core rules — MP chains, conjunction introductions, disjunction eliminations. FL14 defines the opening and closing moves; FL13 defines all internal moves."),
    ],
},

# ── BATCH 3: QL + METATHEORY + EXTENSIONS ─────────────────────────────────

{
    "id": "FL15",
    "title": "PL Metatheory (Soundness and Completeness)",
    "filename": "FL15_pl_metatheory.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Propositional logic is metatheoretically complete in both directions: every semantically valid argument has a syntactic proof, and every syntactic proof preserves semantic truth. Soundness (if Γ ⊢ B then Γ ⊨ B) ensures no proof yields a false conclusion from true premises. Completeness (Kalmár 1935: if Γ ⊨ B then Γ ⊢ B) ensures no valid argument escapes formal proof. Together: ⊢ iff ⊨. PL is also decidable, compact, and has the finite model property."),
        ("Mathematical Form", 1, "Soundness: if Γ ⊢ B then Γ ⊨ B. Completeness (Kalmár 1935): if Γ ⊨ B then Γ ⊢ B. Combined: Γ ⊢ B iff Γ ⊨ B. Decidability: TAUT is co-NP-complete (2^n rows). Compactness: Γ ⊨ B iff some finite Γ₀ ⊆ Γ has Γ₀ ⊨ B. Finite model property: if satisfiable, satisfiable in a finite model."),
        ("Constraint Category", 2, "Informatic (In): PL metatheory enforces exact correspondence between syntactic derivability ⊢ and semantic entailment ⊨. This is the gold standard of logical system design — neither gap nor excess between what can be proved and what is true. The constraint also imposes decidability, distinguishing PL from richer systems."),
        ("DS Cross-References", 3, "FL9 (Tautological Entailment) establishes the semantic ⊨ relation. FL12 (Natural Deduction) establishes the syntactic ⊢ relation. MATH4 (Gödel): PL is the good case — incompleteness only hits systems strong enough to encode arithmetic. FL20 (QL Semantics): first-order completeness is harder, proved by Gödel 1930."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nThe soundness/completeness bridge conserves the meaning of logical consequence across syntax and semantics. What can be proved equals what is true — no information is lost or gained in translating between the proof-theoretic and model-theoretic perspectives."),
        ("What The Math Says", 5, "Soundness is proved by induction on proof length: base case (assumptions entail themselves), inductive step (each rule preserves the entailment property). Completeness is harder: the standard proof constructs a maximal consistent extension of any consistent set Γ, then uses this extension as a canonical model. The Lindenbaum lemma ensures the extension exists. For PL, the canonical model is a truth-value assignment, making the construction finite. This breaks down for first-order logic, where the canonical model must be constructed from terms of the language."),
        ("Concept Tags", 6, "• soundness\n• completeness\n• metatheory\n• turnstile\n• double turnstile\n• decidability\n• compactness\n• finite model property\n• Kalmár completeness\n• Lindenbaum lemma"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "soundness, completeness, metatheory, turnstile, double turnstile, decidability, compactness, finite model property, Kalmár completeness, Lindenbaum lemma", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("couples to", "FL15", "PL Metatheory (Soundness and Completeness)", "FL9", "Tautological Entailment", "FL15 validates FL9: the semantic consequence relation ⊨ defined in FL9 is exactly captured by the syntactic derivability relation ⊢. Every tautological entailment has a proof, and every proof witnesses an entailment."),
        ("couples to", "FL15", "PL Metatheory (Soundness and Completeness)", "FL12", "Natural Deduction (Fitch System)", "FL15 validates FL12: the Fitch system is sound (truth-preserving) and complete (derives every valid argument). The natural deduction system is a formally adequate representation of the semantic consequence relation."),
        ("analogous to", "FL15", "PL Metatheory (Soundness and Completeness)", "MATH4", "Gödel's Incompleteness Theorems", "PL completeness (⊢ iff ⊨) is exactly what Gödel shows fails for arithmetic: there exist true arithmetical sentences with no proof. PL is the instructive limit case where syntax and semantics fully coincide."),
    ],
},

{
    "id": "FL16",
    "title": "Quantificational Logic (First-Order)",
    "filename": "FL16_quantificational_logic.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Quantificational logic (QL, first-order logic) extends propositional logic with quantifiers ∀x (for all) and ∃x (there exists), individual variables and constants, and predicates expressing properties and relations. QL can formalize statements about objects in a domain: 'all humans are mortal', 'some number is prime'. It is the standard logic for mathematics and science. QL is semi-decidable (valid formulas can be enumerated) but undecidable in general (Church 1936, Turing 1936)."),
        ("Mathematical Form", 1, "Syntax: constants a,b,...; variables x,y,...; predicates F,G,R,...; quantifiers ∀,∃. ∀x Fx: every individual has property F. ∃x Fx: some individual has F. Models: M = (D, I) where D is a non-empty domain and I maps constants to objects, predicates to relations over D. Satisfaction: M ⊨ ∀x A(x) iff for all d∈D, M[x↦d] ⊨ A(x)."),
        ("Constraint Category", 2, "Informatic (In): QL adds a dimension — quantification over individuals — to PL's truth-functional calculus. This dimensional extension is what enables QL to express properties, relations, and generalizations that PL cannot see. The cost is decidability: while PL validity is decidable, QL validity is not (Church-Turing)."),
        ("DS Cross-References", 3, "FL5 (Propositional Logic): PL is the propositional fragment of QL — QL inherits all PL connectives and tautologies. FL18 (Quantifier Rules): the inference rules for ∀ and ∃. FL20 (QL Semantics): models, Q-valuations, and Q-validity. CS2 (Halting Problem): QL undecidability is proved by reduction from the halting problem — the fundamental link between logic and computability."),
        ("Mathematical Archetype", 4, "Mathematical archetype: dimensional-scaling\n\nQL adds a new dimension — quantification over individuals in a domain — to PL's Boolean calculus. This dimensional scaling increases expressive power (can talk about objects, not just propositions) at the cost of decidability (infinite models are possible)."),
        ("What The Math Says", 5, "Church (1936) and Turing (1936) independently proved QL validity is undecidable: no algorithm can determine for every QL formula whether it is valid. However, Gödel (1930) proved QL is complete: every valid formula has a proof. The combination — complete but undecidable — means proofs exist for all valid formulas but no algorithm can find them in bounded time for all inputs. This is the fundamental difference from PL, where completeness plus decidability makes everything mechanically resolvable."),
        ("Concept Tags", 6, "• quantificational logic\n• first-order logic\n• universal quantifier\n• existential quantifier\n• predicates\n• domain of discourse\n• interpretation\n• semi-decidable\n• Church undecidability\n• Gödel completeness"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "quantificational logic, first-order logic, universal quantifier, existential quantifier, predicates, domain of discourse, interpretation, semi-decidable, Church undecidability, Gödel completeness", 0),
        ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "FL16", "Quantificational Logic (First-Order)", "FL5", "Propositional Logic (PL)", "QL extends PL with quantifiers ∀ and ∃ and a domain of individuals. PL is the propositional fragment: all PL tautologies remain QL theorems. The extension adds expressive power at the cost of decidability."),
        ("couples to", "FL16", "Quantificational Logic (First-Order)", "CS2", "Halting Problem — Turing Undecidability", "QL undecidability is proved by reducing the halting problem to QL validity: if QL validity were decidable, we could decide HALT. This is the fundamental bridge between logic and computability theory."),
        ("derives from", "FL16", "Quantificational Logic (First-Order)", "FL18", "Quantifier Inference Rules", "FL18 provides the QL-specific inference rules (∀E, ∀I, ∃I, ∃E) that extend PL's rule set. These rules are the operational content that makes QL reasoning possible within a natural deduction framework."),
    ],
},

{
    "id": "FL17",
    "title": "QL Translation and Scope",
    "filename": "FL17_ql_translation_scope.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Translating English into quantificational logic requires identifying the logical form hidden in natural language. Key challenges: scope of quantifiers ('every student passed a test' — one test or many?), restricted quantification ('every F is G' = ∀x(Fx→Gx) vs 'some F is G' = ∃x(Fx∧Gx)), and the asymmetry between universal-conditional and existential-conjunctive forms. Order of quantifiers matters: ∀x∃y Lxy ≠ ∃y∀x Lxy in general."),
        ("Mathematical Form", 1, "'Every F is G': ∀x(Fx→Gx). 'Some F is G': ∃x(Fx∧Gx). 'No F is G': ¬∃x(Fx∧Gx) ≡ ∀x(Fx→¬Gx). Scope: ∀x∃y Lxy (each x has its own y) vs ∃y∀x Lxy (one y for all x). Scope ambiguity arises when natural language leaves quantifier order unspecified."),
        ("Constraint Category", 2, "Informatic (In): translation is a precision constraint — natural language is systematically ambiguous about quantifier scope, and QL resolves each ambiguity into a unique parse. The universal-conditional / existential-conjunctive asymmetry is a design feature preventing vacuous readings of restricted quantification."),
        ("DS Cross-References", 3, "FL16 (QL): provides the syntax and quantifiers. FL3 (Topic Neutrality): translation strips domain-specific content, leaving only logical form — the same schematization principle applied at the predicate level. FL10 (Material Conditional): the conditional reappears in universal quantification ∀x(Fx→Gx), inheriting the material conditional's vacuous-truth behavior when no Fs exist."),
        ("Mathematical Archetype", 4, "Mathematical archetype: symmetry-conservation\n\nCorrect translation preserves logical form: the validity or invalidity of the English argument must be preserved in the QL rendering. Translation is a form-preserving map from natural language to formal language, conserving inferential structure across the representation change."),
        ("What The Math Says", 5, "The universal-conditional form ∀x(Fx→Gx) is vacuously true when nothing is F — a consequence of the material conditional's truth table. This is not a bug but a design feature: in an empty extension, 'all unicorns fly' is logically true, which matches the convention that universal claims have no existential import. The existential-conjunctive form ∃x(Fx∧Gx) does carry existential import: it asserts at least one F exists. The scope distinction ∀x∃y vs ∃y∀x is the quantifier analogue of the de re / de dicto distinction in modal logic."),
        ("Concept Tags", 6, "• QL translation\n• quantifier scope\n• restricted quantification\n• universal conditional\n• existential conjunction\n• scope ambiguity\n• formalization\n• logical form extraction\n• vacuous truth\n• de re / de dicto"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "QL translation, quantifier scope, restricted quantification, universal conditional, existential conjunction, scope ambiguity, formalization, logical form extraction, vacuous truth, de re / de dicto", 0),
        ("DS Facets", "mathematical_archetype", "symmetry-conservation", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL17", "QL Translation and Scope", "FL16", "Quantificational Logic (First-Order)", "Translation presupposes QL's syntax: quantifiers, predicates, variables, and constants are the target vocabulary. FL16 defines the formal language into which English is translated."),
        ("derives from", "FL17", "QL Translation and Scope", "FL3", "Logical Form and Topic Neutrality", "Translation is schematization at the predicate level — stripping domain content and exposing logical form. FL3's topic-neutrality principle guarantees that the logical form, once extracted, determines validity independently of the original domain."),
        ("couples to", "FL17", "QL Translation and Scope", "FL10", "The Material Conditional", "The material conditional reappears in restricted universal quantification: ∀x(Fx→Gx). This inherits the vacuous-truth property — true when nothing is F — which is the source of the 'existential import' puzzle in syllogistic logic."),
    ],
},

{
    "id": "FL18",
    "title": "Quantifier Inference Rules",
    "filename": "FL18_quantifier_inference_rules.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "The quantifier inference rules extend PL's rule set to handle universal and existential statements. Universal elimination (∀E): from ∀x Fx, derive Fa for any term a. Universal introduction (∀I): from Fa where a is arbitrary (not in any undischarged assumption), derive ∀x Fx. Existential introduction (∃I): from Fa, derive ∃x Fx. Existential elimination (∃E): from ∃x Fx, assume Fa for fresh a, derive a conclusion not mentioning a. Strict freshness restrictions prevent logical fallacies."),
        ("Mathematical Form", 1, "∀E: ∀x A(x) / A(t) for any term t. ∀I: A(a) / ∀x A(x), where a is not in any undischarged assumption or the conclusion. ∃I: A(t) / ∃x A(x). ∃E: ∃x A(x), [A(a)]⊢C / C, where a is fresh (new to the proof) and does not appear in C or any undischarged assumption outside the subproof."),
        ("Constraint Category", 2, "Informatic (In): the freshness restrictions on ∀I and ∃E prevent overgeneralization — they ensure that what is proved about an arbitrary individual genuinely holds for all individuals, and that what is derived from 'something has property F' does not smuggle in assumptions about which thing it is."),
        ("DS Cross-References", 3, "FL13 (Core PL Rules): the quantifier rules extend the PL rule set, adding four new rules that handle the ∀ and ∃ connectives missing from propositional logic. FL12 (Natural Deduction): the Fitch framework hosts these rules, with ∃E requiring a subproof (like CP and RAA). FL16 (QL): defines the syntax and semantics over which these rules operate."),
        ("Mathematical Archetype", 4, "Mathematical archetype: conservation-law\n\nEach quantifier rule preserves truth in all models. ∀E: if everything has property F, then a specific thing has it. ∃I: if a specific thing has property F, then something does. The freshness restrictions ensure that the conservation is strict: no unwarranted information is created."),
        ("What The Math Says", 5, "The freshness restriction on ∀I prevents the fallacy of hasty generalization: without it, one could 'prove' ∀x∀y Lxy from ∀x Lxx (everyone loves themselves → everyone loves everyone). The restriction requires that the name a not appear in any undischarged assumption, ensuring a is genuinely arbitrary. Similarly, the ∃E freshness restriction prevents the fallacy of treating an existential witness as a specific known individual. These restrictions are the proof-theoretic encoding of the semantic distinction between 'for all' and 'for some particular'."),
        ("Concept Tags", 6, "• quantifier rules\n• universal elimination\n• universal introduction\n• existential introduction\n• existential elimination\n• freshness restriction\n• arbitrary name\n• QL proof\n• instantiation\n• generalization"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "quantifier rules, universal elimination, universal introduction, existential introduction, existential elimination, freshness restriction, arbitrary name, QL proof, instantiation, generalization", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL18", "Quantifier Inference Rules", "FL13", "Modus Ponens and Core Inference Rules", "The quantifier rules extend FL13's PL rule set with four new rules for ∀ and ∃. The PL rules remain available unchanged; the quantifier rules add the ability to reason about individuals and generalizations."),
        ("implements", "FL18", "Quantifier Inference Rules", "FL16", "Quantificational Logic (First-Order)", "FL18 provides the operational rules that make QL reasoning possible. Without these rules, QL's quantifiers would be uninterpretable symbols; the rules give them proof-theoretic meaning."),
        ("derives from", "FL18", "Quantifier Inference Rules", "FL12", "Natural Deduction (Fitch System)", "∃E requires a subproof (assuming Fa for fresh a, deriving C), using the same Fitch subproof mechanism as CP and RAA. The natural deduction framework hosts the quantifier rules naturally."),
    ],
},

{
    "id": "FL19",
    "title": "The Empty Domain Problem",
    "filename": "FL19_empty_domain_problem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Standard quantificational logic assumes the domain of discourse is non-empty — there exists at least one object. If this assumption is dropped, paradoxes arise: in an empty domain, ∀x Fx is vacuously true for any F (no counterexample exists), while ∃x Fx is false (no witness exists). Using ∀E and ∃I, one could derive ∃x Fx from ∀x Fx, which is false in an empty domain — a 'logical disaster'. Free logic addresses this by allowing empty domains and non-denoting terms."),
        ("Mathematical Form", 1, "Standard QL: |D| ≥ 1 (non-empty domain assumption). If D = ∅: ∀x A(x) is vacuously true for any A; ∃x A(x) is false for any A. Paradox: ∀x Fx, by ∀E: Fa, by ∃I: ∃x Fx — but ∃x Fx is false when D = ∅. Free logic: drops |D| ≥ 1, restricts ∃I to require independent existence proof."),
        ("Constraint Category", 2, "Informatic (In): the empty domain problem reveals a boundary condition in quantifier logic. The non-empty domain assumption is a hidden existential commitment that standard QL smuggles in. Free logic makes this commitment explicit and optional, allowing formal reasoning about possibly non-existent entities."),
        ("DS Cross-References", 3, "FL16 (QL): assumes non-empty domain by convention. FL10 (Material Conditional): vacuous truth in the empty domain parallels the material conditional's behavior with false antecedent — both satisfy universal claims trivially. FL21 (Identity and Descriptions): Russell's theory handles non-denoting terms in a non-empty domain; free logic extends this to the empty-domain case. FL22 (Non-Classical Logics): free logic is a non-classical variant."),
        ("Mathematical Archetype", 4, "Mathematical archetype: threshold-transition\n\nThe empty/non-empty boundary is a sharp phase transition: above it (|D| ≥ 1), standard QL inference is valid; at it (|D| = 0), standard inference rules become unsound. The transition is discontinuous and qualitative."),
        ("What The Math Says", 5, "The empty domain problem is resolved in practice by convention (mathematicians assume non-empty domains) and in theory by free logic (Bencivenga, Lambert). In free logic, universal instantiation ∀x Fx → Fa requires an additional premise E!a (a exists), and existential generalization Fa → ∃x Fx likewise requires E!a. This makes the existence assumption explicit at each inference step rather than hidden in the background. The payoff is the ability to reason formally about fictional entities, empty extensions, and non-denoting terms without logical collapse."),
        ("Concept Tags", 6, "• empty domain\n• vacuous truth\n• free logic\n• existence assumption\n• non-empty domain\n• existential import\n• quantifier semantics\n• boundary case\n• non-denoting terms\n• logical paradox"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "empty domain, vacuous truth, free logic, existence assumption, non-empty domain, existential import, quantifier semantics, boundary case, non-denoting terms, logical paradox", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "FL19", "The Empty Domain Problem", "FL16", "Quantificational Logic (First-Order)", "The empty domain problem arises from QL's non-empty domain assumption. FL16 defines the standard framework; FL19 identifies the boundary condition where that framework fails."),
        ("analogous to", "FL19", "The Empty Domain Problem", "FL10", "The Material Conditional", "Both involve vacuous truth: the material conditional is vacuously true when the antecedent is false; universal quantification is vacuously true when the domain is empty. The structural parallel illuminates how logical systems handle trivial satisfaction."),
        ("couples to", "FL19", "The Empty Domain Problem", "FL21", "Identity, Descriptions, and Functions", "Russell's theory of descriptions handles non-denoting terms (the present king of France) within standard QL by parsing out existence claims. Free logic generalizes this to the empty-domain case, where all terms potentially lack referents."),
    ],
},

{
    "id": "FL20",
    "title": "QL Semantics and Validity",
    "filename": "FL20_ql_semantics_validity.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "QL validity is defined model-theoretically: an argument is Q-valid iff every model making the premises true also makes the conclusion true. A QL formula is Q-valid iff true in every model. Unlike PL, QL validity is undecidable (Church 1936) but semi-decidable: Gödel's completeness theorem (1930) guarantees every valid formula has a proof. The combination — complete but undecidable — is the fundamental metatheoretic result distinguishing first-order logic from propositional logic."),
        ("Mathematical Form", 1, "Model M = (D, I) where D is non-empty domain, I maps constants to elements of D, predicates to relations over D. M ⊨ ∀x A(x) iff for every d∈D, M[x↦d] ⊨ A(x). Q-valid: for all M, M ⊨ A. Gödel completeness (1930): ⊨ A iff ⊢ A. Church undecidability (1936): {A : ⊨ A} is not decidable. Compactness: if every finite subset of Γ has a model, Γ has a model."),
        ("Constraint Category", 2, "Informatic (In): QL semantics defines the standard of truth for quantified statements via model theory. The undecidability/completeness tension means QL is the strongest logic with a complete proof system — any extension either loses completeness (second-order logic) or gains it trivially (propositional fragments)."),
        ("DS Cross-References", 3, "FL15 (PL Metatheory): PL completeness is the simpler case; QL completeness is Gödel's 1930 result, proved before the 1931 incompleteness theorems. MATH4 (Gödel Incompleteness): first-order logic itself is complete, but first-order arithmetic within it is not — the incompleteness applies to specific theories, not to the logic. CS2 (Halting Problem): QL validity is undecidable by reduction from HALT."),
        ("Mathematical Archetype", 4, "Mathematical archetype: dimensional-scaling\n\nQL semantics scales from PL by adding domain and interpretation dimensions. PL valuations are points in {T,F}ⁿ; QL models are structures (D,I) with potentially infinite domains, making the space of models uncountably rich."),
        ("What The Math Says", 5, "Gödel's completeness theorem (1930) is proved by constructing a canonical model from a maximal consistent set of formulas: if Γ is consistent, extend it to a maximal consistent set Γ*, then build a model whose domain consists of equivalence classes of terms under Γ*-provable identity. The Löwenheim-Skolem theorem follows: any satisfiable first-order theory has a countable model. This means first-order logic cannot distinguish countable from uncountable structures — a fundamental limitation that motivates second-order logic."),
        ("Concept Tags", 6, "• QL validity\n• model theory\n• Q-valid\n• interpretation\n• domain of discourse\n• Gödel completeness\n• Church undecidability\n• semantic consequence\n• Löwenheim-Skolem\n• compactness"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "QL validity, model theory, Q-valid, interpretation, domain of discourse, Gödel completeness, Church undecidability, semantic consequence, Löwenheim-Skolem, compactness", 0),
        ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "FL20", "QL Semantics and Validity", "FL15", "PL Metatheory (Soundness and Completeness)", "PL completeness (Kalmár) and QL completeness (Gödel 1930) are structurally parallel results — both establish ⊢ iff ⊨ — but QL completeness is harder and does not carry decidability with it."),
        ("couples to", "FL20", "QL Semantics and Validity", "MATH4", "Gödel's Incompleteness Theorems", "First-order logic is complete (Gödel 1930); first-order arithmetic is incomplete (Gödel 1931). The distinction is crucial: the incompleteness applies to specific theories formulated in QL, not to the logic itself."),
        ("couples to", "FL20", "QL Semantics and Validity", "CS2", "Halting Problem — Turing Undecidability", "QL validity is undecidable: deciding whether a QL formula is valid requires, in the worst case, solving instances equivalent to the halting problem. This is the fundamental link between logic and computation."),
    ],
},

{
    "id": "FL21",
    "title": "Identity, Descriptions, and Functions",
    "filename": "FL21_identity_descriptions_functions.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "QL with identity (QL=) adds the identity predicate '=', enabling statements like 'there is exactly one F' and 'a and b are the same object.' Leibniz's Law (Indiscernibility of Identicals): if a = b then anything true of a is true of b. Russell's theory of definite descriptions: 'the F is G' is analyzed as ∃x(Fx ∧ ∀y(Fy→y=x) ∧ Gx) — there exists exactly one F and it is G. Functions extend QL= by combining with terms to form new complex terms."),
        ("Mathematical Form", 1, "Identity: a = b. Leibniz's Law: a = b, A(a) / A(b). Russell: 'The F is G' = ∃x(Fx ∧ ∀y(Fy→y=x) ∧ Gx). 'Exactly one F': ∃x(Fx ∧ ∀y(Fy→y=x)). 'At most one F': ∀x∀y((Fx∧Fy)→x=y). Functions: f(a) = b, total and single-valued. Function terms compose: f(g(a))."),
        ("Constraint Category", 2, "Informatic (In): identity is the smallest equivalence relation, partitioning a domain into singleton classes. Leibniz's Law is an information-transfer principle: anything known about a transfers to b when a = b. Russell's analysis eliminates singular terms that might lack referents, preventing truth-value gaps."),
        ("DS Cross-References", 3, "FL16 (QL): identity extends the base QL language. FL18 (Quantifier Rules): identity rules (reflexivity, substitution) extend the quantifier rule set. FL3 (Topic Neutrality): Leibniz's Law is maximally topic-neutral — it applies to any predicate in any domain, making identity the purest case of domain-independent reasoning. FL19 (Empty Domain): Russell's theory handles non-denoting descriptions within non-empty domains."),
        ("Mathematical Archetype", 4, "Mathematical archetype: symmetry-conservation\n\nIdentity is the symmetry relation: a = b means a and b are interchangeable in all contexts. Leibniz's Law conserves truth under substitution of identicals — the same symmetry-conservation principle that underlies topic neutrality (FL3), now applied at the individual level rather than the schema level."),
        ("What The Math Says", 5, "Russell's analysis of 'the present King of France is bald' as ∃x(Kx ∧ ∀y(Ky→y=x) ∧ Bx) is false (not meaningless) because there is no x satisfying Kx. This preserves bivalence: every sentence is true or false, with no truth-value gaps. Functions in QL= are restricted to total, single-valued mappings — every input has exactly one output. They streamline mathematical reasoning by allowing nested terms like f(g(a)) without quantifier nesting, enabling the formalization of arithmetic, algebra, and analysis within first-order logic."),
        ("Concept Tags", 6, "• identity predicate\n• Leibniz's Law\n• definite descriptions\n• Russell's analysis\n• QL with identity\n• indiscernibility of identicals\n• numerical quantification\n• singular terms\n• functions in logic\n• substitutivity"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "identity predicate, Leibniz's Law, definite descriptions, Russell's analysis, QL with identity, indiscernibility of identicals, numerical quantification, singular terms, functions in logic, substitutivity", 0),
        ("DS Facets", "mathematical_archetype", "symmetry-conservation", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "FL21", "Identity, Descriptions, and Functions", "FL16", "Quantificational Logic (First-Order)", "QL= extends QL with the identity predicate and function symbols. Identity adds no new quantificational structure but dramatically increases expressive power: numerical claims, definite descriptions, and mathematical functions all become formalizable."),
        ("derives from", "FL21", "Identity, Descriptions, and Functions", "FL3", "Logical Form and Topic Neutrality", "Leibniz's Law is the purest expression of topic neutrality at the individual level: if a = b, then any property of a is a property of b regardless of what domain or predicate is involved. It is substitution invariance for individuals."),
        ("couples to", "FL21", "Identity, Descriptions, and Functions", "FL19", "The Empty Domain Problem", "Russell's theory handles non-denoting descriptions ('the present King of France') by parsing out an existence claim. Free logic extends this approach to the case where the entire domain might be empty."),
    ],
},

{
    "id": "FL22",
    "title": "Intuitionistic and Non-Classical Logics",
    "filename": "FL22_intuitionistic_nonclassical_logics.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "formal logic · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "FL",
    "sections": [
        ("What It Claims", 0, "Classical logic assumes bivalence (every proposition is determinately true or false) and the law of excluded middle (A ∨ ¬A). Intuitionistic logic (Brouwer, Heyting) rejects LEM: a disjunction is assertable only when one disjunct is constructively established. Double negation elimination (¬¬A → A) fails intuitionistically. Many-valued logics assign truth values beyond {T,F}. Relevant logic requires premises to be relevant to conclusions. Paraconsistent logic rejects explosion, allowing localized inconsistencies."),
        ("Mathematical Form", 1, "Classical: v(A) ∈ {T,F} (bivalence); ⊨ A ∨ ¬A (LEM). Intuitionistic (BHK interpretation): a proof of A∨B is a proof of A or a proof of B; ¬¬A → A fails. Kripke semantics: formulas evaluated at worlds in a partial order; A holds at w iff A holds at all accessible worlds. Many-valued: truth values in [0,1] or {T,F,I}. Paraconsistent: A, ¬A ⊭ B."),
        ("Constraint Category", 2, "Informatic (In): non-classical logics explore the design space of formal reasoning by varying which classical assumptions are retained. Each variant modifies the conservation law: intuitionistic logic strengthens the proof requirement (constructive witness needed); paraconsistent logic weakens explosion (contradictions are contained); relevant logic strengthens the relevance requirement."),
        ("DS Cross-References", 3, "FL11 (Explosion): intuitionistic logic accepts explosion; paraconsistent logic rejects it — this is the key branching point in the non-classical design space. FL15 (PL Metatheory): completeness holds classically but intuitionistic proof theory is different — intuitionistic PL is complete with respect to Kripke semantics, not truth-table semantics. MATH4 (Gödel): Gödel showed classical PA is consistent iff intuitionistic HA (Heyting Arithmetic) is — the two systems are equiconsistent, though they differ in provable theorems."),
        ("Mathematical Archetype", 4, "Mathematical archetype: threshold-transition\n\nThe classical/intuitionistic boundary is a sharp divergence in what counts as proof. Rejecting LEM is not a quantitative weakening but a qualitative shift: the space of provable theorems changes discontinuously. Similarly, rejecting explosion transforms the consistency landscape from all-or-nothing to gradual."),
        ("What The Math Says", 5, "Gödel's double-negation translation (1933) shows that every classically provable formula has an intuitionistically provable double-negation translation: if classical PA proves A, then intuitionistic HA proves ¬¬A*. This means intuitionistic logic is not weaker than classical logic in a simple sense — it proves different things about the same structures. Kripke semantics (1965) provides a complete semantics for intuitionistic logic using partially-ordered sets of worlds. The Curry-Howard correspondence maps intuitionistic proofs to typed lambda terms, making intuitionistic logic the natural logic of computation: a proof of A→B is literally a program transforming evidence for A into evidence for B."),
        ("Concept Tags", 6, "• intuitionistic logic\n• non-classical logic\n• law of excluded middle\n• bivalence\n• constructive proof\n• BHK interpretation\n• Kripke semantics\n• many-valued logic\n• paraconsistent logic\n• double negation elimination"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "intuitionistic logic, non-classical logic, law of excluded middle, bivalence, constructive proof, BHK interpretation, Kripke semantics, many-valued logic, paraconsistent logic, double negation elimination", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("couples to", "FL22", "Intuitionistic and Non-Classical Logics", "FL11", "Explosion and Absurdity (Ex Falso Quodlibet)", "Paraconsistent logics are defined by rejecting explosion. Intuitionistic logic retains explosion but rejects LEM. FL11 and FL22 together map the design space: classical = explosion + LEM; intuitionistic = explosion − LEM; paraconsistent = − explosion + LEM (or neither)."),
        ("analogous to", "FL22", "Intuitionistic and Non-Classical Logics", "MATH4", "Gödel's Incompleteness Theorems", "Gödel's double-negation translation shows classical and intuitionistic arithmetic are equiconsistent: one is consistent iff the other is. This deep connection means incompleteness constrains both systems equally, despite their different proof-theoretic properties."),
        ("couples to", "FL22", "Intuitionistic and Non-Classical Logics", "FL15", "PL Metatheory (Soundness and Completeness)", "Intuitionistic PL is sound and complete with respect to Kripke semantics (not truth tables). The metatheory changes: completeness is preserved but with a different semantics, showing that the soundness/completeness paradigm extends beyond classical logic."),
    ],
},

]  # end ENTRIES (all 22)


def insert_entries(db_path, entries):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    inserted = skipped = 0

    for e in entries:
        cur.execute("""
            INSERT OR IGNORE INTO entries
                (id, title, filename, entry_type, scale, domain, status, confidence, type_group, authoring_status)
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (e["id"], e["title"], e["filename"], e["entry_type"], e["scale"],
              e["domain"], e["status"], e["confidence"], e["type_group"], None))

        if cur.rowcount == 0:
            print(f"  SKIP (exists): {e['id']}")
            skipped += 1
            continue

        for (sname, sorder, content) in e["sections"]:
            cur.execute("""
                INSERT INTO sections (entry_id, section_name, section_order, content)
                VALUES (?,?,?,?)
            """, (e["id"], sname, sorder, content))

        for (tname, pname, pvalue, porder) in e["properties"]:
            cur.execute("""
                INSERT INTO entry_properties
                    (entry_id, table_name, property_name, property_value, prop_order)
                VALUES (?,?,?,?,?)
            """, (e["id"], tname, pname, pvalue, porder))

        for (ltype, src, slabel, tgt, tlabel, desc) in e.get("links", []):
            cur.execute("""
                INSERT OR IGNORE INTO links
                    (link_type, source_id, source_label, target_id, target_label,
                     description, link_order, confidence_tier)
                VALUES (?,?,?,?,?,?,?,?)
            """, (ltype, src, slabel, tgt, tlabel, desc, 0, "1.5"))

        print(f"  INSERT: {e['id']} — {e['title']}")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone: {inserted} inserted, {skipped} skipped.")
    return inserted


if __name__ == "__main__":
    print(f"Inserting FL entries ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)
