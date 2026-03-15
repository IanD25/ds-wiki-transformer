# Contributing to Principia Formal Diagnostics (PFD)

Thank you for your interest in PFD! This document explains how to get set up and contribute.

## Quick Setup

```bash
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd ds-wiki-transformer
bash setup.sh                    # creates .venv, installs deps, verifies data
source .venv/bin/activate
python -m pytest tests/ -v       # 450 tests should pass
```

Or with pip (editable install):

```bash
git clone https://github.com/IanD25/ds-wiki-transformer.git
cd ds-wiki-transformer
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python -m pytest tests/ -v
```

## Project Structure

```
src/
├── config.py              # All paths, model config, thresholds
├── sync.py                # Rebuild ChromaDB from ds_wiki.db
├── embedder.py            # BGE embedding pipeline
├── analysis/              # Diagnostic tools
│   ├── fisher_diagnostics.py   # Core FIM math
│   ├── fisher_report.py        # Two-tier PFD report
│   ├── claim_extractor.py      # Phase 3A claim extraction
│   ├── result_validator.py     # Claim validation + channel resolution
│   └── structural_alignment.py # Signed polarity scoring
├── ingestion/             # RRP parsers
│   ├── parsers/           # One parser per format
│   └── cross_universe_query.py  # RRP → DS Wiki bridge detection
└── viz/                   # Visualization (D3.js, Plotly)
```

## How to Contribute

### Adding a new RRP parser

This is the most impactful contribution. See existing parsers in `src/ingestion/parsers/` for patterns.

1. Create `src/ingestion/parsers/your_parser.py`
2. Parse your dataset into the RRP schema (entries, links, sections, properties)
3. Use `create_rrp_bundle()` from `ingestion.rrp_bundle`
4. Run Pass 2 to build cross-universe bridges: `python scripts/run_entity_catalog_pass.py your_rrp.db data/chroma_db data/ds_wiki.db`
5. Run Fisher Suite: `python scripts/run_fisher_suite.py --mode report --rrp your_rrp.db --db data/ds_wiki.db`
6. Add tests in `tests/`

### Adding DS Wiki entries

DS Wiki entries go in `data/ds_wiki.db`. Use a migration script in `scripts/migrations/` with `INSERT OR IGNORE` for safe re-runs. Never alter the schema — only add data.

### Improving claim extraction

The claim extractor (`src/analysis/claim_extractor.py`) uses pattern-based extraction. Contributions welcome for:
- New polarity markers (domain-specific negative/positive indicators)
- Better SRO extraction patterns
- Domain-specific claim indicators

## Code Standards

- **Tests required** — every new module needs tests in `tests/`
- **INSERT OR IGNORE** — all database writes must be idempotent
- **No schema changes to ds_wiki.db** — it's read-only; new tables go in `wiki_history.db`
- **Probabilistic, not boolean** — never return VALID/INVALID; return confidence scores (0–1)
- **numpy only in ingestion** — no scipy dependency in the ingestion pipeline

## Running Tests

```bash
python -m pytest tests/ -v              # all tests
python -m pytest tests/test_claim_extractor.py -v   # specific module
python -m pytest tests/ -k "integration" -v         # integration only
```

## Key Documents

- [README.md](README.md) — public overview
- [CLAUDE.md](CLAUDE.md) — full technical context (auto-loaded by Claude Code)
- [MASTER_SUMMARY.md](MASTER_SUMMARY.md) — deep technical reference
- [docs/FISHER_PIPELINE_REDESIGN.md](docs/FISHER_PIPELINE_REDESIGN.md) — pipeline spec
- [docs/ARCHITECTURE_DECISIONS.md](docs/ARCHITECTURE_DECISIONS.md) — ADR log

## Architectural Constraints

These are hard rules — please don't propose changes that violate them:

1. **ds_wiki.db is read-only** (schema never altered)
2. **Mandatory human gate** at claim extraction (Layer 1)
3. **Probabilistic pipeline** (confidence 0–1, never binary verdicts)
4. **Transparency** — every output shows full reasoning
5. **formality_tier caps** — Tier 1 max 0.95, Tier 2 max 0.85, Tier 3 max 0.70

## License

MIT — see [LICENSE](LICENSE).
