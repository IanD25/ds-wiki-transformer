"""
Source-Domain Taxonomy — Schema + Seed — 2026-04-17

Creates three new tables in wiki_history.db supporting the hierarchical
source-domain taxonomy + cross-domain borrowings + per-entry tagging.
See docs/GSW_ANCHOR_ARCHITECTURE.md §4.2 and subsequent sections.

Tables created:
- source_domain_taxonomy       : the hierarchical tag tree (10 top-level + sub-tags)
- tag_cross_domain_borrowings  : first-layer cross-domain bridges at sub-tag level
- entry_source_domains         : per-entry tag assignments with review metadata

Seed content:
- 10 top-level domains
- ~40 level-1 sub-tags
- ~5 level-2 sub-sub-tags (only high-value cases)
- ~15 high-confidence cross-domain borrowings (differential geometry -> GR, group
  theory -> chemistry crystallography, Shannon -> stat mech, etc.)

NOT included:
- Per-entry tagging (separate retroactive pass over 278 entries)

CONSTRAINTS:
- Never schema-alter ds_wiki.db
- CREATE TABLE IF NOT EXISTS / INSERT OR IGNORE — safe to re-run
- Taxonomy rows are append-only; superseded tags set `superseded_by`

Run with: python3 scripts/migrations/create_domain_taxonomy_2026_04_17.py
"""

import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-taxonomy-seed-2026-04-17"


VALID_PRIMACY = ("primary", "secondary", "auxiliary")
VALID_CONFIDENCE = ("high", "medium", "low")
VALID_REVIEW_STATUS = ("current", "superseded", "contested")
VALID_BRIDGE_NATURE = (
    "applied_to",          # D_borrow applies the sub-tag's methods directly
    "specialized_as",      # D_borrow uses a specialized variant
    "generalized_in",      # D_borrow has a generalization of the sub-tag
    "analogous_structure", # structural analogy without direct use
)


def create_schema(conn: sqlite3.Connection) -> None:
    primacy_check = ", ".join(f"'{p}'" for p in VALID_PRIMACY)
    conf_check = ", ".join(f"'{c}'" for c in VALID_CONFIDENCE)
    review_check = ", ".join(f"'{r}'" for r in VALID_REVIEW_STATUS)
    bridge_check = ", ".join(f"'{b}'" for b in VALID_BRIDGE_NATURE)

    conn.executescript(f"""
    CREATE TABLE IF NOT EXISTS source_domain_taxonomy (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        tag_path         TEXT NOT NULL UNIQUE,
        display_name     TEXT NOT NULL,
        parent_id        INTEGER,
        depth            INTEGER NOT NULL CHECK(depth >= 0 AND depth <= 3),
        description      TEXT,
        created_date     DATE NOT NULL,
        superseded_by    INTEGER,
        FOREIGN KEY(parent_id) REFERENCES source_domain_taxonomy(id),
        FOREIGN KEY(superseded_by) REFERENCES source_domain_taxonomy(id)
    );
    CREATE INDEX IF NOT EXISTS idx_taxonomy_parent
        ON source_domain_taxonomy(parent_id);
    CREATE INDEX IF NOT EXISTS idx_taxonomy_depth
        ON source_domain_taxonomy(depth);
    CREATE INDEX IF NOT EXISTS idx_taxonomy_path
        ON source_domain_taxonomy(tag_path);

    CREATE TABLE IF NOT EXISTS tag_cross_domain_borrowings (
        id                   INTEGER PRIMARY KEY AUTOINCREMENT,
        tag_id               INTEGER NOT NULL,
        borrowing_domain_id  INTEGER NOT NULL,
        bridge_nature        TEXT NOT NULL CHECK(bridge_nature IN ({bridge_check})),
        canonical_example    TEXT,
        evidence_refs        TEXT,
        confidence           TEXT NOT NULL CHECK(confidence IN ({conf_check})),
        notes                TEXT,
        created_date         DATE NOT NULL,
        UNIQUE(tag_id, borrowing_domain_id),
        FOREIGN KEY(tag_id) REFERENCES source_domain_taxonomy(id),
        FOREIGN KEY(borrowing_domain_id) REFERENCES source_domain_taxonomy(id),
        CHECK (tag_id != borrowing_domain_id)
    );
    CREATE INDEX IF NOT EXISTS idx_borrow_tag
        ON tag_cross_domain_borrowings(tag_id);
    CREATE INDEX IF NOT EXISTS idx_borrow_domain
        ON tag_cross_domain_borrowings(borrowing_domain_id);

    CREATE TABLE IF NOT EXISTS entry_source_domains (
        id                        INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_id                  TEXT NOT NULL,
        tag_id                    INTEGER NOT NULL,
        primacy                   TEXT NOT NULL CHECK(primacy IN ({primacy_check})),
        via_borrowing_id          INTEGER,
        assigned_date             DATE NOT NULL,
        assigned_by_session       TEXT,
        last_reviewed_date        DATE NOT NULL,
        last_reviewed_by_session  TEXT,
        confidence                TEXT NOT NULL CHECK(confidence IN ({conf_check})),
        review_status             TEXT NOT NULL CHECK(review_status IN ({review_check})),
        rationale                 TEXT,
        FOREIGN KEY(tag_id) REFERENCES source_domain_taxonomy(id),
        FOREIGN KEY(via_borrowing_id) REFERENCES tag_cross_domain_borrowings(id)
    );
    CREATE UNIQUE INDEX IF NOT EXISTS idx_entry_domain_current
        ON entry_source_domains(entry_id, tag_id)
        WHERE review_status = 'current';
    CREATE INDEX IF NOT EXISTS idx_entry_domain_entry
        ON entry_source_domains(entry_id);
    CREATE INDEX IF NOT EXISTS idx_entry_domain_tag
        ON entry_source_domains(tag_id);
    """)
    conn.commit()


