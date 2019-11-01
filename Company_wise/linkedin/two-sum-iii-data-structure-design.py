import collections
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numberMap = collections.defaultdict(int)
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.numberMap[number] +=1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for digit in self.numberMap.keys():
            target = value - digit
            if target in self.numberMap:
                if target == digit and self.numberMap[target]==1:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(0)
obj.add(-1)
obj.add(1)
print obj.find(0)
# print obj.find(7)

# obj = TwoSum()
# obj.add(3)
# obj.add(1)
# obj.add(2)
# print obj.find(3)
# print obj.find(6)