"""
Endpoint decision + MMR scope exclusion — 2026-05-04

Owner decision, this session. Two parts, the second doing more work than
the first.

PART 1 — ENDPOINTS SETTLED: [2/3, 3/4]
--------------------------------------
H5's bounding exponents are fixed at surface law (2/3) and WBE network
optimum (3/4), replacing the previous [d_f/(d_f+1), 1]. This contains the
observed strict mammalian BMR of 0.676, maps onto the actual historical
2/3-vs-3/4 debate, and gives Kolokotrones' curvature a natural reading.

PART 2 — MMR EXCLUDED ON ONTOLOGICAL GROUNDS
---------------------------------------------
Owner's argument, recorded because it is stronger than a scope decision:
maximum metabolic rate is a temporary "overclock" — unsustainable, costly
to the organism, individual rather than species-characteristic, trainable,
and never a baseline. BMR and MMR are therefore not two points on one
continuum. They are different KINDS of quantity:

  BMR — species-characteristic, sustainable indefinitely, a steady state
  MMR — individual-specific, transient, trainable, incurs recovery debt

This reframes the earlier finding. H5 was described as "unable to reach
MMR at 0.87." The correct statement is that MMR was never in scope: a
formula for sustained metabolic scaling should not be expected to produce
a transient individual peak. The apparent failure was a category error in
the framing, not a deficiency in the formula.

Generalises beyond metabolism: sustained capacity and peak capacity are
distinct quantities in most engineered and evolved systems (continuous vs
peak power rating; base vs boost clock; yield vs ultimate strength;
sustained vs burst bandwidth). They are limited by different things — the
sustained value by what can be maintained indefinitely, the peak by
instantaneous capacity plus tolerance for accumulating debt — so there is
no reason to expect one formula to cover both.

THREE CONSEQUENCES, RECORDED HONESTLY
--------------------------------------
(a) DEFLATIONARY: with endpoints [2/3, 3/4], observed BMR 0.676 implies
    lambda = 0.112. Mammals realise ~11% of the network advantage over
    pure surface scaling. This says WBE's fractal mechanism does very
    little work for resting metabolism. Defensible — it restates White &
    Seymour's 2/3 finding — but it is a real cost of the choice and
    should not be buried.

(b) LAMBDA MAY NOT BE A CONSTANT: if Kolokotrones' curvature is real
    (small mammals ~2/3, large ~3/4), then lambda varies with body mass
    within a taxon. lambda(M) running 0 -> 1 with increasing mass would
    reproduce the curvature automatically, with Xiao's ~10 kg breakpoint
    at lambda ~ 0.5. But this makes lambda mass-dependent rather than a
    species-level structural parameter, which is a third distinct reading
    on top of the state/structure conflation already recorded in H3.

(c) OPEN PUZZLE — THE CURVATURE RUNS THE WRONG WAY FOR THE NAIVE STORY:
    a surface-vs-network constraint crossover predicts the OPPOSITE
    direction from what is observed. Surface-to-volume ratio is HIGH for
    small animals, so heat dissipation is easy for them; large animals
    are the ones with dissipation problems (hence elephant ears, whale
    countercurrent circulation). So a naive surface constraint should
    bind for LARGE animals, giving beta -> 2/3 at large mass. Observed is
    the reverse. Kolokotrones' own proposed mechanism has not been read
    and is NOT reconstructed here. Flagged as open rather than papered
    over.

Run: python3 scripts/migrations/m0_endpoint_decision_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
TODAY = date.today().isoformat()
SESSION = "gsw-endpoint-decision-2026-05-04"


EDITS = [
    # --------------------------------------------------------------- H5
    ("E1_H5_conj", "sections",
     {"entry_id": "H5", "section_name": "What's Conjectured"},
     "content", "append",
     "\n\n---\n\n"
     "**ENDPOINTS SETTLED 2026-05-04 (owner decision).** The bounding "
     "exponents are fixed at\n\n"
     "$$\\beta(\\lambda) = \\lambda \\cdot \\tfrac{3}{4} + (1-\\lambda) "
     "\\cdot \\tfrac{2}{3}$$\n\n"
     "replacing the previous $[d_f/(d_f+1),\\ 1]$. Lower bound is the "
     "**surface law** (heat dissipation through body surface); upper bound "
     "is the **WBE network optimum**. $\\lambda$ is therefore the fraction "
     "of the network advantage realised *over pure surface scaling* — which "
     "is what settles the question H3 was blocked on ($\\lambda$ is a "
     "fraction *of* what).\n\n"
     "Rationale: this range contains the observed strict mammalian BMR of "
     "0.676, maps onto the actual century-long 2/3-vs-3/4 debate rather "
     "than an invented pair, and gives Kolokotrones' curvature a natural "
     "reading.\n\n"
     "**MMR is out of scope — on ontological, not range, grounds.** The "
     "earlier framing of this entry's failure said H5 \"cannot reach MMR at "
     "0.87.\" That framing was wrong. Maximum metabolic rate is a temporary "
     "*overclock*: unsustainable, costly to the organism, individual rather "
     "than species-characteristic, trainable, and never a baseline. BMR and "
     "MMR are not two points on one continuum — they are different **kinds "
     "of quantity**:\n\n"
     "| | BMR | MMR |\n"
     "|---|---|---|\n"
     "| Level | species-characteristic | individual |\n"
     "| Duration | sustainable indefinitely | minutes |\n"
     "| Cost | none beyond upkeep | recovery debt, oxidative stress |\n"
     "| Trainable | no | substantially |\n\n"
     "A formula for *sustained* metabolic scaling should not be expected to "
     "produce a *transient individual peak*. The apparent failure was a "
     "category error in the framing, not a deficiency in the formula.\n\n"
     "This generalises. Sustained capacity and peak capacity are distinct "
     "quantities in most engineered and evolved systems — continuous versus "
     "peak power rating, base versus boost clock, yield versus ultimate "
     "strength, sustained versus burst bandwidth. They are limited by "
     "different things: the sustained value by what can be maintained "
     "indefinitely, the peak by instantaneous capacity plus tolerance for "
     "accumulating debt. There is no reason to expect one formula to cover "
     "both, and the wiki should stop treating the BMR/MMR spread as a "
     "single phenomenon requiring a single explanation.\n\n"
     "**Three consequences, recorded rather than buried:**\n\n"
     "**(a) The choice is deflationary about WBE.** With these endpoints, "
     "observed BMR 0.676 implies $\\lambda = 0.112$ — mammals realise about "
     "**11%** of the network advantage over pure surface scaling. That says "
     "WBE's fractal mechanism does very little work for resting metabolism. "
     "It is defensible (it restates White & Seymour's 2/3 finding) but it "
     "is a real cost of the decision.\n\n"
     "**(b) $\\lambda$ may not be a constant.** If Kolokotrones' curvature "
     "is real, $\\lambda$ varies with body mass *within* a taxon. A "
     "$\\lambda(M)$ running $0 \\to 1$ with increasing mass would reproduce "
     "the curvature automatically, with Xiao's ~10 kg breakpoint at "
     "$\\lambda \\approx 0.5$. But that makes $\\lambda$ mass-dependent "
     "rather than a species-level structural parameter — a **third** "
     "distinct reading, on top of the state-versus-structure conflation "
     "already recorded in H3.\n\n"
     "**(c) OPEN PUZZLE — the curvature runs the wrong way for the obvious "
     "mechanism.** A surface-versus-network constraint crossover predicts "
     "the *opposite* direction from what is observed. Surface-to-volume "
     "ratio is high for small animals, so heat dissipation is easy for "
     "them; large animals are the ones with dissipation problems (elephant "
     "ears, whale countercurrent circulation). So a naive surface "
     "constraint should bind for **large** animals, giving $\\beta \\to "
     "2/3$ at large mass. Observed is the reverse. **Kolokotrones' own "
     "proposed mechanism has not been read and is not reconstructed here.** "
     "This is flagged as open. Anyone adopting the surface-to-network "
     "crossover story should resolve it first."),

    # --------------------------------------------------------------- P14
    ("E2_P14_design", "conjectures", {"id": "P14"}, "critical_gaps", "append",
     "\n\n**DESIGN IMPLICATION OF MMR'S STATUS (2026-05-04).** The endpoint "
     "decision recorded MMR as an individual, trainable, transient "
     "*overclock* rather than a species-characteristic baseline. That "
     "affects P14a, which regresses branching variance against the BMR/MMR "
     "exponent gap.\n\n"
     "**The target is noisier than P14a's framing implies.** Branching "
     "variance is a species-level anatomical property. The cross-taxon MMR "
     "exponent aggregates individual peaks that vary substantially with "
     "fitness, training history, and condition at time of measurement. So "
     "P14a regresses a species property against a gap whose upper term is "
     "individually variable. This does not invalidate the test, but it "
     "means:\n\n"
     "- MMR measurement conditions must be standardised and reported "
     "(wild-caught vs captive, trained vs untrained, season, age)\n"
     "- within-species MMR variance may partly swamp the cross-species "
     "signal\n"
     "- a null result would be ambiguous between \"no relationship\" and "
     "\"relationship obscured by MMR heterogeneity\"\n\n"
     "**A cleaner design exists, at higher cost.** Test *within* a single "
     "species: do individuals with different branching variance have "
     "different MMR? This controls for phylogeny, body plan, and ecology in "
     "one move, and it matches MMR's actual level of description (the "
     "individual). It requires micro-CT and $\\dot{V}O_2$max on the **same "
     "animals**, which is a harder protocol than assembling published "
     "cross-taxon values.\n\n"
     "**Recommendation:** run the cross-taxon version first since the data "
     "largely exist, but pre-register the MMR-heterogeneity concern so a "
     "null is interpretable. Treat the within-species design as the "
     "confirmatory test if the cross-taxon regression is suggestive."),
]


CALIBRATIONS = [
    ("H5", "entry", "Speculative", TODAY, SESSION,
     "Endpoints settled at [2/3, 3/4]; MMR excluded on ontological grounds",
     "Owner decision. Bounding exponents fixed at surface law (2/3) and WBE "
     "network optimum (3/4), replacing [d_f/(d_f+1), 1]. Contains observed "
     "strict mammalian BMR 0.676, maps onto the historical 2/3-vs-3/4 "
     "debate, gives Kolokotrones curvature a natural reading. lambda is now "
     "well-posed as 'fraction of network advantage realised over pure "
     "surface scaling', which unblocks H3's definition question. MMR "
     "excluded not because the formula cannot reach it but because it is a "
     "different KIND of quantity — individual, transient, trainable, costly "
     "— so the earlier 'cannot reach 0.87' framing was a category error. "
     "Deflationary consequence recorded: BMR 0.676 implies lambda = 0.112, "
     "i.e. mammals realise ~11% of the network advantage, so WBE's "
     "mechanism does little work for resting metabolism."),

    ("mmr_sustained_vs_peak_distinction", "structural_observation",
     "Established", TODAY, SESSION,
     "Sustained and peak capacity are different quantities, not two points on one scale",
     "Owner argument, this session. MMR is a temporary overclock: "
     "unsustainable, costly, individual, trainable, never a baseline. BMR is "
     "species-characteristic and sustainable indefinitely. These are "
     "different kinds of quantity and there is no reason to expect one "
     "formula to cover both. Generalises well beyond metabolism — continuous "
     "vs peak power rating, base vs boost clock, yield vs ultimate strength, "
     "sustained vs burst bandwidth — because the sustained value is limited "
     "by what can be maintained indefinitely while the peak is limited by "
     "instantaneous capacity plus tolerance for accumulating debt. Filed as "
     "Established because it is a conceptual distinction verifiable by "
     "inspection, not an empirical claim. Consequence: the wiki should stop "
     "treating the BMR/MMR spread as one phenomenon needing one explanation."),

    ("curvature_direction_puzzle", "open_question", "Speculative",
     TODAY, SESSION,
     "Observed curvature runs opposite to the naive surface-vs-network crossover",
     "OPEN. Kolokotrones 2010 finds slope ~2/3 for small mammals and ~3/4 "
     "for large. The obvious mechanism — a crossover between surface-limited "
     "and network-limited regimes — predicts the OPPOSITE direction. "
     "Surface-to-volume ratio is high for small animals so heat dissipation "
     "is easy for them; large animals have the dissipation problem (elephant "
     "ears, whale countercurrent circulation). A naive surface constraint "
     "should therefore bind for LARGE animals, giving beta -> 2/3 at large "
     "mass. Observed is the reverse. Kolokotrones' own proposed mechanism "
     "has NOT been read and is not reconstructed. Anyone adopting the "
     "surface-to-network crossover reading of lambda(M) must resolve this "
     "first. Recorded so the gap is not silently inherited."),

    ("P14a", "conjecture", "Speculative", TODAY, SESSION,
     "Design implication: MMR heterogeneity makes a null result ambiguous",
     "MMR's status as an individual, trainable, transient quantity means "
     "P14a regresses a species-level anatomical property (branching "
     "variance) against a gap whose upper term varies substantially within "
     "species. Consequences: MMR measurement conditions must be standardised "
     "and reported; within-species variance may partly swamp the "
     "cross-species signal; a null result is ambiguous between 'no "
     "relationship' and 'relationship obscured by heterogeneity'. A cleaner "
     "within-species design exists (micro-CT plus VO2max on the same "
     "animals) matching MMR's actual level of description, at higher "
     "protocol cost. Recommendation: run cross-taxon first since the data "
     "largely exist, but pre-register the heterogeneity concern so a null is "
     "interpretable; treat within-species as confirmatory."),
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
        (suffix,) = args
        if current.endswith(suffix):
            print(f"  [{label}] OK — already applied, skipping")
            continue
        planned.append((label, table, where, col, current + suffix))
        print(f"  [{label}] OK — append (+{len(suffix)} chars)")
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
        print("\nAll edits already applied.")

    print()
    print("=" * 72)
    print("PHASE 4 — calibration")
    print("=" * 72)
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    hcur = hc.cursor()
    n = 0
    for (eid, etype, confv, cdate, aref, short, rationale) in CALIBRATIONS:
        hcur.execute("""
            INSERT INTO confidence_calibration (entity_id, entity_type,
                confidence, calibration_date, audit_ref, short_status, rationale)
            VALUES (?,?,?,?,?,?,?)
        """, (eid, etype, confv, cdate, aref, short, rationale))
        n += 1
    hc.commit(); hc.close()
    print(f"  calibrations inserted: {n}")
    print()
    print(f"Migration complete. Session: {SESSION}")


if __name__ == "__main__":
    main()
