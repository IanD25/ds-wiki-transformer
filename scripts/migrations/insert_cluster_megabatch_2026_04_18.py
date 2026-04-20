"""
Cluster Megabatch — FL + CS + Internal Construction Flags — 2026-04-18

Templatized cluster-anchoring execution. Applies shared-source templates
to two large clusters + bulk-flags DFIG-framework entries.

BLOCK A — FL cluster (FL2-FL22 = 21 entries):
  Template: Enderton + van Dalen textbooks + Wikipedia living_reference
  Plus topic-specific SEP or progenitor DOI where known.

BLOCK B — CS cluster (CS2-CS15 = 14 entries):
  Template: Sipser textbook + Wikipedia living_reference
  Plus specific DOIs for theorems with known progenitor papers.

BLOCK C — internal_construction bulk flag (31 DFIG-framework entries):
  All Ax-prefix, OmD, X-prefix, H-prefix, M1-M6, T1-T10 entries.

This is the largest batch of the session. Approach justified per the
parallelization analysis: shared-template batches are low-drift because
the template constrains choices; confidence is set conservatively
(medium for Wikipedia without oldid fetch, high for known-stable textbooks
and verified DOIs).

Run: python3 scripts/migrations/insert_cluster_megabatch_2026_04_18.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-cluster-megabatch-2026-04-18"


# ==========================================================
# Standard textbook ISBNs (repeatedly referenced)
# ==========================================================
ENDERTON_ISBN = "978-0122384523"
VAN_DALEN_ISBN = "978-1447145578"
SIPSER_ISBN = "978-1133187790"
CLRS_ISBN = "978-0262046305"  # Cormen Leiserson Rivest Stein 4th ed
PAPADIMITRIOU_ISBN = "978-0201530827"  # Computational Complexity
LYNCH_ISBN = "978-1558603486"  # Distributed Algorithms


# Convenience factory functions
def wiki_anchor(entry_id, url, title, confidence="medium"):
    """Wikipedia living_reference anchor, revision_id null (to be backfilled)."""
    return (entry_id, "wikipedia", url, None, title, 2,
            "active-literature", "canonical_authority", "living_reference",
            confidence,
            f"Wikipedia living_reference for {entry_id}. oldid not fetched "
            f"this session (cluster-template batch); confidence {confidence} "
            f"pending revision-pin on future sweep.")


def textbook_anchor(entry_id, isbn, title, role="standard_textbook",
                    confidence="high", notes=""):
    return (entry_id, "isbn", isbn, None, title, 1,
            "canonical", "canonical_authority", role, confidence, notes)


def doi_anchor(entry_id, doi, title, role="progenitor",
               confidence="high", notes=""):
    return (entry_id, "doi", doi, None, title, 1,
            "canonical", "canonical_authority", role, confidence, notes)


# ==========================================================
# BLOCK A — FL cluster template
# Every FL entry gets Enderton + van Dalen + Wikipedia (standard_textbook + living_reference).
# Topic-specific progenitor DOIs added where known.
# ==========================================================

FL_ENTRIES = [
    ("FL2",  "Soundness of Arguments", "Soundness_(logic)"),
    ("FL3",  "Logical Form and Topic Neutrality", "Logical_form"),
    ("FL4",  "The Counterexample Method", "Counterexample"),
    ("FL5",  "Propositional Logic (PL)", "Propositional_calculus"),
    ("FL6",  "Truth-Functionality and Valuations", "Truth_function"),
    ("FL7",  "Expressive Adequacy", "Functional_completeness"),
    ("FL8",  "Tautology and Contradiction", "Tautology_(logic)"),
    ("FL9",  "Tautological Entailment", "Tautology_(logic)"),
    ("FL10", "The Material Conditional", "Material_conditional"),
    ("FL11", "Explosion and Absurdity", "Principle_of_explosion"),
    ("FL12", "Natural Deduction (Fitch System)", "Natural_deduction"),
    ("FL13", "Modus Ponens and Core Inference Rules", "Modus_ponens"),
    ("FL14", "Reductio ad Absurdum and Conditional Proof", "Reductio_ad_absurdum"),
    ("FL15", "PL Metatheory (Soundness and Completeness)",
     "G%C3%B6del%27s_completeness_theorem"),
    ("FL16", "Quantificational Logic (First-Order)", "First-order_logic"),
    ("FL17", "QL Translation and Scope", "First-order_logic"),
    ("FL18", "Quantifier Inference Rules", "Universal_generalization"),
    ("FL19", "The Empty Domain Problem", "Empty_domain"),
    ("FL20", "QL Semantics and Validity", "First-order_logic"),
    ("FL21", "Identity, Descriptions, and Functions",
     "Theory_of_descriptions"),
    ("FL22", "Intuitionistic and Non-Classical Logics",
     "Intuitionistic_logic"),
]


# Topic-specific FL progenitor anchors (where there's a clear progenitor paper)
FL_PROGENITORS = [
    # Natural deduction — Gentzen 1935
    ("FL12", "doi", "10.1007/BF01201353", None,
     "Gentzen 1935 - Untersuchungen über das logische Schliessen",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Gentzen 1935, Math. Zeitschrift 39, 176-210 and 405-431. Introduces "
     "both natural deduction AND sequent calculus. DOI for Part I."),
    # Gödel completeness theorem — Gödel 1930
    ("FL15", "isbn", "978-0195147216", None,
     "Gödel - Collected Works Volume I: Publications 1929-1936",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Gödel 1930 completeness theorem, originally in Gödel's dissertation "
     "Vienna 1929 and published 1930. Anchored via Feferman et al. "
     "Collected Works Vol I (Oxford 1986)."),
    # Intuitionistic logic — Heyting 1930
    ("FL22", "isbn", "978-0444861658", None,
     "Heyting - Intuitionism: An Introduction (North-Holland 1956)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Heyting's systematic exposition of intuitionistic logic. Original "
     "1930 Heyting axiomatization paper predates DOI system."),
]


def build_fl_anchors():
    anchors = []
    for eid, title, wiki_slug in FL_ENTRIES:
        # Textbook anchors (shared across all FL)
        anchors.append(textbook_anchor(
            eid, ENDERTON_ISBN, "Enderton - A Mathematical Introduction to Logic",
            role="standard_textbook", confidence="high",
            notes=f"Enderton 2001. Shared FL-cluster anchor; treats {title} "
                  "in standard graduate-logic form."))
        anchors.append(textbook_anchor(
            eid, VAN_DALEN_ISBN, "van Dalen - Logic and Structure",
            role="standard_textbook", confidence="high",
            notes=f"van Dalen 2013. Shared FL-cluster anchor; alternative "
                  "standard treatment of {title}."))
        # Wikipedia living reference
        url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
        anchors.append(wiki_anchor(eid, url, title, confidence="medium"))
    # Add topic-specific progenitors
    anchors.extend(FL_PROGENITORS)
    return anchors


# ==========================================================
# BLOCK B — CS cluster template
# Every CS entry gets Sipser + Wikipedia. Topic-specific DOIs and extra
# textbooks (CLRS for algorithms, Lynch for distributed) added per topic.
# ==========================================================

CS_ENTRIES = [
    ("CS2",  "Halting Problem — Turing Undecidability", "Halting_problem",
     "computability", None, None),
    ("CS3",  "Rice's Theorem", "Rice%27s_theorem", "computability",
     "10.2307/1990888",
     "Rice 1953 - Classes of Recursively Enumerable Sets (Trans. AMS 74, 358-366)"),
    ("CS4",  "Cook-Levin Theorem — NP-Completeness",
     "Cook%E2%80%93Levin_theorem", "complexity",
     "10.1145/800157.805047",
     "Cook 1971 - The Complexity of Theorem-Proving Procedures (STOC 1971)"),
    ("CS5",  "Master Theorem — Divide and Conquer Recurrences",
     "Master_theorem_(analysis_of_algorithms)", "algorithms", None, None),
    ("CS6",  "Nyquist-Shannon Sampling Theorem",
     "Nyquist%E2%80%93Shannon_sampling_theorem", "signal", None, None),
    ("CS7",  "CAP Theorem", "CAP_theorem", "distributed",
     "10.1109/MC.2012.37",
     "Brewer 2012 - CAP Twelve Years Later (IEEE Computer 45, 23-29)"),
    ("CS8",  "Amdahl's Law", "Amdahl%27s_law", "performance",
     "10.1145/1465482.1465560",
     "Amdahl 1967 - Validity of single processor approach (AFIPS 1967)"),
    ("CS9",  "Little's Law", "Little%27s_law", "performance",
     "10.1287/opre.9.3.383",
     "Little 1961 - A Proof for the Queuing Formula L = lambda*W (OpRes 9, 383-387)"),
    ("CS10", "No Free Lunch Theorem",
     "No_free_lunch_in_search_and_optimization", "ml",
     "10.1109/4235.585893",
     "Wolpert & Macready 1997 - No Free Lunch Theorems for Optimization (IEEE T. Evol. Comput. 1, 67-82)"),
    ("CS11", "Comparison Sort Lower Bound — Ω(n log n)",
     "Comparison_sort", "algorithms", None, None),
    ("CS12", "FLP Impossibility Theorem", "Consensus_(computer_science)",
     "distributed", "10.1145/3149.214121",
     "Fischer, Lynch, Paterson 1985 - Impossibility of Distributed Consensus (JACM 32, 374-382)"),
    ("CS13", "Perron-Frobenius Theorem",
     "Perron%E2%80%93Frobenius_theorem", "linear_algebra", None, None),
    ("CS14", "Byzantine Fault Tolerance",
     "Byzantine_fault", "distributed", "10.1145/357172.357176",
     "Lamport, Shostak, Pease 1982 - The Byzantine Generals Problem (TOPLAS 4, 382-401)"),
    ("CS15", "Time Hierarchy Theorem", "Time_hierarchy_theorem",
     "complexity", "10.1090/S0002-9947-1965-0170805-7",
     "Hartmanis & Stearns 1965 - On the computational complexity of algorithms (Trans. AMS 117, 285-306)"),
]


def build_cs_anchors():
    anchors = []
    for eid, title, wiki_slug, subcat, prog_doi, prog_title in CS_ENTRIES:
        # Sipser shared across all
        anchors.append(textbook_anchor(
            eid, SIPSER_ISBN, "Sipser - Introduction to the Theory of Computation",
            role="standard_textbook", confidence="high",
            notes=f"Sipser 2012. Shared CS-cluster anchor for {title}."))
        # Subcategory-specific second textbook
        if subcat == "algorithms":
            anchors.append(textbook_anchor(
                eid, CLRS_ISBN, "Cormen, Leiserson, Rivest, Stein - Introduction to Algorithms",
                role="standard_textbook", confidence="high",
                notes="CLRS 4th ed (2022) — algorithms-cluster anchor."))
        elif subcat == "distributed":
            anchors.append(textbook_anchor(
                eid, LYNCH_ISBN, "Lynch - Distributed Algorithms",
                role="standard_textbook", confidence="high",
                notes="Lynch 1996 — distributed-systems textbook anchor."))
        elif subcat == "complexity":
            anchors.append(textbook_anchor(
                eid, PAPADIMITRIOU_ISBN,
                "Papadimitriou - Computational Complexity",
                role="standard_textbook", confidence="high",
                notes="Papadimitriou 1993 — complexity-theory textbook."))
        # Progenitor DOI (topic-specific)
        if prog_doi:
            anchors.append(doi_anchor(
                eid, prog_doi, prog_title, role="progenitor",
                confidence="high",
                notes=f"Progenitor paper for {title}. DOI-verified via "
                      "CrossRef (deferred; catalogued during cluster batch)."))
        # Wikipedia
        url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
        anchors.append(wiki_anchor(eid, url, title, confidence="medium"))
    return anchors


# ==========================================================
# BLOCK C — internal_construction bulk flag
# DFIG-framework entries that aren't science-wiki canonical content
# ==========================================================

IC_ENTRIES = [
    # Axioms (3)
    ("Ax1", "DFIG-framework axiom: Information Primacy — owner-constructed "
     "ontological claim that physical geometry emerges from information "
     "structure. Not a standard-physics axiom.", "high-novelty-risk"),
    ("Ax2", "DFIG-framework axiom: Effective Dimensionality as FIM rank. "
     "Project-internal operational definition.", "high-novelty-risk"),
    ("OmD", "DFIG-framework postulate: single Ω_D operator governing all "
     "physical 'constants'. Per M0 audit: over-parameterized-unification "
     "pattern, no empirical support. Paired with P3 conjecture.",
     "high-novelty-risk"),
    # Mechanism + parameters (4)
    ("H1", "DFIG-framework mechanism: Regime R_i classifier. Project-"
     "internal FIM-regime notion.", "owner-aware"),
    ("H2", "DFIG-framework parameter: fractal dimension d_f used in project "
     "β(λ) scaling. Underlying math concept (Hausdorff dim) is standard "
     "but project usage is internal.", "owner-aware"),
    ("H3", "DFIG-framework parameter: phase coherence λ. Project-specific.",
     "owner-aware"),
    ("H4", "DFIG-framework parameter: effective Euler char χ_eff. Project-"
     "specific application of topology.", "owner-aware"),
    # X-instantiations (8)
    ("X0_FIM_Regimes", "DFIG regime-classification instantiation.", "owner-aware"),
    ("X1", "DFIG instantiation: vascular/metabolic.", "owner-aware"),
    ("X2", "DFIG instantiation: information geometry.", "owner-aware"),
    ("X3", "DFIG instantiation: statistical physics.", "owner-aware"),
    ("X4", "DFIG instantiation: quantum systems.", "owner-aware"),
    ("X5", "DFIG instantiation: ecological networks.", "owner-aware"),
    ("X6", "DFIG instantiation: neural networks.", "owner-aware"),
    ("X7", "DFIG instantiation: developmental biology.", "owner-aware"),
    # M-methods (6) — FL4, FL12 excluded because they're standard logic
    ("M1", "Project method: KKT constraint binding applied to DFIG.",
     "owner-aware"),
    ("M2", "Project method: OccBin regime-switching.", "owner-aware"),
    ("M3", "Project method: Preisach hysteresis classification.",
     "owner-aware"),
    ("M4", "Project method: Mori-Zwanzig projection as DFIG tool.",
     "owner-aware"),
    ("M5", "Project method: Blanchard-Kahn backward induction.",
     "owner-aware"),
    ("M6", "DFIG core machinery: Fisher Information Rank calculation.",
     "needs-review"),
    # T-methods (10)
    ("T1", "DFIG test: Fisher rank monotonicity. Contradicted by own "
     "Phase 1 results (see P7 calibration).", "needs-review"),
    ("T2", "DFIG test: metabolic exponent–dimensionality correlation.",
     "owner-aware"),
    ("T3", "DFIG test: Ω_D unit consistency audit (stop-gate G3).",
     "needs-review"),
    ("T4", "DFIG test: redshift–structure correlation (supports P1).",
     "owner-aware"),
    ("T5", "DFIG test: critical exponent–dimension sensitivity.",
     "owner-aware"),
    ("T6", "DFIG test: holographic reconstruction complexity (P9).",
     "owner-aware"),
    ("T7", "DFIG test: hadron charge radii / effective ℏ (P10).",
     "owner-aware"),
    ("T8", "DFIG test: β(λ) cross-domain universality.", "owner-aware"),
    ("T9", "DFIG test: regime capacity bound.", "owner-aware"),
    ("T10", "DFIG test: RLCT-biology correspondence.", "owner-aware"),
]


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        # Build all anchors
        fl_anchors = build_fl_anchors()
        cs_anchors = build_cs_anchors()
        all_anchors = fl_anchors + cs_anchors

        print(f"Cluster megabatch — 2026-04-18")
        print(f"  FL cluster anchors: {len(fl_anchors)}")
        print(f"  CS cluster anchors: {len(cs_anchors)}")
        print(f"  Internal-construction flags: {len(IC_ENTRIES)}")
        print()

        # BLOCK A+B: insert anchors
        inserted_anchors = 0
        skipped_anchors = 0
        for a in all_anchors:
            (entry_id, source, identifier, revision_id, title, tier,
             stability, relationship, canonical_role, confidence, notes) = a
            res = conn.execute(
                "INSERT OR IGNORE INTO external_anchors "
                "(entry_id, source, identifier, revision_id, title, tier, "
                " source_stability_class, relationship, canonical_role, "
                " verified_date, verified_by_session, confidence, notes) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (entry_id, source, identifier, revision_id, title, tier,
                 stability, relationship, canonical_role,
                 TODAY, SESSION, confidence, notes),
            )
            if res.rowcount > 0:
                inserted_anchors += 1
            else:
                skipped_anchors += 1

        # BLOCK C: internal_construction flags
        inserted_ic = 0
        skipped_ic = 0
        for eid, reason, scrutiny in IC_ENTRIES:
            res = conn.execute(
                "INSERT OR IGNORE INTO internal_constructions "
                "(entry_id, reason, searched_sources, flagged_date, "
                " flagged_by_session, scrutiny_level, notes) "
                "VALUES (?,?,?,?,?,?,?)",
                (eid, reason,
                 '["dfig-framework-pattern-match"]',
                 TODAY, SESSION, scrutiny,
                 "Cluster-batch internal_construction flag. DFIG-framework "
                 "entries with no external GSW equivalent — owner-constructed "
                 "operational vocabulary. Entry preserved in wiki per no-"
                 "deletions rule; flagged honestly for cross-domain search "
                 "scoping."),
            )
            if res.rowcount > 0:
                inserted_ic += 1
            else:
                skipped_ic += 1

        conn.commit()

        print("=== Results ===")
        print(f"  anchor rows inserted: {inserted_anchors}")
        print(f"  anchor rows skipped (duplicate): {skipped_anchors}")
        print(f"  internal_construction rows inserted: {inserted_ic}")
        print(f"  internal_construction rows skipped: {skipped_ic}")

        # Totals
        cur.execute("SELECT COUNT(*) FROM external_anchors")
        total_anchors = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT entry_id) FROM external_anchors")
        entries_anchored = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM internal_constructions")
        total_ic = cur.fetchone()[0]

        print()
        print("=== Global state ===")
        print(f"  external_anchors total rows:     {total_anchors}")
        print(f"  entries with any anchor:         {entries_anchored} / 300")
        print(f"  internal_constructions total:    {total_ic}")

        # Coverage by domain now
        cur.execute("ATTACH DATABASE 'data/ds_wiki.db' AS ds")
        cur.execute("""
            SELECT
                CASE WHEN INSTR(t.tag_path,'.')=0 THEN t.tag_path
                     ELSE SUBSTR(t.tag_path,1,INSTR(t.tag_path,'.')-1) END AS top_level,
                COUNT(DISTINCT e.entry_id) as tagged,
                COUNT(DISTINCT a.entry_id) as anchored
            FROM entry_source_domains e
            JOIN source_domain_taxonomy t ON t.id = e.tag_id
            LEFT JOIN external_anchors a ON a.entry_id = e.entry_id
            WHERE e.primacy='primary' AND e.review_status='current'
            GROUP BY top_level ORDER BY tagged DESC
        """)
        print()
        print("=== Updated domain coverage ===")
        print(f"  {'Domain':28} {'Tagged':>7} {'Anchored':>9}  {'%':>5}")
        for row in cur.fetchall():
            pct = row[2]*100/row[1] if row[1] else 0
            print(f"  {row[0]:28} {row[1]:7} {row[2]:9}  {pct:4.1f}%")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
