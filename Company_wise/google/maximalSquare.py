'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix) )]
        max_square = 0
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i] == 1:
                max_square = 1
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                max_square = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                max_square = max(max_square, dp[i][j])
        return max_square * max_square

obj = Solution()
matrix = [["1","1","1","0","0"],
          ["1","1","1","0","0"],
          ["1","1","1","1","1"],
          ["0","1","1","1","1"],
          ["0","1","1","1","1"],
          ["0","1","1","1","1"]]

print obj.maximalSquare(matrix)