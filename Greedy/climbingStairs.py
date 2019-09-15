# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution(object):
    def __init__(self):
        self.total_ways = 0
        self.memo = list()
    def countStepsToTop(self, i , n):
        if i == n:
            return 1
        if i > n :
            return 0
        if self.memo[i] != 0:
            return self.memo[i]
        count1 = self.countStepsToTop(i + 1, n)
        count2 = self.countStepsToTop(i + 2, n)
        self.memo[i] = self.memo[i] + count1 + count2
        return self.memo[i]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.__init__()
        self.memo = [0] * (n+1)
        self.countStepsToTop(0, n)
        # print self.memo
        return self.memo[0]


obj = Solution()
print obj.climbStairs(4), "Expected : 2"
print obj.climbStairs(3), "Expected : 3"
print obj.climbStairs(1), "Expected : 1"
print obj.climbStairs(2), "Expected : 2"
print obj.climbStairs(35), "Expected : 2"

