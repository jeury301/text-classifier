def noise_removal_w_list(input_text):
    """Removing noise from text using a list of noise words.
    :param input_text: Noisy text.
    :return: Clean text.
    """
    # noise to be removed
    noise_words = ["is", "a", "this", "..."]
    # converting sentence into words
    words = input_text.split()
    # noise-free words
    noise_free_words = [word for word in words if word not in noise_words]
    # building noise-free text
    return " ".join(noise_free_words)

def noise_removal_w_regex(input_text):
    """Removing noise from using using regular expression.
    :param input_text: Noisy text.
    :return: Clean text.
    """
    import re

    # pattern to remove hashtagged words eg. #this
    r_pattern = "#[\w]*"
    # matches iterator
    matches = re.finditer(r_pattern, input_text)

    for i in matches:
        # removing each match from original input text
        input_text = re.sub(i.group().strip(),'', input_text)

    # removing inner extra spaces
    return re.sub(' +',' ',input_text)

if __name__ == '__main__':
    while True:
        text = input("> ")
        print("noise-removal-with-list", noise_removal_w_list(text))
        print("noise-remove-with-regex", noise_removal_w_regex(text))
