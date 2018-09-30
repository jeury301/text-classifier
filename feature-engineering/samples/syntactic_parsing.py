from nltk import word_tokenize, pos_tag

def speech_tag(input_text):
    """Defining the usage and the function of each word in the sentence.

    Using nltk's 'pos_tag' to generate the spech_tagging for a given input text.
    
    :param input_text: Original input.
    :return: List of tags for each word in the input sentence.
    """
    tokens = word_tokenize(input_text) # tokens from sentence
    return pos_tag(tokens) # generating tags from tokens

if __name__ == '__main__':
    while True:
        text = input("> ")
        print("speech_tag", speech_tag(text))
