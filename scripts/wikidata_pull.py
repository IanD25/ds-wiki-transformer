"""
wikidata_pull.py — Pull all Wikidata physical-law entries and cross-reference
against ds_wiki.db to identify coverage gaps.

Queries:  P31 = Q214070 (physical law)
          Also walks subclasses (gas law, thermodynamic relation, etc.)
Fields pulled per entry:
  - label, description
  - P2534  formula (LaTeX)
  - P101   field of work
  - P61    discoverer / named after
  - P571   inception (year discovered)
  - sitelink to English Wikipedia article

Output modes:
  --report   : human-readable gap report (default)
  --json     : full JSON dump for downstream LLM drafting
  --matched  : only entries already in ds_wiki.db (verify coverage)

Run:
    python3 scripts/wikidata_pull.py
    python3 scripts/wikidata_pull.py --json > data/wikidata_laws.json
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from config import SOURCE_DB

# ── Wikidata endpoints ────────────────────────────────────────────────────────
SPARQL_URL = "https://query.wikidata.org/sparql"
API_URL    = "https://www.wikidata.org/w/api.php"
HEADERS    = {"User-Agent": "DS-Wiki-Transformer/1.0 (research; contact: ds-wiki-bot)"}

# Physical law + clean subclasses only.
# Q11348 (law of science) and Q185864 (scientific law) are dropped —
# both are badly curated on Wikidata (include "seigneur of Uzès", math functions, etc.)
TARGET_CLASSES = {
    "Q214070":  "physical law",
    "Q379231":  "gas law",
}

# Properties to fetch
PROPS = {
    "P2534": "formula",
    "P101":  "field_of_work",
    "P61":   "discoverer",
    "P138":  "named_after",
    "P571":  "inception",
}

SPARQL_BATCH = """
SELECT DISTINCT ?item ?itemLabel ?itemDescription ?formula ?field ?fieldLabel
                ?discoverer ?discovererLabel ?namedAfter ?namedAfterLabel
                ?inception ?wpTitle
