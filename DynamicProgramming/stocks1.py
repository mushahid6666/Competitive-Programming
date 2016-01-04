__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit = 0
        for i in range(1, len(A)):
            diff = A[i] - A[i - 1]
            if diff > 0:
                profit += diff
        return profit


obj = Solution()
arr = [10, -6, -3, 7, 8, -1]
obj.stocks(arr)
