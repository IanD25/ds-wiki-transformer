# Fisher Diagnostic Suite — Implementation Specification
**Version:** 1.0 | **Date:** 2026-03-11 | **Status:** Approved for implementation
**Theoretical basis:** DS Wiki entries M6, T1, X0_FIM_Regimes (all pre-existing)
**Phase:** 1.5 (inserted between Phase 1 diagnostic tools and Phase 2 RRP completion)

---

## 0. Why This Exists Now

The DS Wiki already contains the full theoretical foundation for this suite:

| DS Wiki Entry | What It Is | Role in Implementation |
|---|---|---|
| **M6** — Fisher Information Rank | The measurement method (formula + validated results) | This spec implements M6 as executable code |
| **T1** — Fisher Rank Monotonicity | The theorem D_eff is non-increasing under coarse-graining | Unit test ground truth (T1 must hold on all test graphs) |
| **X0_FIM_Regimes** — Three Information-Geometric States | The regime classifier | Output vocabulary for all FIM results |
| **BIO3** — Fisher's Fundamental Theorem | Fisher's original information framework | Background context |

All 16 DS Wiki conjectures (P1–P16) link to X0_FIM_Regimes via `implements`. Running the Fisher Suite on the DS Wiki graph is therefore not external validation — it is **the DS Wiki testing its own claims**.

---

## 1. What the Suite Measures

Given a graph G = (V, E) with a distance metric and a center vertex v₀, the Fisher Diagnostic Suite computes:

1. **D_eff** — how many *independent* dimensions of information exist at v₀
2. **PR** (Participation Ratio) — continuous dimension estimate (non-integer sensitive)
3. **SV Profile** — normalized singular value spectrum (encodes degeneracy structure)
4. **η (Disorder Index)** — system-type classifier; separates structured from noise-dominated

It answers: **is this node in an ordered, critical, or noise-dominated information regime?**

### The Three Output Regimes (from X0_FIM_Regimes)

| Regime | SV Profile Signature | η | Physical Meaning | PFD Interpretation |
|--------|---------------------|---|------|---|
| **State 1 — Radial-Dominated** | [1, a, a, ..., small]; a ≪ 1 | ~0.23 | Exponential correlations, short-range order | Entry is a focused hub — one dominant connection direction |
| **State 2 — Isotropic** | [1, ≈1, ≈1, ..., small residuals] | ~0.5 | Power-law/system-spanning correlations | Entry is a cross-domain bridge — multiple independent pathways |
| **State 3 — Noise-Dominated** | [1, ~0.5, ~0.5, ..., ~0.2]; all comparable | ~0.93 | Flat/saturated correlations | Entry's connections are statistically random — high noise, low logical structure |

---

## 2. Mathematical Pipeline (Exact Specification)

### Step 1 — Graph and Distance Matrix

```
Input:  G = (V, E), center vertex v₀
        Edge weights w(e) ∈ {1.0, 1.5, 2.0, 3.0} based on confidence_tier
        (tier-1 → 1.0, tier-1.5 → 1.5, tier-2 → 2.0, null-tier → 3.0)

Compute: d(v₀, u) for all u ∈ V via Dijkstra's (weighted) or BFS (unweighted)
         d(wⱼ, u) for all neighbors wⱼ of v₀, for all u ∈ V

Note: If u is unreachable from v₀, d(v₀, u) = ∞ and f(∞) = 0 by definition.
```

### Step 2 — Kernel Functions

Three kernel types are supported. Kernel choice determines what "distance" means:

```
EXPONENTIAL kernel (structural analysis):
    f(d) = exp(-α * d)        α ∈ (0, ∞), default α = 1.0
    Use: measuring structural dimension of knowledge graph

CORRELATION kernel (semantic analysis):
    f(u) = max(0, cosine_sim(emb_v₀, emb_u))
    Use: measuring semantic geometry; bridge quality scoring
    Requires: embedding vectors for all vertices

WEIGHTED_HOP kernel (hybrid):
    f(d, u) = max(0, cosine_sim(emb_v₀, emb_u)) * exp(-α * d_hop(v₀, u))
    Use: combines structural position with semantic similarity
```

### Step 3 — Position-Indexed Distributions

For center v₀ and each neighbor wⱼ (j = 1..k, where k = degree(v₀)):

```
pᵥ₀(u)   = f(d(v₀, u)) / Σᵤ f(d(v₀, u))       # distribution over V from center
p_wⱼ(u)  = f(d(wⱼ, u)) / Σᵤ f(d(wⱼ, u))       # distribution over V from neighbor j

Numerical guard: if Σᵤ f(...) < ε (= 1e-10), return degenerate result (skip node)
```

### Step 4 — Score Vectors

For each neighbor wⱼ, compute the log-likelihood ratio against the center:

