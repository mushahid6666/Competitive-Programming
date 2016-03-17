__author__ = 'mushahidalam'
import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, arr):
        n = len(arr)
        jumps = [0] * n
        jumps[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if arr[i] == 0:
                jumps[i] = sys.maxint
            elif arr[i] >= n - i - 1:
                jumps[i] = 1
            else:
                min = sys.maxint
                for j in range(i + 1, n):
                    if j <= arr[i] + i:
                        if min > jumps[j]:
                            min = jumps[j]
                    else:
                        break
                if min != sys.maxint:
                    jumps[i] = min + 1
                else:
                    jumps[i] = min
        if jumps[0] == sys.maxint:
            return -1
        return jumps[0]


# [3,1 ,1, 4, 1,2 ,1]
# n=7
# 3+4
#
# [3,1  3,1 3,1  7,2 7,2 7,2 7,2]

obj = Solution()
arr = [3, 0, 0, 0, 0, 0, 0, 1]
print obj.jump(arr)
