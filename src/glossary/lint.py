"""
Glossary lint — flag load-bearing words used in prose without binding.

For each entry section, scan for occurrences of any load-bearing word from
LOAD_BEARING_WORDS. For each occurrence, check whether either:
  (a) it is inside a [[g:slug]] glossary markup, OR
  (b) the section contains a binding pattern within reasonable proximity
      ("Here, X means ..." / "where X denotes ..." / "By X we mean ...")

Sections that fail both checks become punch-list items.

This is the operational form of the methodology rule "name the specific
mathematical object, every time" from the 2026-05-04 deep-research pass.

The word list is a curated seed of about twenty concepts where the project
has empirically demonstrated vocabulary-stacking risk. New words can be
added to LOAD_BEARING_WORDS as new conflations are caught.
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from glossary.render import parse_markup


# ---------------------------------------------------------------------------
# Seed list of load-bearing words.  Expand cautiously.  Each string is a
# regex pattern; word boundaries are added automatically.  The point is to
# catch the project-relevant senses of these words, not every conceivable
# physics word.  See data/reports/hypothesis_2026_05_04/TRIAGE_2026_05_04.md
# for the empirical motivation.
# ---------------------------------------------------------------------------
LOAD_BEARING_WORDS: list[str] = [
    # The 10 high-priority words with documented multi-sense conflations
    r"Fisher information",
    r"Fisher[-\s]Rao",
    r"effective dimension",
    r"d_eff|D_eff|d_\\text\\{eff\\}|D_\\text\\{eff\\}",
    r"relative entropy",
    r"anomalous dimension",
    r"\\beta(\\(\\)|)|η|eta",   # rough — flagged as soft (see SOFT_WORDS)
    r"information geometry",
    r"observer",
    r"emergent spacetime",
    r"emergent space[-\\s]?time",
    r"holography|holographic",
    r"entropy",
    r"quantum corrections?",
    # The 10 medium-priority words (ambiguity less established but watched)
    r"modular Hamiltonian",
    r"phase transition",
    r"criticality",
    r"monotonicity",
    r"coarse[-\s]graining",
    r"duality",
    r"symmetry",
    r"connection",
    r"fluctuation",
    r"participation ratio",
]

# Words we expect to be heavy enough that flagging EVERY occurrence is
# noise; only flag when used near "the" or as a noun phrase head.  These
# are heuristics, not hard rules — the lint is a candidate-surfacer.
SOFT_WORDS = {"observer", "entropy", "symmetry", "connection", "fluctuation"}

# Binding patterns: prose shapes that count as a definition or pin.
BINDING_PATTERNS = [
    r"[Hh]ere,?\s+[\"\*\`]?\\?[A-Za-z][A-Za-z0-9_]*[\"\*\`]?\s+(means|denotes|refers to)",
    r"[Bb]y\s+[\"\*\`]?\\?[A-Za-z][A-Za-z0-9_]*[\"\*\`]?\s+(we mean|we denote)",
    r"[Ll]et\s+[\"\*\`]?\\?[A-Za-z][A-Za-z0-9_]*[\"\*\`]?\s+(be|denote)",
    r"defined as",
    r"\\bgiven by\\b",
    r"is the [A-Za-z\\-]+ on",
]

BINDING_RE = re.compile("|".join(BINDING_PATTERNS))


@dataclass
class LintFinding:
    entry_id: str
    section_name: str
    word_pattern: str
    word_match: str
    context: str
    in_markup: bool
    near_binding: bool
    flag_severity: str  # "high" | "medium" | "soft"

    def is_problem(self) -> bool:
        return not (self.in_markup or self.near_binding)


def _word_re_list() -> list[tuple[str, re.Pattern]]:
    out = []
    for raw in LOAD_BEARING_WORDS:
        # Add word boundaries; case-insensitive.
        try:
            patt = re.compile(rf"\b(?:{raw})\b", re.IGNORECASE)
        except re.error:
            # If raw is already a regex with funny chars, fall back to non-boundary
            patt = re.compile(raw, re.IGNORECASE)
        out.append((raw, patt))
    return out


def audit_entry(
    entry_id: str,
    sections: list[tuple[str, str]],
) -> list[LintFinding]:
    """
    Audit one entry's sections.  Returns a list of LintFinding rows; only
    those with is_problem()==True are punch-list items.
    """
    word_res = _word_re_list()
    findings: list[LintFinding] = []
    for sec_name, content in sections:
        if not content:
            continue
        # Compute markup spans so we can test "is this match inside markup?"
        markup_spans = [(m["start"], m["end"]) for m in parse_markup(content)]
        # Compute binding-pattern presence (per section, anywhere)
        has_binding = bool(BINDING_RE.search(content))
        for raw, patt in word_res:
            for m in patt.finditer(content):
                in_mk = any(s <= m.start() < e for s, e in markup_spans)
                ctx_a = max(0, m.start() - 60)
                ctx_b = min(len(content), m.end() + 60)
                ctx = content[ctx_a:ctx_b].replace("\n", " ")
                low = raw.lower()
                if any(s in low for s in SOFT_WORDS):
                    severity = "soft"
                else:
                    severity = "high"
                findings.append(LintFinding(
                    entry_id=entry_id,
                    section_name=sec_name,
                    word_pattern=raw,
                    word_match=m.group(0),
                    context=ctx,
                    in_markup=in_mk,
                    near_binding=has_binding,
                    flag_severity=severity,
                ))
    return findings


def audit_wiki(
    ds_wiki_db: Path,
    *,
    skip_glossary: bool = True,
    skip_internal_construction: bool = True,
    wiki_history_db: Path | None = None,
) -> list[LintFinding]:
    """
    Audit the entire wiki. Returns the aggregated findings list.
    Glossary entries themselves are skipped by default (they ARE the
    definitions, so the lint rule doesn't apply to them).
    """
    conn = sqlite3.connect(f"file:{ds_wiki_db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    entries = conn.execute(
        "SELECT id, entry_type FROM entries"
    ).fetchall()
    sections_by_entry: dict[str, list[tuple[str, str]]] = {}
    for s in conn.execute("SELECT entry_id, section_name, content FROM sections "
                          "ORDER BY entry_id, section_order"):
        sections_by_entry.setdefault(s["entry_id"], []).append(
            (s["section_name"], s["content"])
        )
    conn.close()

    skip_ids: set[str] = set()
    if skip_internal_construction and wiki_history_db is not None:
        hc = sqlite3.connect(f"file:{wiki_history_db}?mode=ro", uri=True)
        for r in hc.execute("SELECT entry_id FROM internal_constructions"):
            skip_ids.add(r[0])
        hc.close()

    findings: list[LintFinding] = []
    for e in entries:
        if skip_glossary and e["entry_type"] in ("defined_term", "disambiguation_page"):
            continue
        if e["id"] in skip_ids:
            continue
        if e["id"] not in sections_by_entry:
            continue
        findings.extend(audit_entry(e["id"], sections_by_entry[e["id"]]))
    return findings


def report_markdown(findings: list[LintFinding]) -> str:
    """Punch-list markdown report. Only includes problem findings."""
    problems = [f for f in findings if f.is_problem()]
    by_entry: dict[str, list[LintFinding]] = {}
    for f in problems:
        by_entry.setdefault(f.entry_id, []).append(f)

    lines = [
        "# Glossary Lint — Punch List",
        "",
        f"- Total findings scanned: {len(findings)}",
        f"- Problems flagged: {len(problems)}",
        f"- Entries needing attention: {len(by_entry)}",
        "",
        "Each finding is a load-bearing word that appears in prose without "
        "either `[[g:slug]]` markup OR a 'Here, X means ...'-style binding "
        "in the same section. The lint is a candidate-surfacer, not a "
        "verdict — some flagged usages are fine (well-known phrases in "
        "context). Triage manually.",
        "",
        "---",
        "",
    ]
    # Sort entries by number of problems desc, then entry_id
    sorted_entries = sorted(
        by_entry.items(), key=lambda x: (-len(x[1]), x[0])
    )
    for entry_id, items in sorted_entries:
        lines += [
            f"## {entry_id}  ({len(items)} flag{'s' if len(items) != 1 else ''})",
            "",
        ]
        # Group by section
        by_section: dict[str, list[LintFinding]] = {}
        for f in items:
            by_section.setdefault(f.section_name, []).append(f)
        for sec, secfs in by_section.items():
            lines.append(f"**Section: {sec}**")
            lines.append("")
            for f in secfs:
                badge = {"high": "⚠️", "medium": "•", "soft": "·"}[f.flag_severity]
                lines.append(f"- {badge} `{f.word_match}` — {f.context!r}")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)
