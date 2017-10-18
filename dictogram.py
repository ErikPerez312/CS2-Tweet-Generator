"""Dictogram class"""

import random


class Dictogram(dict):
    """docstring to stop warnings."""

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items."""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable."""
        for item in iterable:
            # TODO: increment item count
            if item not in self.keys():
                self[item] = 1
                self.types += 1
                self.tokens += 1
            else:
                self[item] += 1
                self.tokens += 1
            pass

    def count(self, item):
        """Return the count of the given item in this histogram, or 0."""
        # TODO: retrieve item count
        if item in self.keys():
            return self[item]
        else:
            return 0
        pass

    def return_random_word(self):
        """Return random word."""
        random_word = random.sample(self, 1)
        return random_word[0]

    def get_weighted_random_word(self):
        """Returns random word based off weight."""
        # Elmer
        # Step 1: Generate random number between 0 and total count - 1
        index = 0
        random_int = random.randint(0, self.tokens - 1)
        list_of_keys = self.keys()
        # print 'the random index is:', random_int
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            # print index
            if(index > random_int):
                # print(list_of_keys[i])
                return list_of_keys[i]

    def add(self, word):
        if word in self:
            self.tokens += 1
            self[word] += 1
        else:
            self.tokens += 1
            self.types += 1
            self[word] = 1
