def look_up_words(input_text):
    """Replacing social media slangs with more standarized words.
    
    :param input_text: Slanged social media text.
    :return: Standarized text.
    """

    # look-up dictionary
    social_media_look_up = {
        'rt':'Retweet',
        'dm':'direct message',
        "awsm" : "awesome",
        "luv" :"love"
    }

    # words in sentence
    words = input_text.split()
    # standarize each word using look-up table
    return " ".join([social_media_look_up.get(word.lower(),word) for word in words])

if __name__ == '__main__':
    while True:
        text = input("> ")
        print("standarized-text",look_up_words(text))
