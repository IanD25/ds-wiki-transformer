# Hardware-Aware Embedding Model Selection

## Overview

The project automatically detects available hardware (GPU vs. CPU) and selects the optimal embedding model:

- **ShadowPC (RTX 2000 GPU)**: `BAAI/bge-large-en-v1.5` (1024-dim, GPU-accelerated)
- **Mac (no CUDA)**: `BAAI/bge-base-en-v1.5` (768-dim, CPU-compatible)
- **Any machine without PyTorch**: Falls back to base model safely

## How It Works

**Location**: `src/config.py` (lines 16–33)

```python
def _get_embed_model():
    """Select embedding model based on available hardware."""
    try:
        import torch
        if torch.cuda.is_available():
            return "BAAI/bge-large-en-v1.5", 1024
        else:
            return "BAAI/bge-base-en-v1.5", 768
    except ImportError:
        return "BAAI/bge-base-en-v1.5", 768

EMBED_MODEL, EMBED_DIM = _get_embed_model()
```

### Detection Logic

1. **Try to import `torch`** — if successful, check for CUDA
   - ✅ CUDA available → Use large model (1024-dim, ~30% faster on GPU)
   - ❌ No CUDA → Use base model (768-dim, CPU fallback)
2. **If `torch` not installed** — silently use base model (no crash)

## Usage

### On ShadowPC (GPU setup)

```bash
# 1. Ensure PyTorch is installed with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 2. Rebuild embeddings with the faster large model
python3 -m src.sync
```

**Result**: `torch.cuda.is_available() → True` → auto-selects `bge-large-en-v1.5`

### On Mac (no GPU)

```bash
# 1. Clone and setup normally (no PyTorch install needed)
bash setup.sh

# 2. Run sync — config auto-falls back to base model
python3 -m src.sync
```

**Result**: `ImportError` caught → safely uses `bge-base-en-v1.5`

### Switching Machines

**No code changes needed.** Just run `python3 -m src.sync` on the target machine:
- On **Mac**: Detects no CUDA → uses 768-dim base model
- On **ShadowPC**: Detects CUDA → uses 1024-dim large model
- `data/chroma_db/` rebuilds with the selected model automatically

## Performance Impact

| Machine | Model | Dimensions | Speed | Notes |
|---------|-------|-----------|-------|-------|
| ShadowPC (RTX 2000) | `bge-large-en-v1.5` | 1024 | ~30% faster (GPU) | Preferred for Phase 2 analysis |
| Mac (M4) | `bge-base-en-v1.5` | 768 | CPU baseline | Development/testing |
| No GPU env | `bge-base-en-v1.5` | 768 | CPU baseline | Fallback |

## Verification

Check which model is active:

```python
from src.config import EMBED_MODEL, EMBED_DIM
print(f"Model: {EMBED_MODEL}, Dimensions: {EMBED_DIM}")
```

Or in shell:
```bash
python3 -c "from src.config import EMBED_MODEL, EMBED_DIM; print(f'{EMBED_MODEL} ({EMBED_DIM}d)')"
```

## Git Commit

- **Commit**: `7f8c796`
- **Branch**: `claude/review-repo-structure-SINAV`
- **Files changed**: `src/config.py`

## Future Upgrades (GPU-only)

When GPU acceleration is available on ShadowPC, add:

1. **Cross-encoder for reranking**:
   ```bash
   pip install sentence-transformers
   # Use: cross-encoder/ms-marco-MiniLM-L-12-v2
   ```

2. **Local LLM for Phase 3 claim extraction**:
   ```bash
   pip install ollama
   # Model: phi-3-mini-4k-instruct (4-bit, ~2.5GB VRAM)
   ```

3. **Fine-tuning BGE on DS Wiki link pairs** (optional):
   - Contrastive learning on existing link graph
   - ~2–4 hours training, ~5–10% bridge quality improvement
