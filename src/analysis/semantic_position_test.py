"""
semantic_position_test.py — Semantic Position Test (SPT)

STATUS: PROTOTYPE / ASPIRATIONAL — not part of the active pipeline.
        The core SPT concept (comparing bridge scores across neutral/supportive/critical
        RRP variants) has a known limitation: LLM framing changes vocabulary, and the
        BGE embedding measures topic proximity not argument sign. The α score captures
        "formal vocabulary density" rather than "logical alignment". Parked pending a
        structural alternative (link-type weighted bridge scoring). Do not integrate
        into reports without revisiting the SEO contamination problem.

Calibrated Semantic Stress Testing.

The LLM skew belongs at INTAKE, not post-processing.
When an LLM parses raw data into RRP entries, the intake prompt determines
how facts are framed. By running intake three ways (neutral / supportive /
critical) on the same raw source, we produce three structurally identical
RRP databases whose prose framing differs in a known, directional way.

SPT is the COMPARISON TOOL. It takes those 3 pre-built databases and computes
where each entry's raw framing sits between the two poles.

Architecture:
  Raw source data
        │
   ┌────┼────────────┐
   ▼    ▼            ▼
  [N]  [S]          [C]
  Neutral  Supportive  Critical
  intake   intake      intake
  prompt   prompt      prompt
        │
  rrp_neutral.db  rrp_supportive.db  rrp_critical.db
        │
  Pass 2 (bridges) run on each
        │
  α = (sim_N - sim_C) / (sim_S - sim_C)  per entry
        │
  α ≈ 1.0  → neutral framing is near its most supportive form
  α ≈ 0.0  → neutral framing is near its most critical form
  α ≈ 0.5  → genuinely ambiguous / contested

Intake prompt variants (versioned — embed in your parser's system prompt):
  SPT_SYSTEM_NEUTRAL    — balanced, factual prose (default)
  SPT_SYSTEM_SUPPORTIVE — emphasise alignment with formal foundations
  SPT_SYSTEM_CRITICAL   — emphasise tensions with formal foundations

For the OPERA prototype, three variant JSON files serve as the three inputs,
with framing bias baked into the section prose by hand. Same pipeline, same
parser, same Pass 2 — only the content framing differs.
"""

import json
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ── Intake system prompt variants (embed in your LLM parser prompt) ──────────

SPT_PROMPT_VERSION = "v1.1"

SPT_SYSTEM_NEUTRAL = """You are a scientific knowledge engineer writing formal RRP entries.
Write balanced, factual prose that accurately describes the scientific content.
Use precise technical vocabulary. State what is established, what is claimed,
and what is contested — without editorial bias in either direction.
Output valid JSON matching the required entry schema."""

SPT_SYSTEM_SUPPORTIVE = """You are a scientific knowledge engineer writing formal RRP entries.
Write prose that emphasises how each concept, measurement, or claim aligns with,
extends from, and is grounded in established formal scientific principles.
Where relevant, name the specific laws, theorems, or mathematical foundations
that support or contextualise the content. Do not fabricate facts.
Output valid JSON matching the required entry schema."""

SPT_SYSTEM_CRITICAL = """You are a scientific knowledge engineer writing formal RRP entries.
Write prose that emphasises tensions, evidential gaps, potential inconsistencies,
or contradictions between the content and established formal scientific principles.
Where relevant, name the specific laws, theorems, or constraints that the content
engages with or sits in tension with. Do not fabricate facts.
Output valid JSON matching the required entry schema."""


# ── Data structures ───────────────────────────────────────────────────────────

@dataclass
class EntryBridgeScore:
    entry_id: str
    title: str
    entry_type: str
    sim_neutral: float
    sim_supportive: float
    sim_critical: float
    top_wiki_neutral: str = ""
    top_wiki_supportive: str = ""
    top_wiki_critical: str = ""

    @property
    def delta(self) -> float:
        """Full dynamic range between S and C poles."""
        return self.sim_supportive - self.sim_critical

    @property
    def alpha(self) -> Optional[float]:
        """Position of neutral framing between C (0.0) and S (1.0) poles.
        Returns None if dynamic range is too small to be meaningful (< 0.002)."""
        if self.delta < 0.002:
            return None
        return (self.sim_neutral - self.sim_critical) / self.delta

    @property
    def interpretation(self) -> str:
        a = self.alpha
        if a is None:
            return "FLAT (no dynamic range)"
        if a >= 0.75:
            return "ALIGNED    (neutral near supportive pole)"
        if a >= 0.40:
            return "AMBIGUOUS  (between poles)"
        return "CONTESTED  (neutral near critical pole)"


