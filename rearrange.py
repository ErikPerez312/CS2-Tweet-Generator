"""Script will rearrange a list of words."""

import sys
import random


def rearrange(words):
    """Will rearrange and return list of WORDS."""
    scrambled_list = list(words)
    words_length = len(words)
    # Code below taken from StackOverflow. Link below
    # https://stackoverflow.com/questions/17489477/shuffle-a-python-list-without-using-the-built-in-function
    assert words_length > 2, 'Array is too short to shuffle!'
    for index in range(words_length):
        swap = random.randrange(words_length - 1)
        swap += swap >= index
        scrambled_list[index], scrambled_list[swap] = scrambled_list[swap], scrambled_list[index]
    print(scrambled_list)
    return scrambled_list


if __name__ == "__main__":
    words = sys.argv
    del words[0]

    rearrange(words)