```
sⱼ(u) = log(p_wⱼ(u)) - log(pᵥ₀(u))    for all u ∈ V

Special cases:
    If pᵥ₀(u) = 0 AND p_wⱼ(u) = 0:  sⱼ(u) = 0  (both unreachable — no information)
    If pᵥ₀(u) = 0 AND p_wⱼ(u) > 0:  sⱼ(u) = +MAX_SCORE (= 20.0)  (neighbor visible, center not)
    If pᵥ₀(u) > 0 AND p_wⱼ(u) = 0:  sⱼ(u) = -MAX_SCORE          (center visible, neighbor not)
```

### Step 5 — Fisher Information Matrix

Build the k × k FIM (where k = degree(v₀)):

```
F[i,j] = Σᵤ sᵢ(u) * sⱼ(u) * pᵥ₀(u)

Result: real symmetric k×k matrix
Minimum valid degree: k ≥ 2 (k=1 returns degenerate single-entry result)
```

### Step 6 — SVD Extraction

```python
σ = np.linalg.svd(F, compute_uv=False)   # returns σ in descending order
σ = σ[σ > ε]                              # drop near-zero singular values

# D_eff: position of largest gap in singular value spectrum
ratios = σ[:-1] / σ[1:]                   # σᵢ/σᵢ₊₁ for i=0..n-2
d_eff  = int(np.argmax(ratios)) + 1       # 1-indexed

# Participation Ratio (continuous dimension):
pr = (np.sum(σ))**2 / np.sum(σ**2)

# SV Profile (normalized):
sv_profile = σ / σ[0]                    # range [0, 1], first entry always 1.0

# Disorder Index:
if d_eff < len(σ):
    eta = σ[d_eff] / σ[d_eff - 1]        # ratio right after the gap
else:
    eta = 0.0                             # gap is at end — perfectly ordered
```

### Step 7 — Regime Classification

```
Using X0_FIM_Regimes vocabulary:

if η < 0.35:                → RADIAL_DOMINATED   (State 1)
elif η < 0.65:              → ISOTROPIC           (State 2)
else:                       → NOISE_DOMINATED     (State 3)

Note: Transition zone thresholds 0.35 and 0.65 are working defaults.
      Calibrate against DS Wiki ground-truth nodes after first sweep.
```

---

## 3. File Structure (New Files)

```
src/
├── analysis/
│   ├── fisher_diagnostics.py       ← PRIMARY MODULE (new)
│   └── fisher_bridge_filter.py     ← Bridge quality scorer (new)
scripts/
├── run_fisher_suite.py             ← CLI (new)
tests/
├── test_fisher_diagnostics.py      ← Test suite (new)
```

**Modified files:**
```
src/mcp_server.py                   ← Add 3 new MCP tools
src/ingestion/cross_universe_query.py ← Add optional eta filtering
data/wiki_history.db (schema only)  ← Add fisher_metrics table (auto-created)
CLAUDE.md                           ← Update phase status
```

---

## 4. Core Module: `src/analysis/fisher_diagnostics.py`

### 4.1 Imports and Dependencies

```python
# Standard library only (+ numpy) — no new dependencies
import sqlite3
import json
import logging
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Optional
import numpy as np
import networkx as nx

from src.config import SOURCE_DB, HISTORY_DB
```

### 4.2 Enumerations

```python
class KernelType(str, Enum):
    EXPONENTIAL  = "exponential"   # f(d) = exp(-alpha * d)
    CORRELATION  = "correlation"   # f(u) = cosine_sim(emb_v0, emb_u)
    WEIGHTED_HOP = "weighted_hop"  # product of both

class RegimeType(str, Enum):
    RADIAL_DOMINATED = "radial_dominated"   # State 1: η < 0.35
    ISOTROPIC        = "isotropic"          # State 2: 0.35 ≤ η < 0.65
    NOISE_DOMINATED  = "noise_dominated"    # State 3: η ≥ 0.65
    DEGENERATE       = "degenerate"         # degree < 2, cannot compute FIM
```

### 4.3 Data Structures

