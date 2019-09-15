__author__ = 'mushahidalam'
class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, s):
        #Attempt 2:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
                continue
            if len(stack)==0:
                return False
            if bracket == ")" and stack[-1] == "(":
                stack.pop()
                continue
            if bracket == "]" and stack[-1] == "[":
                stack.pop()
                continue
            if bracket == "}" and stack[-1] == "{":
                stack.pop()
                continue
            return False
        if len(stack) == 0:
            return True
        return False
A = Solution()
# str = ')'
# str = "({[]})"
# str = '()'
# str = "({[}])"
# str = ""
# str = "((()))"
str = "((("
print A.isValid(str)
        #Accepted Solution
        # stack = []
        # for i in range(0, len(s)):
        #     if s[i]== '[' or s[i]== '{' or s[i]== '(':
        #         stack.append(s[i])
        #     else:
        #         if s[i]== ')':
        #             if len(stack)==0:
        #                 return 0
        #             if stack[-1]=='(':
        #                 stack.pop()
        #             else:
        #                 return 0
        #         elif s[i]== '}':
        #             if len(stack)==0:
        #                 return 0
        #             if stack[-1]=='{':
        #                 stack.pop()
        #             else:
        #                 return 0
        #         elif s[i]== ']':
        #             if len(stack)==0:
        #                 return 0
        #             if stack[-1]=='[':
        #                 stack.pop()
        #             else:
        #                 return 0
        # if len(stack)==0:
        #     return 1
        # else:
        #     return 0



