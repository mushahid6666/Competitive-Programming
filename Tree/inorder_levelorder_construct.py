__author__ = 'mushahidalam'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param levelorder : list of integers denoting levelorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    # hashinorder = {}
    # def hashconstruct(self,inorder):
    def extract(self,inorder,levelorder):
        retlist = []
        for i in levelorder:
            if i in inorder:
                retlist.append(i)
        return retlist

    def constructTree(self,levelorder,levelstart,levelend,inorder,instart,inend):

        if levelstart > levelend  or instart > inend:
            return None
        val = levelorder[levelstart]
        p = TreeNode(val)

        #find parent element index from inorder
        k = inorder.index(val)
        leftextract = self.extract(inorder[instart:k],levelorder[levelstart:])
        rightextract = self.extract(inorder[k+1:inend+1],levelorder[levelstart:])
        # Split the levelorder based on left and right subtree from inrder
        p.left = self.constructTree(leftextract,0,len(leftextract)-1,inorder,instart,k-1)
        p.right = self.constructTree(rightextract,0,len(rightextract)-1, inorder,k+1,inend)
        return p




    def buildTree(self, levelorder, inorder):
        levelstart = 0
        levelend = len(levelorder)-1
        instart = 0
        inend = len(inorder)-1
        return self.constructTree(levelorder,levelstart,levelend,inorder,instart,inend)



A = Solution()
inorder = [4, 8, 10, 12, 14, 20, 22 ]
level = [ 20, 8, 22, 4, 12, 10, 14]
root =  A.buildTree(level,inorder)
print root.val
print root.left.val
print root.right.val

