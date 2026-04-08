> **⚠️ ARCHIVED 2026-04-08.** Phase 3 (paper analysis pipeline) has been retired along with the PFD product framing.
> See `docs/RESEARCH_PLATFORM_CHARTER.md` for the active mission. Historical reference only.

---

# Semantic Channel Finding (SCF) — PFD Phase 3 Design

**Document Version:** 1.0
**Date:** 2026-03-13
**Status:** Design proposal — pending Phase 3 milestone planning
**Author:** Ian Darling

---

## 1. What is Semantic Channel Finding?

Semantic Channel Finding (SCF) is a methodology developed in large-scale scientific
infrastructure (particle accelerators, multi-facility experiments) to solve the
**heterogeneous naming problem**: the same physical quantity is described by different
local conventions at different facilities, and querying across them requires mapping
local "channel addresses" to a shared semantic backbone.

The three core moves of SCF:

1. **Ontology Integration** — a formal shared vocabulary (core ontology) acts as a
   backbone. Local names are mapped to ontology nodes, not to each other directly.

2. **Intent Mapping** — queries are resolved against the ontology by intent, not
   keyword. "Beam position" resolves to the specific setpoint/readback channel at
   each facility without renaming legacy systems.

3. **Signal Amplification via Structure** — the ontology's relational structure
   amplifies the signal of a query: navigating ontology edges reveals connections
   that flat keyword search would miss.

---

## 2. PFD Is Already Doing SCF

The parallel is exact:

| SCF concept | PFD equivalent | Status |
|---|---|---|
| Core ontology (shared vocabulary) | DS Wiki (laws, methods, principles, axioms) | ✅ Built — 209 entries, 573 links |
| Local channels (facility-specific names) | RRP entries (paper-local terms, lab IDs) | ✅ Built — all parsers |
| Channel address discovery | Cross-universe bridges (BGE cosine → DS Wiki) | ✅ Built — Pass 2 |
| Intent mapping (query → channels) | `result_validator.py` claim→DS Wiki resolution | 🔧 Phase 3 target |
| Signal amplification via structure | Structural alignment scorer (link-type polarity) | ✅ Built — 2026-03-13 |
| Agentic cross-facility workflows | MCP tools (`fisher_analyze_node`, `fisher_sweep_rrp`) | ✅ Single-RRP; multi-RRP pending |
| Cross-facility unified queries | Multi-RRP ontology queries (Phase 3C below) | 📋 Designed |

**The critical difference from classical SCF:**
Classical SCF is *operationally* oriented — route a data request to the right channel.
PFD is *epistemically* oriented — assess the logical alignment of a claim against a
formal channel. The DS Wiki is not just a routing table; it encodes the *logical
structure* of scientific knowledge (tiers, link types, conjectures).

This makes PFD a **logical channel finder** — not just "which DS Wiki entry does this
paper entry semantically resemble?" but "does this paper entry *support*, *contest*, or
*extend* the principle it maps to?"

---

## 3. Why This Framing Matters

### 3.1 SPT vs. Structural Alignment — a case study

The Semantic Position Test (SPT) attempted to detect polarity by varying LLM framing
(neutral/supportive/critical variants) and comparing bridge scores. It failed because
BGE embeddings capture **topic proximity**, not **argument sign**.

The structural alignment scorer (`structural_alignment.py`) succeeds because it reads
polarity from the **RRP link graph** — which is exactly the SCF insight applied to
scientific validation: the ontology's relational structure (link types) carries the
signal that embedding distances cannot.

**SPT result (OPERA paper):** mean α = -0.654, 0 ALIGNED, 9 FLAT — noise.
**SA result (OPERA paper):** mean polarity = +0.217, 4 ALIGNED, 3 CONTESTED —
correctly identifies `original_ftl_claim_2011 CONTESTS QM5 @ -0.8599` and
`corrected_result_2012 ALIGNS QM5 @ +0.5879`.

### 3.2 The "channel quality" metric

In SCF, a channel mapping is good when the local name resolves unambiguously to a
specific ontology node. The bridge similarity score is PFD's channel quality metric.
But classical SCF only measures *resolution quality* (did we find the right channel?).
PFD adds *polarity quality* (does the paper's relationship to that channel make the
right logical claim?).

This is novel. Most semantic search systems return similarity; PFD returns
**signed similarity** — a score that is positive for alignment and negative for
contestation, grounded in the explicit link graph rather than inferred from prose.

