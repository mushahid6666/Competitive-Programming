__author__ = 'mushahidalam'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    final = []

    def findpath(self, A, stack):
        if (A == None):
            return
        if A.left == None and A.right == None:
            stack.append(str(A.val))
            strres = ''
            for i in range(0, len(stack)):
                strres += stack[i]
            self.final.append(int(strres))
            return
        stack.append(str(A.val))
        self.findpath(A.left, stack)
        while len(stack) != 0 and int(stack[-1]) != A.val:
            stack.pop()
        self.findpath(A.right, stack)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findpath(root, [])
        # print(self.final)
        sum = 0
        for i in range(0, len(self.final)):
            sum += self.final.pop(0)
        # sum = sum % 1003
        self.final = []
        return sum


A = TreeNode(2)
A.left = TreeNode(0)
A.right = TreeNode(0)
obj = Solution()
print obj.sumNumbers(A)
