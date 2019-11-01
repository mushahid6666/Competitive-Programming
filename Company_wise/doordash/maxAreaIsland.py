"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution(object):
    def markVisitedRecursive(self, grid, i, j, rows, cols, area_count):

        area_count = 0
        negihbours = [(-1,0),(1,0),(0,1),(0,-1)]
        if i >=0 and i < rows and j >=0 and j < cols:
            if grid[i][j] == 1 and self.visited[i][j] == 0:
                area_count += 1
                self.visited[i][j] = 1
                for cur_neighbour in negihbours:
                    area_count += self.markVisitedRecursive(grid, i+ cur_neighbour[0], j+ cur_neighbour[1], rows, cols, area_count)

        return area_count


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        self.visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])

        max_area =0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and self.visited[i][j] == 0:
                    area_count = self.markVisitedRecursive(grid, i, j, rows, cols, 0)
                    max_area = max(max_area, area_count)
        return max_area




solObj = Solution()
grid = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print solObj.maxAreaOfIsland(grid)
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0]]
print solObj.maxAreaOfIsland(grid)
grid = [[0,0,0,0,0,0,0,0]]
print solObj.maxAreaOfIsland(grid)

