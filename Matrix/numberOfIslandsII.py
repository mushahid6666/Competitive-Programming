class Solution(object):

    def checkIfNewIsland(self, grid, i, j, m , n):

        if i+1>=0 and i+1 <m  and j >=0 and j < n and grid[i+1][j] == 1:
            return False
        if i>=0 and i <m  and j+1 >=0 and j+1 < n and grid[i][j+1] == 1:
            return False
        if i-1>=0 and i-1 <m  and j >=0 and j < n and grid[i-1][j] == 1:
            return False
        if i>=0 and i <m  and j-1 >=0 and j-1 < n and grid[i][j-1] == 1:
            return False
        return True

    def compare(self, p1, p2):
        if p1[0] < p2[0]:
            return -1
        elif p1[0] > p2[0]:
            return 1
        else:
            if p1[1] <p2[1]:
                return -1
            elif p1[0] > p2[0]:
                return 1
            else:
                return 0


    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        positions.sort(self.compare)
        if len(positions) == 0 or m ==0 or n ==0:
            return [0]
        grid = [[0 for _ in range(n)] for j in range(m)]
        result = []
        num_islands = 0
        for new_island in positions:
            isNewIsland = self.checkIfNewIsland(grid, new_island[0], new_island[1],m , n)
            if isNewIsland:
                num_islands += 1
            result.append(num_islands)
            grid[new_island[0]][new_island[1]] = 1
        return result


obj = Solution()
m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
print obj.numIslands2(m, n, positions)
m = 1
n = 3
positions = [[0,0],[0,1],[0,2]]
print obj.numIslands2(m, n, positions)
m = 0
n =0
positions = []
print obj.numIslands2(m, n, positions)
m = 2
n = 2
positions = [[0,0],[1,1],[0,1]]
print obj.numIslands2(m, n, positions)
