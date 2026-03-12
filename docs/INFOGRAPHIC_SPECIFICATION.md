# PFD Workflow Infographic — Complete Specification

**Purpose:** Professional, comprehensive visual guide to the Principia Formal Diagnostics (PFD) 6-step pipeline and two-tier output system.

**Output Format:** Single-page 4K infographic (2560×1440 pixels, 16:9 aspect ratio), PNG or PDF
**Design Philosophy:** "Structural Revelation" — systematic observation, expert craftsmanship, visual clarity
**Audience:** Researchers, data engineers, conference attendees, GitHub visitors

---

## Layout & Structure

The infographic unfolds vertically in three major sections:

### Section 1: Header (Top 15% of canvas)
- **Title:** "Principia Formal Diagnostics" (72pt, bold, dark gray #3C3C3C)
- **Tagline:** "Graph Coherence Engine for Research Datasets" (32pt, medium gray #787878)
- **Divider Line:** Horizontal rule (2px, light gray #C8C8C8) spanning full width minus margins

**Purpose:** Immediate brand identity and value proposition

---

### Section 2: 6-Step Pipeline (15%–35% of canvas)

**Layout:** Horizontal left-to-right flow with 6 nodes and connecting arrows

**Pipeline Steps (in order):**

1. **INGEST**
   - Icon: Circle with "1" (teal #008C9E, white text)
   - Label (below): "INGEST"
   - Sublabel: "RRP\nData"
   - Description: Convert research data into standardized RRP schema

2. **BUILD GRAPH**
   - Icon: Circle with "2"
   - Label: "BUILD\nGRAPH"
   - Sublabel: "Internal\nStructure"
   - Description: Model dataset structure (entries + links)

3. **DIAGNOSE INTERNAL**
   - Icon: Circle with "3"
   - Label: "DIAGNOSE\nINTERNAL"
   - Sublabel: "Coherence\nAnalysis"
   - Description: Compute Fisher metrics (D_eff, noise, regime)

4. **BUILD BRIDGE**
   - Icon: Circle with "4"
   - Label: "BUILD\nBRIDGE"
   - Sublabel: "Cross-RRP\nMapping"
   - Description: Optional — compare to other datasets

5. **DIAGNOSE BRIDGE**
   - Icon: Circle with "5"
   - Label: "DIAGNOSE\nBRIDGE"
   - Sublabel: "Analogy\nDetection"
   - Description: Find structural analogies across datasets

6. **GENERATE REPORT**
   - Icon: Circle with "6"
   - Label: "GENERATE\nREPORT"
   - Sublabel: "Final\nOutput"
   - Description: Two-tier verdict + PFD Score

**Visual Details:**
- Node circles: 70px diameter, teal fill #008C9E, dark gray outline (2px)
- Node numbers: White, 24pt, centered
- Connecting arrows: Gray #787878, 2px width, arrowheads pointing right
- Arrow path: Horizontal line at y-center of nodes
- Step labels: 28pt, dark gray, left-aligned below node
- Sublabels: 15pt, medium gray, below main label
- **Optional:** Subtle vertical line after Step 3 and Step 6 to visually separate pipeline sections (pale divider line)

**Typography Hierarchy:**
- Step labels largest (28pt)
- Descriptions smallest (15pt)
- All sans-serif, thin weight for clinical precision

---

### Section 3: Two-Tier Output & Metrics (35%–85% of canvas)

This section is divided into 3 columns of equal width.

#### **Column A: TIER-1 Verdict (Internal Coherence)**

**Section Title:** "TIER-1: Internal Coherence" (26pt, bold, dark gray)

**Three Verdict Boxes** (vertically stacked, each 60px height):

1. **INTERNALLY CONSISTENT** (top box)
   - Left indicator: 30px circle filled green #2E965F
   - Text: "INTERNALLY CONSISTENT" (20pt, dark gray)
   - Border: 2px green outline, 4px padding
   - Interpretation: Non-noise fraction > 66%

2. **MARGINAL** (middle box)
   - Left indicator: 30px circle filled amber #DC8C19
   - Text: "MARGINAL" (20pt, dark gray)
   - Border: 2px amber outline, 4px padding
   - Interpretation: Non-noise fraction 40–66%

3. **FRAGMENTED** (bottom box)
   - Left indicator: 30px circle filled red #C8323C
   - Text: "FRAGMENTED" (20pt, dark gray)
   - Border: 2px red outline, 4px padding
   - Interpretation: Non-noise fraction < 40%

**Spacing:** 20px between boxes

---

#### **Column B: TIER-2 Verdict (Cross-RRP Analogies)**

**Section Title:** "TIER-2: Cross-RRP Analogies" (26pt, bold, dark gray)

**Three Verdict Boxes** (same style as Tier-1):

1. **WELL-INTEGRATED** (top)
   - Indicator: 30px circle, green #2E965F
   - Text: "WELL-INTEGRATED" (20pt)
   - Border: 2px green
   - Interpretation: > 75% entry reach, similarity > 0.75

2. **PARTIAL** (middle)
   - Indicator: 30px circle, amber #DC8C19
   - Text: "PARTIAL" (20pt)
   - Border: 2px amber
   - Interpretation: 40–75% reach, 0.55–0.75 similarity

3. **ISOLATED** (bottom)
   - Indicator: 30px circle, red #C8323C
   - Text: "ISOLATED" (20pt)
   - Border: 2px red
   - Interpretation: < 40% reach, < 0.55 similarity

---

#### **Column C: PFD Score Scale**

**Section Title:** "PFD Score" (26pt, bold, dark gray)

**Score Visualization:**

- **Gradient Bar:** 300px width × 30px height
- **Color Spectrum:** Red (#C8323C) on left (0.0) → Green (#2E965F) on right (1.0)
- **Gradient Type:** Linear interpolation, pixel-by-pixel smooth transition
- **Scale Labels:**
  - Left: "0.0 (No Structure)" (15pt, medium gray, left-aligned)
  - Right: "1.0 (Perfect)" (15pt, medium gray, right-aligned)

**Example Marker:**
- Vertical line at 0.89 position (267px from left)
- Line color: Blue #19518F, 3px width
- Extends 10px above and below bar
- Label: "0.89 ✓" (20pt, blue, centered above line)

**Interpretation:** Combined Tier-1 + Tier-2 coherence score

---

### Section 4: Key Metrics & Cross-Dataset Example (50%–80% of canvas)

This section is divided into 2 columns.

#### **Column A: Key Metrics** (left half)

**Section Title:** "Key Metrics" (26pt, bold, dark gray)

**Four Metric Definitions** (vertically stacked):

1. **D_eff — Effective Dimensionality (network topology)**
   - Bullet: Small teal circle #008C9E (15px diameter)
   - Text: Full definition (18pt, dark gray, left-aligned)
   - Interpretation: Planar~2.0, modular~5–8, distributed~10+

2. **Noise Fraction — % of random vs. signal links**
   - Bullet: Teal circle
   - Text: Full definition (18pt)
   - Interpretation: Lower = more signal

3. **Entry Reach — % of dataset connected to analogies**
   - Bullet: Teal circle
   - Text: Full definition (18pt)
   - Interpretation: Higher = more bridges found

4. **Similarity Score — Cross-domain structural match (0.0–1.0)**
   - Bullet: Teal circle
   - Text: Full definition (18pt)
   - Interpretation: > 0.75 = strong analogy

**Spacing:** 40px between metrics
**Visual Emphasis:** Bullets create rhythm; text is calm

---

#### **Column B: Cross-Dataset Analogy Example** (right half)

**Section Title:** "Cross-Dataset Analogy" (26pt, bold, dark gray)

**Dataset Box 1** (left, 200px width):
- Border: 2px blue #19518F
- Padding: 15px
- Content:
  - Label: "Dataset 1:" (20pt, dark gray)
  - Name: "Metabolic Network" (18pt, medium gray)
  - Metric: "304 entries" (15pt, medium gray)
- Position: Upper left

**Bridge Arrow** (center, between boxes):
- Start: Right edge of Dataset 1
- End: Left edge of Dataset 2
- Arrow line: 3px, green #2E965F
- Length: 60px
- Label above arrow: "Bridge" (15pt, green)
- Arrowhead: Triangle pointing right

**Dataset Box 2** (right, 200px width):
- Border: 2px blue #19518F
- Padding: 15px
- Content:
  - Label: "Dataset 2:" (20pt, dark gray)
  - Name: "Power Grid" (18pt, medium gray)
  - Metric: "171 entries" (15pt, medium gray)
- Position: Upper right

**Bridge Result** (below both boxes, centered):
- Line 1: "23 structural analogies found" (20pt, green #2E965F, bold)
- Line 2: "Hub topology similarity: 0.87" (18pt, blue #19518F)

**Visual Flow:** Horizontal analogy discovery (left dataset → bridge → right dataset → results below)

---

### Section 5: Footer (Bottom 5%)

**Divider Line:** Horizontal rule (2px, light gray #C8C8C8) spanning width with 20px margin

**Supported Domains Line:**
- Text: "Biochemistry  •  Electrical Engineering  •  Taxonomy  •  Chemistry  •  Knowledge Graphs  •  Bioinformatics"
- Font: 18pt, medium gray #787878
- Alignment: Centered
- Bullet separator: " • " (white space around bullets)

**Purpose:** Communicate domain breadth at a glance

---

## Color Palette

| Purpose | Color | Hex | RGB |
|---------|-------|-----|-----|
| Pipeline/Input | Teal | #008C9E | (0, 140, 158) |
| Secondary analytical | Blue | #19518F | (25, 85, 145) |
| Success/Consistent | Green | #2E965F | (46, 150, 95) |
| Marginal/Caution | Amber | #DC8C19 | (220, 140, 25) |
| Fragmented/Warning | Red | #C8323C | (200, 50, 60) |
| Divider lines | Light Gray | #C8C8C8 | (200, 200, 200) |
| Secondary text | Medium Gray | #787878 | (120, 120, 120) |
| Primary text | Dark Gray | #3C3C3C | (60, 60, 60) |
| Background | Off-white | #FAFAFA | (250, 250, 250) |

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Main Title | Sans-serif (Arial/Helvetica) | 72pt | Bold | Dark Gray #3C3C3C |
| Tagline | Sans-serif | 32pt | Regular | Medium Gray #787878 |
| Section Title | Sans-serif | 26pt | Bold | Dark Gray #3C3C3C |
| Step Labels | Sans-serif | 28pt | Regular | Dark Gray |
| Verdict Text | Sans-serif | 20pt | Regular | Dark Gray |
| Metric Definitions | Sans-serif | 18pt | Regular | Dark Gray |
| Sublabels | Sans-serif | 15pt | Regular | Medium Gray |
| Footer text | Sans-serif | 18pt | Regular | Medium Gray |

**Design Principle:** Thin weights for precision, minimal hierarchy, emphasize whitespace over decoration

---

## Spatial Layout & Margins

- **Canvas:** 2560×1440 pixels (4K, 16:9)
- **Margins:** 40px on all sides
- **Usable Width:** 2480px
- **Section Spacing:** 60px vertical between major sections
- **Column Spacing:** 80px between 3-column sections
- **Element Padding:** 15–20px internal padding for boxes

---

## Data Examples & Realistic Values

### Example 1: E. coli Metabolic Network
- Tier-1: INTERNALLY CONSISTENT (81.3% coherence)
- Tier-2: WELL-INTEGRATED (100% entry reach, 0.89 bridge quality)
- PFD Score: 0.94
- D_eff: 11.2
- Noise: 7.8%

### Example 2: IEEE Power Grid (Case 14)
- Tier-1: INTERNALLY CONSISTENT (66.7% coherence)
- Tier-2: WELL-INTEGRATED (100% entry reach, 0.87 similarity)
- PFD Score: 0.83
- D_eff: 1.75 (planar network)
- Noise: 12.4%

### Example 3: Hypothetical Noisy Data
- Tier-1: FRAGMENTED (35% coherence)
- Tier-2: ISOLATED (40% reach, 0.45 similarity)
- PFD Score: 0.40
- D_eff: 0.8
- Noise: 65%

---

## Design Philosophy: "Structural Revelation"

The infographic should embody:

1. **Systematic Observation**
   - Visual language of scientific diagrams
   - Precision and intentionality in every placement
   - No decorative elements; all visual choices communicate meaning

2. **Expert Craftsmanship**
   - Every alignment pixel-perfect
   - Color transitions smooth and carefully calibrated
   - Typography breathes; text is never crowded
   - Final result looks like it took countless hours of refinement

3. **Visual Clarity**
   - Information organized by spatial proximity
   - Color encodes meaning (teal=process, green=success, red=warning)
   - Generous whitespace allows eyes to rest and process
   - Left-to-right, top-to-bottom reading flow

4. **Scientific Authority**
   - Suggests the invisible can be mapped and understood
   - Uses analytical visual language (diagrams, metrics, gradients)
   - Treats abstract concepts (coherence, topology) with rigor

---

## Quality Standards

- **Resolution:** 2560×1440 pixels minimum (4K)
- **File Format:** PNG (lossless, transparent background if applicable) or PDF (vector preferred)
- **Color Accuracy:** Consistent across all elements, no gradation artifacts
- **Typography:** Crisp, anti-aliased, no pixelation at any size
- **Alignment:** All text and shapes pixel-perfect (no sub-pixel fuzzing)
- **Print-Ready:** Should be suitable for high-quality printing at 300 DPI
- **Accessibility:** High contrast ratios (WCAG AA minimum), clear labels

---

## Variations & Future Extensions

### Potential Alternative Layouts
1. **Vertical Flow:** Stack the 6 steps vertically if horizontal space is constrained
2. **Multi-Page:** Expand to 2–3 pages with detailed metric explanations and domain examples
3. **Interactive Web Version:** SVG-based with hover tooltips for each section

### Content Additions (Phase 3+)
- Add Phase 3 (Claim Validation) step to pipeline
- Include formal axiom symbols
- Add formal logic layer verdict boxes
- Expand example use cases

---

## Technical Implementation Notes

- **Tool Options:** Adobe Illustrator (vector), Figma (collaborative), PIL/Pillow (programmatic Python)
- **Export:** Save at 2560×1440 PNG; also export as PDF for printing
- **Version Control:** Store source file + exported PNG in `docs/design_assets/`
- **Accessibility Alt-Text:**
  ```
  PFD Workflow: 6-step pipeline (Ingest→Build Graph→Diagnose Internal→Build Bridge→Diagnose Bridge→Generate Report)
  producing Tier-1 verdict (Internally Consistent/Marginal/Fragmented) and Tier-2 verdict (Well-Integrated/Partial/Isolated)
  resulting in PFD Score 0.0–1.0. Metrics: D_eff, Noise, Entry Reach, Similarity. Example: Metabolic Network (304 entries)
  bridges to Power Grid (171 entries) with 23 analogies and 0.87 similarity.
  ```

---

## Acceptance Criteria

✅ Infographic communicates the complete 6-step workflow without ambiguity
✅ Tier-1 and Tier-2 verdicts are clearly differentiated
✅ Color coding creates instant visual meaning (green=good, amber=caution, red=warning)
✅ Key metrics are visible and well-explained
✅ Cross-dataset example is concrete and realistic
✅ Supported domains are listed
✅ Design embodies "Structural Revelation" philosophy
✅ Professional enough for GitHub, conference presentations, academic papers
✅ Readable at multiple scales (full-page printed, thumbnail on GitHub, social media)
✅ No jargon unexplained; accessible to researchers outside PFD

---

**Last Updated:** 2026-03-11
**Design Owner:** Ian Darling
**Philosophy Reference:** [docs/design_philosophy/STRUCTURAL_REVELATION.md](docs/design_philosophy/STRUCTURAL_REVELATION.md)
