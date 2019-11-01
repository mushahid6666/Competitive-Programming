# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1])  + 1
        root.left = self.constructFromPrePost(pre[1: L + 1] ,post[:L])
        root.right = self.constructFromPrePost(pre[ L + 1: ], post[L : -1])
        return root

obj = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
root =  obj.constructFromPrePost(pre, post)
print root
