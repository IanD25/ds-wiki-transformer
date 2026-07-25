"""
Maldacena Deep Research Pass — Tier B ds_wiki.db Prose Corrections — 2026-05-04

Owner-approved 2026-05-04. Companion to:
  scripts/migrations/m0_maldacena_research_pass_2026_05_04.py
which inserted anchors and calibration records to wiki_history.db.

This script applies the corresponding ds_wiki.db prose corrections (B1-B7).
Per the architecture rule, schema is unchanged — only existing rows are
UPDATE'd in place. ds_wiki.db is in git, so changes are git-reversible.

Edits:
  B1  P17.critical_gaps   — Amendola "5σ" → 2σ upper limits k<2.1, 5σ was forecast
  B2  P17.phase1_results  — same Amendola correction + DESI DR2 σ-level update
  B3  P23.critical_gaps   — Amendola "5-sigma rejection" → ~3σ tension correction
  B4  P21.claim           — append deep-research addendum disambiguating
                            classical Fisher-Rao from quantum Bures/Petz
  B5  GT02.What It Claims — append Verlinde contested-status paragraph
                            (Brouwer 2017 positive + 4 published negatives)
  B6  GT04.What It Claims — insert quantum-vs-classical-Fisher disambiguation
                            after the matrix-defined sentence
  B7  GT10.What It Claims — append Casini-Galante-Myers scope caveat +
                            Faulkner-Lashkari-Van Raamsdonk parallel result

Method: each edit uses str.replace on a unique substring of the existing
text. Script verifies each replacement actually changed the string before
doing the UPDATE. If any anchor substring is not found verbatim, the script
aborts WITHOUT writing — no partial state.

Run: python3 scripts/migrations/m0_maldacena_tier_b_prose_2026_05_04.py
"""

from __future__ import annotations
import sqlite3
import sys
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
SESSION = "gsw-maldacena-deep-research-2026-05-04"


# ============================================================================
# EDIT SPECIFICATIONS
# Each spec: (label, table, where_clause_kwargs, column, mode, *args)
# Modes:
#   "replace": (find_text, replace_text)
#   "append":  (text_to_append,)
# ============================================================================

