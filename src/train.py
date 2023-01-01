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
        self.model_path = os.path.join(os.path.join(os.getcwd(), 'experiments'),
                                       self.config['EXPERIMENT']['model_path'][1:])
        self.hyperparams = dict(self.config["HYPERPARAMS"])
        self.hyperparams['learning_rate'] = float(
            self.hyperparams['learning_rate'])  # casting hyperparams to needed type
        self.hyperparams['max_depth'] = int(self.hyperparams['max_depth'])  # casting hyperparams to needed type
        self.hyperparams['n_estimators'] = int(self.hyperparams['n_estimators'])  # casting hyperparams to needed type
        self.hyperparams['random_state'] = int(self.hyperparams['random_state'])  # casting hyperparams to needed type
        self.hyperparams['max_features'] = self.hyperparams['max_features'][1:-1]  # casting hyperparams to needed type

    def train_model(self) -> str:
        """
        Method to train model for our dataset
        :return: path to model
        """
        logging.info(f'Model being trained with parameters: {self.hyperparams}')
        classifier = GradientBoostingClassifier(**self.hyperparams)
        classifier.fit(self.X_train, self.y_train)
        self.save_model(classifier, self.model_path)
        logging.info(f'Model saved to {self.model_path}')
        return self.model_path

    @staticmethod
    def save_model(classifier, path: str):
        """
        Method to dump model into file
        :param classifier: model to save
        :param path: path to save to
        :return:
        """
        with open(path, 'wb') as f:
            pickle.dump(classifier, f)


if __name__ == "__main__":
    model = SmileClassifier()
    model.train_model()
