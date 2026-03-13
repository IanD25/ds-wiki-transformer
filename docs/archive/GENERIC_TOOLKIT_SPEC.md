# Semantic Knowledge Graph Toolkit — Generic Architecture Specification

**Version**: 1.0
**Date**: 2026-03-09
**Status**: Design Phase
**Audience**: Engineers, researchers, domain experts

---

## Executive Summary

The DS Wiki Transformation framework has proven that semantic vector indexing + taxonomy enrichment + explicit link validation creates a powerful discovery engine for complex knowledge bases. This spec generalizes that approach into a reusable, pluggable toolkit (`semantic-knowledge-graph-toolkit`) for any research domain.

**Core insight**: The three-layer architecture (SQLite data → ChromaDB vectors → semantic topology) is domain-agnostic. What changes is:
1. **Input schema**: How domain data maps to normalized entities/sections/properties
2. **Taxonomy layer**: Which properties/dimensions/archetypes matter for *this* domain
3. **Diagnostic rules**: What constitutes valid/invalid/novel connections in *this* domain

**Goal**: Enable researchers with complex knowledge bases to plug in their data, run semantic analysis independently, and discover connections their domain expertise alone might miss.

---

## Part 1: Core Architecture

### 1.1 Three-Layer Stack (Unchanged Pattern)

```
┌─────────────────────────────────────────────────────────┐
│  Layer 3: Semantic Enrichment                           │
│  (Custom archetypes, properties, explicit links)        │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Vector Index                                  │
│  (ChromaDB + BGE embeddings, similarity search)         │
├─────────────────────────────────────────────────────────┤
│  Layer 1: Knowledge Base                                │
│  (SQLite normalized schema)                             │
└─────────────────────────────────────────────────────────┘
```

**Invariants**:
- Layer 1 is always SQLite with normalized entity/section/property/link tables
- Layer 2 always uses sentence-transformers (BGE-small or user-selected model)
- Layer 3 always includes custom properties, taxonomy sections, and explicit link validation

### 1.2 Generic SQLite Schema (Normalized, Domain-Agnostic)

**Core Tables** (required, never modified after creation):

```sql
-- Entities: the "things" in your knowledge base (laws, theorems, concepts, findings, assumptions, etc.)
CREATE TABLE entities (
    entity_id TEXT PRIMARY KEY,
    entity_type TEXT,  -- User-defined: "law", "theorem", "finding", "axiom", "conjecture", etc.
    entity_name TEXT,
    description TEXT,
    created_at TIMESTAMP,
    source_reference TEXT  -- DOI, URL, citation, or "native"
);

-- Sections: richly formatted content blocks within entities (typically embeddable as-is)
CREATE TABLE sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT,
    section_name TEXT,  -- "Formula", "Proof Sketch", "Mathematical Archetype", "Concept Tags", etc.
    content TEXT,       -- Raw markdown/HTML; embeddable
    section_order INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES entities(entity_id)
);

-- Properties: structured key-value metadata (queryable, not directly embedded)
CREATE TABLE entity_properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT,
    property_name TEXT,  -- "mathematical_archetype", "dimensionality_sensitivity", "concept_tags", etc.
    property_value TEXT,  -- JSON-serializable if complex
    prop_order INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES entities(entity_id)
);

-- Links: explicit directed relationships between entities (hand-validated or vectorially-discovered)
CREATE TABLE links (
    link_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT,
    target_id TEXT,
    link_type TEXT,  -- "derives_from", "analogous_to", "generalizes", "implements", "contradicts", etc.
    confidence_tier TEXT,  -- "1" (canonical/original), "1.5" (vectorially-discovered), "2" (hand-validated)
    description TEXT,  -- Reasoning for the link
    created_at TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES entities(entity_id),
    FOREIGN KEY (target_id) REFERENCES entities(entity_id)
);
```

**Extensibility**: Additional columns can be added to entities/sections without schema modification (JSON blobs in description or property_value fields).

---

## Part 2: Data Ingestion Pipeline (Transformer Input Translator)

### 2.1 Ingestion Architecture

