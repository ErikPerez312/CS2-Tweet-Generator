"""Doc string."""

from clean_up import clean_text_in
from pprint import pprint
from sys import argv
import histogram
import random


def random_words(word_count, histogram):
    """Returns dict containing random words & number of times it was chosen."""
    # Dict will hold random word and number of times that word was chosen.
    chosen_words = dict()

    weights = get_word_weights(histogram)
    # Adds number(WORD_COUNT) of random words to the CHOSEN_WORDS dict.
    for i in range(0, word_count):
        random_float = random.random()
        cumulative_probability = 0.0
        for (word, word_weight) in weights.items():
            # computing the increasing cumulative probability
            cumulative_probability += word_weight
            # until the cumulative_probability becomes greater than random_int
            if random_float < cumulative_probability:
                if word not in chosen_words:
                    chosen_words[word] = 1
                else:
                    chosen_words[word] += 1
                break
    # pprint(chosen_words)
    return chosen_words


def get_word_weights(histogram):
    """Returns dict with words in histogram and their corresponding weight."""
    weights = dict()
    total_values = sum(histogram.values())

    for key, value in histogram.items():
        weight = float(value) / total_values
        weights[key] = weight
        # print(key, value, weights[key])
        # print("sumtype", type(sum(histogram.values())))

    return weights

# testpy


if __name__ == '__main__':
    filename = argv[1:]
    text = clean_text_in(filename[0])
    fish = {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1}
    # histogram = histogram.make_histogram_from(sys.argv[1])
    # weights = word_weights(histogram)
    histo = histogram.make_histogram_from(text)
    # weights = get_word_weights(histo)
    print(random_words(20000, histo))
