
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import string

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data = pd.read_csv('Tweets.csv')
data = data[['airline_sentiment', 'negativereason', 'airline', 'text']]

stopwords_file = 'stopwords.txt'
def load_stopwords(stopwords_file):
    stopwords = []
    fr = open(stopwords_file)
    for line in fr.readlines():
        lines = line.strip().split('\t')
        stopwords.append(lines[0])
    fr.close()
    return stopwords

stopwords = load_stopwords(stopwords_file)
#stemmer = PorterStemmer()

def sentence_stemmer(text):
    stemmed = []
    for word in text:
        if word not in stopwords:
            stemmed.append(word)
    return stemmed 

def recorganize(text):
    sentence = word_tokenize(text)
    stem_words = sentence_stemmer(sentence)
    #stem_words = stopwords_remove(text)
    return ' '.join(stem_words)

intab = string.punctuation
outtab = '                                '
transtab = string.maketrans(intab,outtab)

def analyseText(text):
    text = text.lower()
    text = text.translate(transtab)
    text = recorganize(text)
    return text

positive = data[data['airline_sentiment'] == 'positive']
negative = data[data['airline_sentiment'] == 'negative']

text_positive = positive['text'].map(lambda x:re.sub(r'^\@\w+',"",x))
text_positive = text_positive.map(analyseText)

text_negative = negative['text'].map(lambda x:re.sub(r'^\@\w+',"",x))
text_negative = text_negative.map(analyseText)

positive_file = "/home/yinhao/scripts/fp_growth/positive.txt"
negative_file = "/home/yinhao/scripts/fp_growth/negative.txt"

with open(positive_file,'w+') as f1:
    for line_pre in list(text_positive):
        lines = re.split(r'\t',line_pre.strip())
        temp = []
        for line_post in lines:
            if line_post not in temp:
                temp.append(line_post)
        for i in temp:
            f1.write(str(i))
        f1.write('\n')
    f1.close()

with open(negative_file,'w+') as f1:
    for line_pre in list(text_negative):
        lines = re.split(r'\t',line_pre.strip())
        temp = []
        for line_post in lines:
            if line_post not in temp:
                temp.append(line_post)
        for i in temp:
            f1.write(str(i))
        f1.write('\n')
    f1.close()

