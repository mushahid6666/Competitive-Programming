# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
class Solution(object):
    def canReachEnd(self, nums, cur_position, memo):

        if cur_position >= len(nums)-1:
            memo[len(nums) -1] = 1
            return True
        if memo[cur_position] == 1:
            return
        max_jum = min(nums[cur_position] + cur_position, len(nums) - 1)
        # max_jum = nums[cur_position]
        next_post = cur_position + 1
        while next_post <= max_jum:
            reached = self.canReachEnd(nums, next_post, memo)
            if reached:
                memo[cur_position] = 1
            next_post += 1
        return False
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        memo = [0]* len(nums)
        self.canReachEnd(nums, 0, memo)
        if memo[len(nums) - 1] == 1:
            return True
        return False

obj = Solution()
arr = [2,3,1,1,4]
print obj.canJump(arr)

arr = [3,2,1,0,4]
print obj.canJump(arr)

arr = [2, 0, 0]
print obj.canJump(arr)
arr = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
print obj.canJump(arr)
