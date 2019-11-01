import math
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            return
        self.nums = nums
        sqrtN = float(math.sqrt(len(nums)))
        self.partition = int(math.ceil(len(nums)/sqrtN))
        self.sumArrBlocks = [0] * len(nums)
        for i in range(len(nums)):
            self.sumArrBlocks[i/self.partition] += nums[i]
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        if len(self.nums) == 0:
            return
        block = i/self.partition
        self.sumArrBlocks[block] = self.sumArrBlocks[block] - self.nums[i] + val
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.nums) == 0:
            return
        result = 0
        startBlock = i/self.partition
        endBlock = j/self.partition
        if startBlock == endBlock:
            for k in range(i,j+1):
                result += self.nums[k]
        else:
            for k in range(i, (startBlock + 1) * self.partition):
                result += self.nums[k]
            for k in range(startBlock +1 , endBlock ):
                result += self.sumArrBlocks[k]
            for k in range(endBlock * self.partition, j+1 ):
                result += self.nums[k]
        return result

# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print obj.sumRange(0,0)
obj.update(1,2)
print obj.sumRange(2,2)
# obj.update(0,2)
# print obj.sumRange(0,2)
# obj.update(2,6)
# print obj.sumRange(0,2)
# obj.update(0,-1)
# print obj.sumRange(0,2)
# print obj.sumRange(0,2)