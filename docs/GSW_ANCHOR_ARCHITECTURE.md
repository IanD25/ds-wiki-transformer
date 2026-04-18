# GSW Anchor Architecture

**Status:** DESIGN — drafted 2026-04-17, not yet implemented
**Anchor docs:** `RESEARCH_PLATFORM_CHARTER.md` (mission), `feedback_prior_art_gate.md` (memory — standing rule)
**Owner approval needed on:** relationship taxonomy (§4), tiering (§5), staleness policy (§7)

---

## 1. Purpose

This wiki's value-add is **not** reproducing content that exists in Wikipedia, Scholarpedia, arXiv, SEP, nLab, etc. Those sources are authoritative and we cannot beat them at their own game. Our value-add is the **semantic relationship layer**: cross-domain links, property/archetype matching, FIM structural alignment, embedding-space bridges — things no external wiki does.

The GSW anchor architecture re-orients the wiki accordingly. Every entry becomes a **semantic hub node** anchored outward to the canonical external source(s) — the Greater Science World (GSW). Our content is the relationships; GSW's content is the content.

**This is the operational expression of the charter's Rule 1 (novelty skepticism default) and Rule 2 (triviality check).** An entry that cannot be anchored to GSW is either a genuine project-internal construction (worth scrutiny) or a restatement of something we haven't found yet (worth more scrutiny).

---

## 2. Relationship to charter

- **Charter rule: never schema-alter `ds_wiki.db`.** The anchor table goes in `wiki_history.db`. `ds_wiki.db` entries table is untouched.
- **Charter rule: no silent promotion, confidence-tag everything.** Every anchor carries a relationship type, a tier, and a notes field making the mapping explicit.
- **Charter rule: falsification first / literature check before novelty claims.** The prior-art gate (see `memory/feedback_prior_art_gate.md`) produces anchor rows as its native output. Anchor creation IS the gate closing.

---

## 3. Schema

New table in `wiki_history.db`:

```sql
CREATE TABLE external_anchors (
    id INTEGER PRIMARY KEY,
    entry_id TEXT NOT NULL,           -- FK to ds_wiki.db entries.id (not enforced; cross-db)
    source TEXT NOT NULL,             -- lowercase source key; see §5 tier table
    identifier TEXT NOT NULL,         -- URL, DOI, arXiv ID, or source-native handle
    revision_id TEXT,                 -- for versioned sources (Wikipedia oldid, arXiv vN)
    title TEXT,                       -- human-readable title of the external resource
    tier INTEGER NOT NULL,            -- 1 = peer-reviewed canonical / 2 = living encyclopedia / 3 = preprint / 4 = domain reference
    source_stability_class TEXT NOT NULL,
        -- 'canonical' | 'active-literature' | 'preprint-evolving' | 'data-ref-periodic'
        -- determines durability model (see §7); age alone never flags an anchor
    relationship TEXT NOT NULL,       -- one of §4 taxonomy values
    canonical_role TEXT,
        -- one of: 'progenitor' | 'axiomatic_foundation' | 'standard_textbook' |
        -- 'living_reference' | 'comprehensive_survey' (see §4.2)
        -- REQUIRED when relationship='canonical_authority', NULL otherwise
        -- (enforced by CHECK constraint at the table level)
    verified_date DATE NOT NULL,      -- YYYY-MM-DD the anchor was last verified (historical record; not a decay clock for canonical sources)
    verified_by_session TEXT,         -- session handover ID or commit SHA for audit trail
    confidence TEXT NOT NULL,         -- 'high' | 'medium' | 'low' — how sure is the mapping
    notes TEXT,                       -- specific pointer, e.g. "our α=3/4 corresponds to eq. 5 in WBE 1997"
    UNIQUE(entry_id, source, identifier, relationship)
);

CREATE INDEX idx_external_anchors_entry ON external_anchors(entry_id);
CREATE INDEX idx_external_anchors_source ON external_anchors(source);
CREATE INDEX idx_external_anchors_relationship ON external_anchors(relationship);
CREATE INDEX idx_external_anchors_verified ON external_anchors(verified_date);
```

**Companion table for tracking the "internal construction" label:**