@dataclass
class SPTResult:
    db_neutral: str
    db_supportive: str
    db_critical: str
    prompt_version: str = SPT_PROMPT_VERSION
    entries: list[EntryBridgeScore] = field(default_factory=list)

    @property
    def contested_entries(self) -> list[EntryBridgeScore]:
        return [e for e in self.entries if e.alpha is not None and e.alpha < 0.40]

    @property
    def aligned_entries(self) -> list[EntryBridgeScore]:
        return [e for e in self.entries if e.alpha is not None and e.alpha >= 0.75]

    @property
    def mean_alpha(self) -> float:
        alphas = [e.alpha for e in self.entries if e.alpha is not None]
        return sum(alphas) / len(alphas) if alphas else 0.5


# ── Bridge extraction ─────────────────────────────────────────────────────────

def _run_bridges(db_path: Path, chroma_dir: Path, label: str) -> dict[str, tuple[float, str]]:
    """
    Run CrossUniverseQuery on a database.
    Returns {entry_id: (best_similarity, top_wiki_entry_id)}.
    Clears existing bridges before running so results are fresh.
    """
    from ingestion.cross_universe_query import CrossUniverseQuery

    conn = sqlite3.connect(db_path)
    conn.execute("DELETE FROM cross_universe_bridges")
    conn.commit()
    conn.close()

    print(f"  [{label}] Running bridge analysis...", flush=True)
    cq = CrossUniverseQuery(bundle_db=db_path, chroma_dir=chroma_dir)
    cq.run()

    conn = sqlite3.connect(db_path)
    rows = conn.execute(
        """SELECT rrp_entry_id, MAX(similarity) as best_sim, ds_entry_id
           FROM cross_universe_bridges
           GROUP BY rrp_entry_id"""
    ).fetchall()
    conn.close()

    return {row[0]: (float(row[1]), row[2]) for row in rows}


# ── SPT Core ──────────────────────────────────────────────────────────────────

def run_spt(
    db_neutral: str | Path,
    db_supportive: str | Path,
    db_critical: str | Path,
    chroma_dir: str | Path = "data/chroma_db",
) -> SPTResult:
    """
    Run SPT comparison across three pre-built RRP variant databases.

    All three databases must have the same entry IDs and link structure.
    Only section prose content should differ between them.

    Args:
        db_neutral:    RRP built with neutral intake prompt (the baseline)
        db_supportive: RRP built with supportive intake prompt
        db_critical:   RRP built with critical intake prompt
        chroma_dir:    Path to ChromaDB index

    Returns:
        SPTResult with α scores per entry
    """
    db_neutral = Path(db_neutral)
    db_supportive = Path(db_supportive)
    db_critical = Path(db_critical)
    chroma_dir = Path(chroma_dir)

    print(f"\n{'='*60}")
    print(f"SEMANTIC POSITION TEST  [{SPT_PROMPT_VERSION}]")
    print(f"N: {db_neutral.name}")
    print(f"S: {db_supportive.name}")
    print(f"C: {db_critical.name}")
    print(f"{'='*60}\n")

    # Run bridges on all three
    bridges_n = _run_bridges(db_neutral,    chroma_dir, "NEUTRAL   ")
    bridges_s = _run_bridges(db_supportive, chroma_dir, "SUPPORTIVE")
    bridges_c = _run_bridges(db_critical,   chroma_dir, "CRITICAL  ")

    # Load entry metadata from neutral DB
    conn = sqlite3.connect(db_neutral)
    entries_meta = conn.execute(
        "SELECT id, title, entry_type FROM entries ORDER BY id"
    ).fetchall()
    conn.close()

    result = SPTResult(
        db_neutral=str(db_neutral),
        db_supportive=str(db_supportive),
        db_critical=str(db_critical),
    )

    for entry_id, title, entry_type in entries_meta:
        sim_n, wiki_n = bridges_n.get(entry_id, (0.0, ""))
        sim_s, wiki_s = bridges_s.get(entry_id, (0.0, ""))
        sim_c, wiki_c = bridges_c.get(entry_id, (0.0, ""))

        result.entries.append(EntryBridgeScore(
            entry_id=entry_id,
            title=title[:60],
            entry_type=entry_type,
            sim_neutral=sim_n,
            sim_supportive=sim_s,
            sim_critical=sim_c,
            top_wiki_neutral=wiki_n,
            top_wiki_supportive=wiki_s,
            top_wiki_critical=wiki_c,
        ))

    # Sort: contested first
    result.entries.sort(key=lambda e: (e.alpha is None, e.alpha or 0.5))
    return result


