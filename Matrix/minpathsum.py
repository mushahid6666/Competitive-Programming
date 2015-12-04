__author__ = 'mushahidalam'
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0 for x in range(n)] for x in range(m)]
        for i in range(n):
            dp[0][i] = dp[0][i-1]+A[0][i]
        for i in range(n):
            dp[0][i] = dp[0][i-1]+A[0][i]