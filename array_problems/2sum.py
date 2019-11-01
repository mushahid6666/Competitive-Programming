"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import collections
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numberDict = collections.defaultdict(int)
        for i in range(len(nums)):
            numberDict[nums[i]] = i

        for i in range(len(nums)):
            num1 = nums[i]
            reqNum = target - num1
            if reqNum in numberDict and numberDict[reqNum] != i:
                return [i, numberDict[reqNum]]

obj = Solution()
nums = [2, 7, 11, 15]
target = 9
print obj.twoSum(nums, target)
nums = [2, 7]
target = 9
print obj.twoSum(nums, target)

