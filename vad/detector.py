from sklearn.externals import joblib

class Detector(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def load(self, path=None):
        if path:
            self.model = joblib.load(path)
        else:
            self.model = self.cfg.instance(self.cfg.CLASSIFIER)

    def save(self, path):
        joblib.dump(self.model, path)

    ## TODO: Replace with specifing class inside config
    ## Keras
    ## TensorFlow
    def teach(self, data_set):
        cross_validation = self.cfg.instance(self.cfg.CV)
        search = self.cfg.instance(self.cfg.SEARCH, self.model, cv=cross_validation)
        search.fit(data_set.x, data_set.y)
        return search

    def detect():
        pass
