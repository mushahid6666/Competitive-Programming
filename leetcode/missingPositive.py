import sys


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        if n == 1:
            if nums[0] != 1:
                return 1
            else:
                return 2
        ele_set = set()
        for i in range(n):
            ele_set.add(nums[i])
        missing = 1
        for i in range(0, n):
            if missing not in ele_set:
                return missing
            missing += 1
        return missing


MissingPositive = Solution()
print MissingPositive.firstMissingPositive([2, 1])
