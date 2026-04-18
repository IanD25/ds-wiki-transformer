"""
Domain Retagging — per-chunk proposal generator — 2026-04-17

Processes entries in a chunk (by ID prefix list) with THREE signals:
1. ID prefix hint (lower weight; piecemeal wiki history)
2. Existing domain string parse
3. Keyword scan in title + "What It Claims" section content

Produces a markdown report showing the proposed tagging per entry + rationale
so owner can eyeball the full chunk and push back on any. NO INSERTS — insert
script runs after owner approval.

Usage:
    python3 scripts/domain_retag_chunk.py --chunk physics
    python3 scripts/domain_retag_chunk.py --chunk bio_chem
    python3 scripts/domain_retag_chunk.py --chunk math_formal
    python3 scripts/domain_retag_chunk.py --chunk info_stat_cs
    python3 scripts/domain_retag_chunk.py --chunk earth_conj_misc
"""

from __future__ import annotations
import argparse
import re
import sqlite3
import time
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

DS_WIKI_DB = Path("data/ds_wiki.db")


HIERARCHY_RANK = {
    "formal_logic":           1,
    "mathematics":            2,
    "information_theory":     3,
    "statistics_probability": 4,
    "computer_science":       5,
    "physics":                6,
    "chemistry":              7,
    "biology":                8,
    "earth_sciences":         9,
    "networks_systems":      10,
}

# ID prefix hints (confirmed ambiguous — treat as hint not rule)
ID_PREFIX_HINT = {
    "BIO":  "biology",
    "CHEM": "chemistry",
    "MATH": "mathematics",
    "INFO": "information_theory",
    "IT":   "information_theory",
    "STAT": "statistics_probability",
    "CS":   "computer_science",
    "FL":   "formal_logic",
    "CR":   "chemistry",
    "MS":   "chemistry.materials",
    "KC":   "chemistry.physical",
    "NE":   None,  # AMBIGUOUS — NE01 is non-eq thermo not neuroscience
    "BR":   None,  # ambiguous
    "GV":   "physics.cosmology",
    "GT":   "physics.cosmology",
    "HB":   "physics.cosmology",
    "DM":   None,  # AMBIGUOUS — DM1 is Fick diffusion not dark matter
    "CM":   "physics.classical",
    "AM":   "physics.classical",
    "EM":   "physics.classical",
    "FM":   "physics.classical",
    "OP":   "physics.classical",
    "RD":   "physics.classical",
    "TD":   "physics.classical",
    "QM":   "physics.modern",
    "RG":   "physics.modern",
    "GL":   "physics.classical",
    "ES":   "earth_sciences",
    "P":    None,
    "Q":    None,
    "Ax":   None,
    "Om":   None,
    "M":    None,
    "B":    None,
    "A":    None,
    "C":    None,
    "D":    None,
    "E":    None,
    "F":    None,
    "G":    None,
    "H":    None,
    "T":    None,
    "X":    None,
}

