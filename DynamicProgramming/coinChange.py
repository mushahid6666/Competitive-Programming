import sys, copy

class Solution(object):
    def computerMinCoins(self,coins, amount, cur_sum, num_of_coins):
        if cur_sum > amount:
            return

        if cur_sum == amount:
            self.min_coins_required = min(self.min_coins_required, num_of_coins)
            return

        for i in range(len(coins)):
            if (cur_sum  + coins[i]) <= amount:
                self.computerMinCoins(coins, amount, cur_sum + coins[i], num_of_coins + 1)

coins = [ 186, 419, 83, 408]
amount = 6249
obj = Solution()
print obj.coinChange(coins, amount)


#Previous Attempted accepted Solution
class Solution2(object):
    min_coin_required = int()

    def getMinCoinRequired(self, coins, current_sum, current_coin_cout, target_amount):
        if current_sum == target_amount:
            self.min_coin_required = min(current_coin_cout, self.min_coin_required)

        if current_sum > target_amount:
            return
        else:
            if current_sum < target_amount:
                for i in range(len(coins) - 1, -1, -1):
                    if current_sum + coins[i] <= target_amount:
                        new_sum = copy.deepcopy(current_sum) + coins[i]
                        new_coin_cout = copy.deepcopy(current_coin_cout) + 1
                        prev_min_coin = copy.deepcopy(self.min_coin_required)
                        self.getMinCoinRequired(coins, new_sum, new_coin_cout,
                                                target_amount)
                        if self.min_coin_required < prev_min_coin:
                            return

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        coins.sort()
        self.min_coin_required = sys.maxint

        self.getMinCoinRequired(coins, 0, 0, amount)
        if self.min_coin_required == sys.maxint:
            return -1
        return self.min_coin_required

