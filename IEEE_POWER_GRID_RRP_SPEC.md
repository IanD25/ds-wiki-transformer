# IEEE Power Grid Test Systems — RRP Ingestion Spec

**Version:** 1.0 | **Date:** 2026-03-11 | **Status:** Ready for implementation
**Phase:** 2 (RRP Ingestion) | **Parser Target:** Phase 2 Task 3
**Why:** Planar graph with known D_eff=2 validation; ground truth for spatial dimensionality

---

## 1. What We're Ingesting

IEEE standard power grid test cases used across electrical engineering research. Nodes = buses (substations/junctions), edges = transmission lines (with impedance/capacity). Known planar geometry (2D geographic layout).

**Test Systems (increasing complexity):**

| Name | Buses | Lines | Generators | Voltage Levels | D_eff Expected | Use Case |
|------|-------|-------|-----------|---|---|---|
| **IEEE-14** | 14 | 20 | 5 | 2 | 2 | Pedagogical minimal case |
| **IEEE-57** | 57 | 80 | 7 | 3 | 2 | Small practical system |
| **IEEE-118** | 118 | 186 | 54 | 3 | 2 | Gold-standard medium case |
| **IEEE-300** | 300 | 411 | 69 | 3 | 2 | Large real-world proxy |

All return D_eff ≈ 2 because power grids are approximately 2D (geographic layout). Critical hubs (high-degree nodes) should show **isotropic** regime (multiple independent load paths). Leaf nodes should show **radial-dominated** (single-path dependency).

---

## 2. Data Sources & Acquisition

### Source 1: MATPOWER (Official, easiest)
**URL:** `https://matpower.org/`
**Format:** MATLAB `.m` files, but modern MATPOWER includes JSON export
**Data:** All four IEEE test systems included in standard distribution

```bash
# Clone MATPOWER
git clone https://github.com/MATPOWER/matpower.git
cd matpower/data
# IEEE cases are: case14.m, case57.m, case118.m, case300.m
```

**Pros:**
- Authoritative source (from MATPOWER developers)
- Can generate JSON directly from MATLAB or Python parser
- Well-documented power flow data structure

**Cons:**
- MATLAB `.m` format requires parsing (non-standard, but straightforward)

### Source 2: PyPower / pandapower (Python, batteries-included)
**URL:** `https://pandapower.readthedocs.io/`
**Install:** `pip install pandapower`
**Data:** IEEE test cases built-in (no download needed)

```python
import pandapower as pp

# Load IEEE-14
net14 = pp.networks.case14()  # Returns pandapower.Network object
# Direct access to net14.bus, net14.line, net14.gen
```

**Pros:**
- Zero download/parse friction
- Native Python, can export to JSON directly
- Mature library with good documentation

**Cons:**
- Slightly less "canonical" than MATPOWER (but equivalent data)

### Source 3: NREL ReEDS / PSSE Data (Advanced)
Skip for Phase 2 — focus on IEEE standard cases first.

---

## 3. Data Format & Schema Mapping

### MATPOWER `.m` File Structure (Example: case14.m)

```matlab
function mpc = case14
% IEEE 14-bus test case
mpc.version = '2';
mpc.baseMVA = 100;

% Bus Data: [bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin]
mpc.bus = [
 1  3  0.0   0.0 0.0 0.0 1 1.060  0.0 345 1 1.06 0.94;
 2  2  21.7  12.7 0.0 0.0 1 1.045 -4.98 345 1 1.06 0.94;
 ...
];

% Line Data: [fbus tbus r x b rateA rateB rateC ratio angle status]
mpc.branch = [
 1  2  0.01938 0.05917 0.0528 0.0 0.0 0.0 0.0 0.0 1;
 1  5  0.05403 0.22304 0.0492 0.0 0.0 0.0 0.0 0.0 1;
 ...
];

% Generator Data: [bus Pg Qg Qmax Qmin Vg mBase status ...]
mpc.gen = [
 1  232.4 -16.9 10.0 0.0 1.06 100 1;
 ...
];
```

### RRP SQLite Schema Mapping

Map MATPOWER bus/line/gen data to standard RRP tables:

