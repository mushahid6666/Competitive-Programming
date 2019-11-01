class Solution(object):
    def __init__(self):
        self.longPali = ""
    def checkPalindrome(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        substr = s[left +1 : right]
        if len(substr) > len(self.longPali):
            self.longPali = substr
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        for i in range(len(s)):
            self.checkPalindrome(s, i, i)
            self.checkPalindrome(s, i, i +1)
        return self.longPali

obj = Solution()
string = "babad"
string = "cbbd"
string  = "a"
print  obj.longestPalindrome(string)