EDITS = [
    # --------------------------------------------------------------------
    # B1 — P17.critical_gaps: Amendola 5σ correction
    # --------------------------------------------------------------------
    ("B1", "conjectures", {"id": "P17"}, "critical_gaps", "replace",
     # FIND
     "5. GW MERGER RATE REJECTION: Amendola et al. (MNRAS 528, 2377, 2024) "
     "showed GW merger rates reject k = 3 beyond 5 sigma — predicted rates "
     "exceed LIGO-Virgo-KAGRA observations by two orders of magnitude.",
     # REPLACE
     "5. GW MERGER RATE TENSION (corrected 2026-05-04): Amendola, Rodrigues, "
     "Kumar, Quartin (MNRAS 528, 2377, 2024; arXiv:2307.02474) place 2σ "
     "upper limits k < 2.1 (PLPP method, GWTC-3) on cosmologically-coupled "
     "BHs, in ~3σ tension with k=3 but not ruling it out from current data. "
     "The 5σ figure was the paper's FORECAST for ~250 additional events, "
     "NOT the current-data result. Original wiki claim of '>5σ rejection' "
     "was a misreading; corrected per M0 Fifth Addendum + 2026-05-04 "
     "deep-research pass."),

    # --------------------------------------------------------------------
    # B2 — P17.phase1_results: two corrections in same column
    # B2a: Amendola 5σ
    # B2b: DESI DR2 σ-level
    # We do these as two replaces against the same column; do them in
    # order via two EDIT entries so each verifies independently.
    # --------------------------------------------------------------------
    ("B2a", "conjectures", {"id": "P17"}, "phase1_results", "replace",
     # FIND
     "- GW merger rates reject k = 3 at >5 sigma (Amendola 2024).",
     # REPLACE
     "- GW merger rates currently in ~3σ tension with k = 3 (Amendola 2024 "
     "GWTC-3 2σ upper limits k<2.1; the 5σ rejection was the paper's "
     "FORECAST for ~250 additional events, not current data — corrected "
     "2026-05-04)."),

    ("B2b", "conjectures", {"id": "P17"}, "phase1_results", "replace",
     # FIND
     "- DESI DR2 (March 2025): Strengthened evolving dark energy signal to 3.9 sigma.",
     # REPLACE
     "- DESI DR2 (March 2025; Phys. Rev. D 112, 083515; arXiv:2503.14738): "
     "reports w0wa-CDM tension with ΛCDM at 2.8σ (Pantheon+) / 3.8σ "
     "(Union3) / 4.2σ (DES-SN5YR), depending on SN Ia compilation. NO "
     "DESI dataset clears the 5σ discovery threshold. Sapone-Nesseris "
     "2025 EPJC (arXiv:2504.15222) flags compilation/prior sensitivity. "
     "(Updated 2026-05-04.)"),

    # --------------------------------------------------------------------
    # B3 — P23.critical_gaps: Amendola "5-sigma" correction
    # --------------------------------------------------------------------
    ("B3", "conjectures", {"id": "P23"}, "critical_gaps", "replace",
     # FIND
     "GW 5-sigma rejection of k = 3 (Amendola 2024)",
     # REPLACE
     "GW ~3σ tension with k = 3 (Amendola 2024 GWTC-3 2σ upper limits "
     "k<2.1; 5σ figure was a forecast for ~250 additional events, not "
     "current data — corrected 2026-05-04)"),

    # --------------------------------------------------------------------
    # B4 — P21.claim: append deep-research addendum
    # The existing claim contains the "REFINED SCOPE" block already; we
    # append a 2026-05-04 addendum AFTER that.
    # --------------------------------------------------------------------
    ("B4", "conjectures", {"id": "P21"}, "claim", "append",
     "\n\n**ADDENDUM 2026-05-04 (deep-research pass):** The four-instance "
     "support list (1)–(4) above conflates two distinct mathematical "
     "objects under the name 'Fisher metric'. (1) Ruppeiner-on-Gibbs and "
     "(4) Fisher-Rao non-equilibrium dissipation paths are both CLASSICAL "
     "Fisher-Rao on probability-distribution parameter manifolds; "
     "Brody-Rivier 1995 (PRE 51, 1006) proved Ruppeiner ⊂ Fisher-Rao on "
     "the Gibbs canonical family in the thermodynamic limit. These are "
     "correctly covered by Chentsov uniqueness (Chentsov 1972/1982; "
     "extended by Ay-Jost-Lê-Schwachhöfer 2015 arXiv:1306.1465 from "
     "finite simplices to general statistical manifolds). (3) Bianconi "
     "2025 PRD 111, 066001 uses QUANTUM relative entropy on density-"
     "matrix-valued metrics; the Hessian is the BURES / quantum Fisher "
     "metric on density matrices, governed by the Petz 1996 (Lin. Alg. "
     "Appl. 244, 81) FAMILY of monotone metrics — no single canonical "
     "choice; Bures (smallest), BKM (unique self-dual), RLD (largest), "
     "Wigner-Yanase as distinguished members. Bures and classical "
     "Fisher-Rao coincide only in the commutative limit. The P21 "
     "universality claim therefore SPLITS: Established for the classical-"
     "Fisher-Rao instances under Chentsov + Ay-Jost-Lê-Schwachhöfer; "
     "Established-AS-CLASSIFICATION (not uniqueness) for the quantum "
     "Fisher / Bures case under Petz; the bridge from one to the other "
     "is the commutative-limit identification, not a deeper theorem. "
     "The 'IT08 ↔ GT04 sim 0.853' similarity score reflects vocabulary "
     "proximity, not mathematical equivalence between classical Fisher-"
     "Rao and the Bures-family object Bianconi uses."),

    # --------------------------------------------------------------------
    # B5 — GT02 'What It Claims' section: append Verlinde contested status
    # --------------------------------------------------------------------
    ("B5", "sections",
     {"entry_id": "GT02", "section_name": "What It Claims"},
     "content", "append",
     "\n\n**Status (2026-05-04 deep-research pass):** Contested in the "
     "published literature with mixed empirical results. POSITIVE: "
     "Brouwer et al. 2017 (MNRAS 466, 2547) tested the Verlinde 2017 "
     "prediction against weak-lensing data on 33,613 galaxies and found "
     "agreement WITHOUT free parameters at galactic scales. NEGATIVE: "
     "Kobakhidze 2011 (PRD 83, 021502) — quantized gravitational states "
     "observed in the GRANIT ultra-cold-neutron experiment are inconsistent "
     "with an entropic-force derivation; Visser 2011 (JHEP 10, 140) — "
     "entropic-force derivations of conservative many-body forces require "
     "unphysical entropy structures and multiple temperature baths; "
     "Hossenfelder & collaborators 2017 (JHEP 11, 007 'Inconsistencies in "
     "Verlinde's emergent gravity') — the elastic-strain MOND derivation "
     "is not self-consistent and a careful redo recovers Newtonian, not "
     "MOND, gravity, with solar-system constraints conflicting; "
     "Dai-Stojkovic 2017 (PRD 96, 108501) — Hossenfelder's covariant "
     "version fails to recover stable de Sitter. The Verlinde program is "
     "currently in active debate, not consensus."),

    # --------------------------------------------------------------------
    # B6 — GT04 'What It Claims' section: insert quantum-vs-classical
    # disambiguation after the matrix-defined sentence
    # --------------------------------------------------------------------
    ("B6", "sections",
     {"entry_id": "GT04", "section_name": "What It Claims"},
     "content", "replace",
     # FIND — end of "the quantum Fisher information matrix — defines a
     # Riemannian metric on the space of quantum states." then continues
     # with "This metric generates curvature, and the curvature satisfies
     # equations analogous to Einstein's field equations."
     "the quantum Fisher information matrix — defines a Riemannian metric "
     "on the space of quantum states. This metric generates curvature, "
     "and the curvature satisfies equations analogous to Einstein's field "
     "equations.",
     # REPLACE
     "the quantum Fisher information matrix — defines a Riemannian metric "
     "on the space of quantum states. **Disambiguation (2026-05-04):** the "
     "'Fisher information matrix' here is the QUANTUM Fisher information / "
     "Bures metric on density matrices, governed by the Petz 1996 family "
     "of monotone metrics (non-unique; Bures is the smallest, BKM the "
     "unique self-dual, RLD the largest). It is NOT the classical Fisher-"
     "Rao metric on a parameter manifold of probability distributions "
     "(the M6 / Ax2 / CCA Fisher object), which is unique by Chentsov "
     "1972/1982. The two coincide only in the commutative limit. "
     "Bianconi's framework therefore is not a continuous extension of "
     "the classical-Fisher-Rao parameter-space-compression programme "
     "(Sethna sloppy models); it is a quantum-information-geometric "
     "construction that uses a different mathematical object. This metric "
     "generates curvature, and the curvature satisfies equations "
     "analogous to Einstein's field equations."),

    # --------------------------------------------------------------------
    # B7 — GT10 'What It Claims' section: append Casini-Galante-Myers
    # scope caveat + Faulkner-Lashkari-Van Raamsdonk parallel result
    # --------------------------------------------------------------------
    ("B7", "sections",
     {"entry_id": "GT10", "section_name": "What It Claims"},
     "content", "append",
     "\n\n**Scope caveat (2026-05-04 deep-research pass):** Jacobson's "
     "derivation requires the modular Hamiltonian on a small geodesic "
     "ball to reduce to the boost generator. Casini-Galante-Myers 2016 "
     "(JHEP 03 (2016) 194; arXiv:1601.00528) showed via holographic "
     "calculation that THIS ASSUMPTION FAILS for relevant operators with "
     "low conformal dimensions. The Einstein-equation derivation is "
     "therefore established for conformal fields but is NOT universal "
     "across QFTs without separate verification of the modular-H "
     "structure. Faulkner-Lashkari-Van Raamsdonk 2014 (JHEP 03 (2014) "
     "051; arXiv:1312.7856) provides a parallel theorem-level holographic "
     "bridge from the boundary entanglement first law to LINEARIZED bulk "
     "Einstein equations within AdS/CFT. Faulkner et al. 2017 (JHEP 08 "
     "(2017) 057) extends toward nonlinear order — but only within "
     "AdS/CFT, not via Jacobson-style local entanglement equilibrium. "
     "Both results are linearized within their stated regimes; nonlinear "
     "Einstein from entanglement remains restricted to AdS/CFT."),
]


