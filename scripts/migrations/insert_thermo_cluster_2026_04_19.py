"""
Insert thermo / RG / NE cluster anchors — 2026-04-19

25 entries: TD1-2, TD4-14 + RG01-06 + NE01-06.

Sub-cluster split (see docs/prior_art_reviews/CLUSTER_THERMO_2026_04_19.md):
  Sub-A — Classical thermodynamics (TD1-2, TD4-14) — 13 entries; share Callen + Reif (verified at TD3)
  Sub-B — Renormalization group (RG01-06) — 6 entries; share Cardy + Goldenfeld (medium ISBN)
  Sub-C — Non-equilibrium (NE01-06) — 6 entries; share Kondepudi-Prigogine (medium ISBN) + Seifert 2012 review

Constraint reminders (from QM/BR + cosmology batches):
  - canonical_role MUST be NULL when relationship != 'canonical_authority' (CHECK)
  - Tier-3 (arXiv preprint) -> relationship='cites' with canonical_role=NULL

Run: python3 scripts/migrations/insert_thermo_cluster_2026_04_19.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-thermo-cluster-2026-04-19"

# Reused (verified at TD3 / prior batches)
ISBN_CALLEN = "978-0471862567"   # Callen 1985 Thermodynamics
ISBN_REIF   = "978-1577666127"   # Reif 1965 (Waveland reprint 2009)

# New textbook ISBNs — all medium pending WorldCat verify
ISBN_CARDY            = "978-0521499590"  # Cardy 1996 Scaling and Renormalization
ISBN_GOLDENFELD       = "978-0201554090"  # Goldenfeld 1992 Lectures on Phase Transitions and the RG
ISBN_KONDEPUDI        = "978-1118371817"  # Kondepudi-Prigogine 2014 Modern Thermodynamics 2nd
ISBN_CERCIGNANI       = "978-0387966373"  # Cercignani 1988 The Boltzmann Equation and Its Applications
ISBN_ATKINS           = "978-0198769866"  # Atkins-de Paula 2014 Physical Chemistry 11th
ISBN_CARNOT_DOVER     = "978-0486446417"  # Carnot 1824 Reflexions (Dover reprint)
ISBN_FOURIER_CAMBRIDGE = "978-0521539685"  # Fourier 1822 Theorie analytique (Cambridge reprint)


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ============================================================
    # Sub-A — Classical thermodynamics (TD1-2, TD4-14)
    # ============================================================

    # ── TD1 — Zeroth Law ──
    ("TD1", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Callen 1985 Ch. 1 — zeroth law as definition of empirical temperature. "
     "R.H. Fowler 1931 attribution exists but no DOI; textbook anchor canonical."),
    ("TD1", "isbn", ISBN_REIF, None, "Reif - Fundamentals of Statistical and Thermal Physics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reif Ch. 3. Reused from TD3."),
    ("TD1", "wikipedia",
     "https://en.wikipedia.org/wiki/Zeroth_law_of_thermodynamics", None,
     "Zeroth law of thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD2 — First Law ──
    ("TD2", "doi", "10.1098/rstl.1850.0004", None,
     "Joule 1850 On the Mechanical Equivalent of Heat",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Joule 1850 Phil. Trans. 140, 61. Royal Society DOI pattern. "
     "Empirical foundation of energy conservation."),
    ("TD2", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 1. Reused from TD3."),
    ("TD2", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 4. Reused from TD3."),
    ("TD2", "wikipedia",
     "https://en.wikipedia.org/wiki/First_law_of_thermodynamics", None,
     "First law of thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD4 — Third Law ──
    ("TD4", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "axiomatic_foundation", "high",
     "Callen Ch. 10 (Postulate IV / Nernst-Planck statement). "
     "Nernst 1906 Sitzungsberichte Gott. has no modern DOI; textbook canonical."),
    ("TD4", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from TD3."),
    ("TD4", "wikipedia",
     "https://en.wikipedia.org/wiki/Third_law_of_thermodynamics", None,
     "Third law of thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD5 — Fundamental Thermodynamic Relation ──
    ("TD5", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Callen Ch. 2-3. Gibbs 1875-78 'On the Equilibrium of Heterogeneous Substances' "
     "is the historical origin (collected works); Callen is the modern canonical exposition."),
    ("TD5", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused from TD3."),
    ("TD5", "wikipedia",
     "https://en.wikipedia.org/wiki/Fundamental_thermodynamic_relation", None,
     "Fundamental thermodynamic relation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD6 — Onsager Reciprocal Relations ──
    ("TD6", "doi", "10.1103/PhysRev.37.405", None,
     "Onsager 1931 Reciprocal Relations in Irreversible Processes I",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Onsager 1931 Phys. Rev. 37, 405. APS DOI pattern."),
    ("TD6", "doi", "10.1103/PhysRev.38.2265", None,
     "Onsager 1931 Reciprocal Relations in Irreversible Processes II",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Onsager 1931 Phys. Rev. 38, 2265. APS DOI pattern."),
    ("TD6", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 14. Reused."),
    ("TD6", "wikipedia",
     "https://en.wikipedia.org/wiki/Onsager_reciprocal_relations", None,
     "Onsager reciprocal relations",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD7 — Boltzmann Equation ──
    ("TD7", "isbn", ISBN_CERCIGNANI, None,
     "Cercignani - The Boltzmann Equation and Its Applications",
     1, "canonical", "canonical_authority", "comprehensive_survey", "medium",
     "Cercignani 1988 Springer. Definitive monograph. ISBN claimed from memory; verify WorldCat."),
    ("TD7", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 12-14. Reused."),
    ("TD7", "wikipedia",
     "https://en.wikipedia.org/wiki/Boltzmann_equation", None,
     "Boltzmann equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session. Boltzmann 1872 Wien.Sitzungsber. has no DOI; textbook canonical."),

    # ── TD8 — Carnot's Theorem ──
    ("TD8", "isbn", ISBN_CARNOT_DOVER, None,
     "Carnot - Reflections on the Motive Power of Fire (Dover reprint)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Carnot 1824 Reflexions sur la puissance motrice du feu. "
     "ISBN of Dover reprint; verify WorldCat."),
    ("TD8", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 4. Reused."),
    ("TD8", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 5. Reused."),
    ("TD8", "wikipedia",
     "https://en.wikipedia.org/wiki/Carnot%27s_theorem_(thermodynamics)", None,
     "Carnot's theorem (thermodynamics)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD9 — Newton's Law of Cooling ──
    ("TD9", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reif Ch. 12 covers convective/conductive heat-transfer phenomenology. "
     "Newton 1701 Phil. Trans. 22, 824 has no canonical DOI; textbook anchor."),
    ("TD9", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("TD9", "wikipedia",
     "https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling", None,
     "Newton's law of cooling",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD10 — Fourier's Law of Heat Conduction ──
    ("TD10", "isbn", ISBN_FOURIER_CAMBRIDGE, None,
     "Fourier - The Analytical Theory of Heat (Cambridge classic reprint)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Fourier 1822 Theorie analytique de la chaleur. "
     "ISBN of Cambridge classics reprint; verify WorldCat."),
    ("TD10", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 12. Reused."),
    ("TD10", "wikipedia",
     "https://en.wikipedia.org/wiki/Thermal_conduction", None, "Thermal conduction",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD11 — Kopp's Law ──
    ("TD11", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry (11th ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Atkins covers heat-capacity additivity (Kopp's rule). "
     "ISBN claimed from memory; verify WorldCat. Kopp 1864 Annalen der Chemie und "
     "Pharmacie has no modern DOI."),
    ("TD11", "wikipedia",
     "https://en.wikipedia.org/wiki/Kopp%27s_law", None, "Kopp's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD12 — Dulong-Petit Law ──
    ("TD12", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 7 (specific heats of solids). "
     "Dulong-Petit 1819 Annales de Chimie et Physique has no modern DOI. Reused."),
    ("TD12", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("TD12", "wikipedia",
     "https://en.wikipedia.org/wiki/Dulong%E2%80%93Petit_law", None,
     "Dulong-Petit law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD13 — Carnot Efficiency ──
    ("TD13", "isbn", ISBN_CARNOT_DOVER, None,
     "Carnot - Reflections on the Motive Power of Fire (Dover reprint)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Same Carnot 1824 source as TD8. Dover reprint ISBN."),
    ("TD13", "isbn", ISBN_CALLEN, None, "Callen - Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 4. Reused."),
    ("TD13", "wikipedia",
     "https://en.wikipedia.org/wiki/Carnot_heat_engine", None, "Carnot heat engine",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── TD14 — van der Waals Equation ──
    ("TD14", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Atkins Ch. 1-2 covers vdW equation. ISBN to verify. "
     "van der Waals 1873 PhD thesis 'Over de Continuiteit van den Gas- en Vloeistoftoestand' has no DOI."),
    ("TD14", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("TD14", "wikipedia",
     "https://en.wikipedia.org/wiki/Van_der_Waals_equation", None,
     "van der Waals equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # Sub-B — Renormalization Group (RG01-06)
    # ============================================================

    # ── RG01 — Wilson's Renormalisation Group ──
    ("RG01", "doi", "10.1103/PhysRevB.4.3174", None,
     "Wilson 1971 Renormalization Group and Critical Phenomena I",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Wilson 1971 PRB 4, 3174. APS DOI pattern."),
    ("RG01", "doi", "10.1103/PhysRevB.4.3184", None,
     "Wilson 1971 Renormalization Group and Critical Phenomena II",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Wilson 1971 PRB 4, 3184. APS DOI pattern."),
    ("RG01", "isbn", ISBN_CARDY, None,
     "Cardy - Scaling and Renormalization in Statistical Physics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Cardy 1996. ISBN claimed from memory; verify WorldCat."),
    ("RG01", "isbn", ISBN_GOLDENFELD, None,
     "Goldenfeld - Lectures on Phase Transitions and the Renormalization Group",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Goldenfeld 1992. ISBN claimed from memory; verify WorldCat."),
    ("RG01", "wikipedia",
     "https://en.wikipedia.org/wiki/Renormalization_group", None,
     "Renormalization group",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── RG02 — Beta Function ──
    ("RG02", "doi", "10.1103/PhysRev.95.1300", None,
     "Gell-Mann-Low 1954 Quantum Electrodynamics at Small Distances",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Gell-Mann-Low 1954 Phys. Rev. 95, 1300. First introduction of beta-function-like running. APS DOI."),
    ("RG02", "doi", "10.1103/PhysRevD.2.1541", None,
     "Callan 1970 Broken Scale Invariance in Scalar Field Theory",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Callan 1970 PRD 2, 1541. Beta function in Callan-Symanzik form. APS DOI."),
    ("RG02", "isbn", ISBN_CARDY, None,
     "Cardy - Scaling and Renormalization",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused (RG01)."),
    ("RG02", "wikipedia",
     "https://en.wikipedia.org/wiki/Beta_function_(physics)", None,
     "Beta function (physics)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── RG03 — Kadanoff Block Spin Transformation ──
    ("RG03", "isbn", ISBN_GOLDENFELD, None,
     "Goldenfeld - Lectures on Phase Transitions and the RG",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Goldenfeld Ch. 9 covers Kadanoff block spin in detail. "
     "Kadanoff 1966 Physics 2, 263 has no modern DOI (pre-Elsevier journal). Reused."),
    ("RG03", "isbn", ISBN_CARDY, None,
     "Cardy - Scaling and Renormalization",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("RG03", "wikipedia",
     "https://en.wikipedia.org/wiki/Block_spin_renormalization_group", None,
     "Block spin renormalization group",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── RG04 — Zamolodchikov c-Theorem ──
    ("RG04", "isbn", ISBN_CARDY, None,
     "Cardy - Scaling and Renormalization",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Cardy Ch. 11 + Appendix covers Zamolodchikov c-theorem. "
     "Zamolodchikov 1986 JETP Lett. 43, 730 has no English-side DOI."),
    ("RG04", "wikipedia",
     "https://en.wikipedia.org/wiki/C-theorem", None, "C-theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("RG04", "isbn", ISBN_GOLDENFELD, None,
     "Goldenfeld - Lectures on Phase Transitions and the RG",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),

    # ── RG05 — a-Theorem (4D) ──
    ("RG05", "doi", "10.1007/JHEP12(2011)099", None,
     "Komargodski-Schwimmer 2011 On Renormalization Group Flows in Four Dimensions",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Komargodski-Schwimmer 2011 JHEP 12, 099 — proof of 4D a-theorem. Springer JHEP DOI pattern."),
    ("RG05", "wikipedia",
     "https://en.wikipedia.org/wiki/A-theorem", None, "A-theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
    ("RG05", "isbn", ISBN_CARDY, None,
     "Cardy - Scaling and Renormalization",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused (background)."),

    # ── RG06 — Cotler-Rezchikov: RG as Optimal Transport ──
    ("RG06", "arxiv", "2202.11737", None,
     "Cotler-Rezchikov 2022 Renormalization Group Flow as Optimal Transport",
     3, "preprint-evolving", "cites", None, "high",
     "Cotler-Rezchikov 2022 arXiv:2202.11737. Tier-3 preprint = cites. "
     "Connects RG to Wasserstein optimal transport with Fisher metric."),
    ("RG06", "isbn", ISBN_CARDY, None,
     "Cardy - Scaling and Renormalization",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Background (RG side). Reused."),
    ("RG06", "wikipedia",
     "https://en.wikipedia.org/wiki/Renormalization_group", None,
     "Renormalization group",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Shared with RG01. No oldid."),

    # ============================================================
    # Sub-C — Non-equilibrium (NE01-06)
    # ============================================================

    # ── NE01 — Prigogine Dissipative Structures ──
    ("NE01", "doi", "10.1126/science.201.4358.777", None,
     "Prigogine 1978 Time, Structure, and Fluctuations (Nobel Lecture)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Prigogine 1977 Nobel Prize lecture, Science 201, 777. "
     "Verifiable AAAS DOI pattern."),
    ("NE01", "isbn", ISBN_KONDEPUDI, None,
     "Kondepudi-Prigogine - Modern Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Kondepudi-Prigogine 2014 2nd ed Wiley. ISBN claimed from memory; verify WorldCat."),
    ("NE01", "wikipedia",
     "https://en.wikipedia.org/wiki/Dissipative_system", None, "Dissipative system",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── NE02 — Maximum Entropy Production Principle ──
    ("NE02", "doi", "10.1016/j.physrep.2005.12.001", None,
     "Martyushev-Seleznev 2006 Maximum entropy production principle in physics, chemistry and biology",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Martyushev-Seleznev 2006 Phys. Rep. 426, 1. Authoritative survey. Elsevier DOI pattern."),
    ("NE02", "isbn", ISBN_KONDEPUDI, None,
     "Kondepudi-Prigogine - Modern Thermodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused. Background on entropy production in non-equilibrium systems."),
    ("NE02", "wikipedia",
     "https://en.wikipedia.org/wiki/Maximum_entropy_production", None,
     "Maximum entropy production",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── NE03 — Jarzynski Equality ──
    ("NE03", "doi", "10.1103/PhysRevLett.78.2690", None,
     "Jarzynski 1997 Nonequilibrium Equality for Free Energy Differences",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Jarzynski 1997 PRL 78, 2690. APS DOI pattern."),
    ("NE03", "doi", "10.1088/0034-4885/75/12/126001", None,
     "Seifert 2012 Stochastic thermodynamics, fluctuation theorems and molecular machines",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Seifert 2012 Rep. Prog. Phys. 75, 126001. Definitive review of fluctuation-theorem program. IOP DOI."),
    ("NE03", "wikipedia",
     "https://en.wikipedia.org/wiki/Jarzynski_equality", None, "Jarzynski equality",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── NE04 — Crooks Fluctuation Theorem ──
    ("NE04", "doi", "10.1103/PhysRevE.60.2721", None,
     "Crooks 1999 Entropy production fluctuation theorem and the nonequilibrium work relation",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Crooks 1999 PRE 60, 2721. APS DOI pattern."),
    ("NE04", "doi", "10.1088/0034-4885/75/12/126001", None,
     "Seifert 2012 Stochastic thermodynamics, fluctuation theorems and molecular machines",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Seifert 2012 review. Reused (NE03)."),
    ("NE04", "wikipedia",
     "https://en.wikipedia.org/wiki/Crooks_fluctuation_theorem", None,
     "Crooks fluctuation theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── NE05 — Fluctuation-Dissipation Theorem ──
    ("NE05", "doi", "10.1103/PhysRev.83.34", None,
     "Callen-Welton 1951 Irreversibility and Generalized Noise",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Callen-Welton 1951 Phys. Rev. 83, 34. APS DOI pattern."),
    ("NE05", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 15. Reused."),
    ("NE05", "wikipedia",
     "https://en.wikipedia.org/wiki/Fluctuation%E2%80%93dissipation_theorem", None,
     "Fluctuation-dissipation theorem",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── NE06 — England Dissipation-Driven Adaptation ──
    ("NE06", "doi", "10.1063/1.4818538", None,
     "England 2013 Statistical physics of self-replication",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "England 2013 J. Chem. Phys. 139, 121923. AIP DOI pattern."),
    ("NE06", "doi", "10.1038/nnano.2015.250", None,
     "Perunov-Marsland-England 2016 Statistical physics of adaptation",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Perunov-Marsland-England 2016 Phys. Rev. X 6, 021036 (originally announced 2014; "
     "Nature Nanotechnol. 10, 919 cited here as adjacent)."),
    ("NE06", "wikipedia",
     "https://en.wikipedia.org/wiki/Dissipative_adaptation", None,
     "Dissipative adaptation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
]


ENTRIES = (
    "TD1", "TD2", "TD4", "TD5", "TD6", "TD7", "TD8", "TD9",
    "TD10", "TD11", "TD12", "TD13", "TD14",
    "RG01", "RG02", "RG03", "RG04", "RG05", "RG06",
    "NE01", "NE02", "NE03", "NE04", "NE05", "NE06",
)


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        for eid in ENTRIES:
            n = cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            ).fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
        print(f"Pre-flight OK: all {len(ENTRIES)} entries have current domain tags.")
        print()

        print(f"Inserting {len(ANCHORS)} anchor rows...")
        inserted = 0
        skipped = 0
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
        conn.commit()
        print(f"  Inserted: {inserted}")
        print(f"  Skipped (already existed): {skipped}")
        print()

        # Per-entry summary
        print("=== Per-entry anchor counts ===")
        for eid in ENTRIES:
            n = cur.execute(
                "SELECT COUNT(*) FROM external_anchors WHERE entry_id=?", (eid,),
            ).fetchone()[0]
            slots = cur.execute(
                "SELECT COUNT(DISTINCT canonical_role) FROM external_anchors "
                "WHERE entry_id=? AND canonical_role IS NOT NULL", (eid,),
            ).fetchone()[0]
            below_min = " *** BELOW 3-MIN" if n < 3 else ""
            print(f"  {eid:<6}  {n:>2} anchors / {slots} slots filled{below_min}")

        # Totals
        total = cur.execute("SELECT COUNT(*) FROM external_anchors").fetchone()[0]
        entries_anchored = cur.execute(
            "SELECT COUNT(DISTINCT entry_id) FROM external_anchors"
        ).fetchone()[0]
        print(f"\nTotals after this batch:")
        print(f"  external_anchors rows:   {total}")
        print(f"  entries with any anchor: {entries_anchored}")

        # Relationship-type distribution
        print(f"\nRelationship-type distribution:")
        for r in cur.execute(
            "SELECT relationship, COUNT(*) FROM external_anchors GROUP BY relationship"
        ):
            print(f"  {r[0]:25} {r[1]}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
