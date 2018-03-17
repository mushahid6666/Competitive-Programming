class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 2:
            return [0, 1]
        ele_dict = dict()
        for i in range(0, n):
            ele_dict[nums[i]] = i
        for j in range(0, n):
            ele1 = nums[j]
            diff = target - ele1
            if diff in ele_dict and ele_dict[diff] != j:
                return [j, ele_dict[diff]]


obj = Solution()
print obj.twoSum([2, 3, 5, 7, 8, 1], 8)




# previous Solution
# num_dict = dict()
# for k in range(len(nums)):
#     if nums[k] not in num_dict:
#         num_dict[nums[k]] = k
# for i in range(len(nums)):
#     num1 = nums[i]
#     if target <> num1:
#         num2 = nums[i] - target
#     else:
#         num2 = target - nums[i]
#     if num2 in num_dict:
#         return [i, k]
# return []