```sql
CREATE TABLE internal_constructions (
    id INTEGER PRIMARY KEY,
    entry_id TEXT NOT NULL UNIQUE,    -- FK to ds_wiki.db entries.id
    reason TEXT NOT NULL,             -- why no GSW anchor exists
    searched_sources TEXT NOT NULL,   -- JSON array of sources that were checked
    flagged_date DATE NOT NULL,
    flagged_by_session TEXT,
    scrutiny_level TEXT NOT NULL,     -- 'owner-aware' | 'needs-review' | 'high-novelty-risk'
    notes TEXT
);
```

Any entry in `ds_wiki.db.entries` should be reachable by:
- one or more rows in `external_anchors`, OR
- exactly one row in `internal_constructions`

Entries not in either table are **orphans** and constitute a defect detectable by a single JOIN.

---

## 4. Relationship taxonomy — **owner review required**

These are the load-bearing vocabulary. They define what the wiki claims about each anchor. Propose 10 types:

| Relationship | Meaning | Example |
|---|---|---|
| `canonical_authority` | External source IS the authoritative statement of this concept. Our entry defers to it. | P21 Fisher-Rao universality → Chentsov 1982 |
| `specialization_of` | Our entry is a special case / instance of the external concept | BIO3 Kleiber's law → Wikipedia: Allometric scaling |
| `generalization_of` | Our entry generalizes the external concept | (rare; flag for scrutiny) |
| `reframing_of` | Same content, different vocabulary — the **restatement-catcher** | P2 → WBE 1997 |
| `adjacent_concept` | Related but not the same thing | P8 critical exponents → Wikipedia: Universality (critical phenomena) |
| `cites` | Our entry explicitly cites the external source as evidence | P17 → Amendola et al. 2024 |
| `cited_by` | External source cites an antecedent our entry also builds on | (rare; for provenance only) |
| `contradicts` | Our entry honestly disagrees with the external source | (use sparingly; must come with evidence) |
| `null_hypothesis` | External is the standard/null our entry is tested against | P1 → ΛCDM |
| `open_in_literature` | External explicitly frames this as an open question | Q-series entries |

**Design decisions embedded in this list (locked 2026-04-17):**
- Q1 — `reframing_of` not split; use `notes` field to distinguish exact vs equivalent
- Q2 — `inspired_by` rejected; an entry either cites or doesn't
- Q3 — **Taxonomy frozen at 10 types.** Anchor candidates that do not map cleanly to any of the 10 become **orphan anchors** (see §4.1) — flagged for literature review before filing. New relationship types are only added after an orphan-anchor review shows a genuine recurring pattern the 10 don't cover.
- `reframing_of` is the key relationship — it lets us fold "this was a restatement" without deleting the entry. The question-and-answer history is preserved; the answer is the linked paper.
- `canonical_authority` is stronger than `cites`. Most conjectures should be `cites`; a reference_law that just repackages a textbook result should be `reframing_of` its source.
- `generalization_of` triggers scrutiny — claiming to generalize a textbook result is a novelty claim and hits the prior-art gate.

## 4.1 Orphan anchors — review queue

When the prior-art gate surfaces a candidate external source but no relationship in §4 fits cleanly, the anchor does NOT get filed in `external_anchors`. Instead it enters a review queue:

```sql
CREATE TABLE pending_anchor_reviews (
    id INTEGER PRIMARY KEY,
    entry_id TEXT NOT NULL,
    proposed_source TEXT NOT NULL,
    proposed_identifier TEXT NOT NULL,
    proposed_title TEXT,
    reason_orphan TEXT NOT NULL,       -- why no relationship type applied
    gate_report_path TEXT,             -- pointer to docs/prior_art_reviews/ report
    flagged_date DATE NOT NULL,
    flagged_by_session TEXT,
    status TEXT NOT NULL DEFAULT 'pending_lit_review',
        -- 'pending_lit_review' | 'resolved_to_existing_relationship' | 'new_relationship_proposed' | 'discarded_not_valid'
    resolution_notes TEXT,
    resolved_date DATE
);
```

**Resolution paths:**
1. Deeper literature review reveals the relationship actually is one of the 10 → resolve and file in `external_anchors`
2. The orphan reveals a genuine gap in the taxonomy → owner approves new relationship type, amend §4, re-file
3. The candidate anchor turns out not to be valid prior art → discard with rationale

**Invariant:** taxonomy changes (adding new relationship types) require at least 2 independent orphan cases before being accepted. No one-off additions — that's how taxonomies bloat.

## 4.2 Canonical roles — decomposing "which is THE authority?"