# ====================================================================
# Taxonomy seed data
# Tuple: (path, display_name, parent_path_or_None, description)
# ====================================================================

TOP_LEVEL = [
    ("physics", "Physics", None,
     "The physical sciences: matter, energy, forces, fields, cosmology"),
    ("mathematics", "Mathematics", None,
     "Pure and applied mathematics: analysis, algebra, geometry, probability"),
    ("formal_logic", "Formal Logic & Foundations", None,
     "Logic, proof theory, model theory, computability foundations, set theory"),
    ("information_theory", "Information Theory", None,
     "Shannon-Kolmogorov lineage: entropy, coding, quantum info, complexity"),
    ("statistics_probability", "Statistics & Probability", None,
     "Inference, estimation, stochastic processes, Bayesian/frequentist methods"),
    ("computer_science", "Computer Science", None,
     "Algorithms, complexity, distributed systems, ML, programming languages"),
    ("biology", "Biology", None,
     "Molecular, evolution, ecology, physiology, neuroscience"),
    ("chemistry", "Chemistry", None,
     "Physical chem, organic, materials, biochemistry"),
    ("earth_sciences", "Earth Sciences", None,
     "Geology, climate, hydrology, planetary"),
    ("networks_systems", "Networks & Complex Systems", None,
     "Complex systems science (Santa Fe tradition), graph theory, dynamical systems"),
]

