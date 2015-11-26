__author__ = 'mushahidalam'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    # hashinorder = {}
    # def hashconstruct(self,inorder):
    def constructTree(self,preorder,prestart,preend,inorder,instart,inend):
        if prestart>preend  or instart > inend:
            return None
        val = preorder[prestart]
        p = TreeNode(val)

        #find parent element index from inorder
        k = inorder.index(val)

        p.left = self.constructTree(preorder,prestart+1,prestart+(k-instart),inorder,instart,k-1)
        p.right = self.constructTree(preorder,prestart+(k-instart)+1,preend, inorder,k+1,inend)
        return p




    def buildTree(self, preorder, inorder):
        prestart = 0
        preend = len(preorder)-1
        instart = 0
        inend = len(inorder)-1
        return self.constructTree(preorder,prestart,preend,inorder,instart,inend)



A = Solution()
pre = [ 1, 2, 3, 4, 5 ]
ino = [ 3, 2, 4, 1, 5 ]
root =  A.buildTree(pre,ino)
print root.val
print root.left.val
print root.right.val

