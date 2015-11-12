__author__ = 'mushahidalam'
class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A<0:
            return 0
        B = str(A)
        lt = len(B)
        for i in range(0,len(B)):
            if B[i]!=B[lt-i-1]:
                return False
        return True

A = Solution()
print(A.isPalindrome(123))