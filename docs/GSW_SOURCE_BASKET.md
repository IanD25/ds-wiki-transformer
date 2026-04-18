# GSW Source Basket — Per-Domain Reference List

**Status:** DESIGN + STARTER — drafted 2026-04-18
**Anchor docs:** `GSW_ANCHOR_ARCHITECTURE.md` (schema, relationships, roles), `feedback_prior_art_gate.md` (standing rule)
**Built on:** taxonomy applied in chunks 1-7 (300 items tagged across 10 top-level domains)

---

## 1. Purpose

For any entry whose primary domain tag is known, the prior-art gate needs to know **which external sources to search** and **how reliably each one responds** via WebFetch. This doc is that reference.

Organization:
- **§2 Universal sources** (apply across all domains — Wikipedia, arXiv, CrossRef, etc.)
- **§3 Reliability classification** (from INFO1 smoke test + general knowledge)
- **§4 Per-domain baskets** (10 sections, one per top-level domain)
- **§5 Missing/weak domains** (coverage gaps to flag)
- **§6 Source enum** (candidate values for `source` column in `external_anchors`)

**Rule applied:** primary-source canonization is intra-domain. Cross-domain concepts are handled by the sub-tag borrowings graph, not by searching every source for every topic.

---

## 2. Universal sources

These apply to EVERY domain's prior-art gate. Every gate run checks these first.

| Source | Role typically filled | Reliability | Enum value |
|---|---|---|---|
| Wikipedia | `living_reference` | ✓ stable via WebFetch | `wikipedia` |
| CrossRef (DOI metadata) | metadata for any paper | ✓ stable via REST API | `doi` |
| arXiv (preprint server) | `progenitor` for math/physics/CS/stats | ✓ stable via API (export.arxiv.org) | `arxiv` |
| Semantic Scholar | citation graph, influential papers | ⚠ rate-limited, use selectively | `semantic-scholar` |
| Google Scholar (via WebSearch) | discovery tool | ⚠ no API, use WebSearch | — |

**Usage pattern per gate:**
1. Start with Wikipedia (fast orientation, citation harvest)
2. Use CrossRef to verify any DOI surfaced
3. Use arXiv API for preprint / recent-paper search scoped to relevant sub-categories
4. Pull Semantic Scholar citation counts for the candidate anchors (rate-limit aware)

---

## 3. Reliability classification (from INFO1 smoke test)

| Source | Status | Notes |
|---|---|---|
| `wikipedia` | ✓ **CONFIRMED** | Fast, reliable, revision-pinnable via `oldid` |
| `mathworld` | ✓ **CONFIRMED** | Wolfram-maintained; stable URLs |
| `nlab` | ✓ **CONFIRMED** | Technical, good for category-theory / adjacent_concept |
| `doi` via `api.crossref.org` | ✓ **CONFIRMED** | Metadata only; does not fetch PDFs |
| `arxiv` via `export.arxiv.org` | ✓ known-reliable | Rate limit: ~1 req/3s |
| `scholarpedia` | ⚠ **FLAKY** | 2× timeouts in smoke test; articles confirmed to exist via WebSearch. **Retry protocol needed.** |
| `encyclopedia-math` | ✗ **BLOCKED** | `ECONNREFUSED` — site appears to block WebFetch. Use as reference only; manual verification |
| `semantic-scholar` | ⚠ **RATE-LIMITED** | 404 on some DOI lookups; 429 on search. Works but sparingly |
| `sep` (Stanford Encyclopedia) | ⚠ needs testing | Should work — static HTML pages |
| `pubmed` (NCBI E-utilities) | ⚠ needs testing | Public API, known-reliable in principle |
| `europe-pmc` | ⚠ needs testing | REST API available |
| `ads` (NASA ADS) | ⚠ requires free token | For astrophysics |
| `inspire-hep` | ⚠ needs testing | For high-energy physics |
| `dblp` | ⚠ needs testing | For CS |
| `living-reviews` | ⚠ needs testing | For GR (Living Reviews in Relativity) |
| `isbn` | N/A | Offline-verifiable for textbook anchors; no fetch path |

