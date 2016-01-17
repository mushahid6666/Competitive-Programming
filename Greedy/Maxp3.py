__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        result = 1
        n = len(A)
        for i in range(n - 3, n):
            result = result * A[i]
        if (n > 3 and A[0] < 0 and A[1] < 0):
            temp = A[0] * A[1] * A[-1]
            if temp > result:
                result = temp
        return result


obj = Solution()
arr = [-1, -2, -3, -4, -5]
print obj.maxp3(arr)
