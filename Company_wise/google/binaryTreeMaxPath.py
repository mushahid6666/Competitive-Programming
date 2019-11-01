# Definition for a binary tree node.
'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
 node to any node in the tree along the parent-child connections. The path must
  contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''
import collections, sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.treeChildMaxSum = collections.defaultdict(TreeNode)
        self.max_sum = -sys.maxint

    def findAllchildMaxPath(self, node, parent):

        self.treeChildMaxSum[node] = [ None, None, parent]
        if node.left == None and node.right == None:
            self.max_sum = max(self.max_sum, node.val)
            return node.val
        if node.left != None:
            self.treeChildMaxSum[node][0] = node.val + self.findAllchildMaxPath(node.left, node)
        if node.right != None:
            self.treeChildMaxSum[node][1 ] = node.val + self.findAllchildMaxPath(node.right, node)
        self.max_sum = max(self.max_sum, max(self.treeChildMaxSum[node][0], self.treeChildMaxSum[node][1]), node.val)
        return max(self.treeChildMaxSum[node][0], self.treeChildMaxSum[node][1], node.val)

    def findChildToParentMaxPath(self):
        for node,value  in self.treeChildMaxSum.items():
            if value[2] != None:
                if value[2].right == node and self.treeChildMaxSum[value[2]][0]!= None:
                    self.max_sum = max(self.max_sum, max(node.val, value[0],value[1 ]) + self.treeChildMaxSum[value[2]][0])
                elif value[2].left == node and self.treeChildMaxSum[value[2]][1] != None:
                    self.max_sum = max(self.max_sum, max(node.val, value[0],value[1 ]) + self.treeChildMaxSum[value[2]][1])


    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.__init__()
        self.findAllchildMaxPath(root, None)
        self.findChildToParentMaxPath()
        return self.max_sum

obj = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
root.right.right.right.right = TreeNode(5)
print obj.maxPathSum(root)
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print obj.maxPathSum(root)
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print obj.maxPathSum(root)
# root = TreeNode(2)
# root.left = TreeNode(-1)
# root.left.left = TreeNode(30)
# root.left.right = TreeNode(5)

# print obj.maxPathSum(root)
