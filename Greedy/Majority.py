__author__ = 'mushahidalam'
import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        majority = math.floor(n / 2)
        dict = {}
        for i in A:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        keys = dict.keys()
        for i in keys:
            if dict[i] > majority:
                return i


obj = Solution()
arr = [2, 1, 2]
print obj.majorityElement(arr)
