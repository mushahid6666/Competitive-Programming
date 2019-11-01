
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        result = []
        deque = []
        if k==0:
            max_num = nums[0]
            for i in range(1,len(nums)):
                max_num = max(max_num, nums[i])
            return [max_num]
        for i in range(0, k):
            while len(deque)!=0 and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
        for i in range(k, len(nums)):
            result.append(nums[deque[0]])
            while len(deque)!=0 and nums[i] >= nums[deque[-1]]:
                deque.pop()
            while len(deque)!=0 and deque[0] <= i-k:
                deque.pop(0)
            deque.append(i)

        result.append(nums[deque[0]])
        return result


obj = Solution()
# nums = [1,3,-1,-3,5,3,6,7]
# k = 0
# print obj.maxSlidingWindow(nums, k)
# nums = [1]
# k = 1
# print obj.maxSlidingWindow(nums, k)
nums = [1,3,1,2,0,5]
k = 3
print obj.maxSlidingWindow(nums, k)