```
┌─────────────────────────────────────┐
│  User's Raw Knowledge Base          │  (CSV, JSON, RDF, domain-specific)
│  (arbitrary structure)              │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Input Translator                   │  (configurable adapter)
│  - Parse domain format              │
│  - Map to normalized schema         │
│  - Validate completeness            │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Normalized SQLite DB               │
│  (ready for enrichment)             │
└─────────────────────────────────────┘
```

### 2.2 Input Translator Configuration

Users define a **YAML-based data mapping** that specifies:

**Example 1: CSV Input (Biology Research Project)**

```yaml
# biology_research_ingestion.yaml

input_format: "csv"
input_path: "/data/research_findings.csv"

entity_mapping:
  entity_id_column: "finding_id"
  entity_type_column: "category"  # Column name in CSV
  entity_name_column: "title"
  description_column: "abstract"
  source_reference_column: "doi"

section_mapping:
  - section_name: "Methods"
    column: "methodology"
  - section_name: "Results"
    column: "results"
  - section_name: "Interpretation"
    column: "interpretation"

property_mapping:
  - property_name: "experimental_organism"
    column: "organism"
  - property_name: "sample_size"
    column: "n_samples"
  - property_name: "confidence_level"
    column: "p_value"

validation:
  required_fields: ["finding_id", "title", "methodology", "results"]
  entity_types: ["experimental_finding", "theoretical_prediction", "literature_review", "meta_analysis"]
```

**Example 2: JSON Input (Materials Science Database)**

```yaml
# materials_ingestion.yaml

input_format: "json"
input_path: "/data/materials_db.json"
json_root: "$.materials[*]"  # JSONPath to entity array

entity_mapping:
  entity_id: "$.material_id"
  entity_type: "$.classification"  # e.g., "polymer", "ceramic", "composite"
  entity_name: "$.common_name"
  description: "$.summary"
  source_reference: "$.source_doi"

section_mapping:
  - section_name: "Mechanical Properties"
    content_path: "$.properties.mechanical"
  - section_name: "Thermal Behavior"
    content_path: "$.properties.thermal"
  - section_name: "Chemical Composition"
    content_path: "$.composition.description"

property_mapping:
  - property_name: "youngs_modulus"
    value_path: "$.properties.mechanical.youngs_modulus"
  - property_name: "density"
    value_path: "$.properties.physical.density"
```

**Example 3: Domain-Specific (Physics — Custom Ontology)**

```yaml
# physics_custom_ingestion.yaml

input_format: "domain_ontology"
input_path: "/data/physics_ontology.xml"

domain_parser: "physics_xml_parser"  # Custom Python parser class

entity_mapping:
  entity_id: "law_id"
  entity_type: "law_category"  # "conservation_law", "symmetry_principle", "field_equation"
  entity_name: "law_name"
  description: "physical_interpretation"
  source_reference: "canonical_reference"

section_mapping:
  - section_name: "Mathematical Form"
    parser_method: "extract_equation"
  - section_name: "Domain of Validity"
    parser_method: "extract_domain"
  - section_name: "Historical Development"
    parser_method: "extract_history"

property_mapping:
  - property_name: "coupling_strength"
    parser_method: "infer_coupling"
  - property_name: "dimensionality_range"
    parser_method: "infer_valid_dimensions"
```

### 2.3 Ingestion Validator

Before SQLite insertion, the translator runs:

```python
class IngestionValidator:
    """Ensures data quality before semantic analysis."""

    def validate(self, mapped_entities: List[Entity]) -> ValidationReport:
        """
        Returns:
        - coverage: % of required fields filled
        - duplicates: entity IDs appearing >1x
        - orphans: sections referencing non-existent entities
        - type_coverage: distribution of entity_types
        - warnings: suggested enrichments or data quality issues
        """
        pass

    @property
    def validation_rules(self) -> Dict[str, Callable]:
        """User-customizable validation functions."""
        pass
```

**Output**: Human-readable validation report before commit to SQLite.

---

## Part 3: Taxonomy Layer System (Custom Semantic Dimensions)

### 3.1 Taxonomy Definition (YAML)

Instead of hardcoding "mathematical_archetype" and "dimensional_sensitivity", users define domain-specific taxonomy:

