import unittest


def first_factorial(input_int):
    output_int = 1
    if input_int < 0:
        raise ValueError('Invalid input: negative factorial detected')
    elif input_int == 0:
        output_int = 1
    else:
        for current_number in range(1, input_int + 1):
            output_int *= current_number
    return output_int


class FirstFactorialTest(unittest.TestCase):

    """ Test For ''first_factorial()'' function     """

    def test_zero_factorial(self):
        input_int = 0
        output_int = 1
        result_int = first_factorial(input_int)
        self.assertEqual(result_int, output_int)

    def test_one_factorial(self):
        input_int = 1
        output_int = 1
        result_int = first_factorial(input_int)
        self.assertEqual(result_int, output_int)

    def test_four_factorial(self):
        input_int = 4
        output_int = 24
        result_int = first_factorial(input_int)
        self.assertEqual(result_int, output_int)

    def test_eight_factorial(self):
        input_int = 8
        output_int = 40320
        result_int = first_factorial(input_int)
        self.assertEqual(result_int, output_int)

    def test_negative_factorial(self):
        input_int = -1
        with self.assertRaises(ValueError):
            first_factorial(input_int)
