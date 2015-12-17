__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        Lmin = [-1]*len(A)
        Rmax = [-1]* len(A)
        Lmin[0] = A[0]
        for i in range(1,len(A)):
            Lmin[i] = min(Lmin[i-1],A[i])

        Rmax[n-1] = A[n-1]
        for j in range(n-2,-1,-1):
            Rmax[j] = max(Rmax[j+1],A[j])

        i = 0
        j = 0
        maxdiff = -1
        while j < n and i <n:
            if Lmin[i] <= Rmax[j]:
                maxdiff = max(maxdiff,j-i)
                j = j+1
            else:
                i = i+1
        return maxdiff

A = Solution()
B = [3 ,5 ,4 ,2 ,3 ,5]
print A.maximumGap(B)