from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn import svm
from loader import load_data

def train_classifier(training_corpus):
    """Building SVM Classifier model.

    :param training_corpus: List of training tuples containing prhase and class.
    :returns: SVM model.
    """
    print("Training model...")

    train_data = []
    train_labels = []
    for row in training_corpus:
        train_data.append(row[0])
        train_labels.append(row[1])

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.9)
    # Train the feature vectors
    train_vectors = vectorizer.fit_transform(train_data)
    # Perform classification with SVM, kernel=linear
    model = svm.SVC(kernel='linear')
    return model, train_vectors, train_labels

if __name__ == '__main__':
    trainig_data = load_data('../../datasets/even_odd.csv')
    model, train_v, train_l = train_classifier(trainig_data)
    model.fit(train_v, train_l)

    while True:
        text = input("> ")
        print("class", model.predict([text]))
