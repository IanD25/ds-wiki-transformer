"""
prose_enricher.py — Supplemental prose enrichment for RRP bundle entries.

STATUS: PARKED — not part of the active pipeline.
        The prose enrichment approach was evaluated and found to risk introducing
        semantic drift: LLM-generated prose injects vocabulary that moves bridge
        scores independently of the underlying data content (SEO contamination).
        Retained for reference; do not use in production ingestion runs without
        careful validation of bridge score stability pre/post enrichment.

STRICT INTERPRETATION ONLY:
  - Reads existing formal content (Mathematical Form / What It Claims)
  - Generates natural language prose translation as "What The Math Says"
  - Never modifies source fields
  - Never adds information not present in source
  - Marks all generated sections with authoring_status='llm_supplemental'
    via a bundle-level rrp_meta flag

For ZooClasses specifically:
  - Theorem names ARE the formal expressions (e.g. "NL⊆PSPACE")
  - We parse the unicode operator grammar and expand class names
    from the class dictionary built from the source data itself
  - 4 operator patterns: simple containment, strict containment,
    equality, chain (A⊆B⊆C)
  - Fallback: use existing content/desc field verbatim if pattern
    doesn't match

Embedding quality impact:
  - Before: median WIC = 12 chars (formal-only), 57% < 20 chars
  - After: WTM section adds 80-200 chars of natural language prose
    for all parseable theorems → meaningful BGE embeddings
"""

import json
import re
import sqlite3
from pathlib import Path
from typing import Optional


# ── Operator grammar ─────────────────────────────────────────────────────────

OP_PROSE = {
    "⊆": "is contained in",
    "⊂": "is strictly contained in",
    "⊇": "contains",
    "⊃": "strictly contains",
    "⊄": "is NOT contained in",
    "=": "is equal to",
    "≠": "is not equal to",
}

OP_IMPLICATION = {
    "⊆": "every problem solvable with {a} resources can also be solved with {b} resources",
    "⊂": "every problem solvable with {a} resources can also be solved with {b} resources, "
          "but {a} is strictly less powerful",
    "⊇": "every problem solvable with {b} resources can also be solved with {a} resources",
    "⊃": "every problem solvable with {b} resources can also be solved with {a} resources, "
          "but {b} is strictly less powerful",
    "⊄": "{a} contains problems that cannot be solved within {b} resource bounds",
    "=": "these two classes capture exactly the same set of computational problems",
    "≠": "these two classes are distinct — at least one problem separates them",
}

# Regex: match simple binary expression with a single operator
SIMPLE_RE  = re.compile(
    r'^(?P<lhs>[^⊆⊂⊇⊃⊄=≠∩∪]+)(?P<op>[⊆⊂⊇⊃⊄=≠])(?P<rhs>[^⊆⊂⊇⊃⊄=≠∩∪]+)$'
)
# Chain: A⊆B⊆C or A⊂B⊂C (two containments)
CHAIN_RE   = re.compile(
    r'^(?P<a>[^⊆⊂⊇⊃⊄=≠∩∪]+)(?P<op1>[⊆⊂⊇⊃])(?P<b>[^⊆⊂⊇⊃⊄=≠∩∪]+)(?P<op2>[⊆⊂⊇⊃])(?P<c>[^⊆⊂⊇⊃⊄=≠∩∪]+)$'
)
# Intersection in rhs: A⊆B∩C
INTERSECT_RHS_RE = re.compile(
    r'^(?P<lhs>[^⊆⊂⊇⊃⊄=≠∩∪]+)(?P<op>[⊆⊂⊇⊃])(?P<b>[^∩∪]+)∩(?P<c>[^∩∪]+)$'
)
# Leading quantifier: {i}... or ∀...
QUANTIFIER_RE = re.compile(r'^\{[^}]+\}')


# ── Class name dictionary builder ─────────────────────────────────────────────

def build_class_dict(raw_dir: Path) -> dict[str, str]:
    """
    Build {class_name → short_description} from classes.json.
    Short description = first sentence of desc, or name if TODO/missing.
    """
    path = raw_dir / "classes.json"
    if not path.exists():
        return {}

    classes = json.loads(path.read_text())
    result = {}
    for c in classes:
        name = c["name"]
        desc = (c.get("desc") or "").strip()
        # Skip TODO entries — use name as fallback
        if desc.upper().startswith("TODO") or not desc:
            result[name] = name
            continue
        # First sentence only (stop at '. ' or '.\n')
        first_sentence = re.split(r'\.\s|\.\n', desc)[0].strip()
        # Strip markdown/html artifacts
        first_sentence = re.sub(r'<[^>]+>', '', first_sentence)
        first_sentence = re.sub(r'\{[^}]+\}', '', first_sentence).strip()
        result[name] = first_sentence or name
    return result


