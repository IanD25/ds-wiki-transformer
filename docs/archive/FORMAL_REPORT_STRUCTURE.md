# PFD Formal Report Structure

**Purpose:** Define the complete report architecture that serves as the container for all visualizations and analysis results.

**Output Format:** Single-page HTML (self-contained, embeddable, printable to PDF)
**Data Flow:** Fisher diagnostics → JSON → Report generator → Report.html (+ visualization embeds)

---

## Report Taxonomy

Reports come in two types, with shared structure:

- **Type A: Single-RRP Report** (Tier-1 only, internal analysis)
- **Type B: Cross-RRP Report** (Tier-1 + Tier-2, bridge analysis)

Both follow the same template structure, with Type B adding bridge-specific sections.

---

## Overall Report Flow (Visual Hierarchy)

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER SECTION                                              │
│ - Title, dataset metadata, timestamp                        │
│ - Quick stats (# entries, # links, coherence %)             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ EXECUTIVE SUMMARY                                           │
│ - PFD Score (large, visual)                                 │
│ - Tier-1 Verdict + Tier-2 Verdict (Type B only)            │
│ - Plain-English interpretation                              │
│ - Key findings in 3–5 bullets                               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SECTION 1: INTERNAL STRUCTURE (Tier-1)                      │
│                                                             │
│ 1.1 Coherence Overview                                      │
│     [Static] Pie chart: Noise vs. Signal                    │
│     [Static] D_eff Gauge                                    │
│                                                             │
│ 1.2 Regime Analysis                                         │
│     [Static] Bar chart: Regime distribution                 │
│     [Interactive] Network graph (explorable)                │
│                                                             │
│ 1.3 Connectivity Profile                                    │
│     [Static] Heatmap: Entry degree distribution             │
│     [Static] Histogram: Link degree distribution            │
│                                                             │
│ 1.4 Detailed Metrics                                        │
│     - D_eff value + interpretation                          │
│     - Noise fraction + interpretation                       │
│     - Top 10 hubs (table)                                   │
│     - Isolated entries (table)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SECTION 2: CROSS-RRP BRIDGES (Tier-2) [TYPE B ONLY]        │
│                                                             │
│ 2.1 Bridge Overview                                         │
│     [Static] Summary: # bridges, mean similarity, reach %   │
│     [Static] PFD Score breakdown (stacked bar)              │
│                                                             │
│ 2.2 Bridge Quality                                          │
│     [Static] Histogram: Similarity distribution             │
│     [Static] Network diagram: Bridge strengths              │
│     [Interactive] Bridge explorer (D3.js bipartite)        │
│                                                             │
│ 2.3 Top Analogies                                           │
│     [Table] Top 20 bridges (entry pairs, similarity, type)  │
│                                                             │
│ 2.4 Domain Mapping                                          │
│     [Static] Sankey: Type A entry types → Type B entry types│
│     [Text] Narrative: Cross-domain insights                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SECTION 3: VERDICTS & INTERPRETATION                        │
│                                                             │
│ 3.1 Tier-1 Verdict                                          │
│     - Verdict: INTERNALLY CONSISTENT / MARGINAL / FRAGMENTED│
│     - Reasoning: (3–4 sentences)                            │
│     - Confidence: (explain noise/signal balance)            │
│                                                             │
│ 3.2 Tier-2 Verdict [TYPE B ONLY]                            │
│     - Verdict: WELL-INTEGRATED / PARTIAL / ISOLATED         │
│     - Reasoning: (3–4 sentences)                            │
│     - Bridge reach: X% of entries found analogies           │
│                                                             │
│ 3.3 Implications                                            │
│     - What this means for your data                         │
│     - Recommended next steps                                │
│     - Caveats / limitations                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SECTION 4: METHODOLOGY & DEFINITIONS                        │
│                                                             │
│ 4.1 How PFD Works (brief)                                   │
│     - 6-step pipeline diagram (reference to USER_GUIDE)     │
│     - "What we measured and why"                            │
│                                                             │
│ 4.2 Key Metrics Explained                                   │
│     - D_eff (Effective Dimensionality)                      │
│     - Noise Fraction                                        │
│     - Entry Reach (for Tier-2)                              │
│     - Similarity Score                                      │
│     - Regimes (Radial / Isotropic / Noise / Degenerate)    │
│                                                             │
│ 4.3 Verdict Interpretation                                  │
│     - How Tier-1 verdict is computed                        │
│     - How Tier-2 verdict is computed                        │
│     - What each verdict category means                      │
│                                                             │
│ 4.4 Assumptions & Limitations                               │
│     - RRP schema assumptions                                │
│     - What PFD can and cannot tell you                      │
│     - When results may be misleading                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ APPENDIX: DATA TABLES                                       │
│                                                             │
│ A1. All Entries (table: ID, type, domain, degree, regime)   │
│ A2. All Links (table: source, target, type, if applicable)  │
│ A3. Hubs Summary (top 20 by degree)                          │
│ A4. Isolated Entries (degree = 0)                           │
│ A5. Bridge List [TYPE B] (all bridges, ranked by similarity)│
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ FOOTER                                                      │
│ - Generation timestamp                                      │
│ - PFD version                                               │
│ - Citation/attribution                                      │
│ - Links to documentation                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Detailed Section Specifications

### HEADER SECTION (Fixed, always visible)

**Layout:** Sticky header (stays at top when scrolling)

**Content:**
```
┌──────────────────────────────────────────────────────┐
│ PFD Report: [Dataset Name]                           │
│ Generated: [Timestamp] | Version: [PFD version]      │
├──────────────────────────────────────────────────────┤
│ QUICK STATS                                          │
│ Entries: 304  |  Links: 536  |  Coherence: 81.3%   │
│ D_eff: 11.2   |  Noise: 7.8% |  Type: [RRP type]   │
│                                                      │
│ PFD SCORE: 0.94 ✓✓                                  │
│ Tier-1: 0.81 (INTERNALLY CONSISTENT)                │
│ Tier-2: 1.00 (WELL-INTEGRATED) [if cross-RRP]      │
└──────────────────────────────────────────────────────┘
```

**Visual Elements:**
- Title (48pt, dark gray)
- Quick stats (grid, 18pt font, monospace for numbers)
- PFD Score badge (large circle, green, 0.94 displayed)
- Verdict icons (✓ for consistent, ⚠ for marginal, ✗ for fragmented)

**Purpose:** At-a-glance summary; user knows verdict immediately

---

### EXECUTIVE SUMMARY

**Layout:** Single column, card-style box

**Content (4 parts):**

1. **PFD Score Visualization** (centered)
   - Large gauge showing 0.94 on 0.0–1.0 scale
   - Color: Green (excellent)

2. **Verdict Statement** (2–3 lines, 20pt)
   ```
   ✓ INTERNALLY CONSISTENT (Tier-1)
   ✓ WELL-INTEGRATED (Tier-2)

   Your dataset exhibits strong internal coherence and robust
   structural alignment with the reference knowledge base.
   ```

3. **Key Findings** (5 bullets, 18pt)
   - Metabolic network shows clear hub structure (D_eff = 11.2)
   - 93% of signal; only 7% noise
   - 23 strong analogies to reference domains
   - Top hub: Pyruvate (central TCA intermediate, 23 links)
   - All entry types well-represented

4. **Next Steps** (suggested actions)
   - "Your data is solid for downstream analysis"
   - "Consider integrating with domains: [list]"
   - "Investigate isolated entries: [list]"

**Purpose:** User can stop here and understand verdict; deeper sections are optional

---

### SECTION 1: INTERNAL STRUCTURE (Tier-1)

#### 1.1 Coherence Overview

**Layout:** Two-column, side-by-side visualizations

**Left Column:**
- **Visualization:** Pie chart (noise vs. signal)
  - 2 slices: Signal (81.3%, green) | Noise (18.7%, orange)
  - Title: "Signal vs. Noise Composition"
  - Annotations: % labels on slices

**Right Column:**
- **Visualization:** D_eff Gauge
  - Semicircular gauge: 1 (left, planar) → 20 (right, distributed)
  - Needle at 11.2 (metabolic hub structure)
  - Color gradient: Blue (low) → Red (high)
  - Title: "Effective Dimensionality"
  - Interpretation text: "11.2 indicates a highly distributed network with clear hub structure. Typical for metabolic networks."

**Below Both:**
- Coherence score: 81.3% (INTERNALLY CONSISTENT)
- Interpretation: "Non-noise fraction > 66%, indicating strong signal."

**Purpose:** User understands dataset balance (signal vs. noise, topology type)

---

#### 1.2 Regime Analysis

**Layout:** Two-column, stacked

**Left Column:**
- **Visualization:** Bar chart (regime distribution)
  - X-axis: Regime types (Radial / Isotropic / Noise / Degenerate)
  - Y-axis: # of nodes or %
  - Colors: Blue (Radial) | Teal (Isotropic) | Orange (Noise) | Red (Degenerate)
  - Title: "Regime Distribution"
  - Value labels on bars

**Right Column:**
- **Text interpretation:**
  ```
  Radial-Dominated (35%): Hub-like structure
  - Few central nodes, many peripheral nodes
  - Typical for metabolic networks

  Isotropic (48%): Balanced structure
  - Evenly distributed connectivity
  - Indicates diverse relationship types

  Noise-Dominated (12%): Potentially random links
  - Flag for manual review

  Degenerate (5%): Isolated nodes
  - See Appendix A4 for list
  ```

**Below:**
- **Visualization:** Interactive Network Graph (D3.js)
  - Force-directed layout
  - Node colors: By regime (blue/teal/orange/red)
  - Node size: By degree
  - Features:
    - Hover: Show entry ID, regime, degree
    - Filter: Checkboxes to show/hide regime types
    - Search: Find entry by ID
    - Zoom/pan enabled
  - Title: "Interactive Network Topology"
  - Instruction: "Click + drag to explore. Hover for details. Use filters (right) to focus."

**Purpose:** User sees topology types and can interactively explore structure

---

#### 1.3 Connectivity Profile

**Layout:** Two-column

**Left Column:**
- **Visualization:** Entry Connectivity Heatmap
  - Matrix: Rows = entries (sorted by degree, desc), Columns = degree bins
  - Color intensity: Bright (many links) → Dark (few links)
  - Red highlight: Isolated entries (degree = 0)
  - Rownames: Entry IDs (sample every Nth to avoid crowding)
  - Title: "Entry Degree Distribution"
  - Scrollable if dataset large

**Right Column:**
- **Visualization:** Link Degree Histogram
  - X-axis: # links per entry (0–max)
  - Y-axis: Frequency (count of entries with X links)
  - Bars colored by regime type
  - Title: "Link Degree Distribution"
  - Annotations: Mean degree, median, max degree

**Below:**
- Summary statistics:
  ```
  Total entries: 304
  Total links: 536
  Mean degree: 3.5
  Max degree: 23 (entry ID)
  Isolated: 0
  Degree-1 entries: 12 (see Appendix A4)
  ```

**Purpose:** User understands connectivity landscape (are hubs clear? are isolated entries problematic?)

---

#### 1.4 Detailed Metrics

**Layout:** Single column, tabular

**Tier-1 Metrics Table:**
| Metric | Value | Interpretation |
|--------|-------|-----------------|
| D_eff | 11.2 | Distributed metabolic structure |
| Noise Fraction | 7.8% | Strong signal (> 92% signal) |
| Coherence Score | 81.3% | INTERNALLY CONSISTENT |
| Entry Count | 304 | Dataset size |
| Link Count | 536 | Link density |
| Mean Degree | 3.5 | Moderate connectivity |
| Max Degree | 23 | Clear hubs present |
| Radial % | 35% | Hub-like regions |
| Isotropic % | 48% | Balanced connectivity |
| Degenerate % | 5% | Few isolated nodes |

**Below: Top Hubs Table**

Title: "Top 10 Network Hubs"
```
Rank | Entry ID | Type | Domain | Degree | Regime |
1    | met_pyr_c | instantiation | biochemistry | 23 | Radial |
2    | met_atp_c | instantiation | biochemistry | 21 | Radial |
3    | met_h2o_c | instantiation | biochemistry | 19 | Isotropic |
...
```

**Purpose:** Researcher can identify key nodes for deeper analysis

---

### SECTION 2: CROSS-RRP BRIDGES (Tier-2) [TYPE B ONLY]

#### 2.1 Bridge Overview

**Layout:** Two-column

**Left Column:**
- **Text summary:**
  ```
  Bridges Found: 47
  Entry Reach: 100% (47/47 Dataset A entries matched)
  Mean Similarity: 0.79
  Strong Bridges (>0.75): 34 (72%)
  Moderate Bridges (0.55–0.75): 13 (28%)

  Interpretation:
  Your dataset shows robust structural alignment with the
  reference knowledge base. All entries found analogous
  structures, indicating high cross-domain relevance.
  ```

**Right Column:**
- **Visualization:** PFD Score Breakdown (stacked horizontal bar)
  - Left 50%: Tier-1 contribution (0.81)
  - Right 50%: Tier-2 contribution (1.00)
  - Colors: Blue (T1) | Green (T2)
  - Center label: PFD Score 0.94
  - Below: "How the final score is calculated: 0.5 × T1 + 0.5 × T2"

**Purpose:** User sees bridge impact on final score

---

#### 2.2 Bridge Quality

**Layout:** Two-column, stacked

**Left Column:**
- **Visualization:** Similarity Distribution Histogram
  - X-axis: Similarity score (0.0–1.0)
  - Y-axis: # bridges
  - Bins: 10–20 buckets
  - Vertical line at 0.75 (strong threshold)
  - Color: Green (> 0.75) | Gray (< 0.75)
  - Title: "Bridge Similarity Distribution"
  - Annotations: Mean, median, mode values

**Right Column:**
- **Visualization:** Bridge Network Diagram (bipartite)
  - Left nodes: Dataset A entries (sample top 10 by bridges)
  - Right nodes: Dataset B entries (sample top 10 by bridges)
  - Edges: Bezier curves, thickness = similarity
  - Edge color: Green (strong) → Gray (weak)
  - Title: "Top Bridge Connections"
  - Instruction: "Width = strength. Hover for similarity scores."

**Below:**
- **Visualization:** Interactive Bridge Explorer (D3.js)
  - Full bipartite graph (all entries)
  - Features:
    - Hover: Show similarity score, link type
    - Filter: Threshold slider (hide bridges < X similarity)
    - Search: Find entry by ID
    - Highlight connected pairs
    - Toggle node labels
  - Title: "Interactive Bridge Explorer"
  - Instruction: "Adjust threshold to focus on strong analogies. Search to isolate entries."

**Purpose:** User can see which entries bridge best and explore interactively

---

#### 2.3 Top Analogies

**Layout:** Full-width table

**Title:** "Top 20 Cross-Domain Analogies"

```
Rank | Dataset A Entry | Type A | Dataset B Entry | Type B | Similarity | Reason |
1    | met_pyr_c | metabolite | CHEM5 | reference_law | 0.89 | Hub topology |
2    | reaction_glyc | reaction | CS15 | theorem | 0.87 | Complexity parallel |
3    | met_atp_c | metabolite | INFO1 | instantiation | 0.84 | Information carrier |
...
20   | ... | ... | ... | ... | ... | ... |
```

**Columns:**
- Rank (1–20)
- Dataset A Entry ID + Type
- Dataset B Entry ID + Type
- Similarity (0.0–1.0)
- Reason (1-line explanation of analogy)

**Purpose:** Researcher can drill into specific analogies for deeper investigation

---

#### 2.4 Domain Mapping

**Layout:** Two-column

**Left Column:**
- **Visualization:** Bridge Distribution Sankey Diagram
  - Left boxes: Dataset A entry types (e.g., metabolite, reaction)
  - Right boxes: Dataset B entry types (e.g., law, theorem, axiom)
  - Flows: # of bridges between type pairs
  - Flow color: By bridge strength (gradient green/gray)
  - Title: "Entry Type Bridging Patterns"
  - Hover: Count of bridges, average similarity

**Right Column:**
- **Narrative text:**
  ```
  Domain Insights:

  Metabolites (Dataset A) most commonly bridge to:
  - Reference laws (CHEM, BIO) — 18 bridges
  - Instantiations (INFO) — 12 bridges
  - Parameters (MATH) — 8 bridges

  This suggests metabolic entities have clear analogues
  in formal sciences and reference domains.

  Strongest analogy:
  Pyruvate (central metabolite) ↔ CHEM5 (Law of
  Thermodynamic Scaling) — both are "crossroads"
  concepts with high structural importance.
  ```

**Purpose:** User understands which domains connect and why

---

### SECTION 3: VERDICTS & INTERPRETATION

#### 3.1 Tier-1 Verdict

**Layout:** Card-style box with border

```
┌─────────────────────────────────────────────────┐
│ TIER-1 VERDICT: INTERNALLY CONSISTENT ✓        │
│                                                │
│ COHERENCE SCORE: 81.3%                         │
│ Non-noise fraction > 66% threshold              │
│                                                │
│ REASONING:                                      │
│ Your dataset exhibits strong internal structure│
│ with 81.3% signal content. The network is not │
│ random; it reflects deliberate relationships.  │
│ Hubs are clear (e.g., pyruvate with 23 links) │
│ and peripheral nodes are few.                  │
│                                                │
│ CONFIDENCE:                                     │
│ High. The 81.3% signal dominates noise,        │
│ making the verdict robust.                     │
│                                                │
│ IMPLICATIONS:                                   │
│ ✓ Proceed to bridge analysis with confidence   │
│ ✓ Use hubs for downstream modeling             │
│ ⚠ Investigate degree-1 entries (n=12)         │
│ ✓ Network structure is suitable for analysis   │
└─────────────────────────────────────────────────┘
```

**Visual elements:**
- Green checkmark icon
- Color: Light green background (#F0F7F4)
- Border: 2px green (#2E965F)

**Purpose:** Crystal-clear statement of data quality

---

#### 3.2 Tier-2 Verdict [TYPE B ONLY]

**Layout:** Card-style box (similar to Tier-1)

```
┌─────────────────────────────────────────────────┐
│ TIER-2 VERDICT: WELL-INTEGRATED ✓✓            │
│                                                │
│ BRIDGE REACH: 100% (47/47 entries)             │
│ MEAN SIMILARITY: 0.79                          │
│ STRONG BRIDGES (>0.75): 72%                    │
│                                                │
│ REASONING:                                      │
│ All 47 of your dataset entries found strong   │
│ structural analogues in the reference         │
│ knowledge base. This indicates your data fits │
│ within established scientific frameworks.     │
│ The analogies are mostly strong (0.79 mean)   │
│ suggesting deep conceptual alignment.         │
│                                                │
│ CONFIDENCE:                                     │
│ High. 100% reach + mean similarity 0.79       │
│ indicates genuine cross-domain connection.    │
│                                                │
│ IMPLICATIONS:                                   │
│ ✓ Your data bridges multiple scientific domains│
│ ✓ Unexpected analogies may reveal new insights│
│ ✓ Reference structures inform your modeling   │
│ ✓ Consider integrating with: [domain list]   │
└─────────────────────────────────────────────────┘
```

**Visual elements:**
- Green double-checkmark icon (✓✓)
- Color: Light green background

**Purpose:** Communicate bridge quality and implications

---

#### 3.3 Implications

**Layout:** Narrative with highlighted boxes

```
WHAT THIS MEANS FOR YOUR WORK:

1. Data Quality ✓
   Your dataset is internally coherent and well-positioned
   for analysis. The 81.3% signal content and 100% bridge
   reach indicate high-quality, well-structured data.

2. Downstream Suitability
   ✓ Suitable for: Machine learning, topological analysis,
                   comparison with other datasets
   ⚠ Investigate: 12 degree-1 entries (could be errors)
   ✗ Not suitable for: Claims without bridge support

3. Methodological Alignment
   Your data aligns with established reference frameworks
   (e.g., CHEM5 for thermodynamic scaling). This suggests
   your modeling should respect these frameworks.

4. RECOMMENDED NEXT STEPS:

   Immediate (Week 1):
   - Review the 12 degree-1 entries (Appendix A4)
   - Identify which bridges are most interesting
   - Consider domain integration (cross-domain modeling)

   Short-term (Month 1):
   - Compare to other datasets using PFD
   - Investigate top analogies for surprising insights
   - Validate bridge hypotheses experimentally

   Long-term (Phase 3+):
   - Integrate with Phase 3 (claim validation)
   - Use PFD Score to track data quality over time
   - Contribute validated bridges back to reference KB

5. CAVEATS & LIMITATIONS:
   - PFD measures *structure*, not biological correctness
   - High coherence ≠ high accuracy; still validate
   - Bridge similarity is semantic, not causal
   - Reference KB is incomplete (bias toward physics/chem)
```

**Purpose:** User has clear guidance on what to do next

---

### SECTION 4: METHODOLOGY & DEFINITIONS

#### 4.1 How PFD Works (Brief)

**Layout:** Single column with diagram reference

```
PFD analyzes your dataset through a 6-step pipeline:

[Diagram: Reference to PFD_WORKFLOW_DIAGRAM.png]

Step 1: INGEST — Parse your data into RRP schema
Step 2: BUILD GRAPH — Model entries + links as a network
Step 3: DIAGNOSE INTERNAL — Compute Fisher metrics
Step 4: BUILD BRIDGE — Compare to reference knowledge base
Step 5: DIAGNOSE BRIDGE — Find structural analogies
Step 6: GENERATE REPORT — Create this report + verdicts

The analysis produces two verdicts:
- Tier-1: Is your data internally consistent? (Steps 1–3)
- Tier-2: How well does it bridge to references? (Steps 4–6)

For full details, see USER_GUIDE.md.
```

**Purpose:** Context for non-experts; points to deeper docs

---

#### 4.2 Key Metrics Explained

**Layout:** Glossary-style, card per metric

```
┌──────────────────────────────────────────────────────┐
│ D_eff: Effective Dimensionality                     │
├──────────────────────────────────────────────────────┤
│ What: A topological measure of network structure    │
│ Range: 1 (planar/tree) → 20+ (highly distributed)  │
│ Examples:                                           │
│   1.5–2.0: Power grids, organizational hierarchies │
│   5–8:     Taxonomies, biological classifications  │
│   10+:     Metabolic networks, social networks     │
│ Why it matters: Tells you the "shape" of your data │
│ In your dataset: 11.2 (highly distributed, hub-like)│
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│ Noise Fraction                                      │
├──────────────────────────────────────────────────────┤
│ What: % of links that appear random vs. meaningful  │
│ Range: 0% (all signal) → 100% (all noise)          │
│ Examples:                                           │
│   < 10%: Strong signal, high confidence            │
│   10–40%: Mixed signal/noise, proceed cautiously   │
│   > 40%: Mostly noise, data quality issues         │
│ Why it matters: Is your network deliberate or random│
│ In your dataset: 7.8% (excellent, strong signal)   │
└──────────────────────────────────────────────────────┘

[Similar cards for Entry Reach, Similarity Score, Regimes]
```

**Purpose:** User understands what each metric means

---

#### 4.3 Verdict Interpretation

**Layout:** Decision table

```
TIER-1 VERDICT INTERPRETATION:

Verdict          | Coherence % | Meaning | Action |
---              | ---         | ---     | ---    |
INTERNALLY       | > 66%       | Strong  | Proceed |
CONSISTENT       |             | signal  | with    |
                 |             |         | confidence |
---              | ---         | ---     | ---    |
MARGINAL         | 40–66%      | Mixed   | Investigate |
                 |             | signal  | discrepancies |
                 |             | + noise |        |
---              | ---         | ---     | ---    |
FRAGMENTED       | < 40%       | Mostly  | Review data |
                 |             | noise   | quality |
                 |             |         | before use |

[Similar table for TIER-2]
```

**Purpose:** User knows how to interpret their verdict

---

#### 4.4 Assumptions & Limitations

**Layout:** Bullet list with callout boxes

```
ASSUMPTIONS UNDERLYING PFD:

✓ Your RRP schema is valid
  (entries are nodes, links are edges)

✓ Link presence is meaningful
  (not random, represents real relationships)

✓ Symmetry: if A→B, also consider B→A
  (bidirectional semantics)

✓ Reference KB is representative
  (but incomplete; more physics/chem than biology)

WHAT PFD CAN TELL YOU:

✓ Is your data internally coherent?
✓ What is the topological structure?
✓ Which entries are hubs vs. peripheral?
✓ How does it align with reference domains?
✓ Are there unexpected cross-domain analogies?

WHAT PFD CANNOT TELL YOU:

✗ Whether your data is scientifically correct
  (PFD measures structure, not accuracy)

✗ Causal relationships
  (structural similarity ≠ causation)

✗ Biological function
  (structure ≠ phenotype)

✗ Completeness
  (a sparse network can still be coherent)

WHEN TO BE CAUTIOUS:

⚠ High coherence with low entry count
  (small networks can be accidentally coherent)

⚠ Bridges to domains you don't expect
  (check the analogy reasoning)

⚠ Biased domains
  (PFD was trained on physics/chemistry-heavy data)

⚠ Isolated entries
  (could be errors or genuine outliers)
```

**Purpose:** User is aware of limitations and avoids misinterpretation

---

### APPENDIX: DATA TABLES

#### A1. All Entries

```
Entry ID | Type | Domain | Degree | Regime | Notes |
met_pyr_c | instantiation | biochemistry | 23 | Radial | TCA hub |
met_atp_c | instantiation | biochemistry | 21 | Radial | Energy carrier |
...
```

**Sortable/Searchable:** Columns allow sorting by any field

**Purpose:** Full transparency; researcher can verify

---

#### A2. All Links

```
Source | Target | Link Type | Weight | Notes |
met_pyr_c | met_acetyl | produces | 1.0 | TCA → Acetyl |
reaction_glyc | met_atp_c | produces | 1.0 | ATP generation |
...
```

**Purpose:** Complete link inventory

---

#### A3–A5: Other tables
(Hubs, Isolated entries, Bridge list)

---

### FOOTER

```
Report generated: 2026-03-11 14:32:15 UTC
PFD version: 0.2.3
Dataset: E. coli core metabolic network

For more information:
- USER_GUIDE.md: Step-by-step usage and examples
- MASTER_SUMMARY.md: Full technical reference
- GitHub: https://github.com/IanD25/ds-wiki-transformer

Citation:
Darling, I. (2026). Principia Formal Diagnostics:
Graph Coherence Analysis for Research Datasets. v0.2.3.
https://github.com/IanD25/ds-wiki-transformer

This report is a diagnostic tool, not a scientific validation.
Always verify findings independently before relying on them.
```

---

## Report Generation Flow

```
Fisher Analysis Results (JSON)
    ↓
ReportGenerator(rrp_db, wiki_db)
    ├─→ Extract metadata
    ├─→ Render Header
    ├─→ Render Executive Summary
    ├─→ Render Section 1 (Tier-1)
    │   ├─→ Call plot_coherence_dashboard() → PNG
    │   ├─→ Call plot_regime_chart() → PNG
    │   ├─→ Call generate_network_graph() → HTML
    │   └─→ Embed in report
    ├─→ Render Section 2 (Tier-2, if applicable)
    │   ├─→ Call plot_bridge_network() → PNG
    │   ├─→ Call plot_similarity_histogram() → PNG
    │   ├─→ Call generate_bridge_explorer() → HTML
    │   └─→ Embed in report
    ├─→ Render Section 3 (Verdicts)
    ├─→ Render Section 4 (Methodology)
    ├─→ Render Appendices (tables)
    ├─→ Render Footer
    └─→ Output: report.html (single, self-contained file)
```

---

## Report Output Specifications

**Format:** Single-page HTML, self-contained (CSS + JS embedded)
**File Size:** ~2–5 MB (includes D3.js + Plotly libraries)
**Browser Compatibility:** Chrome, Firefox, Safari, Edge (ES6+)
**Print-to-PDF:** Supported; maintains formatting

**Responsive Design:**
- Desktop: Full layout with side-by-side columns
- Tablet: Single-column, stacked visualizations
- Print: Optimized for PDF export (page breaks, font sizes)

**Accessibility:**
- WCAG AA compliant (high contrast, semantic HTML)
- Color-blind friendly palette (no red-green only distinction)
- Alt-text for all images
- Keyboard navigation support

---

## Section Summary & Visualization Map

| Section | Purpose | Visualizations | Interactive? |
|---------|---------|-----------------|--------------|
| Header | Quick glance | Summary stats, badges | No |
| Exec Summary | Verdict at a glance | PFD Score, bullets | No |
| 1.1 Coherence | Signal vs. noise | Pie chart, D_eff gauge | No |
| 1.2 Regime | Topology types | Bar chart, network graph | Yes |
| 1.3 Connectivity | Hub/peripheral landscape | Heatmap, histogram | No |
| 1.4 Metrics | Details for experts | Tables | No |
| 2.1 Bridge Overview | Bridge summary | Summary stats, score breakdown | No |
| 2.2 Bridge Quality | Bridge strength | Histogram, network, explorer | Yes |
| 2.3 Top Analogies | Specific analogies | Table | Sortable |
| 2.4 Domain Mapping | Type bridging | Sankey, narrative | No |
| 3.1–3.3 Verdicts | Interpretation | Cards + guidance | No |
| 4.1–4.4 Methodology | Context + caveats | Diagram references, glossary | No |
| Appendices | Full data | Tables | Searchable |
| Footer | Attribution | Links, citation | No |

---

## Design Consistency

**Color Palette:**
- Tier-1 verdict: Green #2E965F (internally consistent)
- Tier-2 verdict: Blue #19518F (cross-domain insight)
- Noise/warning: Amber #DC8C19
- Error: Red #C8323C
- Text: Dark gray #3C3C3C

**Typography:**
- Title: 48pt, bold, sans-serif
- Verdict text: 20–24pt
- Body: 16–18pt
- Labels: 14–16pt
- Monospace for data/metrics

**Spacing:**
- Margins: 40px
- Section breaks: 60px
- Element padding: 15–20px

---

**This specification is the blueprint for Report.html. Visualizations are designed to serve narrative sections, not stand alone.**
