import argparse

from vad import DataSet, Config, Detector

def process_args():
    parser = argparse.ArgumentParser(description='Detector of vulnerabilities')
    parser.add_argument('config', metavar='config', nargs='?', type=str, default='config.json')
    parser.add_argument('-d', '--dataset', dest='dataset', type=str)
    parser.add_argument('-l', '--load', dest='load', type=str, default=None)
    parser.add_argument('-s', '--save', dest='save', type=str, default=None)
    return parser.parse_args()

# TODO: Datasets
# SQLMap - useful tool
# Tune network
# true positive/negative, other metrics
# CLI
# Error function plot during education

if __name__ == '__main__':
    args = process_args()
    cfg = Config(args.config)
    detector = Detector(cfg)
    detector.load(args.load)
    if args.dataset:
        data_set = DataSet(args.dataset, cfg)
        search = detector.teach(data_set)
        print('Best parameters:', search.best_params_)
        print('Best score:',      search.best_score_)
    # TODO: Prediction
    if args.save:
        detector.save(args.save)
