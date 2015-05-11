import unittest


def first_reverse(input_string):
    """Implement a function to reverse a string

     Args:
        input_string: input string waiting to be reversed

    Returns: The reverse of the input string
    """
    output_list = []
    character_list = list(input_string)
    for character in reversed(character_list):
        output_list.append(character)
    return ''.join(output_list)


class FirstReverseTest(unittest.TestCase):

    """ Test for the ''first_reverse()'' function     """

    def test_first_reverse(self):
        input_string = 'coderbyte'
        output_string = 'etybredoc'
        result_string = first_reverse(input_string)
        self.assertEqual(result_string, output_string)

    def test_second_first_reverse_example(self):
        input_string = 'I Love Code'
        output_string = 'edoC evoL I'
        result_string = first_reverse(input_string)
        self.assertEqual(result_string, output_string)

if __name__ == '__main__':
    unittest.main()