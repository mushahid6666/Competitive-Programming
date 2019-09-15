__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        arr = A
        n = len(A)

        lst = [1] * n

        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and lst[i] < lst[j] + 1:
                    lst[i] = lst[j] + 1
        max = lst[0]
        for i in range(1, n):
            if lst[i] > max:
                max = lst[i]
        return max
