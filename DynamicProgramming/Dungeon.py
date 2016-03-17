__author__ = 'mushahidalam'
import sys


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[sys.maxint for x in range(n + 1)] for x in range(m + 1)]
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                minht = min(dp[i + 1][j], dp[i][j + 1]) - A[i][j]
                dp[i][j] = 1 if minht <= 0 else minht
        return dp[0][0]


obj = Solution()
matrix = [[-2, -3, 3],
          [-5, -10, 1],
          [10, 30, -5]
          ]
print obj.calculateMinimumHP(matrix)
