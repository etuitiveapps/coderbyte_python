import unittest



class FirstReverseTest(unittest.TestCase):
    """ Test for the ''first_reverse()'' function     """

    def test_first_reverse(self):
        input_string = 'coderbyte'
        output_string = 'etybredoc'
        result_string = first_reverse(input_string)
        self.assertEqual(result_string, output_string)