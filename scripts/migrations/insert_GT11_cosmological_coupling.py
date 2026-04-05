"""
Insert GT11: Cosmological Coupling (Farrah-Croker)

BH mass evolution M(a) = M(a_i)(a/a_i)^k where k = -3P/rho.
Vacuum energy interior (P = -rho) gives k = 3.

STATUS: Tier 2 †  (contested)

Supporting evidence:
  - Farrah et al. 2023: k = 3.11 +/- 1.19 from elliptical galaxy SMBHs
  - DESI BAO recovery with 2 fewer parameters (Croker 2024)
  - H0 = 69.94 +/- 0.81, reducing Hubble tension to 2.7 sigma
  - Positive neutrino masses from DESI DR2

Challenging evidence:
  - GW merger rates reject k = 3 beyond 5 sigma (Amendola 2024)
  - Gaia BH1/BH2: 6.9% probability of forming above TOV under k = 3
  - Cadoni 2023: generic nonsingular GR interiors give k = 1, not 3
  - EP/momentum conservation critique (Avelino 2023)
  - Least-action derivation challenge (Wang & Wang 2023)
  - JWST AGN tension at 95% CL (Lei 2024)
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRY = {
    "id": "GT11",
    "title": "GT11: Cosmological Coupling (Farrah-Croker)",
    "filename": "GT11_cosmological_coupling.md",
    "entry_type": "reference_law",
    "scale": "cosmological",
    "domain": "physics",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "GT",
    "authoring_status": "",
    "formality_tier": 2,
}

SECTIONS = [
    (0, "What It Claims",
     "Croker and Weiner (2019) showed that within GR, if black holes possess realistic "
     "non-singular interiors, their gravitating mass can increase with the expansion of "
     "the universe independently of accretion or mergers. The mass evolution is "
     "M(a) = M(a_i)(a/a_i)^k, where a is the cosmological scale factor, a_i is the "
     "scale factor at formation, and k = -3P/rho depends on the interior equation of "
     "state. For a vacuum energy interior (P = -rho, de Sitter), k = 3 and the BH "
     "population maintains constant comoving energy density — mimicking a cosmological "
     "constant.\n\n"
     "SUPPORTING EVIDENCE: Farrah et al. (ApJ 944 L31, 2023) measured k = 3.11 +/- 1.19 "
     "from SMBH masses in elliptical galaxies over 0 < z < 2.5, excluding k = 0 at "
     "99.98% confidence. Croker et al. (2024) showed the CCBH model recovers DESI BAO "
     "evolving dark energy with 2 fewer parameters than w0wa-CDM, yielding H0 = 69.94 "
     "+/- 0.81 km/s/Mpc (reducing Hubble tension to 2.7 sigma). DESI DR2 analysis "
     "(2025) yields positive neutrino masses where standard Lambda-CDM gives unphysical "
     "negative values.\n\n"
     "CHALLENGING EVIDENCE: Amendola et al. (MNRAS 528, 2377, 2024) showed GW merger "
     "rates reject k = 3 beyond 5 sigma — predicted merger rates exceed LIGO-Virgo-KAGRA "
     "observations by two orders of magnitude. Andrae et al. (A&A, 2023) found Gaia "
     "BH1/BH2 have only 6.9% combined probability of forming above the TOV limit under "
     "k = 3. Cadoni et al. (JCAP, 2023) showed generic nonsingular GR interiors give "
     "k = 1, not k = 3 — the k = 3 case requires a very specific (gravastar-like) "
     "interior. The EP/momentum conservation critique (Avelino 2023), the least-action "
     "derivation challenge (Wang & Wang 2023), and JWST high-z AGN tension at 95% CL "
     "(Lei et al. 2024) further constrain the hypothesis."),

    (1, "Mathematical Form",
     "Cosmological coupling:\n"
     "  M(a) = M(a_i) * (a/a_i)^k\n\n"
     "Coupling constant from interior EoS:\n"
     "  k = -3P/rho  (P = interior pressure, rho = energy density)\n\n"
     "Special cases:\n"
     "  k = 0: No coupling (Schwarzschild singularity, standard GR)\n"
     "  k = 1: Comoving scaling (generic nonsingular, Cadoni et al.)\n"
     "  k = 3: Constant comoving energy density (de Sitter interior, w = -1)\n\n"
     "Dark energy equivalence (k = 3):\n"
     "  rho_BH(a) = rho_BH(a_i) * (a/a_i)^0 = const  (comoving)\n"
     "  Effective equation of state: w_eff = -1  (cosmological constant)\n\n"
     "Measurement (Farrah et al. 2023):\n"
     "  k = 3.11 +/- 1.19  (elliptical galaxy SMBHs, 0 < z < 2.5)\n"
     "  k = 0 excluded at 99.98% confidence (3.9 sigma)\n\n"
     "Constraints:\n"
     "  LVK GW data: k < 2.1 (2-sigma, standard), k < 1.1 (CCBH-corrected)\n"
     "  Gaia BH1/BH2: P(both above TOV | k=3) = 6.9%"),

    (2, "Constraint Category",
     "Thermodynamic-Geometric (Th-Gm): The coupling arises from matching interior "
     "and exterior solutions of the Einstein field equations in an expanding background. "
     "The interior EoS determines the coupling strength k. The constraint is geometric "
     "(junction conditions at the horizon) with thermodynamic content (the EoS determines "
     "the effective dark energy contribution). Status: contested — supporting cosmological "
     "evidence vs severe GW and stellar-mass BH constraints."),

    (3, "DS Cross-References",
     "GT01 (Jacobson Thermodynamic Derivation — the coupling arises within GR for "
     "non-singular interiors; Jacobson's framework provides the thermodynamic "
     "interpretation of the Einstein equations that govern the junction conditions). "
     "HB01 (Bekenstein Bound — maximum information density S <= A/4; saturation at "
     "the horizon is proposed as the trigger distinguishing coupled from uncoupled "
     "objects). "
     "HB02 (Bekenstein-Hawking Entropy — S = A/4 saturates the Bekenstein bound at the "
     "horizon; the coupling mechanism activates when this saturation is reached). "
     "GT09 (Choptuik Critical Collapse — Choptuik describes the BH formation threshold; "
     "cosmological coupling describes the post-formation mass evolution). "
     "HB10 (Hawking-Page Transition — both are BH phase transitions; Hawking-Page is "
     "first-order in AdS, cosmological coupling is proposed as continuous in FRW "
     "background)."),

    (4, "Mathematical Archetype",
     "Mathematical archetype: dimensional-scaling\n\n"
     "The mass-scale factor relation M ~ a^k is a power-law scaling where the exponent "
     "k encodes the interior physics. Different values of k correspond to different "
     "universality classes of BH interior: k = 0 (singular, no scaling), k = 1 (generic "
     "nonsingular, comoving), k = 3 (vacuum energy, cosmological constant). The scaling "
     "exponent k plays the same structural role as a critical exponent in statistical "
     "mechanics — it classifies the macroscopic behavior without specifying microscopic "
     "details."),

    (5, "What The Math Says",
     "In standard GR, a Schwarzschild black hole has constant mass forever — its mass "
     "at formation is its mass for eternity (k = 0). But Schwarzschild has a singularity, "
     "and singularities are unphysical. If the interior is replaced with something "
     "non-singular (a de Sitter core, a gravastar, a Bardeen black hole), the junction "
     "conditions between interior and exterior in an expanding FRW universe allow the "
     "mass to evolve with the scale factor. The rate of evolution depends on the interior "
     "pressure-to-density ratio: k = -3P/rho. For a vacuum energy interior where "
     "P = -rho, you get k = 3. If all BHs have k = 3, their total energy density "
     "stays constant as the universe expands — exactly like a cosmological constant. "
     "Farrah et al. measured this in elliptical galaxies (gas-poor, minimal accretion) "
     "and found k consistent with 3. The DESI BAO data showing evolving dark energy can "
     "be explained by the cosmic BH formation rate (peaking at z ~ 2) rather than a "
     "time-varying cosmological constant. However, GW data severely constrain k > 2 "
     "for stellar-mass BHs, and Cadoni et al. showed that the most natural nonsingular "
     "interiors give k = 1, not 3. The hypothesis remains actively contested."),

    (6, "Concept Tags",
     "• cosmological coupling\n"
     "• Farrah-Croker\n"
     "• black hole mass evolution\n"
     "• scale factor coupling\n"
     "• k = -3P/rho\n"
     "• de Sitter interior\n"
     "• dark energy from black holes\n"
     "• DESI BAO\n"
     "• Hubble tension\n"
     "• gravastar\n"
     "• non-singular black hole\n"
     "• GW constraints\n"
     "• Gaia BH constraints\n"
     "• Cadoni k=1\n"
     "• equivalence principle debate"),
]

PROPERTIES = [
    ("DS Facets", "Constraint Category", "Th-Gm", 0),
    ("entries", "concept_tags", "cosmological coupling, Farrah-Croker, BH mass evolution, dark energy from black holes, DESI, Hubble tension, GW constraints", 0),
    ("DS Facets", "mathematical_archetype", "dimensional-scaling", 1),
    ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
]

LINKS = [
    ("GT11", "GT01", "derives from", "2",
     "Coupling arises within GR for non-singular interiors; Jacobson's framework "
     "provides the thermodynamic interpretation of the junction conditions"),
    ("GT11", "HB01", "couples to", "2",
     "Bekenstein bound sets maximum information density; saturation at the horizon "
     "is the proposed trigger for cosmological coupling activation"),
    ("GT11", "HB02", "couples to", "2",
     "BH entropy S = A/4 saturates the Bekenstein bound; the coupling mechanism "
     "activates when this saturation is reached at horizon formation"),
    ("GT11", "GT09", "couples to", "2",
     "Choptuik critical collapse describes the BH formation threshold; cosmological "
     "coupling describes the post-formation mass evolution with scale factor"),
    ("GT11", "HB10", "analogous to", "2",
     "Both are BH phase transitions; Hawking-Page is first-order in AdS, cosmological "
     "coupling is proposed as continuous in expanding FRW background"),
]


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    labels = {r[0]: r[1] for r in cur.execute("SELECT id, title FROM entries")}

    existing = cur.execute("SELECT id FROM entries WHERE id = ?", (ENTRY["id"],)).fetchone()
    if existing:
        print(f"  SKIP (exists): {ENTRY['id']}")
        conn.close()
        return

    cur.execute(
        """INSERT INTO entries
           (id, title, filename, entry_type, scale, domain, status, confidence,
            type_group, authoring_status, formality_tier)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (ENTRY["id"], ENTRY["title"], ENTRY["filename"], ENTRY["entry_type"],
         ENTRY["scale"], ENTRY["domain"], ENTRY["status"], ENTRY["confidence"],
         ENTRY["type_group"], ENTRY["authoring_status"], ENTRY["formality_tier"])
    )
    print(f"  Inserted entry: {ENTRY['id']} — {ENTRY['title']}")

    for order, name, content in SECTIONS:
        cur.execute(
            "INSERT INTO sections (entry_id, section_name, section_order, content) "
            "VALUES (?, ?, ?, ?)",
            (ENTRY["id"], name, order, content)
        )
        print(f"    Section [{order}]: {name} ({len(content)} chars)")

    for tname, pname, pval, pord in PROPERTIES:
        cur.execute(
            "INSERT OR IGNORE INTO entry_properties "
            "(entry_id, table_name, property_name, property_value, prop_order) "
            "VALUES (?, ?, ?, ?, ?)",
            (ENTRY["id"], tname, pname, pval, pord)
        )
    print(f"    Properties: {len(PROPERTIES)} inserted")

    labels[ENTRY["id"]] = ENTRY["title"]

    for src, tgt, lt, tier, desc in LINKS:
        src_label = labels.get(src, src)
        tgt_label = labels.get(tgt, tgt)
        cur.execute(
            "INSERT OR IGNORE INTO links "
            "(link_type, source_id, source_label, target_id, target_label, description, link_order, confidence_tier) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (lt, src, src_label, tgt, tgt_label, desc, 0, tier)
        )
        print(f"  Link: {src} -> {tgt} ({lt})")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    print(f"Inserting GT11 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