```python
@dataclass
class FisherResult:
    node_id:       str
    kernel_type:   KernelType
    alpha:         float           # exponential decay parameter (ignored for CORRELATION)
    center_degree: int             # k = degree(v₀)
    d_eff:         int             # gap-based effective dimension
    pr:            float           # participation ratio (continuous dimension)
    eta:           float           # disorder index (regime classifier)
    regime:        RegimeType      # one of the three X0 states
    sv_profile:    list[float]     # normalized singular values [1.0, ...]
    raw_sigmas:    list[float]     # unnormalized singular values
    n_vertices:    int             # |V| at time of computation
    skipped:       bool = False    # True if degree < 2 or degenerate FIM
    skip_reason:   str = ""

    def as_dict(self) -> dict:
        d = asdict(self)
        d["kernel_type"] = self.kernel_type.value
        d["regime"] = self.regime.value
        return d

@dataclass
class FisherSweepResult:
    graph_source:  str             # 'ds_wiki' or path to RRP bundle
    kernel_type:   KernelType
    alpha:         float
    n_analyzed:    int             # nodes where FIM ran successfully
    n_skipped:     int             # degree < 2 nodes
    results:       dict[str, FisherResult] = field(default_factory=dict)

    # Aggregate statistics
    mean_d_eff:    float = 0.0
    median_eta:    float = 0.0
    regime_counts: dict[str, int] = field(default_factory=dict)

    def top_hubs(self, n: int = 10) -> list[FisherResult]:
        """Return top n entries by d_eff, then by PR for ties."""
        valid = [r for r in self.results.values() if not r.skipped]
        return sorted(valid, key=lambda r: (r.d_eff, r.pr), reverse=True)[:n]

    def ordered_nodes(self) -> list[FisherResult]:
        """All non-skipped results sorted by d_eff desc, eta asc."""
        valid = [r for r in self.results.values() if not r.skipped]
        return sorted(valid, key=lambda r: (r.d_eff, -r.eta), reverse=True)
```

### 4.4 Graph Construction Helpers

```python
def build_wiki_graph(db_path: Path) -> tuple[nx.Graph, dict[str, str]]:
    """
    Build a NetworkX graph from a DS Wiki or RRP bundle SQLite database.

    Returns:
        G      — undirected graph; nodes = entry IDs; edges = links
        labels — {entry_id: title}

    Edge weight encoding (for Dijkstra distance):
        confidence_tier '1'   → weight = 1.0
        confidence_tier '1.5' → weight = 1.5
        confidence_tier '2'   → weight = 2.0
        confidence_tier None  → weight = 3.0   (original/unclassified)

    Note: DS Wiki uses 'links' table (source_id/target_id/confidence_tier).
          RRP bundles use the same schema (mirrored from DS Wiki).
    """

def build_distance_matrix(G: nx.Graph, source: str) -> dict[str, float]:
    """
    Dijkstra shortest path from source to all reachable nodes.
    Returns {node_id: distance}. Unreachable nodes are absent.
    Uses edge 'weight' attribute if present; falls back to hop count.
    """
```

### 4.5 Kernel Functions

```python
def exponential_kernel(distances: dict[str, float], alpha: float = 1.0) -> dict[str, float]:
    """f(d) = exp(-alpha * d). Returns {node_id: kernel_value}."""

def correlation_kernel(
    center_emb: np.ndarray,
    all_embeddings: dict[str, np.ndarray]
) -> dict[str, float]:
    """
    f(u) = max(0, cosine_sim(center_emb, emb_u)).
    Returns {node_id: kernel_value}.
    Requires embedding vectors for all nodes.
    """

def weighted_hop_kernel(
    distances: dict[str, float],
    center_emb: np.ndarray,
    all_embeddings: dict[str, np.ndarray],
    alpha: float = 1.0
) -> dict[str, float]:
    """
    f(d, u) = max(0, cosine_sim) * exp(-alpha * d).
    Product of structural and semantic kernels.
    """
```

### 4.6 FIM Construction

```python
def build_distribution(kernel_values: dict[str, float], vertex_ids: list[str]) -> np.ndarray:
    """
    p(u) = kernel_value(u) / sum_u kernel_value(u)
    Returns numpy array of length |V|, indexed by vertex_ids ordering.
    Handles zero denominator by returning uniform distribution (degenerate case).
    """

def build_score_vectors(
    neighbor_dists: list[dict[str, float]],
    center_dist:    dict[str, float],
    vertex_ids:     list[str]
) -> np.ndarray:
    """
    Compute k × |V| score matrix S where S[j, u] = log(p_wj(u)) - log(p_v0(u)).

    Special cases handled per Step 4 of the mathematical pipeline.
    MAX_SCORE = 20.0 (capped log-ratio for 0/non-0 crossings).
    Returns numpy array shape (k, |V|).
    """

def build_fim(
    score_matrix: np.ndarray,
    center_distribution: np.ndarray
) -> np.ndarray:
    """
    F[i,j] = sum_u S[i,u] * S[j,u] * p_v0(u)

    Vectorized: F = S @ diag(p_v0) @ S.T
    Returns k × k symmetric real matrix.
    """
```

### 4.7 SVD Extraction

