# Implementation Roadmap — Semantic Knowledge Graph Toolkit

**Current Status**: Specification complete (GENERIC_TOOLKIT_SPEC.md)
**Next**: Begin Phase 1 implementation (Diagnostic Toolkit)

---

## What's Been Designed

✅ **GENERIC_TOOLKIT_SPEC.md** — 1,083 lines covering:
- Core architecture (SQLite + ChromaDB + taxonomy)
- Data ingestion pipeline (CSV/JSON/custom formats via YAML config)
- Taxonomy layer system (user-defined properties, controlled vocabularies)
- Vector indexing and semantic enrichment (BGE embeddings + boosting)
- Link management and validation (3-tier confidence tiers)
- **Diagnostic Toolkit Features** (result validator, gap analyzer, hypothesis generator)
- Reusability patterns and PyPI packaging
- DS framework as flagship application
- 4-phase MVP roadmap

---

## Phase 0: Scaffolding (COMPLETE)

**Current state**: All infrastructure built in DS framework

- ✅ SQLite schema (normalized entities/sections/properties/links)
- ✅ Ingestion framework (reference laws imported + Phase 1-3 taxonomy applied)
- ✅ Taxonomy YAML loader + application engine (archetypes, D-sensitivity, concept tags)
- ✅ ChromaDB + sentence-transformers embedding pipeline
- ✅ Pairwise analysis engine (983 pairs discovered post-Phase2)
- ✅ Link validator and confidence tiers (254 total links: 167 canonical + 87 discovered + 38 validated)

**Proven on**: 156 entries, 1,261 chunks, 384-dim embeddings

---

## Phase 1: Diagnostics (NEXT — 2-3 weeks)

Implement the four core diagnostic tools:

### 1.1 Result Validator

**Goal**: User submits research claim; system checks KB for supporting/contradicting evidence.

**Implementation file**: `src/analysis/result_validator.py`

```python
class ResultValidator:
    def __init__(self, db_path: str, chroma_collection):
        """Load KB embeddings + link structure."""
        pass

    def validate_claim(self, claim: str, claim_entity_type: str) -> ValidationResult:
        """
        1. Embed claim using BGE
        2. Query ChromaDB for top-10 similar chunks (cosine similarity)
        3. Trace chunk → entity → existing links
        4. Categorize evidence:
           - supporting: exists high-sim entity with derives_from or analogous_to link
           - contradicting: exists high-sim entity with contradicts link
           - related: high-sim but no direct link (suggest for investigation)
        5. Return consistency_score, supporting_evidence list, contradictions list

        Consistency_score = (supporting_count - 0.5*contradicting_count) / total_relevant
        """
        pass
```

**Input**: Research claim string + entity type
**Output**: `ValidationResult` with consistency score (0-1), supporting evidence, contradictions, related entities

**Test case**: User submits claim "Protein X inhibits pathway Y" → System finds 3 high-sim experimental findings that support, 0 contradictions → consistency_score = 0.85

---

### 1.2 Gap Analyzer

**Goal**: Identify under-covered domains and suggest entity creation priorities.

**Implementation file**: `src/analysis/gap_analyzer.py`

```python
class GapAnalyzer:
    def analyze_coverage(self, db_path: str) -> GapAnalysisReport:
        """
        For each (entity_type, property_name) pair:
        1. Count entities with property_value populated
        2. Compute % coverage
        3. Identify properties with <80% coverage (flag for enrichment)

        For each taxonomy layer:
        1. Count entities per controlled vocabulary value
        2. Compute distribution (e.g., "60% of laws are conservation-law, 15% are power-law...")
        3. Flag extremely sparse categories (<3% representation)

        For each entity_type:
        1. Compare observed count vs. expected count (heuristic based on domain)
        2. Suggest "add 5-10 more experimental_findings to balance organism coverage"

        Returns: GapAnalysisReport with human-readable markdown summary + structured data
        """
        pass

    @property
    def heuristics(self) -> Dict[str, Callable]:
        """User-customizable coverage expectation heuristics."""
        pass
```

