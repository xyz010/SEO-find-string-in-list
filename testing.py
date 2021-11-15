import unittest
import main

"""
    This script is to perform unit testing on edge cases and check correct function of every module
"""

class FindMatchingStringsTest(unittest.TestCase):

    def assignment_test(self):
        # GIVEN
        input_list = ["helloworld", "foo", "bar", "stylight", "seo"]
        target_string = "eos"
        expected_value = ['eos']
        message = "Values are not equal"
        # WHEN
        answer = main.MatchingString.find(target_string, input_list)
        # THEN
        self.assertEqual(expected_value, answer, message)

    def test_empty_list(self):
        # GIVEN
        input_list = []
        target_string = "test"
        expected_value = []
        message = "Values are not equal"
        # WHEN
        answer = main.MatchingString.find(target_string, input_list)
        # THEN
        self.assertEqual(expected_value, answer, message)

    def test_empty_target_string(self):
        # GIVEN
        input_list = []
        target_string = "test"
        expected_value = []
        message = "Values are not equal"
        # WHEN
        answer = main.MatchingString.find(target_string, input_list)
        # THEN
        self.assertEqual(expected_value, answer, message)

    def multiple_strings_exist_test(self):
        # GIVEN
        input_list = ["world", "wordl", "orwld", "dlrow", "foo", "bar", "stylight", "seo"]
        target_string = "world"
        expected_value = ["world", "wordl", "orwld", "dlrow"]
        message = "Values are not equal"
        # WHEN
        answer = main.MatchingString.find(target_string, input_list)
        # THEN
        self.assertEqual(expected_value, answer, message)

    def dict_creation_test(self):
        # GIVEN
        word = 'seo'
        expected_value = {'s':1, 'e':1, 'o':1}
        message = "Dictionary is wrong"
        # WHEN
        answer = main.MatchingString.create_dict(word)
        # THEN
        self.assertEqual(expected_value, answer, message)

    def dict_sorting_test(self):
        # GIVEN
        word_dict = {'s':1, 'e':1, 'o':1}
        expected_value = {'e':1, 'o':1, 's':1,}
        message = "Dictionary is sorted wrong"
        # WHEN
        answer = main.MatchingString.sort_dict(word_dict)
        # THEN
        self.assertEqual(expected_value, answer, message)


if __name__ == '__main__':
    unittest.main()