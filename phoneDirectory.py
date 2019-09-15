import random

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        # self.validpphoneNumbers = dict()
        self.remainingNumbersMap = dict()
        self.generatePhoneNumbers(maxNumbers)

    def generatePhoneNumbers(self, maxNumbers):
        """
        :param maxNumbers: int
        :return: None
        """
        phoneNumbersList = random.sample(range(0,maxNumbers), maxNumbers)
        for number in phoneNumbersList:
            self.remainingNumbersMap[number] = 1

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.remainingNumbersMap) > 0:
            numbersList = self.remainingNumbersMap.keys()
            number = numbersList[0]
            del self.remainingNumbersMap[number]
            return number
        else:
            return -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if number in self.remainingNumbersMap.keys():
            return True
        else:
            return False

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        self.remainingNumbersMap[number] = 1


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)