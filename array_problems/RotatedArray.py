__author__ = 'mushahidalam'
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

# if a[high] < a[low]
#   if target > a[low]
#      high = mid - 1
#   else:
#      low = mid + 1
class Solution:
    # @param A : tuple of integers
    # @return an integer
    #LEETCODE
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return -1
        low = 0
        high = n -1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[high]: # rotation + left part of array
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:# rotation + right part of array
                if target > nums[mid] and target <= nums[high]:
                    low  = mid + 1
                else:
                    high = mid - 1
            else:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1


        return -1

solObj = Solution()
# nums = [4,5,6,7,0,1,2]
# target = 0
# print "Expected: 4,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,0,1,2]
# target = 6
# print "Expected: 2,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,0,1,2]
# target = 4
# print "Expected: 0,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,8,1,2]
# target = 1
# print "Expected: 5,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,8,9,2]
# target = 2
# print "Expected: 6,Answer:", solObj.search(nums, target)
nums = [9,0,1,2,3,4,5]
target = 9
print "Expected: 0,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,0,1,2,3]
# target = 0
# print "Expected: 4,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,0,1,2,3]
# target = 7
# print "Expected: 3,Answer:", solObj.search(nums, target)
# nums = [4,5,6,7,0,1,2]
# target = 3
# print "Expected: -1,Answer:", solObj.search(nums, target)
# nums = []
# target = 10
# print "Expected: -1,Answer:", solObj.search(nums, target)
# nums = [4]
# target = 4
# print "Expected: 0,Answer:", solObj.search(nums, target)
nums = [5, 1, 3]
target = 3
# print "Expected: 2,Answer:", solObj.search(nums, target)

    #Interviewbit
    # def findMin(self, A):
    #     n = len(A)
    #     low = 0
    #     high = len(A) - 1
    #     if A[low] <= A[high]:
    #         return A[low]
    #     while (low <= high):
    #         mid = (low + high) / 2
    #         if A[mid] <= A[(mid + 1) % n] and A[mid] <= A[(mid + n - 1) % n]:
    #             return A[mid]
    #         elif A[mid] <= A[high]:
    #             high = mid - 1
    #         elif A[mid] >= A[low]:
    #             low = mid + 1
    #     return -1


# obj = Solution()
# arr = [2, 1]
# print obj.findMin(arr)