# Keyword lexicons — lowercase match, whole-word where useful
KEYWORDS = {
    "physics.classical": [
        "newton", "lagrangian", "hamiltonian", "kepler", "hooke", "archimedes",
        "lorentz", "maxwell", "ampère", "ampere", "faraday", "coulomb",
        "thermodynamic", "thermodynamics", "carnot", "clausius", "boltzmann",
        "fluid", "navier", "stokes", "bernoulli", "snell", "fermat",
        "refraction", "diffraction", "optics", "euler", "radiative",
        "stefan", "wien", "planck's law", "heat conduction", "fourier's law",
    ],
    "physics.modern": [
        "schrödinger", "schrodinger", "heisenberg", "quantum", "pauli",
        "dirac", "uncertainty", "statistical mechanics", "stat mech",
        "ising", "potts", "phase transition", "renormalization",
        "ensemble", "partition function", "gibbs", "special relativity",
        "lorentz transform", "postulates of special", "onsager",
        # non-equilibrium stat mech (NE-prefix territory)
        "jarzynski", "crooks", "fluctuation theorem", "non-equilibrium",
        "fluctuation-dissipation", "dissipative structure", "prigogine",
        "stochastic thermodynamics", "non-equilibrium thermodynamic",
    ],
    "physics.cosmology": [
        "einstein field", "general relativity", "cosmolog", "hubble",
        "friedmann", "λcdm", "dark energy", "dark matter",
        "black hole", "horizon", "bekenstein", "hawking",
        "gravitational wave", "schwarzschild", "curvature of spacetime",
        "redshift", "inflation", "jacobson", "thermodynamic derivation of einstein",
    ],
    "mathematics": [
        "theorem", "calculus", "differential equation", "bayes",
        "probability measure", "linear algebra", "hilbert space",
        "topology", "manifold", "group theory", "abstract algebra",
        "set theory", "proof", "real analysis", "complex analysis",
    ],
    "mathematics.geometry_topology": [
        "differential geometry", "riemannian", "manifold", "topology",
        "algebraic topology", "homology", "fiber bundle", "curvature",
        "geodesic", "fractal dimension", "hausdorff",
    ],
    "formal_logic": [
        "deductive", "inference rule", "model theory", "proof theory",
        "gödel", "godel", "tarski", "first-order logic", "predicate",
        "axiom schema", "set-theoretic", "completeness theorem",
    ],
    "information_theory": [
        "shannon", "entropy", "information", "kullback-leibler",
        "kl divergence", "channel capacity", "source coding",
        "kolmogorov complexity", "mutual information", "von neumann entropy",
    ],
    "statistics_probability": [
        "bayes", "bayesian", "markov", "stochastic", "posterior", "prior",
        "likelihood", "inference", "maximum entropy", "maximum likelihood",
        "probability", "estimator", "variance",
    ],
    "computer_science": [
        "algorithm", "complexity", "turing", "np-complete", "halting",
        "distributed", "byzantine", "cap theorem", "sorting", "consensus",
        "programming", "amdahl", "master theorem",
    ],
    "biology": [
        "organism", "cell", "gene", "genome", "protein", "enzyme",
        "metabolic", "metabolism", "vascular", "mendel", "inherit",
        "natural selection", "evolution", "ecology", "species",
        "physiolog", "mitochondri", "neural",
    ],
    "biology.neuroscience": [
        "neural avalanche", "neuron", "neuroscience", "cortex", "brain",
        "synapse", "action potential", "spike train",
    ],
    "biology.molecular": [
        "dna", "rna", "genetic code", "gene expression", "mutation",
        "molecular biology", "protein folding",
        # NOTE: "translation" and "transcription" intentionally omitted —
        # both collide with physics usage ("translation symmetry",
        # "transcription of equations"). Require more specific phrases.
        "mrna transcription", "gene translation",
    ],
    "biology.evolution": [
        "natural selection", "fitness", "population genetics", "speciation",
        "phylogen",
    ],
    "biology.physiology": [
        "vascular", "metabolic", "bmr", "kleiber", "west-brown-enquist",
        "respiratory", "allometric",
    ],
    "chemistry": [
        "chemical", "reaction rate", "arrhenius", "periodic", "catalysis",
        "stoichiometr", "bragg", "crystal", "element",
    ],
    "chemistry.physical": [
        "kinetic", "rate constant", "chemical potential", "nernst",
        "le chatelier",
    ],
    "chemistry.materials": [
        "young's modulus", "elastic modulus", "tensile strength",
        "materials science", "crystal structure",
    ],
    "chemistry.biochemistry": [
        "cytochrome", "enzyme kinetic", "michaelis", "atp",
        "oxidative phosphorylation",
    ],
    "earth_sciences": [
        "tobler", "geography", "geologic", "climate", "hydrolog",
        "atmospher", "tectonic", "ocean", "planetary",
    ],
    "networks_systems": [
        "network", "graph", "complex system", "emergent", "self-organi",
        "scaling law", "fractal", "power law", "criticality",
    ],
}


