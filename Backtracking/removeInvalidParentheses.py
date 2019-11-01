import sys
class Solution(object):
    def findAllValidParenthesis(self, string, index, left_count, right_count, expr, rem_count):
        if index == len(string):
            if left_count == right_count:
                if rem_count <= self.minRemCount:
                    ans = "".join(expr)
                    if rem_count < self.minRemCount:
                        self.result = set()
                        self.minRemCount = rem_count
                    self.result.add(ans)
        else:
            if string[index] != "(" and string[index] != ")":
                expr.append(string[index])
                self.findAllValidParenthesis(string, index + 1, left_count, right_count, expr, rem_count )
                expr.pop()
            else:
                self.findAllValidParenthesis(string, index + 1, left_count, right_count, expr, rem_count + 1)
                expr.append(string[index])
                if string[index] == '(':
                    self.findAllValidParenthesis(string, index + 1, left_count + 1, right_count, expr, rem_count)

                elif left_count > right_count:
                    self.findAllValidParenthesis(string, index + 1, left_count, right_count + 1, expr, rem_count)
                expr.pop()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = set()
        self.minRemCount = sys.maxint
        self.findAllValidParenthesis(s, 0, 0, 0 ,[], 0)
        return list(self.result)


obj = Solution()
invalidParenthesis = "()())()"
print obj.removeInvalidParentheses(invalidParenthesis)
