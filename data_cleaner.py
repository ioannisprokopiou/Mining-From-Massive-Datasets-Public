import string
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

# uncomment the first time you run the code
#nltk.download("stopwords")

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 5000)

sample_data = pd.read_csv('sample_data.csv')

def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

# Remove HTML Tags
sample_data['text'] = sample_data['text'].apply(remove_html_tags)

# Convert to Lowercase
sample_data['text'] = sample_data['text'].apply(lambda x: x.lower())

# Remove punctuations
sample_data['text'] = sample_data['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))

# Remove Stop Words
stop_words = set(stopwords.words('english'))
sample_data['text'] = sample_data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))


# Stemming
porter = PorterStemmer()
sample_data['text_stemmed'] = sample_data['text'].apply(lambda x: ' '.join([porter.stem(word) for word in x.split()]))

sample_data.to_csv('sample_data_cleaned.csv',index=False)