CHUNK_PREFIXES = {
    "physics": ["CM", "AM", "EM", "QM", "TD", "GV", "GT", "HB", "RG", "RD",
                "FM", "OP", "DM", "GL", "NE", "BR"],   # include ambiguous NE/BR for review
    "bio_chem": ["BIO", "CHEM", "CR", "MS", "KC"],
    "math_formal": ["MATH", "FL"],
    "info_stat_cs": ["INFO", "IT", "STAT", "CS"],
    "earth_conj_misc": ["ES"],
    # legacy DS Wiki single-letter prefixes (A=theorem, B=law, C/D/E/F/G/H/T/X=
    # mixed categories, M=method) + axioms + postulates + open-question/status-
    # in-entries rows. These were the original type-group identifiers; each
    # span multiple domains and need content inspection.
    "misc_entries": ["A", "B", "C", "D", "E", "F", "G", "H", "M", "T", "X",
                     "Ax", "OmD", "P", "Q"],
}


CONJECTURES_CHUNK = "conjectures"  # separate — reads from conjectures table


@dataclass
class Proposal:
    entry_id: str
    title: str
    entry_type: str
    current_domain: str
    primary: str | None
    secondary: list[str] = field(default_factory=list)
    auxiliary: list[str] = field(default_factory=list)
    confidence: str = "high"
    signals: dict = field(default_factory=dict)
    flags: list[str] = field(default_factory=list)
    rationale: str = ""


def top_level_of(tag_path: str) -> str:
    return tag_path.split(".")[0]


def id_prefix(entry_id: str) -> str:
    m = re.match(r"^([A-Za-z]+)", entry_id)
    return m.group(1) if m else ""


def score_keywords(text: str, keywords: dict) -> dict[str, int]:
    """Keyword scoring with whole-word matching to reduce false hits.

    'translation' (bio keyword) must not match 'translation symmetry' (physics)
    just because both contain the substring 'translation'.
    """
    text_lc = text.lower()
    scores: dict[str, int] = {}
    for tag, kws in keywords.items():
        hits = 0
        for kw in kws:
            # Multi-word keyword -> substring match OK (phrase is specific enough)
            # Single-word keyword -> require word boundary
            if " " in kw or "-" in kw:
                if kw in text_lc:
                    hits += 1
            else:
                pattern = r"\b" + re.escape(kw) + r"\b"
                if re.search(pattern, text_lc):
                    hits += 1
        if hits > 0:
            scores[tag] = hits
    return scores


DOMAIN_STRING_TO_TAGS = {
    "physics":                               ["physics"],
    "biology":                               ["biology"],
    "information":                           ["information_theory"],
    "chemistry":                             ["chemistry"],
    "mathematics":                           ["mathematics"],
    "computer science":                      ["computer_science"],
    "networks":                              ["networks_systems"],
    "earth sciences":                        ["earth_sciences"],
    "geometry":                              ["mathematics.geometry_topology"],
    "cosmology":                             ["physics.cosmology"],
    "astronomy":                             ["physics.cosmology"],
    "formal logic · mathematics":            ["formal_logic", "mathematics"],
    "physics · information":                 ["physics", "information_theory"],
    "chemistry · physics":                   ["chemistry", "physics"],
    "physics · cosmology":                   ["physics.cosmology"],
    "physics · chemistry":                   ["physics", "chemistry"],
    "information · mathematics":             ["information_theory", "mathematics"],
    "computer science · mathematics":        ["computer_science", "mathematics"],
    "physics · mathematics":                 ["physics", "mathematics"],
    "mathematics · physics":                 ["mathematics", "physics"],
    "information · physics":                 ["information_theory", "physics"],
    "mathematics · information":             ["mathematics", "information_theory"],
    "physics · biology":                     ["physics", "biology"],
    "mathematics · computer science":        ["mathematics", "computer_science"],
    "geometry · physics":                    ["mathematics.geometry_topology", "physics"],
    "geometry · biology":                    ["mathematics.geometry_topology", "biology"],
    "geometry · networks":                   ["mathematics.geometry_topology", "networks_systems"],
    "chemistry · biology":                   ["chemistry", "biology"],
    "biology · information":                 ["biology", "information_theory"],
    "earth sciences · biology":              ["earth_sciences", "biology"],
    "earth sciences · networks":             ["earth_sciences", "networks_systems"],
    "physics · mathematics · information":   ["physics", "mathematics", "information_theory"],
    "information · mathematics · physics":   ["information_theory", "mathematics", "physics"],
    "physics · information · networks":      ["physics", "information_theory", "networks_systems"],
    "physics · information · mathematics":   ["physics", "information_theory", "mathematics"],
    "physics · chemistry · biology":         ["physics", "chemistry", "biology"],
    "physics · biology · networks":          ["physics", "biology", "networks_systems"],
    "biology · physics · networks · information": [
        "biology", "physics", "networks_systems", "information_theory"
    ],
    "biology · physics · information":       ["biology", "physics", "information_theory"],
    "geometry · biology · networks":         ["mathematics.geometry_topology", "biology", "networks_systems"],
    "biology, scaling laws":                 ["biology", "networks_systems"],
    "scaling laws, fractals, networks":      ["networks_systems", "mathematics.geometry_topology"],
    "information geometry, statistical physics, networks": [
        "information_theory", "physics.modern.statistical_mechanics", "networks_systems"
    ],
    "information geometry, finance, non-equilibrium thermodynamics": [
        "information_theory", "statistics_probability", "physics.modern.statistical_mechanics"
    ],
}


