__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if A == None or len(A) < 2:
            return 0
        n = len(A)
        left = [0] * n
        right = [0] * n

        left[0] = 0
        minnum = A[0]
        for i in range(1, n):
            minnum = min(minnum, A[i])
            left[i] = max(left[i - 1], A[i] - minnum)

        right[n - 1] = 0
        maxnum = A[n - 1]
        for i in range(n - 2, -1, -1):
            maxnum = max(maxnum, A[i])
            right[i] = max(right[i + 1], maxnum - A[i])

        profit = 0
        for i in range(n):
            profit = max(profit, left[i] + right[i])

        return profit


A = [1, 2]
obj = Solution()
print obj.maxProfit(A)
