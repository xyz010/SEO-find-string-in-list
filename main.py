# Andreas Loutzidis

# This is an assignment for Stylight

# Task definition
# write a class to find matching strings from a list of given strings without considering the order of the strings
# class components
# constructor --> takes in strings
# function "find" which takes a string to be matched, returns all the strings from the list which contain the
#                   EXACT same characters and number of characters as our given string no order is considered
# e.g. given list of strings  = ["helloworld", "foo", "bar", "stylight", "seo"]
#       find("eos") returns "seo"


class MatchingString:

    # constructor of the class
    def __init__(self, givenListOfStrings):
        self.givenStrings = givenListOfStrings
        #e.g. givenListOfStrings = ["helloworld", "foo", "bar", "stylight", "seo"]
        #print(self.givenStrings)

    def createDict(self,targetString):
        frequencyDict = {}
        for i in targetString:
            #check whether character already exists in our dictionary
            if i in frequencyDict:
                frequencyDict[i] += 1
            else:
                frequencyDict[i] = 1
        #print("This is the freq dict form createDict:", frequencyDict)
        return frequencyDict

    # returns the sorted dictionary based on character
    def sortDict(self,inputDictionary):
        return dict(sorted(inputDictionary.items(), key=lambda x: x[0]))


    # This is the function that takes a string as an input in order to be matched
    def find(self, targetString):
        givenStrings = self.givenStrings  # ["helloworld", "foo", "bar", "stylight", "seo"]

        # first create the sorted target dictionary
        targetDictionary = self.createDict(targetString)
        sortedTargetDict = self.sortDict(targetDictionary)

        #initialize the return list of strings
        foundStrings = []

        #traverse through the given strings to see if there is a match
        for i in givenStrings:
            tempDict = self.createDict(i)
            #print("Temp dict", tempDict)
            sortedTempDict = self.sortDict(tempDict)
            #print("Sorted Temp dict", sortedTempDict)

            if sortedTempDict == sortedTargetDict:
                foundStrings.append(i)
        return foundStrings


if __name__ == '__main__':

    # # The following block is for manual entry of target string and the given list of strings
    # inputList = []
    # # Input number of elemetns
    # n = int(input("Enter number of elements in the list : "))
    # # iterating till the range
    # for i in range(0, n):
    #     print("Enter element No-{}: ".format(i + 1))
    #     x = input()
    #     inputList.append(x)  # adding the element
    # print("The entered list is: \n", inputList)
    # targetString = str(input("Please enter the string to be matched : "))
    # #--------------------------------------------------------------------------------------

    inputList = ["hell2oworld", "foo", "bar", "stylight", "seo", "ofo", "oof", "90"]
    targetString = "ofo"

    instanceClass = MatchingString(inputList)
    targetDict = MatchingString.createDict(instanceClass, targetString)
    sortedTargetDict = MatchingString.sortDict(instanceClass, targetDict)
    print("The input string: ", targetString, "is a match with the following: ",MatchingString.find(instanceClass,targetString))