```yaml
# taxonomy.yaml for DS Framework (existing example)

taxonomy_layers:
  mathematical_archetype:
    description: "Category of mathematical structure used in this law"
    type: "controlled_vocabulary"
    values:
      - inverse-square-geometric
      - gradient-flux-transport
      - exponential-decay
      - power-law-scaling
      - variational-principle
      - conservation-law
      - thermodynamic-bound
      - diffusion-equation
      - equilibrium-condition
      - wave-equation
      - symmetry-conservation
      - coupled-field-equations
      - statistical-distribution
      - geometric-ratio
      - dimensional-scaling
    applies_to_entity_types: ["reference_law", "DS_native"]
    embedding_weight: 1.0  # How much to boost in vector index

  dimensional_sensitivity:
    description: "Whether this law's form changes under dimensional scaling"
    type: "boolean"
    applies_to_entity_types: ["reference_law", "DS_native"]
    embedding_weight: 0.8  # Slightly lower weight than archetype

  concept_tags:
    description: "Semantic anchor phrases for similarity search"
    type: "text_list"
    max_items: 10
    applies_to_entity_types: ["reference_law", "DS_native"]
    embedding_weight: 0.9
```

### 3.2 Alternative: Biology Research Taxonomy

```yaml
taxonomy_layers:
  experimental_design:
    description: "Study design used"
    type: "controlled_vocabulary"
    values:
      - "randomized_controlled_trial"
      - "observational_cohort"
      - "case_study"
      - "in_vitro_experiment"
      - "animal_model"
      - "meta_analysis"
    applies_to_entity_types: ["experimental_finding", "meta_analysis"]
    embedding_weight: 1.0

  biological_system:
    description: "Level of biological organization studied"
    type: "controlled_vocabulary"
    values:
      - "molecular"
      - "cellular"
      - "tissue"
      - "organ"
      - "organism"
      - "population"
      - "ecosystem"
    applies_to_entity_types: ["experimental_finding", "theoretical_prediction"]
    embedding_weight: 1.0

  confidence_category:
    description: "How well-supported by evidence"
    type: "ordinal"
    values: ["preliminary", "emerging", "established", "consensus"]
    applies_to_entity_types: ["experimental_finding"]
    embedding_weight: 0.7

  related_pathways:
    description: "Named biological pathways involved"
    type: "text_list"
    max_items: 8
    applies_to_entity_types: ["experimental_finding"]
    embedding_weight: 0.8
```

### 3.3 Taxonomy Application Engine

```python
class TaxonomyApplicationEngine:
    """Applies user-defined taxonomy to all entities."""

    def __init__(self, taxonomy_config: str):  # Path to YAML
        self.taxonomy = self._load_yaml(taxonomy_config)

    def apply_all_layers(self, db_path: str) -> ApplicationReport:
        """
        For each taxonomy layer:
        1. Validate against controlled vocabulary (if applicable)
        2. Insert as entity_properties rows
        3. Create section with formatted content (for embedding)
        4. Generate summary statistics

        Returns report on coverage, errors, auto-completions.
        """
        pass

    def get_embedding_config(self) -> Dict[str, float]:
        """Return embedding_weight config for Vector Boosting (below)."""
        pass
```

---

## Part 4: Vector Indexing and Semantic Enrichment

### 4.1 Embedding Model Selection

**Default**: `BAAI/bge-small-en-v1.5` (112M parameters, 384-dim, no API calls, ~90MB)

**User override options**:
- `BAAI/bge-base-en-v1.5` (higher quality, ~350MB, ~15% slower)
- `sentence-transformers/all-MiniLM-L6-v2` (lightweight, 33M parameters)
- Custom fine-tuned model on domain data

```yaml
# config.yaml

embedding:
  model_id: "BAAI/bge-small-en-v1.5"
  dimension: 384
  batch_size: 32
  device: "cpu"  # or "cuda" if GPU available
  cache_embeddings: true
```

### 4.2 Semantic Chunking Strategy

**Default pattern** (proven in DS framework):

```
- Entity-level chunks: one per section (natural units)
- Conjecture/gate-like structures: one chunk per entity
- Bridge content: separate chunks if > 500 tokens
- Metadata attachment: section_name + entity_type preserved in ChromaDB metadata
```

