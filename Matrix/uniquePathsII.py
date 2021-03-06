import sys
class Solution(object):
    #Time Limit Exceeded recursive Solution
    def recursiveSearch(self, board, i, j, path_exist):
        rows = len(board)
        cols = len(board[0])

        if  i >=rows or j >= cols:
            return None

        if  board[i][j]==1:
            return None

        if path_exist[i][j] != 0:
            return path_exist[i][j]

        if i==rows-1 and j == cols-1:
            return 1

        path_count1 = self.recursiveSearch(board,   i+1, j, path_exist)
        path_count2 = self.recursiveSearch(board,   i, j + 1, path_exist)
        # print path_count1, path_count2, path_exist[i][j]
        if path_count1 != None:
            path_exist[i][j] += path_count1
        if path_count2 != None:
            path_exist[i][j] += path_count2
        return path_exist[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        if len(grid)==0:
            return 0
        if len(grid)==1 and len(grid[0])==1 and grid[0][0]==1:
            return 0
        if len(grid)==1 and len(grid[0])==1 and grid[0][0]==0:
            return 1

        rows = len(grid)
        cols = len(grid[0])
        if grid[rows-1][cols-1]==1 or grid[0][0]==1:
            return 0
        path_exist = [[0 for _ in range(cols)] for _ in range(rows)]

        path_exist[0][0] = 1
        #Only way to reach the cells of first column is from cell above
        for i in range(1,rows):
            if obstacleGrid[i][0] == 0:
                path_exist[i][0] = path_exist[i-1][0]

        # Only way to reach the cells of first row is from cell to left
        for j in range(1,cols):
            if obstacleGrid[0][j] == 0:
                path_exist[0][j] = path_exist[0][j-1]

        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j]==0:
                    path_exist[i][j] = path_exist[i-1][j] + path_exist[i][j-1]

        # self.recursiveSearch(grid, 0, 0, path_exist)
        # return path_exist[0][0]

        return path_exist[rows-1][cols-1]
obj = Solution()
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print obj.uniquePathsWithObstacles(grid)
grid= [[0,1],
       [1,0]]
print obj.uniquePathsWithObstacles(grid)
grid = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],
        [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],
        [1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],
        [1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],
        [0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],
        [1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
print obj.uniquePathsWithObstacles(grid)
grid = [[0,0]]
print obj.uniquePathsWithObstacles(grid)
grid = [[0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0],
        [0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0],
        [0,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0],
        [0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1],
        [0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0],
        [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1],
        [0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1],
        [1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1],
        [0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1],
        [0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1],
        [0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
        [0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0],
        [0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1],
        [0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1],
        [0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0],
        [0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0],
        [1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1],
        [0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0],
        [0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0],
        [1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0],
        [1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
        [1,0,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0],
        [0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],
        [0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1],
        [0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]]
print obj.uniquePathsWithObstacles(grid)
grid = [[0]]
print obj.uniquePathsWithObstacles(grid)
grid = [[1]]
print obj.uniquePathsWithObstacles(grid)
grid = [[0,1]]
print obj.uniquePathsWithObstacles(grid)
