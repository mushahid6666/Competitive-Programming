__author__ = 'mushahidalam'
import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        min = sys.maxint
        result = 0
        A.sort()
        for i in range(0, len(A)):
            j = i + 1
            k = len(A) - 1
            while (j < k):
                sm = A[i] + A[j] + A[k]
                diff = abs(sm - B)
                if (diff == 0):
                    return sm
                if diff < min:
                    min = diff
                    result = sm
                if sm <= B:
                    j += 1
                else:
                    k -= 1
        return result


obj = Solution()
arr = [-1, 2, 1, -4]
print obj.threeSumClosest(arr, 1)