**Chunk ID scheme**: `{entity_id}_{section_name_normalized}` — human-readable, traceable.

### 4.3 Vector Boosting (Taxonomy-Aware Embedding)

**Key innovation**: Higher-valued taxonomy properties amplify their signal in the vector space.

```python
class VectorBoostingEngine:
    """Weights chunk embeddings by taxonomy properties."""

    def compute_boosted_embedding(self,
                                  chunk_id: str,
                                  base_embedding: np.ndarray,  # 384-dim
                                  taxonomy_properties: Dict[str, str],
                                  taxonomy_weights: Dict[str, float]) -> np.ndarray:
        """
        Example:
        - base_embedding: [0.1, -0.05, ..., 0.3]  (384 values)
        - taxonomy_property "mathematical_archetype" = "conservation-law"
        - weight for archetype = 1.0

        Output: scaled embedding where archetype signal is amplified.

        Implementation:
        - For each categorical property, compute micro-embedding
        - Scale by weight
        - Alpha-blend into base embedding
        """
        pass
```

**Effect**: Entries with richer taxonomy data cluster more tightly by domain/category.

### 4.4 Pairwise Analysis (Entry-Level Similarity)

```python
class PairwiseAnalysisEngine:
    """Identifies structural analogies between entries."""

    def compute_entry_centroids(self, db_path: str, chroma_collection) -> Dict[str, np.ndarray]:
        """
        For each entity:
        - Retrieve all chunk embeddings (sections)
        - Average them → entity centroid (384-dim)

        Return: {entity_id: centroid_vector}
        """
        pass

    def find_similar_pairs(self,
                          centroids: Dict[str, np.ndarray],
                          similarity_threshold: float = 0.80) -> List[Tuple[str, str, float]]:
        """
        Compute N×N cosine similarity matrix.
        Return pairs (entity1, entity2, similarity) where similarity >= threshold.
        """
        pass

    def annotate_by_entity_type(self, pairs: List[Tuple[str, str, float]]) -> Dict[str, List[Tuple[str, str, float]]]:
        """Group by (source_type, target_type) for cross-domain analysis."""
        pass
```

**Output**: CSV or interactive visualization showing:
- Intra-domain pairs (high confidence, likely known)
- Cross-domain pairs (novelty signal)
- Isolated entries (low similarity to any other entity)

---

## Part 5: Link Management and Validation

### 5.1 Three-Tier Link Confidence System

**Tier 1**: Canonical links (original knowledge base or authoritative source)
**Tier 1.5**: Vectorially-discovered (high cosine similarity, automated)
**Tier 2**: Hand-validated (domain expert reviewed, explicit reasoning provided)

### 5.2 Link Validator

```python
class LinkValidator:
    """Proposes, validates, and stores explicit links."""

    def extract_tier_1_links(self, db_path: str) -> List[Link]:
        """Read canonical links already in database."""
        pass

    def discover_tier_1_5_links(self,
                               pairwise_pairs: List[Tuple[str, str, float]],
                               min_similarity: float = 0.82) -> List[ProposedLink]:
        """
        Convert pairwise pairs into link objects.
        Assign relationship type heuristically based on entity_type, similarity, etc.

        Returns list of proposed links for review or auto-insertion.
        """
        pass

    def propose_tier_2_links(self,
                            entity_pairs: List[Tuple[str, str]],
                            link_types: List[str]) -> List[ProposedLink]:
        """
        User manually specifies promising entity pairs + link types.
        System generates reasoning placeholders.
        User fills in explicit derivation/reasoning.
        """
        pass

    def validate_link_consistency(self, db_path: str) -> ValidationReport:
        """Check for cycles, contradictions, transitivity violations."""
        pass
```

### 5.3 Link Types (User-Configurable)

```yaml
# link_types.yaml

link_types:
  derives_from:
    description: "Target mathematically follows from source assumptions"
    directionality: "source → target"
    transitive: true

  analogous_to:
    description: "Target has structural similarity to source"
    directionality: "bidirectional"
    transitive: false

  generalizes:
    description: "Source is a special case of target"
    directionality: "source → target"
    transitive: true

  contradicts:
    description: "Target contradicts or refutes source (under certain conditions)"
    directionality: "bidirectional"
    transitive: false

  implements:
    description: "Target is a practical/algorithmic application of source"
    directionality: "source → target"
    transitive: false

  couples_to:
    description: "Source and target appear together in research/applications"
    directionality: "bidirectional"
    transitive: false
```

