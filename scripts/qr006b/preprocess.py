"""Detrending and windows (pre-registration §3, Amendment A4)."""

import math

import numpy as np
from numba import njit
from scipy.ndimage import gaussian_filter
from statsmodels.nonparametric.smoothers_lowess import lowess

from . import config as C

# ewstools convention: the kernel's quartiles sit at +/- 0.25 * bandwidth
KERNEL_SD_PER_BW = 0.25 / 0.675


def lowess_residuals(x, span=C.LOWESS_SPAN):
    """Offline residuals, as ewstools detrend(method='Lowess', span=0.2)."""
    t = np.arange(len(x), dtype=float)
    sm = lowess(x, t, frac=span)[:, 1]
    return x - sm


def gaussian_residuals(x, bw=C.GAUSS_BANDWIDTH):
    """Sensitivity: ewstools detrend(method='Gaussian', bandwidth=0.2)."""
    sm = gaussian_filter(x, sigma=KERNEL_SD_PER_BW * bw * len(x), mode="reflect")
    return x - sm


@njit(cache=True)
def _causal_mean(x, sd):
    n = x.shape[0]
    reach = int(5 * sd) + 1
    w = np.exp(-0.5 * (np.arange(reach) / sd) ** 2)
    out = np.empty(n)
    for t in range(n):
        num = 0.0
        den = 0.0
        lo = max(0, t - reach + 1)
        for s in range(lo, t + 1):
            num += w[t - s] * x[s]
            den += w[t - s]
        out[t] = num / den
    return out


def causal_residuals(x, seg_len, bw=C.GAUSS_BANDWIDTH):
    """§3.3: subtract a one-sided Gaussian-kernel mean of past values, kernel SD
    = (0.25/0.675) x bandwidth x segment length (ewstools convention)."""
    sd = KERNEL_SD_PER_BW * bw * seg_len
    return x - _causal_mean(np.ascontiguousarray(x, dtype=np.float64), sd)


def window_ends(seg_len, frac=C.WINDOW, stride=C.STRIDE):
    w = int(frac * seg_len)
    return w, np.arange(w - 1, seg_len, stride)
