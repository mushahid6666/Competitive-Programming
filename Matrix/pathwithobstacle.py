__author__ = 'mushahidalam'


class Solution:
    # @param A : list of list of integers
    # @return an integer
    count = 0

    def isObstacle(self, i):
        if i == 1:
            return True
        else:
            return False

    def numAllPaths(self, matrix, i, j, m, n):
        if (i > m - 1 or j > n - 1 or self.isObstacle(matrix[i][j])):
            return;
        if i == m - 1 and j == n - 1:
            self.count += 1
            return
        self.numAllPaths(matrix, i, j + 1, m, n)
        self.numAllPaths(matrix, i + 1, j, m, n)

    def uniquePathsWithObstacles(self, A):
        m = len(A)
        n = len(A[0])
        self.count = 0
        self.numAllPaths(A, 0, 0, m, n)
        return self.count


A = Solution()
matrix = [
    [0, 0]
]
print A.uniquePathsWithObstacles(matrix)
