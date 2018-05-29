from sklearn.externals import joblib

class Detector(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def load(self, path=None):
        if path:
            self.search = joblib.load(path)
        else:
            model = self.cfg.instance(self.cfg.CLASSIFIER)
            cross_validation = self.cfg.instance(self.cfg.CV)
            self.search = self.cfg.instance(self.cfg.SEARCH, model, cv=cross_validation)

    def save(self, path):
        joblib.dump(self.search, path)

    ## TODO: Replace with specifing class inside config
    ## Keras
    ## TensorFlow
    def teach(self, data_set):
        # cross_validation = self.cfg.instance(self.cfg.CV)
        # search = self.cfg.instance(self.cfg.SEARCH, self.model, cv=cross_validation)
        self.search.fit(data_set.x, data_set.y)
        return self.search

    def detect(self, to_classify):
        return self.search.predict(to_classify)
