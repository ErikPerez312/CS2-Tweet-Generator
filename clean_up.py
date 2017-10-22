"""Module will remove unwanted characters in a text file"""
from sys import argv
import re


# def remove_unwanted_characters_from(text):
#     unwanted_characters = [",", ".", ":", "_", ";", "!", "?", "\"", "*", "(", ")", "[", "]", "/"]
#     for char in unwanted_characters:
#         text = text.replace(char, "")

#     return text


# def replace_special_chars_from(text):
#     chars_to_replace = ['\n', '--']
#     for char in chars_to_replace:
#         text = text.replace(char, ' ')
#     return text


# def get_text_from(filename):
#     open_file = open(filename, 'r')
#     source_text = open_file.read()
#     open_file.close()

#     return source_text


# def create_file_with_cleaned_text(filename, cleaned_text):
#     text = cleaned_text
#     filename = filename.split('.')[0] + '_cleaned.txt'
#     test_file = open(filename, 'w')
#     test_file.write(text)
#     test_file.close()

def remove_punctuation(text):
    no_punc_text = re.sub('[,()]', '', text)
    # Handles all that are not endlines
    no_punc_text = re.sub('\. +', ' END ', no_punc_text)
    # This does the same as above but also gets new lines and therefore
    # we give an extra space!
    no_punc_text = re.sub('\.\s+', ' END ', no_punc_text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    no_punc_text = re.sub(':', ' ', no_punc_text)

    return no_punc_text

def clean_file(filename):
    data_file = open(filename, 'r')
    words_list = data_file.read().lower()
    words_list = remove_punctuation(words_list)
    result_list = []

    matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
    for match in matches:
        result_list.append(match)
    return ['END'] + result_list


def clean_text_in(filename):
    text = get_text_from(filename)
    cleaned_text = replace_special_chars_from(remove_unwanted_characters_from(text))
    create_file_with_cleaned_text(filename, cleaned_text)

    return cleaned_text


# argv - 1: file to edit
if __name__ == '__main__':
    # Use [1:] get the whole file name
    arguments = argv[1:]
    clean_text_in(arguments[0])
