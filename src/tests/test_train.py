import os.path
import unittest

from src.train import SmileClassifier


class TrainTest(unittest.TestCase):
    def test_model_training(self):
        model = SmileClassifier()
        assert os.path.exists(model.train_model())


if __name__ == '__main__':
    unittest.main()
