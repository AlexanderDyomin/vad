import sys

from sklearn.model_selection import GridSearchCV, ShuffleSplit

from vad import DataSet, Config, Detector

# SQLMap - useful tool
def foo():
    config = Config('config.json')
    detector = Detector(config)
    detector.load()
    data_set = DataSet(sys.argv[1], config)
    search = detector.teach(data_set)
    print('Best parameters:', search.best_params_)
    print('Best score:',      search.best_score_)

# TODO: Datasets
# Tune network
# true positive/negative, other metrics
# CLI
# Error function plot during education

if __name__ == '__main__':
    foo()
    #path = sys.argv[1]
    #teach(path, 'model_dump')
