# Session Handover — 2026-04-18 (GSW Anchor Architecture + 42% Wiki Provenance)

> **Read order for fresh sessions:**
> 1. `docs/RESEARCH_PLATFORM_CHARTER.md` — mission, epistemic contract, working modes
> 2. `CLAUDE.md` — updated project context (this session)
> 3. **This document** — GSW architecture + retagging + anchoring pass
> 4. `docs/GSW_ANCHOR_ARCHITECTURE.md` — schema and design decisions
> 5. `docs/GSW_SOURCE_BASKET.md` — per-domain canonical source list
> 6. `docs/SESSION_HANDOVER_2026-04-16.md` — prior session (M0 audit closeout)

---

## One-paragraph summary

On 2026-04-18, the project transitioned from **"wiki with in-prose citations"** to **"wiki as semantic overlay on the Greater Science World (GSW)"**. In one day we: (a) built the entire GSW anchor architecture with 3 new tables, 10-type relationship taxonomy, 5-role canonical-authority subdivision, and trigger-based durability model; (b) seeded a 57-tag hierarchical domain taxonomy with 16 cross-domain borrowings; (c) retagged all 300 wiki items with canonical domain tags; (d) completed all 9 M0 fold-in conjectures; (e) anchored 88 entries to external canonical sources via 307 anchor rows; (f) flagged 37 DFIG-framework entries as `internal_construction` (including the X8/AlphaEntropy side-project exclusion). The wiki now has GSW provenance recorded for **42% of its 300 items**. Every future entry has a concrete rubric, the restatement-catcher is active in live data, and 8 canonical textbooks serve as structural co-citation hubs.

---

## Major architectural additions (new since 2026-04-16 handover)

### 1. GSW Anchor Architecture

Three new tables in `wiki_history.db` (charter rule preserved — `ds_wiki.db` untouched):

- **`external_anchors`** — typed pointers from wiki entries to canonical external sources. Every anchor carries `source`, `identifier`, `tier` (1-4), `source_stability_class` (canonical / active-literature / preprint-evolving / data-ref-periodic), `relationship` (10 types), `canonical_role` (5 types, required when `relationship='canonical_authority'`), `confidence`, `notes`, `verified_date`, `verified_by_session`.
- **`internal_constructions`** — first-class label for entries with no GSW equivalent (project-internal or side-project content). Preserves the entry under the no-deletions rule but honestly labels it.
- **`pending_anchor_reviews`** — orphan-anchor review queue for candidates that don't fit any relationship type.

Design doc: [GSW_ANCHOR_ARCHITECTURE.md](GSW_ANCHOR_ARCHITECTURE.md). Schema migration: [`scripts/migrations/create_external_anchors_2026_04_17.py`](../scripts/migrations/create_external_anchors_2026_04_17.py). Canonical-role refinement migration: [`scripts/migrations/add_canonical_role_2026_04_17.py`](../scripts/migrations/add_canonical_role_2026_04_17.py).

### 2. Hierarchical Domain Taxonomy

Three new tables + seeded content:

- **`source_domain_taxonomy`** — 10 top-level domains + 42 level-1 sub-tags + 5 level-2 sub-sub-tags (57 total). Dot-path notation: `physics.modern.statistical_mechanics`.
- **`tag_cross_domain_borrowings`** — 16 seeded cross-domain bridges at the sub-tag level (e.g., `mathematics.geometry_topology.differential_geometry` borrowed by physics for GR; `information_theory.shannon` borrowed by physics for stat mech).
- **`entry_source_domains`** — per-entry multi-tag assignments with primacy (`primary` / `secondary` / `auxiliary`), `via_borrowing_id` linking, review metadata, supersession tracking.

Migration: [`scripts/migrations/create_domain_taxonomy_2026_04_17.py`](../scripts/migrations/create_domain_taxonomy_2026_04_17.py).

### 3. GSW Hierarchy Ordering

The 10 top-level domains are hierarchically ranked (foundation-first):

