import argparse
import pandas as pd
from vad import *
from sklearn.metrics import classification_report

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
    lower_string = url_string.lower()
    splitted_string = split_string(lower_string)
    print(splitted_string)
    word_matrix = vectorizer.transform([splitted_string])
    search = detector.search.predict(word_matrix)
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
    vectorizer.vectorizer.set_params(preprocessor=lambda x: x.strip())
    if args.dataset:
        csv_data_set = pd.read_csv(args.dataset).dropna()
        csv_data_set['source'] = list(map(lambda x: x.lower(), csv_data_set['source']))
        csv_data_set['source'] = list(map(split_string, csv_data_set['source']))
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
        # attack = 0
        # normal = 0
        # true_pos = 0
        # true_neg = 0
        # false_pos = 0
        # false_neg = 0
        # for known_class in test_data_set['language']:
            # if known_class == 'normal':
                # normal += 1
            # else:
                # attack += 1
        for url in test_data_set['source']:
            predicted_classes.append(predict(vectorizer, url))
        # for predicted, known in zip(predicted_classes, test_data_set['language']):
            # if (known == 'normal' and predicted == known):
                # true_neg += 1
            # elif(predicted == known):
                # true_pos += 1
            # elif(known == 'normal' and predicted != known):
                # false_neg += 1
            # else:
                # false_pos += 1
        # sum = true_pos + true_neg + false_pos + false_neg
        # precision = true_pos / (true_pos + false_pos)
        # recall = true_pos / (true_pos + false_neg)
        # print('True positive:', true_pos, 'of total', attack, 'it\'s equals'
            # , true_pos / attack if attack > 0 else 0)
        # print('False positive:', false_pos / normal if normal > 0 else 0)
        # print('True negative:', true_neg, 'of total', normal, 'it\'s equals'
            # , true_neg / normal if normal > 0 else 0)
        # print('False negative:', false_neg / attack if attack > 0 else 0)
        # print('Pecision:', precision)
        # print('Recall:', recall)
        print(classification_report(known_classes, predicted_classes))
    if args.save:
        detector.save(args.save)
    if(args.save_vectorizer):
        vectorizer.vectorizer.set_params(preprocessor=None)
        vectorizer.save(args.save_vectorizer)
