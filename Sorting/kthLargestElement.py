class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Using a array of size = k
        if len(nums)== 1:
            return nums[0]
        i = 0
        largetKArr = []
        while i < k :
            number = nums[i]
            index = 0
            while index < len(largetKArr) and largetKArr[index] < number:
                index+=1
            largetKArr.insert(index, number)
            i+=1
        # print largetKArr
        while i < len(nums):
            number = nums[i]
            index = 0
            if number >= largetKArr[0]:
                while index < len(largetKArr) and largetKArr[index] < number:
                        index += 1
                largetKArr.pop(0)
                largetKArr.insert(index-1, number)
            i+=1
            # print largetKArr
        return largetKArr[0]
        #Sorting
        {
        # if k == 1 and len(nums) == 1:
        #     return nums[0]
        # nums.sort()
        # n = len(nums)
        # return nums[n-k]
        }

obj = Solution()
arr = [3,2,1,5,6,4,10]
k = 4
print obj.findKthLargest(arr, k)
arr = [3,2,3,1,2,4,5,5,6]
k = 4
print obj.findKthLargest(arr, k)
arr =[-1,2,0]
k = 2
print obj.findKthLargest(arr, k)
arr = [5,2,4,1,3,6,0]
k = 4
print obj.findKthLargest(arr, k)
