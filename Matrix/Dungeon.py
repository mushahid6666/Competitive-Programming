__author__ = 'mushahidalam'
import sys


class Solution:
    # @param A : list of list of integers
    # @return an integer
    #Attempt 2 11 sept 2019
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon) == 0:
            return 0
        if len(dungeon) == 1 and len(dungeon[0]) == 1:
            if dungeon[0][0] < 0:
                return 1-dungeon[0][0]
            return 1

        rows = len(dungeon)
        cols = len(dungeon[0])

        king_health = [[sys.maxint for _ in range(cols+ 1)] for _ in range(rows+ 1)]

        #will start with health 1 for king to be alive
        king_health[rows][cols-1] = 1
        king_health[rows-1][cols] = 1

        for i in range(rows -1, -1, -1):
            for j in range(cols -1 , -1 , -1):
                minHealth = min(king_health[i + 1][j], king_health[i][j +1]) - dungeon[i][j]
                king_health[i][j] = 1 if minHealth <=0 else minHealth

        # self.recursiveSearch(dungeon, 0, 0, king_health)
        # return king_health[0][0]

        return king_health[0][0]

    #Previous Solution
    # def calculateMinimumHP(self, dungeon):
    #     m = len(dungeon)
    #     n = len(dungeon[0])
    #     dp = [[sys.maxint for x in range(n + 1)] for x in range(m + 1)]
    #     dp[m][n - 1] = 1;
    #     dp[m - 1][n] = 1
    #     for i in range(m - 1, -1, -1):
    #         for j in range(n - 1, -1, -1):
    #             minht = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
    #             dp[i][j] = 1 if minht <= 0 else minht
    #     return dp[0][0]


A = [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]

obj = Solution()
A = [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]
A = [[-10]]
A = [[0]]
A = [[20]]

print obj.calculateMinimumHP(A)