---

## 4. Phase 3 Options — SCF-Grounded

The following options are ordered by value and build on each other. They should be
read as a menu, not a mandatory sequence — the project can stop after any option and
have a coherent, deployable system.

---

### Option 3A — Dynamic Channel Resolution (core Phase 3)

**What it is:** Make channel resolution live and on-demand rather than pre-built.
Currently, bridges are computed at parse time and stored in the RRP database. Option 3A
makes `result_validator.py` resolve a free-text claim to DS Wiki channels in real-time,
without requiring a pre-built RRP.

**Components:**
- `claim_extractor.py` — LLM-based structured claim parser (input: paper prose → output:
  `Claim(subject, relationship, object, confidence)`)
- Enhanced `result_validator.py` — takes a raw claim string, embeds it, queries
  ChromaDB, returns top-K DS Wiki channels with similarity + polarity inference
- **Mandatory human gate** (Foundational Plan §3.1): extracted claims presented for
  human confirmation before downstream processing
- Output: `ClaimResolution(claim, ds_wiki_entry, similarity, polarity_hint, confidence)`

**Polarity inference at this stage:** Since there is no pre-built link graph for a
free-text claim, polarity is inferred from linguistic cues in the claim text. This is
acknowledged as weaker than structural alignment — it is a heuristic, not a ground
truth. Claims with linguistic tension markers ("contradicts", "violates", "exceeds")
receive a provisional negative polarity flag for human review.

**Test case:** OPERA corrected paper — the claim "neutrino velocity is consistent with
c within uncertainties" should resolve to QM5 (Special Relativity) with positive
polarity; "neutrino velocity exceeds c by 6σ" should resolve to QM5 with negative
polarity flag.

**Vertical integration constraint (Foundational Plan §4.2):** Start with
thermodynamics + Special Relativity. Do not attempt universal claim resolution until
>80% of DS Wiki entries have `formality_tier` set.

**Deliverables:**
- `src/analysis/claim_extractor.py`
- Enhanced `src/analysis/result_validator.py`
- MCP tool: `pfd_validate_claim(claim_text) → ClaimResolution`
- Integration test: 10+ claims from OPERA paper, compared against SA results

---

### Option 3B — Structural Alignment in Tier-2 Report

**What it is:** Integrate the structural alignment scorer into the standard Tier-2
PFD report output. Currently `structural_alignment.py` runs as a standalone script.
Option 3B makes it a first-class section of every `--mode report` run.

**Components:**
- `fisher_report.py` — add `structural_alignment_section(rrp_db)` to `PFDReport`
- `tier2_report.py` — add SA visualization: signed bridge chart per entry (positive
  bars = aligns, negative bars = contests), DS Wiki heatmap with polarity color coding
- PFD Score — adjust Tier-2 contribution to include SA signal: papers with high mean
  polarity score higher (well-integrated papers that explicitly align with formal
  principles rank above papers that are merely topically similar)

**Why this matters:** The current Tier-2 score is unsigned — it measures how well-connected
the paper is to DS Wiki, not whether those connections are supportive or contestatory.
An RRP full of `would_have_violated` links to foundational laws could currently score
the same as one full of `is_consistent_with` links. SA polarity corrects this.

**Deliverables:**
- Updated `fisher_report.py` with SA section
- Updated `tier2_report.py` with signed bridge visualization
- Updated PFD Score formula (document in `ARCHITECTURE_DECISIONS.md`)

---

### Option 3C — Multi-RRP Ontology Queries

**What it is:** Enable queries that span multiple RRPs simultaneously, using DS Wiki
as the shared channel backbone. This is the full SCF vision: cross-facility queries
without renaming legacy data.

Example queries:
- "Which entries across all RRPs contest QM5 (Special Relativity)?"
- "Find all `independently_validates` chains that converge on the same DS Wiki node"
- "Which DS Wiki entries have the highest polarity consensus across all ingested papers?"

**Components:**
- `src/analysis/cross_rrp_query.py` — multi-RRP structural alignment aggregator
- DS Wiki entry "reputation score" — weighted sum of signed alignments from all RRPs
  that bridge to it (positive = consistently confirmed, negative = contested)
- MCP tool: `pfd_query_ontology(ds_entry_id, mode="contested|aligned|all") → cross-RRP summary`

