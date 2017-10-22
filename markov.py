"""Generates Markov chain dict from contents in text file"""

from clean_up import clean_file
from collections import deque
from dictogram import Dictogram
import sampling
import random
import re

## Markov Chain Code Reference to Alex Dejeu's article and sample code from HackerNoon
## Link: https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71

def nth_order_markov_model(order, word_list):
    """ Creates a higher order markov chain using 'word_list' entry"""
    word_list = word_list
    chain = dict()

    for i in range(len(word_list) - order):
        current_window = tuple(word_list[i: i + order])
        word_following_current_window = word_list[i + order]
        
        if current_window in chain:
            #update current_window's dictogram in chain using dictogram's update method
            chain[current_window].update([word_list[i+order]])
        else:
            # Add new KEY-VALUE pair to 'chain'
            # KEY: 'current_window' iteration, VALUE: Instance of dictogram containing KEY:'word_following_current_window', Value: frequency count.
            chain[current_window] = Dictogram([word_following_current_window])
    return chain

def markov_chain(word_list):
    """Creates first order markov chain from the 'word_list' entry"""

    chain = dict()

    for index in range(len(word_list) - 1):
        current_word = word_list[index]
        following_word = word_list[index + 1]

        if current_word in chain:
            # update current_word dictogram in chain using dictogram's update method.
            chain[current_word].update([following_word])
        else:
            # Add new KEY-VALUE pair to 'chain'
            # KEY: 'current_word' iteration, VALUE: Instance of dictogram containing KEY:'following_word', Value: frequency count.
            chain[current_word] = Dictogram([following_word])
    return chain

def generate_random_start(model):
    # Generate a "valid" starting word. 
    # A valid starting word are words that start a sentene
    if 'END' in model:
        end_word = 'END'
        while end_word == 'END':
            end_word = model['END'].return_weighted_random_word()
        return end_word
    return random.choice(list(model.keys()))


def generate_random_sentence_n(length, markov_model):
    # Length denotes the max amount of characters

    current_window = generate_random_start(markov_model)
    sentence = [current_window[0]]
    tweet = ''

    valid_tweet_flag = True
    sentence_count = 0
    while valid_tweet_flag:
        # We will generate random sentences until we decide we can not any more

        # Dictogram of words that follow window.
        current_dictogram = markov_model[current_window]
        random_weighted_word = current_dictogram.return_weighted_random_word()

        # Create a deque with current_window. (deque is list)
        ## More info on deque: https://docs.python.org/2/library/collections.html#collections.deque
        current_window_deque = deque(current_window)

        # Remove first word from window 
        current_window_deque.popleft() 
        # Append random word to window 
        current_window_deque.append(random_weighted_word)

        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])

        if sentence[len(sentence)-1] == 'END':
            sentence_string = ' '.join(sentence)
            sentence_string = re.sub(' END', '. ', sentence_string, flags=re.IGNORECASE)
            sentence_string = sentence_string.capitalize()

            new_tweet_len = len(sentence_string) + len(tweet)

            if sentence_count == 0 and new_tweet_len < length:
                # We should add this sentence to the tweet and move on to
                # make another
                tweet += sentence_string
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count == 0 and new_tweet_len >= length:
                # forget the sentence and generate a new one :P
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count > 0 and new_tweet_len < length:
                # More than one sentence. and length is still less max
                # Get another new sentence
                tweet += sentence_string
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            else:
                # Return this good good tweet
                return tweet

def generate_sentence(length, markov_model):
    """Random walk for first order markov"""
    current_word = generate_random_start(markov_model)
    chosen_words_list = [current_word]

    for i in range(length):
        # Dictogram containing all words that follow 'current_word'
        current_dictogram = markov_model[current_word]
        random_word = current_dictogram.return_weighted_random_word()
        
        # 'random_word' becomes current_word
        current_word = random_word

        chosen_words_list.append(current_word)

    # Capitalize first word.
    chosen_words_list[0] = chosen_words_list[0].capitalize()
    sentence = " ".join(chosen_words_list) + "."

    return sentence


if __name__ == '__main__':
    # clean_text_list = clean_text_in("fish.txt").split()
    clean_text_list = clean_file("alan-watts.txt")
    # print(clean_text_list)
    # markov = markov_chain_from("fish.txt")
    # markov = markov_chain(clean_text_list)
    # sentence = generate_sentence(8, markov)
    # print(sentence)

    highmarkov = nth_order_markov_model(2, clean_text_list)
    # print(highmarkov)
    sentence = generate_random_sentence_n(140, highmarkov)
    # sentence = generate_sentence_with_nth_order(8, clean_text_list)
    print("-----------\n", sentence)