```python
def decompose_fim(F: np.ndarray, eps: float = 1e-10) -> tuple[int, float, list[float], float]:
    """
    Compute the four FIM diagnostics from the SVD of F.

    Returns: (d_eff, pr, sv_profile, eta)

    Algorithm:
        σ = np.linalg.svd(F, compute_uv=False)
        Trim near-zero singular values (< eps * σ[0])
        d_eff:      argmax(σᵢ/σᵢ₊₁) + 1 — position of largest gap
        pr:         (Σσ)² / Σσ² — continuous participation ratio
        sv_profile: σ / σ[0] — normalized, first value = 1.0
        eta:        σ[d_eff] / σ[d_eff-1] if d_eff < len(σ) else 0.0
    """

def classify_regime(eta: float) -> RegimeType:
    """
    Map disorder index η to X0 FIM regime.
    Thresholds: RADIAL < 0.35 ≤ ISOTROPIC < 0.65 ≤ NOISE_DOMINATED.
    """
```

### 4.8 Primary Entry Points

```python
def analyze_node(
    G:           nx.Graph,
    node_id:     str,
    kernel_type: KernelType = KernelType.EXPONENTIAL,
    alpha:       float = 1.0,
    embeddings:  Optional[dict[str, np.ndarray]] = None
) -> FisherResult:
    """
    Full FIM pipeline for a single center node.

    Preconditions:
        - node_id must be in G.nodes
        - degree(node_id) ≥ 2 (else returns FisherResult with skipped=True)
        - If kernel_type in {CORRELATION, WEIGHTED_HOP}: embeddings must not be None

    Steps:
        1. Get neighbors of node_id
        2. Compute distance matrices (center → all, each neighbor → all)
        3. Apply kernel to each distance set
        4. Build distributions
        5. Build score matrix
        6. Build FIM
        7. SVD decomposition
        8. Regime classification
        9. Return FisherResult
    """

def sweep_graph(
    G:            nx.Graph,
    graph_source: str,
    kernel_type:  KernelType = KernelType.EXPONENTIAL,
    alpha:        float = 1.0,
    embeddings:   Optional[dict[str, np.ndarray]] = None,
    min_degree:   int = 2
) -> FisherSweepResult:
    """
    Run analyze_node for every node in G with degree ≥ min_degree.
    Collect into FisherSweepResult with aggregate statistics.

    Performance note:
        DS Wiki (209 nodes): < 1s on M4 CPU
        Periodic table bundle (167 nodes): < 1s
        Large corpus (10,000 nodes): ~60s on CPU (acceptable for batch use)
    """

def load_embeddings_from_chroma(
    collection_name: str,
    chroma_dir:      Path
) -> dict[str, np.ndarray]:
    """
    Load all embedding vectors from ChromaDB for correlation kernel use.
    Returns {entry_id: np.ndarray(768,)} for bge-base embeddings.
    Note: chunk embeddings are aggregated to entry level by mean pooling.
    """
```

---

## 5. Bridge Quality Scorer: `src/analysis/fisher_bridge_filter.py`

This module integrates FIM geometry with the existing cross-universe bridge pipeline.

```python
@dataclass
class BridgeQualityScore:
    rrp_entry_id:    str
    ds_entry_id:     str
    cosine_sim:      float          # existing similarity score
    eta:             float          # disorder index at DS Wiki node
    regime:          RegimeType     # X0 regime of DS Wiki node at this bridge
    trust_score:     float          # composite: (1 - eta) * cosine_sim
    is_structured:   bool           # eta < ETA_TRUST_THRESHOLD (default 0.65)

ETA_TRUST_THRESHOLD = 0.65          # noise-dominated bridges are unreliable

def score_bridge(
    rrp_entry_id: str,
    ds_entry_id:  str,
    cosine_sim:   float,
    ds_sweep:     FisherSweepResult
) -> BridgeQualityScore:
    """
    Look up the DS Wiki node's FisherResult from a pre-computed sweep.
    Compute trust_score = (1 - eta) * cosine_sim.
    """

def filter_bridges(
    bridges:       list[dict],        # rows from cross_universe_bridges table
    ds_sweep:      FisherSweepResult,
    eta_threshold: float = ETA_TRUST_THRESHOLD
) -> tuple[list[dict], list[dict]]:
    """
    Split bridge list into (structured, noise) based on DS Wiki node's eta.
    Returns (trusted_bridges, noise_bridges).

    Usage in cross_universe_query.py:
        trusted, noise = filter_bridges(bridges, ds_sweep)
        # Promote trusted bridges; flag noise bridges for human review
    """
```

---

## 6. DB Schema Addition (wiki_history.db)

New table added by `ensure_fisher_table()` in fisher_diagnostics.py (auto-created on first use):

