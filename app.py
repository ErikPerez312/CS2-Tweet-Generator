"""Flask App. Section 5 of Tweet Gen"""

from clean_up import clean_text_in
from flask import Flask
from histogram import make_histogram_from
from sampling import random_words


app = Flask(__name__)


@app.route('/sentence')
def random_sentence():
    text = clean_text_in("alan-watts.txt")
    histogram = make_histogram_from(text)
    # weights = sampling.get_word_weights(histogram)
    word_dict = random_words(20, histogram)

    sentence = " ".join(word_dict.keys())
    return sentence
