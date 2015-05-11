import unittest
import re


def is_clean_string(input_string):
    """Implement a function to determine if string doesn't have any special characters

     Args:
        input_string: input string

    Returns: True if a string does not have any special characters
    """
    if re.match('[a-zA-Z]', input_string) is not None:
        return True
    else:
        return False


def is_vowel(input_char):
    if re.match('[aeiou]', input_char) is not None:
        return True
    else:
        return False


def alphabet_list():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def next_char(character):
    alphabet = alphabet_list()
    index_current_char = alphabet.index(character)
    next_character = alphabet[index_current_char + 1]
    if is_vowel(next_character):
        return next_character.upper()
    else:
        return next_character


def letter_changes(input_string):
    input_list = list(input_string)
    output_list = []
    for character in input_list:
        if is_clean_string(character):
            current_char = next_char(character)
            output_list.append(current_char)
        else:

            output_list.append(character)

    return ''.join(output_list)


class LetterChangesTest(unittest.TestCase):

    """ Test for the ''letter_changes()'' function

    Using the Python language, have the function LetterChanges(str) take
    the str parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the
    alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in
    this new string (a, e, i, o, u) and finally return this modified string.

    """

    def test_longest_word(self):
        input_string = 'hello*3'
        output_string = 'Ifmmp*3'
        result_string = letter_changes(input_string)
        self.assertEqual(result_string, output_string)