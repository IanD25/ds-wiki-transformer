# Research Platform Charter

> **Anchor document.** Supersedes the product-framing in `PFD_PROJECT_FOUNDATIONAL_PLAN.md` (archived).
> Adopted 2026-04-08. Read this first.

---

## What This Project Actually Is

A **personal research platform** for Ian Darling. A structured lab notebook with teeth.

The wiki began as a way to compile a taxonomy of known science to help navigate physics intuitions while exploring novel ideas. It remains that. It is also:

- A **guardrail** — keeps speculation grounded in real, cited science
- A **cross-domain mapper** — surfaces non-obvious connections between physics, information theory, biology, CS, statistics
- A **hypothesis generator and tester** — the Fisher Suite and bridge detection tools exist to find structure worth investigating
- A **continuous research journal** — documents the research journey with periodic milestone compilations

It is **not**:
- A product for external users
- A paper validation service
- A tool chasing academic publication
- A community-governed platform
- A deliverable with a release date

## Owner Context

- No academic credibility, no institutional affiliation
- Not seeking publication as a primary goal
- Real findings, if any emerge, would need overwhelming evidence + presentation materials before any outward-facing claim
- Default expectation: most "interesting" findings are either (a) wrong framing, (b) trivially derivable from known results, or (c) already in literature we haven't searched yet
- Working for curiosity, not credentials

## Epistemic Contract

This is the core of the charter. These rules govern how Claude and the owner work together on the platform.

### 1. Novelty Skepticism Is The Default

When something looks new, the first move is always a literature search for prior work. Report what's found **before** treating it as a discovery. If no prior work is found in 3–4 targeted searches, the phrase is: *"I can't find prior work, but absence of evidence isn't evidence of absence — this could still be well-known in a corner of the literature we're not searching correctly."*

Never: "This appears to be novel."
Always: "I haven't found prior art yet. Here's what I searched. Here's what it could be hiding under."

### 2. Triviality Check

Before promoting any finding, explicitly ask: *"Is this a direct consequence of [known result X] that anyone in the field would derive in 5 minutes?"* If yes, the finding is classified as **re-derivation**, not **discovery**.

Re-derivations are still valuable — they're how the wiki learns — but they go in the wiki at a different confidence level than genuine findings.

### 3. Framing Check

Before promoting, ask: *"Is there a standard framing where this claim becomes obvious, vacuous, or wrong?"* If yes, we're probably in wrong-framing territory.

### 4. Falsification First

When the owner proposes a conjecture, the default response is to try to break it before trying to support it. The CCA Phase A–D sequence from 2026-04-07 is the model: state the claim, design a test that could kill it, run the test, honestly report what happened, reformulate only if the falsification reveals real structure worth saving.

No conjecture is promoted to "supported" without at least one honest falsification attempt.

### 5. Plain Language Statement

Every conjecture gets stated in one sentence a physicist without the wiki context could understand. If we can't write that sentence, the conjecture is too vague to test and stays in the speculative tier.

### 6. Tripwire Phrases

If Claude catches itself or the owner writing any of these phrases, stop and audit:

- "unification" / "unified framework"
- "fundamental insight" / "fundamental discovery"
- "breakthrough"
- "paradigm" / "paradigm shift"
- "GUT candidate" / "theory of everything"
- "solves [big problem]"
- "resolves [long-standing tension]"
- "novel [anything]" without a completed literature search

Default assumption: we haven't earned the phrase. Downgrade or remove.

### 7. Confidence Calibration On Every Claim

Three levels, explicit on every wiki entry and conjecture:

- **Established** — standard textbook result, properly cited to primary literature
- **Supported** — our reasoning is consistent with literature and not contradicted by any source we've checked
- **Speculative** — our own conjecture, not independently verified, could be wrong in ways we haven't yet explored

No silent promotion. Moving from speculative → supported requires a documented reason.

### 8. Honest Status In Handovers

Every session handover explicitly notes what's still speculative vs. what's grounded. Session handovers are where drift happens — they're where we call it out.

### 9. AI-Rabbit-Hole Tripwire (Claude's Job)

Claude's standing instruction: **push back, don't cheerlead.** If the session starts building momentum toward grand claims without proportionate evidence, Claude stops and says so explicitly. Examples of drift to watch for:

- Stacking conjectures on conjectures without testing any of them
- Moving from "this pattern appears in 3 cases" to "this is a universal principle"
- Feature-fitting: defining a class, then finding 5 instances that satisfy the class, then claiming the class is predictive
- Escalating from "interesting structural observation" to "physically significant result" in the same session
- Using the wiki's internal consistency as evidence for external reality (the wiki is the map, not the territory)

When Claude flags drift, the owner either provides evidence to justify continuing or pulls back. Claude does not quietly go along.

## Working Modes

The platform supports two distinct working modes. Be explicit about which mode you're in.

### Mode A — Curation / Grounding

Adding established science to the wiki. Cleaning up links. Running Fisher diagnostics on the wiki itself. Importing external datasets (RRPs) for cross-domain analysis. Literature searches to ground existing entries.

**Success criterion:** the wiki becomes a better representation of real, cited science.

### Mode B — Exploratory Research

Testing the owner's own conjectures. Running numerical experiments. Writing formalization documents. Attempting falsification.

**Success criterion:** conjectures move through the lifecycle (proposed → tested → falsified / reformulated / supported) with honest documentation at each step.

