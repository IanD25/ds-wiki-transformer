# CCBH Cluster — Layer 1 First Pass Analysis

**Date:** 2026-03-14
**Analyst:** Ian Darling (human gate)
**Status:** Layer 1 complete — awaiting pipeline ingestion for Layer 2+

---

## Papers in Cluster

1. **Farrah et al. 2023** — "Observational Evidence for Cosmological Coupling of Black Holes and its Implications for an Astrophysical Source of Dark Energy" (ApJL 944 L31)
2. **Cadoni et al.** — "Cosmologically Coupled Black Holes with Regular Horizons" (arXiv preprint)
3. **DESI Collaboration 2025** — "Positive Neutrino Masses with DESI DR2 via Matter Conversion to Dark Energy" (PRL 135 081003)

---

## Core Claim

Black holes are cosmologically coupled: their mass grows as m ∝ a^k where a is the scale factor and k ≔ −3w_phys. For vacuum energy interior (w = −1), k = 3 = d_spatial. Farrah 2023 measures k = 3.11 ± 1.19 at 90% confidence from elliptical galaxy BH mass evolution.

---

## DS Wiki Conjecture Mapping

### P3 — Running constants via Ω_D
**Connection:** BH mass m ∝ a^k with k = 3 is a running constant determined by spatial dimension. The coupling constant k literally runs with cosmological scale factor.
**Strength:** STRONG — direct example of a fundamental parameter (BH mass) whose evolution encodes dimensional information.

### P5/P6 — Fisher Rank = D_eff
**Connection:** k = 3 = d_spatial = d_eff. This is the first empirical measurement of d_eff at cosmological scales. If Fisher Information's effective dimension equals the number of independently measurable parameters, then k = 3 says the BH-cosmology coupling has exactly 3 independent degrees of freedom — the spatial dimensions.
**Strength:** STRONGEST — k = d_eff is the central novel conjecture from this analysis.

### P8 — Power-law exponents encode D_eff
**Connection:** m ∝ a^k with k = 3 encodes 3D spatial dimensionality in a power-law exponent. The exponent is not arbitrary — it equals the spatial dimension of the embedding space.
**Strength:** STRONG — textbook example of P8 if k = d_eff holds.

### P4/P15 — Information-thermodynamics bridge
**Connection:** BH vacuum energy = dark energy is an information-thermodynamic identification. BH entropy (Bekenstein-Hawking) ∝ A/4 encodes information about the interior equation of state. The k = 3 coupling connects BH thermodynamics to cosmological dark energy via information content of the horizon.
**Strength:** MODERATE — the connection is real but indirect. Needs formal information-theoretic derivation.

### T4 — Redshift-structure correlation
**Connection:** k = 3 BH mass growth contributes to cosmological dynamics at z ~ 0.7 (Farrah 2023 redshift range). BH population statistics at different redshifts show structure in the coupling measurement.
**Strength:** MODERATE — redshift dependence is present but not the primary signal.

### T3 — Ω_D unit consistency
**Connection:** Cadoni et al. provides a dimensionally consistent GR derivation of cosmological coupling. The metric ansatz ensures unit consistency between BH interior and FLRW exterior.
**Strength:** MODERATE — provides the mathematical scaffolding that makes k = 3 physically meaningful rather than numerological.

---

## Proposed New Conjecture

### P_new: d_eff = k = −3w_phys for cosmologically embedded systems

**Statement:** For systems cosmologically coupled to the Friedmann background, the Fisher Information effective dimension d_eff equals the cosmological coupling constant k = −3w_phys. When the interior equation of state is vacuum energy (w = −1), d_eff = k = 3 = d_spatial.

**Why this matters:** This unifies:
- Fisher Information theory (d_eff as the number of independently measurable parameters)
- General Relativity (k as the cosmological coupling exponent from matched metrics)
- Thermodynamics (w as the equation of state parameter)
- Spatial dimension (d = 3 as a measured, not assumed, quantity)

**Evidence:**
- Farrah 2023: k = 3.11 ± 1.19 (90% CL), consistent with k = 3
- Cadoni et al.: Theoretical framework deriving k from GR metric matching
- DESI 2025: CCBH model with k = 3 improves cosmological fits with DESI DR2 data

**Status:** Conjectural. Needs:
1. Independent k measurement from non-elliptical-galaxy channel
2. Formal derivation of d_eff = k from Fisher Information on the matched metric
3. Test against other w values (w ≠ −1 → k ≠ 3 → d_eff ≠ d_spatial?)

---

## Pipeline Next Steps

1. Extract medium-granularity entries from each paper (following OPERA parser pattern)
2. Build `ccbh_cluster_raw.json` with full prose descriptions
3. Parse into `rrp_ccbh_cluster.db`
4. Run Pass 2 (ChromaDB bridges to DS Wiki)
5. Run Fisher Suite + structural alignment
6. Compare pipeline results against this manual conjecture mapping (calibration test for Phase 3)
