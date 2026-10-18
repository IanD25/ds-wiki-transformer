# Personal Knowledge Base — Build Blueprint

> **Purpose.** This document is written to be handed to a fresh AI session as a prompt.
> It describes a working personal knowledge base with a semantic search layer and an
> epistemic audit layer, explains why each decision was made, and flags what went wrong
> so it does not get rebuilt the same way.
>
> Derived from a real system: ~280 entries (319 counting 41 glossary pages), 23 personal
> conjectures, 2,056 embedded chunks, 900 source anchors, and 55 calibrated items — 47
> scientific claims plus 8 process records. Built over six months.
>
> *Corrected 2026-10-18 (`gsw-consistency-pass-2026-10-18`): this line previously read
> "82 logged status changes". 82 was the raw row count of the calibration table, which
> holds several rows per item and mixes claims with process records; it was not a count of
> status changes.*

---

## Paste-ready prompt

> I want to build a personal knowledge base with two layers: a semantic search layer over
> my notes, and an epistemic audit layer that tracks how confident I am in each claim and
> why. The blueprint below describes a working system. Read it, ask me about the choices
> that need my input (domain, scale, what "an entry" means for my material), then build it
> incrementally. Do not build all of it at once. Start with the two-database split and the
> sync pipeline, get that working, then add the audit layer.
>
> Standing instruction while we work: your job is to break my ideas and hunt prior art
> before accepting them, not to draft and extend them. If something I propose is already
> well established elsewhere, say so before building it.

---

## 1. The core architectural decision: two databases

**One immutable source, one rebuildable derived layer.**

| | `source.db` | `history.db` |
|---|---|---|
| Contains | entries, sections, links, your own claims | embeddings, snapshots, anchors, calibration, tags |
| Schema changes | **never** | freely |
| Rebuilt from scratch | no, it *is* the truth | yes, by a sync script |
| In version control | yes | optional (see §7 on size) |

Everything derived goes in the second database. The source database is never
schema-altered, which means every experiment, index, or annotation layer you add later
cannot corrupt what you actually wrote.

This is the single most useful decision in the system. It lets you throw away and rebuild
the entire semantic layer without risk, and it makes "what did I actually claim" always
answerable from one file.

**Adaptation:** if your material is markdown files rather than a database, the same split
applies. Files are the source; a SQLite database holds everything derived.

---

## 2. Chunking: one chunk per section, not per document

Each entry is divided into named sections. Each section becomes one embedded chunk, with
a deterministic ID:

```
chunk_id = f"{entry_id}_{section_name_normalised}"
```

**Why sections rather than documents:** a document-level embedding averages away the thing
you are searching for. Sections are the natural semantic unit, they are already how you
think about the material, and a stable ID means you can detect *which part* of an entry
changed between snapshots.

**Why not sliding windows:** arbitrary overlapping windows produce chunk IDs that are not
stable across edits, which kills drift detection. Give up a little retrieval recall to keep
the change history meaningful.

Current scale: 319 entries producing 2,056 chunks. Roughly 6 sections per entry.

---

## 3. Embeddings and search

```
model:      BAAI/bge-large-en-v1.5   (1024-dim)  on GPU or Apple Silicon
fallback:   BAAI/bge-base-en-v1.5    (768-dim)   on CPU
store:      ChromaDB, single collection
rerank:     cross-encoder/ms-marco-MiniLM-L-12-v2, top-20 candidates
```

Device is auto-detected at import: CUDA via `nvidia-smi`, Apple Silicon via
`system_profiler`, otherwise CPU with the smaller model. This matters if you work across
machines. Note that switching models changes the dimension, so the index must be rebuilt.

**Two-stage retrieval.** Embedding search is fast and approximate; a cross-encoder reranker
over the top 20 candidates is slow and accurate. Use both. The bi-encoder finds the
neighbourhood, the cross-encoder orders it.

*Correction 2026-10-18 (`gsw-consistency-pass-2026-10-18`): in the system this describes,
the reranker is configured but only wired into cross-dataset bridge detection. The
knowledge base's own semantic search is single-stage bi-encoder retrieval. The advice
stands; the description of our system did not.*

---