Rich concepts (Shannon entropy, General Relativity, Maxwell's equations) have **multiple legitimately canonical sources** playing different roles. Treating them all as undifferentiated `canonical_authority` anchors loses information and gives the prior-art gate no principled way to pick a base entry.

The `canonical_role` field (added 2026-04-17) subdivides canonical authority into five slots. It is **required when `relationship = 'canonical_authority'` and forbidden otherwise** (enforced by CHECK constraint).

| Role | Meaning | Example for Shannon entropy |
|---|---|---|
| `progenitor` | First publication establishing the concept. The origin. | Shannon 1948 Pt I + Pt II |
| `axiomatic_foundation` | Formal axiomatic characterization defining the essence | Khinchin 1957 *Mathematical Foundations of Information Theory* |
| `standard_textbook` | Field-standard graduate treatment everyone cites today | Cover & Thomas 2006 *Elements of Information Theory* |
| `living_reference` | Encyclopedia / encyclopedic reference article | Wikipedia + MathWorld + Scholarpedia (all three) |
| `comprehensive_survey` | Well-cited synthesis / review paper | (often unfilled in mature fields) |

### Rubric

Each entry has **5 canonicity slots**. The prior-art gate's job is to fill each slot explicitly (or declare it empty):

- **0 candidates in a slot** → note it as a gap. Informative, not a defect. Common for: concepts too young for textbook status; pre-axiomatic concepts; concepts where the progenitor is unclear (ancient, folkloric).
- **1 candidate in a slot** → anchor it with the `canonical_role` set.
- **Multiple strong candidates in a slot** → anchor all (e.g., Wikipedia + MathWorld + Scholarpedia all live in `living_reference` for Shannon entropy; MTW + Wald + Carroll all live in `standard_textbook` for GR). The `notes` field distinguishes why each is there.

### What this solves

- **"Which is THE base entry?" decomposes into 5 smaller, better-scoped questions.** Each has a clearer answer.
- **Forced ranking between equally-canonical sources is avoided.** No arbitrary choice between MTW and Wald; both are `standard_textbook` for GR.
- **Empty slots surface gaps in a useful way.** A concept with no `progenitor` or no `axiomatic_foundation` carries different epistemic weight than a concept with all five filled.
- **The basket audit becomes 2-D:** `{domain} × {canonical_role} → {candidate GSW sources}`. This surfaces missing sources that a flat list would hide.

### When canonical_role is NULL

For all `relationship` values OTHER than `canonical_authority` — `adjacent_concept`, `cites`, `reframing_of`, `contradicts`, etc. — `canonical_role` must be NULL. Those relationships don't have a canonicity slot; their role is captured by the relationship itself.

### Invariant

Every entry that has any `canonical_authority` anchor should fill **at least one** canonical role. Entries with `canonical_authority` anchors but ZERO filled roles are defective and will be rejected by the CHECK constraint.

An entry is NOT required to fill all 5 roles. For mature canonical concepts, typically 3-4 are filled; for young concepts, fewer; for owner-constructed internal concepts, zero (and those should be flagged `internal_construction`, not anchored to `canonical_authority`).

---

## 5. Source tiering — **owner review required**

Tiers rank GSW sources by authority. Anchors should prefer the highest-tier source available.

| Tier | Examples | Authority basis | Revisability |
|---|---|---|---|
| **1 — peer-reviewed canonical** | Published paper (with DOI), Scholarpedia article, Encyclopedia of Mathematics (Springer), SEP | Expert-reviewed, stable | Rarely |
| **2 — living encyclopedia** | Wikipedia, MathWorld, nLab | Community-curated, may be high-quality but can drift | Continuously (pin with `revision_id`) |
| **3 — preprint / author-version** | arXiv preprint, bioRxiv, author website | Not peer-reviewed; may be revised | Versioned (pin with `arXiv:1234.56789v3`) |
| **4 — domain reference** | PDG, NIST constants, IAU definitions, ICD-11 | Authoritative for specific data types | Periodic updates |

**Tier 1 is preferred for `canonical_authority`.** If only Tier 2 is available, anchor Tier 2 but note that a Tier 1 source is sought. If no Tier 1-4 source exists, the entry is `internal_construction`.

**Open question for owner:**
- (Q4) Should Tier-1 peer-reviewed papers beat Scholarpedia when both exist? (My vote: they tie — both are Tier 1. Scholarpedia is a peer-reviewed encyclopedia and its summaries are sometimes more useful than the original paper for orientation.)

---

## 6. Required invariants

**I1 — Every entry has ≥1 anchor or is flagged internal_construction.** Enforced by nightly (or on-commit) audit query:

```sql
SELECT e.id FROM entries e
LEFT JOIN external_anchors a ON a.entry_id = e.id
LEFT JOIN internal_constructions i ON i.entry_id = e.id
WHERE a.entry_id IS NULL AND i.entry_id IS NULL;
-- any rows returned = orphaned entries
```

**I2 — Every `canonical_authority` anchor has tier ≤ 2.** Tier 3 preprints are provisional; never the ultimate authority.

**I3 — Every `contradicts` anchor has a non-null `notes` field.** You don't get to disagree with the literature silently.

**I4 — `internal_construction` entries are reviewed on every major session.** Handover docs must list them; the count shouldn't grow without explicit owner awareness.

---

## 7. Verification and durability — **revised 2026-04-17**

**Foundational framing:** Age alone does not imply decay. In established science, age + no challenge is durability evidence — the source has stood the test of time. Treating an old anchor as automatically "stale" stigmatizes stability.

**Durability model is trigger-based, not calendar-based, and varies by source stability class.**

New field in `external_anchors`:

```sql
source_stability_class TEXT NOT NULL
  -- 'canonical'           : peer-reviewed, widely-cited, stable reference (Chentsov 1982, Maxwell's equations)
  -- 'active-literature'   : peer-reviewed but in a live debate (cosmological coupling)
  -- 'preprint-evolving'   : arXiv preprint that may be revised
  -- 'data-ref-periodic'   : authoritative data reference with known update cadence (PDG, NIST)
```

| Stability class | Typical tier | Re-verification trigger | Does age trigger review? |
|---|---|---|---|
| `canonical` | 1 | Event-driven: retraction, published errata, new edition, or citation-graph signal (widely-challenged) | **No.** Old + canonical + no events = stronger evidence, not weaker |
| `active-literature` | 1-2 | New papers in the debate; adjacent results; owner-chosen review cadence | Yes, but on domain-specific schedule |
| `preprint-evolving` | 3 | New arXiv `vN` available | Version-based only |
| `data-ref-periodic` | 4 | Per-source schedule (PDG biennial, NIST annual) | Yes, on source schedule |

**Bimodal surfacing — replacement for "stale":**

- **`deep-bench`** — tier 1, `confidence='high'`, `source_stability_class='canonical'`, old `verified_date`, no trigger events fired. **Feature, not defect.** Surface as "long-established anchor."
- **`overdue-review`** — any of: (a) tier 1 with `confidence` below `high` and old `verified_date`; (b) tier 2 past 180d calendar refresh; (c) tier 3 with newer version available; (d) any anchor where a trigger event was detected but re-verification hasn't happened yet.

Age by itself never flags an anchor. Age **combined with** confidence state or triggering signals does.

**Re-verification workflow when a trigger fires:**
1. Re-fetch `identifier`
2. If `revision_id` changed (tier 2) or new `vN` exists (tier 3): re-read to check the relationship still holds; update fields
3. If content changed materially and the relationship no longer holds: flag as `stale-relationship-changed` in `notes` and re-run the prior-art gate
4. For `canonical` class: retraction/errata events rerun the prior-art gate on the anchored entry

**Why this matters for the project:** We WANT a wiki where Chentsov/Amari, Onsager's solution, Bekenstein 1973, Gefen 1980 are anchored once and stay anchored for years. Their stability is load-bearing for the graph. A decay-based UI would paint them "stale" and undermine the epistemic signal that stable results ARE stable.

---

## 8. Worked example — P2 → WBE 1997

**Entry under review:** P2 "Metabolic Exponent Tracks Vascular D_eff"
**Plain-language claim:** Animal metabolic scaling exponent α = D_eff / (D_eff + 1) tracks vascular network dimensionality

**Prior-art gate output:**

```
Search angles run:
  - "metabolic scaling law" [Wikipedia + Semantic Scholar]
  - "Kleiber's law derivation" [Semantic Scholar]
  - "fractal vascular network metabolic rate" [arXiv]

Primary sources checked:
  - West, Brown, Enquist 1997 Science 276, 122 (abstract + full-text)
  - Savage, Gillooly, Woodruff, West, Hou, Woodruff, Brown 2004 Functional Ecology (abstract)
  - Banavar, Maritan, Rinaldo 1999 Nature (abstract)

Prior-art verdict:
  reframing_of: West-Brown-Enquist 1997

Drift-pattern tags:
  restatement-in-new-vocabulary

Recommendation:
  Create 2 anchors:
  1. entry_id='P2', source='doi', identifier='10.1126/science.276.5309.122',
     tier=1, relationship='reframing_of',
     notes='P2 claim α=D_eff/(D_eff+1) is identical to WBE 1997 prediction α=3/4 via
            the fractal vascular derivation (eq. 5, Table 1). The "tracks D_eff"
            framing is owner-constructed; the functional form is WBE.'
  2. entry_id='P2', source='wikipedia', identifier='https://en.wikipedia.org/wiki/Kleiber%27s_law',
     revision_id='<oldid fetched at verification time>',
     tier=2, relationship='adjacent_concept',
     notes='Kleiber observation predates WBE derivation; Wikipedia article surveys both.'

  Update ds_wiki.db.conjectures P2 three_state:
    'Falsified by literature: reframing_of WBE 1997 (DOI:10.1126/science.276.5309.122).
     Pattern: restatement-in-new-vocabulary.'
```

Net effect on the wiki:
- No new reference_law entry duplicating WBE content
- P2 conjecture row preserved with diagnostic label
- 2 anchor rows capturing the actual relationship
- Gap analyzer now sees P2 as "answered by external source"
- Future queries for "metabolic scaling" surface P2 + its anchor chain

---

## 9. Migration plan

1. **This doc reviewed, taxonomy + tiering + staleness locked** (owner decision on Q1-Q5)
2. **Migration script** `scripts/migrations/create_external_anchors_2026_04_17.py`:
   - `CREATE TABLE external_anchors` + `CREATE TABLE internal_constructions` in `wiki_history.db`
   - INSERT OR IGNORE pattern; safe to re-run
   - Test: inserts one demo row, rolls back, verifies schema
3. **Worked-example dry run:** produce the full P2 anchor report (per §8), owner reviews, tweaks format if needed
4. **Apply to Pass 1 fold-in (9 items):** one gate report + anchor insert per item, owner reviews batch
5. **Retrospective anchoring as separate project:** domain-by-domain, multi-session, governed by this same architecture

Estimated effort:
- Steps 1-3: this session or next (hours)
- Step 4: 1-2 sessions (depends on how much primary-source reading the gate triggers)
- Step 5: weeks, distributed across future sessions

---

## 10. What this architecture does NOT solve

Listed for honesty:

- **Coverage gaps.** Some entries are genuinely project-internal (DFIG constructions, CCA sub-claims, Fisher-gravity chain). They get `internal_construction` flags — informative, not dismissive. The label says "novelty burden is on us," which is exactly what the epistemic contract demands.
- **Wikipedia drift.** Living encyclopedias rewrite; `revision_id` pinning helps reproduce what we saw, but the current version may diverge. Staleness policy handles this via periodic re-verification.
- **Semantic-alignment gotchas.** An anchor says "this external source is related to this entry." It doesn't prove our framing of the concept is correct. That's what `notes` + the gate's primary-source reading are for.
- **Novelty verification reliability.** Per M0 meta-observation: single-pass LLM novelty verdicts are historically unreliable on this project. Anchors marked `confidence='low'` flag this; architecture cannot fix it — only discipline can.
- **The question of which bridges to make.** Engine surfaces candidates; the anchor table persists them. Whether a bridge is meaningful is still a human judgment, and should be.

---

## 11. Decision points summary (for quick owner review)

| # | Decision | Resolution (2026-04-17) |
|---|---|---|
| Q1 | Split `reframing_of`? | **No** — use notes field |
| Q2 | Add `inspired_by`? | **No** — too soft |
| Q3 | Missing any relationship type? | **Taxonomy frozen at 10.** Non-fitting candidates → `pending_anchor_reviews` queue for lit review. New types added only after ≥2 independent orphan cases |
| Q4 | Tier 1 papers vs Scholarpedia? | **Tie** |
| Q5 | Freshness thresholds? | Age ≠ decay. Trigger-based for canonical; see §7 |

**All design decisions locked. Ready for migration script + P2 dry run.**
