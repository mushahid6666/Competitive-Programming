class Solution(object):
    def getIndex(self, nums, low, high, left, target):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)/2

            if nums[mid] > target or (left and nums[mid] == target):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        if n == 0:
            return [-1, -1]
        if n == 1 and nums[0] == target:
            return [0, 0]
        targetRangeStart = self.getIndex(nums, 0 , n-1, True, target)

        if targetRangeStart == n or nums[targetRangeStart] != target:
            return [-1, -1]

        targetRangeEnd = self.getIndex(nums,  False, target) - 1
        return [targetRangeStart, targetRangeEnd]

objSolution = Solution()
nums = [5,7,7,8,8,10]
target = 8
# nums = [2, 2]
# target = 1
print objSolution.searchRange(nums, target)