1. `formal_logic` (most foundational)
2. `mathematics`
3. `information_theory`
4. `statistics_probability`
5. `computer_science`
6. `physics`
7. `chemistry`
8. `biology`
9. `earth_sciences`
10. `networks_systems` (most emergent)

This ordering resolves directionality ambiguity in multi-domain entries — the "physics · mathematics" vs "mathematics · physics" duplicates from the legacy `domain` field were normalized by placing the more-foundational domain first in canonical form, with primary selection determined by the entry's ID prefix when deterministic.

### 4. Retagging Pass (100% complete)

All 300 items (277 entries + 23 conjectures) retagged from the legacy free-text `domain` field (44 distinct strings) to canonical tags. 545 `entry_source_domains` rows in total across primary/secondary/auxiliary.

Final primary-tag distribution:

| Top-level | Count | % |
|---|---|---|
| physics | 140 | 47% |
| biology | 28 | 9% |
| information_theory | 25 | 8% |
| formal_logic | 23 | 8% |
| chemistry | 20 | 7% |
| mathematics | 18 | 6% |
| computer_science | 16 | 5% |
| earth_sciences | 14 | 5% |
| networks_systems | 9 | 3% |
| statistics_probability | 7 | 2% |

Apply scripts:
- [`scripts/migrations/apply_domain_retag_clean_2026_04_17.py`](../scripts/migrations/apply_domain_retag_clean_2026_04_17.py) — first 217 entries
- [`scripts/migrations/apply_domain_retag_misc_2026_04_18.py`](../scripts/migrations/apply_domain_retag_misc_2026_04_18.py) — 60 misc entries + X8 exclusion
- [`scripts/migrations/apply_domain_retag_conjectures_2026_04_18.py`](../scripts/migrations/apply_domain_retag_conjectures_2026_04_18.py) — 23 P-series + internal_construction flags

### 5. Anchoring Pass (29% complete — 88 of 300 entries)

Delivered via 5 direct batches + 3 cluster mega-batches:

- **Batch 1 — INFO1 smoke test** (8 anchors): Shannon 1948 Pts I+II, Khinchin 1957, Cover & Thomas, Wikipedia, MathWorld, Scholarpedia, nLab
- **Batch 2 — CM1/GV1/AM5** (19 anchors): Newton Principia, MTW/Wald/Carroll, Einstein 1915/1916, Goldstein, Arnold, Kosmann-Schwarzbach (first `comprehensive_survey` anchor), Noether 1918 Tavel translation
- **Batch 3 — TD3/QM1/CS1** (21 anchors): Clausius 1865, Carathéodory 1909, Lieb-Yngvason 1999, Schrödinger 1926, von Neumann 1932, Sipser, Kleene, Church 1936 + Turing 1937 dual progenitor
- **Batch 4 — MATH1/FL1/CHEM1** (18 anchors): Bayes 1763, Jaynes *Probability Theory*, Gelman, Aristotle, Tarski 1956, Mendeleev (Jensen reprint), Pauling, Scerri
- **Batch 5 — C1/BIO1/ES1** (13 anchors): Kleiber 1932, WBE 1997, Schmidt-Nielsen, West *Scale*, Mendel (Bateson translation), Griffiths *Genetic Analysis*, Tobler 1970, Moran 1950
- **Batch 6 — C2/E1/STAT1** (11 anchors): Bettencourt 2007, Moore 1965/1998, Mack 2011 50-years-of-Moore's-Law, Jaynes 1957 Pts I+II — **closes 10/10 domain ring**
- **Batch 7 — P2/P11/P21 fold-ins** (8 anchors): first `reframing_of` relationships in live data — P2→WBE, P11→Bettencourt, P21 Established canonical_authority set
- **Batch 8 — P5/P8/P10 fold-ins** (7 anchors): debuts `null_hypothesis` relationship (P10) and dual `reframing_of` (P8)
- **Batch 9 — P1/P3/P4 fold-ins** (6 anchors): closes all 9 M0 fold-ins; all three use `null_hypothesis` for heterodox-without-unique-prediction claims
- **Megabatch A — FL + CS + internal_construction** (110 anchors + 31 IC flags): cluster-template pass using FL1 and CS1 as templates; 22 FL entries + 14 CS entries + 31 DFIG-framework internal_construction flags
- **Megabatch B — Classical physics cluster** (86 anchors): CM2-11 + AM1-4 + EM1-14, sharing Goldstein/Taylor/Jackson/Griffiths/Arnold