**Input**: DB path
**Output**: Markdown report with sections:
- Coverage summary (% complete by property)
- Taxonomy distribution (which categories are over/under-represented)
- Entity type balance (do you have enough of each type?)
- Enrichment priorities (ranked list of what to add next)

**Test case**: DS framework → "Concept Tags coverage: 100%. Dimensional_sensitivity: 99%. Gap: only 8/156 entries have cross-domain links. Recommend adding Tier 2 links to 40 more pairs."

---

### 1.3 Hypothesis Generator

**Goal**: Suggest novel research directions from unexpected similarities.

**Implementation file**: `src/analysis/hypothesis_generator.py`

```python
class HypothesisGenerator:
    def __init__(self, db_path: str, chroma_collection, baseline_pairs: int = None):
        """Load pairwise analysis results."""
        pass

    def find_surprising_pairs(self,
                             similarity_threshold: float = 0.80,
                             surprise_factor: float = 2.0) -> List[SurprisingPair]:
        """
        1. Compute pairwise similarities (entry centroids)
        2. Filter to pairs >= similarity_threshold
        3. For each pair, compute "surprise" = actual_similarity / expected_similarity_for_type_pair
           (expected based on baseline intra-domain similarity)
        4. Return pairs where surprise >= surprise_factor (e.g., 2x more similar than expected)
        5. Prefer cross-entity-type and cross-domain pairs
        """
        pass

    def generate_research_prompts(self, pair: Tuple[str, str]) -> List[str]:
        """
        Given entities A and B that are unexpectedly similar, generate 5-7 natural-language
        research questions that could guide domain experts:

        Examples (DS context):
        - "Does [A: Landauer's principle] have analogous form in [B: Wien's displacement law]?"
        - "Could [A: dimensional scaling operator] explain [B: Stefan-Boltzmann law] under D ≠ 4?"
        - "Is [A: information thermodynamics] a special case of [B: statistical mechanics]?"

        Implementation: Template-based LLM prompts or rule-based logic on entity types + similarity.
        """
        pass
```

**Input**: DB path + similarity thresholds
**Output**: List of `SurprisingPair` objects with:
- entity_a, entity_b
- similarity score
- surprise factor (how much more similar than expected?)
- 5-7 natural-language research prompts

**Test case**: DS framework → Finds (B5: "Landauer's principle", TD3: "Second law of thermodynamics"), similarity=0.87, surprise=2.1x → Prompts: "Is Landauer's erasure energy a direct consequence of entropy increase?" "Could information-theoretic bounds generalize the thermodynamic bound?"

---

### 1.4 Coverage Analyzer

**Goal**: Quantify knowledge base completeness and balance.

**Implementation file**: `src/analysis/coverage_analyzer.py`

```python
class CoverageAnalyzer:
    def compute_coverage_by_type(self, db_path: str) -> Dict[str, Dict[str, float]]:
        """
        Structure:
        {
            "reference_law": {
                "mathematical_archetype": 1.0,     # 100% have archetype
                "dimensional_sensitivity": 0.96,
                "concept_tags": 0.98,
                ...
            },
            "DS_native": {
                "mathematical_archetype": 0.95,
                ...
            }
        }
        """
        pass

    def compute_coverage_by_property(self, db_path: str) -> Dict[str, PropertyCoverageStats]:
        """
        Structure:
        {
            "mathematical_archetype": {
                "total_entities": 156,
                "filled": 155,
                "coverage": 0.994,
                "value_distribution": {
                    "conservation-law": 0.32,
                    "power-law-scaling": 0.18,
                    ...
                },
                "sparse_categories": ["geometric-ratio"],  # < 3% representation
            }
        }
        """
        pass

    def compute_network_density(self, db_path: str) -> Dict:
        """
        Link-level metrics:
        - total_entities: N
        - total_links: M
        - density: M / (N * (N-1) / 2)  [0-1; higher = more connected]
        - avg_links_per_entity: M / N
        - isolated_entities: count with no links
        - dominant_link_types: which types are most common
        """
        pass

    def coverage_report(self) -> str:
        """
        Generate markdown report with sections:
        1. Overall statistics (N entities, M links, % coverage)
        2. Coverage by entity type (table)
        3. Coverage by property (table)
        4. Network density and connectivity
        5. Identified gaps (sparse categories, isolated entities)
        6. Recommendations for next enrichment steps
        """
        pass
```

