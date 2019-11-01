"""Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldnt be on the border, which means that any 'O' on the border of the board are
not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border
will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically."""
import sys
class Solution(object):
    def flipRegion(self, board, dp, rows, cols, cur_i, cur_j, cur_region):
        if cur_i >=0 and cur_i < rows and cur_j >=0 and cur_j < cols:
            if board[cur_i][cur_j] == "X":
                return True
            if cur_i ==0 or cur_j ==0 or cur_i == rows -1 or cur_j == cols -1:
                return False
            if dp[cur_i][cur_j] == -1:
                return False
            cur_tuple_i_j = tuple([cur_i, cur_j])
            cur_region.add(cur_tuple_i_j)
            neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
            sourrounded = True
            for cur_neigh in neighbours:
                new_i = cur_i + cur_neigh[0]
                new_j = cur_j + cur_neigh[1]
                tuple_ij = tuple([new_i, new_j])
                if tuple_ij in cur_region:
                    continue
                elif board[new_i][new_j] == "O":
                    if dp[cur_i][cur_j] == 1:
                        continue
                    elif dp[cur_i][cur_j] == -1:
                        sourrounded = False
                        break
                    else:
                        sourrounded = self.flipRegion(board, dp, rows, cols, new_i, new_j, cur_region)
                        if not sourrounded:
                            break
            if sourrounded:
                return True
            else:
                dp[cur_i][cur_j] = -1
                return False
        return False



    def solve1(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board) == 1:
            return
        rows = len(board)
        cols = len(board[0])
        if rows == 1 or cols == 1:
            return

        dp = [[sys.maxint for _ in range(cols)] for _ in range(rows)]
        for i in range(1,rows -1):
            for j in range(1, cols -1):
                if board[i][j] == "O" and dp[i][j] != -1:
                    isSourrounded = self.flipRegion(board, dp, rows, cols, i, j, set())
                    if isSourrounded:
                        board[i][j] = "X"

    def markAllCells(self, board, rows, cols, cur_i, cur_j):
        if cur_i >=0 and cur_i < rows and cur_j >=0 and cur_j < cols:
            if board[cur_i][cur_j] == "O":
                board[cur_i][cur_j] = 1
                neighbours = [(1,0),(-1,0),(0,-1),(0,1)]
                for cur_neigh in neighbours:
                    self.markAllCells(board, rows, cols, cur_i +cur_neigh[0], cur_j +cur_neigh[1])

    def solve(self, board):
        if len(board) <= 1 or len(board[0]) <= 1:
            return
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            self.markAllCells(board, rows, cols, i, 0)
            self.markAllCells(board, rows, cols, i, cols-1)
        for j in range(cols):
            self.markAllCells(board, rows, cols, 0, j)
            self.markAllCells(board, rows, cols, rows-1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

obj = Solution()
# board = [["X","X","X","X"],
#          ["X","O","O","X"],
#          ["X","O","O","X"],
#          ["X","X","X","X"]]
#
# obj.solve(board)
# print board
# board = [["O","O","O","O"],
#          ["O","O","O","O"],
#          ["O","O","O","O"],
#          ["O","O","O","O"]]
# obj.solve(board)
# print board
board = [
["X","O","X","O","X","O"],
["O","X","O","X","O","X"],
["X","O","X","O","X","O"],
["O","X","O","X","O","X"]]
obj.solve(board)
print board
