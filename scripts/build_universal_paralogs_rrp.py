"""
build_universal_paralogs_rrp.py — Build RRP for Goldman et al. (2026)
"Universal paralogs provide a window into evolution before the last
universal common ancestor" — Cell Genomics 6, 101140.

Phase 3D end-to-end: manually extracted claims → RRP bundle → bridges → PFD report.
"""

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from ingestion.rrp_bundle import create_rrp_bundle

DB_PATH = ROOT / "data" / "rrp" / "universal_paralogs" / "rrp_universal_paralogs.db"

# ── Entries ──────────────────────────────────────────────────────────────────
# Extracted from the paper's substantive sections.
# entry_type follows DS Wiki taxonomy:
#   reference_law = established principle
#   instantiation = specific instance/observation
#   method = technique/approach
#   open_question = unresolved issue

ENTRIES = [
    # Core claims about LUCA
    ("luca_complexity", "LUCA as complex cellular organism",
     "reference_law", "biology",
     "All extant life descends from LUCA ~4 billion years ago. "
     "LUCA is consistently depicted as a relatively complex cellular organism "
     "with functional membranes, a complete translation system, a nearly complete "
     "ribosome, the canonical genetic code, and core translation-related proteins."),

    ("luca_genome_structure", "LUCA genome: DNA vs RNA debate",
     "open_question", "biology",
     "The LUCA's genome structure remains debated. Some researchers argue for "
     "an RNA-based genome or DNA/RNA hybrid genome, based on the lack of a "
     "universal replicative DNA polymerase. The LUCA encoded ~2,657 proteins "
     "but only 399 protein families have probability >= 0.75 of being present."),

    ("luca_energy_metabolism", "LUCA energy metabolism via proton gradients",
     "instantiation", "biology · chemistry",
     "Conserved ATP synthase subunits indicate proton gradients were already "
     "being generated to synthesize ATP. The LUCA may have run anaerobic "
     "acetogenesis in reverse as an energy metabolism pathway."),

    # Universal paralogs — core concept
    ("universal_paralog_definition", "Universal paralogs: pre-LUCA gene duplications",
     "reference_law", "biology",
     "Universal paralogs are protein families with at least two related versions "
     "that were present in the LUCA genome and remain in most organisms today. "
     "Their phylogenies contain at least one pre-LUCA branch, offering a unique "
     "window into molecular evolution before LUCA."),

    ("gene_duplication_mechanism", "Gene duplication as source of new function",
     "reference_law", "biology",
     "Paralogy originates primarily from gene duplication. Most duplicate genes "
     "are lost as pseudogenes. Retained paralogs evolve via neofunctionalization "
     "(new function) or subfunctionalization (divided ancestral function). "
     "~70% of human protein-coding genes belong to paralogous families; "
     "46% in E. coli; 17% in Archaeoglobus fulgidus."),

    # Functional categories of known universal paralogs
    ("amino_acid_metabolism_paralogs", "Universal paralogs in amino acid metabolism",
     "instantiation", "biology · chemistry",
     "Known universal paralogs in amino acid metabolism include: "
     "aminotransferases/carbamoyl transferases (amine group transfer), "
     "HisA/HisF imidazole biosynthesis enzymes, and carbamoyl phosphate "
     "synthetases."),

    ("translation_paralogs", "Universal paralogs in translation machinery",
     "instantiation", "biology",
     "Translation-related universal paralogs include: aminoacyl-tRNA synthetases, "
     "initiation factor IF2/elongation factor EF-Tu (and EF-G/EF2), and signal "
     "recognition particle with its receptor. The translation system is the most "
     "ancient molecular system retained in extant life."),

    ("membrane_paralogs", "Universal paralogs in membrane function",
     "instantiation", "biology · chemistry",
     "Membrane-related universal paralogs include: ATP synthase catalytic and "
     "non-catalytic subunits, and ATP-binding cassette (ABC) transporters. "
     "Despite the lack of conserved phospholipid metabolism, proteins involved "
     "in membrane function indicate cellularity was present at LUCA."),

    # Phylogenetic methods and rooting
    ("tree_rooting_by_paralogs", "Rooting the tree of life using universal paralogs",
     "method", "biology",
     "Universal paralog phylogenies serve as mutual outgroups to root the "
     "universal tree of life. Early studies placed the root between bacteria "
     "and archaea/eukaryotes. More recent studies using improved models and "
     "broader taxon sampling confirm the bacteria-archaea root."),

    ("long_branch_attraction", "Long branch attraction artifact in deep phylogenetics",
     "reference_law", "biology · mathematics",
     "Long branch attraction is a systematic error in phylogenetic inference "
     "where rapidly evolving lineages are artifactually grouped together. "
     "Greater taxon sampling, mixed branch length models, and more "
     "sophisticated evolutionary models help mitigate this artifact."),

    # Pre-LUCA reconstruction results
    ("genetic_code_evolution", "Pre-LUCA evolution of the genetic code",
     "instantiation", "biology · chemistry",
     "Ancestral sequence reconstruction of aminoacyl-tRNA synthetases shows "
     "the transition to a modern genetic code was complex, involving "
     "co-evolution with amino acid biosynthesis. The tryptophanyl-tRNA "
     "synthetase evolved through neofunctionalization, while leucyl/isoleucyl/ "
     "valyl-tRNA synthetases show subfunctionalization."),

    ("if2_eftu_reconstruction", "IF2/EF-Tu ancestral protein reconstruction",
     "instantiation", "biology",
     "The pre-LUCA ancestor of IF2/EF-Tu was likely capable of both initiation "
     "and elongation functions. Kinetics experiments show resurrected ancestral "
     "EF-Tu proteins have equal preference for unrelated modern ribosomes, "
     "indicating the ribosomal core evolved before EF-Tu diversification."),

    ("signal_recognition_particle", "Signal recognition particle pre-LUCA history",
     "instantiation", "biology",
     "Analysis of the signal recognition particle universal paralog family shows "
     "the pre-LUCA ancestor was capable of several functions performed by "
     "either the particle or its receptor. Cellularity and complex membrane "
     "structure were well established prior to LUCA."),

    # Methodological advances
    ("ancestral_sequence_reconstruction", "Ancestral sequence reconstruction method",
     "method", "biology · computer science",
     "Modern methods of ancestral sequence reconstruction combined with "
     "protein structure and function prediction enable direct investigation "
     "of pre-LUCA proteins. Ancient protein resurrection (synthetic biology) "
     "and experimental approaches make pre-LUCA protein characterization possible."),

    ("structure_based_homology", "Structure-based homology for deep evolution",
     "method", "biology · computer science",
     "Protein structure is more conserved than amino acid sequence over "
     "evolutionary time. Integration of ancestral sequence reconstruction with "
     "structure prediction (e.g., AlphaFold) allows assessment of structural "
     "variation across entire protein lineages, enabling identification of "
     "very deep evolutionary relationships obscured by sequence divergence."),

    ("gene_tree_reconciliation", "Gene tree/species tree reconciliation",
     "method", "biology · mathematics",
     "Gene tree/species tree reconciliation methods can detect protein families "
     "that underwent pre-LUCA duplications but are no longer retained as "
     "paralogs. Horizontal gene transfers from pre-LUCA lineages can also "
     "be detected, offering another resource for reconstructing common "
     "ancestry predating LUCA."),

    # Key limitations / open questions
    ("gene_loss_obscures_paralogs", "Gene loss obscures universal paralog detection",
     "reference_law", "biology",
     "Gene losses in descendant lineages, high sequence divergence, and "
     "extensive horizontal gene transfer can obscure the ancient origin of "
     "protein families. Non-orthologous gene displacement can also obscure "
     "ancient origins. Most protein families present in LUCA may not be "
     "detectable through phylogenetic analyses."),

    ("pre_luca_bioengineering", "Pre-LUCA proteins as bioengineering resources",
     "open_question", "biology · chemistry",
     "Reconstructed pre-LUCA ancestral proteins could provide novel catalysts "
     "for biotechnology — enzymes capable of fundamental catalytic roles but "
     "no longer existing in modern form. This expands the known functional "
     "repertoire of translation proteins for biotech applications."),

    # Computational future
    ("ai_protein_prediction", "AI/deep learning for protein structure prediction",
     "method", "biology · computer science",
     "Deep learning methods have revolutionized protein structure and function "
     "prediction. AlphaFold and similar tools enable accurate structure-based "
     "homology searches. Quantum computing and exascale HPC may make precise "
     "molecular dynamics modeling of complex biomolecular systems feasible."),
]

