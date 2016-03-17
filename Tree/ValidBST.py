__author__ = 'mushahidalam'
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def checkBST(self, root, min, max):

        if root == None:
            return 1
        if root.val > min and root.val <= max:
            return 1
        return (self.checkBST(root.left, min, root.val) and self.checkBST(root.right, root.val, max))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.checkBST(root, -sys.maxint, sys.maxint)


obj = Solution()
