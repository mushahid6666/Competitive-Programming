# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def checkifSymmetric(self, leftSubTreeNode, rightSubtreeNode):
        """
        :param leftSubTreeNode: TreeNode
        :param rightSubtreeNode: TreeNode
        :return:
        """
        if leftSubTreeNode == None and rightSubtreeNode !=None:
            return False
        if leftSubTreeNode != None and rightSubtreeNode ==None:
            return False
        if leftSubTreeNode == None and rightSubtreeNode == None:
            return True
        if leftSubTreeNode.val == rightSubtreeNode.val:
            return (self.checkifSymmetric(leftSubTreeNode.left, rightSubtreeNode.right) and self.checkifSymmetric(leftSubTreeNode.right, rightSubtreeNode.left))
        return False


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.checkifSymmetric(root.left, root.right)

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
print obj.isSymmetric(root)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print obj.isSymmetric(root)
root = TreeNode(1)
print obj.isSymmetric(root)