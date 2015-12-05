__author__ = 'mushahidalam'
__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        maxlocal = A[0]
        minlocal = A[0]
        globalmax = A[0]

        for i in range(1, len(A)):
            temp = maxlocal
            maxlocal = max(max(A[i] * maxlocal, A[i]), A[i] * minlocal)
            minlocal = min(min(A[i] * temp, A[i]), A[i] * minlocal)
            globalmax = max(globalmax, maxlocal)
        return globalmax


A = Solution()
B = [0, -1, 0, -4, -1, 0]
print A.maxProduct(B)
