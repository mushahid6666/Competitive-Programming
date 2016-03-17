__author__ = 'mushahidalam'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    v1, v2 = 0, 0

    def findlca(self, root, n1, n2):
        if root == None:
            return None
        if root.val == n1:
            self.v1 = 1
            return root.val
        if root.val == n2:
            self.v2 = 1
            return root.val
        LeftLCA = self.findlca(root.left, n1, n2)
        RightLCA = self.findlca(root.right, n1, n2)

        if LeftLCA != None and RightLCA != None:
            return root.val
        if LeftLCA != None:
            return LeftLCA
        else:
            return RightLCA

    def find(self, root, key):
        if root == None:
            return 0
        if root.val == key:
            return 1
        ret1 = self.find(root.left, key)
        ret2 = self.find(root.right, key)
        if ret1 or ret2:
            return 1
        else:
            return 0

    def lca(self, A, val1, val2):
        self.v1, self.v2 = 0, 0
        lca = self.findlca(A, val1, val2)

        if (self.v1 and self.v2) or (self.v1 and self.find(A, val2)) or (self.v2 and self.find(A, val1)):
            return lca

        return -1


obj = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
result = obj.lca(root, 5, 4)
print result
