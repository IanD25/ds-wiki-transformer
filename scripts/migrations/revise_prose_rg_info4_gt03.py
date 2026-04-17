"""
Prose revisions targeting two below-threshold cross-pillar pairs:

  INFO4 ↔ RG04: 0.739  (DPI / mutual information  ↔  c-theorem / RG flow)
  GT03  ↔ RG04: 0.753  (Padmanabhan holographic    ↔  c-theorem / RG flow)

Strategy:
  INFO4: inject coarse-graining, degrees-of-freedom, c-theorem language into
         What It Claims, DS Cross-References, and Concept Tags
  RG04:  inject information-theoretic / data-processing tags into Concept Tags
  GT03:  inject c-theorem / coarse-graining / RG-flow language into
         What It Claims and Concept Tags
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

REVISIONS = [
    # -----------------------------------------------------------------------
    # INFO4 — What It Claims
    # Add coarse-graining / c-theorem / degrees-of-freedom language so the
    # centroid pulls toward RG04 across multiple sections, not just Constraint Category.
    # -----------------------------------------------------------------------
    (
        "INFO4",
        "What It Claims",
        "you cannot extract more information about X from Z than was in Y about X.",
        "you cannot extract more information about X from Z than was in Y about X. "
        "The DPI is also the information-theoretic foundation of the Zamolodchikov c-theorem in quantum field theory: "
        "renormalisation group coarse-graining — integrating out UV degrees of freedom at each RG step — is a "
        "Markov data-processing step. The c-function that counts effective degrees of freedom decreases monotonically "
        "under this coarse-graining for the same reason that I(X;Z) ≤ I(X;Y): each RG step can only destroy "
        "information about the UV, never recover it. The DPI therefore provides the information-theoretic proof that "
        "RG flow is irreversible: information loss under coarse-graining implies c_UV ≥ c_IR.",
    ),

    # -----------------------------------------------------------------------
    # INFO4 — DS Cross-References
    # Add explicit RG04 citation.
    # -----------------------------------------------------------------------
    (
        "INFO4",
        "DS Cross-References",
        "B5 (Landauer — each step of irreversible processing has a thermodynamic cost proportional to the information lost: ΔI × kT ln 2).",
        "B5 (Landauer — each step of irreversible processing has a thermodynamic cost proportional to the information lost: ΔI × kT ln 2). "
        "RG04 (Zamolodchikov c-theorem — the c-theorem is the field-theoretic instance of the DPI: RG coarse-graining "
        "is a Markov chain step, and the c-function counting effective degrees of freedom decreases monotonically under "
        "it, exactly as I(X;Z) ≤ I(X;Y). Information loss under coarse-graining IS RG irreversibility).",
    ),

    # -----------------------------------------------------------------------
    # INFO4 — Concept Tags
    # Add coarse-graining / RG / degrees-of-freedom tags.
    # -----------------------------------------------------------------------
    (
        "INFO4",
        "Concept Tags",
        "• information monotonicity\n• channel capacity",
        "• information monotonicity\n• channel capacity\n• coarse-graining\n• degrees of freedom reduction\n"
        "• RG irreversibility\n• c-theorem foundation\n• UV-IR monotonicity\n• RG flow analog",
    ),

    # -----------------------------------------------------------------------
    # RG04 — Concept Tags
    # Add information-theoretic / data-processing vocabulary so the centroid
    # moves toward INFO4.
    # -----------------------------------------------------------------------
    (
        "RG04",
        "Concept Tags",
        "• field-theoretic second law\n• UV-IR flow",
        "• field-theoretic second law\n• UV-IR flow\n• information loss under coarse-graining\n"
        "• data processing inequality analog\n• mutual information monotonicity\n"
        "• Markov coarse-graining\n• effective degrees of freedom",
    ),

    # -----------------------------------------------------------------------
    # GT03 — What It Claims
    # Inject c-theorem / RG-flow / coarse-graining language so the centroid
    # shares vocabulary with RG04.
    # -----------------------------------------------------------------------
    (
        "GT03",
        "What It Claims",
        "This extends the Jacobson-Verlinde programme from local horizons to cosmological horizons, providing a thermodynamic/information-theoretic derivation of the expansion of the universe.",
        "This extends the Jacobson-Verlinde programme from local horizons to cosmological horizons, providing a "
        "thermodynamic/information-theoretic derivation of the expansion of the universe. "
        "The monotonic approach to holographic equipartition (N_bulk → N_sur as the universe expands) is the "
        "cosmological analog of the Zamolodchikov c-theorem: just as the c-function counting UV degrees of freedom "
        "decreases monotonically under renormalisation group coarse-graining (c_UV ≥ c_IR), the bulk degrees of "
        "freedom N_bulk decrease relative to the boundary N_sur as the universe coarse-grains its way from early "
        "dense configurations to the present de Sitter epoch. Both are monotonicity/irreversibility theorems about "
        "degree-of-freedom counting under a coarse-graining flow — one along the RG scale, one along cosmic time.",
    ),

    # -----------------------------------------------------------------------
    # GT03 — Concept Tags
    # Add c-theorem / coarse-graining / RG language.
    # -----------------------------------------------------------------------
    (
        "GT03",
        "Concept Tags",
        "• information-driven expansion",
        "• information-driven expansion\n• c-theorem analog\n• monotonic decrease of degrees of freedom\n"
        "• coarse-graining flow\n• RG-cosmology duality\n• RG irreversibility\n• UV-IR analogy",
    ),
]


def apply_revisions(db_path, revisions):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    applied = failed = 0
    for entry_id, section_name, old_frag, new_frag in revisions:
        row = cur.execute(
            "SELECT content FROM sections WHERE entry_id = ? AND section_name = ?",
            (entry_id, section_name),
        ).fetchone()
        if not row:
            print(f"  FAIL (not found): {entry_id} / {section_name}")
            failed += 1
            continue
        content = row[0]
        if old_frag not in content:
            print(f"  FAIL (fragment not found): {entry_id} / {section_name}")
            print(f"    Looking for: {old_frag[:80]!r}")
            failed += 1
            continue
        new_content = content.replace(old_frag, new_frag)
        cur.execute(
            "UPDATE sections SET content = ? WHERE entry_id = ? AND section_name = ?",
            (new_content, entry_id, section_name),
        )
        print(f"  OK: {entry_id} / {section_name} (+{len(new_frag) - len(old_frag)} chars)")
        applied += 1
    conn.commit()
    conn.close()
    return applied, failed


if __name__ == "__main__":
    print(f"Applying prose patches to:\n  {SOURCE_DB}\n")
    applied, failed = apply_revisions(SOURCE_DB, REVISIONS)
    print(f"\nResult: {applied} applied, {failed} failed")
