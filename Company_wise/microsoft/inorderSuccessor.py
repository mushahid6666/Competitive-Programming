# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def __init__(self):
        self.preOrder = []
        self.nodeValMap = collections.defaultdict(list)
    def getRecursivePreOrderBST(self, root):
        if root == None:
            return

        self.getRecursivePreOrderBST(root.left)
        self.preOrder.append(root.val)
        self.nodeValMap[root.val] = root
        self.getRecursivePreOrderBST(root.right)
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.__init__()
        self.getRecursivePreOrderBST(root)
        index = self.preOrder.index(p.val)
        if index + 1 == len(self.preOrder):
            return None
        inOrderSuccesor = self.preOrder[index +1]
        return self.nodeValMap[inOrderSuccesor]

obj = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
node = obj.inorderSuccessor(root, root.left)
if node:
    print node.val
else:
    None
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

node = obj.inorderSuccessor(root, root.right)
if node:
    print node.val
else:
    print None

