__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        maxprod = A[0]
        for i in range(1,len(A)):
            if A[i] * maxprod > maxprod:
                maxprod = maxprod*A[i]
            elif A[i] > maxprod:
                maxprod = A[i]
        return maxprod

A = Solution()
B = [2,-1, 2,-4,-1,4]
print A.maxProduct(B)
