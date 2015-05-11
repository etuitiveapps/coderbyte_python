import unittest


class SimpleAdditionTest(unittest.TestCase):

    """ Test For ''simple_addition()'' function     """

    def test_zero_factorial(self):
        input_int = 12
        output_int = 78
        result_int = simple_addition(input_int)
        self.assertEqual(result_int, output_int)