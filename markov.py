"""Generates Markov chain dict from contents in text file"""

from clean_up import clean_text_in
from collections import ChainMap
from dictogram import Dictogram
import sample
import random


def markov_chain_from(text_file_name):
    data = clean_text_in("fish.txt").split()
    # print("TYPE OF DATA:", type(data), "-----------")
    # print("LENGTH OF DATA:", len(data), "----------")
    markov = dict()

    for index in range(0, len(data) - 1):
        if data[index] in markov:
            # if word in markov update values
            markov[data[index]].update([data[index + 1]])
        else:
            # Create dictogram with word.
            markov[data[index]] = Dictogram([data[index + 1]])
    return markov


# def weighted_markov(markov_dict):
#     for markov in markov_dict:
#         histogram = markov_dict[markov]
#         weighted_dicts = sample.create_weighted_sorted_tuple_list_markov(histogram)
#         markov_dict[markov] = weighted_dicts
#
#     return markov_dict
#
#
# def walk_the_markov(num, weighted_markov_dict):
#     sentence = []
#     current_word = random.choice(list(weighted_markov_dict.keys()))
#     print(current_word)
#     for x in range(num):
#         next_word = ""
#         random_range = random.random()
#         for item in weighted_markov_dict[current_word]:
#             if random_range > float(item[0]):
#                 continue
#             else:
#                 next_word = (current_word[1], item[1])
#         current_word = next_word
#         print(current_word)
#         sentence.append(next_word[1])
#
#     return " ".join(sentence)


if __name__ == '__main__':
    clean_text_list = clean_text_in("fish.txt")
    # print(clean_text_list)
    markov = markov_chain_from(clean_text_list)
    # for m in markov.iteritems():
    #     print(m)
    print(markov)
