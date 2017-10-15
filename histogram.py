from text_file_stripper import clean_text_in
from sys import argv


# def convert_text_to_string(text_file_path):
#     """Returns a string made up of the text in the text_file."""
#     file = open(text_file_path, "r")
#     file_text = file.readlines()
#     file.close()
#     string = "".join(file_text)
#     return string


def make_histogram_from(text):
    """Will create a histogram using the text parameter."""
    text_list = text.split()
    histogram = dict()
    for word in text_list:
        # Make all words lower case
        lower_case_word = word.lower()
        if lower_case_word in histogram:
            histogram[lower_case_word] += 1
        else:
            histogram[lower_case_word] = 1
    # print(histogram)
    return histogram


def total_words_in(histogram):
    """Returns the length of the histogram."""
    return len(histogram.keys())


def frequency_of(word, histogram):
    """Gets the frequency of the word in the histogram."""
    lower_case_word = word.lower()
    if lower_case_word not in histogram.keys():
        # print("frequency", 0)
        return 0
    return histogram[lower_case_word]


if __name__ == '__main__':
    filename = argv[1:]
    text = clean_text_in(filename[0])
    # print(text)
    histo = make_histogram_from(text)
    print("total words: ", total_words_in(histo))
    print("freq of: ", frequency_of("take", histo))
