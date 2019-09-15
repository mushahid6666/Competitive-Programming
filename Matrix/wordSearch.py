# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
import copy
class Solution(object):

    #Ideal Solution
    def recursiveSearch(self, board, word, i, j):
        if len(word) == 0:
            return True
        rows = len(board)
        cols = len(board[0])
        if i<0 or j <0 or i >=rows or j >= cols:
            return False
        if board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j]="#"

        result = (self.recursiveSearch(board,  word[1:], i+1, j)
            or self.recursiveSearch(board,  word[1:], i-1, j)
            or self.recursiveSearch(board,  word[1:], i, j + 1)
            or self.recursiveSearch(board, word[1:], i, j-1) )
        board[i][j] = tmp
        return result
    #Attempt Solution: TIme limit Exceeded
    # def recursiveSearch(self, board, letter_position_dict, word, i, j, except_ij):
    #     if len(word) == 0:
    #         return True
    #     rows = len(board)
    #     cols = len(board[0])
    #
    #     if i + 1 < rows and tuple([i+1,j]) not in except_ij :
    #         if board[i + 1][j] == word[0]:
    #             new_used_cells = copy.deepcopy(except_ij)
    #             new_used_cells.add(tuple([i+1,j]))
    #             result = self.recursiveSearch(board, letter_position_dict, word[1:], i+1, j, new_used_cells)
    #             if result:
    #                 return True
    #     if i - 1 >= 0 and tuple([i-1,j]) not in except_ij :
    #         if board[i - 1][j] == word[0]:
    #             new_used_cells = copy.deepcopy(except_ij)
    #             new_used_cells.add(tuple([i - 1, j]))
    #             result = self.recursiveSearch(board, letter_position_dict, word[1:], i-1, j, new_used_cells)
    #             if result:
    #                 return True
    #     if j + 1 < cols and tuple([i,j+1]) not in except_ij:
    #         if board[i][j + 1] == word[0]:
    #             new_used_cells = copy.deepcopy(except_ij)
    #             new_used_cells.add(tuple([i , j + 1]))
    #             result = self.recursiveSearch(board, letter_position_dict, word[1:], i, j+1, new_used_cells)
    #             if result:
    #                 return True
    #     if j - 1 >= 0 and  tuple([i,j-1]) not in except_ij:
    #         if board[i][j - 1] == word[0]:
    #             new_used_cells = copy.deepcopy(except_ij)
    #             new_used_cells.add(tuple([i , j - 1]))
    #             result = self.recursiveSearch(board, letter_position_dict, word[1:], i, j-1, new_used_cells)
    #             if result:
    #                 return True
    #     return False



    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)== 0:
            return False
        letter_position_dict = dict()
        rows = len(board)
        cols = len(board[0])
        if len(word) > rows * cols:
            return False
        for i in range(rows):
            for j in range(cols):
                letter = board[i][j]
                if letter in letter_position_dict:
                    letter_position_dict[letter].append([i, j])
                else:
                    letter_position_dict[letter] = [[i, j]]
        if word[0] not in letter_position_dict:
            return False
        positions = letter_position_dict[word[0]]
        for position in positions:
            i = position[0]
            j = position[1]
            except_ij = set()
            except_ij.add(tuple([i,j]))
            # result = self.recursiveSearch(board, letter_position_dict, word[1:], i, j, except_ij)
            result = self.recursiveSearch(board, word, i, j)
            if result:
                return True
        return False


obj = Solution()
# board =[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# #
# word = "ABCCED" #, return true.
# print obj.exist(board, word )
# word = "SEE" # return true.
# print obj.exist(board,  word)
# word = "ABCB" #, return false.
# print obj.exist(board,  word)
# word = "ASFDEE" #, return true.
# print obj.exist(board,  word)
#
board = [
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","b"]]
word = "aaaaaaaaaaaaaaaaaaaa"

print obj.exist(board,  word)

# board = [["A","B","C","E"],
#          ["S","F","E","S"],
#          ["A","D","E","E"]]
# word = "ABCESEEEFS"
#
# print obj.exist(board,  word)
#