# ── Links ────────────────────────────────────────────────────────────────────
# Internal links within the RRP — the paper's own logical structure.

LINKS = [
    # LUCA complexity grounds the universal paralog concept
    ("universal_paralog_definition", "luca_complexity", "derives from",
     "Universal paralogs derive meaning from LUCA's established complexity"),
    ("luca_genome_structure", "luca_complexity", "couples to",
     "Genome structure is part of LUCA complexity characterization"),
    ("luca_energy_metabolism", "luca_complexity", "couples to",
     "Energy metabolism is part of LUCA complexity"),

    # Functional categories are instances of universal paralogs
    ("amino_acid_metabolism_paralogs", "universal_paralog_definition", "implements",
     "Amino acid metabolism paralogs are instances of universal paralogs"),
    ("translation_paralogs", "universal_paralog_definition", "implements",
     "Translation paralogs are instances of universal paralogs"),
    ("membrane_paralogs", "universal_paralog_definition", "implements",
     "Membrane paralogs are instances of universal paralogs"),

    # Gene duplication is the mechanism behind paralogs
    ("universal_paralog_definition", "gene_duplication_mechanism", "derives from",
     "Universal paralogs arise through gene duplication"),

    # Methods applied to reconstruct pre-LUCA
    ("tree_rooting_by_paralogs", "universal_paralog_definition", "tests",
     "Phylogenetic rooting uses universal paralogs as evidence"),
    ("ancestral_sequence_reconstruction", "translation_paralogs", "tests",
     "ASR tests translation paralog claims via protein resurrection"),
    ("structure_based_homology", "ancestral_sequence_reconstruction", "generalizes",
     "Structure-based homology extends sequence-based ASR"),
    ("gene_tree_reconciliation", "gene_loss_obscures_paralogs", "tests",
     "Reconciliation methods test for hidden paralogs lost to gene loss"),

    # Specific reconstruction results
    ("genetic_code_evolution", "amino_acid_metabolism_paralogs", "derives from",
     "Genetic code evolution evidence derives from aminoacyl-tRNA synthetases"),
    ("if2_eftu_reconstruction", "translation_paralogs", "derives from",
     "IF2/EF-Tu reconstruction derives from translation paralog analysis"),
    ("signal_recognition_particle", "membrane_paralogs", "derives from",
     "SRP analysis derives from membrane paralog family"),

    # Limitations
    ("gene_loss_obscures_paralogs", "universal_paralog_definition", "constrains",
     "Gene loss constrains our ability to detect universal paralogs"),
    ("long_branch_attraction", "tree_rooting_by_paralogs", "constrains",
     "Long branch attraction constrains phylogenetic rooting accuracy"),

    # Future directions
    ("ai_protein_prediction", "structure_based_homology", "generalizes",
     "AI prediction generalizes structure-based homology approaches"),
    ("pre_luca_bioengineering", "ancestral_sequence_reconstruction", "derives from",
     "Bioengineering potential derives from ancestral reconstruction"),

    # Cross-category connections
    ("luca_energy_metabolism", "membrane_paralogs", "couples to",
     "ATP synthase connects energy metabolism to membrane paralogs"),
    ("genetic_code_evolution", "translation_paralogs", "couples to",
     "Genetic code evolution couples to translation machinery"),
]


