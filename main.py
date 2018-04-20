import argparse
import pandas as pd
from vad import DataSet, Config, Detector, Vectorizer

def process_args():
    parser = argparse.ArgumentParser(description='Detector of vulnerabilities')
    parser.add_argument('config', metavar='config', nargs='?', type=str, default='config.json')
    parser.add_argument('--link', metavar='URL to recognize an attack type', nargs='?', type=str, default=None)
    parser.add_argument('-d', '--dataset', dest='dataset', type=str)
    parser.add_argument('-l', '--load', dest='load', type=str, default=None)
    parser.add_argument('-s', '--save', dest='save', type=str, default=None)
    parser.add_argument('--vectorizer', type=str, default=None)
    parser.add_argument('--save-vectorizer', dest='save_vectorizer', type=str, default=None)
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
    vectorizer = Vectorizer(cfg)
    vectorizer.load(args.vectorizer)
    if args.dataset:
        csv_data_set = pd.read_csv(args.dataset).dropna()
        vectorizer.fit(csv_data_set['source'])
        data_set = DataSet(csv_data_set, vectorizer)
        search = detector.teach(data_set)
        print('Best parameters:', search.best_params_)
        print('Best score:',      search.best_score_)
    if args.link:
        word_matrix = vectorizer.transform([args.link])
        search = detector.detect(word_matrix)
        print('Predicted class: ', search)
    if args.save:
        detector.save(args.save)
    if(args.save_vectorizer):
        vectorizer.save(args.save_vectorizer)
