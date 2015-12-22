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
    # def constructTree(self,preorder,prestart,preend,inorder,instart,inend):
    #     if prestart>preend  or instart > inend:
    #         return None
    #     val = preorder[prestart]
    #     p = TreeNode(val)
    #
    #     #find parent element index from inorder
    #     k = inorder.index(val)
    #
    #     p.left = self.constructTree(preorder,prestart+1,prestart+(k-instart),inorder,instart,k-1)
    #     p.right = self.constructTree(preorder,prestart+(k-instart)+1,preend, inorder,k+1,inend)
    #     return p
    #
    #
    #
    #
    # def buildTree(self, preorder, inorder):
    #     prestart = 0
    #     preend = len(preorder)-1
    #     instart = 0
    #     inend = len(inorder)-1
    #     return self.constructTree(preorder,prestart,preend,inorder,instart,inend)
    def findindex(self, lst, num):
        for i in range(0, len(lst)):
            if lst[i] == num:
                return i

    def constructTree(self, preorder, inorder, prestart):
        if prestart >= len(preorder):
            return None
        if len(inorder) == 1:
            root = TreeNode(inorder[0])
            root.left = None
            root.right = None
            return root
        if prestart == 0:
            root = TreeNode(preorder[0])
            index = self.findindex(inorder, preorder[0])
            if index != 0:
                root.left = inorder[:index]
            else:
                root.left = None
            if index + 1 >= len(inorder):
                root.right = None
            else:
                root.right = inorder[index + 1:]
        else:
            root = TreeNode(preorder[prestart])
            index = self.findindex(inorder, preorder[prestart])
            if index != 0:
                root.left = inorder[:index]
            else:
                root.left = None
            if index + 1 >= len(inorder):
                root.right = None
            else:
                root.right = inorder[index + 1:]
        if root.left != None:
            lt = len(root.left)
            root.left = self.constructTree(preorder, root.left, prestart + 1)
        else:
            lt = 0
        if root.right != None:
            root.right = self.constructTree(preorder, root.right, prestart + lt + 1)
        return root

    def buildTree(self, preorder, inorder):
        return self.constructTree(preorder, inorder, 0)



A = Solution()
pre = [2, 1, 6, 5, 3, 4]
ino = [5, 6, 1, 2, 3, 4]
#             2
#         1         3
#     6                   4
# 5
root =  A.buildTree(pre,ino)
print root.val
print root.left.val
print root.right.val

