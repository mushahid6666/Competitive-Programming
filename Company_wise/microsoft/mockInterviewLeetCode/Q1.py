# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.parents = list()
        self.max_diff = -sys.maxint
    def computeDiff(self, node):
        if node == None:
            return
        if node.left != None:
            self.max_diff = max(self.max_diff, abs(node.val - node.left.val))
        if node.right != None:
            self.max_diff = max(self.max_diff, abs(node.val - node.right.val))
        for number in self.parents:
            self.max_diff = max(self.max_diff, abs(node.val - number))
        self.parents.append(node.val)
        self.computeDiff(node.left)
        self.computeDiff(node.right)
        self.parents.pop(-1)

    def maxAncestorDiff(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.__init__()
            if root == None:
                return None
            self.computeDiff(root)
            if self.max_diff == -sys.maxint:
                return None
            return self.max_diff

obj = Solution()
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
print obj.maxAncestorDiff(root)
root = TreeNode(8)
print obj.maxAncestorDiff(root)


