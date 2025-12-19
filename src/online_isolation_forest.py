from sklearn.ensemble import IsolationForest
from collections import deque

class OnlineIForest:
    def __init__(self, window_size=500):
        self.buffer = deque(maxlen=window_size)
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.01,
            random_state=42
        )

    def fit_initial(self, X):
        self.buffer.extend(X)
        self.model.fit(X)

    def score(self, x):
        return self.model.decision_function([x])[0]

    def update(self, x):
        self.buffer.append(x)
        self.model.fit(list(self.buffer))

