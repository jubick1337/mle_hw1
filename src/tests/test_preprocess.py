import os.path
import unittest

from src.preprocess import DataProcessor


class ProcessorTest(unittest.TestCase):
    def test_data_saving(self):
        data_processor = DataProcessor()
        data_processor.process_data()
        assert os.path.exists(data_processor.train_csv)
        assert os.path.exists(data_processor.test_csv)


if __name__ == '__main__':
    unittest.main()
