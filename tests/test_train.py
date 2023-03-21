import unittest

from sklearn.datasets import make_classification
from lab.processing.train.train import RandomForestTrainer


class TestRandomForestTrainer(unittest.TestCase):
    def test_fit(self):
        X, y = make_classification(n_samples=100, n_features=5, random_state=0)
        model = RandomForestTrainer(n_estimators=10, random_state=0, class_weight="balanced", n_jobs=-1)
        model.fit(X, y)
        self.assertIsNotNone(model.clf)


if __name__ == '__main__':
    unittest.main()