**Why this is powerful:** The DS Wiki reputation score turns the knowledge graph into
a *living epistemological ledger*. Each validated RRP adds evidence for or against
each formal principle. Over time, consistently contested entries are flagged for review;
consistently confirmed entries gain confidence weight.

This is the feedback loop that makes PFD a self-improving system rather than a static
validator.

**Dependency:** Requires Option 3B (SA integrated into standard pipeline). Also
requires multiple RRPs with full prose descriptions — currently only OPERA paper has
these; the other RRPs need paper parsers.

**Deliverables:**
- `src/analysis/cross_rrp_query.py`
- DS Wiki reputation scores table in `wiki_history.db` (not ds_wiki.db — read-only)
- MCP tool for cross-RRP ontology queries

---

### Option 3D — Link-Type Weighted PFD Score (Phase 4 foundation)

**What it is:** Replace the current unsigned bridge-count Tier-2 metric with a
fully link-type-weighted score. This is the "formal annotations on RRP entries"
work flagged in Phase 4 of CLAUDE.md, pulled forward because the SA scorer now
provides the infrastructure.

**Revised PFD Score formula:**

```
Tier-2 Score (link-weighted) =
  Σ [bridge_sim(e, w) × |polarity(e)|] / N_bridged_entries
  × polarity_consensus_factor           # fraction of entries where sign is stable
  × coverage_factor                     # fraction of entries with ≥1 bridge > 0.75
```

The polarity_consensus_factor penalizes internally inconsistent papers (half the entries
contest a principle, half align with it — net neutral but genuinely confused).

**Note:** This is a meaningful change to the PFD Score formula and should be
implemented only after Option 3B is validated on ≥3 paper-based RRPs with full prose.
Premature formula changes before sufficient test data risk overfitting to OPERA.

**Deliverables:**
- Updated `fisher_report.py` PFD Score calculation
- Calibration study: rerun all existing RRPs, compare old vs. new scores
- Updated `ARCHITECTURE_DECISIONS.md`

---

## 5. Recommended Phase 3 Sequence

```
3A (Dynamic Channel Resolution — claim_extractor + result_validator)
    │
    ▼
3B (SA in Tier-2 Report — structural alignment as standard output)
    │
    ▼
3C (Multi-RRP Ontology Queries — cross-facility SCF)
    │
    ▼
3D (Link-Type Weighted PFD Score — Phase 4 foundation)
```

**Minimum viable Phase 3:** 3A alone delivers the paper validation use case.
**Full SCF system:** 3A + 3B + 3C. Option 3D is Phase 4 prep.

---

## 6. What Remains Outside SCF

SCF does not address:

- **Formal logic validation** (Phase 4) — verifying logical entailment chains, not
  just semantic channel proximity. This requires `formality_tier` annotations and
  a probabilistic logic engine.
- **Evidence sufficiency** (Phase 3 Layer 5 in Foundational Plan) — whether a paper's
  evidence base is sufficient to support its claims. SA polarity tells you *which way*
  a claim points; evidence sufficiency tells you *how strongly* it is supported.
- **Domain boundary validation** (Phase 3 Layer 6) — whether a claim is being
  applied outside its validity domain (e.g., thermodynamics applied to social systems).

These are distinct from channel finding and should remain in their own pipeline layers.

---

## 7. Relationship to Existing Architecture

```
DS Wiki (core ontology)
    │
    ├─ Pass 2: CrossUniverseQuery ──────── builds unsigned bridges (existing)
    │
    ├─ structural_alignment.py ─────────── adds polarity to bridges (built 2026-03-13)
    │
    ├─ Option 3A: result_validator.py ──── dynamic claim→channel resolution
    │
    ├─ Option 3B: fisher_report.py ─────── SA section in Tier-2 report
    │
    ├─ Option 3C: cross_rrp_query.py ───── multi-RRP ontology queries
    │
    └─ Option 3D: weighted PFD Score ───── link-type weighted scoring formula
```

The structural alignment scorer is the keystone: it is the first PFD component that
amplifies the ontology's *relational structure* rather than just its *topical proximity*.
Everything in Phase 3 builds on it.

---

*See also: `docs/FISHER_PIPELINE_REDESIGN.md` (canonical 6-step pipeline),
`docs/PFD_PROJECT_FOUNDATIONAL_PLAN.md` §4.2 (Phase 3 components),
`src/analysis/structural_alignment.py` (implementation)*
