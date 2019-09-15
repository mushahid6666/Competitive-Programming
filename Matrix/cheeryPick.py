import copy
class Solution(object):
    """
    n*n grid
    0 means the cell is empty, so you can pass through;
    1 means the cell contains a cherry, that you can pick up and pass through;
    -1 means the cell contains a thorn that blocks your way.
    find max cherries, 0,0->(n-1,n-1)->0,0
    """

    def compute_down_path_sum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        down_path_grid = [[0 for _ in range(rows)] for _ in range(cols)]
        # compute max sum to reach n-1,n-1
        down_path_grid[0][0] = grid[0][0]
        if grid[0][0] == 1:
            grid[0][0] = 0
        for i in range(1, rows):
            if grid[i][0] != -1 and down_path_grid[i - 1][0] !=-1:
                down_path_grid[i][0] = grid[i][0] + down_path_grid[i - 1][0]
            else:
                down_path_grid[i][0] = -1

        for j in range(1, cols):
            if grid[0][j] != -1 and down_path_grid[0][j-1] != -1:
                down_path_grid[0][j] = grid[0][j] + down_path_grid[0][j - 1]
            else:
                down_path_grid[0][j] = -1

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] != -1:
                    if down_path_grid[i-1][j]== -1 and down_path_grid[i][j-1]==-1:
                        down_path_grid[i][j] = -1
                    else:
                        max_value = max(down_path_grid[i - 1][j], down_path_grid[i][j - 1])
                        down_path_grid[i][j] = max_value + grid[i][j]
                else:
                    down_path_grid[i][j] = -1
        if down_path_grid[rows-1][cols-1] == -1:
            return -1
        i = rows-1
        j = cols-1

        while i !=0 or j!=0:
            if i==0:
                while j!=0:
                    if grid[0][j] == 1:
                        grid[0][j] = 0
                    j = j-1
            elif j==0:
                while i!=0:
                    if grid[i][0] == 1:
                        grid[i][0] = 0
                    i = i-1
            else:
                if down_path_grid[i-1][j] > down_path_grid[i][j-1]:
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    i = i-1

                else:
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    j = j-1


        return down_path_grid[rows-1][cols-1]

    def compute_up_path_sum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        up_path_grid = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows-2, -1, -1):
            if grid[i][cols-1] != -1:
                up_path_grid[i][cols-1] = grid[i][cols-1] + up_path_grid[i + 1][cols-1]
                if grid[i][cols-1] == 1:
                    grid[i][cols-1] = 0

        for j in range(cols-2,-1,-1):
            if grid[rows-1][j] != -1:
                up_path_grid[rows-1][j] = grid[rows-1][j] + up_path_grid[rows-1][j + 1]
                if grid[rows-1][j] == 1:
                    grid[rows-1][j] = 0

        for i in range(rows-2, -1, -1):
            for j in range(cols-2, -2, -1):
                up_path_grid[i][j] = grid[i][j] + max(up_path_grid[i +1][j], up_path_grid[i][j+1])
                if grid[i][j]==1:
                    grid[i][j]=0
        return up_path_grid[0][0]


    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        if len(grid)==1 and len(grid[0])==1:
            if grid[0][0] != -1:
                return grid[0][0]
            return 0

        down_path_sum = self.compute_down_path_sum(grid)
        if down_path_sum == -1:
            return 0
        up_path_sum = self.compute_up_path_sum(grid)
        return up_path_sum + down_path_sum



obj = Solution()
grid =[[0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]]
#Expected = 5
# grid=[[1,-1],
#       [-1,1]]
# grid=[[0]]
# grid = []
# grid = [[1,1,-1],
#         [1,-1,1],
#         [-1,1,1]]
grid = [[0,1,-1,1],
        [1,0,-1,0],
        [1,1,-1,1],
        [1,-1,-1,1]]
grid = [[1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,1,1,1]]
print obj.cherryPickup(grid)
