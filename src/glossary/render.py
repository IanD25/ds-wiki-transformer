"""
Glossary markup parser + renderers.

Markup convention:
    [[g:slug]]              → resolves to glossary entry "gloss_<slug>"
    [[g:slug|display]]      → custom display text in prose
    [[g:slug#section]]      → reference a particular section of the term
                              (rarely needed; supported for forward-compat)

The slug is the suffix of the entry ID. Glossary entries have IDs of the
form "gloss_<slug>" in ds_wiki.db.entries.

Renderers
---------
- render_markdown_footnotes:  produces markdown with [^slug] footnotes and
                              definitions appended at the end. Best for
                              static reports.
- render_inline_llm:          replaces markup with self-contained inline
                              expansions like  "Fisher information
                              (classical, on a probability-distribution
                              parameter manifold; formula g_ij = E[..]; see
                              IT05/IT08)". Best for LLM context windows
                              where every term is resolved at the use site.
- render_plain:               strips markup, leaves only the display text
                              (or title from glossary). For when you don't
                              want any inline expansion.

Persistence
-----------
- populate_term_uses(): scans the entire wiki and rebuilds the term_uses
                        cache table in wiki_history.db. Idempotent.
"""

from __future__ import annotations

import re
import sqlite3
from datetime import date
from pathlib import Path
from typing import Iterable

# Pattern: [[g:slug]] or [[g:slug|display]] or [[g:slug#section]]
# The slug allows alnum + underscore. No spaces.
MARKUP_RE = re.compile(
    r"\[\[g:(?P<slug>[A-Za-z0-9_]+)(?:#(?P<section>[A-Za-z0-9_-]+))?(?:\|(?P<display>[^\]]+))?\]\]"
)


# --------------------------------------------------------------------- parsing


def parse_markup(text: str) -> list[dict]:
    """
    Extract all [[g:...]] references from prose.

    Returns a list of dicts:
        {slug: str, section: str|None, display: str|None,
         start: int, end: int, raw: str}
    """
    out = []
    for m in MARKUP_RE.finditer(text or ""):
        out.append({
            "slug": m.group("slug"),
            "section": m.group("section"),
            "display": m.group("display"),
            "start": m.start(),
            "end": m.end(),
            "raw": m.group(0),
        })
    return out


# ------------------------------------------------------------- glossary lookup


def fetch_glossary_entry(
    slug: str,
    ds_wiki_db: Path,
) -> dict | None:
    """
    Fetch the glossary entry by slug from ds_wiki.db.
    Returns dict with id, title, entry_type, and {section_name: content} or None.
    """
    full_id = f"gloss_{slug}"
    conn = sqlite3.connect(f"file:{ds_wiki_db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    e = conn.execute(
        "SELECT id, title, entry_type FROM entries WHERE id = ?", (full_id,)
    ).fetchone()
    if e is None:
        conn.close()
        return None
    secs = conn.execute(
        "SELECT section_name, content FROM sections WHERE entry_id = ? "
        "ORDER BY section_order",
        (full_id,),
    ).fetchall()
    conn.close()
    return {
        "id": e["id"],
        "title": e["title"],
        "entry_type": e["entry_type"],
        "sections": {s["section_name"]: s["content"] for s in secs},
    }


# ----------------------------------------------------------------- renderers


def render_markdown_footnotes(
    text: str,
    ds_wiki_db: Path,
    *,
    max_footnotes: int = 30,
) -> str:
    """
    Replace [[g:slug]] with `*display*[^gloss_slug]` and append a footnotes
    block with definitions resolved from glossary entries.
    """
    refs = parse_markup(text)
    if not refs:
        return text

    used: dict[str, dict] = {}
    out_chunks: list[str] = []
    cursor = 0
    for r in refs:
        out_chunks.append(text[cursor:r["start"]])
        ge = fetch_glossary_entry(r["slug"], ds_wiki_db)
        display = r["display"] or (ge["title"] if ge else r["slug"])
        out_chunks.append(f"*{display}*[^gloss_{r['slug']}]")
        cursor = r["end"]
        if ge and r["slug"] not in used:
            used[r["slug"]] = ge

    out_chunks.append(text[cursor:])
    body = "".join(out_chunks)

    if not used:
        return body
    footnotes = ["", "", "---", "", "**Glossary terms used in this section:**", ""]
    for slug, ge in list(used.items())[:max_footnotes]:
        defn = ge["sections"].get("Definition", "").strip()
        formula = ge["sections"].get("Mathematical Form", "").strip()
        regime = ge["sections"].get("Regime", "").strip()
        line = f"[^gloss_{slug}]: **{ge['title']}**."
        if defn:
            line += f" {defn}"
        if formula:
            line += f" Formula: `{formula.splitlines()[0]}`"
        if regime:
            line += f" Regime: {regime}"
        footnotes.append(line)
    return body + "\n" + "\n".join(footnotes)


