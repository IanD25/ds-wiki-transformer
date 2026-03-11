# Principia Formal Diagnostics (PFD) Project
## Foundational Plan & Scope Kickoff

**Document Version:** 1.0
**Date:** 2026-03-11
**Status:** Approved for implementation
**Project:** Transition from DS_Wiki → Principia Formal Diagnostics (PFD)

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
LAYER 2: Foundation Matching
  [Semantic embedding: which DS Wiki principles are relevant?]
  ↓ TRANSPARENT: all matches shown with similarity scores + domain applicability
  ↓
LAYER 3: Formal Logic Validation
  [Does the claim follow valid inference rules?]
  ↓ TRANSPARENT: logical form shown, inference rules cited, confidence per step
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
  [Transparent reasoning trace + confidence + expert override points]
```

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

### 3.1 What Exists (Phase 0-1.5 Complete)

**Repository:** `/Users/iandarling/Projects/DS_Wiki_Transformation`
**Public:** https://github.com/IanD25/ds-wiki-transformer
**Latest Commit:** 789f99f (2026-03-11)

#### Phase 0: Core Pipeline (COMPLETE)
**Status:** ✅ Fully functional, tested
**Components:**
- `src/config.py` — configuration management
- `src/extractor.py` — entry/section/link extraction from SQLite
- `src/embedder.py` — BGE embedding pipeline (BAAI/bge-small-en-v1.5, 384-dim)
- `src/topology.py` — network metrics (density, centrality, clustering)
- `src/sync.py` — sync extracted content to ChromaDB
- `src/mcp_server.py` — FastMCP server (6 tools exposed)

**Data:**
- `data/ds_wiki.db` — source of truth (SQLite, read-only)
- `data/chroma_db/` — semantic index (1,483 chunks, snapshot snap_20260310_205639)
- `wiki_history.db` — embedding history + topology metrics

**Deliverable:** Semantic search capability, cross-wiki querying via MCP

#### Phase 1: Diagnostic Analysis Tools (COMPLETE)
**Status:** ✅ 268 unit + integration tests passing
**Components:**
- `src/analysis/hypothesis_generator.py` — pairwise entry similarity analysis
  - Metrics: cosine similarity, type-aware baselines, surprise_factor
  - 20 typed prompt templates
  - Test: 31 unit tests (test_hypothesis_generator.py)

- `src/analysis/coverage_analyzer.py` — comprehensive coverage metrics
  - Entity, domain, property, archetype, network analysis
  - Gap heuristics (sparse properties, isolated entries, type imbalance)
  - Markdown report generation
  - Test: 56 unit tests (test_coverage_analyzer.py)

- `src/analysis/result_validator.py` — claim validation against DS Wiki
  - Embedding-based query, ChromaDB matching
  - Classification: supporting/contradicting/related
  - Consistency scoring: (S−0.5C)/max(1,S+C+R)
  - Test: 54 unit + integration tests

- `src/analysis/gap_analyzer.py` — structured gap detection
  - Per-type property gaps, taxonomy sparse values, type balance gaps, link gaps
  - EnrichmentPriority ranking (18 prioritization factors)
  - Test: 75 unit + integration tests (test_gap_analyzer.py)

**MCP Tools Exposed:**
- `validate_claim` — embed claim, query DS Wiki, classify result
- `analyze_gaps` — gap detection with optional override parameters

**Test Suite:** `tests/test_*.py` (268 tests total, all passing)
**Run:** `python3 -m pytest tests/ -v`

**Deliverable:** Research gap identification, claim validation, consistency checking

#### Phase 1.5: Entity Catalog Specialized Pass (COMPLETE)
**Status:** ✅ Tested on Periodic Table RRP
**Components:**
- `src/ingestion/passes/entity_catalog_pass.py` (941 lines)
  - Pattern extraction: 5 types (group_trend, period_trend, block_char, category_char, anomaly)
  - Synthetic entry generation (48 entries from 119 periodic table elements)
  - Notable anomalies: hardcoded prose for Au, Hg, He, C, H (5 entries with domain-expert reasoning)
  - Statistical anomaly detection (z-score > 2.5, 7 numeric properties)

- `src/ingestion/detector.py` (added)
  - `classify_dataset_type()` — fingerprint-based classification
  - Signals: tier_1_5_ratio, mean_sim, source_type_count, max_hub_frac
  - Types: entity_catalog, law_catalog, metabolic_network, unknown

- `scripts/run_entity_catalog_pass.py`
  - Orchestrator: classify → Pass 1.5 → Pass 2b (cross-universe re-query)
  - CLI interface with optional overrides

**Periodic Table Results:**
- Pass 1: 119 elements, 279 links, 0 isolated
- Pass 1.5: 48 synthetic entries added
- Pass 2b: 500 bridges (up from 357), 40 tier-1.5 (up from 0), mean_sim 0.818 (up from 0.797)
- Notable connections verified: Au→Wiedemann-Franz Law, He→van der Waals, H→Pauli Exclusion, C→Kopp's Law

**Deliverable:** Automatic pattern extraction from entity catalogs, improved cross-domain bridge detection

#### Phase 2: RRP Ingestion Pipeline (IN PROGRESS)
**Status:** ✅ Two parsers complete, framework ready
**Components:**
- `src/ingestion/rrp_bundle.py` — RRP SQLite schema (mirrors DS Wiki)
- `src/ingestion/detector.py` — 6 format detectors (zoo_classes_json, cobra_json, flat_json, ro_crate, frictionless, codemeta, citation_cff)
- `src/ingestion/parsers/zoo_classes_parser.py` (COMPLETE)
  - ZooClasses JSON → 426 entries (262 theorem, 157 reference_law, 7 open_question)
  - 437 internal links (243 analogous_to, 189 derives_from)
  - 73 isolated entries (59 foundational theorems = correct, 13 sparse classes, 1 open_question)

- `src/ingestion/parsers/periodic_table_parser.py` (COMPLETE)
  - MIT Periodic Table JSON → 119 elements
  - 14 properties per element (symbol, atomic_number, electronegativity, density, melting/boiling points, ionization energies, etc.)
  - 279 links (group analogies, period correlations, category meshes)
  - Rebuilt Pass 1.5: 48 synthetic patterns → tier-1.5 bridges

- `src/ingestion/cross_universe_query.py` (COMPLETE)
  - Pass 2: RRP embeddings → DS Wiki ChromaDB query
  - Fixed: added "What It Captures" to EMBED_SECTIONS (entity catalogs)
  - Bridge storage with confidence tiers
  - Automatic re-run capability (DELETE + full INSERT)

**Pending Parsers:**
- `src/ingestion/parsers/ecoli_core_parser.py` (cobra_json, hardest — stoichiometry IS the link graph)
- Documentation: INGESTION_GUIDE.md, SCHEMA_REFERENCE.md (now informed by 3 real implementations)

**Deliverable:** Framework for ingesting diverse RRP formats, tested on 2 real bundles

#### Visualization & Reporting Module (COMPLETE)
**Status:** ✅ 3 interactive visualizations, tested
**Components:**
- `src/viz/viz_runner.py` — orchestrator
- 3 outputs per bundle:
  - Bridge network (Plotly interactive graph)
  - Domain heatmap (entry type × domain)
  - Similarity histogram (Plotly distribution)

**Output:** `/data/viz/{bundle_name}/` with .png + .html

**Deliverable:** Interactive analysis reports, publishable visualizations

### 3.2 Version Control & Git History

**Repository:** https://github.com/IanD25/ds-wiki-transformer (public)

**Key Commits (recent):**
```
789f99f (HEAD, 2026-03-11) — Add Pass 1.5 entity catalog pass + fix entity embedding bug
39742e0 — Add Periodic Table RRP parser + Pass 1/2 results (119 elements, 357 bridges)
fb5b8ea — Phase 1 complete + RRP ingestion pipeline + visualization module
ea170ac — Make repo self-contained: commit ds_wiki.db, use relative path
854f5bd — Rewrite README as comprehensive LLM reference
62d7590 — Code audit fixes: update stale counts and paths post Option E
```

**Branch Strategy:**
- `main` — production, always working
- Feature branches deleted after merge (clean history)
- All commits squashed + semantically named

**Asset Versioning:**
- `data/ds_wiki.db` — committed (single source of truth)
- `data/chroma_db/` — NOT committed (rebuilt on `sync.py` run)
- `wiki_history.db` — committed (growing append-only)
- `.gitignore` — maintained for generated artifacts

---

## 4. Planned Implementation Roadmap

### 4.1 Phase 2 Completion (Weeks 1-2)

**Goal:** Complete RRP ingestion framework, tested on all 3 formats

**Tasks:**
1. **E. coli Core Parser** (hardest case — metabolic networks)
   - COBRA JSON format (95 reactions, 72 metabolites, 137 genes)
   - Challenge: stoichiometry matrix IS the relationship graph
   - Solution: Parse metabolite↔reaction↔gene networks as RRP links
   - Output: rrp_ecoli_core.db with ~200 entries, ~500+ links (biochemical pathway structure)

2. **Parser Documentation** (INGESTION_GUIDE.md)
   - Format detection strategy
   - Schema translation (what maps to entries vs. links vs. properties)
   - Example workflows for each format

3. **Schema Reference** (SCHEMA_REFERENCE.md)
   - RRP bundle schema (mirrors DS Wiki)
   - Cross_universe_bridges table specification
   - Property metadata conventions

4. **Integration Tests**
   - Test all 3 parsers end-to-end (detect → parse → Pass 1 → Pass 2 → visualize)
   - Validate output against known good bundles

**Success Criteria:**
- All 3 parsers producing valid bundles with >0 internal links
- E. coli bundle reflects actual metabolic pathways
- Documentation sufficient for community contributor to add 4th parser

**Deliverable:** Complete, tested, documented RRP ingestion pipeline

---

### 4.2 Phase 3: Paper Analysis Suite (Weeks 3-6)

**Goal:** Build claim extraction, validation, and reasoning verification for scientific prose

**Components to Build:**

**3.1 Claim Extraction Module** (`src/analysis/claim_extractor.py`)
- LLM-based structured claim parsing
- Input: paper text (abstract, methods, findings sections)
- Output: `Claim(subject, relationship, object, confidence, domain, source_section)`
- Methods:
  - Prompt engineering (5-shot examples per domain)
  - Coreference resolution (what does "it" refer to?)
  - Scope detection (is this a claim or a background statement?)
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

**Deliverable:** End-to-end paper analysis suite with transparent reasoning traces

---

### 4.3 Phase 4: Logic Foundation Layers (Weeks 7-10)

**Goal:** Encode formal logical foundations, rhetorical logic, epistemological standards

**Components to Build:**

**4.1 Formal Logic Axiom Layer** (`data/logic_foundations/`)
- Propositional logic axioms (law of excluded middle, law of non-contradiction, etc.)
- First-order logic rules (universal quantification, existential instantiation, etc.)
- Inference rules (modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, etc.)
- Modal logic (necessity, possibility, counterfactuals)
- Database tables: logic_axioms, logic_inference_rules, logical_forms (for each DS Wiki entry)

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

**Model:** BAAI/bge-small-en-v1.5 (384-dim)
- Small enough for CPU inference
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

**Confidence Scoring:**
- Not binary (valid/invalid) but graded (0-1)
- Based on: similarity strength, foundation count, evidence presence, chain length
- Formula: `confidence = base_sim × domain_match × chain_depth_discount × evidence_multiplier`

### 5.2 Logic Chain Validation

**Graph Representation:**
- Nodes: DS Wiki entries
- Edges: entry_connections with link_type + confidence_tier
- Edge weights: confidence + domain applicability

**Path Finding:**
- DFS to find paths from claim premises to conclusion
- Depth limit: 3 hops (longer chains less confident)
- Direction validation: link type must support premise→conclusion direction

**Missing Link Detection:**
- If no path exists, flag: "No support found" or "Contradicts"
- If weak path, flag: "Requires intermediates"
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

**Phase 2 Success:**
- ✅ E. coli parser producing biochemically plausible link graph
- ✅ All 3 parsers (zoo, periodic, ecoli) working end-to-end
- ✅ Documentation sufficient for external contributor to add 4th parser

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
WEEK 1-2:   Phase 2 completion (E. coli parser, documentation)
WEEK 3-6:   Phase 3 (Paper analysis suite)
WEEK 7-10:  Phase 4 (Logic foundation layers)
WEEK 11+:   Phase 5 (Community governance, federation)
```

**Notes:**
- Timelines are estimates; actual progress depends on resource availability
- Parallel work encouraged (Phase 3 + 4 may overlap)
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

## 12. Next Immediate Actions (Week of 2026-03-11)

1. **Approve this document** — foundational alignment
2. **Begin Phase 2:** E. coli parser development
3. **Start Phase 3 design doc:** detailed claim extraction specification
4. **Set up GitHub Project board:** track Phase 2-3 work
5. **Recruit domain experts:** (physics, CS, biology) as advisors

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
**Version:** 1.0
**Date:** 2026-03-11
**Author:** Principia Formal Diagnostics Core Team
**Status:** Approved for Implementation
**Next Review:** After Phase 2 completion (2026-04-01)
**Git Location:** https://github.com/IanD25/ds-wiki-transformer/blob/main/PFD_PROJECT_FOUNDATIONAL_PLAN.md

