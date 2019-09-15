class Solution(object):
    def recursiveSearch(self, board, i, j, cur_non_obst_cell, max_non_obstacle_cells):
        rows = len(board)
        cols = len(board[0])

        if i<0 or j <0 or i >=rows or j >= cols:
            return

        if board[i][j]=="#" or board[i][j]==-1:
            return

        if board[i][j]==2 and cur_non_obst_cell == max_non_obstacle_cells:
            self.result += 1
            return

        tmp = board[i][j]
        if board[i][j] != 1:
            cur_non_obst_cell+= 1
        board[i][j]="#"
        self.recursiveSearch(board,   i+1, j, cur_non_obst_cell, max_non_obstacle_cells)
        self.recursiveSearch(board,  i-1, j, cur_non_obst_cell, max_non_obstacle_cells)
        self.recursiveSearch(board,   i, j + 1, cur_non_obst_cell, max_non_obstacle_cells)
        self.recursiveSearch(board,  i, j-1 , cur_non_obst_cell, max_non_obstacle_cells)
        board[i][j] = tmp

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        non_obstacle_cells = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    non_obstacle_cells+=1

        self.result = 0

        result = 0
        found_start_square = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    self.recursiveSearch(grid, i, j, 0, non_obstacle_cells)
                    found_start_square = True
                    break
            if found_start_square:
                break
        return self.result

obj = Solution()
grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]
grid = [[1,-1,2]]
print obj.uniquePathsIII(grid)
