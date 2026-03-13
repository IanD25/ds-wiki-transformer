# PFD Visualization Suite — Proposal & Architecture

**Problem:** Users run Fisher diagnostics and get JSON reports. No visual representation of topology, coherence, analogies, or data quality.

**Solution:** Build a comprehensive visualization module that generates static + interactive visuals automatically.

---

## Visualization Categories

### Category A: Static Report Visualizations (PNG/SVG for embedding in documents)

#### 1. **Internal Coherence Dashboard**
- **What it shows:** Tier-1 internal structure health
- **Visualizations:**
  - Pie chart: Noise vs. Signal fraction (color-coded)
  - D_eff gauge: Effective dimensionality on a scale (1→planar, 5→modular, 10+→distributed)
  - Regime distribution bar chart: % Radial-Dominated vs. Isotropic vs. Noise-Dominated vs. Degenerate
  - Histogram: Link degree distribution (how many links per entry)
- **Output:** Single-page PNG suitable for including in research reports
- **Library:** Matplotlib + seaborn

#### 2. **Bridge Quality Network Diagram**
- **What it shows:** Tier-2 cross-RRP analogies
- **Visualization:**
  - Node-link diagram: Dataset A entries (left) connected to Dataset B entries (right)
  - Node size: Proportional to # of bridges
  - Edge width: Proportional to similarity score
  - Edge color: Gradient from weak (gray) to strong (green)
  - Top N bridges highlighted (e.g., top 10 by similarity)
- **Output:** Static SVG/PNG, publication-quality
- **Library:** NetworkX + Matplotlib or Graphviz

#### 3. **PFD Score Breakdown**
- **What it shows:** How Tier-1 + Tier-2 combine into final score
- **Visualization:**
  - Stacked horizontal bar:
    - Left half = Tier-1 contribution (0.0–1.0)
    - Right half = Tier-2 contribution (0.0–1.0)
    - Combined = PFD Score (centered, larger font)
  - Color gradient: Red (poor) → Green (excellent)
  - Annotations: Actual score values on each segment
- **Output:** Single graphic, suitable for presentations/papers

