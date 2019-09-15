__author__ = 'mushahidalam'
import math

class Solution:
    # @param A : tuple of integers
    # @return an integer
    #Leetcode Solution
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_size = len(nums)
        majority_required = math.floor(array_size/2)
        if array_size == 1:
            return nums[0]
        element_count_dict = dict()
        for element in nums:
            if element in element_count_dict:
                element_count_dict[element] += 1
            else:
                element_count_dict[element] = 1
        for element in element_count_dict:
            if element_count_dict[element] > majority_required:
                return element
    #Previous Accepted Solution
{
    # def majorityElement(self, A):
    #     n = len(A)
    #     majority = math.floor(n / 2)
    #     dict = {}
    #     for i in A:
    #         if i in dict:
    #             dict[i] = dict[i] + 1
    #         else:
    #             dict[i] = 1
    #     keys = dict.keys()
    #     for i in keys:
    #         if dict[i] > majority:
    #             return i
}


obj = Solution()
arr = [2, 1, 2]
print obj.majorityElement(arr)
