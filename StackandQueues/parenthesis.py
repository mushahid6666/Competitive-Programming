__author__ = 'mushahidalam'
class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        for i in range(0,len(A)):
            if A[i]=='[' or A[i]=='{' or A[i]=='(':
                stack.append(A[i])
            else:
                if A[i]==')':
                    if len(stack)==0:
                        return 0
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return 0
                elif A[i]=='}':
                    if len(stack)==0:
                        return 0
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return 0
                elif A[i]==']':
                    if len(stack)==0:
                        return 0
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return 0
        if len(stack)==0:
            return 1
        else:
            return 0


A = Solution()
print A.isValid(')')