#### 4. **Entry Connectivity Heatmap**
- **What it shows:** Which entries are well-connected vs. isolated
- **Visualization:**
  - Matrix heatmap: Rows = entries, columns = entry degree (# links)
  - Color intensity: Bright (many links) → Dark (few/no links)
  - Red boxes highlight isolated entries (0 links)
  - Rows sorted by degree (most connected at top)
  - Annotations: Optional entry IDs and link counts
- **Output:** Scalable to dataset size, publication-ready

#### 5. **Regime Distribution Pie Charts**
- **What it shows:** Balance of network topology types
- **Visualization:**
  - 2–3 pie charts:
    - Chart 1: Regime breakdown (Radial / Isotropic / Noise / Degenerate)
    - Chart 2: Entry type distribution (if RRP has type metadata)
    - Chart 3: Degenerate nodes isolated in own wedge (warning color)
  - Legend with percentages
  - Color-coded: Blue (radial), Teal (isotropic), Orange (noise), Red (degenerate)

#### 6. **Similarity Score Distribution Histogram**
- **What it shows:** How strong the bridges are (for Tier-2)
- **Visualization:**
  - Histogram: X-axis = similarity score (0.0–1.0), Y-axis = frequency
  - Bins: 10 or 20 buckets
  - Vertical line marking 0.75 threshold (strong analogy)
  - Color: Green (above threshold) / Gray (below threshold)
  - Annotation: Mean similarity, # bridges total

---

### Category B: Interactive Visualizations (HTML + D3.js / Plotly for exploration)

#### 7. **Interactive Network Graph (D3.js)**
- **What it shows:** Full RRP topology, user-explorable
- **Features:**
  - Force-directed layout: Nodes repel each other, edges attract (natural clustering)
  - Node properties:
    - Size: Proportional to degree (# links)
    - Color: By regime (Radial=blue, Isotropic=teal, Noise=orange, Degenerate=red)
    - Label: Entry ID (show on hover or always)
  - Edge properties:
    - Width: Proportional to link strength (if weighted)
    - Color: Gray or subtle gradient
    - Opacity: Adjustable
  - Interactions:
    - Drag nodes to reposition
    - Hover to highlight node + connected neighbors
    - Click to show entry details (type, domain, # links)
    - Zoom/pan
    - Filter by regime type (checkboxes on side)
    - Search: Find entry by ID and highlight
- **Output:** Single .html file with embedded D3.js
- **Library:** D3.js or Plotly.js (easier, less code)

#### 8. **Cross-RRP Bridge Explorer (D3.js)**
- **What it shows:** Similarity matrix + bridge strength
- **Features:**
  - Bipartite graph (two columns):
    - Left: Dataset A entries
    - Right: Dataset B entries
    - Bezier curves connecting similar entries
  - Curve thickness: Similarity score
  - Curve color: Green (strong) → Gray (weak)
  - Hover: Show similarity score, link type
  - Click: Show details of analogy
  - Zoom: Focus on top N bridges
  - Interactive threshold slider: Hide bridges below X similarity
- **Output:** Single .html file, embedded D3.js

#### 9. **Dimensionality Reduction Plot (t-SNE / UMAP)**
- **What it shows:** Dataset structure in 2D (reveals clusters)
- **Features:**
  - X/Y: t-SNE or UMAP of entry embeddings (if available via semantic similarity)
  - Dot color: By regime (blue/teal/orange/red)
  - Dot size: By degree (connection count)
  - Dot transparency: By noise fraction (noisier nodes are grayed out)
  - Hover: Entry ID, regime, degree, similarity to neighbors
  - Interactive:
    - Highlight entries by regime type
    - Search/filter
    - Zoom to clusters
- **Output:** Plotly .html (easier interactivity)
- **Library:** scikit-learn (t-SNE) + Plotly

#### 10. **Fisher Metrics Dashboard (Plotly)**
- **What it shows:** All Tier-1 metrics in one interactive dashboard
- **Features:**
  - 4 subplots:
    - Gauge: D_eff value with range indicators (1–20)
    - Bar chart: Regime distribution
    - Pie chart: Noise vs. Signal
    - Histogram: Link degree distribution
  - Interactive legend (show/hide subplots)
  - Hover annotations with values
- **Output:** Single Plotly .html
- **Library:** Plotly.js

---

### Category C: Comparison Visualizations (for Workflow B: cross-RRP analysis)

#### 11. **Dataset Comparison Matrix**
- **What it shows:** Side-by-side metrics for 2+ datasets
- **Visualization:**
  - Table with rows = datasets, columns = metrics
  - Metrics: # entries, # links, D_eff, noise %, coherence %, # bridges, bridge quality
  - Color-coded cells: Green (good) → Red (poor)
  - Sorting: Clickable column headers
- **Output:** Styled HTML table or PNG

#### 12. **Bridge Distribution Sankey Diagram**
- **What it shows:** Flow of analogies from Dataset A → Dataset B
- **Visualization:**
  - Left: Dataset A entry types (boxes)
  - Right: Dataset B entry types (boxes)
  - Flows: Thickness = # of bridges between type pairs
  - Color: By bridge strength (similarity)
  - Hover: Entry count, avg similarity
- **Output:** Plotly .html (Sankey built-in)

#### 13. **Coherence Comparison Radar Chart**
- **What it shows:** Tier-1 metrics for multiple datasets
- **Visualization:**
  - Radar/spider chart with 5 axes:
    - D_eff (scaled 0–20)
    - Non-noise fraction (0–100%)
    - Entry reach (0–100%)
    - Regime balance (0–1)
    - Structural diversity (0–1)
  - One polygon per dataset (different color)
  - Area = quality (larger = better)
- **Output:** Plotly .html

---

## Architecture

### Module Structure

```
src/viz/
├── viz_runner.py          ← Main orchestrator (generates all viz)
├── static_plots.py        ← matplotlib/seaborn visualizations
├── interactive_d3.py      ← D3.js graph generation
├── interactive_plotly.py  ← Plotly dashboard generation
├── comparison_viz.py      ← Multi-dataset comparisons
├── embedding_viz.py       ← t-SNE/UMAP visualizations
└── templates/
    ├── network_graph.html     ← D3.js template
    ├── bridge_explorer.html   ← D3.js bipartite template
    └── dashboard.html         ← Plotly template
```

### Key Functions

**Main Entry Point:**
```python
def generate_all_visualizations(
    rrp_db: str,
    wiki_db: str = None,
    output_dir: str = "output/",
    include_interactive: bool = True
) -> dict:
    """
    Generate all visualizations for an RRP.

    Returns:
    {
        "tier1_dashboard.png": path,
        "network_graph.html": path,
        "coherence_gauge.png": path,
        "bridge_explorer.html": path (if wiki_db provided),
        ...
    }
    """
```

**Individual Functions:**
- `plot_coherence_dashboard()` → PNG
- `plot_bridge_network()` → SVG
- `plot_pfd_score_breakdown()` → PNG
- `generate_network_graph_d3()` → HTML with D3.js
- `generate_bridge_explorer()` → HTML with D3.js
- `plot_tsne_reduction()` → Plotly HTML
- `generate_fisher_dashboard()` → Plotly HTML
- `compare_datasets()` → HTML table / PNG

---

## Implementation Phases

### Phase 1: Static Visualizations (Week 1)
- ✓ Coherence dashboard (pie + gauge + bars)
- ✓ PFD score breakdown
- ✓ Entry connectivity heatmap
- ✓ Similarity histogram
- **Libraries:** matplotlib, seaborn, numpy
- **Output:** PNG files, embeddable in reports

### Phase 2: Interactive Basic (Week 2)
- ✓ Interactive network graph (D3.js or Plotly)
- ✓ Fisher metrics dashboard (Plotly)
- ✓ t-SNE plot (Plotly)
- **Output:** .html files, shareable, no server needed

### Phase 3: Cross-RRP Comparison (Week 3)
- ✓ Bridge explorer (D3.js bipartite)
- ✓ Dataset comparison matrix
- ✓ Sankey diagram (Plotly)
- ✓ Radar chart (Plotly)

### Phase 4: Polish & Integration (Week 4)
- ✓ Embed visualizations in HTML report template
- ✓ Add export options (PDF, SVG)
- ✓ Performance optimization for large datasets
- ✓ Accessibility (color-blind palettes, labels)

---

## Integration with Existing Pipeline

### Where Visualizations Fit

```
Step 6: GENERATE REPORT
    ├─→ JSON report (already exists)
    ├─→ Text summary (already exists)
    ├─→ [NEW] PNG visualizations (static plots)
    ├─→ [NEW] HTML interactive (exploratory)
    └─→ [NEW] Combined HTML report (all above)
```

### CLI Integration

```bash
# Current
python scripts/run_fisher_suite.py --mode report \
    --rrp-db data/rrp/dataset/rrp_dataset.db \
    --wiki-db data/ds_wiki.db

# Output:
#   - rrp_dataset_report.json
#   - rrp_dataset_summary.txt

# NEW:
# Output adds:
#   - rrp_dataset_viz_coherence.png (static)
#   - rrp_dataset_viz_network.html (interactive)
#   - rrp_dataset_viz_bridges.html (interactive, if wiki provided)
#   - rrp_dataset_report.html (combined dashboard)
```

---

## Technology Choices

| Visualization Type | Library | Rationale |
|-------------------|---------|-----------|
| Static plots | Matplotlib + Seaborn | Simple, publication-quality, no dependencies beyond pip |
| Interactive graphs | D3.js + HTML | Full control, no server needed, highly customizable |
| Dashboards | Plotly | Easier than D3, built-in interactivity, single HTML file |
| Dimensionality reduction | scikit-learn + Plotly | Standard tools, easy integration |
| Report compilation | Jinja2 + HTML/CSS | Template-based, clean HTML output |

---

## Expected Outputs per Analysis

### After Single RRP Analysis (Internal only)

```
output/
├── rrp_dataset_report.json                 (existing)
├── rrp_dataset_summary.txt                 (existing)
├── viz_coherence_dashboard.png             ← NEW (static)
├── viz_noise_vs_signal.png                 ← NEW (static)
├── viz_regime_distribution.png             ← NEW (static)
├── viz_link_degree_histogram.png           ← NEW (static)
├── viz_network_interactive.html            ← NEW (interactive)
├── viz_pfd_score_breakdown.png             ← NEW (static)
└── report.html                             ← NEW (combined, includes all viz)
```

### After Cross-RRP Analysis (With bridges)

```
output/
├── [all above files from single analysis]
├── viz_bridge_network.png                  ← NEW (static)
├── viz_similarity_distribution.png         ← NEW (static)
├── viz_bridges_interactive.html            ← NEW (interactive)
├── viz_dataset_comparison.png              ← NEW (static)
├── viz_sankey_bridges.html                 ← NEW (interactive)
└── report_cross_rrp.html                   ← NEW (combined)
```

---

## User Experience

### Workflow A: Single Dataset Analysis
1. User runs: `python scripts/run_fisher_suite.py --mode report --rrp-db data/rrp/my_data/rrp_my_data.db`
2. System generates report + ALL visualizations automatically
3. User opens `report.html` in browser → comprehensive dashboard with:
   - Summary metrics
   - Static plots (PNG embeds)
   - Interactive network graph (explore structure)
   - D3.js dashboard (zoom/filter/search)
   - PFD score breakdown
4. User can:
   - Download individual PNG files for presentations
   - Share .html files (standalone, no server needed)
   - Copy graphics into research papers

### Workflow B: Cross-RRP Analysis
1. User compares Dataset A ↔ Dataset B
2. System generates ALL above + cross-RRP specific:
   - Bridge network visualization
   - Bridge explorer (interactive D3)
   - Similarity distribution
   - Sankey flow diagram
   - Dataset comparison table
3. User can see "Aha!" moments:
   - "Ah! Metabolic hub (met_pyr_c) clusters with power grid hub (bus_14) — both highly central"
   - "These taxonomy entries match CS complexity hierarchy entries — interesting analogy"

---

## Design Principles

1. **No Server Required:** All outputs are static HTML (D3.js embedded) or PNG. Share via email, GitHub, S3, etc.
2. **Embeddable:** PNG exports for papers, presentations, proposals
3. **Exploration:** Interactive visualizations reveal patterns
4. **Publication-Ready:** High quality, professional aesthetics
5. **Color-Blind Friendly:** Palettes that work for deuteranopia (red-green colorblind)
6. **Accessibility:** Labels, legends, hover text for all data

---

## Success Metrics

- Users can understand RRP structure visually (not just from JSON)
- Bridge analogies are visually obvious (not abstract)
- Tier-1/Tier-2 verdicts are intuitive (color-coded, gauges)
- Interactive graphs enable exploratory analysis
- Visualizations are polished enough for academic papers
- Setup is automatic (no manual configuration)

---

## Next Steps

1. **Prioritize:** Which visualizations first? (Suggest: static dashboard + interactive network graph)
2. **Prototype:** Build 1–2 key visualizations as proof-of-concept
3. **Integrate:** Wire into `fisher_report.py` output pipeline
4. **Test:** Run on existing datasets (E. coli, Zoo, IEEE grids)
5. **Polish:** Refine styling, optimize for performance
6. **Document:** Update USER_GUIDE to show example visualizations

---

**Estimated Effort:** 3–4 weeks for full suite (all 13 visualization types)
**MVT (Minimum Viable): Coherence dashboard + interactive network graph + PFD score (1 week)**
