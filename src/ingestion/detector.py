"""
detector.py — Detect RRP format from a directory or file path.

Checks for format-specific marker files/keys and returns the format
string used to select the correct parser.

Supported formats (in detection order):
  zoo_classes_json  — Timeroot/ZooClasses (classes.json + theorems.json)
  cobra_json        — COBRA/BiGG metabolic model (reactions/metabolites/genes)
  flat_json         — Generic flat JSON array (Periodic Table, etc.)
  frictionless      — Frictionless Data (datapackage.json)
  ro_crate          — RO-Crate (ro-crate-metadata.json)
  codemeta          — CodeMeta (codemeta.json)
  citation_cff      — Citation File Format (CITATION.cff)
  unknown           — Cannot determine format
"""

import json
from pathlib import Path
from typing import Optional


FORMAT_MARKERS = {
    "zoo_classes_json": ["classes.json", "theorems.json"],
    "cobra_json":       None,   # detected by JSON key inspection
    "flat_json":        None,   # detected by JSON key inspection (fallback)
    "frictionless":     ["datapackage.json"],
    "ro_crate":         ["ro-crate-metadata.json"],
    "codemeta":         ["codemeta.json"],
    "citation_cff":     ["CITATION.cff"],
}


def detect(path: str | Path) -> str:
    """
    Detect the RRP format at the given path (directory or single file).
    Returns a format string from FORMAT_MARKERS or 'unknown'.
    """
    path = Path(path)

    if path.is_dir():
        return _detect_directory(path)
    elif path.is_file():
        return _detect_file(path)
    else:
        raise FileNotFoundError(f"Path not found: {path}")


def _detect_directory(directory: Path) -> str:
    files = {f.name for f in directory.iterdir()}

    # File-marker-based detection (ordered by specificity)
    for fmt, markers in FORMAT_MARKERS.items():
        if markers and all(m in files for m in markers):
            return fmt

    # Fall back to inspecting any .json file
    json_files = list(directory.glob("*.json"))
    for jf in json_files:
        fmt = _detect_file(jf)
        if fmt != "unknown":
            return fmt

    return "unknown"


def _detect_file(file: Path) -> str:
    if file.suffix not in (".json", ".JSON"):
        if file.name == "CITATION.cff":
            return "citation_cff"
        return "unknown"

    try:
        with open(file) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return "unknown"

    # COBRA/BiGG: top-level keys include reactions, metabolites, genes
    if isinstance(data, dict):
        keys = set(data.keys())
        if {"reactions", "metabolites", "genes"}.issubset(keys):
            return "cobra_json"
        if "@context" in data and "@graph" in data:
            return "ro_crate"
        if "name" in data and "resources" in data:
            return "frictionless"

    # Flat JSON array → generic flat_json
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        return "flat_json"

    # Wrapped array: {"elements": [...]} or {"data": [...]} etc.
    if isinstance(data, dict):
        for v in data.values():
            if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                return "flat_json"

    return "unknown"


def detect_with_report(path: str | Path) -> dict:
    """Like detect(), but returns a dict with format + supporting evidence."""
    path = Path(path)
    fmt = detect(path)

    report = {"path": str(path), "format": fmt, "evidence": []}

    if path.is_dir():
        files = [f.name for f in path.iterdir()]
        report["files_found"] = sorted(files)
        if fmt in FORMAT_MARKERS and FORMAT_MARKERS[fmt]:
            report["evidence"] = [
                f"marker file present: {m}"
                for m in FORMAT_MARKERS[fmt]
                if m in files
            ]

    return report
