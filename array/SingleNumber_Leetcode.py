__author__ = 'mushahidalam'


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(0, len(nums)):
            x = x ^ nums[i]
        return x


obj = Solution()
arr = [2, 3, 4, 5, 4, 2, 3]
print(obj.singleNumber(arr))
