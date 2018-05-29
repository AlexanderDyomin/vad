import pandas as pd

class DataSet(object):
    def __init__(self, csv_data_set, vectorizer):
        self.data_set = csv_data_set
        # vectorizer = config.instance(config.VECTORIZER)
        self.x = vectorizer.transform(self.data_set['source'])
        self.y = self.data_set['language']
