__author__ = 'mushahidalam'


# class Solution:
#     # @param A : tuple of integers
#     # @param B : integer
#     # @return a list of integers
#     def slidingMaximum(self, A, B):
#         result = []
#         n = len(A)
#         if B >= n:
#             maxnum = A[0]
#             for i in range(1, n):
#                 if A[i] > maxnum:
#                     maxnum = A[i]
#             return [maxnum]
#         deque = []
#         for i in range(0, B):
#             while (len(deque) != 0 and A[i] >= A[deque[-1]]):
#                 deque.pop()
#             deque.append(i)
#         for i in range(B, n):
#             result.append(A[deque[0]])
#             while (len(deque) != 0 and A[i] >= A[deque[-1]]):
#                 deque.pop()
#             while (len(deque) != 0 and deque[0] <= i - B):
#                 deque.pop(0)
#             deque.append(i)
#         result.append(A[deque[0]])
#         return result


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        if n == 0:
            return []
        if n == 1 and k == 1:
            return nums
        if k == 0:
            return []
        if k >= n:
            maxnum = nums[0]
            for i in range(1, n):
                if nums[i] > maxnum:
                    maxnum = nums[i]
            return [maxnum]
        deque = []
        for i in range(0, k):
            while (len(deque) != 0 and nums[i] >= nums[deque[-1]]):
                deque.pop()
            deque.append(i)
        for i in range(k, n):
            result.append(nums[deque[0]])
            while (len(deque) != 0 and nums[i] >= nums[deque[-1]]):
                deque.pop()
            while (len(deque) != 0 and deque[0] <= i - k):
                deque.pop(0)
            deque.append(i)
        result.append(nums[deque[0]])
        return result


obj = Solution()
arr = (1, 3, -1, -3, 5, 3, 6, 7)
# output = [3 3 5 5 6 7]
output = obj.maxSlidingWindow(arr, 7)
print output
