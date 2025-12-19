import numpy as np

class StatisticalBaseline:
    def __init__(self, alpha=0.01):
        self.alpha = alpha
        self.mean = None
        self.std = None

    def initialize(self, X):
        self.mean = X.mean()
        self.std = X.std().clip(lower=0.01)

    def score(self, x, cap=10):
        z = (x - self.mean) / self.std
        z = z.clip(-cap, cap)
        return z, (abs(z) > 3).any()

    def update(self, x):
        self.mean = self.alpha * x + (1 - self.alpha) * self.mean


