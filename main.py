from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble

import pandas, xgboost, numpy, textblob, string
from pprint import pprint
from keras.preprocessing import text, sequence
from keras import layers, models, optimizers

def load_data():
    # load the dataset
    data = open('data/corpus').read()
    labels, texts = [], []
    for line in data.split("\n"):
        content = line.split()
        labels.append(content[0])
        texts.append(" ".join(content[1:]))
    
    return labels, texts

def build_df(labels, texts):
    # create a dataframe using texts and lables
    df = pandas.DataFrame()
    df['text'] = texts
    df['label'] = labels

    return df

if __name__ == "__main__":
    labels, texts = load_data()
    traindf = build_df(labels, texts)

    pprint(traindf)