# ── Reporting ─────────────────────────────────────────────────────────────────

def print_spt_report(result: SPTResult) -> None:
    print(f"\n{'='*72}")
    print(f"SPT RESULTS  |  prompt {result.prompt_version}  |  mean α = {result.mean_alpha:.3f}")
    print(f"{'='*72}")
    print(f"{'Entry ID':<34} {'α':>6}  {'Δ':>6}  {'N':>6}  {'S':>6}  {'C':>6}  Status")
    print(f"{'─'*72}")

    for e in result.entries:
        alpha_str = f"{e.alpha:.3f}" if e.alpha is not None else "  N/A"
        print(
            f"{e.entry_id:<34} {alpha_str:>6}  {e.delta:>6.4f}  "
            f"{e.sim_neutral:>6.4f}  {e.sim_supportive:>6.4f}  {e.sim_critical:>6.4f}  "
            f"{e.interpretation}"
        )

    print(f"\n{'─'*72}")
    print(f"CONTESTED  (α < 0.40) : {len(result.contested_entries)}")
    print(f"AMBIGUOUS  (0.40–0.74): {len([e for e in result.entries if e.alpha is not None and 0.40 <= e.alpha < 0.75])}")
    print(f"ALIGNED    (α ≥ 0.75) : {len(result.aligned_entries)}")
    print(f"FLAT (no Δ)           : {len([e for e in result.entries if e.alpha is None])}")

    if result.contested_entries:
        print(f"\nCONTESTED ENTRIES:")
        for e in result.contested_entries:
            print(f"  {e.entry_id}  α={e.alpha:.3f}  Δ={e.delta:.4f}")
            print(f"    N bridges → {e.top_wiki_neutral} ({e.sim_neutral:.4f})")
            print(f"    S bridges → {e.top_wiki_supportive} ({e.sim_supportive:.4f})")
            print(f"    C bridges → {e.top_wiki_critical} ({e.sim_critical:.4f})")

    print(f"\n{'─'*72}")
    print("α = (sim_N - sim_C) / (sim_S - sim_C)")
    print("α≥0.75 ALIGNED | 0.40–0.74 AMBIGUOUS | α<0.40 CONTESTED")
    print(f"{'='*72}\n")


def save_spt_json(result: SPTResult, output_path: str | Path) -> None:
    output_path = Path(output_path)
    data = {
        "prompt_version": result.prompt_version,
        "db_neutral": result.db_neutral,
        "db_supportive": result.db_supportive,
        "db_critical": result.db_critical,
        "mean_alpha": result.mean_alpha,
        "n_entries": len(result.entries),
        "n_contested": len(result.contested_entries),
        "n_aligned": len(result.aligned_entries),
        "entries": [
            {
                "entry_id": e.entry_id,
                "title": e.title,
                "entry_type": e.entry_type,
                "alpha": e.alpha,
                "delta": e.delta,
                "sim_neutral": e.sim_neutral,
                "sim_supportive": e.sim_supportive,
                "sim_critical": e.sim_critical,
                "top_wiki_neutral": e.top_wiki_neutral,
                "top_wiki_supportive": e.top_wiki_supportive,
                "top_wiki_critical": e.top_wiki_critical,
                "interpretation": e.interpretation,
            }
            for e in result.entries
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"SPT result saved: {output_path}")