def sort_by_hierarchy(tags: list[str]) -> list[str]:
    return sorted(tags, key=lambda t: (HIERARCHY_RANK.get(top_level_of(t), 99), t))


def derive_proposal(
    entry_id: str, title: str, entry_type: str, current_domain: str,
    claim_text: str,
) -> Proposal:
    prop = Proposal(entry_id, title, entry_type, current_domain, primary=None)
    prefix = id_prefix(entry_id)
    prefix_hint = ID_PREFIX_HINT.get(prefix)

    # Signal 1: prefix hint
    prop.signals["prefix"] = prefix_hint

    # Signal 2: domain string parse
    string_tags = DOMAIN_STRING_TO_TAGS.get(current_domain, None)
    prop.signals["domain_string"] = string_tags
    if string_tags is None:
        prop.flags.append(f"unmapped-domain-string:{current_domain}")

    # Signal 3: keyword scan in title + claim
    text_for_keywords = (title or "") + " " + (claim_text or "")
    keyword_scores = score_keywords(text_for_keywords, KEYWORDS)
    prop.signals["keywords"] = keyword_scores

    # Identify the top keyword-supported domain(s), at any depth
    # Prefer deepest tag (sub-tags beat top-level) when tied on score
    if keyword_scores:
        top_kw_score = max(keyword_scores.values())
        top_kw_tags = [t for t, s in keyword_scores.items() if s == top_kw_score]
        # prefer deepest (sub-tags) among ties
        top_kw_tags.sort(key=lambda t: -t.count("."))
        top_kw_best = top_kw_tags[0]
    else:
        top_kw_best = None

    prop.signals["top_keyword_tag"] = top_kw_best

    # Combine: prefix hint + top_kw agree -> prefer deeper (sub-tag)
    candidates = []
    if prefix_hint:
        candidates.append(("prefix", prefix_hint))
    if top_kw_best:
        candidates.append(("keywords", top_kw_best))
    if string_tags:
        # first tag in string is the "author-declared primary"
        candidates.append(("domain_string", string_tags[0]))

    if not candidates:
        prop.primary = None
        prop.confidence = "low"
        prop.flags.append("no-signal")
        prop.rationale = "No usable signal from prefix, keywords, or domain string"
        return prop

    # Count agreement on top-level — iterate the candidates list (each signal
    # casts one vote, duplicates count separately)
    from collections import Counter
    top_level_counts = Counter(top_level_of(tag) for src, tag in candidates)
    majority_tl, majority_count = top_level_counts.most_common(1)[0]

    # Pick the deepest candidate within the majority top-level
    majority_cands = [tag for src, tag in candidates if top_level_of(tag) == majority_tl]
    majority_cands.sort(key=lambda t: -t.count("."))
    primary = majority_cands[0]
    prop.primary = primary

    # Confidence: all 3 signals agree on top-level -> high
    #             2 of 3 agree                      -> medium
    #             all 3 disagree on top-level       -> low
    agree_count = majority_count
    total_signals = len(candidates)
    if total_signals >= 2 and agree_count == total_signals:
        prop.confidence = "high"
    elif total_signals >= 2 and agree_count >= total_signals - 1:
        prop.confidence = "medium"
        disagreeing = [f"{src}={tag}" for src, tag in candidates
                       if top_level_of(tag) != majority_tl]
        prop.flags.append(f"partial-disagreement: {', '.join(disagreeing)}")
    else:
        prop.confidence = "low"
        prop.flags.append(f"all-signals-disagree: {[(s,t) for s,t in candidates]}")

    # Secondary + auxiliary from domain string (excl. primary top-level), hierarchy-sorted
    if string_tags:
        other = [t for t in string_tags if top_level_of(t) != top_level_of(primary)]
        other = sort_by_hierarchy(other)
        prop.secondary = other[:2]
        prop.auxiliary = other[2:]

    # Rationale
    lines = []
    lines.append(f"Primary = {primary} (via {majority_tl}, "
                 f"{agree_count}/{total_signals} signals agree)")
    if prefix_hint:
        lines.append(f"  prefix hint '{prefix}' -> {prefix_hint}")
    lines.append(f"  domain string -> {string_tags}")
    if top_kw_best:
        lines.append(f"  top keyword match -> {top_kw_best} "
                     f"(score={keyword_scores.get(top_kw_best, 0)})")
    prop.rationale = " | ".join(lines)

    return prop


