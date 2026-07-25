"""
Glossary subsystem — defined-term registry for the DS Wiki.

Provides:
  - Markup parsing for [[g:slug]] inline references
  - Renderers (markdown footnote, inline LLM context, plain text)
  - Lint pass that flags load-bearing words used without binding

See docs/RESEARCH_PLATFORM_CHARTER.md and the 2026-05-04 deep-research
pass for the motivation.
"""

from glossary.render import (
    parse_markup,
    render_markdown_footnotes,
    render_inline_llm,
    populate_term_uses,
)
from glossary.lint import (
    LOAD_BEARING_WORDS,
    audit_entry,
    audit_wiki,
)

__all__ = [
    "parse_markup",
    "render_markdown_footnotes",
    "render_inline_llm",
    "populate_term_uses",
    "LOAD_BEARING_WORDS",
    "audit_entry",
    "audit_wiki",
]
