# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections, sys, bisect
class Solution(object):
    def __init__(self):
        self.result = []
        self.stack = collections.defaultdict(list)

    def getHeightOfTree(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        leftHeight = self.getHeightOfTree(root.left)
        rightHeight = self.getHeightOfTree(root.right)
        return max(leftHeight, rightHeight) + 1

    def postOrder(self, root):
        if root.left == None and root.right == None:
            self.result[0].append(root.val)
            return 1
        level1, level2 = -1, -1
        if root.left:
            level1 = self.postOrder(root.left)
        if root.right:
            level2 =self.postOrder(root.right)
        level = max(level1, level2)
        if root.left != None or root.right != None:
            self.result[level].append(root.val)
        return level + 1

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        height = self.getHeightOfTree(root)
        for i in range(height):
            self.result.append([])
        self.postOrder(root)

        return self.result

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)
print  obj.findLeaves(root)