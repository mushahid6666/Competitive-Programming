"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def __init__(self):
        self.longestduplicateCount = 0
    def dfs_traverse(self, grid, m, n, cur_row, cur_col, visited, number):
        if cur_row >=0 and cur_row < m and cur_col >=0 and cur_col < n:
            if visited[cur_row][cur_col] ==1:
                return 0
            count = 0
            if grid[cur_row][cur_col] != number:
                return 0
            #cur cell is same duplicate number
            count +=1
            visited[cur_row][cur_col] = 1
            grid[cur_row][cur_col]= "#"

            #visit all neighbours
            negihbours = [(0,1),(1,0),(-1,0),(0,-1)]
            for cur_neighbour in negihbours:
                count += self.dfs_traverse(grid, m, n, cur_row + cur_neighbour[0], cur_col+ cur_neighbour[1], visited, number)
            visited[cur_row][cur_col] = 0
            return count
        return 0

    def uniquePaths(self, matrix):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        if m==0 or n==0:
            return 0
        if m==1 and n==1:
            return 1
        self.__init__()
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] != "#":
                    count = self.dfs_traverse(matrix, m , n, i, j, visited, grid[i][j])
                    self.longestduplicateCount = max(self.longestduplicateCount, count)
        return self.longestduplicateCount



obj = Solution()
grid = [
    [1,1],
    [5,5],
    [5,5]]
print obj.uniquePaths(grid)