__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        totalmice = len(A)
        totalholes = len(B)
        maxdiff = abs(A[0] - B[0])
        for i in range(1, totalmice):
            newdiff = abs(A[i] - B[i])
            if newdiff > maxdiff:
                maxdiff = newdiff
        return maxdiff


obj = Solution()
mice = [-2, 8, 9, 0]
holes = [5, 4, 12, 1]
print obj.mice(mice, holes)