Anchor insertion scripts are all in `scripts/migrations/insert_*_2026_04_1[78].py` — eleven scripts total.

### 6. Internal Construction Flags (37 entries)

AlphaEntropy side-project exclusion + DFIG-framework operational vocabulary:
- **X8** — AlphaEntropy finance project (explicit owner exclusion 2026-04-18)
- **P18, P19, P20** — AlphaEntropy-derived single-domain observations (option-b tagging + flag)
- **P13, P15** — owner-acknowledged ansatz, preserved per falsification-learning rule
- **31 DFIG-framework constructs** — Ax1, Ax2, OmD, H1-H4, X0-X7, M1-M6, T1-T10

### 7. Prior-Art Gate + Documentation

- **[GSW_SOURCE_BASKET.md](GSW_SOURCE_BASKET.md)** — per-domain canonical-source basket audit. Covers 10 top-level domains × 5 canonical roles + reliability classification (Wikipedia ✓, Scholarpedia ⚠ flaky, MathWorld ✓, CrossRef ✓, Encyclopedia of Math ✗ blocked, Semantic Scholar ⚠ rate-limited, SEP ✓) + 21-value source enum.
- **`docs/prior_art_reviews/`** — 13 per-chunk proposal reports + 3 cluster proposal reports + INFO1 smoke-test report + domain retag amendments doc.

---

## Current state — 2026-04-18 end-of-session

### Totals

| Metric | Value |
|---|---|
| Entries with external anchors | **88 / 300** (29%) |
| Entries flagged `internal_construction` | **37 / 300** (12%) |
| **Total items with GSW provenance recorded** | **125 / 300 (42%)** |
| External anchor rows | **307** |
| Domain tags (primary + secondary + auxiliary) | **545** |
| Co-citation edges (shared-source entries) | **8+** |
| Relationship types in live use | **5** (canonical_authority, reframing_of, null_hypothesis, cites, adjacent_concept) |
| Canonical-role slots with ≥1 live anchor | **5/5** |
| Entries at 5/5 canonical slots | 3 (TD3, CHEM1, C1) |
| Domains with ≥1 anchor | **10/10** |

### Top co-citation hubs

| Textbook/source | Entries anchored |
|---|---|
| Enderton *Mathematical Intro to Logic* | 22 (all FL cluster) |
| van Dalen *Logic and Structure* | 22 (all FL cluster) |
| Goldstein *Classical Mechanics* | 16 (CM + AM) |
| Sipser *Theory of Computation* | 15 (all CS cluster) |
| Jackson *Classical Electrodynamics* | 14 (all EM) |
| Griffiths *Electrodynamics* | 14 (all EM) |
| Taylor *Classical Mechanics* | 11 (CM) |
| Scholarpedia "Entropy" | 2 (INFO1, TD3) |
| West *Scale* | 3 (C1, C2, P11) |
| WBE 1997 *Science* | 2 (C1 canonical + P2 reframing_of) |

### Domain coverage

| Domain | Tagged | Anchored | % |
|---|---|---|---|
| formal_logic | 23 | 22 | **96%** ✓ |
| computer_science | 16 | 13 | **81%** ✓ |
| networks_systems | 9 | 3 | 33% |
| physics | 140 | 37 | 26% |
| mathematics | 18 | 3 | 17% |
| statistics_probability | 7 | 1 | 14% |
| information_theory | 25 | 3 | 12% |
| chemistry | 20 | 2 | 10% |
| biology | 28 | 3 | 11% |
| earth_sciences | 14 | 1 | 7% |