```sql
CREATE TABLE IF NOT EXISTS fisher_metrics (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id       TEXT,              -- optional: link to wiki_snapshots
    entry_id          TEXT NOT NULL,
    graph_source      TEXT NOT NULL,     -- 'ds_wiki' or absolute path to RRP bundle
    kernel_type       TEXT NOT NULL,     -- 'exponential' | 'correlation' | 'weighted_hop'
    alpha             REAL,              -- exponential decay parameter (NULL for correlation)
    d_eff             INTEGER,
    participation_ratio REAL,
    disorder_index    REAL,
    regime            TEXT,              -- 'radial_dominated' | 'isotropic' | 'noise_dominated' | 'degenerate'
    sv_profile_json   TEXT,              -- JSON array of normalized singular values
    raw_sigmas_json   TEXT,              -- JSON array of raw singular values
    center_degree     INTEGER,
    n_vertices        INTEGER,
    skipped           INTEGER DEFAULT 0, -- 0=computed, 1=skipped (degree<2)
    skip_reason       TEXT,
    computed_at       TEXT DEFAULT (datetime('now')),
    UNIQUE(entry_id, graph_source, kernel_type, alpha)
);

CREATE INDEX IF NOT EXISTS idx_fisher_entry ON fisher_metrics(entry_id);
CREATE INDEX IF NOT EXISTS idx_fisher_regime ON fisher_metrics(regime);
CREATE INDEX IF NOT EXISTS idx_fisher_d_eff  ON fisher_metrics(d_eff DESC);
```

**Access pattern for conjecture validation:**
```sql
-- Find all entries in isotropic regime (cross-domain hubs — P4/P15 territory)
SELECT entry_id, d_eff, disorder_index, regime
FROM fisher_metrics
WHERE graph_source = 'ds_wiki'
  AND kernel_type = 'exponential'
  AND regime = 'isotropic'
ORDER BY d_eff DESC;
```

---

## 7. Integration Points

### 7.1 cross_universe_query.py

Add optional `quality_filter` parameter to `CrossUniverseQuery.run()`:

```python
def run(
    self,
    bundle_db:      Path,
    chroma_dir:     Path,
    ds_wiki_db:     Path,
    quality_filter: bool = False,   # NEW: apply FIM bridge quality filter
    eta_threshold:  float = 0.65    # NEW: disorder index cutoff
) -> list[Bridge]:
    ...
    if quality_filter:
        ds_sweep = sweep_graph(G_wiki, 'ds_wiki', KernelType.EXPONENTIAL)
        trusted, noise = filter_bridges(raw_bridges, ds_sweep, eta_threshold)
        # Store noise bridges separately; promote trusted to tier-1.5 candidates
        ...
```

### 7.2 gap_analyzer.py

Add `FisherDimensionGap` to the gap types (low d_eff = isolated entry):

```python
@dataclass
class FisherDimensionGap:
    entry_id:    str
    d_eff:       int         # effective dimension (low d_eff = structurally weak)
    regime:      RegimeType
    suggestion:  str         # e.g. "Add 2+ tier-1 links from different domains"

# In GapAnalyzer.analyze():
# Load latest fisher_metrics from wiki_history.db
# Flag entries with d_eff == 1 AND regime == RADIAL_DOMINATED as structural gaps
# Add to EnrichmentPriority list with priority = HIGH if d_eff == 1
```

### 7.3 mcp_server.py

Add three new MCP tools:

```python
@mcp.tool()
def fisher_analyze_node(
    entry_id:    str,
    kernel:      str = "exponential",   # "exponential" | "correlation" | "weighted_hop"
    alpha:       float = 1.0
) -> dict:
    """
    Compute Fisher Information Matrix diagnostics for a single DS Wiki entry.
    Returns d_eff, PR, eta, regime, and sv_profile.
    Uses pre-computed FIM sweep if available in wiki_history.db (< 5ms).
    Falls back to live computation if not cached (~100ms on M4).
    """

@mcp.tool()
def fisher_sweep_wiki(
    kernel:      str = "exponential",
    top_n:       int = 20,
    min_degree:  int = 2
) -> dict:
    """
    Run FIM analysis across all DS Wiki entries.
    Returns top_n hubs by d_eff, aggregate statistics, and regime distribution.
    Caches results to wiki_history.db for subsequent calls.
    Expected runtime: < 5s on M4 CPU.
    """

@mcp.tool()
def fisher_classify_bridges(
    rrp_db_path:   str,
    eta_threshold: float = 0.65
) -> dict:
    """
    Apply FIM geometry filter to cross-universe bridges in an RRP bundle.
    Returns bridges split into 'structured' and 'noise' categories.
    Structured bridges (eta < threshold) are promoted for validation.
    """
```

---

## 8. CLI Script: `scripts/run_fisher_suite.py`

