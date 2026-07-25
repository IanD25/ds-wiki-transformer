"""
Kolokotrones deep-research pass — corrections + resolution — 2026-05-04

Three-agent research pass on Kolokotrones et al. 2010 "Curvature in
metabolic scaling" (Nature 464, 753-756), triggered because an earlier
session flagged a curvature-direction puzzle as open while explicitly
noting the paper had not been read. Full text obtained.

=========================================================================
FINDING 1 — BAD CITATION IN C1
=========================================================================
C1 states "Xiao et al. (2015) identified a quantitative breakpoint at
~10 kg body mass." NO SUCH PAPER EXISTS. Xiao Xiao's 2015 output is
maximum-entropy ecology and Taylor's law, not metabolic scaling.

The ~10 kg breakpoint is Dodds, Rothman & Weitz 2001 — already anchored
to C1 earlier today as `contradicts`. Their Table I: alpha = 0.668 +/-
0.019 for 357 species below 10 kg; alpha = 0.877 +/- 0.088 above. They
also cite Economos 1983 for a 20 kg breakpoint.

Third mislabelled quantity found in this entry cluster today, after X1's
"empirical WBE value" and C1's implied-D_eff column.

=========================================================================
FINDING 2 — CURVATURE IS CONTESTED, NOT ESTABLISHED
=========================================================================
C1 records curvature under What's Established. The replication record
does not support that placement:

  Griebeler & Werner 2016 (Ecol. Evol. 6:8352) — 519 species, AICc+PGLS,
    LINEAR BEAT CURVATURE IN 16 OF 17 ORDERS; charges Kolokotrones with
    using R^2 for model selection
  Hudson, Isaac & Reuman 2013 (J. Anim. Ecol. 82:1009) — curvature best
    explained by aquatic/non-aquatic intercept shift; "not real"
  Mori et al. 2010 (PNAS 107:1447) — plants curve CONCAVE, opposite sign
  Ehnes et al. 2011 (Ecol. Lett. 14:993) — invertebrate curvature removed
    by phylogenetic grouping
  Birds, reptiles, fish — no positive replication found
  Clarke 2025 (Ecol. Monogr. 95:e70030) — mammal-specific, so WBE-general
    explanations cannot account for it
  MacKay 2011 (J. Theor. Biol. 280:194) — log-quadratic breaks scale
    invariance; conditioning on Order, only Rodentia significant (p=0.02,
    2% of variance)
  Packard 2016/2017 — log-scale curvature follows from a non-zero
    arithmetic intercept
  Kolokotrones' own figure: quadratic adds 0.3% of variance (96.1/95.8)

Reply exists: Deeds, Savage & Fontana 2011 (J. Theor. Biol. 280:197).
Paywalled, CONTENT NOT READ.

=========================================================================
FINDING 3 — THE DIRECTION PUZZLE IS RESOLVED: MIN-RULE vs SUM-RULE
=========================================================================
The open question recorded earlier today assumed a surface-vs-network
crossover and found the observed direction backwards. The error was the
COMBINATION RULE, not the physics.

  MIN-RULE  B = min(a*M^p, b*M^q)  — lower exponent binds at LARGE mass
                                     -> CONCAVE (the earlier prediction)
  SUM-RULE  B = a*M^p + b*M^q      — lower exponent dominates at SMALL
                                     mass -> CONVEX (observed)

The models that actually reproduce the curvature use sums, not minima:
Ballesteros et al. 2018 (Sci. Rep. 8:1448) write B = f*k*M +
(1-f)*k0*M^(2/3). Zhao (arXiv:1509.08912) derives both 2/3 and 3/4 from
one Murray-law network and explicitly denies the small-mass 2/3 is the
surface law.

Kolokotrones themselves offer NO thermal explanation and never propose a
surface-network crossover. Their fix is vascular: WBE place the
pulsatile-to-smooth flow transition a constant number of levels from the
CAPILLARIES; the variant that fits ("proportional transition") places it
at a constant FRACTION of levels from the HEART, motivated by pulse
attenuation. They explicitly decline to assert it is physically real.

Also settled: WBE's finite-size correction is NOT the explanation. It
predicts CONCAVE curvature. Verbatim: "predicting concave curvature - not
the convex curvature found in the data". That anomaly is why the paper
exists.

=========================================================================
FINDING 4 — CONSTRUCTIVE: H5's FORM IS DERIVABLE
=========================================================================
This follows from Finding 3 by algebra (own derivation, verifiable).

For two processes contributing additively, B = a*M^p + b*M^q, the local
log-log slope is:

    d(log B)/d(log M) = p*f + q*(1-f),    f = a*M^p / B

which is EXACTLY H5's beta(lambda) form, with lambda = the fractional
contribution of process 1 to total metabolic rate.

Consequences:
  - the form was never arbitrary; it is what a two-process sum gives
  - lambda has an operational meaning: fractional contribution
  - lambda is measurable without touching beta (measure contributions)
  - lambda is MASS-DEPENDENT by construction, settling that question
  - the endpoints are the exponents of the two contributing PROCESSES,
    not a free choice
  - "which constraint binds" language implies a MIN-rule and is wrong
    for an additive decomposition; nothing binds, things contribute

Open: WHICH two processes. Ballesteros uses isometric(1) + surface(2/3);
Zhao derives both from network geometry. Not settled here.

=========================================================================
FINDING 5 — FIELD CONSENSUS IS THE NEGATIVE
=========================================================================
Glazier 2022 (Proc. R. Soc. B 289:20221605), White & Marshall 2023
(Physiology 38:266), Clarke 2025: no universal exponent. Price et al.
2012 (Ecol. Lett. 15:1465) — co-authored by BOTH Savage and Dodds —
concedes WBE's derivation is incomplete and a fuller treatment gives a
curve that is not a pure power law.

Run: python3 scripts/migrations/m0_kolokotrones_research_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-kolokotrones-research-2026-05-04"


# Mode "replace_then_append" does BOTH in one string operation, so two
# changes to the same column never become two UPDATEs (the B2a bug).
EDITS = [
    ("K1_C1_estab", "sections",
     {"entry_id": "C1", "section_name": "What's Established"},
     "content", "replace_then_append",
     # --- find ---
     "Kolokotrones et al. (*Nature*, 2010) demonstrated the log-log "
     "relationship has curvature — slope ~2/3 for small mammals, ~3/4 for "
     "large ones. Xiao et al. (2015) identified a quantitative breakpoint "
     "at ~10 kg body mass.",
     # --- replace with ---
     "Kolokotrones et al. (*Nature*, 2010) reported curvature in the log-log "
     "relationship, with the local exponent rising from **0.57 to 0.87** "
     "across the fitted range (corrected 2026-05-04 — the previously stated "
     "\"~2/3 to ~3/4\" understated the range; that gloss comes from their "
     "sub-range linear fits, not the fitted derivative). "
     "**Dodds, Rothman & Weitz (2001)** identified a breakpoint near **10 "
     "kg**: α = 0.668 ± 0.019 for 357 species below it, α = 0.877 ± 0.088 "
     "above; they also cite Economos (1983) for a 20 kg breakpoint.\n\n"
     "> **CITATION CORRECTED 2026-05-04.** This sentence previously "
     "attributed the ~10 kg breakpoint to \"Xiao et al. (2015).\" **No such "
     "paper exists** — verified by targeted search. The finding is Dodds, "
     "Rothman & Weitz 2001, which was already anchored to this entry. The "
     "bad citation is recorded rather than silently removed, per the "
     "no-deletions rule.",
     # --- then append ---
     "\n\n**REPLICATION RECORD (added 2026-05-04) — the curvature is "
     "CONTESTED and its placement under *What's Established* is now "
     "qualified.**\n\n"
     "| Study | Finding |\n"
     "|---|---|\n"
     "| Griebeler & Werner 2016, *Ecol. Evol.* 6:8352 | 519 mammal species, "
     "AICc + PGLS: **linear beat curvature in 16 of 17 orders**; charges "
     "Kolokotrones with using $R^2$ for model selection |\n"
     "| Hudson, Isaac & Reuman 2013, *J. Anim. Ecol.* 82:1009 | curvature "
     "best explained by an aquatic/non-aquatic intercept shift — \"not "
     "real\" |\n"
     "| Mori et al. 2010, *PNAS* 107:1447 | plants curve **concave** — "
     "opposite sign |\n"
     "| Ehnes et al. 2011, *Ecol. Lett.* 14:993 | invertebrate curvature "
     "removed by phylogenetic grouping |\n"
     "| Birds, reptiles, fish | no positive replication found |\n"
     "| Clarke 2025, *Ecol. Monogr.* 95:e70030 | mammal-specific, so "
     "WBE-general explanations cannot account for it |\n"
     "| MacKay 2011, *J. Theor. Biol.* 280:194 | log-quadratic breaks scale "
     "invariance; conditioning on Order, **only Rodentia significant** "
     "($p = 0.02$, 2% of variance) |\n"
     "| Packard 2016/2017 | log-scale curvature follows from a non-zero "
     "arithmetic intercept |\n"
     "| Kolokotrones' own figure | quadratic adds **0.3%** of variance "
     "(96.1% vs 95.8%) |\n\n"
     "A reply to MacKay exists — Deeds, Savage & Fontana 2011, *J. Theor. "
     "Biol.* 280:197 — **paywalled and unread**; its content is not "
     "represented here.\n\n"
     "**Revised status:** curvature in *eutherian mammals* is a real but "
     "small effect that several independent re-analyses fail to reproduce "
     "as the best model. It is **not** established across taxa and should "
     "not be cited as though it were. What IS well supported is the weaker "
     "and more robust negative: **no universal exponent exists** (Glazier "
     "2022 *Proc. R. Soc. B* 289:20221605; White & Marshall 2023 "
     "*Physiology* 38:266; Clarke 2025). Notably Price et al. 2012 "
     "(*Ecol. Lett.* 15:1465), co-authored by **both Savage and Dodds**, "
     "concedes WBE's original derivation is incomplete and a fuller "
     "treatment yields a curve that is not a pure power law.\n\n"
     "**Consequence for the FRAMING note above:** its core point — that "
     "assuming a single exponent may be fitting a line to a curve — "
     "survives, because the no-universal-exponent consensus supports it "
     "independently of whether the specific quadratic holds. But the "
     "framing should rest on that consensus, not on Kolokotrones alone."),

    # ------------------------------------------------------------------ H5
    ("K2_H5_deriv", "sections",
     {"entry_id": "H5", "section_name": "What The Math Says"},
     "content", "append",
     "\n\n---\n\n"
     "**DERIVATION FOUND 2026-05-04 — the $\\beta(\\lambda)$ form is not "
     "arbitrary after all.**\n\n"
     "Earlier today this entry was reframed as \"interpolation between "
     "chosen endpoints, no mechanism generating the line.\" That diagnosis "
     "was correct about how the formula was *constructed* but wrong that no "
     "mechanism *exists*. There is one, and it is elementary.\n\n"
     "Suppose metabolic rate is the sum of two processes with different "
     "mass exponents:\n\n"
     "$$B = a M^{p} + b M^{q}$$\n\n"
     "The local log-log slope is then\n\n"
     "$$\\frac{d\\log B}{d\\log M} = p f + q(1-f), \\qquad "
     "f = \\frac{a M^{p}}{B}$$\n\n"
     "which is **exactly** $\\beta(\\lambda)$, with $\\lambda = f$ — the "
     "**fractional contribution of process 1 to total metabolic rate**.\n\n"
     "**What this settles:**\n\n"
     "- **$\\lambda$ has an operational definition** that mentions neither "
     "$\\beta$ nor any exponent: it is the fraction of the total contributed "
     "by one process. Measurable by measuring the two contributions "
     "separately. This passes the test H3 set.\n"
     "- **$\\lambda$ is mass-dependent by construction**, since $f$ varies "
     "with $M$. The question of whether $\\lambda$ could be a constant is "
     "closed — it cannot, and now there is a reason rather than a puzzle.\n"
     "- **The endpoints are not a free choice.** They are the exponents of "
     "the two contributing processes. Identify the processes and the "
     "endpoints follow.\n"
     "- **A sum produces convex curvature automatically**, because the lower "
     "exponent dominates at small mass. This is the observed direction.\n\n"
     "**Correction to the framework's vocabulary.** \"Which constraint "
     "binds\" language implies a **minimum** rule, $B = \\min(aM^p, bM^q)$, "
     "under which the lower exponent binds at *large* mass and the curve is "
     "**concave** — the opposite of observation. Under an additive "
     "decomposition nothing binds; processes contribute in proportion. The "
     "framework has been sliding between these two rules, and they are "
     "different physics with opposite signatures.\n\n"
     "**Still open: which two processes.** Ballesteros et al. 2018 "
     "(*Sci. Rep.* 8:1448) use isometric ($p=1$) plus surface ($q=2/3$). "
     "Zhao (arXiv:1509.08912) derives both 2/3 and 3/4 from a single "
     "Murray-law network and **explicitly denies** the small-mass 2/3 is "
     "the surface law. These are competing decompositions and this entry "
     "does not choose between them.\n\n"
     "**Caveat on the empirical motivation.** This derivation explains how "
     "convex curvature *would* arise; it does not establish that the "
     "curvature is real. See C1's replication record — several independent "
     "re-analyses fail to reproduce curvature as the best model."),

    # ------------------------------------------------------------------ H3
    ("K3_H3_lambda", "sections",
     {"entry_id": "H3", "section_name": "What It Says"},
     "content", "append",
     "\n\n---\n\n"
     "**DEFINITION RESOLVED 2026-05-04 (see H5 *What The Math Says* for the "
     "derivation).**\n\n"
     "> **$\\lambda$ is the fractional contribution of one process to total "
     "metabolic rate**, where metabolic rate is the sum of two processes "
     "with different mass exponents.\n\n"
     "This mentions neither $\\beta$ nor any exponent, and it is measurable "
     "by measuring the two contributions separately — which is the test this "
     "entry set for a repaired definition. It supersedes both the original "
     "\"phase coherence\" wording and the realisation-fraction candidate "
     "recorded above.\n\n"
     "It also resolves the state-versus-structure conflation recorded "
     "earlier: $\\lambda$ is **neither**. It is mass-dependent by "
     "construction, because the relative contribution of two processes with "
     "different exponents necessarily shifts with $M$. So it is not a "
     "species constant, and it is not an activity state — it is a property "
     "of where on the mass axis the organism sits.\n\n"
     "**Consequences for the cost claim below.** P15's $(1-\\lambda)^2 "
     "\\cdot d_f$ was motivated as a Landauer-class cost of maintaining "
     "synchronisation. Under this definition $\\lambda$ is not a "
     "synchronisation and not something an organism maintains — it is a "
     "ratio that falls out of two processes' relative size at a given mass. "
     "**That motivation is now dead**, not merely weakened. Any surviving "
     "version of P15 needs an entirely different rationale.\n\n"
     "**The name should change.** \"Phase coherence\" is wrong under this "
     "reading, and it collides with standard usage. Something like "
     "*process-contribution fraction* is honest. See `gloss_lambda`."),
]


ANCHORS = [
    ("C1", "doi", "10.1016/j.jtbi.2011.02.011", None,
     "MacKay 2011 - Mass scale and curvature in metabolic scaling",
     1, "canonical", "contradicts", None, "high",
     "Deep-research pass 2026-05-04. Argues the Kolokotrones log-quadratic "
     "breaks scale invariance, so b1 and its significances are artifacts of "
     "setting M0 = 1 g; only b2 is scale-invariant. Under a scale-invariant "
     "test conditioning on taxonomic Order, ONLY Rodentia remains "
     "significant (p=0.02, 2% of variance). Also notes the log-quadratic was "
     "fitted and rejected by Haysen & Lacy 1985, uncited by Kolokotrones. "
     "Stated verdict: scepticism. MacKay thanks Fontana in acknowledgements, "
     "so this is collegial critique rather than camp warfare."),

    ("C1", "doi", "10.1016/j.jtbi.2011.03.036", None,
     "Deeds, Savage & Fontana 2011 - Reply to MacKay",
     1, "canonical", "cites", None, "medium",
     "Deep-research pass 2026-05-04. Formal reply to MacKay 2011. "
     "**PAYWALLED AND UNREAD** — content is NOT represented in the wiki. "
     "Confidence marked medium for that reason: the citation is verified but "
     "its argument is not. Anyone relying on the MacKay critique should read "
     "this reply first. Kolokotrones is not an author."),

    ("C1", "doi", "10.1111/j.1461-0248.2012.01860.x", None,
     "Price et al. 2012 - Testing the metabolic theory of ecology",
     1, "canonical", "cites", None, "high",
     "Deep-research pass 2026-05-04. Co-authored by BOTH Savage and Dodds, "
     "plus Clarke, Niklas, Kerkhoff — which cuts across the usual camp "
     "lines. States WBE's original derivation is incomplete and that a more "
     "complete derivation yields deviations and a universal curve that is "
     "NOT a pure power law, with pipe-flow optimisation giving B ~ M with a "
     "logarithmic mass correction. Load-bearing: this is the WBE lineage "
     "itself abandoning the pure power law, which matters more than any "
     "external critique."),
]


CALIBRATIONS = [
    ("C1", "entry", "Established", TODAY, SESSION,
     "Xiao 2015 citation was fabricated; curvature downgraded from established to contested",
     "TWO corrections. (1) BAD CITATION: C1 attributed the ~10 kg breakpoint "
     "to 'Xiao et al. (2015)'. No such paper exists — targeted search "
     "confirms Xiao Xiao's 2015 output is maximum-entropy ecology and "
     "Taylor's law. The finding is Dodds, Rothman & Weitz 2001 (alpha = "
     "0.668 +/- 0.019 below 10 kg; 0.877 +/- 0.088 above), already anchored "
     "here. Third mislabelled quantity found in this cluster today. "
     "(2) CURVATURE DOWNGRADED: replication record does not support "
     "placement under What's Established. Griebeler & Werner 2016 (519 "
     "species) found linear beat curvature in 16 of 17 orders; Hudson 2013 "
     "attributes it to an aquatic intercept shift; plants curve the opposite "
     "way; invertebrate curvature vanishes under phylogenetic grouping; no "
     "replication in birds/reptiles/fish. Also corrected the slope range "
     "from '~2/3 to ~3/4' to the paper's actual 0.57-0.87. C1's other "
     "empirical content remains Established."),

    ("curvature_direction_puzzle", "open_question", "Established",
     TODAY, SESSION,
     "RESOLVED — the error was min-rule vs sum-rule, not the physics",
     "CLOSED. The puzzle assumed two constraints combine as a MINIMUM, under "
     "which the lower exponent binds at large mass giving concave curvature "
     "— which is why the observed convex direction looked backwards. The "
     "models that reproduce the curvature use SUMS instead: Ballesteros et "
     "al. 2018 write B = f*k*M + (1-f)*k0*M^(2/3). In any sum the lower "
     "exponent dominates at SMALL mass, giving convex. The thermal reasoning "
     "was sound; the combination rule was wrong. Separately confirmed: "
     "Kolokotrones offer no thermal explanation and never propose a "
     "surface-network crossover — their fix is vascular (pulsatile "
     "transition placed a constant fraction of levels from the heart rather "
     "than a constant number from the capillaries, motivated by pulse "
     "attenuation), and they decline to assert it is physically real. Also "
     "settled: WBE's finite-size correction predicts CONCAVE curvature and "
     "is therefore not the explanation — it is the anomaly the paper was "
     "written about."),

    ("H5", "entry", "Speculative", TODAY, SESSION,
     "Form is DERIVABLE from a two-process sum; lambda = fractional contribution",
     "CONSTRUCTIVE REVERSAL of this morning's diagnosis. H5 was reframed as "
     "'interpolation between chosen endpoints with no mechanism generating "
     "the line'. That was right about construction, wrong that no mechanism "
     "exists. For B = a*M^p + b*M^q the local log-log slope is p*f + q*(1-f) "
     "with f = a*M^p/B — exactly beta(lambda), with lambda the fractional "
     "contribution of one process. Consequences: the form is not arbitrary; "
     "lambda has an operational definition mentioning no exponent; lambda is "
     "measurable; lambda is mass-dependent BY CONSTRUCTION (closing that "
     "question); endpoints are the two processes' exponents rather than a "
     "free choice; and a sum yields convex curvature automatically. Also "
     "corrects framework vocabulary: 'which constraint binds' implies a "
     "min-rule, which gives the WRONG curvature sign. Under an additive "
     "decomposition nothing binds — processes contribute in proportion. "
     "STILL OPEN: which two processes (Ballesteros: isometric + surface; "
     "Zhao: both from Murray-law network geometry, explicitly denying the "
     "small-mass 2/3 is the surface law). Caveat: this explains how convex "
     "curvature would arise, not that the curvature is real."),

    ("H3", "entry", "Speculative", TODAY, SESSION,
     "lambda definition RESOLVED as fractional process contribution; P15's motivation dead",
     "lambda is the fractional contribution of one process to total "
     "metabolic rate, where rate is a sum of two processes with different "
     "mass exponents. Mentions neither beta nor any exponent; measurable by "
     "measuring the contributions separately. Passes the test H3 set. "
     "Supersedes both 'phase coherence' and the realisation-fraction "
     "candidate. Resolves the state-vs-structure conflation by being "
     "NEITHER — lambda is mass-dependent by construction, a property of "
     "where on the mass axis the organism sits. CONSEQUENCE: P15's "
     "(1-lambda)^2 * d_f was motivated as a Landauer cost of maintaining "
     "synchronisation; under this definition lambda is not a synchronisation "
     "and not something an organism maintains, so that motivation is DEAD "
     "rather than weakened. Any surviving P15 needs a wholly different "
     "rationale. Name should change from 'phase coherence'."),

    ("endpoint_decision_revised", "structural_observation", "Speculative",
     TODAY, SESSION,
     "[2/3, 3/4] rationale weakened; endpoints are now derivable, not chosen",
     "The endpoint decision recorded earlier today fixed H5's bounds at "
     "[2/3, 3/4] on two grounds: it contains observed BMR 0.676, and it "
     "gives the curvature a natural reading. Both are weakened. (1) "
     "Kolokotrones' local slopes run 0.57 to 0.87 — BOTH ends outside the "
     "wedge. (2) On their account 0.676 is a tangent slope at the mean of "
     "White & Seymour's mass distribution rather than a property of mammals. "
     "(3) The curvature that the choice was meant to accommodate is itself "
     "contested. BUT the two-process derivation supersedes the question: "
     "endpoints are the exponents of the two contributing processes, not a "
     "free choice, so the task is now identifying the processes rather than "
     "picking bounds. The [2/3, 3/4] decision is neither confirmed nor "
     "reversed — it is superseded by a better-posed question. NOTE the "
     "owner's MMR-as-overclock argument is UNAFFECTED and stands on its own "
     "grounds: sustained and peak capacity are different kinds of quantity "
     "regardless of how the sustained curve decomposes."),
]


def fetch(cur, table, where, col):
    wsql = " AND ".join(f"{k}=?" for k in where)
    cur.execute(f"SELECT {col} FROM {table} WHERE {wsql}", tuple(where.values()))
    row = cur.fetchone()
    if row is None:
        raise RuntimeError(f"Row not found: {table} {where}")
    return row[0] or ""


def main() -> None:
    if not DS_WIKI_DB.exists() or not WIKI_HISTORY_DB.exists():
        raise SystemExit("Run from repo root; databases not found")

    print("=" * 72)
    print("PHASE 1 — validation")
    print("=" * 72)
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    planned, seen = [], set()
    for label, table, where, col, mode, *args in EDITS:
        target = (table, tuple(sorted(where.items())), col)
        if target in seen:
            conn.close()
            raise SystemExit(f"[{label}] ABORT — duplicate target {target}")
        seen.add(target)
        current = fetch(cur, table, where, col)

        if mode == "append":
            (suffix,) = args
            if current.endswith(suffix):
                print(f"  [{label}] OK — already applied, skipping"); continue
            new = current + suffix
            print(f"  [{label}] OK — append (+{len(suffix)} chars)")
        elif mode == "replace_then_append":
            find, repl, suffix = args
            if find not in current:
                if current.endswith(suffix):
                    print(f"  [{label}] OK — already applied, skipping"); continue
                conn.close()
                raise SystemExit(f"[{label}] FAIL — anchor not found: {find[:80]!r}")
            new = current.replace(find, repl, 1) + suffix
            print(f"  [{label}] OK — replace ({len(find)}→{len(repl)}) + append (+{len(suffix)})")
        else:
            conn.close(); raise SystemExit(f"[{label}] unknown mode {mode}")
        planned.append((label, table, where, col, new))
    conn.close()

    if planned:
        print()
        print("=" * 72)
        print("PHASE 2 — apply")
        print("=" * 72)
        conn = sqlite3.connect(DS_WIKI_DB)
        cur = conn.cursor()
        for label, table, where, col, new in planned:
            wsql = " AND ".join(f"{k}=?" for k in where)
            cur.execute(f"UPDATE {table} SET {col}=? WHERE {wsql}",
                        (new, *where.values()))
            if cur.rowcount != 1:
                conn.rollback(); conn.close()
                raise SystemExit(f"[{label}] hit {cur.rowcount} rows; rolled back")
            print(f"  [{label}] WRITE — {table} {where} {col}")
        conn.commit(); conn.close()

        print()
        print("=" * 72)
        print("PHASE 3 — verification")
        print("=" * 72)
        conn = sqlite3.connect(DS_WIKI_DB)
        cur = conn.cursor()
        ok = True
        for label, table, where, col, expected in planned:
            if fetch(cur, table, where, col) == expected:
                print(f"  [{label}] OK — verified")
            else:
                print(f"  [{label}] DRIFT"); ok = False
        conn.close()
        if not ok:
            raise SystemExit("Post-write drift; investigate")
    else:
        print("\nAll prose edits already applied.")

    print()
    print("=" * 72)
    print("PHASE 4 — anchors + calibration")
    print("=" * 72)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    hcur = hc.cursor()
    n_a = 0
    for (eid, src, ident, rev, title, tier, stab, rel, role, conf, notes) in ANCHORS:
        hcur.execute("""
            INSERT OR IGNORE INTO external_anchors (
                entry_id, source, identifier, revision_id, title, tier,
                source_stability_class, relationship, canonical_role,
                verified_date, verified_by_session, confidence, notes
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (eid, src, ident, rev, title, tier, stab, rel, role,
              TODAY, SESSION, conf, notes))
        n_a += hcur.rowcount
    n_c = 0
    for (eid, etype, confv, cdate, aref, short, rationale) in CALIBRATIONS:
        hcur.execute("""
            INSERT INTO confidence_calibration (entity_id, entity_type,
                confidence, calibration_date, audit_ref, short_status, rationale)
            VALUES (?,?,?,?,?,?,?)
        """, (eid, etype, confv, cdate, aref, short, rationale))
        n_c += 1
    hc.commit(); hc.close()
    print(f"  anchors inserted:      {n_a}")
    print(f"  calibrations inserted: {n_c}")
    print()
    print(f"Migration complete. Session: {SESSION}")


if __name__ == "__main__":
    main()
