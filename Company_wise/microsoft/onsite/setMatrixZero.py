#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
class Solution(object):
    def setRowColumn(self, matrix, cur_i, cur_j):
        for i in range(len(matrix)):
            if matrix[i][cur_j]!="0" and matrix[i][cur_j][0] != "#":
                matrix[i][cur_j] = "#" + matrix[i][cur_j]
        for j in range(len(matrix[0])):
            if matrix[cur_i][j] != "0" and matrix[cur_i][j][0] != "#":
                matrix[cur_i][j] = "#" + matrix[cur_i][j]

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]= str(matrix[i][j])


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    self.setRowColumn(matrix, i, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j][0]=="#":
                    matrix[i][j]= int(0)
                else:
                    matrix[i][j] = int(matrix[i][j])
obj = Solution()
matrix = [
  [0],
  [0],
    [1]
]
obj.setZeroes(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print matrix[i][j],
    print
#Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

print "==========="
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

obj.setZeroes(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print matrix[i][j],
    print
