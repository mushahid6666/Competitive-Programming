import sys


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDict = dict()
        for i in range(len(nums)):
            numsDict[nums[i]] = 1
        counter = 0
        while counter <= len(nums):
            if counter not in numsDict:
                return counter
            counter += 1
    { # Previous Accepted Solution
    # def firstMissingPositive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         if nums[0] != 1:
    #             return 1
    #         else:
    #             return 2
    #     ele_set = set()
    #     for i in range(n):
    #         ele_set.add(nums[i])
    #     missing = 1
    #     for i in range(0, n):
    #         if missing not in ele_set:
    #             return missing
    #         missing += 1
    #     return missing
    }


MissingPositive = Solution()
# print MissingPositive.missingNumber([2, 1])
print MissingPositive.missingNumber([3,0,1])
print MissingPositive.missingNumber([9,6,4,2,3,5,7,0,1])
