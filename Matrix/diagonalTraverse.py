# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
# Example:
#
# Input:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# Output:  [1, 2, 4, 7, 5, 3, 6, 8, 9]


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        traverse_up = True
        traverse_down = False
        result = []
        result.append(matrix[0][0])
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 1 and cols == 1:
            return [[matrix[0][0]]]
        i = 0
        j = 0
        while i < rows and j < cols:
            if traverse_up:
                new_index_i = i - 1
                new_index_j = j + 1
                if new_index_i >= 0 and new_index_j < cols:
                    result.append(matrix[new_index_i][new_index_j])
                else:
                    if j + 1 >= cols :
                        new_index_i = i + 1
                        new_index_j = j
                    else:
                        new_index_i = i
                        new_index_j = j + 1
                    result.append(matrix[new_index_i][new_index_j])
                    traverse_down = True
                    traverse_up = False
            else:
                new_index_i = i + 1
                new_index_j = j - 1
                if new_index_i < rows and new_index_j >= 0:
                    result.append(matrix[new_index_i][new_index_j])
                else:
                    if i == rows -1:
                        new_index_i = i
                        new_index_j = j + 1
                    else:
                        new_index_i = i + 1
                        new_index_j = j
                    result.append(matrix[new_index_i][new_index_j])
                    traverse_down = False
                    traverse_up = True
            i = new_index_i
            j = new_index_j
            if i == rows -1 and j == cols-1:
                break
        return result

obj = Solution()
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# matrix = []
matrix = [[3]]
Output =  [1, 2, 4, 7, 5, 3, 6, 8, 9]
print obj.findDiagonalOrder(matrix), "Expected", Output
