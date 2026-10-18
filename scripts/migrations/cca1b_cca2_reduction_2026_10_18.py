r"""
CCA-1b-magnitude and CCA-2 reduction test — 2026-10-18 (audit_ref gsw-cca1b-cca2-reduction-2026-10-18). Mode B.

Report: docs/experiments/CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md (pre-registration commit 9a3c125)
Analysis: scripts/cca1b_cca2_reduction.py → data/reports/cca1b_cca2_reduction_2026_10/

Verdicts: CCA-1b-magnitude REDUCES (pre-registered rule). CCA-2 REDUCES on substance; the 1e-8
spectral tolerance was missed in 10/45 configurations by the tool's EPS = 1e-10 guard (owner accepted
the substantive reading before this was applied).

Writes:
- ds_wiki.db: gloss_effective_dimension "Why this disambig exists" — dated qualifier appended after the
  last sentence (single composed write; original text unchanged).
- calibration (append-only): CCA-1b-magnitude Supported → Retired (Folded); CCA-2 Supported → Retired
  (forced by definition).

Dry run by default; --apply writes. Idempotent; read-back verified.
"""
import argparse
import sqlite3
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")
WIKI_HISTORY_DB = Path("data/wiki_history.db")
AUDIT_REF = "gsw-cca1b-cca2-reduction-2026-10-18"
D = "2026-10-18"
REPORT = "docs/experiments/CCA1B_CCA2_REDUCTION_TEST_2026_10_18.md"

SEC_ENTRY, SEC_NAME = "gloss_effective_dimension", "Why this disambig exists"
ANCHOR_TEXT = "Wiki conjectures referencing 'D_eff' must pin which sense applies."
QUALIFIER = (
    f" (Added {D}, `{AUDIT_REF}`: a further sense, not listed above, is the gap-position d_eff of "
    "`src/analysis/fisher_diagnostics.decompose_fim` — argmax_i σ_i/σ_{i+1} + 1 on a per-node Fisher matrix. "
    "The April 2026 CCA Phases A–D (including CCA-2, 'd_eff = d + 1') used this sense, not the participation "
    "ratio. On hypercubic tori it can only take the values 1, d or d + 1, fixed by lattice symmetry and the kernel "
    f"setting; see `{REPORT}`.)"
)

