
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
import string

input_data = pd.read_csv('training_data_cleaned.csv')

# Split the words and flatten the list
split_words = input_data['text'].str.split(' ').explode()

# Count the frequency of each unique word
frequency = split_words.value_counts()
print(frequency)

frequency.to_csv('frequency.csv')