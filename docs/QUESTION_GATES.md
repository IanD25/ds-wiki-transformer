# Question Gates

> Two checks every candidate question, conjecture or claimed new angle must pass before it is treated as worth pursuing. Adopted 2026-10-18 by the owner. They apply to the Questions Raised Log, to Q- and P-series entries, and to any "this looks new" moment in a session.
>
> **Gate 1, the prior-art gate,** asks *has this been done?* Full rule: `memory/feedback_prior_art_gate.md`.
> **Gate 2, the worth-asking gate,** asks *if it hasn't been done, why not, and should it be?* It is new, and set out below.
>
> Order: Gate 1, then Gate 2. Gate 2 runs whenever Gate 1 does not return a clean RESTATEMENT — that is, after a verdict of NO PRIOR ART FOUND, ADJACENT / narrow-novel, or "open in the literature, but we see a new angle". A question reaches **PROCEED** only if it survives both.

---

## Gate 2 — the worth-asking gate

**The stance.** "No prior work found" is not evidence that a question is new or good. Absence usually has a reason, and the gate's job is to find it. Lean towards finding the reason. "I couldn't find one" is a weak result; record it as such.

Answer all five tests in writing, citing evidence, before giving a verdict.

### 1. Triviality — can it be answered in five minutes from something known?

Attempt the short derivation explicitly: an identity, a definition, a textbook theorem, dimensional analysis, a limiting case, a symmetry argument. If it falls out, it is a re-derivation (charter rule 2), not a question.

*Wiki precedents:* H5's two-process form is the elasticity-of-a-sum rule. P12's failure follows from β(λ) ≤ 1. CCA's first-order jump may be the order-parameter jump seen through S(k = 0) (pending test).

### 2. Absence — if no prior work was found, why not?

List every candidate explanation and check each one. Do not stop at the first.

| | Explanation | How to check |
|---|---|---|
| a | **We searched in the wrong words or field** | Re-search in the field's own vocabulary and in at least one adjacent field; check what the glossary says the term means there |
| b | **It is done, but not as a paper** — textbook exercise, review aside, lecture notes, thesis, folklore | Check standard textbooks, review articles' "open problems" and "known results" sections, dissertations |
| c | **It is too obvious to publish** | Would an expert answer it in one line? (see test 4) |
| d | **The premise is false or the question is ill-posed** | Test 3 |
| e | **Experts avoid it for a known reason** — intractable, unmeasurable, known confound, already settled negatively | Look for critiques, negative results, methods papers that warn against it |
| f | **The data or tools became available only recently** | When did the enabling dataset, instrument or method appear? |
| g | **It is genuinely unasked** | What remains after a–f are excluded with evidence |

Only **f** or **g** let a question proceed. If none of a–g can be identified with evidence, say so explicitly: an unexplained absence is a yellow flag, not a green one.

### 3. Is the question, or its expected answer, obvious or erroneous?

- **Well-posed?** Every term is defined, and the glossary sense is named (`[[g:…]]`), not a word that spans several mathematical objects.
- **Premise true?** *Precedent:* T5 planned to measure Ising exponents on the Sierpiński gasket, where T_c = 0.
- **Not vacuous?** The answer is not forced by definitions, and the question is not a category error. *Precedent:* treating BMR and MMR as two points on one scale.
- **Scoped?** "Any", "all" and "universal" claims are narrowed to what could actually be tested. *Precedent:* P7's "under any valid coarse-graining".

### 4. The expert view — would a working expert dismiss it, and why?

Write the one-sentence reply a domain expert would most likely give. Then find evidence for it: review articles, critiques, negative results, community statements, the reasons given in papers that chose *not* to do this. If experts ignore the question, name the reason and cite where it is stated. Claims about expert opinion need a source, not an impression.

### 5. Should it be asked at all?

- **Would either answer change anything?** State what a "yes" would forbid and what a "no" would forbid. If neither forbids anything, the question is decorative.
- **Is it decidable** with data and compute that can actually be obtained?
- **Is it worth the cost** compared with the other items in the log?

---

## Verdicts

| Verdict | Meaning | What happens |
|---|---|---|
| **PROCEED** | Worth asking, and not explained away by a–f | State in one sentence what is unasked and why the absence is real; plan the work |
| **RE-SCOPE** | Worth asking in a narrower or corrected form | Write the corrected question; run the gate on it |
| **FOLD** | Trivial, or answered somewhere we missed | Record it as a re-derivation or restatement and add the knowledge to the wiki |
| **DROP** | Ill-posed, vacuous, undecidable, or not worth asking | Record why, with a reason tag, so the record of what failed stays useful |

**Reason tags for DROP / FOLD** (add to the drift-pattern catalogue in `memory/feedback_diagnostic_labels.md` when first used): `trivial-from-known-result`, `premise-false`, `ill-posed`, `answer-forced-by-definition`, `expert-avoided-for-known-reason`, `undecidable-with-obtainable-data`, `already-settled-negative`, `found-under-other-vocabulary`.

**Recording.** Write the gate report next to the prior-art report in `docs/prior_art_reviews/` (one file per question, both gates). Set the question's status in `docs/QUESTIONS_RAISED_LOG.md`. A PROCEED is **provisional** until a second, independent search (different session, different vocabulary) fails to find the explanation: single-pass novelty verdicts have been wrong on this project before.
