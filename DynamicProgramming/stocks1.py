__author__ = 'mushahidalam'
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_price_left = []
        current_maximum = prices[len(prices) - 1]
        for i in range(len(prices)-1, -1, -1):
            current_maximum = max(current_maximum, prices[i])
            max_price_left.insert(0, current_maximum)
        max_profit = int()
        for i in range(len(prices) - 1):
            profit_i =  max_price_left[i + 1] - prices[i]
            max_profit = max (max_profit, profit_i)
        return  max_profit

obj = Solution()
prices =[7,1,5,3,6,4]
print obj.maxProfit(prices), "Expected : 5"

prices = [7,6,4,3,1]
print obj.maxProfit(prices), "Expected : 0"

prices = [7,8]
print obj.maxProfit(prices), "Expected : 1"

    #Previous Solution
    # @param A : tuple of integers
    # @return an integer
#     def maxProfit(self, A):
#         profit = 0
#         for i in range(1, len(A)):
#             diff = A[i] - A[i - 1]
#             if diff > 0:
#                 profit += diff
#         return profit
#
#
# obj = Solution()
# arr = [10, -6, -3, 7, 8, -1]
# obj.stocks(arr)
