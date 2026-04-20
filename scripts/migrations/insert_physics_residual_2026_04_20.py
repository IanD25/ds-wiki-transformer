"""
Insert physics-residual cluster anchors — 2026-04-20

26 entries total (the remaining physics gap):
  Anchor (24): FM1-7, OP1-6, GL1-5, RD1-3, DM1, STAT3
  IC (2):      G1 (Dimensional Redshift — DFIG), G3 (Holographic Complexity Bound — DFIG)

STAT3 is M0-load-bearing (CCA): anchored to Machta 2013, Brown 2022, Borgs-Chayes 1996,
Vinayak 2014 per M0 audit findings. Corresponds to the wiki's central research thread.

Run: python3 scripts/migrations/insert_physics_residual_2026_04_20.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-physics-residual-2026-04-20"

# Reused (verified at prior batches)
ISBN_ATKINS    = "978-0198769866"  # CHEM1, TD11
ISBN_REIF      = "978-1577666127"  # TD3
ISBN_JACKSON   = "978-0471309321"  # EM
ISBN_GRIFFITHS_EM = "978-1108420419"  # EM (B4)
ISBN_BROWN_GEN = "978-0134414232"  # KC8/9/10 chemistry batch
ISBN_GOLDSTEIN = "978-0201657029"  # CM1

# New textbook ISBNs — medium pending WorldCat verify
ISBN_BATCHELOR  = "978-0521663960"  # Batchelor Fluid Dynamics
ISBN_LL_FLUID   = "978-0750627672"  # Landau-Lifshitz Vol 6 Fluid Mechanics
ISBN_HECHT      = "978-0133977226"  # Hecht Optics 5th
ISBN_BORN_WOLF  = "978-0521642224"  # Born-Wolf Principles of Optics
ISBN_CRANK      = "978-0198533443"  # Crank Mathematics of Diffusion
ISBN_SETHNA     = "978-0198865247"  # Sethna Statistical Mechanics 2nd


ANCHORS = [
    # ============================================================
    # FM — Fluid Mechanics
    # ============================================================

    # ── FM1 Navier-Stokes ──
    ("FM1", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Batchelor 1967 Cambridge UP. Standard derivation. "
     "Navier 1822 + Stokes 1845 historical (no DOIs). ISBN claimed; verify."),
    ("FM1", "isbn", ISBN_LL_FLUID, None,
     "Landau-Lifshitz Vol 6 - Fluid Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "ISBN claimed; verify WorldCat."),
    ("FM1", "wikipedia",
     "https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations", None,
     "Navier-Stokes equations",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── FM2 Bernoulli's Principle ──
    ("FM2", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Bernoulli 1738 Hydrodynamica historical book (no DOI). "
     "Batchelor §3.5. Reused."),
    ("FM2", "isbn", ISBN_LL_FLUID, None,
     "Landau-Lifshitz Vol 6 - Fluid Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("FM2", "wikipedia",
     "https://en.wikipedia.org/wiki/Bernoulli%27s_principle", None,
     "Bernoulli's principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── FM3 Euler Fluid Equations ──
    ("FM3", "isbn", ISBN_LL_FLUID, None,
     "Landau-Lifshitz Vol 6 - Fluid Mechanics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Landau-Lifshitz §1-2. Euler 1757 historical. Reused."),
    ("FM3", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("FM3", "wikipedia",
     "https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)", None,
     "Euler equations (fluid dynamics)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── FM4 Poiseuille's Law ──
    ("FM4", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Batchelor §4.2. Poiseuille 1840-1846 Mémoires de l'Académie has no online DOI. Reused."),
    ("FM4", "isbn", ISBN_LL_FLUID, None,
     "Landau-Lifshitz Vol 6 - Fluid Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("FM4", "wikipedia",
     "https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation", None,
     "Hagen-Poiseuille equation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── FM5 Stokes' Law ──
    ("FM5", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Batchelor §4.9. Stokes 1851 Trans. Camb. Phil. Soc. 9, 8 (no online DOI). Reused."),
    ("FM5", "isbn", ISBN_LL_FLUID, None,
     "Landau-Lifshitz Vol 6 - Fluid Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("FM5", "wikipedia",
     "https://en.wikipedia.org/wiki/Stokes%27_law", None, "Stokes' law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── FM6 Faxén's Law ──
    ("FM6", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Batchelor + Russel-Saville-Schowalter Colloidal Dispersions cover Faxén formulas. "
     "Faxén 1922 Annalen der Physik historical. Reused."),
    ("FM6", "isbn", ISBN_LL_FLUID, None,
     "Landau-Lifshitz Vol 6 - Fluid Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("FM6", "wikipedia",
     "https://en.wikipedia.org/wiki/Fax%C3%A9n%27s_law", None, "Faxén's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── FM7 Darcy's Law ──
    ("FM7", "isbn", ISBN_BATCHELOR, None,
     "Batchelor - An Introduction to Fluid Dynamics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Darcy 1856 Les fontaines publiques de la ville de Dijon has no online DOI. Reused."),
    ("FM7", "isbn", "978-1107006539", None,
     "Turcotte-Schubert - Geodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Background on porous flow in geological context. Reused from earth-sciences batch."),
    ("FM7", "wikipedia",
     "https://en.wikipedia.org/wiki/Darcy%27s_law", None, "Darcy's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # OP — Optics
    # ============================================================

    # ── OP1 Fermat's Principle ──
    ("OP1", "isbn", ISBN_HECHT, None,
     "Hecht - Optics (5th ed.)",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Hecht §4.5 covers Fermat's principle of least time. "
     "Fermat 1657 historical, no DOI. ISBN claimed; verify."),
    ("OP1", "isbn", ISBN_BORN_WOLF, None,
     "Born-Wolf - Principles of Optics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Born-Wolf §3.3. ISBN claimed; verify WorldCat."),
    ("OP1", "wikipedia",
     "https://en.wikipedia.org/wiki/Fermat%27s_principle", None, "Fermat's principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── OP2 Law of Reflection ──
    ("OP2", "isbn", ISBN_HECHT, None,
     "Hecht - Optics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Hecht Ch. 4. Euclid's Catoptrics historical (ancient). Reused."),
    ("OP2", "isbn", ISBN_JACKSON, None,
     "Jackson - Classical Electrodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 7 (boundary conditions for E/M waves). Reused from EM cluster."),
    ("OP2", "wikipedia",
     "https://en.wikipedia.org/wiki/Specular_reflection", None, "Specular reflection",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── OP3 Snell's Law ──
    ("OP3", "isbn", ISBN_HECHT, None,
     "Hecht - Optics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Hecht §4.4. Snell 1621 historical (Ibn Sahl 984 anteceded). Reused."),
    ("OP3", "isbn", ISBN_JACKSON, None,
     "Jackson - Classical Electrodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 7. Reused."),
    ("OP3", "wikipedia",
     "https://en.wikipedia.org/wiki/Snell%27s_law", None, "Snell's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── OP4 Brewster's Angle ──
    ("OP4", "isbn", ISBN_HECHT, None,
     "Hecht - Optics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Hecht §8.6. Brewster 1815 Phil. Trans. Roy. Soc. 105, 125 may have DOI; not WebFetch-verified. Reused."),
    ("OP4", "isbn", ISBN_JACKSON, None,
     "Jackson - Classical Electrodynamics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 7 (Fresnel coefficients → Brewster). Reused."),
    ("OP4", "wikipedia",
     "https://en.wikipedia.org/wiki/Brewster%27s_angle", None, "Brewster's angle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── OP5 Malus's Law ──
    ("OP5", "isbn", ISBN_HECHT, None,
     "Hecht - Optics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Hecht Ch. 8 polarization. Malus 1809 Mémoires Soc. d'Arcueil 2, 143 historical. Reused."),
    ("OP5", "isbn", ISBN_BORN_WOLF, None,
     "Born-Wolf - Principles of Optics",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("OP5", "wikipedia",
     "https://en.wikipedia.org/wiki/Polarizer", None, "Polarizer (covers Malus's law)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Wikipedia Malus's Law content is in the Polarizer article. No oldid."),

    # ── OP6 Beer-Lambert Law ──
    ("OP6", "isbn", ISBN_HECHT, None,
     "Hecht - Optics",
     1, "canonical", "canonical_authority", "progenitor", "medium",
     "Hecht §3.5. Beer 1852 + Bouguer-Lambert 1729-1760 historical. Reused."),
    ("OP6", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Spectroscopy chapter. Reused."),
    ("OP6", "wikipedia",
     "https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law", None, "Beer-Lambert law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # GL — Gas Laws (combination law + 4 historical components)
    # ============================================================

    # ── GL1 Ideal Gas Law ──
    ("GL1", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 1. Combination of Boyle/Charles/Avogadro into PV=nRT; Clapeyron 1834 first integrated form. Reused."),
    ("GL1", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 5. Reused."),
    ("GL1", "wikipedia",
     "https://en.wikipedia.org/wiki/Ideal_gas_law", None, "Ideal gas law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GL2 Boyle's Law ──
    ("GL2", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Atkins Ch. 1. Boyle 1662 historical (no DOI). Reused."),
    ("GL2", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("GL2", "wikipedia",
     "https://en.wikipedia.org/wiki/Boyle%27s_law", None, "Boyle's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GL3 Charles's Law ──
    ("GL3", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Charles 1787 unpublished; reported by Gay-Lussac 1802 (no DOI). Reused."),
    ("GL3", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("GL3", "wikipedia",
     "https://en.wikipedia.org/wiki/Charles%27s_law", None, "Charles's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GL4 Gay-Lussac's Law ──
    ("GL4", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Gay-Lussac 1809 Mém. Soc. d'Arcueil 2, 207 historical (no DOI). Reused."),
    ("GL4", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("GL4", "wikipedia",
     "https://en.wikipedia.org/wiki/Gay-Lussac%27s_law", None, "Gay-Lussac's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GL5 Avogadro's Law ──
    ("GL5", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Avogadro 1811 J. Phys. Chim. 73, 58 historical (no DOI). Reused."),
    ("GL5", "isbn", ISBN_BROWN_GEN, None,
     "Brown-LeMay - Chemistry: The Central Science",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Reused."),
    ("GL5", "wikipedia",
     "https://en.wikipedia.org/wiki/Avogadro%27s_law", None, "Avogadro's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # RD — Radiation
    # ============================================================

    # ── RD1 Planck's Law of Black-Body Radiation ──
    ("RD1", "doi", "10.1002/andp.19013090310", None,
     "Planck 1901 Ueber das Gesetz der Energieverteilung im Normalspectrum",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Planck 1901 Annalen der Physik 309, 553. Wiley Annalen DOI pattern."),
    ("RD1", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 9. Reused."),
    ("RD1", "wikipedia",
     "https://en.wikipedia.org/wiki/Planck%27s_law", None, "Planck's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── RD2 Stefan-Boltzmann Law ──
    ("RD2", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Reif Ch. 9. Stefan 1879 + Boltzmann 1884 historical (no DOIs). Reused."),
    ("RD2", "isbn", ISBN_ATKINS, None,
     "Atkins-de Paula - Physical Chemistry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("RD2", "wikipedia",
     "https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law", None,
     "Stefan-Boltzmann law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── RD3 Planck-Einstein Relation ──
    ("RD3", "doi", "10.1002/andp.19013090310", None,
     "Planck 1901 Energieverteilung im Normalspectrum (E = h nu introduced)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Planck 1901 Annalen der Physik 309, 553. Same paper as RD1; introduces E = h*nu. Reused."),
    ("RD3", "doi", "10.1002/andp.19053220607", None,
     "Einstein 1905 Heuristische Gesichtspunkt betreffend die Erzeugung und Verwandlung des Lichtes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Einstein 1905 Annalen der Physik 17, 132 — photoelectric effect paper; uses E=h*nu for photon. "
     "Wiley Annalen DOI pattern."),
    ("RD3", "isbn", ISBN_REIF, None, "Reif - Fundamentals",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("RD3", "wikipedia",
     "https://en.wikipedia.org/wiki/Planck%E2%80%93Einstein_relation", None,
     "Planck-Einstein relation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # DM — Diffusion
    # ============================================================

    # ── DM1 Fick's Laws of Diffusion ──
    ("DM1", "doi", "10.1002/andp.18551700105", None,
     "Fick 1855 Ueber Diffusion",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Fick 1855 Annalen der Physik 170, 59. Wiley Annalen DOI pattern."),
    ("DM1", "isbn", ISBN_CRANK, None,
     "Crank - The Mathematics of Diffusion (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Crank 1975 Oxford UP. Definitive treatment of diffusion equation. ISBN claimed; verify."),
    ("DM1", "wikipedia",
     "https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion", None,
     "Fick's laws of diffusion",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ============================================================
    # STAT3 — CCA Class (M0-LOAD-BEARING)
    # ============================================================

    # ── STAT3 Constrained Critical Attractor (CCA) Class ──
    # M0 has identified Machta 2013 as the general-setting prior art; Vinayak 2014
    # for correlation-matrix RMT; Borgs-Chayes 1996 for Potts covariance; Brown 2022
    # for the closest broader-program prior art. CCA's narrow novelty (per-site fields
    # + d_eff/eta + T-sweep + first-order Potts) is Speculative per M0 calibration.
    ("STAT3", "doi", "10.1126/science.1238723", None,
     "Machta-Chachra-Transtrum-Sethna 2013 Parameter Space Compression Underlies Emergent Theories and Predictive Models",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Machta 2013 Science 339, 933. AAAS DOI pattern. M0-identified general-setting prior art. "
     "FIM eigenvalue spectrum on Ising at criticality — uses global couplings, not per-site fields."),
    ("STAT3", "arxiv", "1403.7218", None,
     "Vinayak-Prosen-Buca-Seligman 2014 Spectral statistics of corrected Wishart-like ensembles",
     3, "preprint-evolving", "cites", None, "high",
     "Vinayak 2014 EPL 108, 20006. M0 Fifth Addendum — proves correlation matrix eigenvalue density "
     "at 2D Ising criticality is power-law from eta_critical. Tier-3 = cites."),
    ("STAT3", "arxiv", "adap-org/9411001", None,
     "Borgs-Chayes 1996 The covariance matrix of the Potts model: a random-cluster analysis",
     3, "preprint-evolving", "cites", None, "high",
     "Borgs-Chayes 1996 J. Stat. Phys. 82, 1235. M0 Fifth Addendum. Rigorous Potts covariance ↔ FK clusters."),
    ("STAT3", "isbn", ISBN_SETHNA, None,
     "Sethna - Statistical Mechanics: Entropy, Order Parameters, and Complexity (2nd ed.)",
     1, "canonical", "canonical_authority", "standard_textbook", "medium",
     "Sethna 2021 Oxford UP 2nd ed. Sloppy-models program context. ISBN claimed; verify WorldCat."),
    ("STAT3", "wikipedia",
     "https://en.wikipedia.org/wiki/Critical_phenomena", None,
     "Critical phenomena (general background)",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Background. CCA is wiki-specific construction; no dedicated Wikipedia article. No oldid."),
]


# Internal_construction flags
IC_FLAGS = [
    ("G1",
     "G1: Dimensional Redshift Law — DFIG-framework alternative to metric expansion. "
     "Wiki claims cosmological redshift is energy attenuation traversing a D_eff gradient "
     "in a static multi-scale graph (not metric expansion). Owner-derived heterodox claim "
     "tied to wiki's D_eff parameter program. M0 calibration: Speculative.",
     "high-novelty-risk"),
    ("G3",
     "G3: Holographic Complexity Bound — DFIG-framework-derived specific bound (>= 2^Omega(n)) "
     "on bulk-from-boundary reconstruction complexity. Cites Bekenstein-Hawking and AdS/CFT "
     "literature but the specific bound is wiki-internal, not the published "
     "Susskind 2014 / Brown-Susskind 2018 complexity-volume claim.",
     "high-novelty-risk"),
]


ENTRIES_ANCHORED = (
    "FM1", "FM2", "FM3", "FM4", "FM5", "FM6", "FM7",
    "OP1", "OP2", "OP3", "OP4", "OP5", "OP6",
    "GL1", "GL2", "GL3", "GL4", "GL5",
    "RD1", "RD2", "RD3",
    "DM1", "STAT3",
)
ENTRIES_IC = ("G1", "G3")


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
                 "DFIG-framework wiki-internal construction; preserved per no-deletions rule."),
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