SUB_TAGS_LEVEL_1 = [
    # physics
    ("physics.classical", "Classical Physics", "physics",
     "Mechanics, electromagnetism, thermodynamics, fluids, classical fields"),
    ("physics.modern", "Modern Physics", "physics",
     "Quantum mechanics, statistical mechanics, special relativity, particle"),
    ("physics.cosmology", "Cosmology & Gravity", "physics",
     "Cosmology, general relativity, astrophysics, gravitation"),

    # mathematics
    ("mathematics.analysis", "Mathematical Analysis", "mathematics",
     "Real, complex, functional analysis"),
    ("mathematics.algebra", "Algebra", "mathematics",
     "Abstract algebra, linear algebra, representation theory"),
    ("mathematics.geometry_topology", "Geometry & Topology", "mathematics",
     "Differential geometry, algebraic topology, manifolds"),
    ("mathematics.probability_measure", "Probability & Measure Theory", "mathematics",
     "Measure-theoretic probability, ergodic theory"),
    ("mathematics.discrete", "Discrete Mathematics", "mathematics",
     "Combinatorics, discrete structures, number theory"),
    ("mathematics.logic_foundations", "Mathematical Logic & Foundations", "mathematics",
     "Proof structures within mathematics (distinct from formal_logic top-level)"),

    # formal_logic
    ("formal_logic.proof_theory", "Proof Theory", "formal_logic", None),
    ("formal_logic.model_theory", "Model Theory", "formal_logic", None),
    ("formal_logic.computability", "Computability Theory", "formal_logic", None),
    ("formal_logic.set_theory", "Set Theory", "formal_logic", None),

    # information_theory
    ("information_theory.shannon", "Shannon Information Theory", "information_theory",
     "Entropy, channel capacity, source coding"),
    ("information_theory.coding", "Coding Theory", "information_theory",
     "Error correction, compression, rate-distortion"),
    ("information_theory.quantum_info", "Quantum Information", "information_theory", None),
    ("information_theory.kolmogorov_complexity", "Kolmogorov Complexity", "information_theory",
     "Algorithmic information theory, minimum description length"),

    # statistics_probability
    ("statistics_probability.bayesian", "Bayesian Methods", "statistics_probability", None),
    ("statistics_probability.frequentist", "Frequentist Methods", "statistics_probability", None),
    ("statistics_probability.stochastic_processes", "Stochastic Processes", "statistics_probability",
     "Markov chains, martingales, Itô calculus"),
    ("statistics_probability.inference", "Statistical Inference", "statistics_probability", None),

    # computer_science
    ("computer_science.algorithms", "Algorithms", "computer_science", None),
    ("computer_science.complexity", "Computational Complexity", "computer_science", None),
    ("computer_science.distributed", "Distributed Systems", "computer_science", None),
    ("computer_science.ml", "Machine Learning", "computer_science", None),
    ("computer_science.programming_languages", "Programming Languages", "computer_science", None),

    # biology
    ("biology.molecular", "Molecular Biology", "biology", None),
    ("biology.evolution", "Evolutionary Biology", "biology", None),
    ("biology.ecology", "Ecology", "biology", None),
    ("biology.physiology", "Physiology", "biology",
     "Organismal physiology, metabolism, vascular networks"),
    ("biology.neuroscience", "Neuroscience", "biology", None),

    # chemistry
    ("chemistry.physical", "Physical Chemistry", "chemistry", None),
    ("chemistry.organic", "Organic Chemistry", "chemistry", None),
    ("chemistry.materials", "Materials Chemistry", "chemistry", None),
    ("chemistry.biochemistry", "Biochemistry", "chemistry", None),

    # earth_sciences
    ("earth_sciences.geology", "Geology", "earth_sciences", None),
    ("earth_sciences.climate", "Climate Science", "earth_sciences", None),
    ("earth_sciences.hydrology", "Hydrology", "earth_sciences", None),
    ("earth_sciences.planetary", "Planetary Science", "earth_sciences", None),

    # networks_systems
    ("networks_systems.complex_systems", "Complex Systems Science", "networks_systems",
     "Santa Fe tradition: emergence, self-organization, criticality"),
    ("networks_systems.graph_theory", "Graph Theory", "networks_systems",
     "Network science foundations (home is debated with mathematics; modern applied use here)"),
    ("networks_systems.dynamical_systems", "Dynamical Systems", "networks_systems",
     "Chaos, bifurcation, phase space dynamics"),
]

