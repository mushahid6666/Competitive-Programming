# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]
import sys
class Solution(object):
    def findAllValid(self, parenthesis, index, openPcount, closePcount, expr, remCount):
        if index == len(parenthesis):
            if openPcount == closePcount:
                if remCount <= self.minRemCount:
                    ans = "".join(expr)
                    if remCount < self.minRemCount:
                        self.result = set()
                        self.minRemCount = remCount
                    self.result.add(ans)
        else:
            charecter = parenthesis[index]
            if charecter != "(" and charecter != ")":
                expr.append(charecter)
                self.findAllValid(parenthesis, index + 1, openPcount, closePcount, expr, remCount)
                expr.pop()
            else:
                self.findAllValid(parenthesis, index + 1, openPcount, closePcount, expr, remCount + 1)
                expr.append(charecter)
                if charecter == "(":
                    self.findAllValid(parenthesis, index + 1, openPcount + 1, closePcount, expr, remCount)
                else:
                    if openPcount > closePcount:
                        self.findAllValid(parenthesis, index + 1, openPcount, closePcount + 1, expr, remCount)
                expr.pop()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        self.result = set()
        self.minRemCount = sys.maxint
        self.findAllValid(s, 0, 0, 0, [], 0)
        return list(self.result)

obj = Solution()
parenthesis = "()())()"
print obj.removeInvalidParentheses(parenthesis)
parenthesis = "(a)())()"
print obj.removeInvalidParentheses(parenthesis)
parenthesis = ")("
print obj.removeInvalidParentheses(parenthesis)
parenthesis = "("
print obj.removeInvalidParentheses(parenthesis)