**Action items flagged:**
- Write a retry wrapper for Scholarpedia (exponential backoff; 3 attempts)
- Treat Encyclopedia of Mathematics as reference-only; anchor by title without fetch
- Semantic Scholar: keep scoped to citation-graph queries; don't use for bulk paper search

---

## 4. Per-domain baskets

For each domain, the table lists typical sources for each of the 5 canonical roles. This is the **baseline check set** — the gate should sweep across these for entries tagged with this domain as primary.

### 4.1 `physics` (and sub-tags: .classical, .modern, .cosmology)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | arXiv (physics, hep-*, gr-qc, cond-mat, quant-ph), Phys. Rev. A/B/C/D/E, Rev. Mod. Phys., Nature Physics | DOI lookups via CrossRef |
| `axiomatic_foundation` | Sub-domain textbooks (Griffiths EM, Sakurai QM, MTW/Wald GR, Chaikin-Lubensky stat mech) | Scholarpedia article authors' refs |
| `standard_textbook` | Feynman Lectures, Landau-Lifshitz series, Jackson (E&M), Peskin-Schroeder (QFT) | Cosmology: Dodelson, Weinberg |
| `living_reference` | Wikipedia, Scholarpedia (strong for physics — Sethna wrote on sloppy models), **Living Reviews in Relativity** (GR-specific), MathWorld for math-adjacent | nLab for math-phys |
| `comprehensive_survey` | Rev. Mod. Phys., Reports on Progress in Physics, Physics Reports | NASA ADS for astro; INSPIRE-HEP for hep |

**Domain-specific data references (tier 4):** PDG (particle data), NIST (constants), IAU definitions.
**Domain search scope for arXiv:** `physics.*`, `hep-*`, `gr-qc`, `astro-ph`, `cond-mat`, `quant-ph`, `math-ph`.

### 4.2 `mathematics` (and sub-tags: .analysis, .algebra, .geometry_topology, .probability_measure, .discrete, .logic_foundations)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | arXiv (math.*), Annals of Mathematics, Inventiones, JAMS, Duke Math. J., Acta Math. | DOI lookups |
| `axiomatic_foundation` | Rudin (real analysis), Lang (algebra), Hatcher (algebraic topology), do Carmo (differential geometry), Billingsley (probability) | MathWorld, Encyclopedia of Math |
| `standard_textbook` | As above per sub-domain; Atiyah-Macdonald (commutative algebra), Spivak (diff geo) | — |
| `living_reference` | Wikipedia, MathWorld (Wolfram), Encyclopedia of Math (Springer — **currently blocks WebFetch**), nLab | PlanetMath, ProofWiki for proofs |
| `comprehensive_survey` | Bull. AMS, EMS Surveys in Mathematical Sciences, Annual Reviews | — |

**Domain-specific data references:** OEIS (integer sequences).
**Domain search scope for arXiv:** `math.*`.

### 4.3 `formal_logic` (and sub-tags: .proof_theory, .model_theory, .computability, .set_theory)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | J. Symbolic Logic, Annals of Pure and Applied Logic, J. Philosophical Logic, arXiv (math.LO) | DOI |
| `axiomatic_foundation` | Enderton "A Mathematical Introduction to Logic", Mendelson "Intro to Math Logic" | Kleene "Intro to Metamathematics" |
| `standard_textbook` | Van Dalen "Logic and Structure", Shoenfield "Mathematical Logic" | Smullyan (Gödel) |
| `living_reference` | **Stanford Encyclopedia of Philosophy** (primary for this domain), Wikipedia, nLab | MathWorld (for math-facing parts) |
| `comprehensive_survey` | Handbook of Mathematical Logic (Barwise), Handbook of Proof Theory | SEP review articles |

**SEP is the authoritative living reference for this domain** — more than Wikipedia.
**Domain search scope for arXiv:** `math.LO`, `cs.LO`.

