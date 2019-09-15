class Solution(object):

    def robHouseRecursive(self, nums, i, memo):
        if i >= len(nums):
            return 0
        if i==len(nums)-1:
            return nums[i]
        if memo[i] != -1:
            return memo[i]
        result =  max(self.robHouseRecursive(nums, i + 1, memo), nums[i] + self.robHouseRecursive(nums, i+2, memo))
        memo[i] = result
        return result

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [-1] * (len(nums) + 1)
        # result =  self.robHouseRecursive(nums, 0, memo)
        # print memo
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i + 1] = max(memo[i - 1] + val, memo[i])
        return memo[len(nums)]






obj = Solution()
nums = [2,3,2]
print obj.rob(nums)
nums = [1,2,3,1]
print obj.rob(nums)
nums =[50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1,50,20,10,40,200,1, 100,2,1]
print obj.rob(nums)
nums =[10,20,30,100,2,1]
print obj.rob(nums)
nums =[2,7,9,3,1]
print obj.rob(nums)
nums =[2,7]
print obj.rob(nums), "Expected: 7"
nums = [2,1,1,2]
print obj.rob(nums), "Expected: 4"
