class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Second Attempt
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
        for i in range(len(nums)-1, -1, -1):
            product = product * nums[i]
            product_right.insert(0, product)
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(product_right[i+1])
            elif i == len(nums)-1:
                result.append(product_left[i -1])

            else:
                result.append(product_left[i-1] * product_right[i+1])
        return result


        #Previous Solution
        # product = nums[0]
        # leftProd = [nums[0]]
        # rightProd = [nums[-1]]
        # inputLen = len(nums)
        # for i in range(1, inputLen):
        #     leftProd.append(leftProd[i - 1] * nums[i])
        # for i in range(inputLen - 2, -1, -1):
        #     product = rightProd[0] * nums[i]
        #     rightProd.insert(0, product)
        # result = [rightProd[1]]
        # for i in range(1, inputLen - 1):
        #     result.append(leftProd[i - 1] * rightProd[i + 1])
        # result.append(leftProd[i])
        # return result


productSelf = Solution()
print productSelf.productExceptSelf([10, 2, 3, 4])
