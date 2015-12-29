__author__ = 'mushahidalam'
import sys


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[sys.maxint for x in range(n + 1)] for x in range(m + 1)]
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                minht = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if minht <= 0 else minht
        return dp[0][0]


A = [[-1, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]
obj = Solution()
print obj.calculateMinimumHP(A)
