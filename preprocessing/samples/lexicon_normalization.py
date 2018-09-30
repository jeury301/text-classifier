from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def stemming(word):
    """Stemming aka stripping the suffixes (“ing”, “ly”, “es”, “s” etc)
    from a word.

    We make use of the PorterStemmer from nltk.
    
    :param word: Word to stem.
    :return: Stemmed word.
    """
    stem = PorterStemmer() # stemmer object
    return stem.stem(word)

def lemmatization(word):
    """Obtaining the root form of the word.

    We make use of the WordNetLemmatizer from nltk.
    :param word: Word to be lemmatized aka to find root.
    :return
    """
    lem = WordNetLemmatizer() # lemmatizer object
    return lem.lemmatize(word, "v")

if __name__ == '__main__':
    while True:
        words = input("> ").split()
        stems = [stemming(word) for word in words] # finding stems
        roots = [lemmatization(word) for word in words] # finding roots

        print("stems", " ".join(stems))
        print("roots", " ".join(roots))
