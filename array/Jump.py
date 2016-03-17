__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        if len(A) == 1:
            return True
        if len(A) == 2:
            if A[0] != 0:
                return True
        max_reach = A[0]
        if max_reach == 0:
            return False
        end = len(A)
        for i in range(1, len(A) - 1):
            if i > max_reach:
                return False
            cur_max = A[i] + i
            max_reach = max(cur_max, max_reach)
            if max_reach >= end - 1:
                return True
        return False


A = Solution()
b = [1, 0, 1, 0]
print A.canJump(b)
