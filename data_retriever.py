import csv
import pandas as pd

header_names = ['id', 'title', 'text', 'labels']
training_data = pd.read_csv('training_data.tsv', sep='\t', names=header_names)

sample_data = training_data.head(50000)
sample_data.to_csv('sample_data.csv',index=False)