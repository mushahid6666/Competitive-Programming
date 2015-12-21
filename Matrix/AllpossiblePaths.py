__author__ = 'mushahidalam'
import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A == 1:
            return 1
        if B == 1:
            return 1
        return math.factorial(A + B - 2) / (math.factorial(A - 1) * math.factorial(B - 1))


A = Solution()
print(A.uniquePaths(20, 30))