---

## Part 6: Diagnostic Toolkit Features

### 6.1 Independent Result Validation

```python
class ResultValidator:
    """Validates research findings against knowledge base for consistency."""

    def check_claim_against_kb(self,
                               claim: str,
                               claim_entity_type: str) -> ValidationResult:
        """
        User submits a research claim (e.g., "Protein X increases cell proliferation").

        1. Embed the claim
        2. Search knowledge base for relevant entities (semantic neighbors)
        3. Check for:
           - Supporting evidence (high-similarity entities with "supports" or "derives_from" links)
           - Contradictions (high-similarity with "contradicts" links)
           - Domain precedent (are similar claims documented?)

        Returns:
        - consistency_score (0-1)
        - supporting_evidence: [(entity_id, similarity, link_type)]
        - contradictions: [(entity_id, similarity, reasoning)]
        - domain_context: historical claims in same space
        """
        pass

    def gap_analysis(self, db_path: str) -> GapAnalysisReport:
        """
        For each entity_type:
        - Count how many entities vs. expected coverage
        - Identify sparsely-covered domains
        - Suggest entity creation to fill gaps

        Example output:
        "Biological_system taxonomy has 100 cellular entities but only 3 organ-level entities.
         Consider adding 5-10 organ-level findings to balance representation."
        """
        pass
```

### 6.2 Hypothesis Generation

```python
class HypothesisGenerator:
    """Suggests novel research directions from unexpected similarities."""

    def find_surprising_pairs(self,
                             pairwise_pairs: List[Tuple[str, str, float]],
                             baseline_pairs: int) -> List[SurprisingPair]:
        """
        Identify high-similarity pairs that:
        - Cross entity_types (e.g., experimental finding ↔ theoretical prediction)
        - Cross domains (e.g., biology ↔ materials science)
        - Have no existing links (unexpected connection)

        Returns with confidence scores and "why is this pair similar?" heuristics.
        """
        pass

    def generate_research_prompts(self,
                                 surprising_pair: Tuple[str, str]) -> List[str]:
        """
        Given entities A and B that are unexpectedly similar:

        Generate natural-language research questions like:
        "Does mechanism in [Entity A] apply to [Entity B]?"
        "Could [Domain A] findings explain [Domain B] observations?"

        Intended as conversation starters for domain experts.
        """
        pass
```

### 6.3 Domain Coverage Analysis

```python
class CoverageAnalyzer:
    """Measures knowledge base completeness and balance."""

    def compute_coverage_by_type(self, db_path: str) -> Dict[str, float]:
        """
        For each entity_type: % of entities with each property filled.

        Example:
        {
          "reference_law": {
            "mathematical_archetype": 1.0,  # 100% of reference laws have archetype
            "dimensional_sensitivity": 0.96,
            "concept_tags": 0.98,
            ...
          },
          "experimental_finding": {
            "experimental_design": 0.87,
            "biological_system": 0.92,
            ...
          }
        }
        """
        pass

    def compute_coverage_by_property(self, db_path: str) -> Dict[str, CoverageStats]:
        """
        For each property: distribution of values, coverage %, common/rare categories.

        Identifies properties that are under-utilized or over-concentrated.
        """
        pass

    def coverage_report(self) -> str:
        """Human-readable summary with recommendations for gaps."""
        pass
```

---

## Part 7: Reusability Patterns and Packaging

### 7.1 PyPI Package Structure

