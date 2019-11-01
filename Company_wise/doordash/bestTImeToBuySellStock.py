import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_stock_value = sys.maxint
        for i in range(len(prices)):
            if min_stock_value < prices[i]:
                max_profit = max(max_profit, prices[i] - min_stock_value)
            min_stock_value = min(min_stock_value, prices[i])
        return max_profit
solObj = Solution()
stockPrices = [7,1,5,3,6,4]
stockPrices = [7,6,4,3,1]
print solObj.maxProfit(stockPrices)