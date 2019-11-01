__author__ = 'mushahidalam'
class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 and len(word2) == 0:
            return False
        editDistance = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(1, len(word2) + 1):
            editDistance[0][i] = editDistance[0][i - 1] + 1

        for i in range(1, len(word1) + 1):
            editDistance[i][0] = editDistance[i - 1][0] + 1

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    editDistance[i][j] = editDistance[i - 1][j - 1]
                else:
                    editDistance[i][j] = 1 + min(editDistance[i - 1][j - 1], editDistance[i][j - 1],
                                                 editDistance[i - 1][j])
        return editDistance[len(word1)][len(word2)]

    def minDistance1(self, word1, word2):
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
