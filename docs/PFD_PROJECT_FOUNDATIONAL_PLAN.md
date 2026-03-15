# Principia Formal Diagnostics (PFD) Project
## Foundational Plan & Scope Kickoff

**Document Version:** 1.2
**Date:** 2026-03-14
**Status:** Approved for implementation — updated to reflect Phase 2 completion + Fisher Suite + CCBH calibration
**Project:** Transition from DS_Wiki → Principia Formal Diagnostics (PFD)
**Changelog:**
- v1.0 (2026-03-11): Initial foundational plan
- v1.1 (2026-03-11): Stress Test 1 incorporated (see Section 13) — architectural changes: mandatory extraction gate, probabilistic logic, formality tiers, confidence compounding floor, hyperedge decision gate, 4 new risks added
- v1.2 (2026-03-14): §3 updated for Phase 2 completion (6 RRPs, 407 tests), Fisher Suite A–G, structural alignment, CCBH calibration (6/6 recall), P17 conjecture, SCF Phase 3 design. §4.1 marked complete. §10/§12 updated.

---

## Executive Summary

**Principia Formal Diagnostics** is a research validation and coherence verification system that enables automated logical consistency checking of scientific claims, papers, and reports against a formalized knowledge graph of logical foundations.

**Core Value Proposition:**
- Not a judge of truth, but a **diagnostic verifier** of reasoning coherence
- Transparent at every step — all outputs are explainable, auditable, contestable
- 100% open-source, distributed, community-governed
- Verifies reasoning against **formal logical foundations**, not just pattern matching
- Enables researchers to: validate claims, discover gaps, identify novel contributions, verify logical chains

**Project Status:** Foundation Phase (design + Phase 0-1.5 complete, Phase 2+ planned)

---

## 1. Project Identity & Values

### 1.1 Core Mission

To create a transparent, verifiable, distributed system for diagnosing logical coherence in scientific reasoning by:
1. Formalizing the implicit logical structures underlying scientific laws and principles
2. Mapping cross-domain connections through logical relationships (not just semantic similarity)
3. Enabling automated verification of scientific claims against formal foundations
4. Continuously evolving the knowledge graph as scientific consensus shifts
5. Maintaining radical transparency so experts can audit, challenge, and improve every component

### 1.2 Core Values

**Transparency Over Automation**
- Every output must show its reasoning
- No black-box judgments; all chains of inference visible
- Experts can trace, contest, override at any step

**Distributed Authority**
- No single gatekeeper of "truth"
- Open source with community governance
- Multiple maintainers, forkable instances
- Git-based version control of all knowledge

**Logical Rigor**
- Ground everything in formal systems (propositional logic, first-order logic, information theory)
- Distinguish between: axioms, derived rules, domain-specific instantiations
- Encode assumptions and domain boundaries explicitly

**Falsifiability**
- The system itself must be provably wrong when it is
- Failures should be understandable and fixable
- Confidence scores, not binary judgments

**Public Data Only (Currently)**
- All knowledge layers built from public, peer-reviewed sources
- No proprietary data in the knowledge graph
- Enables full community audit and reproducibility

### 1.3 Project Scope Boundaries

**In Scope:**
- Formalizing logical foundations (physics, math, CS, chemistry, biology, logic, rhetoric, epistemology)
- Building diagnostic tools for research verification
- Creating transparent analysis reports with explainable reasoning
- Open-source distribution and community governance

**Out of Scope (Phase 1):**
- Proprietary data sources
- Proprietary algorithms or closed models
- Real-time publishing platforms
- Training/certification systems
- Commercial service delivery

---

## 2. Core Architecture: Transparency & Diagnostics

### 2.1 System Design Philosophy

PFD operates as a **multi-layer verification system** where each layer is independently auditable:

```
INPUT (Scientific Claim / Paper)
  ↓
LAYER 1: Claim Extraction
  [NLP-based: what is being asserted?]
  ↓ TRANSPARENT: extracted claims shown, experts can correct
  ↓
  ⚠ MANDATORY HARD GATE ⚠
  Pipeline PAUSES here. Extracted claims presented to human reviewer.
  Human must CONFIRM, CORRECT, or REJECT each extracted claim before
  pipeline continues. This is not optional — LLM confabulation at
  Layer 1 propagates unchecked through all downstream layers if
  unverified. See Stress Test 1, Vulnerability 1.
  ↓ [Human confirmed → proceed] [Human corrected → re-extract] [Rejected → stop]
  ↓
LAYER 2: Foundation Matching
  [Semantic embedding: which DS Wiki principles are relevant?]
  [Respects formality_tier: hard science = strict, soft science = probabilistic]
  ↓ TRANSPARENT: all matches shown with similarity scores + domain applicability + formality tier
  ↓
LAYER 3: Formal Logic Validation
  [Does the claim follow valid inference rules?]
  [PROBABILISTIC: returns path probability, not boolean valid/invalid]
  ↓ TRANSPARENT: logical form shown, inference rules cited, confidence per step, tier-adjusted
  ↓
LAYER 4: Rhetorical Quality Check
  [Does the argument form avoid fallacies?]
  ↓ TRANSPARENT: argument pattern identified, fallacy risks flagged, strength scored
  ↓
LAYER 5: Evidence Sufficiency
  [Does the paper provide adequate evidence per domain standard?]
  ↓ TRANSPARENT: domain standard shown, evidence type assessed, gaps identified
  ↓
LAYER 6: Domain Boundary Validation
  [Is the claim applied within valid context?]
  ↓ TRANSPARENT: boundaries shown, violations flagged, valid domains listed
  ↓
OUTPUT: Diagnostic Report
  [Transparent reasoning trace + COMPOUNDED confidence score + expert override points]
  [If compounded confidence < 0.6: "Insufficient confidence — human review required"
   NOT a verdict. Pipeline does not emit plausible/contradicting at this threshold.]
```

**Critical architectural constraint (Stress Test 1):** The pipeline is sequential. Errors compound multiplicatively, not additively. A 6-layer pipeline at 90% per-layer accuracy yields ~53% end-to-end reliability if binary. The mandatory hard gate at Layer 1 and probabilistic outputs at all layers prevent binary error cascades. The confidence floor at 0.6 prevents low-quality verdicts from reaching users.

### 2.2 Explainability Design (Trust Framework)

**Never Hide:**
- Why a claim was matched to a specific DS Wiki entry
- What the logical chain is (step-by-step inference)
- Why confidence is 0.71 not 0.95 (specific gaps shown)
- Where DS Wiki is incomplete or uncertain
- What domain boundaries apply

**Always Show:**
- Similarity scores with percentile context
- Premises, inference rules, conclusions (not just verdict)
- Missing links in the logical chain
- Evidence gaps vs. evidence provided
- Alternative interpretations considered and why rejected

**Always Enable:**
- Expert override at any layer ("I disagree with your logic chain")
- Rationale annotation ("Here's why you're wrong")
- DS Wiki improvement suggestions ("This entry should be updated")
- Public audit trail (git history of changes and disagreements)

### 2.3 Knowledge Graph Structure

PFD maintains **formalized knowledge** across 6 interconnected layers:

**Layer 0: Formal Logic Axioms**
- Propositional logic: law of excluded middle, modus ponens, transitivity, etc.
- First-order logic: universal quantification, existential instantiation, etc.
- Modal logic: necessity, possibility, counterfactuals
- Information theory: entropy, mutual information, Kolmogorov complexity
- Database: logic_axioms, logic_inference_rules

**Layer 1: Rhetorical & Epistemological Foundations**
- Valid argument forms (deduction, induction, abduction, analogy)
- Known fallacies catalog (begging the question, ad hominem, false analogy, etc.)
- Evidence standards per domain (empirical, mathematical, computational, logical, social)
- Assumption transparency rules
- Database: argument_templates, fallacy_catalog, epistemological_standards

**Layer 2: Domain-Specific Principles**
- Physics laws (F=ma, conservation laws, thermodynamics, etc.)
- Chemistry principles (Periodic Law, stoichiometry, etc.)
- Biology laws (evolution, homeostasis, scaling laws, etc.)
- CS principles (Turing completeness, P vs NP, complexity classes, etc.)
- Math foundations (axioms, theorems, proof techniques)
- Database: entries (with entry_type, domain, logical_form, assumptions)

**⚠ Formality Tier (REQUIRED field — Stress Test 1, Vulnerability 3):**
Not all domains can be formalized to the same degree. Forcing a single boolean logic schema across physics AND biology causes the graph traversal engine to produce invalid results. Each DS Wiki entry MUST carry a `formality_tier`:

