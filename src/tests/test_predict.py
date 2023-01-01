import unittest

from src.predict import Predictor


class PredictTest(unittest.TestCase):
    def test_prediction(self):
        predictor = Predictor()
        assert predictor.predict_test_data() > 0.5  # we want model to be at least better than random


if __name__ == '__main__':
    unittest.main()
