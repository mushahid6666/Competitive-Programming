# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def __init__(self):
        self.minvalue = sys.maxint
        self.secondMinvalue = sys.maxint
    def traverTreeSecondMin(self, root):
        if root == None:
            return -1
        if self.minvalue < root.val < self.secondMinvalue:
            self.secondMinvalue = root.val
            return
        elif root.val == self.minvalue:
            self.traverTreeSecondMin(root.left)
            self.traverTreeSecondMin(root.right)



    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.__init__()
        if root == None:
            return -1
        self.minvalue = root.val
        self.traverTreeSecondMin(root)
        if self.secondMinvalue == sys.maxint:
            return -1
        return self.secondMinvalue
"""
*         2 
*      /    \ 
*     2      10 
*    / \    /  \    
*   3   2   5   10 

    2
   / \
  2   5
     / \
    5   7
 
"""
obj = Solution()
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print obj.findSecondMinimumValue(root)