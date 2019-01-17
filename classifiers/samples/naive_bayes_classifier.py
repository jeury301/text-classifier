from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
from loader import load_data
import json

def train_classifier(training_corpus):
    """Building Naive Bayes Classifier model.

    :param training_corpus: List of training tuples containing prhase and class.
    :returns: Navie Bayes Classifier model.
    """
    print("Training model...")
    return NBC(training_corpus)

if __name__ == '__main__':
    training_data = load_data('../../datasets/even_odd.csv')
    model = train_classifier(training_data)

    while True:
        text = input("> ")
        print("class: ", model.classify(text))
