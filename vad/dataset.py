import pandas as pd

class DataSet(object):
    def __init__(self, csv_file, config):
        self.data_set = pd.read_csv(csv_file).dropna()
        vectorizer = config.instance(config.VECTORIZER)
        self.x = vectorizer.fit_transform(self.data_set['source'])
        self.y = self.data_set['language']