def fetch_entries_with_claims(conn: sqlite3.Connection, prefixes: list[str]) -> list[dict]:
    """Fetch entries whose id prefix (leading alpha chars) is EXACTLY one of the
    given prefixes. Uses Python filter to avoid LIKE ambiguity (e.g. 'A%' would
    also match 'AM01', 'Ax1').
    """
    prefix_set = set(prefixes)
    rows = conn.execute(
        "SELECT id, title, entry_type, domain FROM entries ORDER BY id"
    ).fetchall()
    entries = []
    for r in rows:
        eid = r[0]
        if id_prefix(eid) not in prefix_set:
            continue
        claim_row = conn.execute(
            "SELECT content FROM sections WHERE entry_id=? AND section_name=? LIMIT 1",
            (eid, "What It Claims"),
        ).fetchone()
        claim = claim_row[0] if claim_row else ""
        entries.append({
            "id": eid, "title": r[1], "entry_type": r[2],
            "domain": r[3], "claim": claim,
        })
    return entries


def fetch_conjectures(conn: sqlite3.Connection) -> list[dict]:
    """Fetch P-series conjectures from the conjectures table (separate schema).

    Conjectures have a single `claim` column rather than sections. We use the
    claim text for keyword matching. Domain is not stored on conjectures;
    derive from claim keywords + P-series knowledge.
    """
    rows = conn.execute(
        "SELECT id, title, claim FROM conjectures "
        "ORDER BY CAST(SUBSTR(id,2) AS INTEGER)"
    ).fetchall()
    return [
        {
            "id": r[0],
            "title": r[1] or "",
            "entry_type": "conjecture",
            "domain": "",  # no domain stored on conjectures
            "claim": r[2] or "",
        }
        for r in rows
    ]


