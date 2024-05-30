from csv import DictReader
from typing import Dict


IMAGES_PATH = 'data/images'
LABELS_PATH = 'data/labels.csv'


class DataHandler:
    def __init__(self, images_path = IMAGES_PATH, labels_path = LABELS_PATH):
       self._images_path = images_path
       self._labels = self._init_labels(labels_path)

    def _init_labels(self, labels_path) -> Dict:
        labels_dict = {}
        reader = DictReader(open(labels_path))
        for row in reader:
            labels_dict[row['Image Index']] = row['Finding Labels'].split('|')

        return labels_dict

    
d = DataHandler()
print(d._labels)