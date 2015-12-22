__author__ = 'mushahidalam'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def findMax(self, lst):
        if len(lst) == 1:
            return 0
        maxele = 0
        for i in range(0, len(lst)):
            if lst[i] > lst[maxele]:
                maxele = i
        return maxele

    def buildTree(self, A):
        if len(A) == 0:
            return None
        index = self.findMax(A)
        root = TreeNode(A[index])
        root.left = A[:index]
        root.right = A[index + 1:]
        root.left = self.buildTree(root.left)
        root.right = self.buildTree(root.right)
        return root


obj = Solution()
inorder = [1, 2, 3]
root = obj.buildTree(inorder)
pass
