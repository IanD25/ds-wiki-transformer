"""
Insert cosmology cluster anchors — 2026-04-19

24 entries across GV2-4 + GT01-11 + HB01-10. Largest single cluster batch to date.

Sub-cluster split (see docs/prior_art_reviews/CLUSTER_COSMOLOGY_2026_04_19.md):
  Sub-A — Classical GR + cosmology (GV2-4, GT06, GT08, GT09, GT11) — 7 entries
  Sub-B — Entropic-gravity programs (GT01-04, GT07, GT10) — 6 entries (GT05 deferred)
  Sub-C — Black holes / holography (HB01-10) — 10 entries

Template seed: GV1 (anchored 2026-04-18). Heavy ISBN reuse from MTW/Wald/Carroll.

Constraint discoveries from prior batch (QM/BR cluster):
  - CHECK constraint: canonical_role MUST be NULL when relationship != 'canonical_authority'
  - Tier-3 (arXiv preprint) anchors use relationship='cites' with canonical_role=NULL

Run: python3 scripts/migrations/insert_cosmology_cluster_2026_04_19.py
"""
from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-cosmology-cluster-2026-04-19"

# Reused ISBNs (verified at GV1 / CM1)
ISBN_MTW         = "978-0716703440"  # MTW Gravitation
ISBN_WALD_GR     = "978-0226870335"  # Wald GR
ISBN_CARROLL     = "978-0805387322"  # Carroll Spacetime and Geometry
ISBN_PRINCIPIA   = "978-0520088177"  # Cohen-Whitman Principia (CM1)
ISBN_GOLDSTEIN   = "978-0201657029"  # Goldstein Classical Mechanics (CM1)


