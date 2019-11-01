import sys
class Solution(object):
    def computeCrossSum(self, nums, low, high, mid):
        if low == high:
            return nums[low]

        max_left_sum = -sys.maxint
        left_sum = 0
        for i in range( mid , low - 1,  -1):
            left_sum += nums[i]
            max_left_sum = max(left_sum, max_left_sum)

        right_sum = 0
        max_right_sum = -sys.maxint
        for i in range(mid + 1, high + 1, 1):
            right_sum += nums[i]
            max_right_sum = max(max_right_sum, right_sum)

        return max_left_sum + max_right_sum


    def computeMaxSumDivNConq(self, nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) / 2
        left_sum = self.computeMaxSumDivNConq(nums, low, mid)
        right_sum = self.computeMaxSumDivNConq(nums, mid + 1, high)
        cross_sum = self.computeCrossSum(nums, low, high, mid)
        return max(left_sum, right_sum, cross_sum)

    def maxSubArrayLinearTime(self,nums):
        cur_sum = -sys.maxint
        max_sum = -sys.maxint
        for i in range(len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return  self.computeMaxSumDivNConq(nums, 0, len(nums) -1)
        return self.maxSubArrayLinearTime(nums)

obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print obj.maxSubArray(nums)
