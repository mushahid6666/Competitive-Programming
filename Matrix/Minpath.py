__author__ = 'mushahidalam'
class Solution:
    # @param A : list of list of integers
    # @return an integer
    #Dynamic Programming solution
    #TODO recurssive solution
    def minPathSum(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0 for x in range(n)] for x in range(m)]
        for i in range(n):
            dp[0][i] = dp[0][i-1]+A[0][i]
        for j in range(m):
            dp[j][0] = dp[j-1][0]+A[j][0]
        for i in range(1,m):
            for j in range(1,n):
                if dp[i-1][j]>dp[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m-1][n-1]