### 4.4 `information_theory` (and sub-tags: .shannon, .coding, .quantum_info, .kolmogorov_complexity)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | IEEE Trans. Info. Theory, Shannon's BSTJ original, arXiv (cs.IT, quant-ph), IEEE ITA Workshop | DOI |
| `axiomatic_foundation` | Khinchin 1957 "Mathematical Foundations of Information Theory", Kolmogorov 1965 (complexity) | Shannon-Weaver 1949 book |
| `standard_textbook` | Cover & Thomas "Elements of Information Theory", MacKay "Info Theory, Inference, and Learning", Gallager | Nielsen & Chuang (quantum info) |
| `living_reference` | Wikipedia, MathWorld, Scholarpedia | nLab for categorical framing |
| `comprehensive_survey` | IEEE Trans. IT review articles, Foundations and Trends in Communications and Information Theory | — |

**Domain search scope for arXiv:** `cs.IT`, `quant-ph` (for quantum info), `math.IT`.

### 4.5 `statistics_probability` (and sub-tags: .bayesian, .frequentist, .stochastic_processes, .inference)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | Annals of Statistics, JASA, Biometrika, J. R. Stat. Soc. B, arXiv (math.ST, stat.*) | — |
| `axiomatic_foundation` | Kolmogorov 1933 "Foundations of the Theory of Probability" | Fisher 1922 (estimation) |
| `standard_textbook` | Casella & Berger (inference), Wasserman "All of Statistics", Gelman BDA (Bayesian), Gardiner (stochastic) | Billingsley (probability) |
| `living_reference` | Wikipedia, StatLect, MathWorld | Scholarpedia |
| `comprehensive_survey` | Statistical Science, Annual Review of Statistics and Its Application | — |

**Domain search scope for arXiv:** `math.ST`, `math.PR`, `stat.*`.

### 4.6 `computer_science` (and sub-tags: .algorithms, .complexity, .distributed, .ml, .programming_languages)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | arXiv (cs.*), JACM, SICOMP, STOC/FOCS proceedings, NeurIPS (for ML), POPL/PLDI (for PL) | DBLP for paper lookup |
| `axiomatic_foundation` | Sipser "Intro to the Theory of Computation", CLRS (algorithms), Papadimitriou (complexity) | — |
| `standard_textbook` | CLRS, Sipser, Bishop "PRML" (ML), Murphy "Probabilistic ML", Pierce "TAPL" (PL) | Distributed: Lynch "Distributed Algorithms" |
| `living_reference` | Wikipedia, Computational Complexity Zoo (for complexity classes) | — |
| `comprehensive_survey` | ACM Computing Surveys | Foundations and Trends series |

**Domain-specific ref:** DBLP for bibliography.
**Domain search scope for arXiv:** `cs.*`.

### 4.7 `chemistry` (and sub-tags: .physical, .organic, .materials, .biochemistry)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | JACS, Angewandte Chemie, Chem. Sci., J. Phys. Chem. A/B/C, Nature Chemistry | ChemRxiv |
| `axiomatic_foundation` | Atkins "Physical Chemistry", McQuarrie "Physical Chemistry: A Molecular Approach" | — |
| `standard_textbook` | Atkins, Clayden (organic), Stryer/Nelson (biochem), Callister (materials) | — |
| `living_reference` | Wikipedia, **MathWorld + Scholarpedia are thin here** | — |
| `comprehensive_survey` | Chem. Rev., Chem. Soc. Rev., Acc. Chem. Res. | — |

