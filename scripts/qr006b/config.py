"""Every QR-006b parameter in one place (pre-registration §2-§7 plus Amendments).

run_confirmatory.py refuses to run unless FROZEN is True and the code and
protocol are committed.
"""

FROZEN = True     # freeze commit, 2026-10-18 (pre-registration §13)

# Values set by the pilot (§7), by their stated rules; see §13 and
# data/reports/qr006b_pilot/pilot_settings.json
PILOT_VALUES = {
    "S3_sigma_a": 0.06,
    "S3_sigma_b": 0.35,
    "S4_sigma_a": 0.03988249760664515,
    "S4_sigma_b": 0.21661863433423317,
    "S5_rc_a": 2.005835039594678,
    "S5_rc_b": 0.3779846535916829,
    "S5_sigma_a": 0.05,
    "S5_sigma_b": 0.05,
}

# ---- seeds (§2.5) ----------------------------------------------------------
SEED_CONFIRMATORY = 20261018
SEED_PILOT = 1
# Fixed integer codes used in the SeedSequence spawn key
# (stratum, family, class, run).
STRATUM_CODE = {"C0": 0, "C0g": 1, "CM": 2, "S1": 3, "S2": 4, "S3": 5,
                "S4": 6, "S5": 7, "SM": 8}
CLASS_CODE = {"transition": 0, "null": 1, "nullB": 2, "aux": 3}

# ---- sample sizes (§2.5, §7) -------------------------------------------------
N_PER_CLASS_CONFIRMATORY = 600
N_PER_CLASS_PILOT = 50
CALIBRATION_EVERY = 3          # run index i is calibration if i % 3 == 0 (1/3)

# ---- simulation (§2.2) -------------------------------------------------------
DT = 0.01
T_MAX = 1500
T_BURN = 100
SAMPLE_EVERY = 1.0             # time units

MAY = dict(r=1.0, k=1.0, s=0.1, b_lo=0.15, b_hi=0.27, b_crit=0.260437,
           x0=0.8197, sigma=0.01)
CUBIC = dict(c_lo=-0.2, c_hi=0.45, sigma=0.05)
CR_HOPF = dict(sf=4, sigma=0.01, r=4.0, k=1.7, h=0.15, e=0.5, m=2.0,
               a_lo=12.0, a_hi=16.0, a_crit=3.923 * 4, x0=1.0, y0=0.412)
CR_TRANS = dict(sf=4, sigma=0.01, r=4.0, k=1.7, h=0.15, e=0.5, m=2.0,
                a_lo=2.0, a_hi=6.0, a_crit=1.4 * 4, x0=1.0, y0=0.412)
LAYRITZ = dict(k_hi=5.0, k_step=1e-4, dt=0.005, spinup=10_000, scale=0.1,
               sample_every=40)
S2_ALPHAS = (1.5, 1.8)
S3_SIGMA_GRID = {"a": (0.02, 0.03, 0.04, 0.05, 0.06),
                 "b": (0.15, 0.2, 0.25, 0.3, 0.35)}
S4_PARAM = {"a": 0.24, "b": 0.1}
S5 = dict(lam_max=3.0, sigma=0.05, n_samples=1500, span_over_rc=10.0,
          substeps=20)

# ---- segments (§2.3) --------------------------------------------------------
BUFFER = 20
BUFFER_SENS = 50
MIN_TIP_FRACTION = 0.4
FLICKER_MIN_LEN = 5

# ---- preprocessing (§3) ------------------------------------------------------
LOWESS_SPAN = 0.2
GAUSS_BANDWIDTH = 0.2          # ewstools convention: kernel SD = (0.25/0.675) * bw * N
WINDOW = 0.25
WINDOW_SENS = 0.5
STRIDE = 5
REFERENCE_FRACTION = 0.2       # FI size-of-states, PC1 projection, C0g s_ref

# ---- indicators (§4) ---------------------------------------------------------
KSG_K = 4
PE_ORDER = 4
PE_ORDER_SENS = (3, 5)
SAMPEN_M = 2
SAMPEN_R = 0.2
RPDE_M = 2
RPDE_M_SENS = 3
RPDE_EPS = 0.12
KM_BINS = 20
KM_CENTRAL = 16
TE_PAIRS_20D = 20

# ---- scoring (§5) ------------------------------------------------------------
FAR = 0.05
FAR_SENS = 0.10
ALARM_RUN = 5
DETECT_WINDOW = 50
DETECT_OFFSETS = (0, 5, 10, 20)
T_RESP_MULTIPLES = (0, 1, 5, 20)
N_BOOT = 10_000
DELTA_AUC_MIN = 0.05
