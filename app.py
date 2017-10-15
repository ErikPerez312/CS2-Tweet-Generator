"""Flask App. Section 5 of Tweet Gen"""

from text_file_stripper import clean_text_in
from flask import Flask
from histogram import make_histogram_from
import stochastic_sampling


app = Flask(__name__)


@app.route('/sentence')
def random_sentence():
    text = clean_text_in("alan-watts.txt")
    histogram = make_histogram_from(text)
    weights = stochastic_sampling.get_word_weights(histogram)
    word_dict = stochastic_sampling.random_words(20, weights)

    sentence = " ".join(word_dict.keys())
    return sentence
