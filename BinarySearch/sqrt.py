__author__ = 'mushahidalam'
import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==0:
            return 0
        if A==1:
            return 1
        low = 0
        high = A+1
        while high-low > 1:
            mid = (low+high) / 2
            print(low,high,mid)
            if mid*mid <= A:
              low = mid
            else:
              high = mid
        return low



obj = Solution()
print obj.sqrt(930675566)