```
Usage:
    python scripts/run_fisher_suite.py [OPTIONS]

Options:
    --mode        {ds_wiki | rrp_bundle | bridges}   [required]
    --rrp         PATH     Path to RRP bundle .db        [required if mode=rrp_bundle|bridges]
    --kernel      {exponential | correlation}            [default: exponential]
    --alpha       FLOAT    Exponential decay parameter   [default: 1.0]
    --top-n       INT      Show top N hubs by d_eff      [default: 20]
    --entry       ENTRY_ID Analyze single entry          [optional]
    --save        BOOL     Save results to wiki_history.db [default: True]
    --filter-bridges BOOL  Apply FIM filter to bridges   [default: False]

Examples:
    # Full DS Wiki sweep, show top 20 dimensional hubs
    python scripts/run_fisher_suite.py --mode ds_wiki --top-n 20

    # Single entry deep analysis
    python scripts/run_fisher_suite.py --mode ds_wiki --entry B5

    # RRP bundle analysis
    python scripts/run_fisher_suite.py --mode rrp_bundle \
        --rrp data/rrp/periodic_table/rrp_periodic_table.db

    # Bridge quality filter
    python scripts/run_fisher_suite.py --mode bridges \
        --rrp data/rrp/periodic_table/rrp_periodic_table.db \
        --filter-bridges true

Expected output (DS Wiki sweep, top 10):
    ╔══════════════════════════════════════════════════════════════════╗
    ║ Fisher Diagnostic Suite — DS Wiki (exponential kernel, α=1.0)   ║
    ╠══════════════════════╦════════╦═════╦═══════╦════════════════════╣
    ║ Entry ID             ║ D_eff  ║ PR  ║  η    ║ Regime             ║
    ╠══════════════════════╬════════╬═════╬═══════╬════════════════════╣
    ║ TD3 (Second Law)     ║   5    ║4.7  ║ 0.41  ║ isotropic          ║
    ║ B5  (Landauer)       ║   5    ║4.3  ║ 0.38  ║ isotropic          ║
    ║ C1  (Kleiber's Law)  ║   6    ║5.1  ║ 0.29  ║ radial_dominated   ║
    ║ ...                  ║        ║     ║       ║                    ║
    ╚══════════════════════╩════════╩═════╩═══════╩════════════════════╝

    Regime distribution: 47 radial | 38 isotropic | 24 noise | 22 skipped (deg<2)
```

---

## 9. Test Suite: `tests/test_fisher_diagnostics.py`

### 9.1 Known-Graph Benchmarks (Ground Truth from M6/T1 DS Wiki entries)

These are the authoritative validation cases. All must pass before integration tests run.

```python
class TestKnownGraphs:
    """
    Ground truth from M6 Phase 1 validation (Darling, 2026):
    'Gap-based rank returns exact integer dimension at every sample vertex
     with zero variance on flat tori.'
    """

    def test_path_graph_d1(self):
        """P_10 (path of 10 nodes): d_eff = 1 at all interior nodes."""
        G = nx.path_graph(10)
        for node in range(1, 9):  # interior nodes (degree 2)
            result = analyze_node(G, str(node), KernelType.EXPONENTIAL)
            assert result.d_eff == 1, f"Path graph: expected d_eff=1, got {result.d_eff}"
            assert result.eta < 0.35, f"Path graph: expected radial regime"

    def test_grid_graph_d2(self):
        """5×5 grid graph: d_eff = 2 at interior nodes."""
        G = nx.grid_2d_graph(5, 5)
        G = nx.convert_node_labels_to_integers(G)
        interior_nodes = [n for n in G.nodes if G.degree(n) == 4]
        for node in interior_nodes[:5]:
            result = analyze_node(G, str(node), KernelType.EXPONENTIAL)
            assert result.d_eff == 2, f"Grid graph: expected d_eff=2, got {result.d_eff}"

    def test_torus_graph_eta_023(self):
        """
        Torus graph: η ≈ 0.23 (State 1 — Radial-Dominated).
        From M6: 'torus ~0.23' in disorder index reference values.
        Tolerance: ±0.10
        """
        G = nx.circulant_graph(16, [1, 4])  # approximates torus topology
        result = analyze_node(G, "0", KernelType.EXPONENTIAL)
        assert result.regime == RegimeType.RADIAL_DOMINATED
        assert 0.13 < result.eta < 0.43, f"Torus: expected η≈0.23, got {result.eta:.3f}"

    def test_er_graph_eta_093(self):
        """
        Erdős–Rényi random graph: η ≈ 0.93 (State 3 — Noise-Dominated).
        From M6: 'ER ~0.93' in disorder index reference values.
        Tolerance: ±0.15. Uses fixed seed for reproducibility.
        """
        rng = np.random.default_rng(42)
        G = nx.erdos_renyi_graph(50, 0.3, seed=42)
        high_degree_nodes = [n for n in G.nodes if G.degree(n) >= 5]
        etas = []
        for node in high_degree_nodes[:10]:
            result = analyze_node(G, str(node), KernelType.EXPONENTIAL)
            if not result.skipped:
                etas.append(result.eta)
        mean_eta = np.mean(etas)
        assert mean_eta > 0.65, f"ER graph: expected mean η>0.65 (noise regime), got {mean_eta:.3f}"

    def test_complete_graph_isotropic(self):
        """
        K_8 (complete graph): all directions equal → isotropic / high D_eff.
        """
        G = nx.complete_graph(8)
        result = analyze_node(G, "0", KernelType.EXPONENTIAL)
        assert result.pr > 3.0, f"Complete graph: expected PR>3, got {result.pr:.2f}"

    def test_t1_monotonicity(self):
        """
        T1 Fisher Rank Monotonicity: coarse-graining cannot increase D_eff.
        Build a 6×6 grid, then 3×3 grid (coarsened version).
        D_eff(coarse) <= D_eff(fine) must hold.
        """
        G_fine   = nx.grid_2d_graph(6, 6)
        G_coarse = nx.grid_2d_graph(3, 3)
        G_fine   = nx.convert_node_labels_to_integers(G_fine)
        G_coarse = nx.convert_node_labels_to_integers(G_coarse)

        fine_center   = [n for n in G_fine.nodes   if G_fine.degree(n) == 4][0]
        coarse_center = [n for n in G_coarse.nodes if G_coarse.degree(n) == 4][0]

        r_fine   = analyze_node(G_fine,   str(fine_center),   KernelType.EXPONENTIAL)
        r_coarse = analyze_node(G_coarse, str(coarse_center), KernelType.EXPONENTIAL)

        assert r_coarse.d_eff <= r_fine.d_eff, (
            f"T1 violated: D_eff increased under coarse-graining "
            f"({r_fine.d_eff} → {r_coarse.d_eff})"
        )
```