```
semantic-knowledge-graph-toolkit/
├── README.md
├── setup.py
├── requirements.txt
├── semantic_kg/
│   ├── __init__.py
│   ├── config.py                    # Configuration management
│   ├── core/
│   │   ├── __init__.py
│   │   ├── schema.py                # SQLite schema creation + ORM
│   │   ├── entity.py                # Entity class
│   │   ├── section.py               # Section class
│   │   ├── link.py                  # Link class
│   │   └── property.py              # Property class
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── translator.py            # Abstract base for custom translators
│   │   ├── validators.py            # IngestionValidator
│   │   └── formats/
│   │       ├── csv_translator.py
│   │       ├── json_translator.py
│   │       ├── rdf_translator.py
│   │       └── custom.py            # Custom domain parser base
│   ├── taxonomy/
│   │   ├── __init__.py
│   │   ├── loader.py                # YAML taxonomy loader
│   │   ├── engine.py                # TaxonomyApplicationEngine
│   │   └── validators.py            # Taxonomy validation
│   ├── embedding/
│   │   ├── __init__.py
│   │   ├── models.py                # Model selection + download
│   │   ├── chunking.py              # Chunk strategy
│   │   ├── vector_boosting.py       # VectorBoostingEngine
│   │   └── indexer.py               # ChromaDB management
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── pairwise.py              # PairwiseAnalysisEngine
│   │   ├── links.py                 # LinkValidator
│   │   └── diagnostics.py           # ResultValidator, HypothesisGenerator, CoverageAnalyzer
│   ├── export/
│   │   ├── __init__.py
│   │   ├── csv_exporter.py          # Export to CSV
│   │   ├── json_exporter.py         # Export to JSON
│   │   ├── visualization.py         # Generate interactive HTML similarity graphs
│   │   └── report_generator.py      # Human-readable markdown reports
│   └── cli/
│       ├── __init__.py
│       ├── commands.py              # CLI entry points
│       └── templates/               # YAML templates for ingestion, taxonomy, config
├── examples/
│   ├── ds_framework/                # Full working example (DS 2.x)
│   ├── biology_research/            # Example biology research project
│   └── materials_science/           # Example materials science database
└── tests/
    ├── test_ingestion.py
    ├── test_taxonomy.py
    ├── test_embedding.py
    ├── test_pairwise.py
    └── test_diagnostics.py
```

### 7.2 Usage Pattern (User Perspective)

```python
from semantic_kg import SemanticKnowledgeGraph

# Initialize with minimal config
kg = SemanticKnowledgeGraph(
    db_path="my_research.db",
    embedding_model="BAAI/bge-small-en-v1.5",
    taxonomy_path="taxonomy.yaml"
)

# Ingest data
ingestion_report = kg.ingest(
    input_path="research_findings.csv",
    ingestion_config="ingestion.yaml"
)
print(ingestion_report)  # Coverage, validation errors, etc.

# Apply taxonomy
taxonomy_report = kg.apply_taxonomy()
print(taxonomy_report)

# Analyze semantically
kg.compute_embeddings()
pairs = kg.find_similar_pairs(min_similarity=0.80)
kg.export_pairs_to_csv("similar_pairs.csv")

# Validate results
validator = kg.get_result_validator()
validation = validator.check_claim_against_kb(
    claim="Protein X inhibits pathway Y",
    claim_entity_type="experimental_finding"
)
print(validation.consistency_score)
print(validation.supporting_evidence)

# Generate hypotheses
generator = kg.get_hypothesis_generator()
for pair in pairs[:10]:
    prompts = generator.generate_research_prompts(pair)
    for prompt in prompts:
        print(f"  ? {prompt}")

# Get coverage report
analyzer = kg.get_coverage_analyzer()
report = analyzer.coverage_report()
print(report)
```

### 7.3 CLI Interface

```bash
# Initialize a new project
semantic-kg init --project my_research --embedding-model bge-small

# Ingest data
semantic-kg ingest --project my_research \
  --input-path data.csv \
  --ingestion-config ingestion.yaml

# Apply taxonomy
semantic-kg taxonomy apply --project my_research \
  --taxonomy-path taxonomy.yaml

# Analyze
semantic-kg analyze --project my_research \
  --output-dir results/
  # Generates: similar_pairs.csv, gap_analysis.md, coverage_report.md

# Validate a claim
semantic-kg validate-claim --project my_research \
  "Does protein X increase proliferation?" \
  --entity-type experimental_finding

# Generate hypothesis prompts
semantic-kg hypothesize --project my_research \
  --surprise-threshold 2.0 \  # 2x expected similarity
  --output-format markdown

# Export and visualize
semantic-kg export --project my_research \
  --format html \
  --output-file knowledge_graph.html
```

---

## Part 8: Domain-Specific Extensions

