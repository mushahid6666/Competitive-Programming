__author__ = 'mushahidalam'


# */
#  int max(int x, int y)
# { return (y > x)? y : x; }
# int maxSubArray(const int* A, int n1) {
#     int max_so_far = A[0], i;
#    int curr_max = A[0];
#
#    for (i = 1; i < n1; i++)
#    {
#         curr_max = max(A[i], curr_max+A[i]);
#         max_so_far = max(max_so_far, curr_max);
#    }
#    return max_so_far;
# }
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],

# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    #Leetcode Attempt1

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)== 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum  = nums[0]
        max_sum = sum
        for i in range(1, len(nums)):
            sum = max(nums[i] , sum + nums[i])
            max_sum = max(max_sum, sum)
        return max_sum

obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print obj.maxSubArray(nums)


    #Previous Solution
    # # @param A : list of integers
    # # @return a list of integers
    # def maxset(self, A):
    #     max_so_far = A[0]
    #     curr_max = A[0]
    #     result = [A[0]]
    #     flag = 0
    #     max_so_far = -1
    #     for i in range(1, len(A)):
    #         if A[i] > 0:
    #             curr_max = max(A[i], curr_max + A[i])
    #             if curr_max == A[i]:
    #                 max_so_far = max(max_so_far, curr_max)
    #                 if max_so_far == A[i]:
    #                     result = []
    #                     result.append(A[i])
    #             else:
    #                 prev_max = max_so_far
    #                 max_so_far = max(max_so_far, curr_max)
    #                 if max_so_far == curr_max and prev_max != max_so_far:
    #                     result.append(A[i])
    #         else:
    #             curr_max = 0
    #
    #     if len(result) == 1 and result[0] < 0:
    #         return
    #     else:
    #         return result
    #     pass


# A = Solution()
# B = [1, 2, 5, -7, 2, 3]
# C = A.maxset(B)
# D = [0, 0, -1, 0]
# F = A.maxset(D)
# pass
