from gensim import models
from gensim import corpora
import json

def topic_modeling(corpus):
    """Implementation of Latent Dirichlet Allocation (LDA). In a list of words.

    LDA automatically identifies topics found in a text corpus. We are using
    nltk's corpora to build the dictionary and the gensim library to build the
    LDA model.

    :param corpus: List of sentences which are part of the text corpus.
    :return: A trained LDA model for topic identification.
    """
    # creating a dictionray from corpus
    # this is a super powerful dictionary object from gensim corpora
    dictionary = corpora.Dictionary(corpus)

    # creating bag of words from corpus
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]

    # LDA model
    Lda = models.ldamodel.LdaModel

    # running and training the model
    ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

    return ldamodel

if __name__ == '__main__':
    doc1 = ("Sugar is bad to consume. My sister likes to have sugar, "
        "but not my father.")
    doc2 = ("My father spends a lot of time driving my sister "
        "around to dance practice.")
    doc3 = ("Doctors suggest that driving may cause increased stress "
        "and blood pressure.")
    doc_complete = [doc1, doc2, doc3]
    corpus = [doc.split() for doc in doc_complete]

    print(json.dumps(topic_modeling(corpus).print_topics(), indent=4))
