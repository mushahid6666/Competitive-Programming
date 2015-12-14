__author__ = 'mushahidalam'
class Solution():

    def findmaxsum(self,A):
        max_excl_prev = 0
        max_incl_prev = A[0]
        for i in range(1,len(A)):
            max_incl_curr = max(max_excl_prev+B[i],max_excl_prev)
            max_excl_curr = max(max_incl_prev,max_excl_prev)
            max_excl_prev = max_excl_curr
            max_incl_prev = max_incl_curr
        return max(max_incl_curr,max_excl_curr)




A = Solution()
B = [3,1,4,10,7]
print A.findmaxsum(B)