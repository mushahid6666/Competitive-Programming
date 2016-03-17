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
        if root.right != None:
            lt = len(root.right)
            root.right = self.constructTree(preorder, root.right, prestart - 1)
        else:
            lt = 0
        if root.left != None:
            root.left = self.constructTree(preorder, root.left, prestart - lt - 1)
        return root

    def buildTree(self, inorder, preorder):
        return self.constructTree(preorder, inorder, len(preorder) - 1)



A = Solution()
ino = [7, 5, 6, 2, 3, 1, 4]
pre = [5, 6, 3, 1, 4, 2, 7]
#             2
#         1         3
#     6                   4
# 5
root = A.buildTree(ino, pre)
print root.val
print root.left.val
print root.right.val

