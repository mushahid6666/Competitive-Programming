__author__ = 'mushahidalam'

class Solution:
    def printallpaths(self,matrix,i,j,m,n,pathno,paths):
        if i==m-1:
            for k in range(j,n):
                if pathno+k-j in paths:
                    paths.insert(pathno+k-j,matrix[i*n-1][k])
                else:
                    paths.insert(pathno+k-j,matrix[i*n][k])
            for l in range(0,pathno+n-j):
                print paths[l]
            return
        if j==n-1:
            for k in range(i,n):
                paths.insert(pathno+k-i,matrix[k*n,j])
            for l in range(0,pathno+m-i):
                print paths[l]
            return
        paths.insert(pathno,matrix[i*n][j])
        self.printallpaths(matrix, i+1, j, m, n, pathno + 1, paths)
        self.printallpaths(matrix, i, j+1, m, n, pathno + 1,paths)

    def printpaths(self,matrix,m,n):
        paths = [None]*m*n
        self.printallpaths(matrix,0,0,m-1,n-1,0,paths)

A = Solution()
matr = [[1,2,3],[4,5,6]]
A.printpaths(matr,2,3)