**Input**: DB path
**Output**: Markdown report with 6 sections + structured metrics

**Test case**: DS framework → "156 entities, 254 links (density: 0.021). Mathematical archetypes: 100% coverage, 15 distinct categories, balanced. Concept tags: 98% coverage. Gap: Isolated entities (ES domain): 3 entries. Recommendation: add cross-domain links to Earth sciences findings."

---

## Implementation Strategy

### Code Organization

```
src/analysis/
├── __init__.py
├── result_validator.py      # Claim consistency checking
├── gap_analyzer.py          # Coverage identification
├── hypothesis_generator.py  # Novelty detection
├── coverage_analyzer.py     # Network metrics
└── diagnostics_suite.py     # Unified entry point
```

### Integration with Existing Code

```python
# In src/sync.py or new src/diagnostics_cli.py

from semantic_kg.analysis import (
    ResultValidator,
    GapAnalyzer,
    HypothesisGenerator,
    CoverageAnalyzer
)

def run_diagnostic_suite(db_path: str, chroma_collection) -> DiagnosticsReport:
    """Run all 4 diagnostic tools and aggregate results."""

    print("Running diagnostics suite...")

    # 1. Coverage analysis
    analyzer = CoverageAnalyzer(db_path, chroma_collection)
    coverage = analyzer.coverage_report()
    print(f"✓ Coverage report generated")

    # 2. Gap analysis
    gap_analyzer = GapAnalyzer(db_path)
    gaps = gap_analyzer.analyze_coverage()
    print(f"✓ Gap analysis complete: {gaps.summary}")

    # 3. Pairwise analysis + hypothesis generation
    hypothesizer = HypothesisGenerator(db_path, chroma_collection)
    surprising_pairs = hypothesizer.find_surprising_pairs(surprise_factor=2.0)
    prompts = {}
    for pair in surprising_pairs:
        prompts[pair] = hypothesizer.generate_research_prompts(pair)
    print(f"✓ Found {len(surprising_pairs)} surprising pairs, generated prompts")

    # 4. Claim validation (example)
    validator = ResultValidator(db_path, chroma_collection)
    # (User-driven; example below)
    # claim_result = validator.validate_claim("...", "experimental_finding")

    return {
        "coverage_report": coverage,
        "gap_analysis": gaps,
        "surprising_pairs": surprising_pairs,
        "research_prompts": prompts
    }
```

---

## Phase 1 Timeline

| Task | Days | Effort |
|------|------|--------|
| ResultValidator implementation + tests | 3 | High |
| GapAnalyzer implementation + tests | 2 | Medium |
| HypothesisGenerator implementation + tests | 3 | High |
| CoverageAnalyzer implementation + tests | 2 | Medium |
| Unified CLI interface (`diagnostics.py`) | 2 | Medium |
| End-to-end testing on DS framework | 1 | Low |
| Documentation + examples | 2 | Medium |
| **Phase 1 Total** | **15 days** | — |

**Realistic timeline**: 2-3 weeks (accounting for iteration, debugging, refinement).

---

## Testing Strategy (Phase 1)