### 8.1 Plugin Architecture

Users can extend the toolkit with domain-specific logic:

```python
# custom_parsers.py (user-provided)
from semantic_kg.ingestion import CustomParser

class BiologyOntologyParser(CustomParser):
    """Custom parser for NCBI or UniProt ontology XML."""

    def parse_entity(self, xml_element) -> Entity:
        """Convert XML element to normalized Entity."""
        pass

    def parse_sections(self, xml_element) -> List[Section]:
        """Extract meaningful sections from XML."""
        pass

# custom_validators.py (user-provided)
from semantic_kg.analysis import DiagnosticsPlugin

class BiologyDomainValidator(DiagnosticsPlugin):
    """Domain-specific validation for biology claims."""

    def check_claim_against_kb(self, claim: str) -> Dict:
        """Biology-specific validation logic (e.g., check pathway consistency)."""
        pass
```

### 8.2 Flagship Application: DS Framework

The DS Toolkit becomes an exemplar, with full source code and documentation:

```
examples/ds_framework/
├── README.md                    # How to run DS example
├── ingestion.yaml              # DS-specific mapping from wiki export
├── taxonomy.yaml               # D-sensitivity, archetypes, concept tags
├── config.yaml                 # BGE model, ChromaDB settings
├── scripts/
│   ├── build_ds_knowledge_graph.py    # End-to-end example
│   └── ds_domain_parser.py            # Custom parser for DS wiki SQL dumps
├── data/
│   ├── ds_wiki_export.sql      # Downloadable from public repo
│   └── reference_laws.csv      # 96 reference laws in CSV
└── results/
    ├── similar_pairs.csv
    ├── hypothesis_prompts.md
    └── coverage_report.md
```

---

## Part 9: Minimum Viable Product (MVP) Roadmap

### Phase 0: Scaffolding (Complete)
- ✅ Core SQLite schema
- ✅ Ingestion framework (CSV, JSON templates)
- ✅ Taxonomy YAML loader + application engine
- ✅ ChromaDB + sentence-transformers embedding pipeline
- ✅ Pairwise analysis engine
- ✅ Link validator and confidence tiers

### Phase 1: Diagnostics (Next)
- [ ] Result validator (claim consistency checking)
- [ ] Gap analyzer
- [ ] Hypothesis generator
- [ ] Coverage analyzer

### Phase 2: Usability & Export
- [ ] CLI interface (14 commands)
- [ ] PyPI package + setup.py
- [ ] Interactive HTML visualization (force-directed graph of entities)
- [ ] Markdown report generator

### Phase 3: Examples & Documentation
- [ ] DS framework as flagship application (full walkthrough)
- [ ] Biology research example (5-entry minimal version)
- [ ] Materials science example (10-entry minimal version)
- [ ] Detailed API documentation

### Phase 4: Advanced Features
- [ ] Vector-boosting optimization (custom weights per taxonomy layer)
- [ ] Temporal analysis (snapshot history tracking like wiki_history.db)
- [ ] Multi-language support (non-English knowledge bases)
- [ ] Fine-tuning scripts (domain-specific embedding model training)

---

## Part 10: Governance & Release Strategy

### 10.1 Repository Structure

**Public repositories** (GitHub):

1. **`semantic-knowledge-graph-toolkit`** (main library)
   - Open-source (Apache 2.0 license)
   - Core ingestion, taxonomy, embedding, analysis
   - Examples and documentation
   - Monthly releases to PyPI

2. **`ds-wiki-transformation`** (flagship example)
   - Full DS framework implementation
   - Reference implementation for custom domains
   - Link to main toolkit docs
   - Shared with original DS 2.x creators for feedback loop

### 10.2 Adoption Path

**Target users**:
1. Academic researchers with structured knowledge bases (biology, materials, physics labs)
2. Industry R&D teams with documented findings/patents
3. Open-source projects wanting to index and discover connections in their codebase
4. Educational institutions building course knowledge graphs

**Value proposition**:
- Semantic discovery without pre-defined taxonomies (vectors do the work)
- Domain-agnostic scaffolding (your data, your taxonomy)
- Independent validation of claims/findings
- Novel hypothesis generation
- No API costs (local embeddings)

