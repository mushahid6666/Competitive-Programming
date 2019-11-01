class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit1 = 0
        max_profit2 = 0
        i = 0
        j = i+1
        n = len(prices)
        while i < n-1 and j < n:
            if prices[j] > prices[j-1] and prices[j] > prices[i]:
                j+=1
                continue
            else:
                if j-1 !=i:
                    profit = prices[j-1] - prices[i]
                    if profit > max_profit1:
                        max_profit2 = max_profit1
                        max_profit1 = profit
                    elif profit > max_profit2:
                        max_profit2 = profit
                i=j
                j=i+1
        if i< n-1:
            profit = prices[j - 1] - prices[i]
            if profit > max_profit1:
                max_profit2 = max_profit1
                max_profit1 = profit
            elif profit > max_profit2:
                max_profit2 = profit
        return max_profit1 + max_profit2
solobj = Solution()
prices = [3,3,5,0,0,3,1,4]
print solobj.maxProfit(prices)
prices = [1,2,3,4,5]
print solobj.maxProfit(prices)
prices = [7,6,4,3,1]
print solobj.maxProfit(prices)
prices = [7]
print solobj.maxProfit(prices)
prices = [7,10]
print solobj.maxProfit(prices)
prices = [1,2,4,2,5,7,2,4,9,0]

print solobj.maxProfit(prices)
