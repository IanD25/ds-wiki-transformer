"""
Option E — Chunk 3: Computer Science + Complexity Theory
Inserts 15 new reference_law entries into ds_wiki.db.
Safe to re-run: INSERT OR IGNORE on entries.

Entries:
  CS1:  Church-Turing Thesis
  CS2:  Halting Problem (Turing Undecidability)
  CS3:  Rice's Theorem
  CS4:  Cook-Levin Theorem (NP-completeness)
  CS5:  Master Theorem (Divide & Conquer Recurrences)
  CS6:  Nyquist-Shannon Sampling Theorem
  CS7:  CAP Theorem
  CS8:  Amdahl's Law
  CS9:  Little's Law (Queuing Theory)
  CS10: No Free Lunch Theorem
  CS11: Comparison Sort Lower Bound (Omega(n log n))
  CS12: FLP Impossibility Theorem
  CS13: Perron-Frobenius Theorem
  CS14: Byzantine Fault Tolerance
  CS15: Time Hierarchy Theorem
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import SOURCE_DB

ENTRIES = [

# ── COMPUTABILITY THEORY ──────────────────────────────────────────────────

{
    "id": "CS1",
    "title": "Church-Turing Thesis",
    "filename": "CS1_church_turing_thesis.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Any function that can be computed by an effective procedure (a finite, deterministic, mechanical process) can be computed by a Turing machine (Church, 1936; Turing, 1936). All known models of computation — lambda calculus, RAM machines, cellular automata, register machines, quantum circuits (for classical output) — compute exactly the class of Turing-computable functions. The thesis is not a theorem (it cannot be formally proved) but is universally accepted as a physical fact about computation."),
        ("Mathematical Form", 1,
         "f is effectively computable ⟺ f is Turing-computable\n\nEquivalent models: λ-calculus, μ-recursive functions, RAM model, Post correspondence, cellular automata\nAll define the same class: the partial recursive functions\nPhysical Church-Turing thesis: any physical process can be simulated by a Turing machine (contested by quantum computing advocates)"),
        ("Constraint Category", 2,
         "Informatic (In): the Church-Turing thesis defines the boundary of the computable — the set of information transformations achievable by mechanical processes. It is the foundational constraint on what algorithms can accomplish. Any physical process that computes must fall within Turing-computable limits (classical Church-Turing); quantum complexity may extend this to probabilistic polynomial time."),
        ("DS Cross-References", 3,
         "INFO5 (Kolmogorov Complexity — K(x) is defined using Turing machines; Church-Turing determines the universe of descriptions over which K is minimised). BIO5 (Central Dogma — gene expression is a molecular computation: transcription and translation implement a read-only tape model; Church-Turing asks whether biological computation exceeds Turing power). MATH4 (Gödel Incompleteness — Church-Turing and Gödel's theorems are equivalent in the sense that undecidability of the halting problem and unprovability of Gödel sentences use identical diagonalisation arguments)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nComputability is conserved across all known models: no reasonable model computes more than the Turing machine, and all compute the same class of functions. This universality is a conservation law in the space of computational models — the Turing-computable functions are the invariant set. The thesis also bounds what physics can compute: physical computation cannot escape the Turing-computable class under classical assumptions."),
        ("What The Math Says", 5,
         "Church's lambda calculus and Turing's machine model were developed independently and proved equivalent in 1936. Every lambda expression has an equivalent Turing machine, and every Turing machine computation can be expressed in lambda calculus. Since then, every proposed model of computation — RAM machines with random-access memory, Post production systems, cellular automata, partial recursive functions defined by Kleene, register machines, and even quantum computers for classical outputs — has been shown equivalent to the Turing machine for the class of decidable problems. The thesis therefore states that Turing computability captures the informal notion of algorithmic solvability: if there exists a precise finite procedure for a problem, a Turing machine can perform it."),
        ("Concept Tags", 6,
         "• Church-Turing thesis\n• Turing machine\n• computability\n• effective procedure\n• lambda calculus\n• partial recursive functions\n• universal computation\n• algorithmic solvability\n• computational models equivalence\n• physical Church-Turing"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Church-Turing thesis, Turing machine, computability, effective procedure, lambda calculus, partial recursive functions, universal computation, algorithmic solvability, computational models equivalence, physical Church-Turing", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("implements", "CS1", "Church-Turing Thesis", "INFO5", "Kolmogorov Complexity", "Kolmogorov complexity K(x) is defined as the length of the shortest Turing machine program that outputs x; Church-Turing ensures this definition is model-independent up to a constant."),
        ("analogous to", "CS1", "Church-Turing Thesis", "MATH4", "Gödel's Incompleteness Theorems", "Both use diagonalisation to establish absolute limits: Gödel limits what formal systems can prove; Church-Turing limits what algorithms can compute. The halting problem proof is structurally identical to Gödel's construction."),
        ("couples to", "CS1", "Church-Turing Thesis", "BIO5", "Central Dogma of Molecular Biology", "The Central Dogma implements a molecular computation (DNA→RNA→Protein); Church-Turing asks whether biological computation — including neural networks and evolution — is equivalent to or exceeds Turing computability."),
    ],
},

{
    "id": "CS2",
    "title": "Halting Problem — Turing Undecidability",
    "filename": "CS2_halting_problem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "There is no algorithm that, given an arbitrary program P and input I, always correctly determines whether P halts (terminates) or runs forever (Turing, 1936). The halting problem is undecidable — it is not merely difficult but provably impossible. This is the first and most fundamental undecidability result, proved by diagonalisation: assume a halter H exists, build a program D that halts iff H says it doesn't, then ask H about D — contradiction."),
        ("Mathematical Form", 1,
         "HALT = {⟨M, w⟩ : Turing machine M halts on input w}\nTheorem: HALT is not Turing-decidable\nProof: Diagonalisation — assume decider H exists, construct D(x): run H(x,x); if H says 'halt', loop; if H says 'loop', halt. Then H(D,D) is contradictory.\nHALT is Turing-recognisable (semi-decidable) but not co-recognisable."),
        ("Constraint Category", 2,
         "Informatic (In): the halting problem establishes a sharp boundary in the information landscape — a problem that is precisely statable and meaningful but forever beyond algorithmic reach. The proof introduces self-referential computation (Turing's version of Gödel's diagonalisation) as the technique for proving absolute computational limits."),
        ("DS Cross-References", 3,
         "MATH4 (Gödel Incompleteness — the halting problem proof is structurally identical to Gödel's: self-reference via diagonalisation generates an undecidable statement). INFO5 (Kolmogorov Complexity — K(x) is uncomputable because computing K requires solving an infinite family of halting problems). CS1 (Church-Turing — the halting problem demonstrates the limits of the Turing-computable class; undecidability is the hard boundary of Church-Turing). CS3 (Rice's Theorem — the halting problem is the special case of Rice's theorem for the non-trivial property 'program terminates on given input')."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nUndecidability is a conserved property: the halting problem cannot be decided by any Turing machine, and any attempt to decide it can be shown undecidable in turn. The set of undecidable problems is closed under Turing reduction — you cannot 'reduce away' undecidability. The halting problem sits at the base of an infinite hierarchy of undecidable problems (Turing degrees), and its undecidability propagates to all problems that reduce to it."),
        ("What The Math Says", 5,
         "Suppose for contradiction there exists a Turing machine H that takes as input the description of any program M and an input w, and outputs 'halt' if M terminates on w and 'loop' otherwise. Construct a program D that takes a program x as input, runs H on (x, x), and does the opposite: if H says x halts on x, then D loops; if H says x loops on x, then D halts. Now run D on its own description. If D halts on D, then H must have said 'loop' — but then D loops, contradiction. If D loops on D, then H must have said 'halt' — but then D halts, contradiction. Therefore no such H can exist."),
        ("Concept Tags", 6,
         "• halting problem\n• undecidability\n• Turing 1936\n• diagonalisation\n• self-reference\n• computability limits\n• semi-decidable\n• Turing reduction\n• undecidable language\n• computational impossibility"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "halting problem, undecidability, Turing 1936, diagonalisation, self-reference, computability limits, semi-decidable, Turing reduction, undecidable language, computational impossibility", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "CS2", "Halting Problem — Turing Undecidability", "MATH4", "Gödel's Incompleteness Theorems", "The halting problem proof uses the same diagonalisation construction as Gödel's incompleteness: both create a self-referential statement that leads to contradiction, establishing an absolute logical/computational limit."),
        ("derives from", "CS2", "Halting Problem — Turing Undecidability", "CS1", "Church-Turing Thesis", "The halting problem proves the limits of the Turing-computable class established by Church-Turing: there exist well-defined problems (like HALT) that are not Turing-computable."),
        ("couples to", "CS2", "Halting Problem — Turing Undecidability", "INFO5", "Kolmogorov Complexity", "Kolmogorov complexity K(x) is uncomputable because computing K would require solving an unbounded family of halting problems; undecidability of HALT is the root cause of K's incomputability."),
    ],
},

{
    "id": "CS3",
    "title": "Rice's Theorem",
    "filename": "CS3_rice_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Every non-trivial semantic property of programs is undecidable (Rice, 1953). A semantic property P is a set of computable functions (not programs); it is non-trivial if some programs have it and some don't. Rice's theorem states: you cannot algorithmically determine whether an arbitrary program computes a function with property P — not for any interesting property. This subsumes all specific undecidability results about program behaviour."),
        ("Mathematical Form", 1,
         "Let P be a non-empty proper subset of computable functions.\nThen {M : φ_M ∈ P} is undecidable.\n\nExamples of undecidable properties:\n  Does M ever output 0?\n  Does M halt on all inputs?\n  Does M compute the constant-zero function?\n  Does M halt in ≤ n steps for some n?\n  Is M equivalent to program M'?"),
        ("Constraint Category", 2,
         "Informatic (In): Rice's theorem establishes that programs are opaque with respect to their semantic behaviour — you cannot extract meaningful information about what a program computes just by analysing the program text, for any non-trivial property. This is the formal basis for the impossibility of perfect static program analysis, formal verification at scale, and malware detection."),
        ("DS Cross-References", 3,
         "CS2 (Halting Problem — halting on a given input is a special case of Rice's theorem: 'the program terminates on this input' is a non-trivial semantic property). MATH4 (Gödel Incompleteness — Rice's theorem is the program-behaviour analog: Gödel shows no formal system decides all mathematical truth; Rice shows no algorithm decides all program behaviours). INFO5 (Kolmogorov Complexity — computing K(x) requires deciding whether programs halt, a Rice-undecidable property)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe undecidability of non-trivial semantic properties is conserved: no algorithmic technique can overcome Rice's theorem for all programs. The theorem is a conservation law for program opacity — information about program behaviour cannot be extracted algorithmically from syntax alone, for any non-trivial behaviour. This is more powerful than the halting problem: it is a single theorem covering infinitely many specific undecidability results."),
        ("What The Math Says", 5,
         "Rice's theorem is proved by reduction from the halting problem. Suppose for contradiction we have a decider D for a non-trivial property P. Since P is non-trivial, there is some function f in P and some function g not in P, with corresponding programs M-f and M-g. Given any program M and input w, construct a new program M-prime that ignores its input, runs M on w, and if M halts runs M-f. Then M-prime computes f if M halts on w (so M-prime is in P), and computes g otherwise (not in P). Therefore D on M-prime decides the halting problem — contradiction. The reduction works for any non-trivial P."),
        ("Concept Tags", 6,
         "• Rice's theorem\n• semantic property undecidability\n• program behaviour\n• static analysis limits\n• formal verification limits\n• undecidability\n• computable functions\n• program opacity\n• Rice 1953\n• malware detection impossibility"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Rice's theorem, semantic property undecidability, program behaviour, static analysis limits, formal verification limits, undecidability, computable functions, program opacity, Rice 1953, malware detection impossibility", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("generalizes", "CS3", "Rice's Theorem", "CS2", "Halting Problem — Turing Undecidability", "The halting problem is a special case of Rice's theorem — 'this program terminates on this input' is a non-trivial semantic property. Rice's theorem derives all such undecidabilities from a single argument."),
        ("analogous to", "CS3", "Rice's Theorem", "MATH4", "Gödel's Incompleteness Theorems", "Both establish that no formal system (Rice: no algorithm; Gödel: no axiomatic system) can decide all instances of a non-trivial class of truths — program behaviour for Rice, mathematical truth for Gödel."),
        ("constrains", "CS3", "Rice's Theorem", "INFO5", "Kolmogorov Complexity", "Determining whether a program computes a function with a given property (needed for computing K) is Rice-undecidable — the incomputability of Kolmogorov complexity is a consequence of Rice's theorem applied to minimum-length programs."),
    ],
},

# ── COMPUTATIONAL COMPLEXITY ───────────────────────────────────────────────

{
    "id": "CS4",
    "title": "Cook-Levin Theorem — NP-Completeness",
    "filename": "CS4_cook_levin_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Boolean satisfiability (SAT) is NP-complete: (1) SAT ∈ NP — a satisfying assignment can be verified in polynomial time; (2) every problem in NP can be reduced to SAT in polynomial time (Cook, 1971; Levin, 1973). SAT is therefore the canonical hardest problem in NP. If SAT can be solved in polynomial time, then every NP problem can be — proving P = NP. The Cook-Levin theorem launched the field of NP-completeness and identified thousands of practically important problems as computationally equivalent to SAT."),
        ("Mathematical Form", 1,
         "SAT = {φ : φ is a satisfiable Boolean formula}\nSAT ∈ NP: ∃ poly-time verifier V(φ, assignment)\n∀L ∈ NP: L ≤_p SAT  (polynomial-time many-one reduction)\n\nConsequence: P ≠ NP ⟺ SAT ∉ P\nNP-complete class: NPC = {L : L ∈ NP ∧ SAT ≤_p L}"),
        ("Constraint Category", 2,
         "Coordination (Co): NP-completeness is a coordination hardness result — the difficulty arises from coordinating exponentially many potential configurations. SAT captures the essence of constraint satisfaction: is there a consistent assignment to boolean variables satisfying all clauses? The threshold between easy (satisfiable, 2-SAT) and hard (3-SAT) is a computational phase transition analogous to physical phase transitions."),
        ("DS Cross-References", 3,
         "D2 (Feigenbaum Universality — NP-completeness is a universality result: SAT is the universal hard problem just as Feigenbaum's constant is universal across period-doubling cascades). INFO2 (Source Coding Theorem — NP-hardness of optimal compression is a consequence: finding the shortest encoding for a general source is NP-hard). STAT1 (Maximum Entropy Principle — MaxEnt inference can become NP-hard when the constraint set generates a combinatorial structure equivalent to SAT). MATH4 (Gödel — if P ≠ NP, then NP-completeness gives a polynomial-time analog of Gödel incompleteness: hard instances are 'true but unprovable in polynomial time')."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: threshold-transition\n\nNP-completeness marks a phase transition in computational difficulty. For constraint satisfaction problems (like k-SAT), there is a sharp threshold in clause density α = m/n: below α_c, almost all instances are satisfiable and easy; above α_c, almost all are unsatisfiable and hard; near α_c, instances are hard and rare satisfying assignments exist. This is a computational phase transition with critical exponents, analogous to thermodynamic phase transitions."),
        ("What The Math Says", 5,
         "Cook's proof encodes any NP computation as a polynomial-size Boolean formula. An NP machine M on input x runs in polynomial time p(n); its entire computation tableau — the sequence of configurations — can be described by a Boolean formula phi of size polynomial in n. The formula is satisfiable if and only if M accepts x. Therefore SAT is NP-hard: any NP problem reduces to it. Since a satisfying assignment can be verified in polynomial time, SAT is in NP. Together: SAT is NP-complete. Levin independently discovered the same result in the Soviet Union. The k-SAT phase transition occurs at clause-to-variable ratio approximately 4.27 for 3-SAT: below this, instances are almost surely satisfiable; above, almost surely unsatisfiable."),
        ("Concept Tags", 6,
         "• Cook-Levin theorem\n• NP-completeness\n• SAT satisfiability\n• polynomial reduction\n• P vs NP\n• computational phase transition\n• Boolean formula\n• NP-hard\n• constraint satisfaction\n• complexity theory"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Co", 0),
        ("entries", "concept_tags", "Cook-Levin theorem, NP-completeness, SAT satisfiability, polynomial reduction, P vs NP, computational phase transition, Boolean formula, NP-hard, constraint satisfaction, complexity theory", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "CS4", "Cook-Levin Theorem — NP-Completeness", "D2", "D2: Feigenbaum Universality", "Feigenbaum universality identifies a universal constant across all period-doubling systems; NP-completeness identifies SAT as the universal hard problem — both are universality results where diverse instances reduce to a single canonical form."),
        ("analogous to", "CS4", "Cook-Levin Theorem — NP-Completeness", "MATH4", "Gödel's Incompleteness Theorems", "If P ≠ NP, NP-completeness gives a polynomial-time analog of Gödel incompleteness: hard NP instances are problems whose solutions exist but cannot be found in polynomial time — 'true but efficiently unprovable'."),
        ("implements", "CS4", "Cook-Levin Theorem — NP-Completeness", "CS1", "Church-Turing Thesis", "NP-completeness refines the Church-Turing framework by classifying problems within the decidable: not just can they be computed, but at what cost? Cook-Levin defines the boundary between tractable and intractable within the Turing-computable."),
    ],
},

{
    "id": "CS5",
    "title": "Master Theorem — Divide and Conquer Recurrences",
    "filename": "CS5_master_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The Master Theorem gives asymptotic solutions to recurrences of the form T(n) = aT(n/b) + f(n), which arise from divide-and-conquer algorithms that split a problem of size n into a subproblems of size n/b with f(n) work at each level (Cormen, Leiserson, Rivest, Stein). The solution depends on whether the recursive work (n^{log_b a}) dominates, equals, or is dominated by the non-recursive work f(n). This covers merge sort, binary search, FFT, Strassen matrix multiplication, and hundreds of other algorithms."),
        ("Mathematical Form", 1,
         "T(n) = aT(n/b) + f(n),  a ≥ 1, b > 1\n\nCase 1: f(n) = O(n^{log_b a − ε})  →  T(n) = Θ(n^{log_b a})  [recursion dominates]\nCase 2: f(n) = Θ(n^{log_b a})      →  T(n) = Θ(n^{log_b a} log n)  [equal work]\nCase 3: f(n) = Ω(n^{log_b a + ε})  →  T(n) = Θ(f(n))  [work dominates]\n\nExamples: Merge sort T(n)=2T(n/2)+n → Θ(n log n); Strassen T(n)=7T(n/2)+n² → Θ(n^{log_2 7})"),
        ("Constraint Category", 2,
         "Dynamical (Di): the Master Theorem solves recurrence relations — the discrete dynamical system T(n) evolves through recursive subdivision. The three cases correspond to three dynamical regimes: subproblem overhead dominated, balanced, and top-level-work dominated. The critical exponent log_b a is the effective dimension of the recursion tree — the fractal dimension of the recursive decomposition."),
        ("DS Cross-References", 3,
         "A1 (Square-Cube Law — the Master Theorem is the algorithmic analog: it relates how work scales with problem size through recursive subdivision, just as Square-Cube relates surface to volume through dimension change). C1 (Metabolic Scaling — both express how a complex process scales with size through a power law exponent; in both cases the exponent reflects the effective dimension of the underlying structure). H2 (Fractal Dimension — log_b a is the fractal dimension of the recursion tree; the Master Theorem is the computational version of fractal scaling)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: power-law-scaling\n\nThe Master Theorem shows that divide-and-conquer algorithms scale as power laws: T(n) = Θ(n^α) where α = log_b a is the critical exponent determined by the branching ratio a and subdivision factor b. This is algorithmically the same structure as metabolic scaling B ∝ M^α where α = D_eff/(D_eff+1). The recursion tree has a fractal structure with dimension log_b a, and the Master Theorem reads off the scaling from this dimension."),
        ("What The Math Says", 5,
         "The recurrence T(n) = aT(n/b) + f(n) describes an algorithm that splits each problem of size n into a subproblems of size n/b and does f(n) extra work. Unrolling the recursion creates a tree of depth log-base-b of n. At depth k, there are a-to-the-k nodes, each of size n over b-to-the-k, contributing a-to-the-k times f(n over b-to-the-k) total work. The total work is dominated by the level with the most work: if f(n) grows slower than n-to-the-log-base-b-of-a, the leaves (bottom) dominate and T(n) equals Theta of n-to-the-log-base-b-of-a. If f(n) grows proportionally, each level contributes equally and a log factor appears. If f(n) grows faster, the root dominates and T(n) equals Theta of f(n)."),
        ("Concept Tags", 6,
         "• master theorem\n• divide and conquer\n• recurrence relation\n• algorithm complexity\n• recursive algorithms\n• merge sort\n• Strassen algorithm\n• algorithmic scaling\n• recursion tree\n• CLRS"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "master theorem, divide and conquer, recurrence relation, algorithm complexity, recursive algorithms, merge sort, Strassen algorithm, algorithmic scaling, recursion tree, CLRS", 0),
        ("DS Facets", "mathematical_archetype", "power-law-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("analogous to", "CS5", "Master Theorem — Divide and Conquer Recurrences", "C1", "C1: Metabolic Scaling (Kleiber's Law)", "Both describe power-law scaling where the exponent reflects an effective dimension: in Kleiber's law α = D_eff/(D_eff+1); in the Master Theorem α = log_b a is the fractal dimension of the recursion tree."),
        ("implements", "CS5", "Master Theorem — Divide and Conquer Recurrences", "A1", "A1: Square-Cube Law", "The Square-Cube Law is the geometric version of recursive subdivision — surface scales as L² and volume as L³ when subdividing space. The Master Theorem generalises this to arbitrary branching ratios and work functions."),
        ("implements", "CS5", "Master Theorem — Divide and Conquer Recurrences", "H2", "H2: Fractal Dimension (d_f)", "The critical exponent log_b a in the Master Theorem is the fractal dimension of the algorithm's recursion tree — the Master Theorem is the algorithmic version of fractal dimension determining scaling behaviour."),
    ],
},

# ── SIGNAL PROCESSING / INFORMATION ───────────────────────────────────────

{
    "id": "CS6",
    "title": "Nyquist-Shannon Sampling Theorem",
    "filename": "CS6_nyquist_shannon_sampling.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "information · physics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "A continuous-time signal with maximum frequency component B Hz can be exactly reconstructed from discrete samples taken at a rate f_s ≥ 2B samples per second — the Nyquist rate (Nyquist, 1928; Shannon, 1949). Sampling below 2B causes aliasing: high-frequency components fold back into the low-frequency range, irreversibly corrupting the signal. The theorem is the mathematical foundation of all digital signal processing, telecommunications, and audio/video digitisation."),
        ("Mathematical Form", 1,
         "If x(t) is band-limited: X(f) = 0 for |f| > B\nThen: x(t) = Σ_n x(nT) · sinc((t − nT)/T),  T = 1/(2B)\n\nNyquist rate: f_s = 2B  (minimum sampling rate for perfect reconstruction)\nAliasing: f_s < 2B → components above f_s/2 appear as spurious lower-frequency aliases\nBandwidth-limited channel: capacity C = B log₂(1 + SNR)  (Shannon-Hartley, using Nyquist)"),
        ("Constraint Category", 2,
         "Informatic (In): the Nyquist theorem is an information-theoretic bound on the sampling of continuous signals. A signal with bandwidth B contains at most 2B independent numbers per second — this is the information content of the signal. Sampling at the Nyquist rate extracts exactly this information; lower sampling rates lose information irreversibly (aliasing is information destruction)."),
        ("DS Cross-References", 3,
         "INFO3 (Shannon Noisy-Channel Coding Theorem — Shannon-Hartley C = B log₂(1+SNR) combines Nyquist bandwidth B with Shannon's capacity formula; the Nyquist theorem determines how many independent channel uses per second are possible). QM2 (Heisenberg Uncertainty Principle — both are time-frequency uncertainty bounds: Nyquist says bandwidth B requires 2B samples/second; Heisenberg says Δt·Δν ≥ 1/2; they are the classical and quantum versions of the same time-frequency duality). INFO1 (Shannon Entropy — the information content per sample is log₂(1+SNR) bits; Nyquist determines the sample rate, Shannon the information per sample)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nThe Nyquist rate 2B is a hard physical lower bound on sampling: no reconstruction is possible below it regardless of processing power. Like a thermodynamic bound, it is universal (applies to all band-limited signals), tight (achievable by sinc interpolation), and expressed as a rate (information per unit time). The aliasing that occurs below the Nyquist rate is an irreversible information loss — the computational analog of thermodynamic irreversibility."),
        ("What The Math Says", 5,
         "A signal x(t) is band-limited to B Hz if its Fourier transform X(f) is zero for all frequencies above B. By sampling x at times n divided by 2B (the Nyquist rate), we collect x(0), x(1/2B), x(2/2B), and so on. The signal can be perfectly reconstructed from these samples using sinc interpolation: x(t) equals the sum over all integers n of x(n/2B) times sinc(2Bt minus n). The sinc function sin(pi*x) over (pi*x) acts as a perfect interpolation filter — it is the ideal low-pass filter. If the sampling rate falls below 2B, frequencies above half the sampling rate alias: a 3B Hz component sampled at 2B appears as a B Hz component. This aliasing is not a numerical error but an information-theoretic impossibility: insufficient samples simply cannot distinguish high-frequency from low-frequency components."),
        ("Concept Tags", 6,
         "• Nyquist-Shannon sampling theorem\n• Nyquist rate\n• aliasing\n• band-limited signal\n• digital signal processing\n• sinc interpolation\n• sampling frequency\n• time-frequency duality\n• reconstruction theorem\n• Shannon-Nyquist"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "Nyquist-Shannon sampling theorem, Nyquist rate, aliasing, band-limited signal, digital signal processing, sinc interpolation, sampling frequency, time-frequency duality, reconstruction theorem, Shannon-Nyquist", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("derives from", "CS6", "Nyquist-Shannon Sampling Theorem", "INFO3", "Shannon Noisy-Channel Coding Theorem", "Shannon-Hartley C = B log₂(1+SNR) combines the Nyquist bandwidth (samples/second) with Shannon information (bits/sample); the Nyquist theorem determines the temporal information rate."),
        ("analogous to", "CS6", "Nyquist-Shannon Sampling Theorem", "QM2", "Heisenberg Uncertainty Principle", "Both express time-frequency duality as a hard bound: Nyquist requires Δt ≤ 1/(2B) for bandwidth B; Heisenberg requires Δt·Δν ≥ 1/2. They are the classical and quantum versions of the same Fourier uncertainty principle."),
        ("implements", "CS6", "Nyquist-Shannon Sampling Theorem", "INFO1", "Shannon Entropy", "The information content of a sampled signal is determined by Nyquist (how many samples/second) times Shannon (how many bits/sample = log₂(1+SNR)): together they give the total information rate in bits per second."),
    ],
},

# ── DISTRIBUTED SYSTEMS ────────────────────────────────────────────────────

{
    "id": "CS7",
    "title": "CAP Theorem",
    "filename": "CS7_cap_theorem.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "A distributed data store cannot simultaneously guarantee all three of: Consistency (every read returns the most recent write or an error), Availability (every request receives a non-error response), and Partition tolerance (the system continues operating despite network partitions that prevent communication between nodes). Any practical distributed system must choose two of the three (Brewer conjecture, 2000; proved Gilbert & Lynch, 2002). In the presence of partitions — which are unavoidable in real networks — a system must choose between consistency and availability."),
        ("Mathematical Form", 1,
         "CAP: ¬(C ∧ A ∧ P)  — at most two of three simultaneously\n\nWith partitions (unavoidable in practice):\n  CP systems: consistent + partition-tolerant (sacrifice availability: return errors during partitions)\n  AP systems: available + partition-tolerant (sacrifice consistency: may return stale data)\n  CA systems: only possible without network partitions (unrealistic for distributed systems)\n\nFormal: in an asynchronous network, ∄ algorithm guaranteeing all three."),
        ("Constraint Category", 2,
         "Coordination (Co): CAP is a coordination constraint — consistency requires coordinating all nodes to agree on the current state, which is impossible during a partition without sacrificing availability. The theorem captures the fundamental tension between distributed coordination and resilience."),
        ("DS Cross-References", 3,
         "F1 (Ashby's Law of Requisite Variety — a distributed system needs sufficient coordination complexity (variety) to maintain consistency; partitions reduce the available variety, forcing a trade-off). CS12 (FLP Impossibility — FLP proves impossibility of consensus with crash failures; CAP is the consistency/availability consequence when network partitions occur). BIO10 (Homeostasis — distributed biological systems (e.g., immune coordination, multi-organ regulation) face analogous trade-offs between consistent global state and resilient local response). TD3 (Second Law — maintaining global consistency in the presence of partitions requires entropy-reducing coordination that becomes thermodynamically costly)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe CAP theorem is a conservation constraint: C + A + P ≤ 2 (in a rough Boolean sense). Gaining one property requires sacrificing another — the total is conserved. This is the distributed systems analog of Heisenberg's uncertainty: you cannot simultaneously maximise all three properties of a distributed system. The theorem represents an impossibility conservation: no engineering solution eliminates the trade-off."),
        ("What The Math Says", 5,
         "Gilbert and Lynch's formal proof models the distributed system as a set of nodes communicating over a network. They consider a two-node system with a read-write register. During a partition — when no messages can pass between the two nodes — one node receives a write and must update its state. When a client reads from the other node, that node cannot know about the write. If the system is available (must respond to the read) and partition-tolerant (must operate during partition), it may return a stale value — violating consistency. Conversely, to maintain consistency, the non-updated node must refuse to answer — violating availability. Therefore, consistency and availability cannot both hold during a partition."),
        ("Concept Tags", 6,
         "• CAP theorem\n• Brewer conjecture\n• distributed systems\n• consistency availability partition\n• network partition\n• distributed consensus\n• AP systems\n• CP systems\n• Gilbert Lynch proof\n• distributed trade-offs"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Co", 0),
        ("entries", "concept_tags", "CAP theorem, Brewer conjecture, distributed systems, consistency availability partition, network partition, distributed consensus, AP systems, CP systems, Gilbert Lynch proof, distributed trade-offs", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "CS7", "CAP Theorem", "F1", "F1: Ashby's Law of Requisite Variety", "Ashby's Law requires that a controller's variety matches the disturbance variety; CAP instantiates this — a distributed system's coordination variety (consistency) is limited by partition tolerance, forcing trade-offs."),
        ("couples to", "CS7", "CAP Theorem", "CS12", "FLP Impossibility Theorem", "FLP shows consensus is impossible with crash failures in asynchronous systems; CAP shows that even without failures, network partitions force a consistency-availability trade-off. Together they define the limits of distributed agreement."),
        ("analogous to", "CS7", "CAP Theorem", "QM2", "Heisenberg Uncertainty Principle", "Both are irreducible trade-off constraints: Heisenberg between position and momentum; CAP between consistency and availability. Neither can be resolved by better engineering — they are structural impossibilities."),
    ],
},

{
    "id": "CS8",
    "title": "Amdahl's Law",
    "filename": "CS8_amdahl_law.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "The theoretical maximum speedup of a program using p processors is fundamentally limited by the serial fraction of the program: if fraction f can be parallelised, maximum speedup S(p) = 1/((1−f) + f/p), which approaches 1/(1−f) as p → ∞ (Amdahl, 1967). A program with 10% serial code can never exceed 10× speedup no matter how many processors are used. Amdahl's Law explains why parallel computing has diminishing returns and why serial bottlenecks dominate large-scale systems."),
        ("Mathematical Form", 1,
         "S(p) = 1 / ((1 − f) + f/p)\n\nAsymptotic limit: S_max = 1 / (1 − f)  as p → ∞\nLatency: T(p) = T_serial · ((1 − f) + f/p)\n\nGustafson's Law (weak scaling): S(p) = p − f(p − 1)  (larger problem for larger p)\nEfficiency: E(p) = S(p)/p → 0 as p → ∞  (efficiency always drops with scale)"),
        ("Constraint Category", 2,
         "Thermodynamic bound (Th): the serial fraction 1−f is a hard ceiling on speedup — an irreducible overhead analogous to a thermodynamic inefficiency. Like Carnot efficiency, Amdahl's bound cannot be exceeded regardless of the parallel architecture. The law establishes that serial code is the limiting resource in parallel computation."),
        ("DS Cross-References", 3,
         "C1 (Metabolic Scaling — both relate system performance to a power law of resources; Amdahl is the computational analog of metabolic scaling: both show sublinear returns on increasing resources). E1 (Moore's Law — Moore's Law increases single-processor performance; Amdahl's Law determines how much of that increase benefits parallel workloads). E2 (Koomey's Law — Koomey describes power efficiency scaling; Amdahl limits the effective speedup from more (efficient) processors). C2 (Urban Scaling — both describe sublinear scaling: urban productivity ~ population^0.85; parallel speedup ~ processors^{f})."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: dimensional-scaling\n\nAmdahl's Law is a dimensional scaling law: speedup S(p) scales sub-linearly with processor count p, with the critical parameter being the serial fraction 1−f. As p increases, the f/p term vanishes and S approaches the hard ceiling 1/(1−f). This is the computational version of resource saturation — adding more of a resource (processors) has diminishing returns when the system is limited by a non-scalable component."),
        ("What The Math Says", 5,
         "Suppose a program has total serial execution time T. A fraction f of the work can be parallelised; fraction 1 minus f must run serially. With p processors, the parallel part takes f times T over p and the serial part takes (1 minus f) times T. Total time is T times (1 minus f plus f over p). Speedup is original time over new time: 1 divided by (1 minus f plus f over p). As p goes to infinity, speedup approaches 1 over (1 minus f). For f = 0.9, maximum speedup is 10; for f = 0.99, maximum speedup is 100 — but achieving the second requires 100× more processors and nearly perfect parallelism. Gustafson noted that in practice, larger problem sizes proportionally increase the parallelisable fraction, giving better scaling on scientific workloads."),
        ("Concept Tags", 6,
         "• Amdahl's law\n• parallel computing\n• speedup scaling\n• serial fraction\n• parallelisation limit\n• Gustafson's law\n• processor scaling\n• computational efficiency\n• parallel overhead\n• diminishing returns"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Amdahl's law, parallel computing, speedup scaling, serial fraction, parallelisation limit, Gustafson's law, processor scaling, computational efficiency, parallel overhead, diminishing returns", 0),
        ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("analogous to", "CS8", "Amdahl's Law", "C1", "C1: Metabolic Scaling (Kleiber's Law)", "Both are sublinear resource-scaling laws: Kleiber's law B ∝ M^{3/4} shows metabolic rate scales sublinearly with mass; Amdahl's law shows computational speedup scales sublinearly with processors — both reflect the cost of coordination overhead."),
        ("couples to", "CS8", "Amdahl's Law", "E1", "E1: Moore's Law", "Moore's Law increases processor count and single-core performance; Amdahl's Law determines how much benefit a parallel program actually gains — together they predict the effective computational progress for parallel workloads."),
        ("analogous to", "CS8", "Amdahl's Law", "TD8", "TD8: Carnot's Theorem", "Both define hard efficiency ceilings: Carnot efficiency 1 − T_c/T_h bounds heat engine efficiency; Amdahl's ceiling 1/(1−f) bounds parallel speedup. Both cannot be exceeded regardless of engineering improvements."),
    ],
},

{
    "id": "CS9",
    "title": "Little's Law",
    "filename": "CS9_little_law.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "In any stable system where items arrive and depart, the long-run average number of items L in the system equals the long-run average arrival rate λ times the long-run average time W each item spends in the system: L = λW (Little, 1961). This holds regardless of arrival distribution, service distribution, number of servers, queue discipline (FIFO, LIFO, random), or any other system detail — it is a universal flow conservation law."),
        ("Mathematical Form", 1,
         "L = λ · W\n\nwhere:\n  L = average number of items in system (queue + service)\n  λ = average arrival rate (items per unit time)\n  W = average time in system (waiting + service)\n\nApplied to queue only: L_q = λ · W_q\nApplied to service only: L_s = λ · W_s\nStability condition: λ < μ  (arrival rate < service rate)"),
        ("Constraint Category", 2,
         "Dynamical (Di): Little's Law is a flow balance equation — a conservation law for items moving through a system. It emerges from the equality of the time-average number of items and the arrival-rate-weighted average sojourn time, regardless of the system's internal dynamics. It is the queueing analog of the continuity equation in fluid mechanics."),
        ("DS Cross-References", 3,
         "FM2 (Bernoulli's Principle — both are flow conservation laws: Bernoulli for fluid flow, Little's Law for discrete items in queues; both relate flow rate, quantity, and time/pressure). DM1 (Fick's Laws of Diffusion — Fick's first law J = −D·∇c relates flux to concentration gradient; Little's Law L = λW relates population to flow rate — both are conservation equations for transported quantities). C1 (Metabolic Scaling — blood circulation obeys Little's Law: average red blood cell count in vessels = arrival rate × average transit time; metabolic scaling determines the transit time scaling with body size)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nLittle's Law is a conservation law for items in a system: L = λW holds exactly as a time-average identity, regardless of any distributional assumptions. It is the most general queueing result precisely because it requires only flow balance — the same number of items enter as leave in the long run. This universality makes it the flow-conservation analog of charge conservation in electromagnetism."),
        ("What The Math Says", 5,
         "Consider any system in steady state where items arrive at average rate lambda and each item spends average time W inside. Define L(t) as the number of items in the system at time t. Little's theorem proves that the time average of L(t) equals lambda times W, using a simple geometric argument: the total area under the L(t) curve over a long time T approximately equals the number of arrivals N(T) in that time times the average sojourn time W, since each arrival contributes W to the area. Dividing by T: average L equals N(T)/T times W, which equals lambda times W as T goes to infinity. The remarkable fact is that no assumptions are needed about arrival distributions (Poisson, deterministic, bursty), service time distributions, or queuing discipline — the law holds universally."),
        ("Concept Tags", 6,
         "• Little's law\n• queueing theory\n• flow conservation\n• average number in system\n• arrival rate\n• sojourn time\n• stable system\n• universal queueing law\n• throughput\n• performance analysis"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "Little's law, queueing theory, flow conservation, average number in system, arrival rate, sojourn time, stable system, universal queueing law, throughput, performance analysis", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "CS9", "Little's Law", "FM2", "FM2: Bernoulli's Principle", "Both are flow conservation laws: Bernoulli relates pressure, velocity, and height for fluid flow; Little's Law relates average count, arrival rate, and sojourn time for item flow — both express conservation along flow lines."),
        ("analogous to", "CS9", "Little's Law", "DM1", "DM1: Fick's Laws of Diffusion", "Fick's law J = −D∇c relates flux to concentration; Little's L = λW relates population to flow rate — both are continuity equations expressing conservation of transported quantities."),
        ("couples to", "CS9", "Little's Law", "C1", "C1: Metabolic Scaling (Kleiber's Law)", "Blood circulation obeys Little's Law: the average number of red blood cells in a vessel segment equals the transit rate times the sojourn time; metabolic scaling determines how these quantities scale with body mass."),
    ],
},

{
    "id": "CS10",
    "title": "No Free Lunch Theorem",
    "filename": "CS10_no_free_lunch.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "For any two optimisation algorithms A and B, when their performance is averaged uniformly over all possible objective functions, they perform identically (Wolpert & Macready, 1997). Any algorithm that outperforms random search on some functions must underperform on equally many others. There is no universally best optimisation algorithm — performance above average on one class of problems must be paid for by below-average performance on others."),
        ("Mathematical Form", 1,
         "NFL: Σ_f P(d^m_y | f, m, a₁) = Σ_f P(d^m_y | f, m, a₂)  for all a₁, a₂\n\nwhere d^m_y is the sequence of objective values encountered in m steps,\nf is the objective function, a is the algorithm.\n\nImplication: E_f[performance(a₁)] = E_f[performance(a₂)]\nfor any two algorithms a₁, a₂ when averaged over all f uniformly.\n\nMachine learning version: no classifier is universally best across all data-generating distributions."),
        ("Constraint Category", 2,
         "Informatic (In): the NFL theorem is an information-theoretic constraint — without prior knowledge about the problem structure (the distribution over f), no algorithm can outperform random search. All performance gains from algorithms come from exploiting problem structure, not from algorithmic ingenuity alone. The theorem forces explicit acknowledgement of assumptions about the problem domain."),
        ("DS Cross-References", 3,
         "AM1 (Principle of Least Action — both are extremal principles bounded by the space of possibilities: least action selects the optimal path in configuration space; NFL proves that over all possible spaces, no single selection strategy is uniformly optimal). TD3 (Second Law — both are no-free-something theorems: the Second Law says no free energy (entropy always increases); NFL says no free performance (gains must be paid for elsewhere)). STAT1 (Maximum Entropy Principle — MaxEnt and NFL are complementary: MaxEnt specifies the least-biased prior when constraints are known; NFL shows that without such constraints, no algorithm has an edge)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe total performance of any algorithm, summed uniformly over all objective functions, is conserved — it equals the performance of random search. Performance is zero-sum across the space of all functions: gaining on one region must be paid for in another. This is a conservation law in algorithm space: the integral of performance over all functions is constant regardless of the algorithm."),
        ("What The Math Says", 5,
         "For any algorithm a and any performance measure based on the sequence of objective values encountered, the sum over all possible objective functions f of the probability of obtaining output d given f and algorithm a is the same for every algorithm. This means: evaluate any algorithm on every possible function; add up the scores. The total is identical for random search and for the most sophisticated algorithm. The implication is that algorithms succeed only by exploiting structure in the problem distribution — inductive bias. A neural network trained on image data performs well because image data has specific statistical structure; applied to random functions, it performs no better than guessing. The NFL theorem is the formal statement that there is no inductive bias that is universally correct."),
        ("Concept Tags", 6,
         "• no free lunch theorem\n• Wolpert Macready\n• optimisation limits\n• inductive bias\n• algorithm performance\n• universal optimiser impossibility\n• machine learning generalisation\n• problem structure\n• search algorithm\n• function distribution"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "no free lunch theorem, Wolpert Macready, optimisation limits, inductive bias, algorithm performance, universal optimiser impossibility, machine learning generalisation, problem structure, search algorithm, function distribution", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "CS10", "No Free Lunch Theorem", "TD3", "Second Law of Thermodynamics", "Both are no-free-something conservation laws: the Second Law forbids perpetual free energy extraction; the NFL theorem forbids perpetual free performance extraction — any gain in one domain requires an equal loss elsewhere."),
        ("analogous to", "CS10", "No Free Lunch Theorem", "AM1", "Principle of Least Action", "Both are optimisation principles bounded by phase space: least action finds the optimal path given dynamics; NFL shows that without knowledge of the dynamics (function distribution), no strategy is optimal — the action can only be minimised relative to a known Lagrangian."),
        ("implements", "CS10", "No Free Lunch Theorem", "STAT1", "Maximum Entropy Principle", "MaxEnt specifies the least-biased distribution given known constraints; NFL formalises why this is necessary — without assumed structure (constraints), all algorithms are equivalent, and MaxEnt's uniformity is the only defensible choice."),
    ],
},

{
    "id": "CS11",
    "title": "Comparison Sort Lower Bound — Ω(n log n)",
    "filename": "CS11_sort_lower_bound.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "Any algorithm that sorts n elements solely by pairwise comparisons requires at least Ω(n log n) comparisons in the worst case (Knuth, 1973). This lower bound is information-theoretic: to determine the correct sorted order among n! equally likely permutations requires at least log₂(n!) ≈ n log₂ n bits of information, and each comparison extracts at most 1 bit. The bound is tight — Merge sort and Heapsort achieve Θ(n log n) comparisons in all cases."),
        ("Mathematical Form", 1,
         "Decision tree model: any comparison sort corresponds to a binary decision tree\nTree height ≥ log₂(n!)  (must have ≥ n! leaves to distinguish all orderings)\nStirling: log₂(n!) = n log₂ n − n log₂ e + O(log n)\nTherefore: any comparison sort is Ω(n log n)\n\nAchieved by: Merge sort, Heap sort — both Θ(n log n) in worst/average case\nNon-comparison sorts: Radix, Counting, Bucket — can beat Ω(n log n) using key structure"),
        ("Constraint Category", 2,
         "Informatic (In): the lower bound is information-theoretic — distinguishing n! orderings requires extracting log₂(n!) bits of information. Each comparison is a binary question (is element a < element b?) extracting exactly 1 bit. The total information needed divided by information per step gives the lower bound. This is a direct application of Shannon entropy to algorithm complexity."),
        ("DS Cross-References", 3,
         "INFO1 (Shannon Entropy — the proof uses entropy: log₂(n!) bits are needed to sort n elements; the lower bound is the entropy of the uniform distribution over n! permutations). INFO2 (Source Coding Theorem — the lower bound proof mirrors source coding: you cannot do better than H bits to distinguish H-entropy outcomes; sorting is a special case of optimal encoding of permutation space). B5 (Landauer's Principle — each comparison is an irreversible information operation; the Ω(n log n) minimum comparisons times kT ln 2 joules per comparison gives the minimum thermodynamic cost of sorting)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: thermodynamic-bound\n\nΩ(n log n) is a hard lower bound on comparison-based sorting — a computational thermodynamic floor. Like thermodynamic bounds, it: (1) is universal (applies to all comparison algorithms), (2) is tight (achieved by Merge sort), (3) emerges from information content (log₂(n!) bits needed). Non-comparison sorts escape the bound by using additional information about key structure — analogous to using specific physical properties to bypass thermodynamic efficiency limits."),
        ("What The Math Says", 5,
         "Model any comparison sort as a binary decision tree where each internal node represents a comparison and each leaf represents a final sorted ordering. There are n-factorial possible orderings of n elements, so the tree must have at least n-factorial leaves. A binary tree with at least n-factorial leaves has height at least log base 2 of n-factorial. By Stirling's approximation, log base 2 of n-factorial equals n times log base 2 of n minus n times log base 2 of e plus lower-order terms — this is Theta of n log n. Therefore any comparison sort takes at least Omega of n log n comparisons. The bound is tight: Merge sort achieves exactly Theta of n log n in worst and average cases. Sorting algorithms that use structure beyond comparisons (Radix sort, Counting sort) can achieve linear time by extracting more than 1 bit per step."),
        ("Concept Tags", 6,
         "• sorting lower bound\n• comparison sort\n• omega n log n\n• decision tree model\n• information-theoretic lower bound\n• merge sort\n• heap sort\n• permutation entropy\n• Stirling approximation\n• optimal sorting"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "In", 0),
        ("entries", "concept_tags", "sorting lower bound, comparison sort, omega n log n, decision tree model, information-theoretic lower bound, merge sort, heap sort, permutation entropy, Stirling approximation, optimal sorting", 0),
        ("DS Facets", "mathematical_archetype", "thermodynamic-bound", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("derives from", "CS11", "Comparison Sort Lower Bound — Ω(n log n)", "INFO1", "Shannon Entropy", "The lower bound is the entropy of the uniform distribution over n! permutations: H = log₂(n!) ≈ n log₂ n bits. Each comparison extracts 1 bit, so n log n comparisons are needed — direct application of Shannon entropy as a lower bound."),
        ("implements", "CS11", "Comparison Sort Lower Bound — Ω(n log n)", "INFO2", "Shannon Source Coding Theorem", "The source coding theorem says you need at least H bits to encode an H-entropy source; sorting is encoding the correct permutation from H = log₂(n!) bits of entropy — the sort bound is source coding applied to permutation space."),
        ("analogous to", "CS11", "Comparison Sort Lower Bound — Ω(n log n)", "B5", "B5: Landauer's Principle", "Each comparison is an irreversible binary decision extracting 1 bit of information; Landauer's principle assigns minimum energy kT ln 2 to each irreversible bit operation — the Ω(n log n) bound gives the minimum thermodynamic cost of sorting."),
    ],
},

{
    "id": "CS12",
    "title": "FLP Impossibility Theorem",
    "filename": "CS12_flp_impossibility.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "In a completely asynchronous distributed system — where message delivery delays are unbounded but messages are eventually delivered — there is no deterministic algorithm that guarantees consensus (agreement, validity, termination) even if at most one process may fail by crashing and stopping (Fischer, Lynch, Paterson, 1985). The FLP theorem is considered one of the most important impossibility results in distributed computing. It explains why all practical consensus protocols make timing assumptions (Paxos, Raft) or use randomisation (Ben-Or's algorithm)."),
        ("Mathematical Form", 1,
         "Model: asynchronous system, processes communicate by message passing,\nat most f = 1 process may crash-fail.\n\nConsensus requirements:\n  Agreement: all non-faulty processes decide the same value\n  Validity: if all processes propose v, then v is decided\n  Termination: every non-faulty process eventually decides\n\nFLP theorem: ∄ deterministic algorithm satisfying all three in this model.\n\nProof strategy: show any algorithm has a bivalent initial configuration\nthat can be extended to remain bivalent arbitrarily long."),
        ("Constraint Category", 2,
         "Coordination (Co): FLP captures the fundamental impossibility of coordination under asynchrony and failure. In asynchronous systems, slow message delivery and process failure are indistinguishable — you cannot tell if a process is slow or dead. This ambiguity makes it impossible to simultaneously guarantee termination (liveness) and agreement (safety) in the presence of any failures."),
        ("DS Cross-References", 3,
         "CS7 (CAP Theorem — FLP is the foundational impossibility that motivates CAP: consensus is needed for consistency, but FLP makes it impossible under asynchrony and failures, forcing the CAP trade-off). CS14 (Byzantine Fault Tolerance — FLP covers crash failures; Byzantine FT covers malicious failures which are strictly harder — if consensus is impossible for 1 crash failure, it is also impossible for 1 Byzantine failure). MATH4 (Gödel Incompleteness — both are impossibility results proved by self-referential construction: FLP uses a 'valence argument' to show an algorithm can always be kept in a undecided state, structurally similar to Gödel's undecidable sentence). CS1 (Church-Turing — FLP extends undecidability from single machines to distributed systems: just as Turing showed single algorithms have limits, FLP shows distributed algorithms have limits from failure and asynchrony)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nFLP is a conservation impossibility: the three consensus properties (agreement, validity, termination) cannot all be conserved simultaneously in an asynchronous faulty system. The proof shows that any algorithm always has reachable states from which it can be forced to remain undecided — termination (liveness) can always be sacrificed to maintain safety. The impossibility is conserved under all algorithmic strategies."),
        ("What The Math Says", 5,
         "The FLP proof proceeds by defining the 'valence' of a configuration: a configuration is 0-valent if all continuations lead to deciding 0, 1-valent if all lead to deciding 1, and bivalent if both outcomes are reachable. First, the authors show every consensus algorithm must have a bivalent initial configuration — an initial state from which both outcomes are still possible. Second, they show that from any bivalent configuration, the adversary (who controls message scheduling) can always find a next step that leads to another bivalent configuration, by exploiting the fact that a crashed process and a slow process are indistinguishable. Therefore, the algorithm can be kept in a bivalent (undecided) state forever — violating termination. Any algorithm that guarantees termination can be forced to violate agreement."),
        ("Concept Tags", 6,
         "• FLP impossibility\n• distributed consensus impossibility\n• Fischer Lynch Paterson\n• asynchronous distributed systems\n• crash failure\n• bivalent configuration\n• consensus protocol\n• Paxos Raft motivation\n• liveness safety tradeoff\n• fault tolerance impossibility"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Co", 0),
        ("entries", "concept_tags", "FLP impossibility, distributed consensus impossibility, Fischer Lynch Paterson, asynchronous distributed systems, crash failure, bivalent configuration, consensus protocol, Paxos Raft motivation, liveness safety tradeoff, fault tolerance impossibility", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "CS12", "FLP Impossibility Theorem", "CS7", "CAP Theorem", "FLP is the foundational impossibility underlying CAP: the inability to achieve consensus under asynchrony and failure (FLP) directly causes the consistency-availability trade-off in CAP — consistency requires consensus, which FLP makes impossible under partition + asynchrony."),
        ("analogous to", "CS12", "FLP Impossibility Theorem", "MATH4", "Gödel's Incompleteness Theorems", "Both are proved by maintaining an 'undecidable state' — Gödel's Gödel sentence remains neither provable nor disprovable; FLP's bivalent configuration remains neither 0-valent nor 1-valent. Both show that completeness (decidability/termination) is incompatible with consistency (soundness/agreement)."),
        ("couples to", "CS12", "FLP Impossibility Theorem", "CS14", "Byzantine Fault Tolerance", "FLP covers crash failures (processes stop and send no messages); Byzantine FT covers malicious failures (processes send arbitrary messages). Byzantine failures are strictly harder — FLP impossibility for crash failures implies impossibility for Byzantine failures without additional resources."),
    ],
},

{
    "id": "CS13",
    "title": "Perron-Frobenius Theorem",
    "filename": "CS13_perron_frobenius.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · computer science",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "For any square matrix A with strictly positive real entries (Perron, 1907), and more generally for non-negative irreducible matrices (Frobenius, 1912): (1) The spectral radius r(A) = max|λᵢ| is a simple eigenvalue — the Perron root. (2) The corresponding Perron eigenvector has all strictly positive components. (3) All other eigenvalues satisfy |λᵢ| < r(A). The Perron root dominates the long-run behaviour of A^n: the iteration converges to the Perron eigenvector direction. This theorem underlies PageRank, Leslie population matrices, Markov chain stationary distributions, and network centrality measures."),
        ("Mathematical Form", 1,
         "For non-negative irreducible matrix A:\n  ∃ unique r > 0  s.t.  Av = rv,  v > 0  (Perron root and vector)\n  |λᵢ| ≤ r  for all eigenvalues λᵢ,  with equality only for λ = r\n  A^n / r^n → v · uᵀ  as n → ∞  (convergence to rank-1 matrix)\n  \nPageRank: p = (1−d)/n · 1 + d · A · p  (fixed point of Perron-Frobenius iteration)\nMarkov: stationary distribution π satisfies πᵀP = πᵀ  (π = Perron vector of P)"),
        ("Constraint Category", 2,
         "Geometric (Ge): the Perron-Frobenius theorem is a statement about the geometry of the positive orthant — non-negative irreducible matrices preserve the cone of non-negative vectors and have a unique fixed direction (Perron eigenvector) within this cone. The theorem is the non-negative matrix version of the spectral theorem, with positivity replacing symmetry as the key condition."),
        ("DS Cross-References", 3,
         "C3 (Heavy-Tailed Distributions — in scale-free networks, the adjacency matrix has a Perron root proportional to the maximum degree; the Perron root controls how power-law degree distributions propagate through the network). BIO7 (Lotka-Volterra — stability of ecological equilibria is determined by the dominant eigenvalue of the community matrix; Perron-Frobenius gives the leading eigenvalue of interaction matrices with non-negative entries). BIO3 (Fisher's Fundamental Theorem — Leslie population matrices use Perron-Frobenius to compute population growth rates: the Perron root r is the long-run growth rate λ = e^r of the population vector)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: equilibrium-condition\n\nThe Perron-Frobenius theorem establishes a unique positive equilibrium: repeated application of A (normalised) converges to the Perron eigenvector regardless of starting direction in the positive orthant. This is a global attractor in the projective positive cone. The convergence rate is determined by the spectral gap r − |λ₂| — larger gap means faster convergence to equilibrium."),
        ("What The Math Says", 5,
         "An irreducible non-negative matrix A has the property that from any index i you can reach any index j by multiplying matrix entries: the directed graph defined by A is strongly connected. Perron's theorem for positive matrices (all entries strictly greater than zero) guarantees a unique largest eigenvalue r, called the Perron root, which is real, positive, and simple (multiplicity one). The corresponding eigenvector v with Av = rv has all positive components. All other eigenvalues have strictly smaller magnitude. For the more general irreducible case (Frobenius), some other eigenvalues may have magnitude equal to r but their number is the period of A. The power iteration A-to-the-n applied to any initial positive vector, after normalising, converges to v. This is the basis of PageRank: the ranking vector is the Perron eigenvector of the (modified) web link matrix."),
        ("Concept Tags", 6,
         "• Perron-Frobenius theorem\n• Perron root\n• non-negative matrix\n• dominant eigenvalue\n• irreducible matrix\n• PageRank\n• stationary distribution\n• spectral radius\n• Markov chain\n• population growth matrix"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Ge", 0),
        ("entries", "concept_tags", "Perron-Frobenius theorem, Perron root, non-negative matrix, dominant eigenvalue, irreducible matrix, PageRank, stationary distribution, spectral radius, Markov chain, population growth matrix", 0),
        ("DS Facets", "mathematical_archetype", "equilibrium-condition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("implements", "CS13", "Perron-Frobenius Theorem", "C3", "C3: Heavy-Tailed Distributions (Unified)", "In scale-free networks, the adjacency matrix has a Perron root proportional to the maximum degree; Perron-Frobenius explains how the power-law degree distribution generates a dominant eigenvalue that controls network dynamics and spreading processes."),
        ("couples to", "CS13", "Perron-Frobenius Theorem", "BIO7", "Lotka–Volterra Predator–Prey Equations", "Ecological community stability near equilibrium is determined by eigenvalues of the interaction matrix; Perron-Frobenius gives the dominant eigenvalue for non-negative matrices, characterising the leading mode of population dynamics."),
        ("implements", "CS13", "Perron-Frobenius Theorem", "BIO3", "Natural Selection — Fisher's Fundamental Theorem", "Leslie matrices (age-structured population models) apply Perron-Frobenius: the Perron root is the long-run population growth rate r, directly analogous to Fisher's increase in mean fitness. Both describe convergence to a dominant eigenvector (stable age distribution / gene frequency equilibrium)."),
    ],
},

{
    "id": "CS14",
    "title": "Byzantine Fault Tolerance",
    "filename": "CS14_byzantine_fault_tolerance.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "A distributed system of n nodes can reach consensus despite f Byzantine (arbitrarily malicious or faulty) nodes if and only if n ≥ 3f + 1 and the number of communication rounds is at least f + 1 (Lamport, Shostak, Pease, 1982). Byzantine faults are the hardest failure model: a Byzantine node may send contradictory messages, lie, collude, or behave arbitrarily. The 3f+1 bound is tight — with fewer nodes, no algorithm can distinguish a malicious minority from a correct majority. This theorem underlies blockchain consensus protocols, Byzantine-tolerant databases, and secure multi-party computation."),
        ("Mathematical Form", 1,
         "Byzantine consensus possible iff: n ≥ 3f + 1\n\nRequired: f < n/3  (fewer than one-third Byzantine nodes)\nCommunication rounds: ≥ f + 1\nMessage complexity: O(n²) per round (every node broadcasts to all)\n\nSynchronous model (oral messages): n ≥ 3f + 1\nAuthenticated messages (signed): n ≥ 2f + 1  (digital signatures break symmetry)\nSingle-bit consensus: achievable with n = 3f + 1 in O(f) rounds"),
        ("Constraint Category", 2,
         "Coordination (Co): Byzantine tolerance is the hardest distributed coordination problem — achieving consensus when up to f of the n participants may actively try to prevent it. The 3f+1 bound arises from the need to have a majority of non-faulty nodes in every quorum: with n = 3f+1, a majority f+1 can outvote up to f Byzantine nodes even when the f Byzantines maximally misbehave."),
        ("DS Cross-References", 3,
         "CS12 (FLP Impossibility — FLP covers crash failures; Byzantine faults are strictly harder. If consensus is impossible with 1 crash failure in asynchronous systems, it is also impossible with 1 Byzantine failure — Byzantine FT requires synchrony or randomisation, just like post-FLP consensus protocols). CS7 (CAP Theorem — Byzantine-fault-tolerant systems are a special case of consistent distributed systems; achieving BFT consistency while maintaining availability under Byzantine partitions is even harder than the standard CAP trade-off). F1 (Ashby's Law of Requisite Variety — the 3f+1 requirement can be read through Ashby's lens: the system needs sufficient variety (n nodes) to overcome f Byzantine agents' variety; n must exceed 3f to have strictly more non-Byzantine variety than Byzantine variety)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: conservation-law\n\nThe 3f+1 bound is a conservation constraint on consensus under Byzantine failure: the honest majority must be at least 2f+1 (to outvote f Byzantine nodes) plus f additional nodes to ensure this majority cannot be faked. Equivalently, n − f ≥ 2f + 1 → n ≥ 3f + 1. This is conserved: no algorithmic ingenuity reduces the requirement below n = 3f+1 for unauthenticated messages."),
        ("What The Math Says", 5,
         "The Byzantine Generals Problem frames consensus as: n generals must agree to attack or retreat; up to f are traitors who may lie. With 3 generals and 1 traitor, the loyal generals cannot distinguish which of the other two is lying — no consensus is possible. With 4 generals and 1 traitor, majority voting succeeds. In general, to handle f traitors you need n greater than or equal to 3f plus 1. The proof of impossibility for n less than 3f+1 partitions the nodes into three equal groups: Byzantine nodes can make group 1 think the decision should be 0 and group 2 think it should be 1, while group 3 sees conflicting messages. With fewer than 3f+1 nodes, no group has a strict majority. With digital signatures (authenticated messages), a Byzantine node cannot forge signatures, reducing the requirement to n greater than or equal to 2f+1, since signed messages are verifiable."),
        ("Concept Tags", 6,
         "• Byzantine fault tolerance\n• Byzantine generals problem\n• Lamport Shostak Pease\n• distributed consensus\n• Byzantine failure\n• malicious fault tolerance\n• 3f+1 bound\n• blockchain consensus\n• BFT protocol\n• fault tolerance"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Co", 0),
        ("entries", "concept_tags", "Byzantine fault tolerance, Byzantine generals problem, Lamport Shostak Pease, distributed consensus, Byzantine failure, malicious fault tolerance, 3f+1 bound, blockchain consensus, BFT protocol, fault tolerance", 0),
        ("DS Facets", "mathematical_archetype", "conservation-law", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "links": [
        ("generalizes", "CS14", "Byzantine Fault Tolerance", "CS12", "FLP Impossibility Theorem", "FLP shows consensus is impossible with 1 crash failure in asynchronous systems; Byzantine faults are strictly harder than crash failures. Byzantine FT extends FLP by requiring synchrony (or randomisation) AND the 3f+1 bound to overcome the stronger adversary."),
        ("implements", "CS14", "Byzantine Fault Tolerance", "F1", "F1: Ashby's Law of Requisite Variety", "Ashby's Law requires controller variety ≥ disturbance variety; Byzantine FT instantiates this: the system needs n − f ≥ 2f+1 honest nodes (honest variety) to overcome f Byzantine nodes (adversary variety) — n ≥ 3f+1 is the minimum requisite honest variety."),
        ("analogous to", "CS14", "Byzantine Fault Tolerance", "BIO10", "Homeostasis Principle", "Both maintain system integrity despite faulty components: homeostasis maintains physiological set-points despite cellular failures; Byzantine FT maintains consensus despite malicious node failures. Both require minimum redundancy (3f+1 nodes / N-fold homeostatic control) to sustain function."),
    ],
},

{
    "id": "CS15",
    "title": "Time Hierarchy Theorem",
    "filename": "CS15_time_hierarchy.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "computer science · mathematics",
    "status": "established",
    "confidence": "Tier 1",
    "type_group": "RL",
    "sections": [
        ("What It Claims", 0,
         "More time gives strictly more computational power: for any time-constructible function f(n), there exist decision problems solvable in O(f(n) log f(n)) time but not in O(f(n)) time (Hartmanis & Stearns, 1965). Consequently, the complexity classes are strictly nested: TIME(n) ⊊ TIME(n²) ⊊ TIME(n log n) ⊊ TIME(n²), and so on indefinitely. The theorem proves that the complexity hierarchy is infinite and non-collapsing — adding more time always increases the class of solvable problems."),
        ("Mathematical Form", 1,
         "If f(n) log f(n) = o(g(n)):\n  DTIME(f(n)) ⊊ DTIME(g(n))  (strict containment)\n\nConsequences:\n  TIME(n) ⊊ TIME(n²) ⊊ TIME(n³) ⊊ ... (strict polynomial hierarchy)\n  P = ∪_k TIME(n^k)  ⊊  EXP = ∪_k TIME(2^{n^k})  (P ≠ EXP, the only known separation)\n  \nSpace analogue (Savitch/Space Hierarchy): DSPACE(f) ⊊ DSPACE(g) if f = o(g) and f(n) ≥ log n"),
        ("Constraint Category", 2,
         "Dynamical (Di): the time hierarchy is a dynamical separation result — more computational steps yield a larger computational phase space. The hierarchy reflects the non-collapsibility of resource-bounded computation: each time class is a distinct dynamical regime with problems that cannot be solved in any shorter time. This is the computational version of the physical principle that longer processes can accomplish strictly more than shorter ones."),
        ("DS Cross-References", 3,
         "MATH4 (Gödel Incompleteness — the time hierarchy is proved by diagonalisation, the same technique as Gödel. The proof constructs a language that is not in TIME(f(n)) by enumerating all f(n)-time machines and building a language that differs from each — a computational analog of Gödel's self-referential construction). CS4 (Cook-Levin — the time hierarchy establishes that P ≠ EXP, which is the known part of the P vs NP landscape; Cook-Levin identifies what is hard in P vs NP; the hierarchy tells us the landscape is truly infinite). TD3 (Second Law — both express the irreversibility of resource expenditure: the Second Law says thermodynamic processes are irreversible; the time hierarchy says that problems requiring more time cannot be solved in less time — computational irreversibility mirrors thermodynamic irreversibility)."),
        ("Mathematical Archetype", 4,
         "Mathematical archetype: dimensional-scaling\n\nThe time hierarchy is a dimensional scaling result: computational power scales strictly with allocated time, and each time class represents a distinct computational dimension. Just as higher spatial dimensions contain strictly more geometric objects, higher time classes contain strictly more decision problems. The hierarchy TIME(n) ⊊ TIME(n²) ⊊ ... is infinite and strict — there is no dimension collapse."),
        ("What The Math Says", 5,
         "The proof uses diagonalisation over time-bounded Turing machines. Fix any time-constructible function f(n) — meaning a Turing machine can compute f(n) in O(f(n)) steps. Define the language L containing all strings x such that the x-th Turing machine M-x, when run on input x with a time limit of f(|x|) steps, does NOT accept. The language L is computable in O(f(n) log f(n)) time (simulating M-x with the log-factor overhead from universal simulation). But L differs from every f(n)-time machine M-x on input x — by construction, M-x accepts x if and only if x is not in L. Therefore no f(n)-time machine can decide L, but an f(n)log(f(n))-time machine can. This strict separation extends to all time functions, giving the infinite hierarchy."),
        ("Concept Tags", 6,
         "• time hierarchy theorem\n• Hartmanis Stearns\n• computational complexity hierarchy\n• DTIME complexity class\n• diagonalisation\n• strict complexity separation\n• P vs EXP\n• complexity class containment\n• resource-bounded computation\n• time-constructible function"),
    ],
    "properties": [
        ("DS Facets", "Constraint Category", "Di", 0),
        ("entries", "concept_tags", "time hierarchy theorem, Hartmanis Stearns, computational complexity hierarchy, DTIME complexity class, diagonalisation, strict complexity separation, P vs EXP, complexity class containment, resource-bounded computation, time-constructible function", 0),
        ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
        ("DS Facets", "dimensional_sensitivity", "D-invariant", 2),
    ],
    "links": [
        ("analogous to", "CS15", "Time Hierarchy Theorem", "MATH4", "Gödel's Incompleteness Theorems", "Both use diagonalisation to prove strict limits: Gödel builds a statement unprovable in F; the Time Hierarchy builds a language not computable in f(n) time. Both establish infinite non-collapsing hierarchies: Gödel's axiom hierarchy, Hartmanis-Stearns's time hierarchy."),
        ("implements", "CS15", "Time Hierarchy Theorem", "CS4", "Cook-Levin Theorem — NP-Completeness", "The time hierarchy proves P ≠ EXP (the only known unconditional separation), establishing that the polynomial hierarchy is a strict subset of exponential time. Cook-Levin identifies the NP-complete problems; the time hierarchy confirms the complexity landscape is truly infinite."),
        ("analogous to", "CS15", "Time Hierarchy Theorem", "TD3", "Second Law of Thermodynamics", "Both express the irreversibility of resource expenditure: the Second Law forbids undoing thermodynamic entropy at zero cost; the time hierarchy forbids solving higher-time problems in less time — computational time, like thermodynamic entropy, accumulates strictly and cannot be fully recovered."),
    ],
},

]  # end ENTRIES


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
    print(f"Inserting Chunk 3 ({len(ENTRIES)} entries) into:\n  {SOURCE_DB}\n")
    insert_entries(SOURCE_DB, ENTRIES)