| Tier | Description | Domains | Validation Behavior |
|------|-------------|---------|---------------------|
| 1 | Hard axioms — deterministic, mathematically provable | Physics, Mathematics, CS Theory | Strict boolean logic chain, high confidence possible |
| 2 | Statistical tendencies with domain conditions — usually true, with exceptions | Chemistry, Molecular Biology, Materials Science | Probabilistic chain, confidence capped at 0.85 |
| 3 | Contextual heuristics — environmentally contingent, emergent | Ecology, Economics, Social Sciences, Systems Biology | Probabilistic only, confidence capped at 0.70, always flagged as "domain-dependent" |

The logic chain validator checks `formality_tier` before applying inference rules. Tier 3 entries never produce strict logical derivations — only probabilistic associations. This is not a limitation; it is accurate representation of epistemological reality.

**Layer 3: Relationships & Bridges**
- Logical connections: derives_from, predicts_for, assumes, contradicts_under
- Structural isomorphism: analogous_to, isomorphic_structure
- Domain bridges: appears_in, cross_domain_instantiation
- Database: entry_connections (with link_type, confidence_tier, logical_justification)

**Layer 4: Domain Boundaries & Assumptions**
- Explicit domain applicability (where this law applies/doesn't apply)
- Boundary conditions and edge cases
- Unstated assumptions
- Regimes of invalidity
- Database: domain_boundaries (per entry)

**Layer 5: Version History & Evolution**
- Git-tracked changes to knowledge graph
- Rationale for updates
- Conflicting interpretations (recorded, not hidden)
- Community feedback and override history
- Database: wiki_history.db with snapshots and change logs

---

## 3. Current Implementation Status

### 3.1 What Exists (Phases 0–2 Complete, Fisher Suite Complete)

**Repository:** `/Users/iandarling/Projects/DS_Wiki_Transformation`
**Public:** https://github.com/IanD25/ds-wiki-transformer
**Latest Commit:** c1c60a1 (2026-03-14)
**Test Suite:** 407 tests passing (`python3 -m pytest tests/ -v`)

#### Phase 0: Core Pipeline (COMPLETE)
**Status:** ✅ Fully functional, tested
**Components:**
- `src/config.py` — configuration management, auto-detects CUDA/MPS/CPU
- `src/extractor.py` — entry/section/link extraction from SQLite
- `src/embedder.py` — BGE embedding pipeline (BAAI/bge-large-en-v1.5, 1024-dim on MPS/CUDA; bge-base 768-dim CPU fallback)
- `src/topology.py` — network metrics (density, centrality, clustering)
- `src/sync.py` — sync extracted content to ChromaDB + wiki_history snapshots
- `src/mcp_server.py` — FastMCP server (9 tools exposed)

**Data (all committed to repo):**
- `data/ds_wiki.db` — source of truth (SQLite, read-only schema)
  - 209 entries, 573 links, 786 properties, 17 conjectures (P1–P17), 11 gates (G1–G11)
- `data/chroma_db/` — semantic index (1,486 chunks, bge-large 1024-dim, snapshot snap_20260314_123401)
- `data/wiki_history.db` — embedding history + topology metrics (append-only)

**Deliverable:** Semantic search capability, cross-wiki querying via MCP

#### Phase 1: Diagnostic Analysis Tools (COMPLETE)
**Status:** ✅ Tested (hypothesis, coverage, validator, gap tools)
**Components:**
- `src/analysis/hypothesis_generator.py` — pairwise similarity, surprise_factor, 20 typed prompts (31 tests)
- `src/analysis/coverage_analyzer.py` — entity/domain/property/archetype/network metrics (56 tests)
- `src/analysis/result_validator.py` — claim validation via ChromaDB matching (54 tests)
- `src/analysis/gap_analyzer.py` — structured gap detection, EnrichmentPriority ranking (75 tests)
- `src/analysis/link_classifier.py` — LLM-powered link classification with BGE filter

**MCP Tools:** `validate_claim`, `analyze_gaps`, `get_link_candidates`, `insert_triage_results`

**Deliverable:** Research gap identification, claim validation, consistency checking

#### Phase 1.5: Entity Catalog Specialized Pass (COMPLETE)
**Status:** ✅ Tested on Periodic Table RRP
**Components:**
- `src/ingestion/passes/entity_catalog_pass.py` — pattern extraction (5 types), synthetic entry generation, anomaly detection
- `src/ingestion/detector.py` — fingerprint-based dataset type classification (entity_catalog, law_catalog, metabolic_network)
- `scripts/run_entity_catalog_pass.py` — CLI orchestrator

**Deliverable:** Automatic pattern extraction from entity catalogs, improved bridge detection

#### Phase 2: RRP Ingestion Pipeline (COMPLETE)
**Status:** ✅ 6 parsers complete, 6 RRP bundles built, framework proven
**Components:**
- `src/ingestion/rrp_bundle.py` — RRP SQLite schema (mirrors DS Wiki + cross_universe_bridges)
- `src/ingestion/detector.py` — 7 format detectors (zoo_classes_json, cobra_json, flat_json, ro_crate, frictionless, codemeta, citation_cff)
- `src/ingestion/cross_universe_query.py` — Pass 2: RRP embeddings → DS Wiki ChromaDB → bridge candidates

**Parsers (6 complete):**

| Parser | Format | Entries | Links | Bridges | Notes |
|--------|--------|---------|-------|---------|-------|
| `zoo_classes_parser.py` | zoo_classes_json | 426 | 437 | 1,135 | Law catalog; 70 tier-1.5 bridges |
| `periodic_table_parser.py` | flat_json | 119 | 279 | 497 | Entity catalog; Pass 1.5 adds 48 synthetic entries |
| `ecoli_core_parser.py` | cobra_json | 304 | 536 | 912 | Metabolic network; stoichiometry reified as nodes |
| `opera_paper_parser.py` | paper_manual | — | — | — | Phase 3 prototype (single paper RRP) |
| `ccbh_cluster_parser.py` | paper_manual | 22 | 29 | 66 | First multi-paper cluster; 3 cosmology papers |
| `ieee_power_grid_parser.py` | — | — | — | — | IEEE power grid dataset |

**Hyperedge Decision (ADR):** Option A (reification) adopted for E. coli — reactions are nodes, edges to reactants/products. Documented in `ARCHITECTURE_DECISIONS.md`.

**Deliverable:** Complete, tested RRP ingestion pipeline for diverse formats (data, paper, multi-paper cluster)

#### Fisher Suite A–G: Full PFD Diagnostic Pipeline (COMPLETE)
**Status:** ✅ All 6 phases built and tested
**Canonical spec:** `docs/FISHER_PIPELINE_REDESIGN.md`

**Six-step PFD diagnostic pipeline:**
```
Step 1: Ingest RRP → rrp_*.db (entries + links)
Step 2: Build G_internal (within-RRP graph)
Step 3: Internal Diagnostics → Tier-1 Report (coherence, d_eff, regime distribution)
Step 4: Build G_bridge (Option B: rrp:: + wiki:: nodes + bridge edges)
Step 5: Bridge Diagnostics → Tier-2 Report (DS Wiki integration quality)
Step 6: Two-Tier Output → PFD Score (0.0–1.0)
```

**Components:**
- `src/analysis/fisher_diagnostics.py` — FIM math: `decompose_fim`, `build_fim`, `FIMResult`, `analyze_node`, `sweep_graph`, `build_wiki_graph`, `build_bridge_graph`
- `src/analysis/fisher_bridge_filter.py` — per-bridge quality scoring
- `src/analysis/fisher_report.py` — `PFDReport`, `generate_report` (two-tier HTML + console output)
- `src/analysis/structural_alignment.py` — link-type weighted signed polarity scoring (SCF replacement for broken SPT)
- `scripts/run_fisher_suite.py` — CLI: 6 modes (ds_wiki, node, bridges, internal_rrp, bridge, report)
- `scripts/run_structural_alignment.py` — CLI: structural alignment on any RRP with bridges

**MCP Tools:** `fisher_analyze_node`, `fisher_sweep_rrp`, `fisher_sweep_bridge`

**PFD Scores (validated bundles):**

| Bundle | PFD Score | Tier-1 Verdict | Tier-2 Verdict | Notable |
|--------|-----------|----------------|----------------|---------|
| E. coli Core | 0.973 | INTERNALLY CONSISTENT | WELL-INTEGRATED | Top hub: pyruvate (d_eff=11); CHEM5 anchor (134 bridges) |
| CCBH Cluster | 0.882 | MARGINAL (76.5%) | WELL-INTEGRATED (100%) | 6/6 Layer 1 recall; G1 top anchor (10 entries) |

**Deliverable:** Complete Fisher Information diagnostic pipeline with two-tier PFD scoring

#### Structural Alignment & SCF (COMPLETE)
**Status:** ✅ Built, tested on CCBH cluster
**Spec:** `docs/SCF_PHASE3_DESIGN.md`

**Key insight:** PFD implements Semantic Channel Finding (SCF). DS Wiki = core ontology. RRP entries = local channels. Cross-universe bridges = channel discovery. Structural alignment adds *signed polarity* — does the entry support or contest the formal principle?

**Polarity taxonomy:** would_have_violated (−1.0), contradicted (−1.0), explains_anomaly (−0.5), supersedes (+0.5), supports (+0.7), independently_validates (+0.8), is_consistent_with (+1.0)

**CCBH calibration test (2026-03-14):**
- Mean polarity: +0.925, 0 contested, 4 aligned entries
- Pipeline independently recovered all 6 manually identified conjecture targets (P3→OmD, P5/P6→X0, P8→H5, P4/P15→B5+conj_P15, T4→G1, T3→B3)
- **Recall: 6/6 (100%)** against human Layer 1 gate — validates Phase 3 methodology

**Deliverable:** Signed polarity bridge scoring, proven pipeline-vs-human calibration

#### Visualization & Reporting Module (COMPLETE)
**Status:** ✅ Tier-1 + Tier-2 interactive visualizations
**Components:**
- `src/viz/viz_runner.py` — orchestrator
- Tier-1: D3.js network graph, coherence/regime charts, HTML report per dataset
- Tier-2: Bridge histogram, bipartite network, domain heatmap, HTML report
- Fisher Suite HTML reports: `data/reports/`

**Output:** `data/viz/` and `data/viz_outputs/` with .png + .html

**Known issues:**
- D3.js degenerate node toggle: can toggle off but not back on
- Node sizes could be 30% larger for readability

**Deliverable:** Interactive analysis reports, publishable visualizations

#### P17 Conjecture: Cosmological Coupling (2026-03-14)
**Status:** ✅ Inserted into ds_wiki.db + ChromaDB indexed

**P17: Cosmological Coupling Exponent Equals D_eff**
- Claim: D_eff = k = −3w_phys. Vacuum energy (w = −1) → k = 3 = d_spatial.
- Depends on: P5, G1, GV4, OmD
- Gate: G11 (Critical) — requires independent k measurement + formal Fisher derivation on Cadoni matched metric
- Evidence: Farrah 2023 k = 3.11 ± 1.19; DESI 2025 k = 3 improves fits
- Status: State 2 / Phase 1 partial (CCBH cluster 6/6 recall)

### 3.2 Version Control & Git History

**Repository:** https://github.com/IanD25/ds-wiki-transformer (public)

**Key Commits (recent):**
```
c1c60a1 (HEAD, 2026-03-14) — feat: Add conjecture P17 (cosmological coupling k = D_eff) and gate G11
dfcc482 (2026-03-14) — docs: Update CLAUDE.md, README.md, setup.sh for committed artifacts
cf2cc3b (2026-03-14) — feat: Track all generated artifacts — chroma_db, reports, viz, wiki_history
f014c21 (2026-03-14) — feat: Add CCBH paper cluster — 3-paper RRP + Layer 1 conjecture analysis
86c2d64 (2026-03-13) — feat: Add SCF Phase 3 design — structural alignment scorer + roadmap
9bec3c8 (2026-03-13) — feat: Add OPERA paper parser — first Phase 3 paper-based RRP
```

**Branch Strategy:**
- `main` — production, always working
- Feature branches deleted after merge (clean history)
- All commits squashed + semantically named

**Asset Versioning (all committed):**
- `data/ds_wiki.db` — committed (single source of truth, read-only schema)
- `data/chroma_db/` — committed (rebuilt on `sync.py` run, bge-large 1024-dim)
- `data/wiki_history.db` — committed (growing append-only)
- `data/reports/` — committed (Fisher Suite HTML reports + structural alignment JSON)
- `data/viz/`, `data/viz_outputs/` — committed (visualization outputs)

---

## 4. Planned Implementation Roadmap

### 4.1 Phase 2 Completion — COMPLETE (2026-03-14)

**Goal:** ✅ Complete RRP ingestion framework, tested on all formats

**Completed:**
- Hyperedge decision: Option A (reification) adopted, documented in `ARCHITECTURE_DECISIONS.md`
- E. coli Core parser: 304 entries, 536 links, 912 bridges (PFD Score 0.973)
- OPERA paper parser: first paper-based RRP (Phase 3 prototype)
- CCBH cluster parser: first multi-paper cluster (3 cosmology papers, 22 entries, 66 bridges)
- IEEE power grid parser
- 6 total parsers, 6 RRP bundles, all with cross-universe bridges

**Outstanding (deferred, non-blocking):**
- Documentation: INGESTION_GUIDE.md, SCHEMA_REFERENCE.md (deferred to Phase 5 community readiness)

**Success Criteria — All Met:**
- ✅ All parsers producing valid bundles with >0 internal links
- ✅ E. coli bundle reflects actual metabolic pathways (pyruvate top hub, d_eff=11)
- ✅ Framework proven on 4 format types: entity catalog, law catalog, metabolic network, paper-based
- ✅ Multi-paper cluster pipeline validated (CCBH 6/6 recall)

---

### 4.2 Phase 3: Paper Analysis Suite (Weeks 3-6)

**Goal:** Build claim extraction, validation, and reasoning verification for scientific prose

**⚠ Vertical Integration Constraint (Stress Test 1, Vulnerability 6 + Recommendation 1):**
Phase 3 MUST begin with a single well-covered domain before expanding. Do not attempt cross-domain paper analysis until DS Wiki has sufficient coverage of the target domain.

**Approved starting verticals (in priority order):**
1. Classical thermodynamics (TD cluster — well-represented in DS Wiki, deterministic laws, Tier 1)
2. Computational complexity theory (ZooClasses RRP already ingested — proven bridge quality)
3. Expand to chemistry/biology only after thermodynamics vertical is validated end-to-end

Rationale: The cold-start problem (Stress Test 1, Vulnerability 6) means PFD must demonstrate value in a narrow domain before the knowledge graph is sufficiently broad. Attempting universal analysis immediately will produce low-confidence outputs that undermine user trust before the system can prove itself.

**Components to Build:**

**3.1 Claim Extraction Module** (`src/analysis/claim_extractor.py`)
- LLM-based structured claim parsing
- Input: paper text (abstract, methods, findings sections)
- Output: `Claim(subject, relationship, object, confidence, domain, source_section)`
- Methods:
  - Prompt engineering (5-shot examples per domain)
  - Coreference resolution (what does "it" refer to?)
  - Scope detection (is this a claim or a background statement?)
- **MANDATORY HARD GATE:** Extracted claims are presented to user for confirmation before downstream processing. Pipeline does not continue without explicit human sign-off. This is a hard architectural requirement, not a UX preference. (Stress Test 1, Vulnerability 1)
- Test: 50+ examples from real papers (physics, CS, biology)

**3.2 Claim Validator Enhancement** (`src/analysis/claim_validator.py` — extends Phase 1)
- BGE embedding of extracted claims
- ChromaDB query against DS Wiki
- Return: top-K matches with similarity + domain applicability + confidence
- Enhanced output includes: potential contradictions, related principles, supporting principles
- Test: Claim should match >1 DS Wiki entry >0.7 sim (baseline)

**3.3 Logic Chain Validator** (`src/analysis/logic_chain_validator.py`)
- Graph traversal on DS Wiki entry_connections
- Check: Does link path exist from premise to conclusion?
- Validate: Direction correct? (cause→effect or bidirectional?)
- Flag: Missing intermediate steps, broken assumptions, circular reasoning
- Methods:
  - DFS/BFS on knowledge graph (entry → related entries → ... → target)
  - Link type validation (does "assumes" link apply here?)
  - Depth analysis (depth-1 = direct support, depth-2+ = requires intermediates)
- Test: Known valid chains from DS Wiki should validate, invalid chains should fail

**3.4 Argument Quality Checker** (`src/analysis/argument_quality_checker.py`)
- Pattern detection: identify argument form (deduction, induction, analogy, appeal to authority, etc.)
- Fallacy detection: known patterns (begging the question, ad hominem, false cause, strawman, etc.)
- Strength scoring: valid forms highest, risky forms flagged, known fallacies = red flag
- Methods:
  - Rule-based pattern matching (induction = "all X observed have property Y" + "therefore all X have property Y")
  - LLM-based fallacy detection (more subtle fallacies)
- Database: argument_templates, fallacy_catalog (to be built in Phase 4)
- Test: Train on 50 good/bad arguments, validate F1 score >0.85

**3.5 Evidence Sufficiency Auditor** (`src/analysis/evidence_auditor.py`)
- Domain-based evidence standard lookup
- Evidence type detection (empirical, mathematical, computational, logical, testimonial)
- Gap analysis: what evidence is claimed vs. what standard requires
- Methods:
  - Query epistemological_standards table (built in Phase 4)
  - Parse paper's evidence section
  - Compare evidence type + quantity to standard
- Test: Reproduce known peer review verdicts ("this claim needs empirical evidence but paper only has theory")

**3.6 Domain Boundary Checker** (`src/analysis/domain_boundary_checker.py`)
- Extract domain context from claim
- Cross-check against DS Wiki entry domain_boundaries
- Flag: boundary violations, invalid regime applications
- Methods:
  - Claim mentions "dilute solution" → check if law applies to dilute regime
  - Claim applies to "high-energy physics" → check if law restricted to low-energy
- Test: Common boundary violations (applying ideal gas law to compressed gas) should be caught

**3.7 Review Report Generator** (`src/analysis/review_report_generator.py`)
- Markdown report with full reasoning trace
- Structure:
  ```
  CLAIM ANALYSIS REPORT
  =====================

  1. CLAIM EXTRACTION
     [Extracted claims with confidence]

  2. FOUNDATION MATCHING
     [Top-K DS Wiki entries with sim + applicability]

  3. LOGICAL CHAIN VALIDATION
     [Premises → inference rules → conclusion]
     [Confidence per step, overall chain confidence]

  4. ARGUMENT QUALITY
     [Argument form identified, fallacy risks, strength score]

  5. EVIDENCE SUFFICIENCY
     [Domain standard shown, evidence assessed, gaps]

  6. DOMAIN BOUNDARIES
     [Applicability checked, violations flagged]

  7. EXPERT CHECKPOINTS
     [Where experts can override/annotate]

  8. OVERALL VERDICT
     [Plausible/contradicting/novel, confidence, next steps]
  ```
- Interactive: links to DS Wiki entries, explanation of every flag

**3.8 MCP Tools for Paper Analysis**
- `analyze_paper(paper_text: str) → review_report`
- `extract_claims(text: str) → [claims]`
- `validate_claim_chain(claim_set: List[str]) → consistency_report`
- `compare_papers(paper1_text, paper2_text) → concordance_analysis`

**Success Criteria:**
- 20 test papers from different domains analyzed with human expert agreement >0.80
- All 7 layers operating independently (can disable/override any layer)
- Report generation <10s for typical paper (abstract + findings)

---

### 4.2a Phase 3 — SCF Grounding (added 2026-03-13)

**Context:** The structural alignment scorer (`structural_alignment.py`, built 2026-03-13)
demonstrated that PFD is implementing a form of **Semantic Channel Finding (SCF)** —
the methodology used in multi-facility scientific infrastructure to map local naming
conventions to a shared ontology backbone. Full design: `docs/SCF_PHASE3_DESIGN.md`.

**The key insight:** DS Wiki = core ontology. RRP entries = local channels. Cross-universe
bridges = channel address discovery. Structural alignment polarity = signed channel quality
(does the entry *support* or *contest* the formal principle it maps to?). This is
qualitatively more powerful than unsigned semantic similarity alone.

**SCF-grounded Phase 3 options (see SCF_PHASE3_DESIGN.md for full spec):**

| Option | Description | Dependency | Priority |
|--------|-------------|------------|----------|
| **3A** | Dynamic Channel Resolution — `claim_extractor.py` + enhanced `result_validator.py`. Free-text claims resolved to DS Wiki channels in real-time with provisional polarity hints. Mandatory human gate. | §3.1 above | **High — Phase 3 core** |
| **3B** | Structural Alignment in Tier-2 Report — SA section added to `fisher_report.py` + signed bridge visualization in `tier2_report.py`. Unsigned PFD Score partially replaced with polarity-weighted score. | 3A + structural_alignment.py | **High — improves all existing RRPs** |
| **3C** | Multi-RRP Ontology Queries — `cross_rrp_query.py` enables cross-facility SCF: "which entries across all RRPs contest QM5?" DS Wiki reputation scores (stored in wiki_history.db). | 3B + ≥3 paper-based RRPs | **Medium — full SCF vision** |
| **3D** | Link-Type Weighted PFD Score — full formula revision using SA polarity + consensus factor. Replaces bridge-count Tier-2 metric. | 3C + calibration study | **Low — Phase 4 prep** |

**Vertical integration constraint (unchanged):** Options 3A and 3B restricted to
thermodynamics + Special Relativity verticals until >80% of DS Wiki entries have
`formality_tier` set. OPERA paper (Special Relativity) is the approved initial test case.

**What SCF does NOT replace (still required):**
- Formal logic validation (Phase 4) — logical entailment, not just semantic channel proximity
- Evidence sufficiency (§3.5 above) — how strongly a claim is supported
- Domain boundary validation (§3.6 above) — applicability of laws outside their validity regimes

**Recommended Phase 3 sequence:** 3A → 3B → §3.3–3.7 (logic + evidence layers) → 3C → 3D

**Deliverable:** End-to-end paper analysis suite with transparent reasoning traces

---

### 4.3 Phase 4: Logic Foundation Layers (Weeks 7-10)

**Goal:** Encode formal logical foundations, rhetorical logic, epistemological standards

**Components to Build:**

**4.0 Schema Migration: formality_tier (PREREQUISITE — Stress Test 1, Vulnerability 3)**
- Before Phase 4 logic work begins, ALL existing DS Wiki entries must receive a `formality_tier` value (1, 2, or 3)
- Add column: `ALTER TABLE entries ADD COLUMN formality_tier INTEGER DEFAULT 2`
- Assign tiers in batch: physics/math/CS theory → 1, chemistry/molecular biology → 2, ecology/economics → 3
- Domain experts validate tier assignments before Phase 4 logic encoding begins
- This is a data migration task, not a code task — but it gates all Phase 4 work

**4.1 Formal Logic Axiom Layer** (`data/logic_foundations/`)
- Propositional logic axioms (law of excluded middle, law of non-contradiction, etc.)
- First-order logic rules (universal quantification, existential instantiation, etc.)
- Inference rules (modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, etc.)
- Modal logic (necessity, possibility, counterfactuals)
- Database tables: logic_axioms, logic_inference_rules, logical_forms (for each DS Wiki entry)
- Note: Formal axioms apply ONLY to Tier 1 entries. Tier 2/3 entries receive probabilistic association rules, not deterministic axioms.

**4.2 Argument Templates & Fallacy Catalog** (`data/rhetorical_foundations/`)
- Valid argument forms with examples
- Known fallacies with patterns and explanations
- Database: argument_templates, fallacy_catalog
- Structure: each with detection rules (pattern matching or LLM)

**4.3 Epistemological Standards Layer** (`data/epistemological_standards/`)
- Evidence standards per domain
  - Physics: empirical + mathematical + computational
  - CS: computational + mathematical + logical proof
  - Biology: empirical + statistical + mathematical
  - etc.
- Confidence levels required per claim type
- Database: epistemological_standards, evidence_type_definitions

**4.4 Domain Boundaries Formalization** (`data/domain_boundaries/`)
- For each DS Wiki entry: explicit boundary conditions
  - Valid regimes (temperature, pressure, concentration, scale, etc.)
  - Invalid regimes
  - Edge cases
- Database: domain_boundaries (per entry)

**4.5 Cross-Domain Bridge Analysis** (`src/analysis/cross_domain_analyzer.py`)
- Detect isomorphic structures across domains
  - Physics phase transitions ↔ CS computational phase transitions
  - Information theory entropy ↔ Thermodynamic entropy
  - Conservation laws in physics ↔ Conservation in information theory
- Methods: graph alignment algorithms (GraphMatcher, VF2)
- Output: bridge_candidates with structure similarity scores

**Success Criteria:**
- All DS Wiki entries have logical_form annotation
- >50 argument templates + fallacies documented
- >10 cross-domain bridges identified with confidence >0.8
- Formal logic layer enables validation of reasoning chains from first principles

**Deliverable:** Complete logical foundation layers, formalized knowledge graph

---

### 4.4 Phase 5: Distributed Governance & Community Tools (Weeks 11+)

**Goal:** Enable community-driven improvement and versioning

**Components to Build:**

**5.1 Knowledge Graph Versioning** (`src/governance/`)
- Git-based versioning of all knowledge layers
- Each DS Wiki entry update = commit with rationale
- Branching: main (consensus) + proposed_changes (community PRs)
- Diff visualization: show what changed, why

**5.2 Community Contribution Framework**
- GitHub Issues: propose new entries, flag errors, suggest links
- GitHub Discussions: debate conflicting interpretations
- PR workflow: contributor proposes DS Wiki change, experts review, merge or comment

**5.3 Audit Trail & Transparency Report** (`src/governance/audit_tools.py`)
- Generate: "Here's how entry X evolved"
- Show: all changes, who made them, rationale, expert feedback
- Enable: anyone to fork a version they disagree with

**5.4 Multiple Instance Deployment**
- Docker image: full PFD stack (DS Wiki + PFD tools + MCP server)
- Deployment guide: how to run your own instance
- Federation protocol: how multiple instances can share knowledge updates

**Success Criteria:**
- Public GitHub issues open to community
- >3 external contributors
- >2 successful knowledge conflicts resolved via documentation

**Deliverable:** Community-governed, distributed knowledge graph

---

## 5. Technical Methods & Designs

### 5.1 Embedding & Similarity Matching

**Model:** BAAI/bge-large-en-v1.5 (1024-dim on MPS/CUDA; bge-base 768-dim CPU fallback)
- Auto-detected at import time via `src/config.py` — no manual configuration needed
- Apple M4 (MPS) and ShadowPC RTX 2000 (CUDA) both run bge-large
- Trained on scientific abstracts (relevant to our domain)
- Open-source, reproducible

**Chunking Strategy:**
- One chunk per section (natural unit)
- Conjectures, gates, bridge_content = one chunk each
- Format: `{entry_id}_{section_name_normalized}`

**Similarity Matching:**
- Cosine similarity on L2-normalized embeddings
- Threshold tiers: >0.85 (tier-1.5), >0.75 (tier-2), >0.65 (weak)
- Contextualization: compare within domain when possible

**Confidence Scoring (updated v1.1 — Stress Test 1, Vulnerability 2):**
- Not binary (valid/invalid) but graded (0-1)
- Cross-layer compounding: errors multiply, not add. This is a feature, not a flaw — it forces honest uncertainty
- Base formula per layer: `layer_confidence = base_sim × domain_match × chain_depth_discount × evidence_multiplier`
- Cross-layer formula: `final_confidence = Π(layer_i_confidence for i in 1..6)`
- Formality tier caps: Tier 1 max 0.95 | Tier 2 max 0.85 | Tier 3 max 0.70
- **Confidence floor:** If `final_confidence < 0.60`, output is NOT a verdict. Output is: `"Insufficient confidence (score: X) — human expert review required. Specific gaps: [list]"`. Never emit plausible/contradicting/novel below this floor.
- Rationale: A 0.55 confidence claim flagged as "probably contradicts" IS alert fatigue. A 0.55 claim flagged as "too uncertain to judge, here's why" IS useful diagnostic information.

### 5.2 Logic Chain Validation (updated v1.1 — Stress Test 1, Vulnerability 2 & 3)

**Graph Representation:**
- Nodes: DS Wiki entries (each tagged with formality_tier)
- Edges: entry_connections with link_type + confidence_tier
- Edge weights: confidence + domain applicability + formality_tier of source node

**Path Finding — PROBABILISTIC (not boolean):**
- DFS to find paths from claim premises to conclusion
- Depth limit: 3 hops (longer chains less confident — confidence decays by 0.15 per additional hop)
- Direction validation: link type must support premise→conclusion direction
- **Never return boolean VALID/INVALID.** Always return `path_probability` (0-1) with path shown.
- Rationale: Scientific knowledge chains are probabilistic by nature. A boolean engine that fails when a premise is missing is a fragile tool. A probabilistic engine that says "this chain is 0.72 probable given these foundations" is a useful diagnostic.

**Tier-Adjusted Traversal:**
- Tier 1 nodes: boolean inference rules apply (modus ponens, transitivity)
- Tier 2 nodes: probabilistic inference (edge weight × statistical confidence)
- Tier 3 nodes: association only (no logical derivation, only co-occurrence patterns)
- Mixed-tier chains: final tier = minimum tier of all nodes in path (weakest link determines chain strength)

**Unarticulated Assumption Handling (Stress Test 1, Vulnerability 5):**
- DS Wiki domain_boundaries encode "standard background knowledge" per domain
- Type A omissions (standard background for domain): NOT flagged (e.g., conservation of energy in a thermodynamics paper)
- Type B omissions (non-standard intermediate steps): flagged as "implicit assumption: [entry X]"
- Type C gaps (no DS Wiki entry exists for a required step): flagged as "DS Wiki gap — requires expert review"
- PFD explicitly acknowledges it cannot catch all implicit assumptions — this limitation is stated in every report

**Missing Link Detection:**
- If no path exists: "No DS Wiki support found" (not "INVALID" — DS Wiki may be incomplete)
- If weak path (prob < 0.6): "Requires intermediates — see Type B assumptions above"
- If contradicting path: "Found opposing chain — review: [entry chain]"
- Suggest: "Claim would be stronger if it cited [entry X]"

### 5.3 LLM Integration Points

**Claim Extraction:** Claude + structured output (5-shot prompting)
**Fallacy Detection:** Claude on suspicious argument patterns
**Report Generation:** Claude for prose narrative (structured template filling)
**Alternative Interpretation Consideration:** Claude to brainstorm alternative readings of claim

**Rationale:** Use LLM for linguistic/creative tasks, not for truth judgment. Formal logic for reasoning validation.

### 5.4 Testing & Validation

**Unit Tests:**
- Each layer has unit tests (claim extraction, validator, checker, etc.)
- Synthetic data + real examples
- Target: >85% code coverage

**Integration Tests:**
- End-to-end: paper text → extracted claims → validation → report
- Test papers from different domains
- Human expert evaluation of reports

**Calibration:**
- Collect baseline: known good papers (high citations, peer-reviewed) should score high
- Collect baseline: known problematic papers (retracted, controversial) should flag issues
- Adjust confidence formulas until calibration achieved

**Public Benchmarking:**
- Publish benchmark dataset (anonymized papers + ground truth verdicts)
- Publish results: precision/recall/F1 per layer
- Enable external validation

---

## 6. Organization & Governance

### 6.1 Decision Authority

**Design Decisions** (what goes into PFD):
- Authority: core team + scientific advisory board
- Process: GitHub Issues/Discussions, documented decision docs
- Appeal: fork the project if you disagree

**Knowledge Graph Updates** (what goes into DS Wiki):
- Authority: domain experts + community
- Process: GitHub PR with peer review
- Standards: cite sources, justify links, explain domain boundaries

**Tool Development:**
- Authority: core team
- Process: feature branches, documented design docs
- Community: external contributors welcome via PR

### 6.2 Roles

**Core Maintainer** (1 person initially: @IanD25)
- Final authority on design/architecture decisions
- Merge decisions on PRs
- Release management

**Domain Experts** (recruited phase-by-phase)
- Physics expert: validate physics laws + boundaries
- CS expert: validate CS principles + complexity theory
- Biology expert: validate biological principles
- etc.
- Responsibility: review domain contributions, maintain quality

**Community Contributors**
- Open to: anyone with expertise
- Contribution: parser implementations, new entry suggestions, bug reports

### 6.3 Conflict Resolution

**If experts disagree on a knowledge claim:**
1. Document both interpretations in DS Wiki entry (sections: "Interpretation A" vs "Interpretation B")
2. Record: which experts support each, what evidence supports each
3. Track: are interpretations converging or diverging over time?
4. Never delete: let disagreements live publicly until consensus emerges

**If contributors disagree on design:**
1. Make decision transparently in GitHub issue
2. Record: rationale for chosen direction
3. Document: alternative not chosen and why
4. Enable: fork/alternative implementation if disagreement fundamental

---

## 7. Version Control & Release Strategy

### 7.1 Git Conventions

**Commit Messages:**
- Format: `[PHASE/TYPE] Brief title\n\nDetailed explanation`
- Examples:
  - `[Phase 3] Add claim extraction module — LLM-based parser for scientific prose`
  - `[Phase 2] Fix entity embedding bug — add "What It Captures" to EMBED_SECTIONS`
  - `[Data] Update Periodic Law domain boundaries`

**Branching:**
- `main` — always working, always deployable
- `feature/parser-ecoli` — feature branches for major work
- `data/update-physics-laws` — data update branches
- Merge via PR with peer review

**Semantic Versioning:**
- PFD vX.Y.Z
- X: major phase (0=foundation, 1=diagnostics, 2=RRP, 3=paper analysis, 4=logic foundations)
- Y: feature additions
- Z: bug fixes, data updates

**Releases:**
- Tag: `pfd-v1.0`, `pfd-v1.5`, `pfd-v2.0` on main
- Changelog: what's new, breaking changes, known issues

### 7.2 Data Versioning

**DS Wiki DB:**
- Committed to git (immutable, source of truth)
- Snapshot captures: `snap_YYYYMMDD_HHMMSS` in wiki_history.db
- Never deleted, never altered in-place

**ChromaDB:**
- NOT committed (rebuilt from DS Wiki on each sync)
- Build reproducible: same BGE model, same embedding params
- Document: rebuild instructions in README

**RRP Bundles:**
- Committed (artifacts of successful ingestion)
- Naming: `rrp_{dataset_name}.db`
- Dated: embed run timestamp

**Analysis Outputs:**
- NOT committed (transient)
- Gitignored: `/data/viz/`, `/data/analysis_reports/`
- Regenerable: rerun scripts to reproduce

---

## 8. Risk Analysis & Mitigation

### 8.1 Risks

**Risk 1: DS Wiki Becomes Authoritative / Dogmatic**
- Symptom: "PFD said my claim is invalid, so it must be wrong"
- Mitigation:
  - Always show reasoning (never hide why)
  - Enable override/disagreement (expert can say "I disagree")
  - Public audit trail (anyone can see DS Wiki history)
  - Explicit uncertainty (confidence scores, not binary)
  - Governance: community-driven, not top-down

**Risk 2: Knowledge Graph Becomes Stale / Incorrect**
- Symptom: PFD validates against outdated DS Wiki, misses paradigm shifts
- Mitigation:
  - Continuous git versioning (easy to track changes)
  - Community contribution (anyone can propose updates)
  - Benchmark testing (calibrate against known good/bad papers regularly)
  - Fork capability (if community disagrees, they can maintain own version)

**Risk 3: Claim Extraction (LLM) is Wrong**
- Symptom: LLM misinterprets paper intent, validation is invalid
- Mitigation:
  - Show extracted claims to user (reviewer can correct)
  - Never auto-correct, always flag if unsure
  - Unit test on 100+ real examples before deployment
  - Human-in-the-loop (expert can override extraction)

**Risk 4: Overconfidence in Automated Validation**
- Symptom: Researchers trust PFD output too much, skip peer review
- Mitigation:
  - Explicit messaging: "This is a diagnostic tool, not a judge"
  - Confidence bounds (never >0.95)
  - Flag uncertainty (missing data, weak links)
  - Marketing: position as peer review aid, not replacement

**Risk 5: Scaling & Maintenance**
- Symptom: DS Wiki grows to 10k+ entries, maintenance burden exceeds capacity
- Mitigation:
  - Decentralization (domain experts each maintain their domain)
  - Automation (CI/CD checks for entry completeness)
  - Community contributions (distribute load)
  - Modular structure (can extend without rewriting core)

**Risk 6: Pipeline Error Compounding (Stress Test 1, Vulnerability 2)**
- Symptom: Sequential 6-layer pipeline compounds errors multiplicatively; low-quality verdicts erode user trust
- Root cause: If layer accuracies are 0.90 each, end-to-end = 0.90^6 ≈ 0.53 in a binary system
- Mitigation:
  - Probabilistic outputs at every layer (no boolean VALID/INVALID)
  - Cross-layer confidence compounding formula (Section 5.1) — uncertainty is honest, not hidden
  - Confidence floor: outputs below 0.60 are never verdicts, always "insufficient confidence"
  - Mandatory human gate at Layer 1 breaks the cascade before it starts
  - Benchmark calibration ensures per-layer accuracy targets are met before deployment

**Risk 7: Ontological Overreach — Soft Science Formalization Failure (Stress Test 1, Vulnerability 3)**
- Symptom: System attempts to apply strict logical axioms to biology/economics; produces invalid conclusions; expert community rejects the tool
- Root cause: Deterministic axioms cannot represent emergent, statistical, context-dependent phenomena
- Mitigation:
  - formality_tier system (Tier 1/2/3) enforces appropriate inference rules per domain
  - Tier 3 entries (ecology, economics, social sciences) never trigger strict logical derivations
  - Explicit acknowledgment in every Tier 3 report: "This domain relies on probabilistic tendencies, not deterministic laws"
  - Domain experts validate tier assignments before deployment

**Risk 8: Hypergraph Topology Distortion (Stress Test 1, Vulnerability 4)**
- Symptom: N-to-N scientific relationships (stoichiometry, multi-factor causation, gene regulatory networks) forced into binary edges; logical validation produces invalid conclusions
- Root cause: Relational schemas and standard graph databases are optimized for binary relationships
- Mitigation:
  - Explicit hyperedge architecture decision required before metabolic/network dataset parsing (Section 4.1, Task 0)
  - Phase 2: Reification approach (pragmatic, documented as known limitation)
  - Phase 4: Native hyperedge schema upgrade evaluated
  - All reports from metabolic/network datasets carry: "Stoichiometric/network relationships approximate — binary graph representation used"

**Risk 9: Cold Start — Insufficient Coverage Undermines Early Trust (Stress Test 1, Vulnerability 6)**
- Symptom: PFD produces low-confidence outputs across all domains early on; users dismiss the tool before coverage improves; community never reaches critical mass
- Root cause: System needs critical mass to demonstrate value; needs demonstrated value to attract community
- Mitigation:
  - Strict vertical integration discipline (Phase 3 restricted to thermodynamics + CS complexity initially)
  - ZooClasses + Periodic Table RRP results serve as demonstration proof before Phase 3
  - Success in narrow domains publicly documented and shared to attract domain expert contributors
  - DS Wiki coverage dashboard published publicly (shows community which domains need work)
  - No cross-domain claims until coverage threshold met (>80% of entries in domain have formality_tier + domain_boundaries)

### 8.2 Mitigation Strategies (Cross-Cutting)

1. **Transparency as Risk Control**
   - All outputs explainable → easy to spot errors
   - All decisions documented → easy to correct course
   - All data in git → easy to revert bad changes

2. **Continuous Testing & Calibration**
   - Regular benchmark runs (known papers)
   - Precision/recall tracking over time
   - Public reporting of metrics

3. **Community Governance**
   - Distributed authority (no single gatekeeper)
   - Open PR/issue process
   - Documented decision rationale

---

## 9. Success Criteria & Metrics

### Phase-Specific

**Phase 2 Success:** ✅ ALL MET (2026-03-14)
- ✅ E. coli parser producing biochemically plausible link graph (PFD 0.973, pyruvate top hub)
- ✅ All 6 parsers (zoo, periodic, ecoli, opera, ccbh, ieee) working end-to-end
- ✅ Multi-paper cluster pipeline proven (CCBH: 6/6 recall vs human Layer 1)
- ⚠ Documentation (INGESTION_GUIDE.md) deferred to Phase 5 — framework is proven by 6 working parsers

**Phase 3 Success:**
- ✅ Claim extraction: accuracy >85% on test papers
- ✅ Logic chain validation: matches expert opinion >80% of time
- ✅ Report generation: <10s per paper, readable to domain expert
- ✅ Human evaluation: 10 experts review 5 papers each, average satisfaction >4/5

**Phase 4 Success:**
- ✅ >100 DS Wiki entries have formal_logic annotations
- ✅ >50 cross-domain bridges identified & documented
- ✅ All reasoning chains in Phase 3 reports traceable to formal logic axioms

**Phase 5 Success:**
- ✅ >3 external contributors with merged PRs
- ✅ >2 conflicting interpretations documented & tracked
- ✅ Community fork successfully maintained by others

### Ongoing Metrics

**Coverage:**
- % of DS Wiki entries with domain_boundaries
- % of entries with formal_logic annotation
- # of cross-domain bridges per domain pair

**Quality:**
- Benchmark F1 score (on known good/bad papers)
- Precision/recall of claim extraction
- Calibration of confidence scores

**Community:**
- # of GitHub issues opened per month
- # of external contributors
- # of community forks
- # of alternative implementations

---

## 10. Timeline (Indicative, Non-Binding)

```
WEEK 1-2:   ✅ Phase 2 completion — DONE (6 parsers, 6 RRPs, Fisher Suite, 407 tests)
WEEK 3-4:   Phase 3A — Dynamic Channel Resolution (claim_extractor.py + result_validator enhancement)
WEEK 4-5:   Phase 3B — Structural alignment in Tier-2 report + polarity-weighted PFD score
WEEK 5-6:   Phase 3 remaining layers (logic chain, evidence sufficiency, domain boundary)
WEEK 7-10:  Phase 4 (Logic foundation layers, formality_tier assignment)
WEEK 11+:   Phase 5 (Community governance, federation)
```

**Notes:**
- Timelines are estimates; actual progress depends on resource availability
- Phase 3 SCF-grounded design validated by CCBH calibration (6/6 recall)
- Quality over speed: comprehensive tests required before merging
- Community contributions may accelerate or redirect timeline

---

## 11. Implementation Notes & Constraints

### 11.1 Technology Stack

**Language:** Python 3.13+
**Core Libraries:**
- sqlite3 (standard library, data storage)
- sentence-transformers (BGE embeddings)
- chromadb (semantic search)
- fastmcp (MCP server)
- pytest (testing)
- numpy (numeric operations)

**No:** TensorFlow, PyTorch, scipy (keep dependency footprint light)

**Deployment:**
- Docker (optional, for reproducibility)
- GitHub (version control + community platform)
- Public cloud (optional, user-hosted instances)

### 11.2 Data & Privacy

**All public data only:**
- DS Wiki: peer-reviewed scientific literature
- RRP bundles: public datasets
- Test papers: published or consent-obtained
- No proprietary/confidential sources

**User data privacy:**
- Paper analysis done locally (on user's machine or private cloud)
- No analytics/logging of papers analyzed
- No model training on user data
- MCP server: local only, no remote connection

### 11.3 Open Source License

**License:** MIT (permissive, enables forks + commercial use)
**Reasoning:** Enable maximum community use & variation

---

## 12. Next Immediate Actions (Week of 2026-03-14)

**Completed since v1.1:**
1. ✅ Hyperedge decision: Option A (reification) adopted, documented in `ARCHITECTURE_DECISIONS.md`
2. ✅ Phase 2 complete: 6 parsers (zoo, periodic, ecoli, opera, ccbh, ieee), 407 tests
3. ✅ Fisher Suite A–G: Full 6-step PFD pipeline, two-tier reports, 3 MCP tools
4. ✅ Structural alignment: Link-type weighted signed polarity scoring (replaced broken SPT)
5. ✅ SCF Phase 3 design: `docs/SCF_PHASE3_DESIGN.md` (Options 3A–3D)
6. ✅ CCBH cluster calibration: 6/6 recall against human Layer 1 gate
7. ✅ P17 conjecture (d_eff = k = −3w) + G11 gate inserted, ChromaDB rebuilt

**Current priorities:**
1. **Update PFD_PROJECT_FOUNDATIONAL_PLAN.md** — ✅ this update (v1.2)
2. **Fix D3.js bugs:** degenerate node toggle (can't re-enable) + 30% node size increase
3. **Begin Phase 3A:** Dynamic Channel Resolution — `claim_extractor.py` + enhanced `result_validator.py`
4. **Begin formality_tier batch assignment** for existing DS Wiki entries (gates Phase 4)
5. **Formal derivation:** D_eff = k from Fisher Information on Cadoni matched metric (feeds G11)
6. **Phase 3C prerequisite:** Build ≥1 more paper-based RRP to enable cross-RRP ontology queries

---

---

## 13. Stress Test Record

### 13.1 Stress Test 1 (2026-03-11)

**Source Document:** `Outside Ref/Analysis of Systemic Vulnerabilities.md`
**Conducted by:** External analysis, incorporated into v1.1
**Purpose:** Identify critical architectural vulnerabilities and implementation impediments before Phase 3 development begins

**Summary:** 6 vulnerabilities identified, 3 architectural mitigations recommended. All 6 assessed. 3 required immediate architectural changes (incorporated into v1.1). 2 manageable by existing design with clarification. 1 known gap acknowledged as partially unresolvable.

---

#### Vulnerability 1: Linguistic-to-Logical Translation Discrepancy

**Stated Risk:** LLM claim extraction is unreliable. Confabulation and oversimplification corrupt downstream layers. The entire pipeline is only as valid as its first step.

**Assessment: VALID — requires architectural enforcement**

LLMs produce confident-sounding but incorrect structural representations of complex prose. This is well-documented. The downstream layers cannot detect or correct a bad extraction — they will build valid-looking logic chains on invalid premises.

**Resolution in v1.1:**
- Layer 1 elevated from "optional review" to **mandatory hard gate** — pipeline pauses, human confirms every extracted claim before proceeding
- This is a hard architectural requirement enforced in the pipeline controller, not a UI preference
- Extraction module documentation explicitly states: "Output is a hypothesis about what the paper claims, not a ground truth"

**Status:** ✅ Resolved architecturally in v1.1

---

#### Vulnerability 2: Error Propagation and Compounding

**Stated Risk:** 6-layer sequential pipeline compounds errors multiplicatively. At 90% per-layer accuracy, end-to-end reliability is ~53%. Alert fatigue and tool abandonment follow.

**Assessment: VALID for binary systems — resolved by probabilistic design**

The arithmetic is correct. Binary pipelines (VALID/INVALID per step) cascade errors catastrophically. However, our design does not use binary outputs — it uses graded confidence scores. The compounding is real but becomes honest uncertainty representation, not cascading false alarms.

**Resolution in v1.1:**
- Explicit cross-layer confidence compounding formula added (Section 5.1): `final_confidence = Π(layer_i_confidence)`
- Confidence floor added: outputs below 0.60 are flagged as "insufficient confidence — human review required" and do NOT produce plausible/contradicting/novel verdicts
- Formality tier caps prevent overconfident outputs from soft-science chains
- Mandatory Layer 1 gate interrupts the cascade before it propagates

**Status:** ✅ Resolved by design — compounding is honest, not hidden; floor prevents false verdicts

---

#### Vulnerability 3: Ontological Engineering Dilemma

**Stated Risk:** Formalizing biology, sociology, economics into strict logic axioms is historically intractable. A unified schema across physics AND soft sciences causes graph traversal failures.

**Assessment: VALID — requires multi-tier formality architecture**

This is the core failure mode of CYC, the Semantic Web, and virtually every universal knowledge formalization attempt. Deterministic axioms cannot represent emergent phenomena, statistical tendencies, or context-dependent heuristics.

**Resolution in v1.1:**
- `formality_tier` field added as required schema element for all DS Wiki entries (Section 2.3, Layer 2)
- Tier 1 (physics/math/CS): strict logical axioms, boolean inference where warranted
- Tier 2 (chemistry/molecular biology): probabilistic inference, confidence capped at 0.85
- Tier 3 (ecology/economics/social sciences): association patterns only, confidence capped at 0.70, always labeled "domain-dependent"
- Logic chain validator applies tier-appropriate inference rules — no longer one universal engine
- Phase 4.0 prerequisite: batch formality_tier assignment for all existing DS Wiki entries before logic encoding

**Status:** ✅ Resolved architecturally in v1.1. Tier system is the formal response to this class of failure.

---

#### Vulnerability 4: Hypergraph Topology Distortion

**Stated Risk:** Scientific relationships are often N-to-N (stoichiometry, metabolic networks, multi-factor causation). Binary node-edge graphs distort these relationships and invalidate logical conclusions.

**Assessment: VALID — known issue, design decision required before Phase 2**

This is not a new discovery — the E. coli parser notes ("stoichiometry IS the link graph") already identified this. What the stress test correctly flags is that failing to make an explicit architectural decision before implementation will result in a parser that silently distorts biochemical reality.

**Resolution in v1.1:**
- Phase 2, Task 0 added: explicit hyperedge architecture decision MUST be documented before any E. coli code
- Two options presented (reification vs. native hyperedge table)
- Recommendation: Option A reification for Phase 2 (pragmatic), native hyperedge upgrade in Phase 4
- All metabolic/network RRP analysis reports carry explicit disclaimer about binary graph approximation

**Status:** ✅ Gated — cannot be ignored, decision forced before implementation

---

#### Vulnerability 5: Contextual Collapse and Unarticulated Assumptions

**Stated Risk:** Papers omit enormous amounts of implicit background knowledge. PFD cannot distinguish a fatal logical gap from a permissible expert assumption. False flagging of standard omissions creates noise.

**Assessment: PARTIALLY VALID — partially convertible to a feature**

Cannot be fully solved. No system can enumerate all implicit assumptions across all domains. However, it is partially addressable:

- DS Wiki domain_boundaries encode "standard background knowledge" per domain
- Type A omissions (universally assumed for domain) are excluded from flagging
- Type B omissions (non-standard intermediate steps) ARE flagged — this is genuinely useful
- Type C (DS Wiki gap, no entry exists) are flagged as DS Wiki improvement requests

**Resolution in v1.1:**
- Three-tier assumption classification added to Section 5.2: Type A (suppress), Type B (flag), Type C (DS Wiki gap)
- Every PFD report includes explicit disclaimer: "PFD cannot detect all implicit assumptions. Domain experts should review flagged assumptions in context."
- Type A assumption lists per domain = Phase 4 contribution task (community-maintained)

**Status:** ⚠ Partially resolved. Known irreducible limitation. Explicitly acknowledged in all report outputs.

---

#### Vulnerability 6: Cold Start Knowledge Deficit

**Stated Risk:** System must demonstrate value before DS Wiki achieves critical mass, but needs critical mass before it can demonstrate value. Paradox.

**Assessment: VALID — managed by roadmap discipline, not architecture**

This is a bootstrapping problem, not an architectural one. No code change solves it. It requires sequence discipline and demonstrating value in narrow domains before attempting breadth.

**Resolution in v1.1:**
- Phase 3 restricted to thermodynamics + CS complexity vertical (Section 4.2 vertical integration constraint)
- ZooClasses and Periodic Table analyses serve as pre-Phase-3 demonstration assets
- DS Wiki coverage dashboard planned (shows community which domains need work)
- Cross-domain analysis gated behind coverage threshold (>80% entries with formality_tier + domain_boundaries)
- Cold start acknowledged as ongoing risk (Risk 9)

**Status:** ✅ Managed by roadmap discipline. Not architecturally solvable — requires sustained community building.

---

#### Recommended Mitigations — Adoption Status

| Recommendation | Status | Implementation |
|----------------|--------|----------------|
| Vertical integration first (start with one sub-domain) | ✅ Adopted | Phase 3 restricted to thermodynamics + CS complexity; Section 4.2 updated |
| Probabilistic logic networks (not boolean graph traversal) | ✅ Adopted | Section 5.2 rewritten; probabilistic traversal specified; Tier system enforces domain-appropriate inference |
| Interactive interventions (human gate between layers) | ✅ Adopted | Layer 1 mandatory hard gate added to Section 2.1; Section 4.2 claim extractor updated |

---

#### Architectural Changes Made in v1.1 (Summary)

| Change | Section | Drives |
|--------|---------|--------|
| Layer 1 mandatory hard gate | 2.1 | Stops error cascade at source |
| Probabilistic pipeline notation | 2.1 | Honest uncertainty representation |
| `formality_tier` field (Tier 1/2/3) | 2.3 | Prevents soft-science formalization failure |
| Cross-layer confidence compounding formula | 5.1 | Honest compounding, not hidden |
| Confidence floor at 0.60 | 5.1 | Prevents low-quality verdicts |
| Probabilistic logic chain traversal | 5.2 | Not boolean — path probability not VALID/INVALID |
| Three-tier assumption handling (Type A/B/C) | 5.2 | Reduces false flagging of standard omissions |
| Phase 2 Task 0: hyperedge decision gate | 4.1 | Forces architectural decision before implementation |
| Phase 3 vertical integration constraint | 4.2 | Cold start mitigation |
| 4 new risks added (6-9) | 8.1 | Expands risk register |

---

### 13.2 Stress Test 2 (Pending)

**Scheduled:** After Phase 2 completion
**Scope:** Validate that E. coli parser hyperedge approach is sound; validate that Phase 3 thermodynamics vertical produces useful outputs before expanding; validate confidence compounding formula calibration

---

## Appendix A: Glossary

- **PFD:** Principia Formal Diagnostics (full project name)
- **DS Wiki:** Original project (prior to transition)
- **RRP:** Reproducible Research Package (ingested dataset bundle)
- **Pass 1:** Parsing (extract entries + links from RRP)
- **Pass 1.5:** Entity Catalog Pass (extract patterns from entity data)
- **Pass 2:** Cross-Universe Query (find DS Wiki bridges)
- **Pass 2b:** Re-run of Pass 2 (after Pass 1.5, on enriched bundle)
- **Tier-1.5 Bridge:** High-confidence semantic connection (>0.85 similarity)
- **Tier-2 Bridge:** Medium-confidence connection (0.75-0.85)
- **Confidence Tier:** Link classification by strength
- **Domain Boundary:** Limits of applicability for a principle
- **Formal Logic Form:** Mathematical representation of a principle
- **Anomaly Detection:** Identifying statistical outliers in data

---

## Appendix B: Example Paper Analysis Report (Template)

```
RESEARCH COHERENCE ANALYSIS REPORT
===================================
Paper: "Relativistic Effects in Gold: Spectroscopic Evidence"
Analysis Date: 2026-03-11
Analyst: PFD v1.0

1. CLAIM EXTRACTION
─────────────────
Extracted 3 core claims:
  Claim 1: Gold exhibits relativistic electron contraction
           Confidence: 0.92 | Domain: Physics/Chemistry
  Claim 2: This contraction affects optical absorption spectra
           Confidence: 0.87 | Domain: Spectroscopy
  Claim 3: The effect is inconsistent with non-relativistic QM
           Confidence: 0.95 | Domain: Quantum Mechanics

2. FOUNDATION MATCHING
──────────────────────
Claim 1 — Top DS Wiki matches:
  ✓ EM13 (Wiedemann-Franz Law)      — Sim: 0.83 | Domain: Electromagnetic
  ✓ QM3 (Pauli Exclusion)            — Sim: 0.76 | Domain: Quantum
  ⚠ B3 (Wien's Displacement Law)    — Sim: 0.79 | Marginal applicability

3. LOGICAL CHAIN VALIDATION
─────────────────────────────
Claim 1 logical structure:
  Premise 1: Z(Au) = 79 (high nuclear charge)
    ✓ Support: Documented in DS Wiki
  Premise 2: High charge → strong e⁻ attraction
    ✓ Support: Coulomb's Law (EM6)
  Premise 3: Strong attraction → relativistic velocities
    ⚠ Support: Requires QED (NOT explicit in DS Wiki) — CONFIDENCE DROP: 0.71
  Conclusion: Orbitals contract
    ✓ Logical consequence of premises

Confidence: 0.71 (plausible, but relies on missing formal layer)

4. ARGUMENT QUALITY
──────────────────
Argument form identified: Causal chain (cause → effect → observable)
  Risk: "Missing QED axioms" — flag for expert review
  Strength: Valid argument form, but weak on formal grounding
  No fallacies detected

5. EVIDENCE SUFFICIENCY
───────────────────────
Domain: Physics/Chemistry
Required evidence standard: [empirical + mathematical + computational]
  ✓ Mathematical: Cites QED derivation
  ~ Computational: Band structure diagram shown, not analyzed
  ⚠ Empirical: XPS spectra mentioned but not analyzed in detail
Verdict: PARTIAL — missing explicit spectroscopic analysis

6. DOMAIN BOUNDARY CHECK
────────────────────────
Gold at: STP (standard temperature/pressure)
Applicable laws:
  ✓ Wiedemann-Franz applies to: metals at STP
  ✓ Pauli Exclusion applies to: fermionic systems (includes Au)
  ✓ No boundary violations detected

7. EXPERT OVERRIDE POINTS
──────────────────────────
[ ] Disagree with logical chain? ← Click to annotate
[ ] Think evidence is sufficient? ← Override standard
[ ] Know a DS Wiki entry we missed? ← Suggest link
[ ] Disagree with argument quality? ← Explain why

8. OVERALL ASSESSMENT
─────────────────────
Status: PLAUSIBLE & CONSISTENT (0.71 confidence)
Verdict: Paper is logically sound but relies on missing formal layer (QED)
Next Steps:
  → Either: DS Wiki needs QED axioms formalized
  → Or: Paper should cite QED explicitly
Recommendation: ACCEPT with minor revision (add QED citation)

AUDIT TRAIL
────────────
Generated by: PFD v3.0
Timestamp: 2026-03-11 14:32:05 UTC
Domain Expert Review: None yet (open for annotation)
```

---

## Document Metadata

**Document:** PFD_PROJECT_FOUNDATIONAL_PLAN.md
**Version:** 1.1
**Date:** 2026-03-11
**Author:** Principia Formal Diagnostics Core Team
**Status:** Approved for Implementation — Stress Test 1 Incorporated
**Stress Tests Completed:** 1 of 2 (ST2 scheduled post Phase 2)
**Next Review:** After Phase 2 completion + Stress Test 2 (2026-04-01)
**Git Location:** https://github.com/IanD25/ds-wiki-transformer/blob/main/PFD_PROJECT_FOUNDATIONAL_PLAN.md

