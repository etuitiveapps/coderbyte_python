import unittest


def first_factorial(input_int):
    output_int = 1
    if input_int == 0 or input_int == 1:
        return 1
    else:
        return -1



class FirstFactorialTest(unittest.TestCase):

    """ Test For ''first_factorial()'' function     """

    def test_first_reverse(self):
        input_int = 0
        output_int = 1
        result_int = first_factorial(input_int)
        self.assertEqual(result_int, output_int)