WHERE {{
  VALUES ?class {{ {classes} }}
  ?item wdt:P31 ?class .
  OPTIONAL {{ ?item wdt:P2534 ?formula . }}
  OPTIONAL {{ ?item wdt:P101  ?field . }}
  OPTIONAL {{ ?item wdt:P61   ?discoverer . }}
  OPTIONAL {{ ?item wdt:P138  ?namedAfter . }}
  OPTIONAL {{ ?item wdt:P571  ?inception . }}
  OPTIONAL {{
    ?wpArticle schema:about ?item ;
               schema:inLanguage "en" ;
               schema:isPartOf <https://en.wikipedia.org/> .
    BIND(REPLACE(STR(?wpArticle), "https://en.wikipedia.org/wiki/", "") AS ?wpTitle)
  }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY ?itemLabel
"""


def run_sparql(query: str, timeout: int = 60) -> list:
    for attempt in range(3):
        try:
            r = requests.get(
                SPARQL_URL,
                params={"query": query, "format": "json"},
                headers={**HEADERS, "Accept": "application/sparql-results+json"},
                timeout=timeout,
            )
            r.raise_for_status()
            return r.json()["results"]["bindings"]
        except requests.exceptions.Timeout:
            if attempt < 2:
                print(f"  [SPARQL timeout, retry {attempt+1}]", file=sys.stderr)
                time.sleep(5)
            else:
                raise
    return []


def pull_wikidata_laws() -> List[Dict]:
    """Fetch all physical-law entries from Wikidata. Deduplicates by QID."""
    classes_str = " ".join(f"wd:{qid}" for qid in TARGET_CLASSES)
    query = SPARQL_BATCH.format(classes=classes_str)

    print("Querying Wikidata SPARQL...", file=sys.stderr)
    rows = run_sparql(query, timeout=90)
    print(f"  {len(rows)} raw rows returned", file=sys.stderr)

    # Deduplicate by QID, merging fields
    by_qid: Dict[str, Dict] = {}
    for row in rows:
        qid = row["item"]["value"].split("/")[-1]
        if qid not in by_qid:
            by_qid[qid] = {
                "qid":         qid,
                "label":       row.get("itemLabel",       {}).get("value", ""),
                "description": row.get("itemDescription", {}).get("value", ""),
                "formula":     None,
                "field":       None,
                "discoverer":  None,
                "named_after": None,
                "inception":   None,
                "wp_title":    None,
            }
        entry = by_qid[qid]
        if not entry["formula"]     and row.get("formula"):
            entry["formula"]     = row["formula"]["value"]
        if not entry["field"]       and row.get("fieldLabel"):
            entry["field"]       = row["fieldLabel"]["value"]
        if not entry["discoverer"]  and row.get("discovererLabel"):
            entry["discoverer"]  = row["discovererLabel"]["value"]
        if not entry["named_after"] and row.get("namedAfterLabel"):
            entry["named_after"] = row["namedAfterLabel"]["value"]
        if not entry["inception"]   and row.get("inception"):
            raw = row["inception"]["value"]
            entry["inception"]   = raw[:4] if raw else None   # year only
        if not entry["wp_title"]    and row.get("wpTitle"):
            entry["wp_title"]    = row["wpTitle"]["value"].replace("_", " ")

    # Remove unlabeled / Q-code-only stubs
    laws = [v for v in by_qid.values()
            if v["label"] and not v["label"].startswith("Q")]
    laws.sort(key=lambda x: x["label"].lower())
    return laws


def load_existing_titles() -> set:
    """Load all entry titles from ds_wiki.db for cross-reference."""
    conn = sqlite3.connect(SOURCE_DB)
    cur = conn.cursor()
    cur.execute("SELECT title FROM entries")
    titles = {row[0].lower() for row in cur.fetchall()}
    conn.close()
    return titles


def _normalize(s: str) -> str:
    """Normalise for fuzzy matching: lowercase, strip 's, apostrophes."""
    return (s.lower()
              .replace("'s", "")
              .replace("'", "")
              .replace("law of ", "")
              .replace("principle of ", "")
              .strip())


def find_match(label: str, existing: set) -> Optional[str]:
    """Return matching DB title or None."""
    label_l = label.lower()
    if label_l in existing:
        return label

    # Fuzzy: try normalised forms
    norm = _normalize(label)
    for t in existing:
        if _normalize(t) == norm:
            return t

    # Partial: label is a substring of DB title or vice versa
    for t in existing:
        if norm in _normalize(t) or _normalize(t) in norm:
            return t
    return None


# Labels that indicate noise — pure math constructs, bureaucratic titles, etc.
_NOISE_TOKENS = {
    "function", "integral", "symbol", "factorial", "operator", "polynomial",
    "zeta", "gamma", "coefficient", "conjecture", "hypothesis", "metric",
    "seigneur", "bishop", "commander", "prefect", "viscount", "administrator",
    "councillor", "councilor", "councellor", "Geheimer", "Landesvorstand",
    "3d texture", "color mapping", "digital root", "square root", "greatest common",
    "least common", "prime-counting", "probit", "logit", "p-value",
}

def _is_noise(label: str) -> bool:
    low = label.lower()
    return any(tok in low for tok in _NOISE_TOKENS)


def print_report(laws: List[Dict], existing: set) -> None:
    matched    = []
    new_signal = []   # new + not noise
    new_noise  = []   # new + looks like noise

    for law in laws:
        m = find_match(law["label"], existing)
        if m:
            matched.append((law, m))
        elif _is_noise(law["label"]):
            new_noise.append(law)
        else:
            new_signal.append(law)

    new_with_formula    = [l for l in new_signal if l["formula"]]
    new_without_formula = [l for l in new_signal if not l["formula"]]

    print(f"\n{'='*70}")
    print(f"WIKIDATA PHYSICAL LAW COVERAGE REPORT  (classes: Q214070, Q379231)")
    print(f"{'='*70}")
    print(f"  Wikidata entries pulled       : {len(laws)}")
    print(f"  Already in ds_wiki.db         : {len(matched)}")
    print(f"  New — signal (not noise)      : {len(new_signal)}")
    print(f"    WITH formula (P2534)        :   {len(new_with_formula)}")
    print(f"    WITHOUT formula             :   {len(new_without_formula)}")
    print(f"  Filtered as noise             : {len(new_noise)}")
    print(f"{'='*70}\n")

    print("── ALREADY IN DB (confirmed coverage) ─────────────────────────────")
    for law, match in matched:
        f_flag = "F" if law["formula"] else " "
        print(f"  [{f_flag}] {law['label'][:50]:52s} → {match[:35]}")

    print(f"\n── NEW — have formula (priority drafting candidates) ────────────────")
    for law in new_with_formula:
        disc = law["discoverer"] or law["named_after"] or "—"
        yr   = law["inception"] or "—"
        print(f"  {law['qid']:12s}  {law['label'][:50]:52s}  {law['field'] or '—'}")
        print(f"               discoverer: {disc:30s}  year: {yr}")

    print(f"\n── NEW — no formula (lower priority) ────────────────────────────────")
    for law in new_without_formula:
        print(f"  {law['qid']:12s}  {law['label'][:55]:57s}  {law['field'] or '—'}")

    print()


def main():
    parser = argparse.ArgumentParser(description="Pull Wikidata physical laws")
    parser.add_argument("--json",    action="store_true", help="Dump full JSON")
    parser.add_argument("--matched", action="store_true", help="Only matched entries")
    args = parser.parse_args()

    laws     = pull_wikidata_laws()
    existing = load_existing_titles()

    if args.json:
        # Annotate with match info then dump
        for law in laws:
            law["db_match"] = find_match(law["label"], existing)
        print(json.dumps(laws, indent=2, ensure_ascii=False))
        return

    if args.matched:
        print("QID          | Wikidata label                          | DB title")
        print("-" * 90)
        for law in laws:
            m = find_match(law["label"], existing)
            if m:
                print(f"{law['qid']:12s} | {law['label'][:40]:42s} | {m}")
        return

    print_report(laws, existing)


if __name__ == "__main__":
    main()
