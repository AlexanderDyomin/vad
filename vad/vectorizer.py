from sklearn.externals import joblib

class Vectorizer(object):
    def __init__(self, config):
        self.config = config
        
    def load(self, path=None):
        if path:
            self.vectorizer = joblib.load(path)
        else:
            self.vectorizer = self.config.instance(self.config.VECTORIZER)
            
    def save(self, path):
        joblib.dump(self.vectorizer, path)
        
    def fit(self, documents):
        self.vectorizer.fit(documents)
    
    def transform(self, documents):
        return self.vectorizer.transform(documents)