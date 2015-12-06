__author__ = 'mushahidalam'


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        table = A
        row = len(A)
        for i in range(1, row):
            for j in range(0, i + 1):
                if j == 0:
                    table[i][j] += table[i - 1][j]
                    continue
                if j + 1 >= len(table[i]):
                    table[i][j] += table[i - 1][j - 1]
                    continue
                if table[i - 1][j] < table[i - 1][j - 1]:
                    table[i][j] += table[i - 1][j]
                else:
                    table[i][j] += table[i - 1][j - 1]
        minimum = table[row - 1][0]
        for i in range(0, row):
            if minimum > table[row - 1][i]:
                minimum = table[row - 1][i]
        return minimum


A = Solution()
B = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print A.minimumTotal(B)