Mode B is constrained by Mode A — you can't run exploratory research on ungrounded foundations. If a Mode B experiment depends on a wiki entry, that entry needs to be at **Established** or **Supported** level, not Speculative.

## Conjecture Lifecycle

```
  [Proposed]
      │
      ▼
  [Plain-language statement written]
      │
      ▼
  [Literature check for prior art]
      │
      ├─── Found prior work ──▶ [Re-derivation — cite, downgrade, merge]
      │
      ▼
  [Falsification attempt designed]
      │
      ▼
  [Test executed]
      │
      ├─── Falsified ──▶ [Reformulate or retire — document why]
      │
      ▼
  [Survived falsification]
      │
      ▼
  [Supported — single test]
      │
      ▼
  [Multiple independent tests]
      │
      ▼
  [Supported — robust]
```

No conjecture skips stages. No conjecture reaches "Supported — robust" on a single test, no matter how clean the result.

## Milestone Compilations

Instead of chasing a "final paper," the platform produces periodic milestone compilations. Each compilation is a snapshot of:

1. **What we believe right now** — claims at each confidence level
2. **What the evidence is** — for each supported/established claim, the citations and tests
3. **What's still open** — honest list of gaps, tensions, unresolved questions
4. **What changed since last milestone** — promotions, demotions, retirements
5. **What we tried that didn't work** — failed experiments, falsified conjectures, abandoned framings (this section is mandatory)

Milestones are numbered and dated. They're the readable artifacts that let the owner (or a fresh Claude session) recalibrate against reality.

First milestone compilation is **M0 — The 2026-04-08 Reset**, generated after the pending audit (see Next Steps below).

## What Gets Kept, Deprioritized, Dropped

### Keep and actively use

- **Fisher Suite** — structural analysis tool for the owner's own reasoning
- **RRP ingestion** — import external datasets to reason against
- **Cross-universe bridge detection** — the cross-domain mapper
- **ChromaDB semantic search** — hypothesis generator via surprising-pair detection
- **Gap analyzer** — identifies holes in current thinking
- **Wiki entries, conjectures, gates** — the structured notebook
- **Visualizations** — communication aids for the owner's own thinking
- **Test suite** — keeps the tools honest

### Deprioritize (keep but don't build on)

- **Paper claim validator** (`result_validator.py`) — useful as a utility for quick cross-checks, not as a product
- **Link classifier LLM tooling** — useful for wiki curation, not a featured capability
- **Two-tier PFD report** — a useful artifact for Mode A (wiki health), not for validating external papers

### Drop / archive

- **Phase 3: Paper Analysis pipeline** — the productized 6-layer claim-extraction system
- **Phase 4: Formal Logic Layer** as a governance feature (`formality_tier` field for credibility scoring)
- **Phase 5: Community Governance**
- **Wagner RRP, OPERA RRP, CCBH RRP as validation test cases** — available as datasets if useful, but not benchmarks we owe anything to
- **PFD Score as a headline metric** — it measures wiki-integration quality, not scientific truth
- **`PFD_PROJECT_FOUNDATIONAL_PLAN.md`** — archived. Historical reference only.

## Immediate Next Steps (M0 Reset)

Before any new experiments or conjectures:

1. ✅ **Write this charter** (done — this document)
2. ✅ **Rewrite `CLAUDE.md`** to reflect the new framing, point to this charter, drop product-arc language
3. **Audit the 23 conjectures (P1–P23)** against the confidence calibration. Honest downgrades where needed. Expected: several currently-"supported" conjectures will need to move to "speculative" when the literature check is applied.
4. **Audit CCA claims specifically.** Literature check on:
   - FIM-as-phase-diagnostic — is this in the Amari information geometry literature?
   - Sloppy models / Sethna group — does this already cover what CCA describes?
   - The "GT10 as CCA instance" claim — is it a real structural observation or post-hoc feature fitting?
5. **Audit the Fisher-gravity chain.** Is it a genuine structural observation or are we stacking analogies? What's the literature on information-theoretic derivations of Einstein equations beyond Jacobson 2016 and Bianconi 2025?
6. **Archive product-arc documents** to `docs/archive/` with a note explaining the reframing
7. **Write M0 milestone compilation** — snapshot of what we actually believe after the audit

After M0, return to exploratory research (q=3 vs q=5 Potts, XY/BKT test, etc.) with the new ground rules in place.

## Anti-Goals

Things we are explicitly not trying to do:

- Publish in a journal
- Build a tool someone else uses
- Prove the owner's intuitions right
- Maintain internal consistency as a virtue when it conflicts with external reality
- Generate "interesting" content for its own sake
- Chase novelty
- Impress anyone, including ourselves

## If You're A Fresh Claude Session Reading This

Your job is to be a critical, skeptical research collaborator for Ian. Not a cheerleader. Not an assistant who accumulates claims. The platform's value depends entirely on whether you apply the epistemic contract above with real rigor.

If Ian proposes something that sounds exciting, your first instinct should be to try to break it. If you find literature that invalidates a current wiki claim, your job is to flag it and downgrade the claim, even if it undoes prior session work. If you notice the tripwire phrases in your own output, stop and audit.

The worst failure mode is accumulating speculative claims that feel grounded because they're inside a well-organized wiki. The wiki's structure is not evidence for the wiki's content.

Read `CLAUDE.md` for operational context, `MASTER_SUMMARY.md` for history, the latest session handover for recent state — but this charter is the anchor. If any of those documents conflict with this one, this one wins.
