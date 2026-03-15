#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# PFD Project — One-command environment setup
# Run from repo root: bash setup.sh
#
# Works on: macOS (M-series), Linux, Windows WSL / ShadowPC
# Requires: Python 3.11+ already installed
# ─────────────────────────────────────────────────────────────────────────────

set -e  # exit on first error

echo "═══════════════════════════════════════════════════════"
echo "  Principia Formal Diagnostics (PFD) — Environment Setup"
echo "═══════════════════════════════════════════════════════"
echo ""

# ── 1. Detect Python ──────────────────────────────────────────────────────────
PYTHON=""
for cmd in python3.13 python3.12 python3.11 python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VER=$($cmd --version 2>&1 | awk '{print $2}')
        MAJOR=$(echo "$VER" | cut -d. -f1)
        MINOR=$(echo "$VER" | cut -d. -f2)
        if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 11 ]; then
            PYTHON="$cmd"
            echo "✓ Python found: $cmd ($VER)"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo "✗ Python 3.11+ not found. Please install Python 3.11 or higher."
    echo "  macOS:   brew install python@3.13"
    echo "  Ubuntu:  sudo apt install python3.13 python3.13-venv"
    echo "  Windows: https://www.python.org/downloads/"
    exit 1
fi

# ── 2. Create virtual environment ─────────────────────────────────────────────
if [ -d ".venv" ]; then
    echo "✓ .venv already exists — skipping creation"
else
    echo "→ Creating virtual environment..."
    $PYTHON -m venv .venv
    echo "✓ .venv created"
fi

# ── 3. Activate ───────────────────────────────────────────────────────────────
echo "→ Activating .venv..."
# shellcheck disable=SC1091
source .venv/bin/activate

# ── 4. Upgrade pip silently ───────────────────────────────────────────────────
echo "→ Upgrading pip..."
pip install --upgrade pip -q

# ── 5. Install package (editable) + dependencies ────────────────────────────
echo "→ Installing PFD in editable mode (pip install -e .)..."
pip install -e ".[dev]" -q
echo "✓ PFD installed (editable) with all dependencies"

# ── 6. Optional: CUDA detection for GPU install ───────────────────────────────
echo ""
echo "→ Checking for CUDA GPU (ShadowPC / RTX upgrade)..."
if command -v nvidia-smi &>/dev/null; then
    GPU_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null | head -1)
    echo "  GPU detected: $GPU_NAME"
    echo ""
    echo "  ┌─ GPU UPGRADE AVAILABLE ──────────────────────────────────────────┐"
    echo "  │ Install PyTorch with CUDA support for faster embeddings:          │"
    echo "  │   pip install torch --extra-index-url \                           │"
    echo "  │         https://download.pytorch.org/whl/cu118                   │"
    echo "  │                                                                   │"
    echo "  │ bge-large-en-v1.5 (1024-dim) auto-selected when GPU is detected.  │"
    echo "  │ No manual config needed — src/config.py handles it.              │"
    echo "  └───────────────────────────────────────────────────────────────────┘"
else
    echo "  No NVIDIA GPU detected — CPU mode (M-series or no CUDA)"
fi

# ── 7. Verify data files ──────────────────────────────────────────────────────
echo ""
echo "→ Checking data files..."
if [ -f "data/ds_wiki.db" ]; then
    SIZE=$(du -sh data/ds_wiki.db | cut -f1)
    echo "  ✓ data/ds_wiki.db ($SIZE)"
else
    echo "  ✗ data/ds_wiki.db not found — check git clone was complete"
fi

if [ -d "data/rrp" ]; then
    echo "  ✓ data/rrp/ present"
else
    echo "  ✗ data/rrp/ not found"
fi

# ── 8. Check generated artifacts ─────────────────────────────────────────────
echo ""
if [ -d "data/chroma_db" ] && [ -f "data/wiki_history.db" ]; then
    echo "✓ chroma_db + wiki_history.db present (committed to repo)"
    echo "  Only rebuild if ds_wiki.db changes: python3 -m src.sync"
else
    echo "→ chroma_db or wiki_history.db missing — rebuilding..."
    python3 -m src.sync
    echo "✓ Artifacts rebuilt"
fi

# ── 9. Run tests ─────────────────────────────────────────────────────────────
echo ""
read -r -p "→ Run test suite now? (~15s) [Y/n]: " RUNTESTS
RUNTESTS="${RUNTESTS:-Y}"
if [[ "$RUNTESTS" =~ ^[Yy]$ ]]; then
    echo "→ Running pytest..."
    python3 -m pytest tests/ -v --tb=short -q
else
    echo "  Skipped — run 'python3 -m pytest tests/ -v' manually when ready"
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════════════════"
echo "  Setup complete!"
echo ""
echo "  Next steps:"
echo "    source .venv/bin/activate     (each new terminal)"
echo "    pfd report --rrp data/rrp/ecoli_core/rrp_ecoli_core.db   (run analysis)"
echo "    pfd --help                    (see all commands)"
echo "    python3 src/mcp_server.py     (optional: MCP server for Claude)"
echo ""
echo "  Full reference: CLAUDE.md | User guide: USER_GUIDE.md"
echo "═══════════════════════════════════════════════════════"
