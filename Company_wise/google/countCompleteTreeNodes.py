# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution(object):
    def __init__(self):
        self.node_leaf_count = 0
        self.tree_height = 0
        self.stop_recursion = False
    def find_depth(self, root, left_or_right):
        if root == None:
            return 0
        if left_or_right:
            return 1 + self.find_depth(root.left, left_or_right)
        else:
            return 1 + self.find_depth(root.right, left_or_right)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.__init__()
        if root == None:
            return 0

        left_depth = 0
        right_depth = 0
        node = root
        while node != None:
            left_depth += 1
            node = node.left
        node = root
        while node != None:
            right_depth += 1
            node= node.right

        # left_depth = self.find_depth(root.left, True)
        # right_depth = self.find_depth(root.right, False)
        if left_depth == right_depth:
            return pow(2, left_depth) -1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
print obj.countNodes(root)