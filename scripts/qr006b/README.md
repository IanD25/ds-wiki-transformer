# QR-006b benchmark pipeline

Implements `docs/experiments/QR006B_BENCHMARK_PREREGISTRATION.md` (the protocol; §12 lists
the amendments made while building this code). Mode B. Pilot report:
`docs/experiments/QR006B_PILOT_REPORT_2026_10_18.md`.

## Environment

A separate environment keeps the main `.venv` unchanged:

```bash
uv venv .venv-qr006b --python 3.13
VIRTUAL_ENV=.venv-qr006b uv pip install -r scripts/qr006b/requirements.txt
```

## Run (from `scripts/`)

```bash
../.venv-qr006b/bin/python -m pytest qr006b/tests -q          # estimator checks (§7 item 2)
../.venv-qr006b/bin/python -m qr006b.fidelity_bury ../data/reports/qr006b_pilot   # §7 item 1
../.venv-qr006b/bin/python -m qr006b.run_pilot --workers 9     # §7 pilot
```

The confirmatory run is not implemented as a runnable script until the owner starts it
(`config.FROZEN` must be True first).

## Layout

| File | Content |
|---|---|
| `config.py` | every parameter, one place |
| `models.py` | simulators (§2.2; Bury's models re-implemented, Amendment A1; Lever/Weinans, A12; R-tipping, A11) |
| `strata.py` | strata, families, validity rules, null pairing, splits (§2.3–2.5) |
| `preprocess.py` | Lowess / Gaussian / causal detrending, windows (§3) |
| `indicators/info.py` | I1–I6 (KSG MI, KSG transfer entropy, permutation and sample entropy, Fisher index, RPDE) |
| `indicators/baselines.py` | B1–B12 |
| `pipeline.py` | per-series indicators, Kendall τ, expanding τ, detection windows |
| `score.py` | AUC, directions, bootstrap, Holm, false-alarm thresholds, lead time |
| `pilot_settings.py` | the values the pilot sets (§7) |
| `fidelity_bury.py` | wrapper-fidelity check against Bury's unmodified scripts (§7 item 1) |
| `run_pilot.py` | the pilot |
| `data/` | Weinans et al. 2021 20D matrices (transcribed from their SI, CC BY 4.0) |

## Third-party material and licences

- `external/bury2021/` (git-ignored): sparse clone of
  `github.com/ThomasMBury/deep-early-warnings-pnas` at commit `d56b5df8`, `test_models/` only.
  CC BY-NC-SA 4.0 (README). It is run unmodified by `fidelity_bury.py` and never copied
  into this repository. Cloned 2026-10-18 with the owner's approval.
- hctsa's `EN_rpde.m` (GPL v3) and Little's `close_ret.c` (no licence) were read, not
  ported; RPDE is re-implemented from Little et al. 2007 (Amendment A5).
- cRAD follows the authors' MIT-licensed code (`brendanjohnharris/Criticality`), re-implemented.
- Raw outputs go to `data/experiments/qr006b/` (git-ignored); summaries to `data/reports/`.