SUB_TAGS_LEVEL_2 = [
    ("mathematics.geometry_topology.differential_geometry",
     "Differential Geometry", "mathematics.geometry_topology",
     "Smooth manifolds, Riemannian geometry, connections, curvature"),
    ("mathematics.geometry_topology.algebraic_topology",
     "Algebraic Topology", "mathematics.geometry_topology",
     "Homology, homotopy, fiber bundles"),
    ("mathematics.algebra.group_theory",
     "Group Theory", "mathematics.algebra",
     "Abstract groups, Lie groups, representation theory"),
    ("physics.modern.statistical_mechanics",
     "Statistical Mechanics", "physics.modern",
     "Thermodynamics from first principles, phase transitions, ensembles"),
    ("physics.modern.quantum_mechanics",
     "Quantum Mechanics", "physics.modern",
     "Foundations and formalism of non-relativistic QM"),
]


# ====================================================================
# Seed borrowings data
# Tuple: (tag_path, borrowing_domain_path, bridge_nature, canonical_example,
#         confidence, notes)
# ====================================================================
SEED_BORROWINGS = [
    # differential geometry -> physics (GR, gauge theory)
    ("mathematics.geometry_topology.differential_geometry", "physics",
     "applied_to",
     "General Relativity applies differential geometry to spacetime (Levi-Civita connection, Riemann tensor). Gauge theory applies principal bundles and connections.",
     "high",
     "Canonical case: Einstein 1916 uses Ricci calculus from Levi-Civita. Gauge theory formalism via Yang-Mills."),

    # group theory -> physics (Noether, symmetry)
    ("mathematics.algebra.group_theory", "physics",
     "applied_to",
     "Noether's theorem maps continuous symmetry groups to conservation laws. Lie groups underpin gauge theory and particle classification (SU(2), SU(3), ...).",
     "high",
     "Wigner 1939 on Poincaré group representations; particle physics Standard Model is group-theoretic."),

    # group theory -> chemistry (crystallography)
    ("mathematics.algebra.group_theory", "chemistry",
     "specialized_as",
     "Space groups and point groups classify crystal symmetries; 230 space groups in 3D.",
     "high",
     "International Tables for Crystallography."),

    # group theory -> computer_science (cryptography)
    ("mathematics.algebra.group_theory", "computer_science",
     "applied_to",
     "Elliptic-curve cryptography; discrete log problem; RSA via modular arithmetic.",
     "high",
     "Koblitz; Miller 1986 ECC."),

    # Shannon -> physics (stat mech)
    ("information_theory.shannon", "physics",
     "analogous_structure",
     "Shannon entropy structurally matches Boltzmann-Gibbs thermodynamic entropy (Jaynes 1957 MaxEnt). Both are H = -Sum p log p on a probability distribution.",
     "high",
     "Jaynes 1957 Phys Rev bridges. Distinction: thermodynamic S is base e and kBT-scaled; Shannon H is base 2 dimensionless."),

    # Shannon -> biology (genetic code)
    ("information_theory.shannon", "biology",
     "applied_to",
     "Information content of genetic sequences; entropy of codon distributions; mutual information in gene regulation.",
     "high",
     "Schneider 1986 sequence logos; Tkačik neural/genetic MaxEnt work."),

    # Shannon -> computer_science (compression)
    ("information_theory.shannon", "computer_science",
     "applied_to",
     "Source coding theorem bounds lossless compression. Huffman, arithmetic coding realize the bound.",
     "high",
     "Shannon 1948 noisy-channel theorem; Huffman 1952."),

    # Bayesian -> physics
    ("statistics_probability.bayesian", "physics",
     "applied_to",
     "Bayesian inference in cosmology (CMB, GW parameter estimation), particle physics fits, systematic uncertainty quantification.",
     "high",
     "Planck 2018 cosmology likelihood; LIGO parameter estimation."),

    # Bayesian -> biology
    ("statistics_probability.bayesian", "biology",
     "applied_to",
     "Phylogenetic inference (MrBayes, BEAST); systems biology parameter inference; epidemiological models.",
     "high",
     "MrBayes 2001; Stan in systems bio."),

    # Bayesian -> computer_science
    ("statistics_probability.bayesian", "computer_science",
     "applied_to",
     "Bayesian machine learning, probabilistic programming, variational inference.",
     "high",
     "Pearl 1988 belief networks; Stan/PyMC."),

    # graph theory -> biology
    ("networks_systems.graph_theory", "biology",
     "applied_to",
     "Protein-protein interaction networks, metabolic networks, neural connectomes.",
     "high",
     "Barabasi lab work; Connectome Project."),

    # graph theory -> computer_science
    ("networks_systems.graph_theory", "computer_science",
     "applied_to",
     "Data structures, routing, PageRank, social networks.",
     "high",
     "Dijkstra 1959; Brin-Page 1998."),

    # graph theory -> physics
    ("networks_systems.graph_theory", "physics",
     "applied_to",
     "Lattice models in stat mech; network-based models of phase transitions.",
     "high",
     "Dorogovtsev-Goltsev-Mendes reviews."),

    # measure-theoretic probability -> physics
    ("mathematics.probability_measure", "physics",
     "applied_to",
     "Statistical mechanics is measure-theoretic probability on configuration spaces (Gibbs measure, thermodynamic limit).",
     "high",
     "Ruelle, Sinai, Gallavotti treatments."),

    # complex systems -> biology
    ("networks_systems.complex_systems", "biology",
     "applied_to",
     "Self-organization in development, criticality in neural avalanches, allometric scaling (WBE).",
     "high",
     "Santa Fe Institute bio work; WBE 1997 vascular scaling."),

    # stochastic processes -> biology
    ("statistics_probability.stochastic_processes", "biology",
     "applied_to",
     "Population genetics (Wright-Fisher), gene expression noise, neural spike trains.",
     "high",
     "Kimura 1962; Gardiner Handbook."),
]


