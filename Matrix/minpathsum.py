__author__ = 'mushahidalam'
# Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]

        rows = len(grid)
        cols = len(grid[0])

        path_exist = [[0 for _ in range(cols)] for _ in range(rows)]

        path_exist[0][0] = grid[0][0]
        # Only way to reach the cells of first column is from cell above
        for i in range(1, rows):
            path_exist[i][0] = grid[i][0] + path_exist[i - 1][0]

        # Only way to reach the cells of first row is from cell to left
        for j in range(1, cols):
            path_exist[0][j] = grid[0][j] + path_exist[0][j - 1]

        for i in range(1, rows):
            for j in range(1, cols):
                path_exist[i][j] = min(path_exist[i - 1][j], path_exist[i][j - 1]) + grid[i][j]

        # self.recursiveSearch(grid, 0, 0, path_exist)
        # return path_exist[0][0]

        return path_exist[rows - 1][cols - 1]

obj = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
# Output: 7
print obj.minPathSum(grid)
grid = [[0]]
print obj.minPathSum(grid)
grid = []
print obj.minPathSum(grid)
grid = [[1,1],
        [2,1]]
print obj.minPathSum(grid)
grid = [[1,0],
        [2,1]]
print obj.minPathSum(grid)