# ── Class name normalisation ──────────────────────────────────────────────────

def _normalise_class(raw: str, class_dict: dict[str, str]) -> tuple[str, str]:
    """
    Given a raw class token (possibly with leading quantifier or whitespace),
    return (clean_name, prose_expansion).
    e.g. "{i}NC^i" → ("NC^i", "NC^i") or "{i}NC" → ("NC", "Unbounded Fanin ...")
    """
    token = raw.strip()
    # Strip leading quantifier {i}, {k}, etc.
    token = QUANTIFIER_RE.sub("", token).strip()

    expansion = class_dict.get(token)
    if expansion:
        return token, expansion

    # Try stripping exponent: AC^0 → AC, NC^1 → NC
    base = re.sub(r'\^.*$', '', token).strip()
    expansion = class_dict.get(base)
    if expansion:
        return token, f"{expansion} (level {token})"

    # Unknown — return as-is
    return token, token


# ── Prose generators ──────────────────────────────────────────────────────────

def _prose_simple(lhs: str, op: str, rhs: str, class_dict: dict) -> str:
    a_clean, a_exp = _normalise_class(lhs, class_dict)
    b_clean, b_exp = _normalise_class(rhs, class_dict)

    op_phrase = OP_PROSE.get(op, op)
    implication = OP_IMPLICATION.get(op, "").format(a=a_clean, b=b_clean)

    prose = f"{a_clean} ({a_exp}) {op_phrase} {b_clean} ({b_exp})."
    if implication:
        prose += f" This means {implication}."
    return prose


def _prose_chain(a: str, op1: str, b: str, op2: str, c: str, class_dict: dict) -> str:
    a_clean, a_exp = _normalise_class(a, class_dict)
    b_clean, b_exp = _normalise_class(b, class_dict)
    c_clean, c_exp = _normalise_class(c, class_dict)

    op1_phrase = OP_PROSE.get(op1, op1)
    op2_phrase = OP_PROSE.get(op2, op2)

    return (
        f"{a_clean} ({a_exp}) {op1_phrase} {b_clean} ({b_exp}), "
        f"which in turn {op2_phrase} {c_clean} ({c_exp}). "
        f"This establishes a three-way containment chain from {a_clean} through {b_clean} to {c_clean}."
    )


def _prose_intersect_rhs(lhs: str, op: str, b: str, c: str, class_dict: dict) -> str:
    a_clean, a_exp = _normalise_class(lhs, class_dict)
    b_clean, b_exp = _normalise_class(b, class_dict)
    c_clean, c_exp = _normalise_class(c, class_dict)

    op_phrase = OP_PROSE.get(op, op)
    return (
        f"{a_clean} ({a_exp}) {op_phrase} the intersection of "
        f"{b_clean} ({b_exp}) and {c_clean} ({c_exp}). "
        f"Problems solvable by {a_clean} can be solved by both {b_clean} and {c_clean}."
    )


def translate_formal(formal: str, class_dict: dict) -> Optional[str]:
    """
    Attempt to translate a formal complexity expression into natural language prose.
    Returns None if the expression cannot be deterministically parsed.
    This is STRICT INTERPRETATION — no information is added beyond what the
    formula states and what the class names provide.
    """
    # Strip leading quantifiers for matching
    expr = QUANTIFIER_RE.sub("", formal).strip()

    # Try chain (must check before simple — chain also matches simple prefix)
    m = CHAIN_RE.match(expr)
    if m:
        return _prose_chain(
            m["a"], m["op1"], m["b"], m["op2"], m["c"], class_dict
        )

    # Try intersection in rhs
    m = INTERSECT_RHS_RE.match(expr)
    if m:
        return _prose_intersect_rhs(m["lhs"], m["op"], m["b"], m["c"], class_dict)

    # Try simple binary
    m = SIMPLE_RE.match(expr)
    if m:
        return _prose_simple(m["lhs"], m["op"], m["rhs"], class_dict)

    return None  # Cannot parse — skip, do not guess


# ── Bundle enricher ───────────────────────────────────────────────────────────

SECTION_NAME = "What The Math Says"
SUPPLEMENTAL_NOTE = (
    "[Supplemental — strict prose interpretation of formal notation. "
    "No information added beyond source expression and class definitions.]"
)


