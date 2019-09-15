import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """Given an array of n positive integers and a positive integer s
         find the minimal length of a contiguous subarray of which the sum greater than or equal to s 
         If there isn't one, return 0 instead"""
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >= s:
                return 1
            else:
                return 0
        result = sys.maxint
        l = 0
        r = l
        curSum = nums[l]
        curlen = 1
        while r < len(nums):
            if curSum >= s:
                result = min(result, curlen)
                while curSum >= s and l < r:
                    result = min(result, curlen)
                    curSum = curSum - nums[l]
                    curlen = curlen - 1
                    l = l + 1
                if l == r:
                    if curSum >= s:
                        result = min(result, curlen)
                    r = r + 1
                    if r < len(nums):
                        curSum = curSum + nums[r]
                        curlen = curlen + 1
            else:
                r = r + 1
                if r < len(nums):
                    curSum = curSum + nums[r]
                    curlen = curlen + 1

        #Brute Force Solution
        # for i in range(len(nums)):
        #     if nums[i] >= s:
        #         return 1
        #     curSum = nums[i]
        #     curlen = 1
        #     for j in range(i+1, len(nums)):
        #         curlen = curlen + 1
        #         curSum = curSum + nums[j]
        #         if curSum >= s:
        #             result = min(curlen, result)
        #             break
        if result == sys.maxint:
            return 0
        return result
# Input:
s = 7
nums = [2,3,1,2,3,3]
# s = 6
# nums = [10,2, 3, 1]
# nums = [0, 1]
# Output: 2
s = 15
nums = [5,10]
solutionObj = Solution()
print solutionObj.minSubArrayLen(s, nums)
