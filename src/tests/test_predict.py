import os.path
import unittest

from src.predict import Predictor


class PredictTest(unittest.TestCase):
    def test_prediction(self):
        predictor = Predictor()
        assert predictor.predict_test_data() > 0.5


if __name__ == '__main__':
    unittest.main()
