import unittest


def simple_addition(input_int):
    sum_of_numbers = 0
    for current_number in range(input_int + 1):
        sum_of_numbers += current_number
    return sum_of_numbers

class SimpleAdditionTest(unittest.TestCase):

    """ Test For ''simple_addition()'' function
     Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num.
     For the test cases, the parameter num will be any number from 1 to 1000.
    """
    def test_zero_factorial(self):
        input_int = 12
        output_int = 78
        result_int = simple_addition(input_int)
        self.assertEqual(result_int, output_int)