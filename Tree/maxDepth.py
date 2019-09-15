# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.maxTreeDepth = 0
    def findMaxDepth(self, root, currentDepth):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.maxTreeDepth = max(currentDepth, self.maxTreeDepth)
        self.findMaxDepth(root.left, currentDepth + 1)
        self.findMaxDepth(root.right, currentDepth + 1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxTreeDepth = 0
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        self.findMaxDepth(root, 1)
        return self.maxTreeDepth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
obj = Solution()
print obj.maxDepth(root)