# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
class Solution(object):
    def recurSearchRotatedArr(self, nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high)/ 2
        if nums[mid] > nums[high]:
            return self.recurSearchRotatedArr(nums, mid + 1, high)
        elif nums[mid] < nums[low]:
            return self.recurSearchRotatedArr(nums, low, mid)
        else:
            return self.recurSearchRotatedArr(nums, low, high - 1)

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.recurSearchRotatedArr(nums, 0, len(nums)-1)

obj = Solution()

#
# Example 1:
#
# nums =  [3,4,5,1,2]
# # Output: 1
# print obj.findMin(nums)
# # Example 2:
# #
# nums= [4,5,6,7,0,1,2]
# # Output: 0
# print obj.findMin(nums)
#
# nums= [2,3,-1,1]
# # Output: -1
# print obj.findMin(nums)

nums = [3,3,1,3]
print obj.findMin(nums)

nums = [3,3,1,3,3,3,3,3,3,3]
print obj.findMin(nums)
