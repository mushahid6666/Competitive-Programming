import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        threeSumClosestDifference = sys.maxint
        for i in range(len(nums)-2):
            num1 = nums[i]
            twoSumTarget = target - num1
            low = i+1
            high = len(nums) - 1

            while low < high:
                curThreeSumClosestDifference = abs(target - (num1 + nums[low] + nums[high]))
                if curThreeSumClosestDifference < threeSumClosestDifference:
                    threeSumClosestDifference = curThreeSumClosestDifference
                    sum = num1 + nums[low] + nums[high]
                if nums[low] + nums[high] > twoSumTarget:
                    high = high - 1
                else:
                    low = low + 1
        return sum



nums = [-1, 2, 1, -4]
target = 1

#Expected 2 : (-1 + 2 + 1 = 2)
solObject = Solution()
print solObject.threeSumClosest(nums, target)
