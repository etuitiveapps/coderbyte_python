import unittest
import re


def is_clean_string(input_string):
    match = re.match('[a-zA-Z]*', input_string)
    match_group = match.group(0)
    return match_group == input_string


def longest_word(input_string):
    """Implement a function to find longest word in a string

     Args:
        input_string: input string

    Returns: The longest word in the input string
    """
    input_list = input_string.split()
    longest_word_int = 0
    longest_word_string = None
    current_string_size = 0
    for current_string in input_list:
        current_string_size = len(current_string)
        if is_clean_string(current_string) and (current_string_size > longest_word_int):
            longest_word_int = current_string_size
            longest_word_string = current_string
    return longest_word_string


class LongestWordTest(unittest.TestCase):

    """ Test for the ''longest_word()'' function     """

    def test_longest_word(self):
        input_string = 'fun&!! time'
        output_string = 'time'
        result_string = longest_word(input_string)
        self.assertEqual(result_string, output_string)
