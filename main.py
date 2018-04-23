import argparse
import pandas as pd
from vad import *

def process_args():
    parser = argparse.ArgumentParser(description='Detector of vulnerabilities')
    parser.add_argument('config', metavar='config', nargs='?', type=str, default='config.json')
    parser.add_argument('--link', metavar='URL to recognize an attack type', nargs='?', type=str, default=None)
    parser.add_argument('-d', '--dataset', dest='dataset', type=str)
    parser.add_argument('-l', '--load', dest='load', type=str, default=None)
    parser.add_argument('-s', '--save', dest='save', type=str, default=None)
    parser.add_argument('--vectorizer', type=str, default=None)
    parser.add_argument('--save-vectorizer', dest='save_vectorizer', type=str, default=None)
    parser.add_argument('--test', dest='test', type=str, default=None)
    return parser.parse_args()
    
def predict(vectorizer, url_string):
    splitted_string = split_string(url_string)
    word_matrix = vectorizer.transform([splitted_string])
    search = detector.detect(word_matrix)
    return str(search[0])

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
        # splitted_string = split_string(args.link)
        # word_matrix = vectorizer.transform([splitted_string])
        # search = detector.detect(word_matrix)
        search = predict(vectorizer, args.link)
        print('Predicted class:', search)
    if args.test:
        test_data_set = pd.read_csv(args.test).dropna()
        known_classes = test_data_set['language']
        predicted_classes = []
        true_pos = 0
        true_neg = 0
        false_pos = 0
        false_neg = 0
        for url in test_data_set['source']:
            predicted_classes.append(predict(vectorizer, url))
        for predicted, known in zip(predicted_classes, test_data_set['language']):
            if (known == 'normal' and predicted == known):
                true_neg += 1
            elif(predicted == known):
                true_pos += 1
            elif(known == 'normal' and predicted != known):
                false_neg += 1
            else:
                false_pos += 1
        sum = true_pos + true_neg + false_pos + false_neg
        print('True positive:', true_pos, 'of total', sum, 'it\'s equals', true_pos / sum)
        print('False positive:', false_pos, 'of total', sum, 'it\'s equals', false_pos / sum)
        print('True negative:', true_neg, 'of total', sum, 'it\'s equals', true_neg / sum)
        print('False negative:', false_neg, 'of total', sum, 'it\'s equals', false_neg / sum)
    if args.save:
        detector.save(args.save)
    if(args.save_vectorizer):
        vectorizer.save(args.save_vectorizer)
