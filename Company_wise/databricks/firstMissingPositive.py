class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        if len(nums) == 1 :
            if nums[0] != 1:
                return 1
            else:
                return 2

        if 1 not in nums:
            return 1

        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <=0 or nums[i] > n:
                nums[i] = 1

        for i in range(len(nums)):
            if abs(nums[i]) == n:
                nums[0] = -(abs(nums[0]))
            else:
                index = abs(nums[i])
                nums[index] = -(abs(nums[index]))

        for i in range(1,len(nums)):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n
        return n+1

obj = Solution()
nums = [1,2,3]
print obj.firstMissingPositive(nums)