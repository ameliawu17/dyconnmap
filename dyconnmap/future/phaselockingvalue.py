"""

"""
import numpy as np
import itertools

from estimator import Estimator

import sys

sys.path.append("/home/makism/Github/dyconnmap-feature_dataset/")
from dyconnmap import analytic_signal


class PhaseLockingValue(Estimator):
    """Phase Locking Value (PLV)."""

    def __init__(self):
        super()
        self.dtype = np.complex
        self.requires_preprocessing = True

    def preprocess(self, data: np.ndarray, **kwargs) -> np.ndarray:
        # super().preprocess(data, **kwargs)
        _, u_phases = analytic_signal(data)

        return u_phases

    def estimate(self, data: np.ndarray, **kwargs) -> np.ndarray:
        rois = kwargs["rois"]
        samples = kwargs["samples"]

        # Cartesian product of all ROIs.
        tmp = list(range(rois))
        rois_pairs = list(itertools.product(*[tmp, tmp]))

        ts = np.zeros((rois, rois, samples), dtype=np.complex)
        avg = np.zeros((rois, rois))

        for pair in rois_pairs:
            u_phases1, u_phases2 = data[pair,]
            ts_plv = np.exp(1j * (u_phases1 - u_phases2))
            avg_plv = np.abs(np.sum((ts_plv))) / float(samples)

            ts[pair] = ts_plv
            avg[pair] = avg_plv

        return avg
