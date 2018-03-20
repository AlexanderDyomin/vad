import sys

from sklearn.model_selection import GridSearchCV, ShuffleSplit

from vad import Model, DataSet, Config

def teach(path, save=None):
    config = Config('config.json')
    # TODO: Replace with specifing class inside config
    data_set = DataSet(path, **config['dataset'])
    cross_validation = ShuffleSplit(**config['validation'])
    model = Model()
    parameters = config['search'].pop('parameters')
    search = GridSearchCV(model, parameters,
            cv=cross_validation, **config['search'])
    search.fit(data_set.x, data_set.y)
    print('Best parameters:', search.best_params_)
    print('Best score:',      search.best_score_)
    if save is not None:
        model.save(save)



if __name__ == '__main__':
    path = sys.argv[1]
    teach(path, 'model_dump')
