# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """


obj = Solution()
preOrder = [8,5,1,7,10,12]
root = obj.bstFromPreorder(preOrder)
temp = root
while temp!= None:
    print temp.val
    temp  = temp.next
