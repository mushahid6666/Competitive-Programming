import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        # A = A.replace(' ','')
        A = ''.join(e for e in A if e.isalnum())
        reverse = ''
        last = len(A)
        for i in range(0,len(A)):
            reverse = reverse+A[last-i-1]
        A= A.lower()
        reverse = reverse.lower()
        if reverse==A:
            print True
        else:
            print False
        print reverse
        print A

A = Solution()
A.isPalindrome("A man, a plan, a canal: Panama")