def tag_id_by_path(conn: sqlite3.Connection, path: str) -> int:
    row = conn.execute(
        "SELECT id FROM source_domain_taxonomy WHERE tag_path = ?", (path,)
    ).fetchone()
    if row is None:
        raise KeyError(f"taxonomy path not found: {path}")
    return row[0]


def seed_taxonomy(conn: sqlite3.Connection) -> dict:
    """Insert top-level, level-1, level-2 tags. Returns counts."""
    counts = {"level_0": 0, "level_1": 0, "level_2": 0, "skipped": 0}

    for path, name, parent_path, desc in TOP_LEVEL:
        parent_id = None
        try:
            res = conn.execute(
                "INSERT OR IGNORE INTO source_domain_taxonomy "
                "(tag_path, display_name, parent_id, depth, description, created_date) "
                "VALUES (?,?,?,?,?,?)",
                (path, name, parent_id, 0, desc, TODAY),
            )
            if res.rowcount > 0:
                counts["level_0"] += 1
            else:
                counts["skipped"] += 1
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to insert top-level {path}: {e}")

    for path, name, parent_path, desc in SUB_TAGS_LEVEL_1:
        parent_id = tag_id_by_path(conn, parent_path)
        res = conn.execute(
            "INSERT OR IGNORE INTO source_domain_taxonomy "
            "(tag_path, display_name, parent_id, depth, description, created_date) "
            "VALUES (?,?,?,?,?,?)",
            (path, name, parent_id, 1, desc, TODAY),
        )
        if res.rowcount > 0:
            counts["level_1"] += 1
        else:
            counts["skipped"] += 1

    for path, name, parent_path, desc in SUB_TAGS_LEVEL_2:
        parent_id = tag_id_by_path(conn, parent_path)
        res = conn.execute(
            "INSERT OR IGNORE INTO source_domain_taxonomy "
            "(tag_path, display_name, parent_id, depth, description, created_date) "
            "VALUES (?,?,?,?,?,?)",
            (path, name, parent_id, 2, desc, TODAY),
        )
        if res.rowcount > 0:
            counts["level_2"] += 1
        else:
            counts["skipped"] += 1

    conn.commit()
    return counts


