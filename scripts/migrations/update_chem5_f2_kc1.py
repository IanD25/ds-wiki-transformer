"""
Migration: update CHEM5, F2, KC1 with metabolic network context from primary sources.

Sources:
  CHEM5: Orth, Thiele & Palsson (2010) "What is flux balance analysis?" Nat Biotech 28:245
  F2:    Monod (1949) "The Growth of Bacterial Cultures" Ann Rev Microbiol 3:371
  KC1:   Atkins Physical Chemistry (textbook basis) — van't Hoff / delta-G quantitative form

Run: PYTHONUTF8=1 .venv/Scripts/python.exe scripts/migrations/update_chem5_f2_kc1.py
"""

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DB = ROOT / "data" / "ds_wiki.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()


# ─────────────────────────────────────────────────────────────────────────────
# CHEM5 — add new section "Metabolic Network Instantiation"
# Source: Orth, Thiele & Palsson (2010), Box 1 and pp. 1–2
# ─────────────────────────────────────────────────────────────────────────────

CHEM5_NEW_SECTION_NAME = "Metabolic Network Instantiation"
CHEM5_NEW_SECTION_CONTENT = (
    "In metabolic reaction networks, mass action is expressed through the stoichiometric matrix S "
    "(m metabolites × n reactions), where each column encodes the stoichiometric coefficients of one "
    "reaction — negative for consumed metabolites, positive for produced metabolites (Orth, Thiele & Palsson, "
    "2010, Nature Biotechnology 28:245). At steady state, the mass balance condition S·v = 0 holds for every "
    "metabolite simultaneously: the total flux into each metabolite pool equals the total flux out. This is "
    "mass action applied to the full reaction network rather than a single reaction. The flux vector v (length n) "
    "is further constrained by upper and lower bounds on each reaction rate: lb ≤ v ≤ ub, where exchange "
    "reactions (substrate uptake) set the primary capacity limits. For E. coli aerobic growth on glucose, "
    "the binding constraint is the glucose uptake bound — set to a physiologically realistic maximum of "
    "18.5 mmol gDW⁻¹ hr⁻¹ — not oxygen availability (Orth et al. 2010, p. 2). Flux balance analysis (FBA) "
    "solves the linear program: maximize Z = c^T v subject to S·v = 0 and lb ≤ v ≤ ub. The stoichiometric "
    "matrix S is the algebraic encoding of mass action constraints across the entire metabolic network; the "
    "Guldberg–Waage rate law for individual reactions and the steady-state network constraint S·v = 0 are "
    "the same law operating at different scales."
)

# Check if section already exists
exists = cur.execute(
    "SELECT id FROM sections WHERE entry_id='CHEM5' AND section_name=?",
    (CHEM5_NEW_SECTION_NAME,)
).fetchone()

if exists:
    print(f"[SKIP] CHEM5 / {CHEM5_NEW_SECTION_NAME} already exists — skipping insert")
else:
    # Get max section_order for CHEM5
    max_order = cur.execute(
        "SELECT MAX(section_order) FROM sections WHERE entry_id='CHEM5'"
    ).fetchone()[0]
    cur.execute(
        "INSERT INTO sections (entry_id, section_name, content, section_order) VALUES (?,?,?,?)",
        ("CHEM5", CHEM5_NEW_SECTION_NAME, CHEM5_NEW_SECTION_CONTENT, max_order + 1)
    )
    print(f"[OK] CHEM5 / {CHEM5_NEW_SECTION_NAME} inserted at order {max_order + 1}")

# Update CHEM5 concept tags to include metabolic network terms
CHEM5_NEW_TAGS = (
    "mass action\nreaction rate law\nrate constant\nreaction order\nequilibrium constant\n"
    "Arrhenius kinetics\nGuldberg Waage\nconcentration dependence\nfirst order reaction\n"
    "chemical kinetics\nstoichiometric matrix\nflux balance analysis\nmetabolic network\n"
    "steady state constraint\nS·v=0\nsubstrate uptake\nFBA"
)
cur.execute(
    "UPDATE sections SET content=? WHERE entry_id='CHEM5' AND section_name='Concept Tags'",
    (CHEM5_NEW_TAGS,)
)
cur.execute(
    "UPDATE entry_properties SET property_value=? WHERE entry_id='CHEM5' AND property_name='concept_tags'",
    ("mass action, reaction rate law, rate constant, reaction order, equilibrium constant, "
     "Arrhenius kinetics, stoichiometric matrix, flux balance analysis, metabolic network, "
     "S v=0, FBA, substrate uptake, chemical kinetics",)
)
print("[OK] CHEM5 concept tags updated")


# ─────────────────────────────────────────────────────────────────────────────
# F2 — extend "What's Established" with Monod (1949) microbial growth findings
# Source: Monod (1949), pp. 379–384 (journal pagination)
# ─────────────────────────────────────────────────────────────────────────────

