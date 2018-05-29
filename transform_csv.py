import argparse
import pandas as pd
from vad import split_string
    
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-file', dest='input_file', metavar='input .csv file', nargs='?', type=str, default=None)
parser.add_argument('-o','--output-file', dest='output_file', metavar='output .csv file', nargs='?', type=str, default=None)
args = parser.parse_args()
csv_data_set = pd.read_csv(args.input_file).dropna()
# for url in csv_data_set['source']:
    # url = split_string(url)
csv_data_set['source'] = list(map(split_string, csv_data_set['source']))
csv_data_set.to_csv(args.output_file, columns=['language', 'source'])
