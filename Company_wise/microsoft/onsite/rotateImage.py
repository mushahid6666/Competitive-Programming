class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        dest_column = len(matrix[0]) - 1
        for j in range(len(matrix[0]) / 2):
            for i in range( len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][dest_column]
                matrix[i][dest_column] = temp
            dest_column -=1

obj = Solution()
input_matrix =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

obj.rotate(input_matrix)
for i in range(len(input_matrix)):
    for j in range(len(input_matrix)):
        print input_matrix[i][j],
    print "\n"
print "==="

input_matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
obj.rotate(input_matrix)

for i in range(len(input_matrix)):
    for j in range(len(input_matrix)):
        print input_matrix[i][j],
    print "\n"
print "==="
input_matrix =[
  [ 5, 1],
  [ 2, 4]
]
obj.rotate(input_matrix)
for i in range(len(input_matrix)):
    for j in range(len(input_matrix)):
        print input_matrix[i][j],
    print "\n"
print "==="
input_matrix =[
  # [ 5]
]
obj.rotate(input_matrix)
for i in range(len(input_matrix)):
    for j in range(len(input_matrix)):
        print input_matrix[i][j],
    print "\n"