F2_ESTABLISHED_ORIGINAL = cur.execute(
    "SELECT content FROM sections WHERE entry_id='F2' AND section_name=\"What's Established\""
).fetchone()[0]

MONOD_PARAGRAPH = (
    "\n\nThe quantitative expression of substrate-limited bacterial growth was derived by Monod "
    "(1949, Annual Review of Microbiology 3:371). He showed that within a defined experiment where a "
    "single essential nutrient is the sole limiting factor, total growth G is linear in the initial "
    "nutrient concentration C: G = KC, where K is a yield constant independent of concentration "
    "(Monod 1949, p. 380). The limiting nutrient is fully consumed before growth stops; no threshold "
    "concentration is required. Monod further showed that the exponential growth rate R follows a "
    "hyperbolic saturation equation: R = R_K · C / (C\u2081 + C), where R_K is the maximum growth rate "
    "and C\u2081 is the substrate concentration at half-maximum rate — analogous to the Michaelis constant "
    "(Monod 1949, p. 383, equation [2]). For E. coli growing on glucose, he measured R_K = 1.35 "
    "divisions per hour and C\u2081 = 0.22 \u00d7 10\u207b\u2074 M (Monod 1949, Fig. 4). Monod used the language "
    "of 'sole limiting factor' and 'essential nutrient' rather than citing Liebig by name; the "
    "connection between his framework and Liebig's law of the minimum was made explicit in later "
    "literature (de Baar 1994; Tilman 1980). The Monod equation is Liebig's minimum constraint "
    "expressed as a continuous saturation function rather than a step function: when C << C\u2081, "
    "growth is proportional to C (fully resource-limited); when C >> C\u2081, growth saturates at R_K "
    "(resource no longer limiting)."
)

# Only append if not already added
if "Monod" not in F2_ESTABLISHED_ORIGINAL:
    cur.execute(
        "UPDATE sections SET content=? WHERE entry_id='F2' AND section_name=\"What's Established\"",
        (F2_ESTABLISHED_ORIGINAL + MONOD_PARAGRAPH,)
    )
    print("[OK] F2 / What's Established extended with Monod (1949)")
else:
    print("[SKIP] F2 / What's Established already contains Monod reference")

# Extend F2 "What The Math Says" with Monod growth saturation paragraph
F2_MATH_ORIGINAL = cur.execute(
    "SELECT content FROM sections WHERE entry_id='F2' AND section_name='What The Math Says'"
).fetchone()[0]

MONOD_MATH_PARAGRAPH = (
    "\n\nAt the level of microbial growth (Monod 1949), the growth rate R equals the maximum rate R_K "
    "times C divided by (C\u2081 plus C), where C is substrate concentration and C\u2081 is the "
    "half-saturation constant. This is Liebig's minimum-bottleneck principle in continuous dynamic "
    "form: when C is much less than C\u2081, R \u2248 R_K \u00b7 C/C\u2081 — growth is proportional to the "
    "scarce nutrient, fully resource-limited. When C is much greater than C\u2081, R \u2248 R_K — the "
    "nutrient is no longer limiting and growth saturates. The transition between these regimes is "
    "the constraint binding shift that Liebig's law describes as a step function; the Monod equation "
    "describes it as a smooth hyperbola. The binding constraint — which resource is scarce enough "
    "to limit growth — can shift dynamically as cultivation conditions change, exactly as the "
    "framework's constraint binding tables capture."
)

if "Monod 1949" not in F2_MATH_ORIGINAL:
    cur.execute(
        "UPDATE sections SET content=? WHERE entry_id='F2' AND section_name='What The Math Says'",
        (F2_MATH_ORIGINAL + MONOD_MATH_PARAGRAPH,)
    )
    print("[OK] F2 / What The Math Says extended with Monod growth saturation")
else:
    print("[SKIP] F2 / What The Math Says already contains Monod reference")

# Update F2 concept tags
F2_NEW_TAGS = (
    "limiting factor\nbottleneck resource\nminimum constraint\nLiebig barrel\nresource colimitation\n"
    "binding constraint\nagricultural yield\necological carrying capacity\nnutrient limitation\n"
    "growth ceiling\nMonod equation\nmicrobial growth kinetics\nsubstrate saturation\n"
    "half-saturation constant\nbacterial growth\nflux balance constraint"
)
cur.execute(
    "UPDATE sections SET content=? WHERE entry_id='F2' AND section_name='Concept Tags'",
    (F2_NEW_TAGS,)
)
print("[OK] F2 concept tags updated")


# ─────────────────────────────────────────────────────────────────────────────
# KC1 — update "Mathematical Form" and "What The Math Says" with
#        delta-G / van't Hoff quantitative form
# Source: Atkins Physical Chemistry (textbook basis — established thermodynamics)
# ─────────────────────────────────────────────────────────────────────────────

