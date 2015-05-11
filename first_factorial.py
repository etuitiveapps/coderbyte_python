import unittest


class FirstFactorialTest(unittest.TestCase):

    """ Test For ''first_factorial()'' function     """

    def test_first_reverse(self):
        input_int = 4
        output_int = 24
        result_int = first_factorial(input_int)
        self.assertEqual(result_int, output_int)