## 4. The idea worth stealing: objective link tiers

Links between entries carry a confidence tier, and the tier is **derived from cosine
similarity**, not assigned by hand:

```
≥ 0.90   tier 1     definitionally certain
0.85–0.89 tier 1.5   strong semantic bond, not definitional
0.82–0.84 tier 2     plausible, needs review
```

This removes an entire class of self-deception. A hand-assigned confidence drifts toward
whatever you want to be true. A threshold on a measured quantity does not.

Keep the raw score alongside the tier so thresholds can be re-tuned without re-judging
anything.

---

## 5. Snapshots and drift

Every sync writes a snapshot row and one embedding row per chunk:

```
wiki_snapshots         snapshot_id, created_at, trigger, chunk_count, embed_model
chunk_embedding_history snapshot_id, chunk_id, entry_id, content_hash,
                        embedding BLOB, top5_neighbors, centroid_distance
```

Storing `content_hash` and `top5_neighbors` per chunk lets you ask questions no plain
vector store answers:

- which chunks changed meaning since last month, not just which changed text
- which chunks drifted in the embedding space without being edited, because their
  *neighbours* changed
- when did this idea first sit next to that one

`DRIFT_THRESHOLD = 0.05` cosine distance flags a chunk as meaningfully changed.

**Retention:** keep the last N snapshots and prune older ones, or this table dominates your
disk. Ours reached over 100 MB before culling and is now 29 MB with 3 snapshots retained.

---

## 6. The audit layer — the part that makes it a knowledge base rather than a search index

Four mechanisms. None is clever; all are structural, which is the point. They work whether
or not you are paying attention on a given day.

### 6.1 Source anchors

Every entry must point at a canonical external source, **or carry an explicit label saying
none exists.**

```sql
external_anchors(
  entry_id, source, identifier, revision_id, title,
  tier,                      -- 1 peer-reviewed … 4 domain reference
  source_stability_class,    -- canonical | active-literature | preprint | data-periodic
  relationship,              -- see below
  canonical_role,            -- progenitor | textbook | living_reference | survey | axiomatic
  confidence, verified_date, verified_by_session, notes
)
internal_constructions(entry_id, reason, searched_sources, scrutiny_level, ...)
```

An entry in neither table is an **orphan**, detectable by one JOIN. That is the whole
enforcement mechanism.

**The relationship vocabulary is where the value is.** Ours has ten types; the load-bearing
ones are:

- `canonical_authority` — the external source *is* the authoritative statement
- `reframing_of` — same content, your vocabulary. **The restatement catcher.**
- `null_hypothesis` — the external source is the standard your claim is tested against
- `contradicts` — you disagree, and must say why in `notes`
- `disambiguates_from` — same name, different object

*Correction 2026-10-18 (`gsw-consistency-pass-2026-10-18`): `disambiguates_from` is a
link type between entries (it connects glossary disambiguation pages), not one of the ten
anchor relationships. The ten are `canonical_authority`, `specialization_of`,
`generalization_of`, `reframing_of`, `adjacent_concept`, `cites`, `cited_by`,
`contradicts`, `null_hypothesis`, `open_in_literature`.*

`reframing_of` is the one that earns its keep. It lets you record "this idea of mine turned
out to be a restatement of a 1997 paper" without deleting the idea. The question and the
answer both survive.

### 6.2 Automated vague-term flagging

A lint pass over all prose, checking a curated list of load-bearing words for use without
binding to a specific definition. In our physics material one word was in use with five
unrelated meanings; the check found 611 high-priority cases across 122 entries.

Implementation is simple: a regex list, a check for whether the occurrence sits inside an
explicit definition markup, and a check for a nearby binding phrase. Output is a punch list.

**Treat it as a candidate surfacer, not a verdict.** Some flagged uses are fine.

The same check in a business setting catches "engagement", "quality" or "churn" meaning
three different things in one document.

### 6.3 Calibration records

```sql
confidence_calibration(
  entity_id, entity_type, confidence,     -- Established | Supported | Speculative | Falsified
  calibration_date, audit_ref, short_status, rationale
)
```