### 9.2 Unit Tests

```python
class TestFIMConstruction:
    def test_distributions_sum_to_one(self)
    def test_fim_is_symmetric(self)
    def test_score_zero_for_identical_distributions(self)
    def test_degenerate_node_degree1_skipped(self)
    def test_degenerate_node_degree0_skipped(self)
    def test_disconnected_component_handled(self)
    def test_fim_with_uniform_kernel_isotropic(self)
    def test_sv_profile_first_element_is_1(self)
    def test_eta_in_range_0_1(self)
    def test_pr_at_least_1(self)

class TestKernels:
    def test_exponential_kernel_decays_monotonically(self)
    def test_exponential_kernel_sum_normalizes(self)
    def test_correlation_kernel_nonnegative(self)
    def test_correlation_kernel_max_1(self)
    def test_weighted_hop_bounded_by_correlation(self)

class TestRegimeClassification:
    def test_eta_below_035_is_radial(self)
    def test_eta_035_to_065_is_isotropic(self)
    def test_eta_above_065_is_noise(self)
    def test_degenerate_result_returns_degenerate_regime(self)
```

### 9.3 Integration Tests

```python
class TestDSWikiIntegration:
    """Use real ds_wiki.db — requires data/ds_wiki.db to exist."""

    def test_sweep_runs_without_error(self):
        """Full sweep of DS Wiki with exponential kernel completes."""

    def test_b5_landauer_is_isotropic_or_radial(self):
        """B5 (degree=16) must be in radial_dominated or isotropic regime."""
        result = analyze_node(G_wiki, "B5", KernelType.EXPONENTIAL)
        assert result.regime in (RegimeType.RADIAL_DOMINATED, RegimeType.ISOTROPIC)
        assert result.d_eff >= 2

    def test_x0_fim_regimes_high_degree(self):
        """X0_FIM_Regimes (degree=16, all conjecture links) should be high D_eff."""
        result = analyze_node(G_wiki, "X0_FIM_Regimes", KernelType.EXPONENTIAL)
        assert not result.skipped
        assert result.d_eff >= 2

    def test_degree1_nodes_skipped(self):
        """Known degree-1 nodes (CM6, EM10, etc.) must return skipped=True."""
        for node_id in ["CM6", "EM10", "ES1"]:
            result = analyze_node(G_wiki, node_id, KernelType.EXPONENTIAL)
            assert result.skipped, f"Expected {node_id} to be skipped (degree=1)"

    def test_results_persist_to_db(self):
        """sweep_graph with save=True must write rows to wiki_history.db."""

class TestBridgeFilter:
    """Use real periodic table RRP bundle."""

    def test_filter_reduces_bridge_count(self):
        """ETA filtering must remove at least some bridges."""

    def test_structured_bridges_below_eta_threshold(self):
        """All 'trusted' bridges must have eta < ETA_TRUST_THRESHOLD."""

    def test_noise_bridges_not_deleted(self):
        """Noise bridges are retained in a separate list, not discarded."""
```

---

## 10. Validation Protocol

### Before Implementation Merge

Run this validation sequence to confirm the implementation matches M6/T1 ground truth:

```bash
python scripts/run_fisher_suite.py --mode ds_wiki --top-n 30

# Expected checkpoints:
# 1. TD3 (Second Law, degree=19)    → d_eff ≥ 3, regime = isotropic or radial
# 2. B5  (Landauer, degree=16)      → d_eff ≥ 3, regime = isotropic
# 3. X0_FIM_Regimes (degree=16)     → d_eff ≥ 3 (the FIM spec itself is a hub)
# 4. ~22 degree-1 nodes             → all skipped
# 5. Mean D_eff across all:         → 2.5–4.5 (reasonable for this graph density)
# 6. Regime distribution            → majority radial or isotropic (DS Wiki is structured)
```

### Periodic Table Bridge Filter Validation

```bash
python scripts/run_fisher_suite.py --mode bridges \
    --rrp data/rrp/periodic_table/rrp_periodic_table.db \
    --filter-bridges true

# Expected:
# 500 total bridges → X structured (trusted), Y noise
# X should be in the range 60–80% of 500 (high-quality corpus)
# The 40 existing tier-1.5 bridges should overwhelmingly land in 'structured'
```

---

## 11. Implementation Checklist (Ordered)

```
Phase A — Core module (no integration yet)
[ ] A1. Create src/analysis/fisher_diagnostics.py
        - KernelType, RegimeType enums
        - FisherResult, FisherSweepResult dataclasses
        - build_wiki_graph(), build_distance_matrix()
        - All three kernel functions
        - build_distribution(), build_score_vectors(), build_fim()
        - decompose_fim(), classify_regime()
        - analyze_node(), sweep_graph()
        - ensure_fisher_table(), save_sweep_to_db()
        - load_embeddings_from_chroma() (stub OK for Phase A)

[ ] A2. Create tests/test_fisher_diagnostics.py
        - All TestKnownGraphs (path, grid, torus, ER, K8, T1 monotonicity)
        - All TestFIMConstruction unit tests
        - All TestKernels unit tests
        - All TestRegimeClassification unit tests
        - Run: pytest tests/test_fisher_diagnostics.py -v
        - STOP: all must pass before Phase B

Phase B — CLI and DS Wiki integration
[ ] B1. Create scripts/run_fisher_suite.py
[ ] B2. Run full DS Wiki sweep, verify checkpoints in Section 10
[ ] B3. Add DS Wiki integration tests to test suite
[ ] B4. Run: pytest tests/test_fisher_diagnostics.py -v (all tests pass)

Phase C — Bridge filter integration
[ ] C1. Create src/analysis/fisher_bridge_filter.py
[ ] C2. Run periodic table bridge filter, verify checkpoints in Section 10
[ ] C3. Add integration tests for bridge filter
[ ] C4. Add optional quality_filter parameter to CrossUniverseQuery.run()

Phase D — MCP and persistence
[ ] D1. Add ensure_fisher_table() call to mcp_server.py startup
[ ] D2. Add fisher_analyze_node MCP tool
[ ] D3. Add fisher_sweep_wiki MCP tool
[ ] D4. Add fisher_classify_bridges MCP tool

Phase E — Gap analyzer integration
[ ] E1. Load FisherDimensionGap from wiki_history.db in GapAnalyzer.analyze()
[ ] E2. Add FisherDimensionGap to EnrichmentPriority ranking
[ ] E3. Add to gap_analyzer tests

Phase F — Commit and update project files
[ ] F1. Update CLAUDE.md Phase Status table (add FIM Suite entry)
[ ] F2. Commit: "[Phase 1.5] Add Fisher Diagnostic Suite"
[ ] F3. Push to origin/main
```

---

## 12. Key Architectural Decisions Recorded

| Decision | Choice | Rationale |
|---|---|---|
| Graph distance metric | Dijkstra with tier-based weights | Tier-1 links are structurally "closer" than null-tier links |
| Default kernel | EXPONENTIAL | Returns exact integers on manifolds (M6 validation); no embedding dependency |
| Minimum degree for FIM | 2 | 1-neighbor FIM is trivially rank-1 and uninformative |
| Noise bridge threshold η | 0.65 | Upper boundary of isotropic state from X0_FIM_Regimes |
| Storage location | wiki_history.db (not ds_wiki.db) | Constraint: ds_wiki.db is read-only source of truth |
| numpy SVD | np.linalg.svd(compute_uv=False) | scipy not installed; numpy SVD sufficient for k≤25 matrices |
| Degree-1 nodes | Skipped (not error) | 22 known degree-1 entries; skipping is correct, not a failure |
| MAX_SCORE cap | 20.0 | Prevents numerical explosion on 0/non-0 distribution crossings |

---

*This spec implements DS Wiki entries M6 (Fisher Information Rank) and T1 (Fisher Rank Monotonicity) as executable software. The output vocabulary is defined by X0_FIM_Regimes. All 16 DS Wiki conjectures (P1–P16) claim to implement X0_FIM_Regimes — running this suite on the DS Wiki graph is the system testing its own theoretical claims.*
