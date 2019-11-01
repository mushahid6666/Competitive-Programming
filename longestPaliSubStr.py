"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    def __init__(self):
        self.longestPali = ""
    def checkPali(self,s , left, right):
        while left >=0 and right < len(s) and s[left]== s[right]:
            left -=1
            right +=1
        return s[left + 1:right]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)== 0 or len(s)== 1:
            return s
        self.__init__()
        for i in range(len(s)):
            #mid point with pali length is odd
            pali = self.checkPali(s, i, i)
            if len(self.longestPali) < len(pali):
                self.longestPali = pali

            #mid point with pali length is even
            pali = self.checkPali(s, i, i +1)
            if len(self.longestPali) < len(pali):
                self.longestPali = pali

        return self.longestPali

obj = Solution()
s = "babad"
print obj.longestPalindrome(s)
s = ""
print obj.longestPalindrome(s)
s = "a"
print obj.longestPalindrome(s)