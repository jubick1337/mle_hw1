import configparser
import logging
import os.path

import numpy as np
import pandas as pd
import tqdm
from PIL import Image

logging.basicConfig(level=logging.INFO)


class DataProcessor:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.getcwd(), 'config.ini')
        self.config.read(self.config_path)
        self.raw_data_path = os.path.join(os.getcwd() + '/' + self.config['DATA']['raw_data'])
        self.images_dir = os.path.join(os.getcwd() + '/' + self.config['DATA']['images_dir'])

        self.train_csv = self.config['DATA']['train']
        self.test_csv = self.config['DATA']['test']

    def process_data(self):
        df = pd.read_csv(self.raw_data_path, delim_whitespace=True, header=1)
        smiling = df['Smiling'].dropna()
        smiling = (smiling + 1) / 2
        smiling = smiling.dropna()
        dataset = []
        for img_index, label in tqdm.tqdm(
                zip(smiling.index[:1001], smiling[:1001])):  # We're using only 1000 images due to lack of RAM
            img = np.asarray(Image.open(f'{self.images_dir}{img_index}'))
            dataset.append(np.append(
                img[img.shape[0] // 2: img.shape[0] // 2 + 50, img.shape[1] // 2: img.shape[1] // 2 + 50, :].mean(
                    -1) / 255, label))
        logging.info(f'Saving train data at {self.train_csv}')
        self.save_data(dataset, True)
        logging.info(f'Saving test data at {self.test_csv}')
        self.save_data(dataset, False)

    def save_data(self, data, is_train: bool):
        if is_train:
            with open(self.train_csv, 'w') as f:
                for d in tqdm.tqdm(data[:900]):
                    f.write(','.join(["{:.3f}".format(x) for x in d]).strip() + '\n')
        else:
            with open(self.test_csv, 'w') as f:
                for d in tqdm.tqdm(data[901:]):
                    f.write(','.join(["{:.3f}".format(x) for x in d]).strip() + '\n')


if __name__ == "__main__":
    data_processor = DataProcessor()
    data_processor.process_data()