**Domain-specific data references:** PubChem, ChemSpider, Reaxys (subscription), NIST WebBook.
**⚠️ Note:** chemistry is under-served by the standard academic encyclopedias (Scholarpedia, MathWorld don't have much). Heavier reliance on Wikipedia + primary literature.

### 4.8 `biology` (and sub-tags: .molecular, .evolution, .ecology, .physiology, .neuroscience)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | Cell, Nature, Science, PLoS Biology, eLife, PNAS, bioRxiv | — |
| `axiomatic_foundation` | Alberts "Molecular Biology of the Cell", Campbell (intro bio), Nelson's Biochemistry (biochem) | Futuyma (evolution), Krebs (ecology) |
| `standard_textbook` | As above + Kandel (neuroscience), Schmidt-Nielsen (physiology) | — |
| `living_reference` | Wikipedia, **NCBI Bookshelf** (open-access textbooks) | Scholarpedia (some biology content) |
| `comprehensive_survey` | Annual Reviews series (many bio titles), Nature Reviews series | — |

**Domain-specific data references:** PubMed (NCBI), UniProt (proteins), KEGG (pathways), Gene Ontology, Encyclopedia of Life.
**Domain search scope for arXiv:** `q-bio.*` (limited use; most bio is on bioRxiv/PubMed instead).

### 4.9 `earth_sciences` (and sub-tags: .geology, .climate, .hydrology, .planetary)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | JGR, GRL, EPSL, Nature Geoscience, Science Advances, AGU journals | — |
| `axiomatic_foundation` | Turcotte & Schubert "Geodynamics", Holton "Intro to Dynamic Meteorology" | — |
| `standard_textbook` | As above + Anderson/Anderson (Earth surface), IPCC reports for climate | — |
| `living_reference` | Wikipedia, **USGS** pages for geology specifics | NASA Earth Observatory |
| `comprehensive_survey` | Annual Review of Earth and Planetary Sciences, Rev. Geophysics | IPCC assessment reports |

**Domain-specific data references:** USGS databases, NOAA, NASA Earth Data, PANGAEA.
**Domain search scope for arXiv:** limited — earth sciences mostly outside arXiv; check Earth ArXiv / EarthArXiv.

### 4.10 `networks_systems` (and sub-tags: .complex_systems, .graph_theory, .dynamical_systems)

| Canonical role | Primary sources | Secondary sources |
|---|---|---|
| `progenitor` | arXiv (nlin.*, physics.soc-ph), Nature, Science, PRL, Nature Physics, PNAS, Chaos (AIP), Physica D | — |
| `axiomatic_foundation` | Newman "Networks: An Introduction", Strogatz "Nonlinear Dynamics and Chaos", Guckenheimer-Holmes | — |
| `standard_textbook` | Barrat-Barthélemy-Vespignani (networks), Ott (chaos), Wiggins (dynamical systems) | Santa Fe Institute press |
| `living_reference` | Wikipedia, nLab (for category-theoretic networks) | Complexity Explorer (SFI) |
| `comprehensive_survey` | Phys. Rep., Rev. Mod. Phys. (for complex systems reviews), Chaos reviews | Annual Review of Condensed Matter Physics |

**Domain search scope for arXiv:** `nlin.*`, `physics.soc-ph`, `cond-mat.stat-mech`.

---

## 5. Coverage gaps and weak domains

Honest accounting of where the basket is thin or fragile:

1. **Chemistry encyclopedias** are thin (Scholarpedia + MathWorld don't have much chemistry). Heavier Wikipedia dependency — treat with more caution for `living_reference` role
2. **Earth sciences** not on arXiv broadly (use EarthArXiv); no single dominant living-reference site
3. **Encyclopedia of Mathematics** blocks WebFetch — need manual-verification fallback for the `living_reference` role in math
4. **Biology databases** (UniProt, KEGG) are `data-ref-periodic` tier 4, not canonical-authority sources for concepts — they're for entity-level data, not principles
5. **Economics / social sciences** absent from top-level taxonomy. P18/P19/P20 are tagged `statistics_probability` as closest proxy, but if the wiki grows into socio-economic modeling, we'll need a top-level `social_sciences` with RePEc / NBER / SSRN as sources
6. **Philosophy of physics / foundations** (interpretations of QM, philosophy of statistical mechanics) — covered under `formal_logic` or `physics` depending on framing; SEP is the authority. No dedicated top-level
7. **Medicine / clinical** — no coverage. Would need PubMed + Cochrane + UpToDate. Not a gap now but flag if biomedical content grows

---

## 6. `source` enum — proposed canonical values

The `external_anchors.source` column is currently free-text. Based on the basket audit, the following values should be standard. Adding non-enum values requires an owner decision.

| Enum value | Tier typical | Used for |
|---|---|---|
| `doi` | 1 | Any peer-reviewed paper via DOI |
| `arxiv` | 3 | arXiv preprints (versioned via `arxiv:XXXX.YYYYYvN`) |
| `wikipedia` | 2 | Wikipedia articles (revision-pinned via `oldid`) |
| `scholarpedia` | 1 | Scholarpedia articles |
| `sep` | 1 | Stanford Encyclopedia of Philosophy |
| `mathworld` | 2 | Wolfram MathWorld |
| `nlab` | 2 | nLab wiki |
| `encyclopedia-math` | 1 | Springer Encyclopedia of Mathematics |
| `isbn` | 1 | Textbooks by ISBN (offline verification) |
| `inspire-hep` | 1-3 | INSPIRE-HEP record (physics literature service) |
| `ads` | 1-3 | NASA ADS bibcode (astrophysics) |
| `pubmed` | 1 | PubMed record (PMID) |
| `europe-pmc` | 1 | Europe PMC (PMCID) |
| `dblp` | 1-3 | DBLP record (CS) |
| `living-reviews` | 1 | Living Reviews in Relativity / Solar Physics |
| `semantic-scholar` | — | Semantic Scholar paper ID (mainly for citation-graph context) |
| `pdg` | 4 | Particle Data Group |
| `nist` | 4 | NIST physical constants / reference data |
| `pubchem` | 4 | PubChem compound |
| `uniprot` | 4 | UniProt protein record |
| `usgs` | 4 | USGS data / pages |
| `oeis` | 4 | OEIS integer sequence |

Codifying these in a CHECK constraint is optional for now — leaving the column as free-text with this enum as documented convention is simpler. Can tighten later.

---

## 7. How the prior-art gate uses this doc

Workflow when gating a new entry with primary domain `D` and candidate sub-tag `S`:

1. **Identify baseline basket** = universal sources (§2) + domain-D basket (§4)
2. **If the entry's tags include a borrowing** (sub-tag from another home domain): also pull that home domain's basket
3. **Scope primary-source search** to the arXiv sub-categories / journals listed for `D`
4. **Living reference check** always includes Wikipedia + the domain-specific living_reference (Scholarpedia if exists, SEP for logic/philosophy, Living Reviews for GR, etc.)
5. **Reliability fallbacks** per §3: if a source is `FLAKY` or `BLOCKED`, note it in the gate report rather than silently skip

---

## 8. Scope of what this doc does NOT do

- Does not enumerate every paper in each domain (not a bibliography)
- Does not rank textbooks (there are multiple "standard" textbooks for most domains; the basket lists several)
- Does not handle domain-specific niche venues well — the tables are oriented toward major venues
- Does not (yet) include a live, fetchable "source registry" — this is a markdown reference doc; a future database-backed version could surface per-source availability statistics

---

## 9. Update cadence

- Add sources opportunistically as they're needed during anchoring
- Review + prune every 12-18 months (sources evolve — journals rebrand, sites go down)
- Failures-in-gate (repeated timeouts, blocks) should be logged back into §3 reliability classification

---

## 10. Immediate next step after this doc lands

With the basket locked in, the prior-art gate has a concrete rubric per entry. Natural next moves:

1. **Insert the INFO1 smoke-test anchors** (8 rows already drafted in the INFO1 report; the taxonomy + source enum + canonical_role are now all in place)
2. **Begin retrospective anchoring pass** — start with the highest-leverage entries per domain (tier-1 reference_laws first, conjectures second)
3. **Apply the 9 fold-in conjecture anchors** (P1 → ΛCDM, P2 → WBE, P8 → Gefen/JJK, P21 → Chentsov/Amari, etc.)

Each of those uses this basket as the baseline.