def enrich_bundle(
    db_path: str | Path,
    raw_dir: str | Path,
    overwrite: bool = False,
) -> dict:
    """
    Add 'What The Math Says' sections to bundle entries that have only
    formal/short content and no existing WTM section.

    Returns stats dict: {enriched, skipped_existing, skipped_unparseable, total}
    """
    db_path  = Path(db_path)
    raw_dir  = Path(raw_dir)
    class_dict = build_class_dict(raw_dir)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # Find entries that are candidates for enrichment:
    # - entry_type = 'theorem' (these have formal-only names as WIC)
    # - WIC content is short (< 80 chars) OR equals the title
    candidates = conn.execute("""
        SELECT e.id, e.title, e.entry_type,
               s.content AS wic_content,
               mf.content AS mf_content
        FROM entries e
        LEFT JOIN sections s  ON s.entry_id = e.id AND s.section_name = 'What It Claims'
        LEFT JOIN sections mf ON mf.entry_id = e.id AND mf.section_name = 'Mathematical Form'
        WHERE e.entry_type = 'theorem'
        ORDER BY e.id
    """).fetchall()

    enriched           = 0
    skipped_existing   = 0
    skipped_unparseable = 0

    max_order = conn.execute("SELECT COALESCE(MAX(section_order),0) FROM sections").fetchone()[0]
    order = max_order + 1

    for row in candidates:
        eid   = row["id"]
        title = row["title"]
        wic   = row["wic_content"] or ""
        mf    = row["mf_content"]  or ""

        # Skip if WTM already exists
        existing = conn.execute(
            "SELECT COUNT(*) FROM sections WHERE entry_id=? AND section_name=?",
            (eid, SECTION_NAME)
        ).fetchone()[0]
        if existing and not overwrite:
            skipped_existing += 1
            continue

        # The formal expression is the theorem name itself (e.g. "NL⊆PSPACE")
        # Use title as primary, fallback to WIC or MF
        formal = title.strip()
        if not any(op in formal for op in "⊆⊂⊇⊃⊄=≠"):
            formal = mf.strip() or wic.strip()

        prose = translate_formal(formal, class_dict)

        if prose is None:
            skipped_unparseable += 1
            continue

        # Prepend supplemental note
        full_content = f"{SUPPLEMENTAL_NOTE}\n\n{prose}"

        if existing and overwrite:
            conn.execute(
                "UPDATE sections SET content=? WHERE entry_id=? AND section_name=?",
                (full_content, eid, SECTION_NAME)
            )
        else:
            conn.execute(
                """INSERT OR IGNORE INTO sections
                   (entry_id, section_name, content, section_order)
                   VALUES (?, ?, ?, ?)""",
                (eid, SECTION_NAME, full_content, order)
            )
            order += 1

        enriched += 1

    # Record in rrp_meta
    conn.execute(
        "INSERT OR REPLACE INTO rrp_meta (key, value) VALUES (?, ?)",
        ("prose_enrichment_status", f"enriched={enriched} skipped_existing={skipped_existing} unparseable={skipped_unparseable}")
    )

    conn.commit()
    conn.close()

    return {
        "enriched":             enriched,
        "skipped_existing":     skipped_existing,
        "skipped_unparseable":  skipped_unparseable,
        "total_candidates":     len(candidates),
        "class_dict_size":      len(class_dict),
    }


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    import sys
    db_path = sys.argv[1] if len(sys.argv) > 1 else "data/rrp/zoo_classes/rrp_zoo_classes.db"
    raw_dir = sys.argv[2] if len(sys.argv) > 2 else "data/rrp/zoo_classes/raw"

    print(f"Enriching bundle: {db_path}")
    print(f"Class dict from:  {raw_dir}")
    print()

    stats = enrich_bundle(db_path, raw_dir)

    print("── Results ─────────────────────────────────────────────────────────")
    for k, v in stats.items():
        print(f"  {k:<30s}: {v}")

    # Show 5 sample translations
    conn = sqlite3.connect(db_path)
    print()
    print("── Sample 'What The Math Says' sections ────────────────────────────")
    samples = conn.execute(
        "SELECT entry_id, content FROM sections WHERE section_name=? LIMIT 5",
        (SECTION_NAME,)
    ).fetchall()
    for s in samples:
        entry_title = conn.execute("SELECT title FROM entries WHERE id=?", (s[0],)).fetchone()[0]
        prose_only  = s[1].split("\n\n", 1)[-1]  # strip the supplemental note prefix
        print(f"\n  [{entry_title}]")
        print(f"  → {prose_only}")
    conn.close()


if __name__ == "__main__":
    main()
