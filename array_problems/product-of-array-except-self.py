class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftMult = [1]
        n = len(nums)
        cur_prod = 1
        for i in range(1,len(nums)):
            cur_prod = cur_prod* nums[i-1]
            leftMult.append(cur_prod)
        righMult = [1]
        cur_prod = 1
        for i in range(len(nums) - 2, -1,-1):
            cur_prod = cur_prod * nums[i+1]
            righMult.insert(0, cur_prod)
        result = []
        for i in range(len(nums)):
            result.append(leftMult[i] * righMult[i])
        return result
obj = Solution()
arr = [1,2,3,4]
print obj.productExceptSelf(arr)


class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        product_left = []
        product_right = []
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
            product_left.append(product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product = product * nums[i]
            product_right.insert(0, product)
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(product_right[i + 1])
            elif i == len(nums) - 1:
                result.append(product_left[i - 1])

            else:
                result.append(product_left[i - 1] * product_right[i + 1])
        return result
