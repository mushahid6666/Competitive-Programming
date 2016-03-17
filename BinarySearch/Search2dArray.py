__author__ = 'mushahidalam'


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        m = len(A)
        n = len(A[0])
        for i in range(0, m):
            if B > A[i][n - 1]:
                continue
            else:
                low = 0
                high = n - 1
                while (low <= high):
                    mid = (low + high) / 2
                    if A[i][mid] == B:
                        return 1
                    if B > A[i][mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                return 0
        return 0


A = Solution()
arr = [
    [2, 9, 12, 13, 16, 18, 18, 19, 20, 22],
    [29, 59, 62, 66, 71, 75, 77, 79, 97, 99]
]
print(A.searchMatrix(arr, 45))