def fetch_value(cur, table: str, where: dict[str, str], col: str) -> str:
    where_sql = " AND ".join(f"{k}=?" for k in where.keys())
    cur.execute(f"SELECT {col} FROM {table} WHERE {where_sql}", tuple(where.values()))
    row = cur.fetchone()
    if row is None:
        raise RuntimeError(f"Row not found: {table} where {where}")
    return row[0] or ""


def update_value(cur, table: str, where: dict[str, str], col: str, new_value: str) -> int:
    where_sql = " AND ".join(f"{k}=?" for k in where.keys())
    cur.execute(
        f"UPDATE {table} SET {col}=? WHERE {where_sql}",
        (new_value, *where.values()),
    )
    return cur.rowcount


def main() -> None:
    if not DS_WIKI_DB.exists():
        raise SystemExit(f"Cannot find {DS_WIKI_DB}; run from repo root")

    # Phase 1: dry-run validate every edit can find its anchor substring
    # without writing anything. Abort if any fails.
    print("=" * 70)
    print("PHASE 1: Validation (dry run, no writes)")
    print("=" * 70)
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    planned: list[tuple[str, str, dict, str, str, str]] = []  # (label, table, where, col, old, new)

    for spec in EDITS:
        label, table, where, col, mode, *args = spec
        current = fetch_value(cur, table, where, col)

        if mode == "replace":
            find_text, replace_text = args
            if find_text not in current:
                print(f"  [{label}] FAIL — anchor substring not found in {table}.{col} where {where}")
                print(f"           Looking for: {find_text[:80]!r}...")
                conn.close()
                raise SystemExit(f"Aborting before any writes; fix anchor substring for {label}")
            new_value = current.replace(find_text, replace_text, 1)
            if new_value == current:
                print(f"  [{label}] FAIL — replacement was a no-op")
                conn.close()
                raise SystemExit(f"Aborting; replacement no-op for {label}")
            print(f"  [{label}] OK    — replace verified ({len(find_text)} chars → {len(replace_text)} chars)")
            planned.append((label, table, where, col, current, new_value))

        elif mode == "append":
            (suffix,) = args
            if current.endswith(suffix):
                print(f"  [{label}] OK    — already appended (idempotent)")
                continue
            new_value = current + suffix
            print(f"  [{label}] OK    — append verified (+{len(suffix)} chars)")
            planned.append((label, table, where, col, current, new_value))

        else:
            raise RuntimeError(f"Unknown mode {mode}")

    conn.close()

    if not planned:
        print("\nAll edits are no-ops (already applied). Nothing to do.")
        return

    print(f"\nValidation passed for {len(planned)} edits.")
    print()

    # Phase 2: Apply
    print("=" * 70)
    print("PHASE 2: Apply (writing to ds_wiki.db)")
    print("=" * 70)
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    for label, table, where, col, old, new in planned:
        rowcount = update_value(cur, table, where, col, new)
        if rowcount != 1:
            print(f"  [{label}] FAIL — UPDATE affected {rowcount} rows (expected 1)")
            conn.rollback()
            conn.close()
            raise SystemExit(f"Aborted after partial work; rolled back. Failure on {label}")
        print(f"  [{label}] WRITE — {table} {where} {col}: 1 row updated")

    conn.commit()
    conn.close()

    # Phase 3: Verify
    print()
    print("=" * 70)
    print("PHASE 3: Post-write verification")
    print("=" * 70)
    conn = sqlite3.connect(DS_WIKI_DB)
    cur = conn.cursor()
    all_ok = True
    for label, table, where, col, old, expected_new in planned:
        actual = fetch_value(cur, table, where, col)
        if actual == expected_new:
            print(f"  [{label}] OK    — verified")
        else:
            print(f"  [{label}] DRIFT — actual ≠ expected (length {len(actual)} vs {len(expected_new)})")
            all_ok = False
    conn.close()

    if not all_ok:
        raise SystemExit("Post-write verification found drift; investigate ds_wiki.db state")

    print()
    print(f"Migration complete. Session: {SESSION}")
    print(f"Total edits applied: {len(planned)}")


if __name__ == "__main__":
    main()
