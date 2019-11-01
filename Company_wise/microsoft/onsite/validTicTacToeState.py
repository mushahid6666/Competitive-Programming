class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        first, second = 'XO'
        x_count = sum(row.count(first) for row in board)
        o_count = sum(row.count(second) for row in board)
        def win(board, player):
            for i in xrange(3):
                if all(board[i][j] == player for j in xrange(3)):
                    return True
                if all(board[j][i] == player for j in xrange(3)):
                    return True
                if (board[0][0] == board[1][1] == board[2][2] == player or
                    board[2][0] == board[1][1] == board[0][2] == player):
                    return True

        if o_count not in {x_count, x_count-1}: return False
        if win(board, first) and x_count -1 != o_count: return False
        if win(board, second) and x_count != o_count: return False
        return True

obj = Solution()
board = ["O  ","   ","   "]
print obj.validTicTacToe(board)
board = ["XOX", " X ", "   "]
print obj.validTicTacToe(board)
board = ["XXX", "   ", "OOO"]
print obj.validTicTacToe(board)
board = ["XXX", "   ", "OOO"]
print obj.validTicTacToe(board)
board = ["XOX", "O O", "XOX"]
print obj.validTicTacToe(board)