Append-only. Every promotion, downgrade, correction and retirement gets a dated row with
its reasoning. `audit_ref` groups rows by the pass that produced them, so you can ask "what
did that review change" as a single query.

Ours, counting each item once at its latest status (2026-10-18): **47 scientific claims —
29 Speculative, 8 Supported, 7 Established, 3 Falsified** — plus 8 process records
(terminology decisions, reading priorities) tracked separately. The distribution is the
interesting part. A knowledge base where everything is Established is a knowledge base
that is not being audited.

**Count items, not rows, and keep claims apart from process.** The raw table held 82 rows
across 11 audit passes, split 53 / 13 / 13 / 3 — and that is how we first quoted it. It
overstated Established: three of those were process items (a terminology rename, a
symbol-collision note, a framework diagnosis) and several were repeat rows for the same
entity. Give the table two read-only views — latest row per entity, scientific types only,
and process types only — and quote numbers from the claim view.

*Corrected 2026-10-18 (`gsw-consistency-pass-2026-10-18`); the earlier figures are kept
above as the record of the mistake.*

### 6.4 Falsified work is labelled and kept, never deleted

A standing rule, not a mechanism. Wrong work stays with the evidence that killed it.

Two reasons. A deleted mistake is one you get to repeat. And the *pattern* in how you get
things wrong is only visible if the failures are still there to count. Tag each resolution
with a specific cause ("falsified by X", "restatement of Y") rather than a generic
"resolved", or the pattern is destroyed.

---

## 7. Honest notes from the build

Things that went wrong. Worth knowing before you repeat them.

**The derived database gets big.** `history.db` exceeded GitHub's 100 MB file limit and
blocked a push. Decide early: retention policy, or gitignore plus a rebuild script.

**Same-column edits in migration scripts silently overwrite.** A script that computes two
edits to the same field from the same starting value, then applies both as separate
UPDATEs, keeps only the second. Caught by post-write verification, not by the script
logic. Every migration should: validate all edits in a dry run first, abort on duplicate
`(table, row, column)` targets, apply, then read back and compare against expected.

**Drift detection undercounts.** Our sync reported "0 changed chunks" after eight prose
edits. The embeddings were correct; the change accounting was wrong. If drift numbers
matter to you, test that path deliberately.

**AI-assisted entries accumulate specific error types.** In one audit of a single cluster
we found a citation to a paper that does not exist, two numerically impossible values, and
a number labelled as evidence for the thing it was derived from. All three had passed
earlier reviews. None needed external literature to catch, only reading entries against
each other.

Build the check for the first one early: **does this cited source actually exist.** It is
the cheapest high-value audit available and the failure mode AI produces most confidently.

---

## 8. Suggested build order

1. Two-database split, source schema, one entry by hand
2. Extractor: source → chunks with stable IDs
3. Embedder + ChromaDB + a sync script that rebuilds the whole index
4. Snapshots with content hashes; verify drift detection actually works
5. Search with cross-encoder reranking
6. **Stop and use it for a week.** Everything after this point is worthless if the base
   layer is not something you actually reach for.
7. Anchors and the orphan-detection JOIN
8. Calibration records
9. Vague-term lint
10. Scheduled audit pass whose only job is to attack the existing record

Items 7 to 10 are the difference between a search index and a knowledge base. Item 6 is
the difference between a knowledge base and an abandoned project.

---

## 9. What to decide before starting

Questions a fresh session should ask rather than assume:

- What is an "entry" in your material? A concept, a source, a project, a person?
- What are your section names? These become chunk boundaries and should be consistent.
- Do you have claims of your own that need confidence tracking, or is this reference
  material only? If the latter, skip the calibration layer entirely.
- Which words in your domain are load-bearing and ambiguous? This seeds the lint list.
- Single machine, or synced across several? Affects the model auto-detection choice.
- How much history do you want to keep? Affects retention policy and repository size.

---

## 10. The operating principle underneath all of it

The apparatus exists because **confidence is not evidence**, and AI output is confident by
default. Every mechanism above converts a good intention into something a script can check,
a table can count, and a later reader can audit.

Discipline that depends on remembering to be careful will fail. The parts of this system
that have caught real errors are the parts that run on a schedule and do not care how
certain anyone felt at the time.
