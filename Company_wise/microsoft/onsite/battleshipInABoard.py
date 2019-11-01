# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's,
# empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words,
# they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
# where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
#

class Solution(object):
    def markVisited(self, board, visited, cur_row, cur_col):
        visited[cur_row][cur_col] = 1
        neighbours = [[0,1],[1,0],[-1,0],[0,-1]]
        for neighbour in neighbours:
            new_row = cur_row + neighbour[0]
            new_col = cur_col + neighbour[1]
            if new_row >=0 and new_row< len(board) and new_col >=0 and new_col < len(board[0]):
                if board[new_row][new_col] == "X":
                    if neighbour[0] == 1:
                        k = new_row
                        while k <  len(board) and board[k][new_col]=="X":
                            visited[k][new_col] = 1
                            k+=1
                    elif neighbour[0] == -1:
                        k = new_row
                        while k >=0  and board[k][new_col] == "X":
                            visited[k][new_col] = 1
                            k -= 1
                    elif neighbour[1] == 1:
                        k = new_col
                        while k <  len(board[0]) and board[new_row][k]=="X":
                            visited[new_row][k] = 1
                            k += 1
                    elif neighbour[1] == -1:
                        k = new_col
                        while k >=0 and board[new_row][k]=="X":
                            visited[new_row][k] = 1
                            k-=1
                    break


    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) ==0:
            return 0
        battleship_count = 0
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="X" and visited[i][j]==0:
                    self.markVisited(board, visited,i , j)
                    battleship_count +=1
        return battleship_count



obj = Solution()
board = [["X",".","X","."],
         [".","X",".","X"],
         ["X","","X","."]]
print obj.countBattleships(board)

board = [["X",".","X",".","X"],
         ["X",".","X",".","."]]
print obj.countBattleships(board)
board = [["."]]
print obj.countBattleships(board)