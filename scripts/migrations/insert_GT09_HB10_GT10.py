"""
Insert three Tier 1 established reference law entries:

  GT09: Choptuik Critical Collapse (1993)
        Universal scaling at BH formation threshold. M ~ |p - p*|^gamma with
        gamma ≈ 0.37. Discrete self-similarity. Critical solution is an
        intermediate attractor with one unstable mode.

  HB10: Hawking-Page Transition (1983)
        First-order phase transition between thermal radiation in AdS and large
        Schwarzschild-AdS BH. Maps to confinement/deconfinement via AdS/CFT.

  GT10: Jacobson Entanglement Equilibrium (2016)
        Einstein equation from maximal vacuum entanglement entropy at fixed
        volume. Upgrades Jacobson 1995 (GT01) from classical thermodynamics
        to quantum entanglement.

All three are established physics — no controversy.
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

# ---------------------------------------------------------------------------
# Entry definitions
# ---------------------------------------------------------------------------

ENTRIES = [
    {
        "id": "GT09",
        "title": "GT09: Choptuik Critical Collapse",
        "filename": "GT09_choptuik_critical_collapse.md",
        "entry_type": "reference_law",
        "scale": "cosmological",
        "domain": "physics",
        "status": "established",
        "confidence": "Tier 1",
        "type_group": "GT",
        "authoring_status": "",
        "formality_tier": 1,
    },
    {
        "id": "HB10",
        "title": "HB10: Hawking-Page Transition",
        "filename": "HB10_hawking_page_transition.md",
        "entry_type": "reference_law",
        "scale": "cosmological",
        "domain": "physics",
        "status": "established",
        "confidence": "Tier 1",
        "type_group": "HB",
        "authoring_status": "",
        "formality_tier": 1,
    },
    {
        "id": "GT10",
        "title": "GT10: Jacobson Entanglement Equilibrium",
        "filename": "GT10_jacobson_entanglement_equilibrium.md",
        "entry_type": "reference_law",
        "scale": "cross-scale",
        "domain": "physics · information",
        "status": "established",
        "confidence": "Tier 1",
        "type_group": "GT",
        "authoring_status": "",
        "formality_tier": 1,
    },
]

# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------

SECTIONS = {
    "GT09": [
        (0, "What It Claims",
         "Choptuik (PRL 70, 9, 1993) discovered that the threshold of black hole "
         "formation in the space of initial data exhibits genuine critical phenomena: "
         "universality, power-law scaling of black hole mass, and discrete self-similarity. "
         "For a one-parameter family of initial data p, there exists a critical value p* "
         "such that for p < p* the field disperses and for p > p* a black hole forms. "
         "Near the threshold, the black hole mass scales as M ~ |p - p*|^gamma with a "
         "universal exponent gamma that depends only on the matter type, not the initial "
         "data family. For massless scalar fields, gamma = 0.374 +/- 0.001. The critical "
         "solution at p = p* is discretely self-similar with echoing period Delta = 3.44. "
         "Two types of critical collapse exist: Type II (mass continuous from zero, as "
         "described above) and Type I (mass gap — the smallest BH has finite mass, found "
         "in Einstein-Yang-Mills and other massive systems). The critical solution is an "
         "intermediate attractor in the space of initial data with exactly one unstable "
         "mode — a codimension-1 surface separating collapse from dispersal. "
         "Gundlach (Living Rev. Rel. 10, 5, 2007) provides the comprehensive review."),

        (1, "Mathematical Form",
         "Type II critical collapse (massless scalar field):\n"
         "  M ~ |p - p*|^gamma\n"
         "  gamma = 0.374 +/- 0.001 (massless scalar)\n"
         "  gamma = 0.356 +/- 0.001 (radiation fluid)\n"
         "  gamma = 0.119 +/- 0.001 (axion/massive scalar)\n\n"
         "Discrete self-similarity:\n"
         "  Z(r, t) = Z(e^Delta r, e^Delta t)\n"
         "  Delta = 3.44 (massless scalar)\n\n"
         "Critical solution structure:\n"
         "  One unstable mode (Lyapunov exponent lambda_1 > 0)\n"
         "  All other modes stable (lambda_i < 0 for i > 1)\n"
         "  gamma = 1/lambda_1 (universal exponent = inverse of unstable eigenvalue)\n\n"
         "Type I critical collapse:\n"
         "  M jumps from 0 to M_min > 0 at p = p*\n"
         "  Critical solution is a static or oscillating star (not self-similar)\n"
         "  Scaling: lifetime ~ -gamma * ln|p - p*|"),

        (2, "Constraint Category",
         "Geometric (Gm): The critical threshold is a codimension-1 surface in the space "
         "of initial data, determined by the Einstein field equations. The universality "
         "of the scaling exponent gamma — independent of initial data family — demonstrates "
         "that BH formation has the same structural character as a continuous phase "
         "transition: the critical solution is a fixed point of the RG-like scaling "
         "symmetry Z -> Z(e^Delta r, e^Delta t), and gamma is determined by the single "
         "unstable eigenvalue of this fixed point."),

        (3, "DS Cross-References",
         "GT01 (Jacobson Thermodynamic Derivation — critical collapse occurs within GR; "
         "Jacobson's entropy-area framework provides the thermodynamic interpretation of "
         "the formation threshold). "
         "HB02 (Bekenstein-Hawking Entropy — BH formation saturates S = A/4; Choptuik "
         "scaling describes how mass and therefore entropy approach zero continuously "
         "at the critical threshold in Type II collapse). "
         "HB06 (Black Hole Area Theorem — the area theorem dA/dt >= 0 governs post-formation "
         "evolution; Choptuik critical collapse governs the formation threshold itself). "
         "D2 (Feigenbaum Universality — both exhibit universal scaling exponents at critical "
         "thresholds; Choptuik gamma is the gravitational analog of Feigenbaum delta, "
         "with the critical solution playing the role of the period-doubling fixed point)."),

        (4, "Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "Choptuik critical collapse is the prototypical threshold transition in "
         "gravitational physics. The scaling M ~ |p - p*|^gamma has the same structure "
         "as the order parameter scaling |T - T_c|^beta in statistical mechanics: "
         "a power law with a universal exponent determined by the critical fixed point. "
         "The discrete self-similarity Z(r,t) = Z(e^Delta r, e^Delta t) is the analog "
         "of log-periodic corrections to scaling near the fixed point."),

        (5, "What The Math Says",
         "Consider a family of initial data for the Einstein-scalar field equations, "
         "parameterized by a single number p (e.g., the amplitude of a scalar field "
         "pulse). At low p, the field disperses to infinity. At high p, it collapses "
         "to form a black hole. At the critical value p*, the evolution approaches a "
         "universal critical solution that is discretely self-similar — it repeats "
         "itself on ever-smaller scales with period Delta in the logarithm of the "
         "spacetime scale. This critical solution has exactly one unstable direction "
         "in the space of all possible evolutions. A slight perturbation above p* "
         "sends the solution toward collapse; below p*, toward dispersal. The mass "
         "of the resulting black hole (for p slightly above p*) scales as a power "
         "law M ~ |p - p*|^gamma, where gamma is determined entirely by the unstable "
         "eigenvalue of the critical solution: gamma = 1/lambda_1. Different families "
         "of initial data all produce the same gamma — this is the universality. "
         "The critical exponent depends on the matter type (scalar, radiation, etc.) "
         "but not on the specific initial data family, exactly as critical exponents "
         "in statistical mechanics depend on universality class but not on microscopic "
         "details."),

        (6, "Concept Tags",
         "• critical collapse\n"
         "• Choptuik\n"
         "• universal scaling exponent\n"
         "• Type II critical collapse\n"
         "• Type I critical collapse\n"
         "• discrete self-similarity\n"
         "• echoing period\n"
         "• BH formation threshold\n"
         "• intermediate attractor\n"
         "• codimension-1 critical surface\n"
         "• gravitational critical phenomena\n"
         "• naked singularity\n"
         "• Gundlach review"),
    ],

    "HB10": [
        (0, "What It Claims",
         "Hawking and Page (Comm. Math. Phys. 87, 577, 1983) showed that in anti-de "
         "Sitter (AdS) spacetime, there is a first-order phase transition between two "
         "gravitational configurations: thermal radiation in AdS (no black hole) and a "
         "large Schwarzschild-AdS black hole. Below a critical temperature T_HP = 1/(pi*l) "
         "where l is the AdS radius, thermal AdS is thermodynamically preferred (lower free "
         "energy). Above T_HP, the large BH phase dominates. The transition is first-order: "
         "the entropy jumps discontinuously at T_HP. Via the AdS/CFT correspondence "
         "(Maldacena 1997, Witten 1998), this gravitational phase transition maps to the "
         "confinement/deconfinement transition in the dual gauge theory living on the "
         "boundary. Kubiznak and Mann (JHEP 2012) extended this to charged AdS BHs, "
         "treating the cosmological constant as thermodynamic pressure P = -Lambda/(8*pi) "
         "and conjugate volume V = (4/3)*pi*r_+^3. Charged AdS BHs exhibit Van der Waals-"
         "type critical points with mean-field exponents, including a critical isotherm "
         "and coexistence curves identical to the liquid-gas transition."),

        (1, "Mathematical Form",
         "Hawking-Page critical temperature:\n"
         "  T_HP = 1/(pi*l)  for AdS radius l\n\n"
         "Free energy comparison:\n"
         "  F = M - TS (Gibbs free energy)\n"
         "  F_BH = r_+/4 - pi*T*r_+^2  (large Schwarzschild-AdS BH)\n"
         "  Phase transition at F_BH = 0  =>  r_+ = l  =>  T = T_HP\n\n"
         "Euclidean path integral:\n"
         "  Z = sum exp(-I_E[g])  over gravitational instantons\n"
         "  I_E(BH) < I_E(thermal AdS)  for T > T_HP\n\n"
         "Extended thermodynamics (Kubiznak-Mann 2012):\n"
         "  Pressure: P = -Lambda/(8*pi) = 3/(8*pi*l^2)\n"
         "  Volume: V = (4/3)*pi*r_+^3\n"
         "  Equation of state: P = T/(2*r_+) - 1/(8*pi*r_+^2) + Q^2/(8*pi*r_+^4)\n"
         "  Critical point: P_c*v_c/(T_c) = 3/8  (Van der Waals universal ratio)\n"
         "  Mean-field critical exponents: alpha=0, beta=1/2, gamma=1, delta=3"),

        (2, "Constraint Category",
         "Thermodynamic (Th): The Hawking-Page transition is a genuine thermodynamic "
         "phase transition in the gravitational sector. The constraint is free energy "
         "minimization: the system occupies whichever phase has lower Gibbs free energy "
         "F = M - TS. At T = T_HP, the free energies cross and the preferred phase "
         "switches discontinuously. The Kubiznak-Mann extension reveals that the same "
         "Van der Waals universality class governs both charged AdS BHs and classical "
         "fluids, establishing that gravitational thermodynamics shares the same "
         "phase structure as ordinary thermodynamics."),

        (3, "DS Cross-References",
         "HB04 (Hawking Radiation — provides the temperature assignment T = kappa/(2*pi) "
         "that makes the BH a thermal object; without Hawking temperature, there is no "
         "thermodynamic competition to define a phase transition). "
         "HB02 (Bekenstein-Hawking Entropy — S = A/4 enters the free energy F = M - TS "
         "that determines which phase is thermodynamically preferred). "
         "HB03 (Holographic Principle — AdS/CFT maps the bulk Hawking-Page transition "
         "to a boundary confinement/deconfinement transition; the holographic principle "
         "underlies this duality). "
         "GT01 (Jacobson Thermodynamic Derivation — Jacobson's framework of treating "
         "spacetime as a thermodynamic system provides the conceptual basis for treating "
         "gravitational configurations as thermodynamic phases with free energies)."),

        (4, "Mathematical Archetype",
         "Mathematical archetype: threshold-transition\n\n"
         "The Hawking-Page transition is a first-order threshold: free energy comparison "
         "determines a sharp boundary at T = T_HP between two distinct phases. The "
         "Kubiznak-Mann extension reveals a critical point where the first-order line "
         "terminates, with Van der Waals mean-field exponents (beta = 1/2, gamma = 1, "
         "delta = 3). This critical endpoint is a continuous transition embedded within "
         "the first-order structure, paralleling the liquid-gas critical point."),

        (5, "What The Math Says",
         "Place a black hole in a box (anti-de Sitter space acts as a natural box with "
         "reflecting boundary conditions). The BH radiates at temperature T = kappa/(2*pi) "
         "and is in thermal equilibrium with its own radiation. But there is a competing "
         "configuration: empty AdS space filled with thermal radiation at the same "
         "temperature. The question is which configuration has lower free energy "
         "F = E - TS. At low temperature, thermal radiation wins (low energy, modest "
         "entropy). At high temperature, the large BH wins (huge entropy ~ A/4 "
         "overwhelms the energy cost). The crossover at T_HP = 1/(pi*l) is a first-order "
         "phase transition: the entropy jumps discontinuously. Through AdS/CFT, this maps "
         "to the deconfinement transition in gauge theory: below T_HP, the gauge theory is "
         "confining (no free quarks); above T_HP, it deconfines (quark-gluon plasma). "
         "When electric charge is added, the story gets richer: charged BHs exhibit a "
         "liquid-gas type critical point where the first-order line terminates. The "
         "critical exponents match Van der Waals exactly, suggesting that gravitational "
         "thermodynamics falls into the same universality classes as ordinary statistical "
         "mechanics."),

        (6, "Concept Tags",
         "• Hawking-Page transition\n"
         "• first-order phase transition\n"
         "• anti-de Sitter space\n"
         "• AdS/CFT correspondence\n"
         "• confinement/deconfinement\n"
         "• Gibbs free energy\n"
         "• BH thermodynamics\n"
         "• Euclidean path integral\n"
         "• gravitational instantons\n"
         "• extended BH thermodynamics\n"
         "• Kubiznak-Mann\n"
         "• Van der Waals critical point\n"
         "• mean-field exponents\n"
         "• charged AdS black holes"),
    ],

    "GT10": [
        (0, "What It Claims",
         "Jacobson (PRL 116, 201101, 2016) showed that the Einstein equation follows "
         "from the condition that vacuum entanglement entropy is maximal at fixed volume "
         "in all small geodesic balls. This upgrades Jacobson's own 1995 derivation "
         "(GT01), which used the classical Clausius relation delta_Q = T*dS on local "
         "Rindler horizons, to a quantum-information-theoretic foundation. The key "
         "insight: for conformal matter, decompose the entanglement entropy of a small "
         "geodesic ball into an area term (Bekenstein-Hawking, proportional to the boundary "
         "area A/4G) and a bulk term (the expectation value of the modular Hamiltonian K). "
         "If the vacuum state is stationary under first-order metric perturbations — "
         "delta_S_EE|_V = 0 for all geodesic balls — then the Einstein equation holds "
         "exactly. The stationarity condition means: the area contribution to entanglement "
         "entropy (which wants to increase with curvature) is exactly balanced by the bulk "
         "contribution (which resists concentration of stress-energy). The Einstein equation "
         "IS this balance condition. No thermodynamic assumptions (heat, temperature, "
         "Clausius relation) are needed — only the entanglement structure of the vacuum."),

        (1, "Mathematical Form",
         "Entanglement entropy decomposition in geodesic ball B:\n"
         "  S_EE(B) = S_area + S_bulk\n"
         "  S_area = (A/4G)(1 + delta_A/A)\n"
         "  S_bulk = <K>  (expectation of modular Hamiltonian)\n\n"
         "Stationarity condition (maximal entanglement at fixed volume):\n"
         "  delta_S_EE|_V = 0  for all geodesic balls B\n\n"
         "Expanded:\n"
         "  delta<T_ab> k^a k^b = (1/8*pi*G) G_ab k^a k^b\n"
         "  for all null vectors k^a\n\n"
         "This IS the Einstein equation:\n"
         "  G_ab + Lambda*g_ab = 8*pi*G * T_ab\n\n"
         "Relationship to GT01 (Jacobson 1995):\n"
         "  GT01: delta_Q = T*dS on Rindler horizons => Einstein equation\n"
         "  GT10: delta_S_EE|_V = 0 in geodesic balls => Einstein equation\n"
         "  GT10 is the quantum-informatic generalization of GT01"),

        (2, "Constraint Category",
         "Informatic-Geometric (In-Gm): The Einstein equation emerges as the condition "
         "for maximal vacuum entanglement entropy at fixed volume. This is an "
         "information-geometric constraint: the geometry of spacetime (encoded in G_ab) "
         "is determined by the requirement that entanglement entropy is extremal. "
         "No classical thermodynamic concepts (heat flux, temperature, Clausius relation) "
         "are invoked — the constraint is purely quantum-informatic. The area-entanglement "
         "connection from the Ryu-Takayanagi formula (HB07) is promoted from a static "
         "holographic identity to a dynamical principle: the Einstein equation is what "
         "you get when you demand that this identity holds everywhere."),

        (3, "DS Cross-References",
         "GT01 (Jacobson Thermodynamic Derivation — GT10 generalizes GT01 from classical "
         "Clausius delta_Q = T*dS to quantum delta_S_EE|_V = 0; the 1995 result is the "
         "classical-thermodynamic limit of the 2016 entanglement-equilibrium derivation). "
         "GT03 (Padmanabhan Holographic Equipartition — N_sur = N_bulk is the global "
         "version of GT10's local entanglement equilibrium; both express the balance "
         "between surface and bulk degrees of freedom). "
         "HB07 (Ryu-Takayanagi Formula — provides the area-entanglement relation "
         "S = A/4G_N that GT10 promotes from a static holographic identity to a "
         "dynamical constraint determining spacetime geometry). "
         "HB02 (Bekenstein-Hawking Entropy — S = A/4 emerges as the area contribution "
         "to entanglement entropy in each geodesic ball; GT10 gives it a dynamical role). "
         "IT03 (KL Divergence — departure from maximal entanglement is measured by "
         "relative entropy; GT10's stationarity condition delta_S_EE = 0 is equivalent "
         "to delta_D_KL = 0 around the maximally entangled vacuum state)."),

        (4, "Mathematical Archetype",
         "Mathematical archetype: optimization-principle\n\n"
         "The Einstein equation is the condition for extremal vacuum entanglement entropy "
         "at fixed volume. This is a variational principle: among all possible spacetime "
         "geometries, the physical geometry maximizes entanglement entropy in every small "
         "region. The optimization structure parallels the principle of least action, "
         "but the quantity being extremized is quantum information (entanglement entropy) "
         "rather than a classical action functional."),

        (5, "What The Math Says",
         "Pick any point in spacetime and draw a small geodesic ball around it. The "
         "quantum fields inside this ball are entangled with those outside. The total "
         "entanglement entropy has two contributions: an area term proportional to the "
         "boundary surface (the Bekenstein-Hawking piece) and a bulk term capturing the "
         "matter content (the modular Hamiltonian expectation). Jacobson asks: what if "
         "the vacuum state locally maximizes this entanglement entropy, holding the volume "
         "fixed? The answer: you get the Einstein equation. The area piece wants to grow "
         "(more boundary area means more entanglement); the bulk piece constrains it "
         "(concentrating stress-energy costs entanglement). The balance between these "
         "two — delta_S_EE|_V = 0 — is precisely G_ab = 8*pi*G*T_ab. This means gravity "
         "is not a fundamental force transmitted by gravitons; it is the condition for "
         "equilibrium of quantum entanglement. Compared to the 1995 derivation which used "
         "classical heat flow and the Clausius relation, this formulation uses only quantum "
         "information theory. No temperature, no heat, no thermodynamics — just entanglement "
         "structure."),

        (6, "Concept Tags",
         "• entanglement equilibrium\n"
         "• Jacobson 2016\n"
         "• vacuum entanglement entropy\n"
         "• modular Hamiltonian\n"
         "• geodesic ball\n"
         "• area-entanglement relation\n"
         "• Einstein equation from entanglement\n"
         "• gravity as entanglement\n"
         "• Ryu-Takayanagi dynamical\n"
         "• quantum information gravity\n"
         "• holographic entanglement\n"
         "• stationarity condition\n"
         "• informatic-geometric constraint"),
    ],
}

# ---------------------------------------------------------------------------
# Properties
# ---------------------------------------------------------------------------

PROPERTIES = {
    "GT09": [
        ("DS Facets", "Constraint Category", "Gm", 0),
        ("entries", "concept_tags", "critical collapse, Choptuik, universal scaling exponent, Type I/II, discrete self-similarity, BH formation threshold", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "HB10": [
        ("DS Facets", "Constraint Category", "Th", 0),
        ("entries", "concept_tags", "Hawking-Page transition, first-order phase transition, AdS/CFT, confinement/deconfinement, extended BH thermodynamics, Van der Waals", 0),
        ("DS Facets", "mathematical_archetype", "threshold-transition", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
    "GT10": [
        ("DS Facets", "Constraint Category", "In-Gm", 0),
        ("entries", "concept_tags", "entanglement equilibrium, Jacobson 2016, vacuum entanglement, modular Hamiltonian, Einstein from entanglement, gravity as information", 0),
        ("DS Facets", "mathematical_archetype", "optimization-principle", 1),
        ("DS Facets", "dimensional_sensitivity", "D-sensitive", 2),
    ],
}

# ---------------------------------------------------------------------------
# Links
# ---------------------------------------------------------------------------

LINKS = [
    # GT09 links
    ("GT09", "GT01", "derives from", "1.5",
     "Critical collapse occurs within GR; Jacobson's thermodynamic derivation provides "
     "the entropy-area framework underlying the formation threshold"),
    ("GT09", "HB02", "couples to", "1.5",
     "BH formation saturates Bekenstein-Hawking entropy; Choptuik scaling describes "
     "how mass and entropy approach zero continuously at the Type II threshold"),
    ("GT09", "HB06", "couples to", "1.5",
     "Area theorem dA/dt >= 0 governs post-formation evolution; Choptuik critical "
     "collapse governs the formation threshold itself"),
    ("GT09", "D2", "analogous to", "1.5",
     "Both exhibit universal scaling exponents at critical thresholds; Choptuik gamma "
     "is the gravitational analog of Feigenbaum delta"),

    # HB10 links
    ("HB10", "HB04", "derives from", "1.5",
     "Hawking radiation provides the temperature T = kappa/(2*pi) that makes BHs "
     "thermal objects; without it no free energy competition defines the transition"),
    ("HB10", "HB02", "couples to", "1.5",
     "BH entropy S = A/4 enters the free energy comparison F = M - TS that determines "
     "which phase is thermodynamically preferred at a given temperature"),
    ("HB10", "HB03", "couples to", "1.5",
     "AdS/CFT maps the bulk Hawking-Page transition to a boundary confinement/"
     "deconfinement transition; the holographic principle underlies this duality"),
    ("HB10", "GT01", "derives from", "1.5",
     "Jacobson's framework of spacetime as a thermodynamic system provides the "
     "conceptual basis for treating gravitational configurations as thermodynamic phases"),

    # GT10 links
    ("GT10", "GT01", "generalizes", "1.5",
     "Replaces classical Clausius delta_Q = T*dS with quantum delta_S_EE|_V = 0; "
     "GT01's equilibrium thermodynamics is the classical limit of entanglement equilibrium"),
    ("GT10", "GT03", "couples to", "1.5",
     "Padmanabhan's holographic equipartition N_sur = N_bulk is the global version of "
     "Jacobson 2016's local entanglement equilibrium condition delta_S_EE|_V = 0"),
    ("GT10", "HB07", "derives from", "1.5",
     "Ryu-Takayanagi formula S = A/4G provides the area-entanglement link that Jacobson "
     "2016 promotes from a static holographic identity to a dynamical principle"),
    ("GT10", "HB02", "couples to", "1.5",
     "Bekenstein-Hawking entropy S = A/4 emerges as the area contribution to entanglement "
     "entropy in each geodesic ball; GT10 gives it a dynamical role"),
    ("GT10", "IT03", "couples to", "1.5",
     "KL divergence measures departure from maximal entanglement; GT10's stationarity "
     "condition delta_S_EE = 0 is equivalent to delta_D_KL = 0 at the vacuum state"),
]


def insert(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    labels = {r[0]: r[1] for r in cur.execute("SELECT id, title FROM entries")}

    for entry in ENTRIES:
        existing = cur.execute("SELECT id FROM entries WHERE id = ?", (entry["id"],)).fetchone()
        if existing:
            print(f"  SKIP (exists): {entry['id']}")
            continue

        cur.execute(
            """INSERT INTO entries
               (id, title, filename, entry_type, scale, domain, status, confidence,
                type_group, authoring_status, formality_tier)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (entry["id"], entry["title"], entry["filename"], entry["entry_type"],
             entry["scale"], entry["domain"], entry["status"], entry["confidence"],
             entry["type_group"], entry["authoring_status"], entry["formality_tier"])
        )
        print(f"  Inserted entry: {entry['id']} — {entry['title']}")

        for order, name, content in SECTIONS[entry["id"]]:
            cur.execute(
                "INSERT INTO sections (entry_id, section_name, section_order, content) "
                "VALUES (?, ?, ?, ?)",
                (entry["id"], name, order, content)
            )
            print(f"    Section [{order}]: {name} ({len(content)} chars)")

        if entry["id"] in PROPERTIES:
            for tname, pname, pval, pord in PROPERTIES[entry["id"]]:
                cur.execute(
                    "INSERT OR IGNORE INTO entry_properties "
                    "(entry_id, table_name, property_name, property_value, prop_order) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (entry["id"], tname, pname, pval, pord)
                )
            print(f"    Properties: {len(PROPERTIES[entry['id']])} inserted")

    # Update labels to include new entries
    labels.update({e["id"]: e["title"] for e in ENTRIES})

    print()
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
    print(f"Inserting GT09 + HB10 + GT10 into:\n  {SOURCE_DB}\n")
    insert(SOURCE_DB)
