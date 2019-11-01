class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        columns = len(board[0])

        board_copy = [[board[row][col] for col in range(columns)] for row in range(rows)]

        for row in range(rows):
            for col in range(columns):

                live_neighbour = 0
                for neighbour in neighbours:
                    r = (row + neighbour[0])
                    c = (col + neighbour[1])

                    if (r >= 0 and r < rows) and (c >= 0 and c < columns) and (board_copy[r][c] == 1 or board_copy[r][c] == -1):
                        live_neighbour += 1

                if board_copy[row][col] == 1 and (live_neighbour < 2 or live_neighbour > 3):
                    board[row][col] = -1

                if board_copy[row][col] == 0 and live_neighbour == 3:
                    board[row][col] = 2
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1

solObj = Solution()
board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]
solObj.gameOfLife(board)
print board
print "Expected"
print "[[0, 0, 0], " \
      "[1, 0, 1], " \
      "[0, 1, 1], " \
      "[0, 1, 0]]"

