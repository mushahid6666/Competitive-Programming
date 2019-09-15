__author__ = 'mushahidalam'
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    #Attempt 2
    inorder_output = list()
    def __init__(self):
        self.inorder_output = []

    def inorderTraversal(self, root):
        """
        :param root: TreeNode
        :return: None
        """
        if root == None:
            return
        self.inorderTraversal(root.left)
        self.inorder_output.append(root.val)
        self.inorderTraversal(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        self.inorderTraversal(root)
        if len(self.inorder_output) == 1:
            return True
        for i in range(len(self.inorder_output) - 1):
            if self.inorder_output[i] < self.inorder_output[i+1]:
                continue
            return False
        return True

    #Previous Accepted Recursive Solution
    # def checkBST(self, root, min, max):
    #
    #     if root == None:
    #         return 1
    #     if root.val > min and root.val <= max:
    #         return 1
    #     return (self.checkBST(root.left, min, root.val) and self.checkBST(root.right, root.val, max))

    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     self.checkBST(root, -sys.maxint, sys.maxint)
obj = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print obj.isValidBST(root)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print obj.isValidBST(root)
