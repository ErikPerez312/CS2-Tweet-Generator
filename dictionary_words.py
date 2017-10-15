"""Extract text from a file and generated random sentence."""

import random
import sys


def extract_text():
    """Extract text from hard coded file path."""
    file_path = "/usr/share/dict/words"

    file = open(file_path)
    text = list(file)
    file.close()

    return text


def make_random_sentence(count):
    """Returns string of random words with length being the count parameter."""
    text = extract_text()
    words = list()

    for index in range(int(count)):
        random_index = random.randint(0, len(text) - 1)
        stript_word = text[random_index].strip("\n")
        words.append(stript_word)

    string_of_words = " ".join(words) + "."
    print(string_of_words)
    return string_of_words


if __name__ == '__main__':
    make_random_sentence(sys.argv[1])
