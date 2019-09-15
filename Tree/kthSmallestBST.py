# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    inorder_output = list()
    def __init__(self):
        self.inorder_output = []

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.inorder_output.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root)
        if k <= len(self.inorder_output):
            return self.inorder_output[k-1]

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
obj = Solution()
print obj.kthSmallest(root, 1), "Expected: 1"

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right = TreeNode(6)
obj = Solution()
print obj.kthSmallest(root, 3), "Expected: 3"
