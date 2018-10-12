import fuzzy
import math
from collections import Counter

def get_cosine(vec1, vec2):
    """Computing cosine similarities between 2 vectors.

    Code from: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

    :param vec1: Vector representation of first string.
    :param vec2: Vector representation of second string.
    :returns: COSINE SIMILARITY
    """
    common = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in common])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = text.split()
    return Counter(words)

def phonetic_matching(s1, s2):
    """Computing the phonetic sound of 2 strings and using LD to compute its
    similarity.

    :param s1: First string.
    :param s2: A second string.
    :returns: The LD between the 2 string phonetic representations.
    """
    soundex = fuzzy.Soundex(4)
    return levenshtein_distance(soundex(s1),soundex(s2))

def levenshtein_distance(s1, s2):
    """Computing the Levenshtein Distance between two strings.

    The Levenshtein Distance consists of the minimum number of edits needed to
    transform one string into the other.

    Code from: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

    :param s1: First string.
    :param s2: A second string.
    :returns: The LD between the 2 strings.
    """
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                    distances[index1+1], newDistances[-1])))
        distances = newDistances
    return distances[-1]

if __name__ == '__main__':
    while True:
        s1 = input("> Enter string 1: ")
        s2 = input("> Enter string 2: ")

        print("LD Phonetic Distance", phonetic_matching(s1, s2))
        print("Cosine similarity", get_cosine(text_to_vector(s1), text_to_vector(s2)))
