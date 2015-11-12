__author__ = 'mushahidalam'
import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A==1 and B==1:
            return 1
        n = A+B-2
        r = B-1
        result = math.factorial(n)/math.factorial(n-r)
        print(result)

obj = Solution()
print obj.uniquePaths(3,2)