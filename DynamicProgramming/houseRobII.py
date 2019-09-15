import copy


class Solution(object):

    def robHouseRecursive(self, nums, i, memo):
        if i >= len(nums):
            return 0
        if i == len(nums) - 1:
            return nums[i]
        if memo[i] != -1:
            return memo[i]
        result = max(self.robHouseRecursive(nums, i + 1, memo), nums[i] + self.robHouseRecursive(nums, i + 2, memo))
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

        memo1 = [-1] * (len(nums))
        memo2 = [-1] * (len(nums))
        # print nums[:-1], nums[1:]
        result =  max(self.robHouseRecursive(nums[:-1], 0, memo1), self.robHouseRecursive(nums[1:], 0, memo2))
        return result
        # print memo

        #Crappy Iterative
        # nums1 = copy.deepcopy(nums)
        # nums2 = copy.deepcopy(nums)
        # nums1.pop(0)
        # nums2.pop(-1)
        #
        # memo1 = [-1] * (len(nums1) + 1)
        # memo1[0] = 0
        # memo1[1] = nums[0]
        # for i in range(1, len(nums1)):
        #     val = nums1[i]
        #     memo1[i + 1] = max(memo1[i - 1] + val, memo1[i])
        #
        # memo2 = [-1] * (len(nums2) + 1)
        # memo2[0] = 0
        # memo2[1] = nums2[0]
        # for i in range(1, len(nums2)):
        #     val = nums2[i]
        #     memo2[i + 1] = max(memo2[i - 1] + val, memo2[i])
        # return max(memo1[len(nums1)], memo2[len(nums2)])


obj = Solution()
nums = [1,2,1,1]
print obj.rob(nums)
nums = [2, 3, 2]
print obj.rob(nums)
nums = [1, 2, 3, 1]
print obj.rob(nums)
nums = [50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20,
        10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40,
        200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1,
        100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2,
        1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50,
        20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10,
        40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40,
        200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1,
        100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2,
        1, 50, 20, 10, 40, 200, 1, 100, 2, 1, 50, 20, 10, 40, 200, 1, 100, 2, 1]
print obj.rob(nums)
nums = [10, 20, 30, 100, 2, 1]
print obj.rob(nums)
nums = [2, 7, 9, 3, 1]
print obj.rob(nums)
nums = [2, 7]
print obj.rob(nums), "Expected: 7"
nums = [2, 1, 1, 2]
print obj.rob(nums), "Expected: 4"
