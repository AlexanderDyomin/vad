from sklearn.neural_network  import MLPClassifier
from sklearn.externals       import joblib

Model = MLPClassifier

def __save(self, path):
    joblib.dump(self, path)

def __load(path):
    return joblib.load(path)

Model.save = __save
Model.load = __load
