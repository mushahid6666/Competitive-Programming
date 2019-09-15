__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        dict = {}
        for i in range(0, n):
            if A[i] in dict:
                continue
            else:
                dict[A[i]] = i
        for i in range(0, n):
            num1 = A[i] - B
            num2 = A[i] + B
            if num1 in dict:
                if dict[num1] != i:
                    return 1
            if num2 in dict:
                if dict[num2] != i:
                    return 1
        return 0


obj = Solution()
A = (1, 5, 3)
print obj.diffPossible(A, 2)
