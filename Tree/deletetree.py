__author__ = 'mushahidalam'
import gc
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class DeleteTree:
    def deltree(self,root):
        if root==None:
            return
        self.deltree(root.left)
        self.deltree(root.right)
        print("deleting",root.val)
        del root

obj = DeleteTree()
A = TreeNode(3)
A.left = TreeNode(4)
A.right = TreeNode(5)
obj.deltree(A)