```sql
-- entries: one row per bus
INSERT INTO entries (id, title, entry_type, domain, status, type_group)
VALUES (
  'IEEE14_B1',  -- id: IEEE14_B<bus_number>
  'Bus 1 (Gen)',  -- title: Bus <number> (<type>)
  'instantiation',  -- all buses are instantiations (grid nodes)
  'engineering',
  'complete',
  'GRID'
);

-- sections: bus metadata
INSERT INTO sections (entry_id, section_name, content)
VALUES (
  'IEEE14_B1',
  'Bus Specification',
  'Bus Number: 1\nType: Generator (PV bus)\nNominal Voltage: 345 kV\nBase MVA: 100\nVm: 1.060 pu\nVa: 0.0°'
);

INSERT INTO sections (entry_id, section_name, content)
VALUES (
  'IEEE14_B1',
  'Electrical Parameters',
  'Real Power Load (Pd): 0.0 MW\nReactive Power Load (Qd): 0.0 Mvar\nShunt Conductance (Gs): 0.0 pu\nShunt Susceptance (Bs): 0.0 pu'
);

-- entry_properties: bus data as properties
INSERT INTO entry_properties (entry_id, property_name, property_value)
VALUES
  ('IEEE14_B1', 'voltage_magnitude', '1.060'),
  ('IEEE14_B1', 'voltage_angle_deg', '0.0'),
  ('IEEE14_B1', 'nominal_voltage_kv', '345'),
  ('IEEE14_B1', 'bus_type', 'generator'),
  ('IEEE14_B1', 'real_power_load_mw', '0.0'),
  ('IEEE14_B1', 'reactive_power_mvar', '0.0'),
  ('IEEE14_B1', 'shunt_g_pu', '0.0'),
  ('IEEE14_B1', 'shunt_b_pu', '0.0');

-- links: transmission lines (edges)
-- One link per line: source_id = from_bus, target_id = to_bus
INSERT INTO links (source_id, target_id, link_type, description, confidence_tier)
VALUES (
  'IEEE14_B1',
  'IEEE14_B2',
  'transmits_power_to',  -- or 'electrically_adjacent_to'
  'Transmission Line 1-2: R=0.01938 pu, X=0.05917 pu, B=0.0528 pu, Capacity=500 MVA',
  '1'  -- tier-1: topology is definitional (hard connection)
);
```

### Property Schema for Power Grid

```
Bus Properties (entry_properties):
  - voltage_magnitude_pu
  - voltage_angle_deg
  - bus_type (load | generator | slack)
  - nominal_voltage_kv
  - real_power_load_mw
  - reactive_power_mvar
  - shunt_conductance_pu
  - shunt_susceptance_pu
  - area_id
  - zone_id
  - max_voltage_pu
  - min_voltage_pu

Line Properties (links table — stored as link description):
  - series_resistance_pu
  - series_reactance_pu
  - shunt_susceptance_pu
  - mva_rating_a  (continuous rating)
  - mva_rating_b  (short-term rating)
  - mva_rating_c  (emergency rating)
  - tap_ratio
  - phase_shift_deg
  - line_status (in_service | out_of_service)

Generator Properties (separate entries for IEEE14_G1, etc.):
  - real_power_mw
  - reactive_power_mvar
  - max_reactive_mvar
  - min_reactive_mvar
  - voltage_setpoint_pu
```

---

## 4. Parser: `src/ingestion/parsers/ieee_power_grid_parser.py`

### High-Level Algorithm

```
Input:  MATPOWER .m file (or pandapower Network object)
Output: SQLite RRP bundle with schema matching above

Step 1: Parse MATPOWER .m file or load pandapower.Network
        Extract: mpc.bus, mpc.branch, mpc.gen

Step 2: Create RRP SQLite (or use existing ieee_<casename>.db)

Step 3: Ingest Bus Data
        For each bus row:
          - Create entry: id=IEEE<case>_B<bus_num>
          - Extract bus properties (voltage, type, loads, etc.)
          - Create 'Bus Specification' and 'Electrical Parameters' sections

Step 4: Ingest Generator Data
        For each gen row:
          - Create entry: id=IEEE<case>_G<gen_num>
          - Link to bus: G→B link with type 'supplies_power_to'
          - Extract gen properties

Step 5: Ingest Line (Transmission) Data
        For each branch row:
          - Create link: IEEE<case>_B<from> → IEEE<case>_B<to>
          - Type: 'transmits_power_to'
          - Store impedance/rating in link.description
          - confidence_tier: '1' (topological—hard connection)

Step 6: Verify & Finalize
        - All buses reachable? (check connectivity)
        - Degree distribution (identify hubs vs. leaves)
        - Summary: <N> buses, <E> lines, <G> generators
```