### M0 conjecture fold-in: complete

All 9 fold-in conjectures closed:

| Conjecture | Relationship | Canonical target |
|---|---|---|
| P2 Metabolic / D_eff | `reframing_of` | WBE 1997 Science |
| P5 FIM Rank = D_eff | `reframing_of` | Machta et al. 2013 |
| P8 Critical exponents fractal-D | `reframing_of` | Gefen 1980 + JJK 2004 |
| P11 Urban scaling | `reframing_of` | Bettencourt 2007 |
| P1 Dimensional redshift | `null_hypothesis` | Hubble 1929 + Planck 2018 |
| P3 Ω_D single operator | `null_hypothesis` | Adelberger 2003 + Peskin-Schroeder |
| P4 CcO thermodynamic refresh | `null_hypothesis` | Lehninger Biochemistry |
| P10 Hadron radii / running ℏ | `null_hypothesis` | Pohl 2010 + Peskin-Schroeder |
| P21 Fisher-Rao universality | `canonical_authority` | Chentsov 1982 + Amari 1985 + Amari-Nagaoka 2000 |

### 14 conjectures remaining unanchored

P6, P7, P9, P12, P13, P14, P15, P16, P17, P18, P19, P20, P22, P23

- **P13, P15** — internal_construction flagged (owner ansatz); tagged, awaiting `contradicts` or additional `cites` anchors
- **P6, P7** — contradicted by own Phase 1 tests; should get `contradicts` anchors (would debut `contradicts` relationship type)
- **P17, P23** — Amendola/Cadoni citations verified in M0 but still need wording corrections in `ds_wiki.db.conjectures`
- **P9, P22** — reclassify-to-Q-series flagged but not yet migrated
- **P18, P19, P20** — AlphaEntropy-adjacent, internal_construction flagged; could optionally get anchors
- **P12, P14, P16** — archive bucket; untestable without data, may just need minimal anchors

---

## Memory preferences saved this session (global, not in repo)

- [`feedback_preserve_falsifications.md`](../../.claude/projects/-Users-iandarling-Projects-DS-Wiki-Transformation/memory/feedback_preserve_falsifications.md) — never delete wrong/falsified claims; label them and keep as learning artifacts
- [`feedback_diagnostic_labels.md`](../../.claude/projects/-Users-iandarling-Projects-DS-Wiki-Transformation/memory/feedback_diagnostic_labels.md) — specific labels required ("Falsified by Phase C q=10 Potts", "Restatement of WBE 1997"); 10-tag drift pattern catalog
- [`feedback_prior_art_gate.md`](../../.claude/projects/-Users-iandarling-Projects-DS-Wiki-Transformation/memory/feedback_prior_art_gate.md) — mandatory deep literature review before any new Q/P/Postulate; "yes and" scaffolding explicitly harmful
- [`feedback_age_is_not_decay.md`](../../.claude/projects/-Users-iandarling-Projects-DS-Wiki-Transformation/memory/feedback_age_is_not_decay.md) — old + uncontested = durability signal; trigger-based re-verification for canonical sources

---

## Open action items (prioritized)

### Immediate housekeeping

1. **`alpha_entropy_v22.py`** untracked in repo root — user flagged X8-adjacent 2026-04-18. Relocate to separate repo OR `.gitignore` here with note.
2. **Commit the session's work** — last push attempt failed because `data/wiki_history.db` exceeds GitHub's 100MB limit. Options discussed with user: (A) Git LFS, (B) gitignore + history rewrite + rebuild script, (C) keep local-only. Pending decision.
3. **Write `scripts/rebuild_wiki_history.sh`** — single-command reconstitution of `wiki_history.db` from migration scripts, for fresh clones. Especially needed if option (B) chosen.

