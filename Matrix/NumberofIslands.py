__author__ = 'mushahidalam'


class Solution(object):
    def isSafe(self, grid, i, j, visited, ROW, COL):
        if (i >= 0 and i < ROW and j >= 0 and j < COL and grid[i][j] == "1" and visited[i][j] == 0):
            return 1

    def DFS(self, grid, i, j, visited, Row, Col):
        rowno = [-1, 0, 0, 1]
        colno = [0, -1, 1, 0]
        visited[i][j] = 1
        for k in range(0, 4):
            if self.isSafe(grid, i + rowno[k], j + colno[k], visited, Row, Col):
                self.DFS(grid, i + rowno[k], j + colno[k], visited, Row, Col)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        # if len(grid)==1 and len(grid[0])==1 and grid[0][0]==1:
        #     return 0
        count = 0
        Row = len(grid)
        Col = len(grid[0])
        visited = [[0] * Col for _ in range(Row)]
        for i in range(Row):
            for j in range(Col):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    self.DFS(grid, i, j, visited, Row, Col)
                    count += 1
        return count


obj = Solution()
grid = ["1111111",
        "0000001",
        "1111101",
        "1000101",
        "1010101",
        "1011101",
        "1111111"]
print obj.numIslands(grid)
