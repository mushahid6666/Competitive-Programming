class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = nums[0]
        leftProd = [nums[0]]
        rightProd = [nums[-1]]
        inputLen = len(nums)
        for i in range(1, inputLen):
            leftProd.append(leftProd[i - 1] * nums[i])
        for i in range(inputLen - 2, -1, -1):
            product = rightProd[0] * nums[i]
            rightProd.insert(0, product)
        result = [rightProd[1]]
        for i in range(1, inputLen - 1):
            result.append(leftProd[i - 1] * rightProd[i + 1])
        result.append(leftProd[i])
        return result


productSelf = Solution()
print productSelf.productExceptSelf([0, 2, 3, 4])
