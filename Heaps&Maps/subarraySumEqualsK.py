class Solution(object):
    # Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

    # Example 1:
    # Input:nums = [1,1,1], k = 2
    # Output: 2
    # Input:nums = [1,1,-1,1,1], k = 2
    # Note:
    # The length of the array is in range [1, 20,000].
    # The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == k:
                return 1
        left_sum_arr = [0]
        for i in range(1, len(nums) + 1):
            sum  = left_sum_arr[i-1] + nums[i-1]
            left_sum_arr.append(sum)

        # print left_sum_arr
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if left_sum_arr[j] - left_sum_arr[i] == k:
                    result += 1
        return result

obj = Solution()
nums = [1,1,1]
k = 2
print  obj.subarraySum(nums, k)
nums = [1,1,-1,1,1]
k = 2
print  obj.subarraySum(nums, k)