### Next-session anchoring work (parallelizable via cluster templates)

**High-leverage clusters (do these first):**

4. **QM cluster** — QM1 anchored; QM2-5 + BR01-05 need cluster-batch using Sakurai/Griffiths/Shankar template. ~5-10 entries.
5. **Cosmology cluster** — GV1 anchored; GV2-4 + GT01-11 + HB01-10 need MTW/Wald/Carroll template + individual progenitor DOIs. ~20-25 entries, will produce more `comprehensive_survey` fills via Living Reviews in Relativity.
6. **Thermodynamics cluster** — TD3 anchored; TD1-2, TD4-14 + RG01-06 + NE01-06 need Callen/Reif template. ~25-30 entries.
7. **Biology cluster** — C1, BIO1, ES1 anchored; BIO2-9, D1, F1-5, NE02/05 need Alberts/Campbell template + specific refs. ~25 entries.
8. **Chemistry cluster** — CHEM1 anchored; CHEM2-4 + KC1-10 + CR1 + MS1 need Atkins/McQuarrie/Clayden template. ~15 entries.
9. **Math cluster** — MATH1 anchored; MATH2-8 + STAT2-3 + IT series need Rudin/Lang/Billingsley template. ~15 entries.
10. **Earth sciences cluster** — ES1 anchored; ES2-14 need Turcotte-Schubert + USGS + Wikipedia. ~13 entries.
11. **Remaining conjectures** — P6/P7 `contradicts`; P12/14/16 archive; P17/P23 cosmology archive; P22 reclassify; P9 reclassify. ~1-2 sessions.
12. **Remaining misc entries** — A1/A2, B1-4, C3, D2, E2, F1-5, G1/3, Q1-5, P_STATUS, remaining X-series. ~1-2 sessions.

### M0 open items (carryover from 2026-04-16)

13. **P17/P23 wording correction** in `ds_wiki.db` — verified Amendola "5σ" was forecast (not data); Cadoni "universal" (not "generic"). Needs explicit owner sign-off to alter source-of-truth DB.
14. **CCA terminology rename** — see [`docs/CCA_TERMINOLOGY_RENAME_PROPOSAL.md`](CCA_TERMINOLOGY_RENAME_PROPOSAL.md). Two collisions: CCA d_eff vs Mattingly 2018 d_eff; CCA η vs standard stat-mech η_critical.
15. **Read Vinayak 2014 EPL + Borgs-Chayes 1996** — two primary sources still on the CCA prior-art reading list.
16. **CCA Potts sweep q=2,5,7,10** — extended experiment to test vs Brown 2022 GTE.

### Infrastructure polish

17. **Scholarpedia retry wrapper** — 6/6 timeouts across sessions via WebFetch. Need 3-attempt exponential backoff protocol.
18. **Wikipedia oldid backfill sweep** — cluster batches used `revision_id=null` with confidence=medium for Wikipedia anchors. A batch re-fetch can upgrade all to high.
19. **Source enum formalization** — 21 values documented in basket audit §6. Could tighten to CHECK constraint on `external_anchors.source`.
20. **Rebuild script** — see item 3.

### Dead-conjecture surgery

21. **P9 + P22 → Q-series migration** — flagged as RECLASSIFY in M0 + retagging. Actual schema-level move from `conjectures` to open-question entries is a separate task.

---

## Cluster-template workflow — pattern for future sessions

The mega-batch approach proved efficient. Template:

1. Identify a cluster of 10-25 entries that share 2-3 canonical textbooks
2. Use an already-anchored exemplar as the template (FL1 for formal_logic, CS1 for CS, CM1/AM5 for classical mechanics, etc.)
3. Write a cluster-insertion script with:
   - Shared-textbook anchors (ISBN-verified, high confidence)
   - Wikipedia living_reference per entry (medium confidence pending oldid sweep)
   - Topic-specific progenitor DOIs where known (verify via CrossRef)
