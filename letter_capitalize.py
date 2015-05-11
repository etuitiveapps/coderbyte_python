import unittest


class LetterCapitalizeTest(unittest.TestCase):

    """ Test For ''letter_capitalize()'' function     """

    def test_letter_capitalize(self):
        input_int = 'hello world'
        output_int = 'Hello World'
        result_int = letter_capitalize(input_int)
        self.assertEqual(result_int, output_int)