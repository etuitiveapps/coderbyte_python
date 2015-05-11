import unittest
import re


def letter_capitalize(input_string):
    string_list = re.split(r'(\s*)', input_string)
    output_list = []
    for current_string in string_list:
        result = current_string.capitalize()
        output_list.append(result)
    return ''.join(output_list)


class LetterCapitalizeTest(unittest.TestCase):

    """ Test For ''letter_capitalize()'' function
        Using the Python language, have the function LetterCapitalize(str) take the str parameter
        being passed and capitalize the first letter of each word. Words will be separated by only one space.
    """

    def test_letter_capitalize(self):
        input_string = 'hello world'
        output_string = 'Hello World'
        result_string = letter_capitalize(input_string)
        self.assertEqual(result_string, output_string)