### Implementation Notes

**MATPOWER Parser (if using .m files):**
```python
def parse_matpower_case(filepath: str) -> dict:
    """
    Parse MATPOWER .m case file into Python dict.

    Naive approach: read .m file as text, extract matrix definitions.
    Regex to find: mpc.bus = [...]; mpc.branch = [...]; mpc.gen = [...];
    Convert to numpy arrays via eval() or ast.literal_eval().

    Alternative: Use MATPOWER's JSON export (modern versions support this).
    """
```

**pandapower approach (simpler):**
```python
import pandapower as pp

def load_ieee_case(case_name: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    case_name: 'case14', 'case57', 'case118', 'case300'
    Returns: (buses, lines, gens) as DataFrames.
    """
    net = getattr(pp.networks, case_name)()
    return net.bus, net.line, net.gen
```

**Recommendation:** Use pandapower (zero download friction, native Python DataFrames).

---

## 5. Expected RRP Output

After parsing `case14.m`:

```
data/rrp/ieee_power_grid/
├── raw/
│   ├── case14.m
│   ├── case57.m
│   ├── case118.m
│   └── case300.m
└── rrp_ieee_power_grid_case14.db
    ├── entries (14 buses + 5 gens = 19 entries)
    ├── sections (38 sections: 2 per bus + 1 per gen)
    ├── entry_properties (152 property rows: 8 per bus + 1 per line)
    ├── links (20 transmission lines)
    └── rrp_meta (case name, version, date_ingested)

Example row counts:
  entries:           19 (14 buses + 5 generators)
  sections:          38 (2 per bus + 1 per gen)
  links:             20 (one per transmission line)
  entry_properties:  152 (8 properties × 14 buses + 3 properties × 5 gens + line metadata)
```

---

## 6. D_eff Validation Expectations

### Hypothesis
Power grids are 2D (geographic layout). The Fisher Diagnostic Suite should return:
- **All non-leaf nodes:** D_eff = 2 (planar graph, 2D embedding)
- **Hub nodes (degree ≥ 4):** Isotropic regime (η ≈ 0.5), multiple independent directions
- **Leaf nodes (degree = 1):** Skipped (FIM requires degree ≥ 2)
- **Radial-dominated nodes (degree = 2):** η < 0.35 (single dominant path direction)

### Ground Truth Benchmark
```
IEEE-14:
  Node with max degree: Bus 4 (degree 4–5)
    Expected: D_eff = 2, regime = isotropic, η ≈ 0.45–0.55

IEEE-118:
  Hub buses (E.g., Bus 69 is a major junction):
    Expected: D_eff = 2, regime = isotropic, η ≈ 0.4–0.6
  Leaf buses (E.g., Bus 1 connected to 1 line):
    Expected: skipped (degree < 2)
```

### Test Assertion (for test_fisher_diagnostics.py)
```python
def test_ieee_14_bus4_is_isotropic():
    """Bus 4 (degree 4) in IEEE-14 should have D_eff=2, isotropic regime."""
    G = build_wiki_graph('data/rrp/ieee_power_grid/rrp_ieee_power_grid_case14.db')
    result = analyze_node(G, 'IEEE14_B4', KernelType.EXPONENTIAL)

    assert result.d_eff == 2, f"Expected D_eff=2, got {result.d_eff}"
    assert result.regime == RegimeType.ISOTROPIC, f"Expected isotropic, got {result.regime}"
    assert 0.35 < result.eta < 0.65, f"Expected η in [0.35, 0.65], got {result.eta}"
```

---

## 7. Integration with PFD

### After Ingestion
1. Run Pass 1.5 (entity catalog): identify key network patterns (central buses, loop structures, voltage collapse risks)
2. Run Pass 2b (cross-universe query): map power grid buses to DS Wiki entries
   - Expected bridges: EM entries (Maxwell equations), TD entries (energy conservation), CS entries (NP-hard optimization of unit commitment)
3. Run Fisher Diagnostic Suite: validate D_eff=2 hypothesis
4. Build visualization: network diagram with D_eff/regime colors

