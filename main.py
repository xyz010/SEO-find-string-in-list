# (C) Andreas Loutzidis 2021

"""
    This is class that checkes whether an input string belongs to a list of strings
    either as-is or at any given order. For example the word "toy" belongs to the list
    ["car", "world", "yto"]
"""


class MatchingString:

    def __init__(self, list_of_strings):

        self.given_strings = list_of_strings

    @staticmethod
    def create_dict(target_string):

        frequency_dict = {}
        for i in target_string:
            if i in frequency_dict: #character already exists in our dictionary
                frequency_dict[i] += 1
            else:
                frequency_dict[i] = 1
        return frequency_dict

    @staticmethod
    # returns the sorted dictionary based on character
    def sort_dict(input_dict):

        return dict(sorted(input_dict.items(), key=lambda x: x[0]))

    @staticmethod
    def find(target_string, given_strings):

        # first create the sorted target dictionary
        target_dict = MatchingString.create_dict(target_string)
        sorted_target_dict = MatchingString.sort_dict(target_dict)

        found_strings = []
        #traverse through the given strings to see if there is a match
        for i in given_strings:
            temp_dict = MatchingString.create_dict(i)
            sorted_temp_dict = MatchingString.sort_dict(temp_dict)
            if sorted_temp_dict == sorted_target_dict:
                found_strings.append(i)
        return found_strings


if __name__ == '__main__':


    '''The following block is for manual entry of target string and the given list of strings
    input_list = []
    n = int(input("Enter number of elements in the list : "))
    # iterating till the range
    for i in range(0, n):
        print("Enter element No-{}: ".format(i + 1))
        x = input()
        input_list.append(x)  # adding the element
    print("The entered list is: \n", input_list)
    target_string = str(input("Please enter the string to be matched : "))
    '''

    input_list = ["world", "wordl", "orwld", "dlrow", "foo", "bar", "stylight", "seo"]
    target_string = "world"

    print("The input string: ", target_string, "is a match with the following: ", MatchingString.find(target_string, input_list))