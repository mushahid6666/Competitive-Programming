__author__ = 'mushahidalam'
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m==0:
            return n
        if n==0:
            return m
        dp = [[0 for x in range(m+1)]for y in range(n+1)]
        for i in range(m+1):
            for j in range(n+1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i][j-1],
                                     dp[i-1][j],
                                     dp[i-1][j-1])
        return dp[m][n]

A = Solution()
word1 = "a"
word2 = "b"
A.minDistance(word1,word2)
