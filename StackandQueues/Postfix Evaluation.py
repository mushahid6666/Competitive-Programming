# from __future__ import division
__author__ = 'mushahidalam'


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        n = len(A)
        stack = []
        for i in range(0, n):
            if A[i] == "+" or A[i] == "*" or A[i] == "/" or A[i] == "-":
                a = stack.pop()
                b = stack.pop()
                if A[i] == "+":
                    c = b + a
                    stack.append(c)
                if A[i] == "-":
                    c = b - a
                    stack.append(c)
                if A[i] == "/":
                    c = int(float(b) / a)
                    stack.append(c)
                if A[i] == "*":
                    c = b * a
                    stack.append(c)
            else:
                stack.append(int(A[i]))
        return stack.pop()


obj = Solution()
str = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print obj.evalRPN(str)