def seed_borrowings(conn: sqlite3.Connection) -> int:
    """Insert high-confidence cross-domain borrowings."""
    inserted = 0
    for tag_path, borrow_path, nature, example, confidence, notes in SEED_BORROWINGS:
        tag_id = tag_id_by_path(conn, tag_path)
        borrow_id = tag_id_by_path(conn, borrow_path)
        res = conn.execute(
            "INSERT OR IGNORE INTO tag_cross_domain_borrowings "
            "(tag_id, borrowing_domain_id, bridge_nature, canonical_example, "
            " confidence, notes, created_date) "
            "VALUES (?,?,?,?,?,?,?)",
            (tag_id, borrow_id, nature, example, confidence, notes, TODAY),
        )
        if res.rowcount > 0:
            inserted += 1
    conn.commit()
    return inserted


def verify(conn: sqlite3.Connection) -> None:
    print("\nVerification:")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM source_domain_taxonomy WHERE depth=0")
    print(f"  [taxonomy] top-level: {cur.fetchone()[0]} (expected 10)")

    cur.execute("SELECT COUNT(*) FROM source_domain_taxonomy WHERE depth=1")
    print(f"  [taxonomy] level-1:   {cur.fetchone()[0]} (expected >=40)")

    cur.execute("SELECT COUNT(*) FROM source_domain_taxonomy WHERE depth=2")
    print(f"  [taxonomy] level-2:   {cur.fetchone()[0]} (expected 5)")

    cur.execute("SELECT COUNT(*) FROM tag_cross_domain_borrowings")
    print(f"  [borrowings] total:   {cur.fetchone()[0]} (expected >=15)")

    # Per-domain sub-tag counts for sanity
    print("\n  Per-domain sub-tag counts:")
    for row in cur.execute("""
        SELECT p.tag_path, COUNT(c.id)
        FROM source_domain_taxonomy p
        LEFT JOIN source_domain_taxonomy c ON c.parent_id = p.id
        WHERE p.depth = 0
        GROUP BY p.id
        ORDER BY p.tag_path
    """):
        print(f"    {row[0]:25} {row[1]} direct children")

    print("\n  Borrowings by home-domain:")
    for row in cur.execute("""
        SELECT home.tag_path, COUNT(b.id)
        FROM tag_cross_domain_borrowings b
        JOIN source_domain_taxonomy tag ON tag.id = b.tag_id
        JOIN source_domain_taxonomy home ON home.id = (
            -- walk up to the top-level ancestor
            SELECT CASE
                WHEN tag.depth = 0 THEN tag.id
                WHEN parent.depth = 0 THEN parent.id
                ELSE grandparent.id
            END
            FROM source_domain_taxonomy t2
            LEFT JOIN source_domain_taxonomy parent ON parent.id = t2.parent_id
            LEFT JOIN source_domain_taxonomy grandparent ON grandparent.id = parent.parent_id
            WHERE t2.id = tag.id
        )
        GROUP BY home.id
        ORDER BY COUNT(b.id) DESC
    """):
        print(f"    {row[0]:25} {row[1]} borrowings outward")


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        print(f"Applying domain-taxonomy schema + seed to {WIKI_HISTORY_DB}...")
        create_schema(conn)
        print("  [OK] schema created")

        counts = seed_taxonomy(conn)
        print(f"  [OK] taxonomy seeded: "
              f"{counts['level_0']} top-level, {counts['level_1']} level-1, "
              f"{counts['level_2']} level-2 (+ {counts['skipped']} skipped-existing)")

        borrow_n = seed_borrowings(conn)
        print(f"  [OK] borrowings seeded: {borrow_n} rows")

        verify(conn)
        print("\nMigration complete. Safe to re-run.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
