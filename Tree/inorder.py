# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderIterative(self, root):
        pass
    def inorderRecursive(self, root, result):
        if root == None:
            return
        self.inorderRecursive(root.left, result)
        result.append(root.val)
        self.inorderRecursive(root.right, result)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorderRecursive(root, result)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solutionObj = Solution()
print solutionObj.inorderTraversal(root)