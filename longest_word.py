import unittest


class LongestWordTest(unittest.TestCase):

    """ Test for the ''longest_word()'' function     """

    def test_longest_word(self):
        input_string = 'fun&!! time'
        output_string = 'time'
        result_string = longest_word(input_string)
        self.assertEqual(result_string, output_string)