4. Minimum-viable = 3 anchors per entry (2 textbooks + Wikipedia)
5. Run inserts; duplicates caught by UNIQUE constraint
6. Accept that 5/5 slot coverage is NOT required for bulk-anchoring — 3/5 is sufficient for graph quality

**Confidence calibration discipline:** Wikipedia without revision_id = `medium`. Textbook by ISBN = `high`. Verified DOI via CrossRef = `high`. Scholarpedia = `medium` pending retry wrapper. Resist inflation.

**Relationship type discipline:** bulk clusters are nearly all `canonical_authority`. Reserve `reframing_of` for fold-in conjectures that are restatements. Reserve `null_hypothesis` for heterodox-without-unique-prediction claims. Reserve `contradicts` for own-test-falsified conjectures (not yet used). Reserve `specialization_of`, `generalization_of`, `cited_by`, `open_in_literature` for cases that arise organically.

---

## Key files for fresh sessions

### Always read first

| File | What it does |
|------|---|
| [`docs/RESEARCH_PLATFORM_CHARTER.md`](RESEARCH_PLATFORM_CHARTER.md) | Mission, epistemic contract, working modes |
| [`CLAUDE.md`](../CLAUDE.md) | Auto-loaded project context (updated 2026-04-18) |
| **This document** | GSW architecture + anchoring state |

### Design docs written this session

| File | What |
|---|---|
| [`docs/GSW_ANCHOR_ARCHITECTURE.md`](GSW_ANCHOR_ARCHITECTURE.md) | Schema, 10 relationships, 5 canonical roles, trigger-based durability, owner-approved decision log |
| [`docs/GSW_SOURCE_BASKET.md`](GSW_SOURCE_BASKET.md) | Per-domain canonical sources × 5 roles; reliability classification from INFO1 smoke test; 21-value source enum |
| [`docs/prior_art_reviews/`](prior_art_reviews/) | 13 per-chunk retag reports + INFO1 smoke test + cluster proposals |

### Migration scripts (all in `scripts/migrations/`)

**Schema:**
- `create_external_anchors_2026_04_17.py`
- `add_canonical_role_2026_04_17.py`
- `create_domain_taxonomy_2026_04_17.py`

**Retagging:**
- `apply_domain_retag_clean_2026_04_17.py` (217 entries)
- `apply_domain_retag_misc_2026_04_18.py` (60 entries + X8)
- `apply_domain_retag_conjectures_2026_04_18.py` (23 + IC flags)

**Anchor inserts:**
- `insert_info1_anchors_2026_04_18.py` (8)
- `insert_tier1_batch_2026_04_18.py` (CM1/GV1/AM5 — 19)
- `insert_tier1_batch2_2026_04_18.py` (TD3/QM1/CS1 — 21)
- `insert_tier1_batch3_2026_04_18.py` (MATH1/FL1/CHEM1 — 18)
- `insert_tier1_batch4_2026_04_18.py` (C1/BIO1/ES1 — 13)
- `insert_tier1_batch5_2026_04_18.py` (C2/E1/STAT1 — 11)
- `insert_foldin_batch1_2026_04_18.py` (P2/P11/P21 — 8)
- `insert_foldin_batch2_2026_04_18.py` (P5/P8/P10 — 7)
- `insert_foldin_batch3_2026_04_18.py` (P1/P3/P4 — 6)
- `insert_cluster_megabatch_2026_04_18.py` (FL + CS + internal_construction — 110 + 31)
- `insert_physics_classical_cluster_2026_04_18.py` (CM/AM/EM — 86)

### Useful queries