### DS Wiki Connections
- **EM1–EM13** (Electromagnetic): Faraday's Law, Ohm's Law, Maxwell equations
- **TD3** (Second Law): Energy conservation in power systems
- **CS4, CS8** (Computational): Unit commitment is NP-hard; Amdahl's Law applies to grid simulation
- **H2** (Fractal Dimension): Power grid topology research often studies fractal properties

---

## 8. Implementation Checklist

```
[ ] A1. Choose source: pandapower (recommended) vs. MATPOWER .m parsing
        pip install pandapower
        Verify: python -c "import pandapower; print(pandapower.networks.case14())"

[ ] A2. Write src/ingestion/parsers/ieee_power_grid_parser.py
        Functions:
          - load_case(case_name: str) → (buses_df, lines_df, gens_df)
          - ingest_case_to_db(case_name, output_path) → None
          - validate_connectivity(G) → bool

[ ] A3. Create data/rrp/ieee_power_grid/raw/ directory
        Download or copy: case14.m, case57.m, case118.m, case300.m

[ ] A4. Run parser on case14 (smallest, fastest)
        python -c "
from src.ingestion.parsers.ieee_power_grid_parser import ingest_case_to_db
ingest_case_to_db('case14', 'data/rrp/ieee_power_grid/rrp_ieee_power_grid_case14.db')
"
        Expected output: db with 19 entries, 20 links

[ ] A5. Verify schema matches RRP standard (check with sqlite3)
        SELECT COUNT(*) FROM entries;  -- expect 19
        SELECT COUNT(*) FROM links;    -- expect 20

[ ] B1. Run Pass 1.5 on case14
        python scripts/run_entity_catalog_pass.py \
            data/rrp/ieee_power_grid/rrp_ieee_power_grid_case14.db \
            data/chroma_db \
            data/ds_wiki.db

[ ] B2. Run Pass 2b (cross-universe bridges)
        Note: analyze results for EM / TD / CS connections

[ ] C1. Run Fisher Diagnostic Suite on case14
        python scripts/run_fisher_suite.py --mode rrp_bundle \
            --rrp data/rrp/ieee_power_grid/rrp_ieee_power_grid_case14.db

[ ] C2. Validate: check that high-degree buses return D_eff=2, isotropic

[ ] D1. Repeat for case57, case118 (case300 optional for Phase 2)

[ ] E1. Add test: test_fisher_diagnostics.py TestIEEEPowerGrid class
        - Test D_eff=2 for each case
        - Test hub nodes are isotropic
        - Test leaf nodes are skipped

[ ] F1. Commit: "[Phase 2] Add IEEE power grid RRP (case14, case57, case118)"

[ ] G1. (Optional) Add visualization: power network diagram with D_eff heatmap
```

---

## 9. Timeline & Complexity

| Task | Effort | Estimated Time |
|------|--------|---|
| A1–A2: Parser | Low | 30–45 min |
| A3–A5: Ingest case14 | Low | 10 min |
| B1–B2: Pass 1.5 + Pass 2b | Medium (dependent on other passes) | 20 min |
| C1–C2: Fisher Suite + validation | Medium | 15 min |
| D1: Repeat for larger cases | Low (copy-paste) | 5 min |
| E1–F1: Tests + commit | Low | 20 min |
| **Total** | — | **~100–120 min** |

---

## 10. Rationale: Why IEEE Power Grid Now

1. **D_eff ground truth:** Planar graph → guaranteed D_eff=2. This validates the Fisher Suite on a new system class (not lattices, not random graphs).

2. **Engineering relevance:** Power grids are critical infrastructure. Showing D_eff can identify structural vulnerabilities (e.g., buses with D_eff=1 or η→1 are fragile) adds practical value to PFD.

3. **Low friction:** pandapower makes data acquisition + parsing a 1-hour task (no external downloads, no format pain).

4. **DS Wiki bridges:** EM / TD / CS connections are predictable, should yield clean Pass 2 results.

5. **Scales elegantly:** case14 is minimal validation, case118 is industry standard, case300 tests scalability.

---

*This spec makes IEEE power grid the second RRP test case after the already-complete Zoo Classes, Periodic Table, and E. coli Core (in progress). It is a planar-graph ground-truth validation for the Fisher Diagnostic Suite and a practical engineering application of D_eff.*
