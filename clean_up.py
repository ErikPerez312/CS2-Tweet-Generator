"""Module will remove unwanted characters in a text file"""
from sys import argv


def remove_unwanted_characters_from(text):
    unwanted_characters = [",", ".", ":", "_", ";", "!", "?", "\"", "*", "(", ")", "[", "]", "/"]
    for char in unwanted_characters:
        text = text.replace(char, "")

    return text


def replace_special_chars_from(text):
    chars_to_replace = ['\n', '--']
    for char in chars_to_replace:
        text = text.replace(char, ' ')
    return text


def get_text_from(filename):
    open_file = open(filename, 'r')
    source_text = open_file.read()
    open_file.close()

    return source_text


def create_file_with_cleaned_text(filename, cleaned_text):
    text = cleaned_text
    filename = filename.split('.')[0] + '_cleaned.txt'
    test_file = open(filename, 'w')
    test_file.write(text)
    test_file.close()


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
