__author__ = 'mushahidalam'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    dict = {}

    def inorder(self, A):
        if (A == None):
            return
        if A.val not in self.dict:
            self.dict[A.val] = 1
        self.inorder(A.left)
        self.inorder(A.right)

    def t2Sum(self, A, B):
        self.inorder(A)
        for i in self.dict:
            num = B - i
            if num in self.dict and num != i:
                self.dict.clear()
                return 1
        self.dict.clear()
        return 0


A = TreeNode(7)
A.left = TreeNode(10)
A.left.left = TreeNode(20)
A.right = TreeNode(9)
obj = Solution()
print obj.t2Sum(A, 40)
