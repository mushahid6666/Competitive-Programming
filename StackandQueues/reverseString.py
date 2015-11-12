__author__ = 'mushahidalam'
class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack = []
        for i in range(len(A)):
            stack.append(A[i])
        reverse = ''
        for j in range(len(stack)):
            reverse = reverse + stack.pop()
        return reverse



A = Solution()
print A.reverseString('pop')
