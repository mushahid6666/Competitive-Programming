__author__ = 'mushahidalam'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindNode(A):
        if A==None:
            return None
        while A.left!=None:
            A = A.left
        return A
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        root = A
        while root.val!=B:
            if B > root.val:
                root = root.right
            else:
                root = root.left
        if root==None:
            return None
        # print("found",A.val)
        if root.right!=None:
            return self.FindNode(root.right)
        else:
            sucessor = None
            ancestor = A
            while ancestor!=root:
                if ancestor.val < root.val:
                    ancestor = ancestor.right
                else:
                    sucessor = ancestor
                    ancestor = ancestor.left

            return sucessor

A = Solution()
B = TreeNode(3)
B.left = TreeNode(2)
B.right = TreeNode(4)
#B.right.right = TreeNode(5)
D = A.getSuccessor(B,2)
print(D.val)
