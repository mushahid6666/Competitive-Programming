
class Solution(object):
    def findPeakRecursiveBS(self, nums, low, high):
        if low == high:
            return low
        mid =( low + high) / 2
        if nums[mid] > nums [mid+1]:
            return self.findPeakRecursiveBS(nums,low, mid)
        else:
            return self.findPeakRecursiveBS(nums, mid + 1, high)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findPeakRecursiveBS(nums, 0 , len(nums)-1)
        # if len(nums) == 1:
        #     return 0
        # for i in range(len(nums)):
        #     if i == 0:
        #         if nums[i] > nums[i+1]:
        #             return i
        #     elif i == len(nums) - 1:
        #         if nums[i] > nums[i-1]:
        #             return i
        #     elif nums[i] > nums[i-1] and nums[i] > nums [i + 1]:
        #         return i

obj = Solution()
# Input:
nums = [1,2,3,1]
# Output: 2
print obj.findPeakElement(nums)

nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
print obj.findPeakElement(nums)

nums = [-1,2]
# Output: 1 or 5
print obj.findPeakElement(nums)
# nums = [1,2,3,1]
# # Output: 2
# print obj.findPeakElement(nums)
#
# nums = [1,2,3,1]
# # Output: 2
# print obj.findPeakElement(nums)
#
# nums = [1,2,3,1]
# # Output: 2
# print obj.findPeakElement(nums)