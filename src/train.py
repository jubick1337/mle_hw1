import configparser
import logging
import os
import pickle

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

logging.basicConfig(level=logging.INFO)


class SmileClassifier:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.getcwd(), 'config.ini')
        self.config.read(self.config_path)
        self.train_data = pd.read_csv(
            self.config["DATA"]["train"], header=None).dropna()
        self.X_train = self.train_data.drop(2500, axis=1)
        self.y_train = self.train_data[2500].astype(int)
        self.test_data = pd.read_csv(
            self.config["DATA"]["test"], header=None).dropna()
        self.X_test = self.test_data.drop(2500, axis=1)
        self.y_test = self.test_data[2500].astype(int)
        self.model_path = os.path.join(os.path.join(os.getcwd(), 'experiments'), 'model.pkl')
        self.hyperparams = dict(self.config["HYPERPARAMS"])
        self.hyperparams['learning_rate'] = float(self.hyperparams['learning_rate'])
        self.hyperparams['max_depth'] = int(self.hyperparams['max_depth'])
        self.hyperparams['n_estimators'] = int(self.hyperparams['n_estimators'])
        self.hyperparams['random_state'] = int(self.hyperparams['random_state'])
        self.hyperparams['max_features'] = self.hyperparams['max_features'][1:-1]

    def train_model(self):
        logging.info(f'Model being trained with parameters: {self.hyperparams}')
        classifier = GradientBoostingClassifier(**self.hyperparams)
        classifier.fit(self.X_train, self.y_train)
        self.save_model(classifier, self.model_path)
        logging.info(f'Model saved to {self.model_path}')

    @staticmethod
    def save_model(classifier, path: str):
        with open(path, 'wb') as f:
            pickle.dump(classifier, f)


if __name__ == "__main__":
    model = SmileClassifier()
    model.train_model()
