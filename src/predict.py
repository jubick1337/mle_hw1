import configparser
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

    def predict_test_data(self):
        test_data = pd.read_csv(
            self.config["DATA"]["test"], header=None).dropna()
        X_test = test_data.drop(2500, axis=1)
        y_test = test_data[2500].astype(int)
        logging.info(f'Got score of {self.classifier.score(X_test, y_test)}')


if __name__ == '__main__':
    predictor = Predictor()
    predictor.predict_test_data()