### Unit Tests
- `test_result_validator.py`: Claim embedding, similarity search, evidence classification
- `test_gap_analyzer.py`: Coverage computation, heuristic validation
- `test_hypothesis_generator.py`: Pairwise analysis, surprise factor, prompt generation
- `test_coverage_analyzer.py`: Metrics computation, report generation

### Integration Tests
- Run all diagnostics on DS framework → validate expected outputs
- Spot-check: surprise_pairs should include known cross-domain analogies (e.g., Landauer ↔ Wien)
- Spot-check: gap_analysis should flag isolated ES entries
- Spot-check: coverage_report should show 100% archetype, 98% tags, 99% D-sensitivity

### Expected Output (DS Framework)

```markdown
# Diagnostic Suite Report — DS Framework

## Coverage Analysis
- Entities: 156
- Sections: 1,261
- Links: 254 (canonical: 167, discovered: 87, validated: 38)

### Property Coverage
| Property | Filled | % | Notes |
|----------|--------|---|-------|
| mathematical_archetype | 156 | 100% | Complete |
| dimensional_sensitivity | 155 | 99% | 1 entry needs review |
| concept_tags | 153 | 98% | 3 entries sparse |

### Network Metrics
- Link density: 0.021 (2.1% of possible edges)
- Avg links per entity: 1.6
- Isolated entities: 0
- Most common link types: derives_from (89), analogous_to (73), ...

## Gap Analysis
- **Sparse categories**: geometric-ratio (2%), wave-equation (4%)
- **Under-covered domains**: Earth Sciences (3 entities, should be 5-7)
- **Recommendation**: Add 4-5 more ES entries; enrich geometric-ratio laws with additional cross-links

## Surprising Pairs (Novelty Signal)
- B5 (Landauer) ↔ TD3 (2nd Law): 0.87 similarity, 2.1x surprise
- OmD (Ω_D) ↔ EM6 (Lorentz): 0.84 similarity, 1.9x surprise
- [... 12 more pairs ...]

### Generated Research Prompts (Sample)
**For B5 ↔ TD3**:
- "Is Landauer's minimum erasure energy a direct consequence of entropy increase?"
- "Could information-theoretic bounds generalize the thermodynamic bound?"
- "Do erasure cascades mimic thermodynamic irreversibility at the bit level?"

## Result Validation Examples
**Claim**: "Dimensional scaling modifies Newton's constant G"
- **Consistency**: 0.92 (high support)
- **Supporting evidence**: OmD → GV1 (0.89 sim, generalizes), CM2 (0.81 sim, analogous)
- **Contradictions**: None

**Claim**: "Entropy is reversible"
- **Consistency**: 0.05 (strong contradiction)
- **Contradictions**: TD3 (0.98 sim, contradicts), B5 (0.87 sim, contradicts)
```

---

## Next Immediate Step

Once Phase 1 is complete, you'll have:
1. A system for independent claim validation (useful for lab/research teams)
2. Automated gap identification (guides future KB enrichment)
3. Hypothesis generation (novel research directions)
4. Metrics dashboard (know your KB coverage/balance at a glance)

This positions the toolkit for **Phase 2: Usability & Export** (CLI, PyPI packaging, interactive visualizations).

---

## Questions for User Feedback

Before starting Phase 1 implementation, consider:

1. **Result Validator priority**: Is claim validation the highest-value diagnostic, or should we prioritize gap analysis?
2. **Custom validation rules**: Do you want users to define domain-specific validation logic (e.g., "in biology, claims about cell-level processes shouldn't contradict organism-level findings")?
3. **Visualization preference**: Should hypothesis generation output be:
   - Markdown prompts (text-based) ✓ Simple, portable
   - Interactive HTML graph (entity nodes, edge labels) — requires more work but very visual
   - Both?
4. **Surprise factor tuning**: The 2.0x baseline surprise threshold is tunable. For DS, is this right, or should it be more/less aggressive?

---

**Document Version**: 1.0
**Created**: 2026-03-09
**Status**: Ready for feedback before Phase 1 coding begins
