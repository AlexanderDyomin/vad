import json

class Config(object):
    def __init__(self, path):
        with open(path, 'r') as js:
            self._json = json.load(js)

    def __getitem__(self, key):
        return self._json[key]
