"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import collections
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result = []
        nums.sort()
        i = 0
        while i < len(nums) -1:
            target = -nums[i]
            start = i+1
            end = len(nums) -1
            while start < end:
                sum  = nums[start]  + nums[end]
                if sum < target:
                    start +=1
                elif sum > target:
                    end -=1
                else:
                    triplet = [nums[i], nums[start], nums[end]]
                    result.append(triplet)
                    while start < end and nums[start] == triplet[1]:
                        start +=1
                    while start < end and nums[end] == triplet[2]:
                        end -=1
            while i < len(nums)-1 and nums[i+1] == nums[i]:
                i+=1
            i+=1
        return result


obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print obj.threeSum(nums)
nums = [-1, 0, 1]
print obj.threeSum(nums)
nums = [-1,0,1,0]
print obj.threeSum(nums)