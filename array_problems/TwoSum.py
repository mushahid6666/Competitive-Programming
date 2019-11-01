__author__ = 'mushahidalam'

class Solution(object):


    #Previous SOlution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numberDict = dict()
        for i in range(len(nums)):
            if nums[i] in numberDict:
                numberDict[nums[i]].append(i)
            else:
                numberDict[nums[i]] = [i]
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in numberDict:
                if num1 == num2:
                    if len(numberDict[num1]) > 1:
                        index_list = numberDict[num1]
                        for k in range(len(index_list)):
                            if index_list[k] != i:
                                return [i, index_list[k]]
                    continue
                return [i, numberDict[num2][0]]
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]]= i
        for k in range(len(nums)):
            num1 = nums[k]
            req_num2 = target - num1
            if req_num2 in hash_map and k != hash_map[req_num2]:
                return [k, hash_map[req_num2]]
        return []

        # num_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in num_dict:
        #         num_dict[nums[i]].append(i)
        #     else:
        #         num_dict[nums[i]] = [i]
        # for i in range(len(nums)):
        #     num1 = nums[i]
        #     num2 = target - num1
        #     if num2 in num_dict and i != num_dict[num2][0]:
        #         if num1 == num2:
        #             return [num_dict[num1][0], num_dict[num2][1]]
        #         return [num_dict[num1][0], num_dict[num2][0]]
        # return []

two_sum_obj = Solution()
print two_sum_obj.twoSum([2, 2, 2], 4) # Expected : [1,2]