def build():
    if DB_PATH.exists():
        DB_PATH.unlink()
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    create_rrp_bundle(
        DB_PATH,
        name="Universal Paralogs (Goldman et al. 2026)",
        source="https://doi.org/10.1016/j.xgen.2026.101140",
        fmt="paper_analysis",
    )
    conn = sqlite3.connect(DB_PATH)

    # Insert entries
    for eid, title, etype, domain, wic in ENTRIES:
        conn.execute(
            "INSERT OR IGNORE INTO entries (id, title, entry_type, domain) "
            "VALUES (?, ?, ?, ?)",
            (eid, title, etype, domain),
        )
        # Add WIC as a section
        conn.execute(
            "INSERT OR IGNORE INTO sections (entry_id, section_name, content) "
            "VALUES (?, 'what_it_captures', ?)",
            (eid, wic),
        )

    # Insert links
    for src, tgt, ltype, desc in LINKS:
        conn.execute(
            "INSERT OR IGNORE INTO links (source_id, target_id, link_type, description) "
            "VALUES (?, ?, ?, ?)",
            (src, tgt, ltype, desc),
        )

    # RRP metadata
    conn.execute(
        "INSERT OR IGNORE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("paper_title", "Universal paralogs provide a window into evolution before the last universal common ancestor"),
    )
    conn.execute(
        "INSERT OR IGNORE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("authors", "Goldman AD, Fournier GP, Kaçar B"),
    )
    conn.execute(
        "INSERT OR IGNORE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("journal", "Cell Genomics 6, 101140"),
    )
    conn.execute(
        "INSERT OR IGNORE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("year", "2026"),
    )
    conn.execute(
        "INSERT OR IGNORE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("doi", "10.1016/j.xgen.2026.101140"),
    )
    conn.execute(
        "INSERT OR IGNORE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("dataset_type", "paper_analysis"),
    )

    conn.commit()

    # Summary
    n_entries = conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    n_links = conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
    n_sections = conn.execute("SELECT COUNT(*) FROM sections").fetchone()[0]

    print(f"Built RRP: {DB_PATH}")
    print(f"  {n_entries} entries, {n_links} links, {n_sections} sections")

    # Type breakdown
    for row in conn.execute(
        "SELECT entry_type, COUNT(*) FROM entries GROUP BY entry_type ORDER BY COUNT(*) DESC"
    ):
        print(f"  {row[0]}: {row[1]}")

    conn.close()


if __name__ == "__main__":
    build()