```python
# Per-entry anchor summary
import sqlite3
c = sqlite3.connect('data/wiki_history.db')
for r in c.execute("""
    SELECT source, canonical_role, confidence
    FROM external_anchors WHERE entry_id=? ORDER BY canonical_role
""", ('ENTRY_ID_HERE',)):
    print(r)

# Co-citation graph (sources shared across entries)
c.execute("""
    SELECT source, identifier, COUNT(DISTINCT entry_id) as n, MAX(title)
    FROM external_anchors
    GROUP BY source, identifier HAVING n > 1
    ORDER BY n DESC
""")

# Domain coverage
c.execute("ATTACH DATABASE 'data/ds_wiki.db' AS ds")
c.execute("""
    SELECT
        CASE WHEN INSTR(t.tag_path,'.')=0 THEN t.tag_path
             ELSE SUBSTR(t.tag_path,1,INSTR(t.tag_path,'.')-1) END AS top_level,
        COUNT(DISTINCT e.entry_id) as tagged,
        COUNT(DISTINCT a.entry_id) as anchored
    FROM entry_source_domains e
    JOIN source_domain_taxonomy t ON t.id = e.tag_id
    LEFT JOIN external_anchors a ON a.entry_id = e.entry_id
    WHERE e.primacy='primary' AND e.review_status='current'
    GROUP BY top_level ORDER BY tagged DESC
""")
```

---

## Honest meta-observations from this session

**1. The cluster-template approach buys 3-4× throughput.** First ~5 batches did 3 entries at a time (15 anchors per batch, ~2000 tokens of reasoning). The cluster mega-batches did 22-28 entries per batch (110-86 anchors). Same per-batch judgment work, 3-4× more anchors closed. **For remaining clusters, always template first.**

**2. Confidence calibration held under scale.** Wikipedia-without-oldid stayed `medium` across 50+ anchors. Textbooks stayed `high`. Scholarpedia stayed `medium` across repeated flakiness. The rubric is internalized.

**3. The restatement-catcher works.** 4 conjectures (P2/P5/P8/P11) now have `reframing_of` anchors pointing to pre-existing canonical sources in the graph. The pattern literally shows, via SQL JOIN, which conjectures are restatements of which papers. This is the architectural feature the whole system was designed to enable.

**4. Pre-DOI classical physics works via ISBN anchors.** Newton's Principia, Coulomb, Faraday, Ampère etc. don't have DOIs but anchor cleanly via textbook ISBNs (Cohen-Whitman Principia) or modern reprint DOIs. No source-identifier workaround needed.

**5. Context usage for the cluster work is bimodal.** Building the first template is expensive (~10-15% context for the FL+CS+IC megabatch). Once the template exists, applying it is cheap (~3-5% for the physics-classical mega-batch). **Future sessions should invest heavy in the first template per domain.**

**6. The source-basket audit was prescient.** The 21-value source enum predicted correctly which sources would appear in the anchor graph. Only one unexpected addition: `ads` for pre-DOI physics papers (Einstein 1915). The basket holds.

**7. `internal_construction` flag is a legitimate first-class state.** It's not "defect" or "ignore" — it's an HONEST label that isolates project-internal vocabulary from canonical-science content. 37 entries are now cleanly labeled as DFIG-framework operational terms that live in the wiki by construction and don't need GSW anchoring. The architecture supports this natively.

---

## Session numerical totals

- **Session length**: 1 day
- **Commits in GSW work (pending push)**: 1 local commit so far
- **Migration scripts written**: 13 (3 schema + 3 retag apply + 11 anchor insert)
- **Design docs**: 2 (`GSW_ANCHOR_ARCHITECTURE.md`, `GSW_SOURCE_BASKET.md`) + this handover
- **Prior-art review docs**: 14 (per-chunk + proposals + amendments)
- **Memory preferences saved**: 4 (preserve-falsifications, diagnostic-labels, prior-art-gate, age-is-not-decay)
- **Entries anchored this session**: 88 (from 0)
- **Anchor rows inserted**: 307 (from 0)
- **Internal_construction flags**: 37 (from 0)
- **Tests broken**: 0
- **`ds_wiki.db` schema changes**: 0 (charter rule preserved across all work)

A fresh Claude session reading the recommended doc order will reach the same state without needing to re-derive the architecture. The anchor graph is self-documenting via its notes fields.
