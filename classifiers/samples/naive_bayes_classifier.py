from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
import json
import csv

def load_data(path):
    """Loads data from csv file.

    :param path: Path to file.
    :returns: List of tuples containing the training data
    """
    data = []

    with open(path, 'r') as dt:
        d_csv = csv.reader(dt, delimiter=',')
        for row in d_csv:
            data.append((row[1],row[0]))

    return data[1:]

def train_classifier(training_corpus):
    """Building Naive Bayes Classifier model.

    :param training_corpus: List of training tuples containing prhase and class.
    :returns: Navie Bayes Classifier model.
    """
    print("Training model...")
    return NBC(training_corpus)

if __name__ == '__main__':
    trainig_data = load_data('../../datasets/even_odd.csv')
    model = train_classifier(trainig_data)

    while True:
        text = input("> ")
        print("class: ", model.classify(text))
