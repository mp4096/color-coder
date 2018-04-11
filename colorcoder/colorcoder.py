"""Implementation of the color-coder package."""

import numpy as np
import colorsys


class ColorCoder():
    def __init__(self, samples, num_bins=1000):
        if samples.ndim != 2:
            raise ValueError("Samples must be provided in a matrix.")

        self._num_bins = num_bins

        u, _, _ = np.linalg.svd(samples)
        self._mapper = u[:, 0].squeeze()

        sample_scalars = self._mapper.T @ samples
        max = sample_scalars.max()
        min = sample_scalars.min()

        if np.isclose(max, min):
            raise ValueError("Singular data.")

        self._scale = 1.0 / (max - min)
        self._offset = -min / (max - min)

        pdf, _ = np.histogram(
            self._scale * sample_scalars + self._offset,
            bins=self._num_bins,
            range=(0.0, 1.0),
            density=True,
            )
        self._ecdf = np.cumsum(pdf)
        self._ecdf /= self._ecdf[-1]

    def encode_scalar(self, vector):
        x = self._scale * self._mapper.dot(vector) + self._offset
        x *= float(self._num_bins)
        idx = min(max(int(x), 0), self._num_bins - 1)
        return self._ecdf[idx]

    def encode_hue(self, vector, saturation=0.4, value=1.0):
        h = self.encode_scalar(vector)
        s = saturation
        v = value
        return colorsys.hsv_to_rgb(h, s, v)
