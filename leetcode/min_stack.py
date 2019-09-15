import sys


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack =[]
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        else:
            if x <= self.minStack[-1]:
                self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        poppedElement =  self.stack.pop()
        if poppedElement == self.minStack[-1]:
            self.minStack.pop()
        return poppedElement

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return -1

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

{ # Previous Accepted Solution
# class MinStack(object):
#     min_element = sys.maxint
#     stack = []
#     min_stack = []
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         min_element = sys.maxint
#         stack = []
#         min_stack = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#         if x <= self.min_element:
#             self.min_stack.append(x)
#             self.min_element = x
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         num = self.stack.pop()
#         if num == self.min_element:
#             self.min_stack.pop()
#             if len(self.min_stack) == 0:
#                 self.min_element = None
#             else:
#                 self.min_element = self.min_stack[-1]
#         return num
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min_element
}

#Test case 1:
# minStack = MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# print minStack.getMin();  #--> Returns - 3.
# minStack.pop();
# print minStack.top(); #--> Returns 0.
# print minStack.getMin(); #--> Returns - 2.

#Test Case 2:
minStack = MinStack();
minStack.push(0);
minStack.push(1);
minStack.push(0);
print minStack.getMin();  #--> Returns - 3.
minStack.pop();
print minStack.getMin(); #--> Returns 0.

# minStack = MinStack();
# minStack.push(2147483646);
# minStack.push(2147483646);
# minStack.push(2147483646);
#
# print minStack.top();  # --> Returns - 3.
# minStack.pop();
# print minStack.getMin()
# minStack.pop();
# print minStack.getMin()
# minStack.pop();
# minStack.push(2147483646)
# print minStack.top()
# print minStack.getMin()
# minStack.push(-2147483646)
# print minStack.top()
# print minStack.getMin()
# print minStack.top()
# print minStack.getMin()

#
# print minStack.top(); #--> Returns 0.
# print minStack.getMin(); #--> Returns - 2.
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
