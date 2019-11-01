import copy
class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 :
            return []
        if len(nums) == 1:
            return nums
        color_copy = [1 for _ in range(len(nums))]
        zero_index = 0
        two_index = len(nums)- 1
        for i in range(len(nums)):
            if nums[i]== 0:
                color_copy[zero_index] = 0
                zero_index +=1
            elif nums[i] == 2:
                color_copy[two_index] = 2
                two_index -= 1
        return color_copy

    def sortColors(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        zero_index = 0
        two_index = len(nums) -1
        i = 0
        while i <= two_index:
            if nums[i] == 0:
                nums[i] = nums[zero_index]
                nums[zero_index] = 0
                zero_index += 1
                i+=1
            elif nums[i] == 2:
                nums[i] = nums[two_index]
                nums[two_index] = 2
                two_index -= 1
            else:
                i+=1
        return nums



obj = Solution()
arr = [2,0,2,1,1,0]
print obj.sortColors(arr)
arr = [1,1,0]
print obj.sortColors(arr)
arr = [2,0,2,1,0,2]
print obj.sortColors(arr)
arr = [2,0,1]
print obj.sortColors(arr)
