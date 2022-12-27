from string import punctuation


def load_text(input_file):
    """Load text from a text file and return as a string."""
    with open(input_file, "r") as file:
        text = file.read()
    return text


def clean_text(text):
    """ Lowercase and remove punctuation from a string.""" 
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, " ")
    return text


def count_words(input_file):
    """Count the number of words in a text file."""
    counter = 0
    with open(input_file, "r") as file:
        for line in file:
            counter += 1
    return counter


print(count_words("../zen.txt"))