from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer(object):
    def __init__(self, config):
        self.config = config
        
    def load(self, path=None):
        if path:
            self.vectorizer = joblib.load(path)
        else:
            self.vectorizer = self.config.instance(self.config.VECTORIZER)
            #self.vectorizer = TfidfVectorizer(analyzer = "word",
            #ngram_range = [1, 1],
            #token_pattern = "\\s.+\\s",
			#preprocessor = lambda x: x.strip())
            
    def save(self, path):
        joblib.dump(self.vectorizer, path)
        
    def fit(self, documents):
        self.vectorizer.fit(documents)
    
    def transform(self, documents):
        return self.vectorizer.transform(documents)
    def set_params(**params):
        return self.vectotizer.set_params(**params)