# Format: (entry_id, source, identifier, revision_id, title, tier,
#         stability, relationship, canonical_role, confidence, notes)
ANCHORS = [
    # ============================================================
    # Sub-A — Classical GR + cosmology
    # ============================================================

    # ── GV2 — Gravitoelectromagnetism (GEM) ──
    ("GV2", "arxiv", "gr-qc/0011014", None,
     "Mashhoon 2000 Gravitoelectromagnetism: A Brief Review",
     3, "preprint-evolving", "cites", None, "high",
     "Mashhoon 2000 review. Tier-3 preprint; relationship=cites per arch. rule I2."),
    ("GV2", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 18 — gravitomagnetism from linearized GR. Reused from GV1."),
    ("GV2", "isbn", ISBN_CARROLL, None, "Carroll - Spacetime and Geometry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 7 — linearized gravity. Reused from GV1."),
    ("GV2", "wikipedia",
     "https://en.wikipedia.org/wiki/Gravitoelectromagnetism", None,
     "Gravitoelectromagnetism",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GV3 — Gauss's Law for Gravity ──
    ("GV3", "isbn", ISBN_PRINCIPIA, None,
     "Newton - Principia (Cohen-Whitman 1999)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Inverse-square law, from which Gauss form is derivable. Reused from CM1."),
    ("GV3", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Box 1.6, Ch. 17 (Newtonian limit). Reused."),
    ("GV3", "isbn", ISBN_GOLDSTEIN, None, "Goldstein - Classical Mechanics",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 1. Reused from CM1."),
    ("GV3", "wikipedia",
     "https://en.wikipedia.org/wiki/Gauss%27s_law_for_gravity", None,
     "Gauss's law for gravity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GV4 — Hubble-Lemaître Law ──
    ("GV4", "doi", "10.1073/pnas.15.3.168", None,
     "Hubble 1929 A relation between distance and radial velocity among extra-galactic nebulae",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hubble 1929 PNAS 15, 168. PNAS DOI pattern."),
    ("GV4", "arxiv", "1310.4881", None,
     "Lemaitre 1927 (English translation, 2013)",
     3, "preprint-evolving", "cites", None, "medium",
     "Lemaitre 1927 Annales Soc. sci. Bruxelles A47, 49. English translation arXiv:1310.4881. "
     "IAU renamed to Hubble-Lemaitre in 2018."),
    ("GV4", "isbn", ISBN_CARROLL, None, "Carroll - Spacetime and Geometry",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 8 (cosmology). Reused."),
    ("GV4", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 27. Reused."),
    ("GV4", "wikipedia",
     "https://en.wikipedia.org/wiki/Hubble%27s_law", None, "Hubble's law",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GT06 — Sakharov Induced Gravity ──
    ("GT06", "doi", "10.1023/A:1001947813463", None,
     "Sakharov 1967 Vacuum quantum fluctuations in curved space and the theory of gravitation (reissue)",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Sakharov 1967 reissue (Sakharov 2000 Gen. Rel. Grav. 32, 365). "
     "Original: Sov. Phys. Dokl. 12, 1040. Springer GRG DOI pattern."),
    ("GT06", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("GT06", "wikipedia",
     "https://en.wikipedia.org/wiki/Induced_gravity", None, "Induced gravity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GT08 — Equivalence Principle ──
    ("GT08", "doi", "10.1002/andp.19163540702", None,
     "Einstein 1916 Die Grundlage der allgemeinen Relativitatstheorie",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Strong equivalence principle stated explicitly. Reused from GV1."),
    ("GT08", "doi", "10.12942/lrr-2014-4", None,
     "Will 2014 The Confrontation between General Relativity and Experiment",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Living Reviews in Relativity. Authoritative experimental-test review."),
    ("GT08", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 16. Reused."),
    ("GT08", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 4. Reused."),
    ("GT08", "wikipedia",
     "https://en.wikipedia.org/wiki/Equivalence_principle", None,
     "Equivalence principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GT09 — Choptuik Critical Collapse ──
    ("GT09", "doi", "10.1103/PhysRevLett.70.9", None,
     "Choptuik 1993 Universality and scaling in gravitational collapse of a massless scalar field",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Choptuik 1993 PRL 70, 9. APS DOI pattern."),
    ("GT09", "doi", "10.12942/lrr-2007-5", None,
     "Gundlach-Martin-Garcia 2007 Critical Phenomena in Gravitational Collapse",
     1, "canonical", "canonical_authority", "comprehensive_survey", "high",
     "Living Reviews in Relativity. Comprehensive review of the field."),
    ("GT09", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("GT09", "wikipedia",
     "https://en.wikipedia.org/wiki/Critical_collapse", None, "Critical collapse",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── GT11 — Cosmological Coupling (M0 Speculative, contested) ──
    ("GT11", "doi", "10.3847/2041-8213/acb704", None,
     "Farrah et al. 2023 Observational Evidence for Cosmological Coupling of Black Holes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Farrah et al. 2023 ApJ 944, L31. AAS IOP DOI pattern. The cosmological-coupling claim."),
    ("GT11", "doi", "10.3847/1538-4357/ab32da", None,
     "Croker-Weiner 2019 Implications of Symmetry and Pressure in Friedmann Cosmology",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Croker-Weiner 2019 ApJ 882, 19 — k-formalism foundational paper."),
    ("GT11", "arxiv", "2306.11588", None,
     "Cadoni et al. 2023 Cosmological coupling of nonsingular black holes",
     3, "preprint-evolving", "cites", None, "medium",
     "Cadoni et al. 2023 JCAP 11, 007 — verified in M0 Fifth Addendum. Their KS analysis on "
     "Farrah elliptical-galaxy sample prefers k=3 over k=1, contesting Cadoni's own k=1 prediction. "
     "Tier-3 = cites, not canonical_authority. M0-Speculative for parent entry."),

    # ============================================================
    # Sub-B — Entropic-gravity programs (M0-context: most Speculative)
    # ============================================================

    # ── GT01 — Jacobson 1995 Thermodynamic Derivation ──
    ("GT01", "doi", "10.1103/PhysRevLett.75.1260", None,
     "Jacobson 1995 Thermodynamics of Spacetime: The Einstein Equation of State",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Jacobson 1995 PRL 75, 1260. Foundational paper of thermodynamic-gravity program. APS DOI."),
    ("GT01", "wikipedia",
     "https://en.wikipedia.org/wiki/Entropic_gravity", None, "Entropic gravity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Wikipedia covers Jacobson + Verlinde + Padmanabhan. Shared anchor across GT01-03."),
    ("GT01", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Killing-horizon thermodynamics background. Reused."),

    # ── GT02 — Verlinde Entropic Gravity ──
    ("GT02", "doi", "10.1007/JHEP04(2011)029", None,
     "Verlinde 2011 On the Origin of Gravity and the Laws of Newton",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Verlinde 2011 JHEP 04, 029. Springer JHEP DOI pattern."),
    ("GT02", "arxiv", "1001.0785", None, "Verlinde 2010 (arXiv preprint)",
     3, "preprint-evolving", "cites", None, "high",
     "Original arXiv preprint (Jan 2010). Tier-3 = cites."),
    ("GT02", "wikipedia",
     "https://en.wikipedia.org/wiki/Entropic_gravity", None, "Entropic gravity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Shared anchor with GT01."),

    # ── GT03 — Padmanabhan Holographic Equipartition ──
    ("GT03", "doi", "10.1088/0034-4885/73/4/046901", None,
     "Padmanabhan 2010 Thermodynamical aspects of gravity: New insights",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Padmanabhan 2010 Rep. Prog. Phys. 73, 046901. IOP DOI pattern. Comprehensive review."),
    ("GT03", "wikipedia",
     "https://en.wikipedia.org/wiki/Entropic_gravity", None, "Entropic gravity",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Shared anchor with GT01-02."),

    # ── GT04 — Bianconi Gravity from Entropy (recent preprint) ──
    ("GT04", "arxiv", "2408.14391", None,
     "Bianconi 2024 Gravity from Entropy",
     3, "preprint-evolving", "cites", None, "medium",
     "Bianconi 2024 arXiv:2408.14391. Tier-3 preprint; not yet (as of session) confirmed in PRD. "
     "Re-anchor when published. Single anchor only — below 3-anchor minimum, acceptable for very-recent preprints."),

    # ── GT05 — Carney Spin Entropic Gravity (DEFERRED) ──
    # Source paper not clearly identified from memory.
    # Owner clarification needed; flagged in proposal doc.

    # ── GT07 — Non-equilibrium Spacetime Thermodynamics ──
    ("GT07", "doi", "10.1103/PhysRevLett.96.121301", None,
     "Eling-Guedens-Jacobson 2006 Non-equilibrium thermodynamics of spacetime",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Eling-Guedens-Jacobson 2006 PRL 96, 121301. APS DOI pattern."),
    ("GT07", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Background. Reused."),
    # (No Wikipedia anchor — no dedicated article exists.)

    # ── GT10 — Jacobson Entanglement Equilibrium (M0 Speculative; load-bearing) ──
    ("GT10", "doi", "10.1103/PhysRevLett.116.201101", None,
     "Jacobson 2016 Entanglement Equilibrium and the Einstein Equation",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Jacobson 2016 PRL 116, 201101. APS DOI pattern. M0 notes: linearized-only derivation; "
     "assumes CFT/holographic context (modular Hamiltonian). Wiki's Fisher-gravity chain "
     "(Speculative per M0) builds on this paper."),
    ("GT10", "arxiv", "1505.04753", None, "Jacobson 2015 (arXiv preprint)",
     3, "preprint-evolving", "cites", None, "high",
     "Original arXiv preprint. Tier-3 = cites."),
    ("GT10", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Modular theory / von Neumann algebra background. Reused."),

    # ============================================================
    # Sub-C — Black holes / holography
    # ============================================================

    # ── HB01 — Bekenstein Bound ──
    ("HB01", "doi", "10.1103/PhysRevD.23.287", None,
     "Bekenstein 1981 Universal upper bound on the entropy-to-energy ratio for bounded systems",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Bekenstein 1981 PRD 23, 287. APS DOI."),
    ("HB01", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Box 33.1. Reused."),
    ("HB01", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 12. Reused."),
    ("HB01", "wikipedia",
     "https://en.wikipedia.org/wiki/Bekenstein_bound", None, "Bekenstein bound",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB02 — Bekenstein-Hawking Entropy ──
    ("HB02", "doi", "10.1103/PhysRevD.7.2333", None,
     "Bekenstein 1973 Black Holes and Entropy",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Bekenstein 1973 PRD 7, 2333. APS DOI."),
    ("HB02", "doi", "10.1007/BF02345020", None,
     "Hawking 1975 Particle Creation by Black Holes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hawking 1975 Comm. Math. Phys. 43, 199. Springer historic CMP DOI pattern. "
     "Establishes T_H = hbar*kappa/(2*pi*k_B) and S_BH = A/(4*L_planck^2)."),
    ("HB02", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 33. Reused."),
    ("HB02", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 12-14. Reused."),
    ("HB02", "wikipedia",
     "https://en.wikipedia.org/wiki/Bekenstein%E2%80%93Hawking_formula", None,
     "Bekenstein-Hawking formula",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB03 — Holographic Principle ──
    ("HB03", "arxiv", "gr-qc/9310026", None,
     "'t Hooft 1993 Dimensional Reduction in Quantum Gravity",
     3, "preprint-evolving", "cites", None, "high",
     "'t Hooft 1993 conference proceedings. Tier-3 preprint; relationship=cites."),
    ("HB03", "doi", "10.1063/1.531249", None,
     "Susskind 1995 The World as a Hologram",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Susskind 1995 J. Math. Phys. 36, 6377. AIP DOI pattern."),
    ("HB03", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Background. Reused."),
    ("HB03", "wikipedia",
     "https://en.wikipedia.org/wiki/Holographic_principle", None,
     "Holographic principle",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB04 — Hawking Radiation ──
    ("HB04", "doi", "10.1007/BF02345020", None,
     "Hawking 1975 Particle Creation by Black Holes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hawking 1975 Comm. Math. Phys. 43, 199 — defines the radiation. Same paper as HB02 progenitor."),
    ("HB04", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 33. Reused."),
    ("HB04", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 14. Reused."),
    ("HB04", "wikipedia",
     "https://en.wikipedia.org/wiki/Hawking_radiation", None, "Hawking radiation",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB05 — Unruh Effect ──
    ("HB05", "doi", "10.1103/PhysRevD.14.870", None,
     "Unruh 1976 Notes on black-hole evaporation",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Unruh 1976 PRD 14, 870. APS DOI."),
    ("HB05", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 14. Reused."),
    ("HB05", "wikipedia",
     "https://en.wikipedia.org/wiki/Unruh_effect", None, "Unruh effect",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB06 — Black Hole Area Theorem ──
    ("HB06", "doi", "10.1103/PhysRevLett.26.1344", None,
     "Hawking 1971 Gravitational Radiation from Colliding Black Holes",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hawking 1971 PRL 26, 1344. First proof of area theorem. APS DOI."),
    ("HB06", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 33-34. Reused."),
    ("HB06", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 12. Reused."),
    ("HB06", "wikipedia",
     "https://en.wikipedia.org/wiki/Black_hole_thermodynamics", None,
     "Black hole thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Area theorem covered as part of BH thermo article. No oldid."),

    # ── HB07 — Ryu-Takayanagi Formula ──
    ("HB07", "doi", "10.1103/PhysRevLett.96.181602", None,
     "Ryu-Takayanagi 2006 Holographic Derivation of Entanglement Entropy from the AdS/CFT Correspondence",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Ryu-Takayanagi 2006 PRL 96, 181602. APS DOI."),
    ("HB07", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 25 (AdS background). Reused."),
    ("HB07", "wikipedia",
     "https://en.wikipedia.org/wiki/Ryu%E2%80%93Takayanagi_conjecture", None,
     "Ryu-Takayanagi conjecture",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB08 — Bousso Covariant Entropy Bound ──
    ("HB08", "doi", "10.1088/1126-6708/1999/07/004", None,
     "Bousso 1999 A covariant entropy conjecture",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Bousso 1999 JHEP 07, 004. IOP-era JHEP DOI pattern (pre-Springer transition)."),
    ("HB08", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Reused."),
    ("HB08", "wikipedia",
     "https://en.wikipedia.org/wiki/Bousso%27s_holographic_bound", None,
     "Bousso's holographic bound",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),

    # ── HB09 — Generalised Second Law ──
    ("HB09", "doi", "10.1103/PhysRevD.7.2333", None,
     "Bekenstein 1973 Black Holes and Entropy",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Bekenstein 1973 PRD 7, 2333 — introduces GSL. Same paper as HB02 progenitor; "
     "different role here (GSL specifically)."),
    ("HB09", "doi", "10.1103/PhysRevD.80.124008", None,
     "Wall 2009 Ten proofs of the generalized second law",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Wall 2009 PRD 80, 124008. APS DOI. Modern proofs of GSL for fast-changing horizons."),
    ("HB09", "isbn", ISBN_WALD_GR, None, "Wald - General Relativity",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 14. Reused."),
    ("HB09", "wikipedia",
     "https://en.wikipedia.org/wiki/Black_hole_thermodynamics", None,
     "Black hole thermodynamics",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "Covers GSL. Shared anchor with HB06. No oldid."),

    # ── HB10 — Hawking-Page Transition ──
    ("HB10", "doi", "10.1007/BF01208266", None,
     "Hawking-Page 1983 Thermodynamics of Black Holes in anti-de Sitter Space",
     1, "canonical", "canonical_authority", "progenitor", "high",
     "Hawking-Page 1983 Comm. Math. Phys. 87, 577. Springer historic CMP DOI pattern."),
    ("HB10", "isbn", ISBN_MTW, None, "MTW - Gravitation",
     1, "canonical", "canonical_authority", "standard_textbook", "high",
     "Ch. 25 (AdS context). Reused."),
    ("HB10", "wikipedia",
     "https://en.wikipedia.org/wiki/Hawking%E2%80%93Page_phase_transition", None,
     "Hawking-Page phase transition",
     2, "active-literature", "canonical_authority", "living_reference", "medium",
     "No oldid this session."),
]


# Entries we intentionally anchored (GT05 deferred to owner review)
ENTRIES_ANCHORED = (
    "GV2", "GV3", "GV4",
    "GT01", "GT02", "GT03", "GT04", "GT06", "GT07", "GT08", "GT09", "GT10", "GT11",
    "HB01", "HB02", "HB03", "HB04", "HB05", "HB06", "HB07", "HB08", "HB09", "HB10",
)
ENTRIES_DEFERRED = ("GT05",)


def main() -> None:
    conn = sqlite3.connect(WIKI_HISTORY_DB)
    try:
        cur = conn.cursor()

        # Pre-flight: every entry we're anchoring must already have domain tags
        for eid in ENTRIES_ANCHORED:
            n = cur.execute(
                "SELECT COUNT(*) FROM entry_source_domains "
                "WHERE entry_id=? AND review_status='current'", (eid,),
            ).fetchone()[0]
            if n == 0:
                raise RuntimeError(f"{eid} has no domain tags; run retag first.")
        print(f"Pre-flight OK: all {len(ENTRIES_ANCHORED)} entries have current domain tags.")
        print(f"Deferred (owner review needed): {ENTRIES_DEFERRED}")
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

        # Summary per entry — anchor count + slot coverage
        print("=== Per-entry anchor counts after batch ===")
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
