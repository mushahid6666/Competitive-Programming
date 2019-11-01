# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
class Solution(object):
    def binarySearchSortedRotated(self, nums, target, low, high):
        if low == high:
            return nums[low]
        while low <= high:
            if low == high:
                if nums[low] != target:
                    return -1
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            if nums[low] == nums[mid] == nums[high]:
                low = low + 1
                high = high - 1
            elif nums[mid] >= nums[low]:
                if target>= nums[low] and target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearchSortedRotated(nums, target, 0, len(nums)-1 )

obj = Solution()
# nums = [4,5,6,7,0,1,2]
# target = 0
# print  obj.search(nums, target)
# nums = [4,5,6,7,0,1,2]
# target = 3
# print  obj.search(nums, target)

# nums = [4,5,6,-1,0,1,2]
# target = 6
# print  obj.search(nums, target)
nums = [1,3,1,1,1]
target = 3
print  obj.search(nums, target)