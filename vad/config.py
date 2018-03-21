import json
from importlib import import_module

class Config(object):
    # Available classes
    VECTORIZER = "vectorizer"
    CLASSIFIER = 'classifier'
    CV = 'cross-validation'
    SEARCH = 'search'

    def __init__(self, path):
        with open(path, 'r') as js:
            self._json = json.load(js)

    def __getitem__(self, key):
        return self._json[key]

    def instance(self, key, *args, **kwargs):
        obj = self[key]
        mod, cls = obj['class']
        module = import_module(mod)
        constructor = getattr(module, cls)
        cargs, ckwargs = [], {}
        if 'args' in obj:
            cargs = obj['args']
        if 'kwargs' in obj:
            ckwargs = obj['kwargs']
        return constructor(
            *(list(args) + cargs),
            **dict(kwargs, **ckwargs)
        )
