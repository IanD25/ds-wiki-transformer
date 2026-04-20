"""
Insert math / info_theory / stats / B + A cluster anchors — 2026-04-20

27 entries:
  Anchored (24):  INFO2-5, IT02-08, B5, B1-4, MATH2-8, A1, A2, STAT2, C3
  Cites only (2): Q1, Q2 (wiki-internal open questions citing real ext work)
  IC (1):         Q5 (DFIG (1-λ)² synchronization cost — wiki-internal)

Template seed: INFO1 (Shannon/Khinchin/Cover-Thomas). Heavy reuse + many new
ISBNs marked medium pending WorldCat verify.

Discovered by the new gsw_lookup CLI demo (thermodynamics + info theory topic);
this batch closes the info_theory coverage gap + the wiki-hub B5 Landauer.

Run: python3 scripts/migrations/insert_math_info_cluster_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-math-info-cluster-2026-04-20"

# Reused (verified at INFO1 / QM1 / TD11 / NE03 / P21 prior batches)
ISBN_COVER_THOMAS = "978-0471241959"  # INFO1
ISBN_KHINCHIN     = "978-0486604343"  # INFO1
ISBN_VON_NEUMANN  = "978-0691178561"  # QM1
ISBN_ATKINS       = "978-0198769866"  # TD11
ISBN_REIF         = "978-1577666127"  # TD3
ISBN_JACKSON      = "978-0471309321"  # EM cluster
ISBN_AMARI_CHENT  = "978-0821805312"  # P21 fold-in? verify — using this for Amari-Nagaoka 2000 Methods of Info Geom

# DOIs from INFO1 for Shannon 1948 parts I + II
DOI_SHANNON_I     = "10.1002/j.1538-7305.1948.tb01338.x"
DOI_SHANNON_II    = "10.1002/j.1538-7305.1948.tb00917.x"
DOI_SEIFERT       = "10.1088/0034-4885/75/12/126001"  # NE03/NE04

# New textbook ISBNs — all medium pending WorldCat verify
ISBN_MACKAY       = "978-0521642989"  # MacKay Info Theory 2003
ISBN_NIELSEN_CHUANG = "978-1107002173"  # Nielsen-Chuang 10th anniv ed.
ISBN_RUDIN_PMA    = "978-0070542358"  # Rudin Principles of Math Analysis 3rd
ISBN_APOSTOL_MA   = "978-0201002881"  # Apostol Mathematical Analysis 2nd
ISBN_BILLINGSLEY  = "978-0471007104"  # Billingsley Probability and Measure 3rd
ISBN_HARDY_WRIGHT = "978-0199219865"  # Hardy-Wright Number Theory 6th
ISBN_LANG_ALG     = "978-0387953854"  # Lang Algebra 3rd
ISBN_SPIVAK_COM   = "978-0805390216"  # Spivak Calculus on Manifolds
ISBN_CONNES_NCG   = "978-0121858605"  # Connes 1994 Noncommutative Geometry


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ============================================================
    # INFORMATION THEORY (10 entries, incl. B5)
    # ============================================================

    # ── INFO2 — Shannon Source Coding Theorem ──
    ("INFO2", "doi", DOI_SHANNON_I, None,
     "Shannon 1948 A Mathematical Theory of Communication Pt I",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Shannon 1948 BSTJ 27, 379. Source coding theorem in §9. Reused from INFO1."),
    ("INFO2", "isbn", ISBN_COVER_THOMAS, None,
     "Cover-Thomas - Elements of Information Theory (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 5. Reused from INFO1."),
    ("INFO2", "isbn", ISBN_MACKAY, None,
     "MacKay - Information Theory, Inference, and Learning Algorithms",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "MacKay 2003 Ch. 4-6. ISBN claimed; verify WorldCat."),
    ("INFO2", "wikipedia",
     "https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem", None,
     "Shannon's source coding theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── INFO3 — Shannon Noisy-Channel Coding ──
    ("INFO3", "doi", DOI_SHANNON_II, None,
     "Shannon 1948 A Mathematical Theory of Communication Pt II",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Shannon 1948 BSTJ 27, 623. Noisy-channel coding theorem. Reused from INFO1."),
    ("INFO3", "isbn", ISBN_COVER_THOMAS, None,
     "Cover-Thomas - Elements of Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 7-8. Reused."),
    ("INFO3", "isbn", ISBN_MACKAY, None,
     "MacKay - Information Theory, Inference, and Learning Algorithms",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("INFO3", "wikipedia",
     "https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem", None,
     "Noisy-channel coding theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── INFO4 — Mutual Information & DPI ──
    ("INFO4", "doi", DOI_SHANNON_I, None,
     "Shannon 1948 A Mathematical Theory of Communication Pt I",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Mutual information I(X;Y) introduced in Shannon 1948. Reused."),
    ("INFO4", "isbn", ISBN_COVER_THOMAS, None,
     "Cover-Thomas - Elements of Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 2 (mutual info) + Ch. 2.8 (DPI). Reused."),
    ("INFO4", "isbn", ISBN_KHINCHIN, None,
     "Khinchin - Mathematical Foundations of Information Theory",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Reused from INFO1."),
    ("INFO4", "wikipedia",
     "https://en.wikipedia.org/wiki/Data_processing_inequality", None,
     "Data processing inequality",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── INFO5 — Kolmogorov Complexity ──
    ("INFO5", "doi", "10.1016/S0019-9958(64)90223-2", None,
     "Solomonoff 1964 A Formal Theory of Inductive Inference",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Solomonoff 1964 Information and Control 7, 1. First formulation. Elsevier DOI pattern. "
     "Kolmogorov 1965 Problems Inform. Transmission 1, 1 (Russian, no DOI) is the independent origin."),
    ("INFO5", "isbn", "978-3030112974", None,
     "Li-Vitanyi - An Introduction to Kolmogorov Complexity and Its Applications (4th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Li-Vitanyi 2019 Springer 4th. Definitive treatment. ISBN claimed; verify WorldCat."),
    ("INFO5", "wikipedia",
     "https://en.wikipedia.org/wiki/Kolmogorov_complexity", None,
     "Kolmogorov complexity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── IT02 — Von Neumann Entropy ──
    ("IT02", "isbn", ISBN_VON_NEUMANN, None,
     "von Neumann - Mathematical Foundations of Quantum Mechanics",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "von Neumann 1932. S(rho) = -Tr(rho log rho) defined in Ch. 5. Reused from QM1."),
    ("IT02", "isbn", ISBN_NIELSEN_CHUANG, None,
     "Nielsen-Chuang - Quantum Computation and Quantum Information",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Nielsen-Chuang 10th anniv. Ch. 11. ISBN claimed; verify WorldCat."),
    ("IT02", "wikipedia",
     "https://en.wikipedia.org/wiki/Von_Neumann_entropy", None,
     "Von Neumann entropy",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── IT03 — Kullback-Leibler Divergence ──
    ("IT03", "doi", "10.1214/aoms/1177729694", None,
     "Kullback-Leibler 1951 On Information and Sufficiency",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Kullback-Leibler 1951 Ann. Math. Stat. 22, 79. IMS DOI pattern."),
    ("IT03", "isbn", ISBN_COVER_THOMAS, None,
     "Cover-Thomas - Elements of Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 2. Reused."),
    ("IT03", "isbn", ISBN_MACKAY, None,
     "MacKay - Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("IT03", "wikipedia",
     "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence", None,
     "Kullback-Leibler divergence",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── IT04 — Quantum Relative Entropy ──
    ("IT04", "doi", "10.2996/kmj/1138844604", None,
     "Umegaki 1962 Conditional expectation in an operator algebra IV",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Umegaki 1962 Kodai Math. Sem. Rep. 14, 59. Quantum relative entropy defined. Project Euclid DOI pattern."),
    ("IT04", "doi", "10.1007/BF01646743", None,
     "Lindblad 1973 Entropy, information and quantum measurements",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Lindblad 1973 Comm. Math. Phys. 33, 305. Key inequality properties. Springer historic CMP DOI pattern."),
    ("IT04", "isbn", ISBN_NIELSEN_CHUANG, None,
     "Nielsen-Chuang - Quantum Computation and Quantum Information",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 11.3. Reused."),
    ("IT04", "wikipedia",
     "https://en.wikipedia.org/wiki/Quantum_relative_entropy", None,
     "Quantum relative entropy",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── IT05 — Fisher Information ──
    ("IT05", "doi", "10.1017/S0305004100009580", None,
     "Fisher 1925 Theory of Statistical Estimation",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Fisher 1925 Math. Proc. Camb. Phil. Soc. 22, 700. Cambridge UP DOI pattern."),
    ("IT05", "isbn", ISBN_AMARI_CHENT, None,
     "Amari-Nagaoka - Methods of Information Geometry (2000)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Amari-Nagaoka 2000 AMS. Ch. 2. ISBN claimed; verify WorldCat."),
    ("IT05", "wikipedia",
     "https://en.wikipedia.org/wiki/Fisher_information", None, "Fisher information",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── IT06 — Seifert Stochastic Thermodynamics ──
    ("IT06", "doi", DOI_SEIFERT, None,
     "Seifert 2012 Stochastic thermodynamics, fluctuation theorems and molecular machines",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Seifert 2012 Rep. Prog. Phys. 75, 126001. Reused from NE03/NE04."),
    ("IT06", "wikipedia",
     "https://en.wikipedia.org/wiki/Stochastic_thermodynamics", None,
     "Stochastic thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("IT06", "isbn", ISBN_REIF, None,
     "Reif - Fundamentals of Statistical and Thermal Physics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Background. Reused."),

    # ── IT08 — Fisher-Rao Metric ──
    # P21 already has Chentsov+Amari canonical_authority anchors; IT08 is distinct entry
    ("IT08", "isbn", ISBN_AMARI_CHENT, None,
     "Amari-Nagaoka - Methods of Information Geometry",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Rao 1945 Bull. Calcutta Math. Soc. 37, 81 (no DOI) is the progenitor. "
     "Amari-Nagaoka 2000 is the definitive modern treatment. ISBN claimed; verify."),
    ("IT08", "wikipedia",
     "https://en.wikipedia.org/wiki/Fisher_information_metric", None,
     "Fisher information metric",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("IT08", "isbn", ISBN_COVER_THOMAS, None,
     "Cover-Thomas - Elements of Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 11. Reused."),

    # ── B5 — Landauer's Principle (wiki-hub with 18 links) ──
    ("B5", "doi", "10.1147/rd.53.0183", None,
     "Landauer 1961 Irreversibility and Heat Generation in the Computing Process",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Landauer 1961 IBM J. Res. Dev. 5, 183. IBM journal DOI pattern. "
     "kT*ln(2) minimum energy cost per bit erasure."),
    ("B5", "isbn", ISBN_COVER_THOMAS, None,
     "Cover-Thomas - Elements of Information Theory",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Background on entropy-thermodynamic connection. Reused."),
    ("B5", "wikipedia",
     "https://en.wikipedia.org/wiki/Landauer%27s_principle", None,
     "Landauer's principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # MATHEMATICS (MATH + A)
    # ============================================================

    # ── MATH2 — Central Limit Theorem ──
    ("MATH2", "isbn", ISBN_BILLINGSLEY, None,
     "Billingsley - Probability and Measure (3rd ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Billingsley Ch. 27. Lindeberg 1922 + Lévy 1925 historical progenitors have no accessible DOIs. "
     "ISBN claimed; verify WorldCat."),
    ("MATH2", "isbn", ISBN_RUDIN_PMA, None,
     "Rudin - Principles of Mathematical Analysis (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "ISBN claimed; verify WorldCat."),
    ("MATH2", "wikipedia",
     "https://en.wikipedia.org/wiki/Central_limit_theorem", None, "Central limit theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── MATH3 — Law of Large Numbers ──
    ("MATH3", "isbn", ISBN_BILLINGSLEY, None,
     "Billingsley - Probability and Measure",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Billingsley Ch. 6 + 22. Bernoulli 1713 Ars Conjectandi is historical."),
    ("MATH3", "wikipedia",
     "https://en.wikipedia.org/wiki/Law_of_large_numbers", None, "Law of large numbers",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("MATH3", "isbn", ISBN_RUDIN_PMA, None,
     "Rudin - Principles of Mathematical Analysis",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── MATH5 — Fundamental Theorem of Calculus ──
    ("MATH5", "isbn", ISBN_RUDIN_PMA, None,
     "Rudin - Principles of Mathematical Analysis",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 6 (Riemann-Stieltjes integration). Reused."),
    ("MATH5", "isbn", ISBN_APOSTOL_MA, None,
     "Apostol - Mathematical Analysis (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 7. ISBN claimed; verify WorldCat."),
    ("MATH5", "wikipedia",
     "https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus", None,
     "Fundamental theorem of calculus",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── MATH6 — Prime Number Theorem ──
    ("MATH6", "isbn", ISBN_HARDY_WRIGHT, None,
     "Hardy-Wright - An Introduction to the Theory of Numbers (6th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 22. Hadamard 1896 Bull. SMF 24, 199 + de la Vallée Poussin 1896 (no DOIs). "
     "ISBN claimed; verify WorldCat."),
    ("MATH6", "wikipedia",
     "https://en.wikipedia.org/wiki/Prime_number_theorem", None, "Prime number theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── MATH7 — Euler's Identity / Formula ──
    ("MATH7", "isbn", ISBN_RUDIN_PMA, None,
     "Rudin - Principles of Mathematical Analysis",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 8 (exp, sin, cos series). Euler 1748 Introductio historical. Reused."),
    ("MATH7", "wikipedia",
     "https://en.wikipedia.org/wiki/Euler%27s_identity", None, "Euler's identity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("MATH7", "isbn", ISBN_APOSTOL_MA, None,
     "Apostol - Mathematical Analysis",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── MATH8 — Generalized Stokes' Theorem ──
    ("MATH8", "isbn", ISBN_SPIVAK_COM, None,
     "Spivak - Calculus on Manifolds",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Spivak 1965 Ch. 5. Classical rigorous treatment. ISBN claimed; verify WorldCat."),
    ("MATH8", "wikipedia",
     "https://en.wikipedia.org/wiki/Generalized_Stokes_theorem", None,
     "Generalized Stokes theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── A1 — Square-Cube Law ──
    ("A1", "isbn", ISBN_REIF, None,
     "Reif - Fundamentals of Statistical and Thermal Physics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Context for surface/volume scaling. Galileo 1638 Two New Sciences is the historical origin. Reused."),
    ("A1", "wikipedia",
     "https://en.wikipedia.org/wiki/Square%E2%80%93cube_law", None,
     "Square-cube law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("A1", "isbn", "978-0521319874", None,
     "Schmidt-Nielsen - Scaling",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Biological relevance. Reused from C1."),

    # ── A2 — Richardson Effect (fractal measurement) ──
    ("A2", "doi", "10.1126/science.156.3775.636", None,
     "Mandelbrot 1967 How Long Is the Coast of Britain?",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Mandelbrot 1967 Science 156, 636. AAAS DOI pattern. "
     "Richardson's empirical result (1961) formalized."),
    ("A2", "wikipedia",
     "https://en.wikipedia.org/wiki/How_Long_Is_the_Coast_of_Britain%3F_Statistical_Self-Similarity_and_Fractional_Dimension", None,
     "How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("A2", "isbn", "978-0716711865", None,
     "Mandelbrot - The Fractal Geometry of Nature",
     1, "canonical", "canonical_authority", "comprehensive_survey", "medium",
     "Mandelbrot 1982 Freeman. ISBN claimed; verify WorldCat."),

    # ============================================================
    # STATS (STAT2, C3)
    # ============================================================

    # ── STAT2 — Ergodic Theorem ──
    ("STAT2", "doi", "10.1073/pnas.17.2.656", None,
     "Birkhoff 1931 Proof of the Ergodic Theorem",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Birkhoff 1931 PNAS 17, 656. PNAS DOI pattern."),
    ("STAT2", "isbn", ISBN_BILLINGSLEY, None,
     "Billingsley - Probability and Measure",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Ch. 24. Reused."),
    ("STAT2", "wikipedia",
     "https://en.wikipedia.org/wiki/Ergodic_theorem", None, "Ergodic theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── C3 — Heavy-Tailed Distributions ──
    ("C3", "doi", "10.1080/00107510500052444", None,
     "Newman 2005 Power laws, Pareto distributions and Zipf's law",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Newman 2005 Contemp. Phys. 46, 323. Taylor & Francis DOI pattern. "
     "Definitive modern review unifying Pareto/Zipf/lognormal/stretched-exp."),
    ("C3", "doi", "10.1086/294632", None,
     "Mandelbrot 1963 The Variation of Certain Speculative Prices",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Mandelbrot 1963 J. Business 36, 394. UChicago Press DOI pattern. "
     "Foundational for heavy-tailed distributions in finance/economics."),
    ("C3", "wikipedia",
     "https://en.wikipedia.org/wiki/Heavy-tailed_distribution", None,
     "Heavy-tailed distribution",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # B-SERIES (B1-4) — classical physics laws
    # ============================================================

    # ── B1 — Radioactive Decay (Gamow Tunneling) ──
    ("B1", "doi", "10.1007/BF01343196", None,
     "Gamow 1928 Zur Quantentheorie des Atomkernes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Gamow 1928 Z. Phys. 51, 204. Alpha decay via quantum tunneling. "
     "Springer historic Z.Phys. DOI pattern."),
    ("B1", "isbn", ISBN_REIF, None,
     "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Background on decay statistics. Reused."),
    ("B1", "wikipedia",
     "https://en.wikipedia.org/wiki/Gamow_factor", None, "Gamow factor",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── B2 — Arrhenius Equation ──
    ("B2", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry (11th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Atkins Ch. 21. Arrhenius 1889 Z. phys. Chem. 4, 226 has no DOI. Reused."),
    ("B2", "isbn", ISBN_REIF, None,
     "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("B2", "wikipedia",
     "https://en.wikipedia.org/wiki/Arrhenius_equation", None, "Arrhenius equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── B3 — Wien Displacement Law ──
    ("B3", "isbn", ISBN_REIF, None,
     "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 9. Wien 1893 Sitzungsber. Preuss. Akad. Wiss. has no DOI. Reused."),
    ("B3", "wikipedia",
     "https://en.wikipedia.org/wiki/Wien%27s_displacement_law", None,
     "Wien's displacement law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── B4 — Rayleigh Scattering ──
    ("B4", "isbn", ISBN_JACKSON, None,
     "Jackson - Classical Electrodynamics (3rd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Jackson Ch. 10. Rayleigh 1871 Phil. Mag. 41, 107 has no DOI. Reused from EM cluster."),
    ("B4", "wikipedia",
     "https://en.wikipedia.org/wiki/Rayleigh_scattering", None, "Rayleigh scattering",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # Q1, Q2 — wiki-internal open questions; `cites` real external work
    # ============================================================

    # ── Q1 — cites Kovchegov-Zaliapin 2019 (partial result for Tokunaga trees) ──
    ("Q1", "doi", "10.1214/17-PS101", None,
     "Kovchegov-Zaliapin 2019 Random self-similar trees (Probability Surveys)",
     1, "canonical", "cites", None, "medium",
     "Q1 asks whether d_f = 1 + alpha for branching processes with P(r) ~ r^(-alpha). "
     "Kovchegov-Zaliapin 2019 prove this for Tokunaga self-similar trees specifically. "
     "relationship=cites, canonical_role=NULL (CHECK constraint). "
     "DOI pattern for IMS Probability Surveys; verify via CrossRef."),

    # ── Q2 — cites Connes 1994 spectral triples ──
    ("Q2", "isbn", ISBN_CONNES_NCG, None,
     "Connes - Noncommutative Geometry (1994)",
     1, "canonical", "cites", None, "medium",
     "Q2 asks about spectral triple (A, H, D) effective Poincaré-Hopf framework. "
     "Connes 1994 NCG is the canonical reference for spectral triples. "
     "relationship=cites. ISBN claimed; verify WorldCat."),
]


# Internal_construction flags
IC_FLAGS = [
    ("Q5",
     "Q5: Information Cost of Synchronization — wiki-internal open question "
     "about DFIG (1-lambda)^2 synchronization cost scaling. Tied to wiki's "
     "d_f / lambda parameter program. Owner-derived framing, not standalone "
     "literature. (Physical plausibility argument in entry cites harmonic-"
     "oscillator energy wells but the specific cost functional is wiki-native.)",
     "owner-aware"),
]


ENTRIES_ANCHORED = (
    "INFO2", "INFO3", "INFO4", "INFO5",
    "IT02", "IT03", "IT04", "IT05", "IT06", "IT08",
    "B5", "B1", "B2", "B3", "B4",
    "MATH2", "MATH3", "MATH5", "MATH6", "MATH7", "MATH8",
    "A1", "A2", "STAT2", "C3",
    "Q1", "Q2",  # cites-only but still anchored
)
ENTRIES_IC = ("Q5",)


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        all_entries = ENTRIES_ANCHORED + ENTRIES_IC
        for eid in all_entries:
            n = cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            ).fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
        print(f"Pre-flight OK: all {len(all_entries)} entries tagged.")
        print()

        print(f"Inserting {len(ANCHORS)} anchor rows...")
        inserted = skipped = 0
        for a in ANCHORS:
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
                inserted += 1
            else:
                skipped += 1
        print(f"  Anchors inserted: {inserted}, skipped: {skipped}")

        print(f"\nFlagging {len(IC_FLAGS)} entries as internal_construction...")
        ic_inserted = ic_skipped = 0
        for (eid, reason, scrutiny) in IC_FLAGS:
            res = conn.execute(
                "INSERT OR IGNORE INTO internal_constructions "
                "(entry_id, reason, searched_sources, flagged_date, "
                " flagged_by_session, scrutiny_level, notes) "
                "VALUES (?,?,?,?,?,?,?)",
                (eid, reason,
                 '["wiki-content-inspection-2026-04-20"]',
                 TODAY, SESSION, scrutiny,
                 "Flagged after reading entry content; DFIG-internal framing."),
            )
            if res.rowcount > 0:
                ic_inserted += 1
            else:
                ic_skipped += 1
        print(f"  IC inserted: {ic_inserted}, skipped: {ic_skipped}")

        conn.commit()
        print()

        # Per-entry summary
        print("=== Per-entry anchor counts ===")
        for eid in ENTRIES_ANCHORED:
            n = cur.execute(
                "SELECT COUNT(*) FROM external_anchors WHERE entry_id=?", (eid,),
            ).fetchone()[0]
            slots = cur.execute(
                "SELECT COUNT(DISTINCT canonical_role) FROM external_anchors "
                "WHERE entry_id=? AND canonical_role IS NOT NULL", (eid,),
            ).fetchone()[0]
            below_min = " *** BELOW 3-MIN" if n < 3 else ""
            print(f"  {eid:<6}  {n:>2} anchors / {slots} slots filled{below_min}")
        print(f"\n  IC flagged: {', '.join(ENTRIES_IC)}")

        # Totals
        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        ic_total = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM internal_constructions"
        ).fetchone()[0]
        print(f"\nTotals after this batch:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")
        print(f"  internal_constructions:  {ic_total}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
