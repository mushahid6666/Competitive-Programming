__author__ = 'mushahidalam'
from collections import OrderedDict


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        htable = OrderedDict()
        for i in nums:
            if i in htable:
                htable[i] = htable[i] + 1
            else:
                htable[i] = 1
        result = []
        keys = htable.keys()
        for i in range(0, len(htable)):
            if htable[keys[i]] == 1:
                result.append(keys[i])
        return result


obj = Solution()
arr = [-1, 0]
print obj.singleNumber(arr)
