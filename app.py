"""Flask App. Section 5 of Tweet Gen"""

from clean_up import clean_file
from flask import Flask
from histogram import make_histogram_from
from dictogram import Dictogram
from sampling import random_words
from markov import nth_order_markov_model, generate_random_sentence_n
import json


app = Flask(__name__)


@app.route('/')
def random_sentence():
    # text = clean_text_in("fish.txt").split()
    # print(type(text.split()), "======")
    # histogram = make_histogram_from(text)
    # dictogram = Dictogram(text)

    # print(dictogram)

    # weights = sampling.get_word_weights(histogram)
    # word_dict = random_words(20, histogram)

    # sentence = " ".join(word_dict.keys())
    # markov = markov_chain_from("alan-watts.txt")
    # response = json.dumps(markov)
    # print(markov)
    word_list = clean_file("alan-watts.txt")

    markov = nth_order_markov_model(2, word_list)
    random_tweet = generate_random_sentence_n(240, markov)

    return(random_tweet, 200, None) 

if __name__ == '__main__':
    app.run()