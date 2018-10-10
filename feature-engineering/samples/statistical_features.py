from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tf_idf(corpus):
    """Computing term frequency (tf) - inverse document frequency (idf).

    :param corpus: List of documents.
    :returns: tf-idf of corpus.
    """
    return TfidfVectorizer().fit_transform(corpus)

if __name__ == '__main__':
    sample_corpus =  [
        'This is sample document.',
        'another random document.',
        'third sample document text'
    ]

    print(compute_tf_idf(sample_corpus))
