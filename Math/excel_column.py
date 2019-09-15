__author__ = 'mushahidalam'
import string
class Solution:
    # @param A : string
    # @return an integer
    #Leetcode Attempt 2:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabets = string.ascii_uppercase
        alphabet_dict = dict()
        counter = 1
        for letter in alphabets:
            alphabet_dict[letter] = counter
            counter += 1
        column_number =0
        if len(s) == 1:
            return alphabet_dict[s[0]]
        for i in range(len(s)):
            column_number = column_number* 26 + alphabet_dict[s[i]]
        return column_number
obj = Solution()
print obj.titleToNumber('A')
print obj.titleToNumber('AB')
print obj.titleToNumber('ZY')
print obj.titleToNumber('AAA')