---

## Appendix A: Quick-Start Example (Biology)

**Given**: Lab with 50 experimental findings + 20 published papers, want to:
1. Ingested into unified KB
2. Find unexpected connections
3. Validate new findings against existing knowledge

**Steps**:

```bash
# 1. Define ingestion mapping
cat > ingestion.yaml <<EOF
input_format: csv
input_path: findings.csv
entity_mapping:
  entity_id_column: finding_id
  entity_type_column: category  # "exp_finding", "literature"
  entity_name_column: title
  description_column: abstract
section_mapping:
  - section_name: "Methods"
    column: methods
  - section_name: "Results"
    column: results
EOF

# 2. Define taxonomy
cat > taxonomy.yaml <<EOF
taxonomy_layers:
  experimental_design:
    type: controlled_vocabulary
    values: [RCT, cohort, case_study, in_vitro, animal_model]
  organism:
    type: controlled_vocabulary
    values: [human, mouse, rat, zebrafish, yeast, bacteria]
  biological_system:
    type: controlled_vocabulary
    values: [molecular, cellular, tissue, organ, organism]
EOF

# 3. Run toolkit
semantic-kg init --project my_lab
semantic-kg ingest --project my_lab --input-path findings.csv --config ingestion.yaml
semantic-kg taxonomy apply --project my_lab --taxonomy-path taxonomy.yaml
semantic-kg analyze --project my_lab --output-dir results/

# 4. Review results
open results/similar_pairs.csv
open results/hypothesis_prompts.md
```

**Output**: CSV with cross-domain connections (e.g., "Finding #23 (in-vitro protein) is 0.87 similar to Published Paper #18 (organism-level phenotype) — suggests mechanism link?").

---

## Appendix B: Technical Debt & Known Limitations

1. **Scaling**: Current architecture optimized for <10k entities. Larger KBs require:
   - Hierarchical clustering (subset pairwise analysis)
   - Approximate nearest neighbor (FAISS instead of full N×N)
   - Distributed embedding computation

2. **Language**: BGE models trained on English. Non-English KBs need custom models or translation.

3. **Causality**: Vector similarity ≠ causal relationship. Link validator must catch over-generalization.

4. **Cold start**: New KB with sparse taxonomy → low embedding quality initially. Recommend starting with >20% entity coverage on key properties.

5. **Taxonomy conflicts**: No built-in conflict detection if user defines contradictory relationships (e.g., A derives_from B and B derives_from A with no cycle). LinkValidator should warn.

---

## Appendix C: Success Metrics

For a deployed toolkit, measure:

1. **Adoption**:
   - PyPI downloads/month
   - GitHub stars
   - Publications citing the toolkit

2. **Discovery Quality**:
   - % of vectorially-discovered pairs (Tier 1.5) that become hand-validated links (Tier 2)
   - % of hypothesis prompts that lead to new experiments/papers
   - Gap analyzer recommendations that researchers act upon

3. **Performance**:
   - Time to ingest N entities (should scale linearly)
   - Vector search latency (<100ms for 1k entity KB)
   - Report generation time

4. **User Satisfaction**:
   - Ease of ingestion (measured by setup time, errors)
   - Utility of generated insights (user surveys)
   - Reduction in time to literature review / domain discovery

---

## Summary & Next Steps

**This specification enables**:
- Users to plug in arbitrary knowledge bases (CSV, JSON, custom domain formats)
- Automatic semantic enrichment via configurable taxonomies
- Discovery of surprising cross-domain connections
- Independent validation of research claims
- Hypothesis generation without domain pre-training

**Immediate next steps**:
1. Implement Phase 1 (Result Validator, Gap Analyzer, Hypothesis Generator, Coverage Analyzer)
2. Build CLI interface (14 commands)
3. Package as PyPI library (`semantic-knowledge-graph-toolkit`)
4. Create biology research + materials science examples
5. Publish to GitHub with DS framework as flagship demo

**Estimated scope**: 6-8 weeks for MVP (Phases 0-2), then ongoing maintenance + community contributions.

---

**Document Version**: 1.0
**Last Updated**: 2026-03-09
**Author**: Claude (AI Assistant)
**Status**: Ready for User Review & Feedback
