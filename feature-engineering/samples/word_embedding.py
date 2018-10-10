from gensim.models import Word2Vec

def word_embedding(corpus):
    """Construct the word embedding model for a given corpus.

    :param corpus: List of sentences.
    :returns: Word2Vec model.
    """
    sentences = [[x for x in t.split()] for t in corpus]
    return Word2Vec(sentences, min_count = 1)


if __name__ == '__main__':
    sample_corpus = [
        "data science",
        "jeury data science analytic",
        "machine learning",
        "deep learning"
    ]

    model = word_embedding(sample_corpus)

    print(model)
    print(model.similarity('data', 'science'))
    print(model['learning'])
