'''Give a N*N square matrix, return an array_problems of its anti-diagonals. Look at the example for more details.

Example:


Input:

1 2 3
4 5 6
7 8 9

Return the following :

[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]'''

__author__ = 'mushahidalam'
class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
    def diagonal(self, a):
        column=len(a[0])
        row=len(a)
        rstlst = []
        for i in range(0,column):
            k=i
            temparr = []
            for j in range(0,i+1):
                temparr.append(a[j][k])
                k-=1
            rstlst.append(temparr)
        down = row
        for r in range(1,down):
            k=column-1
            temparr = []
            for j in range(r,down):
                temparr.append(a[j][k])
                k-=1
            rstlst.append(temparr)
        return rstlst


A = Solution()
B = [[1, 2],
     [4, 5]]
print A.diagonal(B)