CALIBRATIONS = [
    ("CCA-1b-magnitude", "cca_conjecture", "Retired", D, AUDIT_REF,
     "Folded: Phase C/D η is a fixed function of the NN bond energy c̄ = −E/2NJ (η = c̄ in one branch); the ~20× "
     "dη/dT separation is latent heat (Baxter 1973; Wu 1982) vs 2D Ising log specific heat (Onsager 1944)",
     "Reduction test on the saved Phase C/D outputs (no new MC), hypothesis and verdict rules pre-registered (commit "
     "9a3c125) — " + REPORT + ". The April 'η' is not Phase E's Zipf exponent: it is the gap ratio σ_{d_eff+1}/σ_{d_eff} "
     "of a per-node 4×4 Fisher matrix (fisher_diagnostics.analyze_node) on the torus with edge weights −ln c_e, c_e = "
     "MC mean of δ(s_i,s_j). With uniform weights −ln c̄ the graph is exactly the bare torus at kernel α′ = −ln c̄, so "
     "η = H_L(α′) in closed form, and c̄ = −E/(2NJ) is the energy per bond. Result: pooled R² = 0.992 over 126 Phase D "
     "points (threshold 0.90; Phase C 0.954); predicted q10/q2 S_max ratio / measured = 1.26, 0.98, 1.06 at L = 16, 32, 48 "
     "(band 0.5–2). The separation is mostly the energy factor (max|dc̄/dT| 9–18× larger at q=10); the geometric lens "
     "contributes 0.8–1.5×. In 2D for 0.61 ≲ −ln c̄ ≲ 0.88, η = c̄ exactly (L→∞). The fixed-trace/λ₁ route does not apply "
     "(this η is not built from χ). Pre-registered verdict: REDUCES. The literature answers the question as the claim "
     "did (yes, it separates the orders, via the energy jump), so Folded, not Falsified. Pattern tags: "
     "restatement-in-new-vocabulary; trivial-from-known-result. Revertible by appending a later row."),
    ("CCA-2", "cca_conjecture", "Retired", D, AUDIT_REF,
     "Forced by definition: gap-position d_eff on hypercubic tori ∈ {1, d, d+1} by point-group symmetry; d+1 = d "
     "translations + 1 uncentred-mean mode, in an α window only; centred FIM gives d",
     "Reduction test on the saved Phase A outputs (no MC), pre-registered (commit 9a3c125) — " + REPORT + ". Phase A's "
     "d_eff is the gap position argmax σ_i/σ_{i+1} + 1 of a per-node 2d×2d Fisher matrix on the bare torus (kernel "
     "exp(−α·hop)), not a participation ratio and not built from any correlation matrix. The kernel factorises over "
     "axes, so F has exactly three levels: λ_T (×d, translations), λ_A = λ_E + 2d·m² (×1; m = −KL per axis, the "
     "uncentred mean score) and λ_E (×(d−1)), closed form in (α, L). Result: closed-form d_eff = analyze_node = recorded "
     "Phase A d_eff in 45/45 torus configs, η within 1.3e-7 in 45/45; centred FIM gives d_eff = d wherever λ_T ≠ λ_E. "
     "d+1 holds only for α ≈ 0.6–1.2 (2D), 0.4–0.9 (3D L=6), ~11% of the α grid; d for smaller α, 1 for larger. The 4³ "
     "'finite-size artifact' is exact: λ_T ≡ λ_E at L = 4. Deviation: the pre-registered 1e-8 spectral tolerance failed "
     "in 10/45 configs (max 3.0e-7), all at large α where the tool's EPS = 1e-10 cut zeroes tiny probabilities; without "
     "the cut the match is 3.5e-15 in 45/45 (post-hoc). Owner accepted the substantive REDUCES reading. The statement is "
     "true within its window and contradicted by nothing — forced, not wrong — so Retired, not Falsified. Secondary: "
     "read as Phase E's χ participation ratio, d_eff at T_c (q=2) is 3.65/3.73/4.72 at L=16/24/32, growing with L, not "
     "d+1. Pattern tags: answer-forced-by-definition; trivial-from-known-result (point-group irreps; Fisher rank of a "
     "location family). Revertible by appending a later row."),
]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DS_WIKI_DB)
    rows = conn.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (SEC_ENTRY, SEC_NAME)).fetchall()
    conn.close()
    if len(rows) != 1: raise SystemExit(f"[{SEC_ENTRY}] FAIL — {len(rows)} matching sections")
    cur_v = rows[0][0]
    if ANCHOR_TEXT + QUALIFIER in cur_v:
        new_v = None; print(f"  [{SEC_ENTRY}] OK — already applied")
    else:
        if cur_v.count(ANCHOR_TEXT) != 1: raise SystemExit(f"[{SEC_ENTRY}] FAIL — anchor count {cur_v.count(ANCHOR_TEXT)}")
        new_v = cur_v.replace(ANCHOR_TEXT, ANCHOR_TEXT + QUALIFIER, 1)
        print(f"  [{SEC_ENTRY}] plan — qualifier (+{len(QUALIFIER)} chars)")
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    cals = []
    for c in CALIBRATIONS:
        got = hc.execute("SELECT short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                         (c[0], c[3], c[4])).fetchone()
        if got is None:
            if not hc.execute("SELECT 1 FROM confidence_calibration WHERE entity_id=?", (c[0],)).fetchone():
                raise SystemExit(f"[cal {c[0]}] ABORT — no prior history")
            cals.append(c); print(f"  [cal {c[0]}] plan — {c[2]}: {c[5][:70]}")
        elif got[0] != c[5]:
            print(f"  [cal {c[0]}] COLLISION — slot held by a different row ({got[0][:60]!r}); NOT written")
        else:
            print(f"  [cal {c[0]}] OK — already present")
    hc.close()
    print(f"  {1 if new_v else 0} section write, {len(cals)} calibration rows")
    if not a.apply:
        print("DRY RUN — nothing written. Re-run with --apply."); return
    if new_v:
        conn = sqlite3.connect(DS_WIKI_DB)
        c = conn.execute("UPDATE sections SET content=? WHERE entry_id=? AND section_name=?", (new_v, SEC_ENTRY, SEC_NAME))
        if c.rowcount != 1: conn.rollback(); raise SystemExit("rowcount")
        conn.commit(); conn.close()
    hc = sqlite3.connect(WIKI_HISTORY_DB)
    for c in cals:
        hc.execute("""INSERT INTO confidence_calibration (entity_id, entity_type, confidence, calibration_date, audit_ref,
                      short_status, rationale) VALUES (?,?,?,?,?,?,?)""", c)
    hc.commit()
    bad = []
    if new_v:
        conn = sqlite3.connect(DS_WIKI_DB)
        if conn.execute("SELECT content FROM sections WHERE entry_id=? AND section_name=?", (SEC_ENTRY, SEC_NAME)).fetchone()[0] != new_v:
            bad.append(SEC_ENTRY)
        conn.close()
    for c in CALIBRATIONS:
        if hc.execute("SELECT confidence, short_status FROM confidence_calibration WHERE entity_id=? AND calibration_date=? AND audit_ref=?",
                      (c[0], c[3], c[4])).fetchone() != (c[2], c[5]):
            bad.append(c[0])
    hc.close()
    if bad: raise SystemExit(f"Post-write drift: {bad}")
    print("  verified")


if __name__ == "__main__":
    main()
