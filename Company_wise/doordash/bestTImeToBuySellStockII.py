class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        i = 0
        j = 1
        n= len(prices)
        while i < n-1 and j < n:
            if prices[j] > prices[j-1] and prices[j] > prices[i]:
                j+=1
                continue
            else:
                if j -1 != i:
                    profit = prices[j-1] - prices[i]
                    max_profit += profit
                i = j
                j= i+1
        if i < n-1:
            max_profit += prices[j-1] - prices[i]

        return max_profit


solObject = Solution()
prices = [ 7, 1, 5, 3, 10, 4]
print solObject.maxProfit(prices), "Expected: 11"
prices = [1,2,3,4,5]
print solObject.maxProfit(prices), "Expected: 4"
prices = [7,6,4,3,1]
print solObject.maxProfit(prices), "Expected: 0"
prices = [7,1,5,3,6,4]
print solObject.maxProfit(prices), "Expected: 7"
prices = []
print solObject.maxProfit(prices), "Expected: 0"
