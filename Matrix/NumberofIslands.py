__author__ = 'mushahidalam'


class Solution(object):
    #Attempt2:
    def markVisited(self, grid, visited, i, j, rows, columns):
        if j >= columns or i >= rows or i < 0 or j < 0:
            return
        if grid[i][j] == "1" and visited[i][j] == "0":
            visited[i][j] = "1"
            self.markVisited(grid, visited, i+1, j, rows, columns)
            self.markVisited(grid, visited, i , j + 1, rows, columns)
            self.markVisited(grid, visited, i , j - 1, rows, columns)
            self.markVisited(grid, visited, i - 1, j, rows, columns)
        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        visited = [["0" for _ in range(columns)] for _ in range(rows)]
        island_count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and visited[i][j] == "0":
                    island_count = island_count + 1
                    self.markVisited(grid, visited, i, j, rows, columns)
        return island_count

test_island =[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
    ]
solutionObj = Solution()
print solutionObj.numIslands(test_island)

test_island = [
    ["1", "1", "1", "1", "1", "1", "1"],
    ["0", "0", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1"]]
print solutionObj.numIslands(test_island)

test_island = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
print solutionObj.numIslands(test_island)

test_island = [
["0"]
]
print solutionObj.numIslands(test_island)

test_island = [
["1"]
]
print solutionObj.numIslands(test_island)

test_island = []
print solutionObj.numIslands(test_island)

test_island = [
["1","0","1","0","1"],
["0","1","0","1","0"],
["1","0","1","0","1"],
["0","1","0","1","0"]
]
print solutionObj.numIslands(test_island)
#Previous Accepted Leetcode Solution
    # def isSafe(self, grid, i, j, visited, ROW, COL):
    #     if (i >= 0 and i < ROW and j >= 0 and j < COL and grid[i][j] == "1" and visited[i][j] == 0):
    #         return 1
    #
    # def DFS(self, grid, i, j, visited, Row, Col):
    #     rowno = [-1, 0, 0, 1]
    #     colno = [0, -1, 1, 0]
    #     visited[i][j] = 1
    #     for k in range(0, 4):
    #         if self.isSafe(grid, i + rowno[k], j + colno[k], visited, Row, Col):
    #             self.DFS(grid, i + rowno[k], j + colno[k], visited, Row, Col)
    #
    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     if len(grid) == 0:
    #         return 0
    #     # if len(grid)==1 and len(grid[0])==1 and grid[0][0]==1:
    #     #     return 0
    #     count = 0
    #     Row = len(grid)
    #     Col = len(grid[0])
    #     visited = [[0] * Col for _ in range(Row)]
    #     for i in range(Row):
    #         for j in range(Col):
    #             if grid[i][j] == "1" and visited[i][j] == 0:
    #                 self.DFS(grid, i, j, visited, Row, Col)
    #                 count += 1
    #     return count