def render_report(chunk_name: str, proposals: list[Proposal], out_path: Path) -> None:
    confs = {"high": 0, "medium": 0, "low": 0}
    for p in proposals:
        confs[p.confidence] += 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        f.write(f"# Domain Retagging — Chunk `{chunk_name}` — Proposals\n\n")
        f.write(f"**Date:** {date.today().isoformat()}\n")
        f.write(f"**Entries in chunk:** {len(proposals)}\n")
        f.write(f"- high confidence: {confs['high']}\n")
        f.write(f"- medium confidence: {confs['medium']}\n")
        f.write(f"- low confidence: {confs['low']}\n\n")

        f.write("## How to review\n\n")
        f.write("1. Skim the HIGH-confidence table first; flag any rows that look wrong\n")
        f.write("2. Deep-dive the MEDIUM and LOW confidence sections\n")
        f.write("3. For each flagged entry: amend the proposed primary/secondary/auxiliary inline OR\n")
        f.write("   tell Claude which row to fix\n")
        f.write("4. Once reviewed, Claude inserts approved rows into "
                "`wiki_history.db.entry_source_domains`\n\n")

        f.write("## High-confidence — auto-apply candidates\n\n")
        f.write("| ID | Title | Type | Current `domain` | Primary | Secondary | Auxiliary |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for p in proposals:
            if p.confidence == "high":
                sec = ", ".join(p.secondary) if p.secondary else "—"
                aux = ", ".join(p.auxiliary) if p.auxiliary else "—"
                f.write(f"| `{p.entry_id}` | {(p.title or '')[:45]} | {p.entry_type} | "
                        f"{p.current_domain} | `{p.primary}` | {sec} | {aux} |\n")

        f.write("\n## Medium-confidence — owner review\n\n")
        for p in proposals:
            if p.confidence == "medium":
                f.write(f"### `{p.entry_id}` — {p.title}\n")
                f.write(f"- Type: {p.entry_type}\n")
                f.write(f"- Current `domain`: `{p.current_domain}`\n")
                f.write(f"- **Proposed primary:** `{p.primary}`\n")
                if p.secondary:
                    f.write(f"- Proposed secondary: {p.secondary}\n")
                if p.auxiliary:
                    f.write(f"- Proposed auxiliary: {p.auxiliary}\n")
                f.write(f"- Rationale: {p.rationale}\n")
                f.write(f"- Flags: {p.flags}\n\n")

        f.write("\n## Low-confidence — mandatory owner review\n\n")
        for p in proposals:
            if p.confidence == "low":
                f.write(f"### `{p.entry_id}` — {p.title}\n")
                f.write(f"- Type: {p.entry_type}\n")
                f.write(f"- Current `domain`: `{p.current_domain}`\n")
                f.write(f"- **Proposed primary:** `{p.primary}`\n")
                if p.secondary:
                    f.write(f"- Proposed secondary: {p.secondary}\n")
                if p.auxiliary:
                    f.write(f"- Proposed auxiliary: {p.auxiliary}\n")
                f.write(f"- Rationale: {p.rationale}\n")
                f.write(f"- Flags: {p.flags}\n")
                f.write(f"- Signals: {p.signals}\n\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--chunk", required=True,
        choices=list(CHUNK_PREFIXES.keys()) + [CONJECTURES_CHUNK],
    )
    args = ap.parse_args()

    conn = sqlite3.connect(DS_WIKI_DB)
    try:
        if args.chunk == CONJECTURES_CHUNK:
            entries = fetch_conjectures(conn)
        else:
            prefixes = CHUNK_PREFIXES[args.chunk]
            entries = fetch_entries_with_claims(conn, prefixes)
    finally:
        conn.close()

    if not entries:
        print(f"No entries matched prefixes {prefixes}")
        return

    t0 = time.time()
    proposals = [
        derive_proposal(e["id"], e["title"], e["entry_type"],
                        e["domain"], e["claim"])
        for e in entries
    ]
    elapsed = time.time() - t0

    out_path = Path(f"docs/prior_art_reviews/DOMAIN_RETAG_{args.chunk.upper()}.md")
    render_report(args.chunk, proposals, out_path)

    confs = {"high": 0, "medium": 0, "low": 0}
    for p in proposals:
        confs[p.confidence] += 1

    print(f"Chunk '{args.chunk}' complete.")
    print(f"  {len(proposals)} entries in {elapsed:.2f}s")
    print(f"  confidence — high: {confs['high']}, medium: {confs['medium']}, low: {confs['low']}")
    print(f"  report: {out_path}")


if __name__ == "__main__":
    main()
