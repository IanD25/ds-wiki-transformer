"""
Scaling queue — deferred items 5 & 6 — 2026-05-04

Owner-approved. Completes the two items held back from the reformulation
migration because re-prioritising conjectures is a larger call than
correcting text.

  Item 6  P12 downgrade
  Item 5  P14 / P16 promotion, with honest blockers named
  Bonus   lambda symbol disambiguation (4 unrelated uses found)

--------------------------------------------------------------------------
ITEM 6 — P12
--------------------------------------------------------------------------
P12 claims beta(lambda) "correctly predicts power-law scaling exponents
across unrelated domains whenever d_f and lambda are independently
measured."

Two distinct problems, and they have different logical status:

  (a) BIOLOGICAL HALF — conditionally untested. If d_f were measured
      anatomically and came out near 2.1 for mammals, the formula would
      fit strict BMR. So the antecedent has not been tested. Blocked,
      not falsified.

  (b) URBAN HALF — STRUCTURALLY FALSIFIED, not conditionally. beta(lambda)
      is a weighted average of d_f/(d_f+1) and 1, so its output is
      confined to [d_f/(d_f+1), 1] and bounded above by 1 for EVERY d_f
      and EVERY lambda in [0,1]. Urban socioeconomic exponents are ~1.15.
      No measurement of d_f or lambda can rescue this — it is a property
      of the functional form.

So P12's cross-domain universality claim is falsified by the urban case
without needing any new measurement. The surviving fragment is
domain-restricted and untested.

Note also that P12's stated would_kill anticipated the wrong failure mode.
It expected "systematically different beta for matched d_f and lambda."
The actual failure is stronger: beta values exist that the formula cannot
produce at all, for any parameter values.

--------------------------------------------------------------------------
ITEM 5 — P14 and P16
--------------------------------------------------------------------------
Both were nominated as the only scaling conjectures with independent
measurement paths. On inspection they are blocked in different ways and
"promote both" is too coarse.

P14 (branching variance predicts exponent gap) — SPLITS usefully:
  P14a  EMPIRICAL CORE: does branching-ratio variance correlate with the
        BMR/MMR exponent gap? Measurable NOW. Requires no lambda, no
        P13, no Q1. Micro-CT plus published exponent gaps plus a
        phylogenetically-corrected regression. This is the genuine
        front-of-queue item.
  P14b  MECHANISM: is that correlation mediated by Delta-lambda =
        1 - lambda_min? Blocked on lambda's reconstruction and on P13
        (acknowledged ansatz).
P14a can succeed or fail independently of P14b. If P14a finds no
correlation, P14b is moot. If P14a finds one, P14b becomes worth arguing.

P16 (RLCT = d_f) — blocked at SPECIFICATION, not measurement. Per Q4's
own status text, no biological learning problem has been mapped to the
SLT framework in a way that yields a computable RLCT. You cannot compute
an RLCT until the statistical model is specified. So the real queue item
is Q4, not P16, and promoting P16 without promoting Q4 would misdescribe
what is blocking it.

--------------------------------------------------------------------------
BONUS — lambda is overloaded four ways
--------------------------------------------------------------------------
Found while reading Q4. Distinct mathematical objects sharing the symbol:
  1. lambda  — phase coherence (H3, H5, P13, P14, P15). Project-internal,
               currently under reconstruction.
  2. lambda_RLCT — Watanabe's Real Log-Canonical Threshold (Q4, P16).
               Standard in singular learning theory. Unrelated to (1).
  3. lambda_i — eigenvalues of the FIM / connected correlation matrix
               (CCA work, PR_FIM definition). Standard linear algebra.
  4. lambda  — wavelength (QM4 de Broglie, optics entries). Textbook.
  Plus: Lagrange multiplier in CCA_MATHEMATICAL_FORMALIZATION Definition 1
  ("delta-F = lambda delta-C"), and Lambda as cosmological constant in the
  GT cluster.
Filed as a glossary disambiguation page using the subsystem built earlier
this session.

Run: python3 scripts/migrations/m0_scaling_queue_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-scaling-queue-2026-05-04"


EDITS = [
    # ------------------------------------------------------------- P12 (item 6)
    ("Q1_P12_gaps", "conjectures", {"id": "P12"}, "critical_gaps", "append",
     "\n\n**DOWNGRADED 2026-05-04 — cross-domain universality falsified; "
     "surviving fragment is domain-restricted and untested.**\n\n"
     "Two problems with different logical status:\n\n"
     "**(a) Biological half — conditionally untested.** The antecedent "
     "\"whenever $d_f$ and $\\lambda$ are independently measured\" has never "
     "been satisfied. It is also not currently satisfiable: $\\lambda$ has no "
     "operational definition permitting independent measurement (see H3's "
     "conflation note), and every $d_f$ in the wiki was obtained by "
     "inverting the formula rather than by anatomy (see C1 Empirical Values, "
     "retired 2026-05-04). Status: blocked, not falsified.\n\n"
     "**(b) Urban half — STRUCTURALLY FALSIFIED.** $\\beta(\\lambda)$ is a "
     "weighted average of $d_f/(d_f+1)$ and $1$, so its output is confined "
     "to $[d_f/(d_f+1),\\ 1]$ — **bounded above by 1 for every $d_f$ and "
     "every $\\lambda \\in [0,1]$.** Urban socioeconomic exponents are "
     "~1.15 (C2). No measurement of $d_f$ or $\\lambda$ can rescue this; it "
     "is a property of the functional form, not of unknown parameter "
     "values. P12's claim that the formula predicts exponents \"regardless "
     "of domain\" is therefore false, and falsified without requiring any "
     "new measurement.\n\n"
     "**The stated `would_kill` anticipated the wrong failure mode.** It "
     "expected systematically different $\\beta$ for systems with matched "
     "$d_f$ and $\\lambda$. The actual failure is stronger: $\\beta$ values "
     "exist which the formula cannot produce at all. A falsification "
     "criterion that misses the way a claim actually fails is itself worth "
     "recording — the criterion assumed the formula's range was adequate "
     "and only its parameter-matching was in question.\n\n"
     "**Surviving fragment**, if any: within a single domain, and "
     "restricted to sublinear exponents inside the achievable window, the "
     "formula may describe exponent variation. That is a much weaker claim "
     "than P12 makes, has no cross-domain content, and is untested. "
     "Pattern-tags: over-extension-beyond-formula-range, "
     "conditional-claim-with-unsatisfiable-antecedent."),

    ("Q2_P12_state", "conjectures", {"id": "P12"}, "three_state", "append",
     " | FALSIFIED (cross-domain universality) 2026-05-04: beta(lambda) is "
     "bounded above by 1 for all d_f and all lambda in [0,1]; urban "
     "socioeconomic exponents ~1.15 are outside its range structurally, not "
     "for want of measurement. Original state designation preserved above "
     "per no-deletions rule."),

    # -------------------------------------------------------- P14 (item 5)
    ("Q3_P14_gaps", "conjectures", {"id": "P14"}, "critical_gaps", "append",
     "\n\n**SPLIT AND PROMOTED 2026-05-04.** P14 bundles a testable "
     "empirical claim with a blocked mechanistic one. Separating them makes "
     "the empirical half actionable now.\n\n"
     "**P14a — empirical core. FRONT OF THE SCALING QUEUE.**\n"
     "> Does vascular branching-ratio variance correlate with the BMR/MMR "
     "metabolic exponent gap across taxa?\n\n"
     "This requires **no $\\lambda$, no P13, no Q1**. Branching variance is "
     "measurable by micro-CT or corrosion casting. Exponent gaps are "
     "already published for multiple taxa. The test is a "
     "phylogenetically-corrected regression, and this entry's existing "
     "`would_confirm` ($R^2 > 0.6$) and `would_kill` (no significant "
     "correlation after controlling for body mass) both apply to P14a "
     "unchanged. **This is the only conjecture in the scaling cluster that "
     "is testable with current methods and no upstream dependencies.**\n\n"
     "**P14b — mechanism. Blocked.**\n"
     "> Is that correlation mediated by $\\Delta\\lambda = 1 - "
     "\\lambda_{\\min}$?\n\n"
     "Blocked on two upstream items: $\\lambda$ has no operational "
     "definition (H3), and $\\lambda_{\\min} = (d_f-1)/(d_f+1)$ is an "
     "acknowledged ansatz (P13).\n\n"
     "**Why the split matters.** P14a and P14b can succeed or fail "
     "independently. If P14a finds no correlation, P14b is moot regardless "
     "of how $\\lambda$ is eventually defined. If P14a finds one, that is a "
     "real empirical result on its own terms, and P14b becomes a question "
     "worth arguing about. Running P14a does not require resolving anything "
     "else in the framework first — which is what makes it the right place "
     "to start."),

    # -------------------------------------------------------- P16 (item 5)
    ("Q4_P16_gaps", "conjectures", {"id": "P16"}, "critical_gaps", "append",
     "\n\n**QUEUE POSITION CLARIFIED 2026-05-04.** P16 was nominated for "
     "promotion as one of only two scaling conjectures offering a route to "
     "$d_f$ independent of $\\beta$. That nomination is withdrawn in favour "
     "of an accurate statement of what blocks it.\n\n"
     "**P16 is blocked at specification, not at measurement.** Q4's own "
     "status text is explicit: no biological learning problem has been "
     "mapped to the SLT framework in a way that produces a computable RLCT "
     "with biological meaning. An RLCT is a property *of a specified "
     "statistical model* — it is determined by the algebraic geometry of "
     "that model's singularity set. Until metabolism is formulated as a "
     "statistical learning problem with an explicit $p(x|\\theta)$, there is "
     "no object whose RLCT could be computed, and no amount of measurement "
     "changes that.\n\n"
     "**So the real queue item is Q4, not P16.** Promoting P16 while Q4 "
     "remains open would misdescribe the blocker as empirical when it is "
     "conceptual. P16 stays valuable — if $\\lambda_{\\text{RLCT}} = d_f$ "
     "held, it would supply exactly the $\\beta$-independent route to $d_f$ "
     "the framework needs — but its value is contingent on a specification "
     "step nobody has taken.\n\n"
     "**Terminology warning.** Q4 and P16 denote the RLCT as "
     "$\\lambda_{\\text{RLCT}}$. This is Watanabe's standard notation and is "
     "**completely unrelated** to the $\\lambda$ of H3/H5/P13/P14 (phase "
     "coherence). Two different objects, same letter, adjacent entries. See "
     "the $\\lambda$ disambiguation page."),
]


# ---------------------------------------------------------------------------
# Glossary: lambda disambiguation page
# ---------------------------------------------------------------------------
GLOSS_LAMBDA = {
    "id": "gloss_lambda",
    "title": "λ (lambda) — disambiguation",
    "domain": "mathematics · physics · information_theory.shannon",
    "sections": {
        "Disambiguation Notice":
            "The symbol **λ** carries at least four unrelated meanings across "
            "this wiki, two of them in adjacent entries. Use the specific "
            "sense in prose; never the bare symbol without a nearby binding.",
        "Senses":
            "- **λ — phase coherence** (H3, H5, P13, P14, P15). "
            "Project-internal parameter weighting the interpolation between "
            "$d_f/(d_f+1)$ and $1$. **Currently under reconstruction** — its "
            "definition is circular and it conflates a state variable with a "
            "structural one (see H3). Most promising replacement reading: "
            "realisation fraction of optimal network topology.\n"
            "- **λ_RLCT — Real Log-Canonical Threshold** (Q4, P16). "
            "Watanabe's quantity in singular learning theory; a rational "
            "number determined by the algebraic geometry of a statistical "
            "model's singularity set, governing asymptotic free energy and "
            "generalisation error. Standard notation in that field. "
            "**Unrelated to phase coherence.**\n"
            "- **λ_i — eigenvalues** (CCA work, PR_FIM definition, X-series). "
            "Eigenvalues of the Fisher information matrix / connected "
            "correlation matrix. Standard linear algebra.\n"
            "- **λ — wavelength** (QM4 de Broglie, optics entries). Textbook "
            "physics.\n"
            "- **λ — Lagrange multiplier** (CCA_MATHEMATICAL_FORMALIZATION "
            "Definition 1, `δF = λ δC`). Standard constrained-optimisation "
            "usage.\n"
            "- **Λ — cosmological constant** (GT01, GT04, GT10). Capitalised, "
            "so lower collision risk, but listed for completeness.",
        "Why this disambig exists":
            "P16 and Q4 sit in the same conjecture cluster as P13/P14 and use "
            "λ for a completely different object. A reader moving between "
            "P14 (phase coherence) and P16 (RLCT) encounters the same symbol "
            "meaning two unrelated things with no warning. This is the same "
            "class of collision the 2026-05-04 deep-research pass found for "
            "*Fisher information*, *effective dimension*, and *η* — except "
            "this one is entirely internal to the project, so no external "
            "literature forced it. Found while reading Q4 during the scaling "
            "queue pass.",
    },
}


CALIBRATIONS = [
    ("P12", "conjecture", "Falsified", TODAY, SESSION,
     "Cross-domain universality falsified structurally by the urban case",
     "beta(lambda) is a weighted average of d_f/(d_f+1) and 1, so its range "
     "is bounded above by 1 for EVERY d_f and EVERY lambda in [0,1]. Urban "
     "socioeconomic exponents ~1.15 lie outside that range as a property of "
     "the functional form, not for want of measurement — so no measurement "
     "of d_f or lambda can rescue the claim. P12's assertion that the "
     "formula predicts exponents 'regardless of domain' is therefore false "
     "and falsified without new data. The biological half remains blocked "
     "rather than falsified (its antecedent is untested and currently "
     "unsatisfiable). Also recorded: P12's would_kill anticipated the wrong "
     "failure mode, expecting mismatched beta for matched parameters rather "
     "than beta values the formula cannot produce at all. Pattern-tags: "
     "over-extension-beyond-formula-range, "
     "conditional-claim-with-unsatisfiable-antecedent."),

    ("P14a", "conjecture", "Speculative", TODAY, SESSION,
     "FRONT OF SCALING QUEUE — lambda-free empirical core, testable now",
     "P14 split into an empirical core and a mechanistic claim. P14a: does "
     "vascular branching-ratio variance correlate with the BMR/MMR exponent "
     "gap across taxa? Requires no lambda, no P13, no Q1 — only micro-CT or "
     "corrosion casting plus published exponent gaps plus a "
     "phylogenetically-corrected regression. P14's existing would_confirm "
     "(R^2 > 0.6) and would_kill (no significant correlation controlling for "
     "body mass) apply unchanged. This is the ONLY conjecture in the scaling "
     "cluster testable with current methods and zero upstream dependencies, "
     "which is what earns it the front position. Succeeds or fails "
     "independently of P14b."),

    ("P14b", "conjecture", "Speculative", TODAY, SESSION,
     "Mechanism blocked on lambda's reconstruction and P13's ansatz status",
     "Is the P14a correlation (if it exists) mediated by Delta-lambda = "
     "1 - lambda_min? Blocked upstream twice: lambda has no operational "
     "definition permitting independent measurement (H3 conflation note), "
     "and lambda_min = (d_f-1)/(d_f+1) is an acknowledged ansatz rather than "
     "a derivation (P13). Moot if P14a finds no correlation."),

    ("P16", "conjecture", "Speculative", TODAY, SESSION,
     "Promotion withdrawn — blocked at specification, not measurement; Q4 is the real item",
     "P16 was nominated as one of two conjectures offering a beta-independent "
     "route to d_f. Nomination withdrawn in favour of naming the blocker "
     "accurately. An RLCT is a property of a SPECIFIED statistical model, "
     "determined by the algebraic geometry of its singularity set. Per Q4's "
     "own status text, no biological learning problem has been mapped to SLT "
     "in a way yielding a computable RLCT. Until metabolism is formulated "
     "with an explicit p(x|theta) there is no object to compute, and "
     "measurement cannot help. The real queue item is Q4. P16 retains its "
     "value contingent on that specification step."),

    ("lambda_symbol_collision", "structural_observation", "Established",
     TODAY, SESSION,
     "lambda carries 4+ unrelated meanings, two in adjacent conjectures",
     "Found while reading Q4 during the scaling queue pass. Distinct objects "
     "sharing the symbol: (1) phase coherence, H3/H5/P13/P14/P15, "
     "project-internal and under reconstruction; (2) lambda_RLCT, Watanabe's "
     "Real Log-Canonical Threshold, Q4/P16, standard in singular learning "
     "theory; (3) lambda_i, FIM/correlation-matrix eigenvalues, CCA work and "
     "PR_FIM; (4) wavelength, QM4 and optics. Plus Lagrange multiplier in "
     "CCA_MATHEMATICAL_FORMALIZATION Def. 1 and Lambda as cosmological "
     "constant in the GT cluster. Note (1) and (2) appear in ADJACENT "
     "conjectures with no warning to the reader. Unlike the Fisher / "
     "effective-dimension / eta collisions found in the deep-research pass, "
     "this one is entirely internal — no external literature forced it. "
     "Filed as gloss_lambda disambiguation page."),
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

    # ---------------- PHASE 1: validate ----------------
    print("=" * 72)
    print("PHASE 1 — validation (dry run)")
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
        (suffix,) = args
        if current.endswith(suffix):
            print(f"  [{label}] OK — already applied, skipping")
            continue
        planned.append((label, table, where, col, current + suffix))
        print(f"  [{label}] OK — append (+{len(suffix)} chars)")

    # glossary page check
    cur.execute("SELECT 1 FROM entries WHERE id=?", (GLOSS_LAMBDA["id"],))
    gloss_needed = cur.fetchone() is None
    print(f"  [gloss_lambda] {'OK — will insert' if gloss_needed else 'OK — exists, skipping'}")
    conn.close()

    # ---------------- PHASE 2: apply ----------------
    if planned or gloss_needed:
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

        if gloss_needed:
            g = GLOSS_LAMBDA
            cur.execute("""
                INSERT INTO entries (id, title, filename, entry_type, scale,
                    domain, status, confidence, type_group, authoring_status,
                    formality_tier)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """, (g["id"], g["title"], f"{g['id']}.md", "disambiguation_page",
                  "—", g["domain"], "glossary", "established", "GL",
                  "complete", 2))
            for i, (sname, scontent) in enumerate(g["sections"].items()):
                cur.execute("""
                    INSERT INTO sections (entry_id, section_name,
                        section_order, content)
                    VALUES (?,?,?,?)
                """, (g["id"], sname, i, scontent))
            print(f"  [gloss_lambda] WRITE — entry + {len(g['sections'])} sections")

        conn.commit(); conn.close()

        # ---------------- PHASE 3: verify ----------------
        print()
        print("=" * 72)
        print("PHASE 3 — post-write verification")
        print("=" * 72)
        conn = sqlite3.connect(DS_WIKI_DB)
        cur = conn.cursor()
        ok = True
        for label, table, where, col, expected in planned:
            if fetch(cur, table, where, col) == expected:
                print(f"  [{label}] OK — verified")
            else:
                print(f"  [{label}] DRIFT"); ok = False
        cur.execute("SELECT COUNT(*) FROM sections WHERE entry_id=?",
                    (GLOSS_LAMBDA["id"],))
        n = cur.fetchone()[0]
        print(f"  [gloss_lambda] OK — {n} sections present")
        conn.close()
        if not ok:
            raise SystemExit("Post-write drift; investigate")
    else:
        print("\nAll edits already applied.")

    # ---------------- PHASE 4: calibration ----------------
    print()
    print("=" * 72)
    print("PHASE 4 — calibration")
    print("=" * 72)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    hcur = hc.cursor()
    n_c = 0
    for (eid, etype, confv, cdate, aref, short, rationale) in CALIBRATIONS:
        hcur.execute("""
            INSERT INTO confidence_calibration (entity_id, entity_type,
                confidence, calibration_date, audit_ref, short_status, rationale)
            VALUES (?,?,?,?,?,?,?)
        """, (eid, etype, confv, cdate, aref, short, rationale))
        n_c += 1
    hc.commit(); hc.close()
    print(f"  calibrations inserted: {n_c}")
    print()
    print(f"Migration complete. Session: {SESSION}")


if __name__ == "__main__":
    main()
