"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
class Solution(object):
    def performOp(self,num1, num2, op):
        num1 = int(num1)
        num2 = int(num2)
        if op == "*":
            return num2 * num1
        elif op == "+":
            return num2 + num1
        elif op == "-":
            return num2 - num1
        elif op == "/":
            if abs(num2) < abs(num1):
                return 0
            result =  int(abs(num2) / abs(num1))
            if num1 < 0 and num2 < 0:
                return result
            elif num1 < 0 or num2 < 0:
                return -(result)
            return result


    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        token_arr_index=0
        while len(tokens) != 1:
            if tokens[token_arr_index] == "*" or tokens[token_arr_index] == "+" or tokens[token_arr_index] == "-" or tokens[token_arr_index] == "/":
                op = tokens.pop(token_arr_index )
                num1 = tokens.pop(token_arr_index -1)
                num2 = tokens.pop(token_arr_index - 2)
                result = self.performOp(num1, num2, op)
                token_arr_index = token_arr_index -2
                tokens.insert(token_arr_index, result)
            else:
                token_arr_index += 1

        return tokens[0]

obj = Solution()
# RPN = ["2", "1", "+", "3", "*"]
# print obj.evalRPN(RPN)
# RPN = ["4", "13", "5", "/", "+"]
# print obj.evalRPN(RPN)
RPN = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
RPN = ["4","13","5","/","+"]
# RPN = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
# RPN = ["12","-11","/"]
print obj.evalRPN(RPN)