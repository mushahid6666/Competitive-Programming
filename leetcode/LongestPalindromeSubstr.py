#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Attempt2
        strLen = len(s)
        if strLen == 0 or strLen == 1:
            return s
        # if strLen == 2:
        #     if s[0] != s[1]:
        #         return s[0]
        #     else:
        #         return s
        #intialize the matrix
        trackPaliMatrix = [[0 for _ in range(strLen + 1)] for _ in range(strLen + 1)]
        for i in range(strLen + 1):
            trackPaliMatrix[0][i] = 1
            trackPaliMatrix[i][0] = 1
            trackPaliMatrix[i][i] = 1

        #Longest pali info
        LPaliStartIndex = 0
        LPaliEndIndex = 0
        LPaliLen = 0
        ispali = False
        #iterate through matrix
        for i in range( strLen -1, 0 , -1):
            for j in range(i + 1 , strLen + 1):
                #if i,j letters match an s[i-1][j-1] is pali, update the longest pali info
                if s[i-1] == s[j-1]:
                    if j-i == 1:
                        ispali = True
                    elif trackPaliMatrix[i+1][j-1] == 1 and i!=j :
                        ispali = True
                    if ispali:
                        trackPaliMatrix[i][j] = 1
                        if j-i+1 >= LPaliLen:
                            LPaliStartIndex = i
                            LPaliEndIndex = j
                            LPaliLen = j - i + 1
                    ispali = False
        # print LPaliStartIndex, LPaliEndIndex
        # print s[LPaliStartIndex - 1:LPaliEndIndex]
        # for i in range(strLen):
        #     for j in range(strLen):
        #         print trackPaliMatrix[i][j],
        #     print  "\n"
        if LPaliStartIndex == 0 and LPaliEndIndex ==0:
            return s[0]
        return s[LPaliStartIndex - 1:LPaliEndIndex]
        #Accepted Leetcode Solution
        {
        # len_str = len(s)
        # if len_str == 1:
        #     return s
        # if len_str == 2:
        #     if s[0] == s[1]:
        #         return s
        #     return s[0]
        # dp = [[0 for _ in range(len_str)] for _ in range(len_str)]
        # pali_str = ""
        # max_length = 0
        # for i in range(len_str):
        #     dp[i][i] = 1
        #     max_length = 1
        #     pali_str = s[i:i + 1]
        # for i in range(len_str - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = 1
        #         max_length = 2
        #         pali_str = s[i:i + 2]
        # for i in range(len_str - 3, -1, -1):
        #     for j in range(len_str - 1, 1, -1):
        #         if dp[i + 1][j - 1] == 1 and s[i] == s[j]:
        #             dp[i][j] = 1
        #             if j - i + 1 > max_length:
        #                 max_length = j - i + 1
        #                 pali_str = s[i:j + 1]
        # return pali_str
        }


obj = Solution()
# str = "ccc"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
# str = "babad"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
# str = "cbbd"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
# str = "abbacca"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
# str = "adbda"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
# str = "papapjsjsj"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
# str = "abcda"
# print "String : " + str + " LPali : " + obj.longestPalindrome(str)
str = "ac"
print "String : " + str + " LPali : " + obj.longestPalindrome(str)