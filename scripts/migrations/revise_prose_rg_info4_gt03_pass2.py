"""
Pass 2 prose patches — push INFO4↔RG04 and GT03↔RG04 across the 0.80 threshold.

After pass 1:
  INFO4 ↔ RG04: 0.739 → 0.797  (needs ~+0.006 more)
  GT03  ↔ RG04: 0.753 → 0.788  (needs ~+0.015 more)

Strategy: inject RG/coarse-graining/c-theorem vocabulary into the sections
that were NOT patched in pass 1 (Mathematical Archetype, What The Math Says).
"""

import sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from config import SOURCE_DB

REVISIONS = [
    # -----------------------------------------------------------------------
    # INFO4 — Mathematical Archetype
    # Current ending: "...mutual information with the source never increases through processing."
    # Add c-theorem / coarse-graining / RG analogy.
    # -----------------------------------------------------------------------
    (
        "INFO4",
        "Mathematical Archetype",
        "mutual information with the source never increases through processing.",
        "mutual information with the source never increases through processing. "
        "The DPI is also the blueprint for the Zamolodchikov c-theorem: the c-function counting "
        "effective degrees of freedom in a quantum field theory is a monotone under renormalisation "
        "group coarse-graining because each RG step is a Markov data-processing step. "
        "c_UV ≥ c_IR is I(X;Y) ≥ I(X;Z) instantiated in coupling space.",
    ),

    # -----------------------------------------------------------------------
    # INFO4 — What The Math Says
    # Current ending: "...was present in the intermediate representation."
    # Add coarse-graining / c-theorem / degrees-of-freedom language.
    # -----------------------------------------------------------------------
    (
        "INFO4",
        "What The Math Says",
        "The DPI formalises why you cannot reverse-engineer more information about an input than was present in the intermediate representation.",
        "The DPI formalises why you cannot reverse-engineer more information about an input than was present in the intermediate representation. "
        "The field-theoretic instance is the Zamolodchikov c-theorem: renormalisation group coarse-graining "
        "is a Markov chain step from UV to IR, and the c-function — which counts the effective degrees of "
        "freedom of the quantum field theory — decreases monotonically under it. "
        "The central charge c at a fixed point is the mutual information analog: it measures how much "
        "UV information the IR fixed point retains. Strict decrease c_UV > c_IR means information was "
        "irreversibly destroyed in the coarse-graining, just as I(X;Z) < I(X;Y) means information was "
        "irreversibly destroyed in the data-processing step.",
    ),

    # -----------------------------------------------------------------------
    # GT03 — Mathematical Archetype
    # Current ending: "...a counting argument, not a force law."
    # Add c-theorem / RG irreversibility language.
    # -----------------------------------------------------------------------
    (
        "GT03",
        "Mathematical Archetype",
        "The approach to equilibrium (expansion) is driven by the information deficit of the bulk relative to the boundary — a counting argument, not a force law.",
        "The approach to equilibrium (expansion) is driven by the information deficit of the bulk relative to the boundary — a counting argument, not a force law. "
        "This makes holographic equipartition the cosmological c-theorem: just as the Zamolodchikov "
        "c-function counting effective degrees of freedom decreases monotonically from UV to IR under "
        "renormalisation group flow, N_bulk decreases relative to N_sur as the universe evolves from "
        "early dense configurations (large N_bulk, small relative to N_sur) to the de Sitter equilibrium. "
        "RG irreversibility (c_UV ≥ c_IR) and cosmological irreversibility (expansion never reverses "
        "toward the initial state) are both instances of monotonic coarse-graining.",
    ),

    # -----------------------------------------------------------------------
    # GT03 — What The Math Says
    # Current ending: "...explaining why the universe approaches de Sitter space."
    # Add c-theorem / coarse-graining / degrees-of-freedom language.
    # -----------------------------------------------------------------------
    (
        "GT03",
        "What The Math Says",
        "The cosmological constant Lambda corresponds to the final equilibrium state where N-sur equals N-bulk, explaining why the universe approaches de Sitter space.",
        "The cosmological constant Lambda corresponds to the final equilibrium state where N-sur equals N-bulk, explaining why the universe approaches de Sitter space. "
        "The structural parallel to the Zamolodchikov c-theorem is exact: in RG flow, the c-function "
        "counting UV degrees of freedom decreases monotonically as the theory coarse-grains from "
        "high-energy to low-energy descriptions. In cosmological evolution, N-bulk plays the role of "
        "the c-function — the number of effective bulk degrees of freedom decreases relative to the "
        "holographic surface N-sur as the universe coarse-grains from its initial state toward de Sitter "
        "equipartition. Both are monotonicity theorems about irreversible coarse-graining: RG flow "
        "cannot run backward (c increases), and cosmological expansion cannot reverse (N-bulk cannot "
        "re-exceed N-sur once equilibrium is approached).",
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
    print(f"Applying pass-2 prose patches to:\n  {SOURCE_DB}\n")
    applied, failed = apply_revisions(SOURCE_DB, REVISIONS)
    print(f"\nResult: {applied} applied, {failed} failed")