KC1_MATH_FORM_NEW = (
    "dG = 0 at equilibrium; perturbation \u2192 sign(dG) < 0 restoring shift\n"
    "\u0394G = \u0394G\u00b0 + RT ln Q  (Q = reaction quotient; K = equilibrium constant)\n"
    "At equilibrium (\u0394G = 0):  \u0394G\u00b0 = \u2212RT ln K\n"
    "Direction of shift: Q < K \u21d2 reaction proceeds forward; Q > K \u21d2 reaction proceeds in reverse\n"
    "van 't Hoff equation:  d(ln K)/dT = \u0394H\u00b0 / RT\u00b2\n"
    "  (endothermic reaction, \u0394H\u00b0 > 0: K increases with T, equilibrium shifts toward products)\n"
    "  (exothermic reaction,  \u0394H\u00b0 < 0: K decreases with T, equilibrium shifts toward reactants)"
)

cur.execute(
    "UPDATE sections SET content=? WHERE entry_id='KC1' AND section_name='Mathematical Form'",
    (KC1_MATH_FORM_NEW,)
)
print("[OK] KC1 / Mathematical Form updated with delta-G and van't Hoff")

# Update KC1 "What The Math Says" — replace the last two sentences (the qualitative-only ending)
KC1_MATH_SAYS_ORIGINAL = cur.execute(
    "SELECT content FROM sections WHERE entry_id='KC1' AND section_name='What The Math Says'"
).fetchone()[0]

# The last two sentences to replace
OLD_ENDING = (
    "The principle is qualitative \u2014 it predicts the direction of shift but not the "
    "magnitude. It follows from the thermodynamic requirement that G is minimized at equilibrium."
)

NEW_ENDING = (
    "The quantitative form is the reaction quotient comparison: \u0394G equals \u0394G\u00b0 plus "
    "RT times the natural log of Q, where Q is the current ratio of product to reactant concentrations "
    "raised to their stoichiometric powers. When Q is less than K, \u0394G is negative and the reaction "
    "proceeds forward; when Q is greater than K, \u0394G is positive and the reaction proceeds in reverse "
    "\u2014 this is the algebraic statement of what Le Chatelier's principle describes qualitatively. "
    "At equilibrium \u0394G equals zero, giving \u0394G\u00b0 equals negative RT times ln K: the standard "
    "free energy directly encodes the equilibrium position. Temperature dependence is given by the "
    "van 't Hoff equation: the derivative of ln K with respect to temperature equals \u0394H\u00b0 divided "
    "by RT squared. For an endothermic reaction (\u0394H\u00b0 > 0), K increases with temperature and "
    "equilibrium shifts toward products; for an exothermic reaction (\u0394H\u00b0 < 0), K decreases with "
    "temperature and equilibrium shifts back toward reactants. This quantifies the magnitude of the "
    "shift, not just its direction."
)

if OLD_ENDING in KC1_MATH_SAYS_ORIGINAL:
    KC1_MATH_SAYS_NEW = KC1_MATH_SAYS_ORIGINAL.replace(OLD_ENDING, NEW_ENDING)
    cur.execute(
        "UPDATE sections SET content=? WHERE entry_id='KC1' AND section_name='What The Math Says'",
        (KC1_MATH_SAYS_NEW,)
    )
    print("[OK] KC1 / What The Math Says updated with van't Hoff quantitative ending")
elif "van" in KC1_MATH_SAYS_ORIGINAL:
    print("[SKIP] KC1 / What The Math Says already contains van't Hoff")
else:
    # Fallback: append
    cur.execute(
        "UPDATE sections SET content=? WHERE entry_id='KC1' AND section_name='What The Math Says'",
        (KC1_MATH_SAYS_ORIGINAL + "\n\n" + NEW_ENDING,)
    )
    print("[OK] KC1 / What The Math Says extended (fallback append)")

# Update KC1 concept tags
KC1_NEW_TAGS = (
    "Le Chatelier principle\nequilibrium shift\nchemical equilibrium\nGibbs free energy minimum\n"
    "opposing perturbation\nreaction equilibrium\npressure temperature concentration effects\n"
    "reaction quotient\nvan t Hoff equation\ndelta G standard\ntemperature dependence of K\n"
    "endothermic exothermic shift\nthermodynamic homeostasis"
)
cur.execute(
    "UPDATE sections SET content=? WHERE entry_id='KC1' AND section_name='Concept Tags'",
    (KC1_NEW_TAGS,)
)
print("[OK] KC1 concept tags updated")


# ─────────────────────────────────────────────────────────────────────────────
# Commit and verify
# ─────────────────────────────────────────────────────────────────────────────
conn.commit()
conn.close()

print()
print("=== Verification ===")
conn = sqlite3.connect(DB)
for eid in ["CHEM5", "F2", "KC1"]:
    secs = conn.execute(
        "SELECT section_name, length(content) FROM sections WHERE entry_id=? ORDER BY section_order",
        (eid,)
    ).fetchall()
    print(f"{eid}: {[(s[0], s[1]) for s in secs]}")
conn.close()
print()
print("Migration complete. Run sync to rebuild ChromaDB.")
