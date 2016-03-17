__author__ = 'mushahidalam'
from collections import OrderedDict


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def countingsort(self, nums, nd):
        n = len(nums)
        count = [0] * 10
        for i in xrange(0, n):
            count[(nums[i] / nd) % 10] += 1
        for i in xrange(1, 10):
            count[i] += count[i - 1]
        output = [0] * n
        for i in xrange(n - 1, -1, -1):
            output[count[(nums[i] / nd) % 10] - 1] = nums[i]
            count[(nums[i] / nd) % 10] -= 1
        return output

    def radixsort(self, num):
        maxnum = max(num)
        nd = 1
        while maxnum / nd > 0:
            num = self.countingsort(num, nd)
            nd = nd * 10
        return num

    def maximumGap(self, A):
        n = len(A)
        if n < 2:
            return 0
        A = self.radixsort(A)
        ret = abs(A[1] - A[0])
        for i in xrange(2, n):
            ret = max(ret, A[i] - A[i - 1])
        return ret


obj = Solution()
arr = [100, 100, 100]
print obj.maximumGap(arr)