def render_inline_llm(
    text: str,
    ds_wiki_db: Path,
) -> str:
    """
    Replace [[g:slug]] with a self-contained inline expansion that an LLM
    reading the resulting text sees the resolved definition at the use
    site. Compact form: "display ⟨gloss_slug: short defn⟩"
    """
    refs = parse_markup(text)
    if not refs:
        return text

    out_chunks: list[str] = []
    cursor = 0
    for r in refs:
        out_chunks.append(text[cursor:r["start"]])
        ge = fetch_glossary_entry(r["slug"], ds_wiki_db)
        display = r["display"] or (ge["title"] if ge else r["slug"])
        if ge:
            defn = ge["sections"].get("Definition", "").strip()
            short = defn.split(".")[0] if defn else ""
            inline = f"{display} ⟨gloss_{r['slug']}: {short}⟩" if short else f"{display} ⟨gloss_{r['slug']}⟩"
        else:
            inline = f"{display} ⟨MISSING_GLOSSARY:gloss_{r['slug']}⟩"
        out_chunks.append(inline)
        cursor = r["end"]
    out_chunks.append(text[cursor:])
    return "".join(out_chunks)


def render_plain(text: str, ds_wiki_db: Path) -> str:
    """
    Strip markup; replace each [[g:slug|display]] with display, or with the
    glossary title if no display given.
    """
    refs = parse_markup(text)
    if not refs:
        return text
    out_chunks: list[str] = []
    cursor = 0
    for r in refs:
        out_chunks.append(text[cursor:r["start"]])
        if r["display"]:
            out_chunks.append(r["display"])
        else:
            ge = fetch_glossary_entry(r["slug"], ds_wiki_db)
            out_chunks.append(ge["title"] if ge else r["slug"])
        cursor = r["end"]
    out_chunks.append(text[cursor:])
    return "".join(out_chunks)


# --------------------------------------------------------- persistence cache


def populate_term_uses(
    ds_wiki_db: Path,
    wiki_history_db: Path,
    session: str = "manual",
) -> dict:
    """
    Scan all entries and sections for [[g:...]] markup; rebuild term_uses
    table in wiki_history.db. Idempotent (deletes prior rows for non-glossary
    sources before re-inserting; preserves rows for glossary entries themselves).
    """
    today = date.today().isoformat()

    src_conn = sqlite3.connect(f"file:{ds_wiki_db}?mode=ro", uri=True)
    src_conn.row_factory = sqlite3.Row
    rows = src_conn.execute(
        "SELECT entry_id, section_name, content FROM sections"
    ).fetchall()
    src_conn.close()

    found = []
    for r in rows:
        refs = parse_markup(r["content"] or "")
        for i, ref in enumerate(refs):
            ctx_start = max(0, ref["start"] - 60)
            ctx_end = min(len(r["content"] or ""), ref["end"] + 60)
            context = (r["content"] or "")[ctx_start:ctx_end].replace("\n", " ")
            found.append({
                "entry_id": r["entry_id"],
                "section_name": r["section_name"],
                "term_slug": ref["slug"],
                "occurrence_index": i,
                "surrounding_context": context,
            })

    hist_conn = sqlite3.connect(wiki_history_db)
    hist_cur = hist_conn.cursor()
    hist_cur.execute("DELETE FROM term_uses")
    for f in found:
        hist_cur.execute("""
            INSERT OR IGNORE INTO term_uses
              (entry_id, section_name, term_slug, occurrence_index,
               surrounding_context, populated_date, populated_by_session)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (f["entry_id"], f["section_name"], f["term_slug"],
              f["occurrence_index"], f["surrounding_context"], today, session))
    hist_conn.commit()
    hist_conn.close()

    return {
        "scanned_sections": len(rows),
        "term_references_found": len(found),
        "unique_terms": len({f["term_slug"] for f in found}),
        "entries_using_terms": len({f["entry_id"] for f in found}),
    }
