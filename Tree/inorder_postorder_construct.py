__author__ = 'mushahidalam'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param postorder : list of integers denoting postorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    # hashinorder = {}
    # def hashconstruct(self,inorder):
    def constructTree(self,postorder,poststart,postend,inorder,instart,inend):
        if poststart < postend  or instart > inend:
            return None
        val = postorder[poststart]
        p = TreeNode(val)

        #find parent element index from inorder
        k = inorder.index(val)

        p.left = self.constructTree(postorder,poststart-(inend-k)-1,postend,inorder,instart,k-1)
        p.right = self.constructTree(postorder,poststart-1,postend+(k-instart), inorder,k+1,inend)
        return p




    def buildTree(self, postorder, inorder):
        poststart = len(postorder)-1
        postend = 0
        instart = 0
        inend = len(inorder)-1
        return self.constructTree(postorder,poststart,postend,inorder,instart,inend)



A = Solution()
ino = [  4 ,2, 5, 1, 6, 7, 3, 8 ]
post = [ 4 ,5 ,2  ,6 ,7 ,8 ,3  ,1]
root =  A.buildTree(post,ino)
print root.val
print root.left.val
print root.right.val

