"""
Insert STAT3: Constrained Critical Attractor (CCA) Class

A structural universality class defined by 5 features:
  1. Ambient phase space with many possible configurations
  2. Non-local constraint forbids most configurations
  3. Accessible attractor is a critical manifold of dimension < ambient
  4. Dynamics or static structure holds system on manifold
  5. Deviation requires breaking the constraint itself

Known instances: Riemann zeros, SOC family, neural criticality, FDS State 2,
critical stat mech. Candidate: BH horizons (conjectural).

STATUS: Tier 2 † (novel framing — no prior literature unifies these systems
under a single structural definition)

SCOPE: Structural classification, NOT mechanism. No shared dynamics claimed.
No proof strategy for individual instances.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

ENTRY = {
    "id": "STAT3",
    "title": "STAT3: Constrained Critical Attractor (CCA) Class",
    "filename": "STAT3_constrained_critical_attractor.md",
    "entry_type": "reference_law",
    "scale": "cross-scale",
    "domain": "mathematics · physics",
    "status": "contested",
    "confidence": "Tier 2 †",
    "type_group": "STAT",
    "authoring_status": "",
    "formality_tier": 2,
}

SECTIONS = [
    (0, "What It Claims",
     "A system exhibits a constrained critical attractor (CCA) configuration when all "
     "five of the following hold: (1) It occupies an ambient phase space with many a "
     "priori possible configurations. (2) A higher-order, non-local constraint forbids "
     "most of those configurations. (3) The accessible attractor is a critical manifold "
     "of dimension strictly less than ambient. (4) Dynamics (for evolving systems) or "
     "static structure (for mathematical objects) hold the system on the manifold. "
     "(5) Deviation from the manifold would require breaking the constraint itself, "
     "which is not accessible through local perturbation of the system's degrees of "
     "freedom.\n\n"
     "Known instances: Riemann zeros (self-adjointness of conjectured Hilbert-Polya "
     "operator constrains zeros to Re(s) = 1/2 — dimensional reduction from the "
     "complex plane to a 1D line; Montgomery-Odlyzko GUE statistics confirmed "
     "numerically). SOC family (slow driving to absorbing-state critical points — "
     "Bak-Tang-Wiesenfeld 1987; note: SOC is a family of universality classes, not "
     "a single class; different SOC models fall into different classes including DP "
     "and RFIM). Neural criticality (STDP-driven tuning to branching ratio sigma = 1 "
     "— Beggs-Plenz 2003; contested as of 2025 Neuron review). Critical stat mech "
     "(RG flow to fixed points — Wilson, Kadanoff; the original and most general "
     "instance). Candidate: BH horizons (conjectural — see P23).\n\n"
     "SCOPE STATEMENT: This entry defines a structural classification, not a dynamical "
     "mechanism. It identifies structural isomorphism across systems without claiming "
     "a shared causal origin. No proof strategy is proposed for any instance (including "
     "the Riemann Hypothesis). Cross-domain transfer of specific results is NOT implied "
     "by class membership. The class is useful for organizing intuition, identifying "
     "candidate systems for cross-domain comparison, and naming the common structural "
     "feature that makes analogies across these systems precise rather than loose.\n\n"
     "Novel framing: No prior literature unifies these systems under a single structural "
     "definition. Closest precursor: arXiv:2601.22389 (convergent discovery of equivalent "
     "critical-phenomena measures across 6-12 domains, Jan 2026) — phenomenological "
     "cataloging without the structural 5-feature definition proposed here."),

    (1, "Mathematical Form",
     "CCA definitional features (all 5 required):\n\n"
     "  F1. Ambient space: dim(Omega) >> dim(A)\n"
     "      Omega = full configuration/phase space\n"
     "      A = accessible attractor manifold\n\n"
     "  F2. Non-local constraint C:\n"
     "      C restricts Omega to A where dim(A) < dim(Omega)\n"
     "      C cannot be decomposed into local constraints\n\n"
     "  F3. Critical manifold:\n"
     "      A is a critical surface (fixed point, critical line, etc.)\n"
     "      System exhibits scale invariance / divergent correlation on A\n\n"
     "  F4. Holding mechanism:\n"
     "      Dynamics d/dt x = f(x) has A as an attractor  (evolving systems)\n"
     "      OR: static structure determines position on A  (mathematical objects)\n\n"
     "  F5. Robustness:\n"
     "      Perturbation delta_x with |delta_x| < epsilon returns to A\n"
     "      Only breaking C itself (producing a different system) moves off A\n\n"
     "Instance table:\n\n"
     "  Riemann zeros:\n"
     "    Omega = critical strip 0 < Re(s) < 1  (2D)\n"
     "    C = self-adjointness of Hilbert-Polya operator  (non-local)\n"
     "    A = critical line Re(s) = 1/2  (1D)\n\n"
     "  SOC (Bak-Tang-Wiesenfeld family):\n"
     "    Omega = high-dim population/resource space\n"
     "    C = conservation + slow driving to absorbing state\n"
     "    A = marginal stability manifold (critical point of absorbing transition)\n\n"
     "  FDS State 2:\n"
     "    Omega = full singular value (SV) space\n"
     "    C = kernel + two-scale commensurability + anisotropy change\n"
     "    A = SV2 = SV1 saddle plane\n"
     "    Diagnostic: SV2/SV1 = 1.000 (2D Ising) vs 0.374 (Potts q=10)\n\n"
     "  Critical stat mech:\n"
     "    Omega = thermodynamic state space\n"
     "    C = Hamiltonian + scaling symmetry\n"
     "    A = critical surface (RG fixed point)"),

    (2, "Constraint Category",
     "Cross-domain structural (Str): The CCA class is defined by structural features "
     "shared across domains, not by a specific physical mechanism. The constraint is "
     "non-local in every instance: self-adjointness is a property of the whole operator; "
     "conservation laws are global; scaling symmetry is global; Bekenstein saturation "
     "depends on the total mass/energy distribution. The dimensional reduction from "
     "ambient space to attractor manifold is the defining signature."),

    (3, "DS Cross-References",
     "D2 (Feigenbaum Universality — Feigenbaum universality is one instance of critical "
     "phenomena where universal scaling exponents emerge at a critical threshold; "
     "CCA generalises the structural pattern across domains). "
     "STAT1 (Maximum Entropy Principle — MaxEnt provides the constraint framework; "
     "CCA instances are systems where non-local constraints force configurations onto "
     "critical manifolds, which can be understood as entropy-extremal surfaces). "
     "MATH6 (Prime Number Theorem — the Riemann zeros instance of CCA connects to "
     "number theory; PNT depends on the zero-free region of zeta, and CCA membership "
     "via Hilbert-Polya would constrain all zeros to Re(s) = 1/2). "
     "HB01 (Bekenstein Bound — Bekenstein saturation as a non-local constraint is "
     "the proposed mechanism for BH horizons as a candidate CCA instance). "
     "T5 (Critical Exponent-Dimension Sensitivity — tests whether CCA crossing "
     "produces universal D-dependent scaling; the CCA framework predicts that "
     "continuous transitions cross CCAs while first-order transitions do not)."),

    (4, "Mathematical Archetype",
     "Mathematical archetype: fixed-point\n\n"
     "The CCA is a fixed-point structure: the critical manifold A is an attractor "
     "of the dynamics (or a static structural feature) that systems are drawn to "
     "and held on. In RG language, the CCA is the critical surface containing the "
     "relevant fixed point(s). The robustness condition F5 means the system returns "
     "to the fixed point under perturbation — only changing the constraint itself "
     "(the Hamiltonian, the operator, the conservation law) can move the system off A. "
     "The FDS diagnostic SV2/SV1 -> 1.000 at continuous transitions is an empirical "
     "detector for CCA crossing within FDS scope."),

    (5, "What The Math Says",
     "Consider a system with many degrees of freedom — a lattice of spins, the zeros "
     "of a function, a population of interacting agents. In the absence of constraints, "
     "the system could occupy any point in its configuration space. But a non-local "
     "constraint — one that cannot be expressed as a sum of local terms — restricts the "
     "accessible configurations to a lower-dimensional manifold. If this manifold happens "
     "to be a critical surface (where the system exhibits scale invariance, divergent "
     "correlation lengths, or universal scaling), and if the system is dynamically "
     "attracted to and held on this surface, then the system is in a CCA configuration. "
     "The key distinction from ordinary critical phenomena is the robustness: in standard "
     "criticality, you tune a parameter (temperature) to reach the critical point. In a "
     "CCA, the constraint itself forces the system to the critical surface without tuning "
     "— the system has no choice but to be critical. The FDS empirical result provides "
     "the sharpest diagnostic: continuous phase transitions (2D Ising, 3D Ising) cross "
     "the CCA surface (SV2/SV1 = 1.000 and 0.956), while first-order transitions "
     "(Potts q=10, SV2/SV1 = 0.374) do not. This suggests that the CCA is specifically "
     "the structure that distinguishes continuous from first-order transitions — an "
     "empirical claim, not a proof."),

    (6, "Concept Tags",
     "• constrained critical attractor\n"
     "• CCA class\n"
     "• structural universality\n"
     "• non-local constraint\n"
     "• dimensional reduction\n"
     "• critical manifold\n"
     "• Riemann zeros\n"
     "• Hilbert-Polya conjecture\n"
     "• Montgomery-Odlyzko\n"
     "• self-organized criticality\n"
     "• Bak-Tang-Wiesenfeld\n"
     "• neural criticality\n"
     "• Beggs-Plenz\n"
     "• FDS State 2\n"
     "• SV2/SV1 diagnostic\n"
     "• RG fixed point\n"
     "• Wilson-Kadanoff\n"
     "• continuous vs first-order transitions\n"
     "• cross-domain critical phenomena"),
]

PROPERTIES = [
    ("DS Facets", "Constraint Category", "Str", 0),
    ("entries", "concept_tags", "constrained critical attractor, CCA, structural universality, non-local constraint, dimensional reduction, critical manifold, Riemann zeros, SOC, neural criticality, FDS State 2", 0),
    ("DS Facets", "mathematical_archetype", "fixed-point", 1),
    ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
]

LINKS = [
    ("STAT3", "D2", "analogous to", "2",
     "Feigenbaum universality is one instance of critical phenomena; CCA class "
     "generalises the structural pattern of universal scaling at critical thresholds"),
    ("STAT3", "STAT1", "derives from", "2",
     "Maximum entropy principle provides the constraint framework; CCA instances are "
     "systems where non-local constraints force configurations onto critical manifolds"),
    ("STAT3", "MATH6", "couples to", "2",
     "Riemann zeros as CCA instance connects to number theory via Hilbert-Polya "
     "self-adjointness constraint; PNT depends on zero-free region of zeta"),
    ("STAT3", "HB01", "couples to", "2",
     "Bekenstein bound as non-local constraint is the proposed mechanism for BH "
     "horizons as a candidate CCA instance (conjectural)"),
    ("STAT3", "T5", "analogous to", "2",
     "Critical exponent dimension sensitivity tests whether CCA crossing produces "
     "universal D-dependent scaling; CCA predicts continuous transitions cross CCAs"),
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
    print(f"Inserting STAT3 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
