import argparse
import configparser
import json
import logging
import os.path
import pickle

import pandas as pd

logging.basicConfig(level=logging.INFO)


class Predictor:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.getcwd(), 'config.ini')
        self.config.read(self.config_path)
        with open(os.path.join(os.path.join(os.getcwd(), 'experiments'),
                               self.config['EXPERIMENT']['model_path'][1:]), 'rb') as model_file:
            self.classifier = pickle.load(model_file)

    def predict(self, data):
        return self.classifier.predict(data)

    def predict_test_data(self) -> int:
        test_data = pd.read_csv(
            self.config["DATA"]["test"], header=None).dropna()
        X_test = test_data.drop(2500, axis=1)  # 2500 is 50x50 patch and 2501 is a label
        y_test = test_data[2500].astype(int)
        res = self.classifier.score(X_test, y_test)
        logging.info(f'Got score of {res}')
        return res

    def func_test(self):
        tests_path = os.path.join(os.getcwd(), "tests")
        for test in os.listdir(tests_path):
            with open(os.path.join(tests_path, test)) as f:
                data = json.load(f)
                X = (
                    pd.json_normalize(data, record_path=['X']))
                y = pd.json_normalize(data, record_path=['y'])
                score = self.classifier.score(X, y)
                print(f'{self.classifier} has {score} score')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--func", action="store_true", help="if specified will run func tests")
    args = parser.parse_args()
    predictor = Predictor()
    predictor.predict_test_data()
    if args.func:
        predictor.func_test()
