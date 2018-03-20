import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

class DataSet(object):
    def __init__(self, csv_file, *args, **kwargs):
        self.data_set = pd.read_csv(csv_file).dropna()
        # analyzer = "word", ngram_range=(1, 4)
        vectorizer = TfidfVectorizer(*args, **kwargs)
        self.x = vectorizer.fit_transform(self.data_set['source'])
        self.y = self.data_set['language']
