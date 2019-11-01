"""
Given a binary tree where every node has a unique value, and a target key k,
find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to
reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row.
The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""


# Definition for a binary tree node.
import collections, copy, bisect, sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findAllLeafNodes(self, root, parent, node2LeafLength, parentLeafList, parentChildMap):
        if root == None:
            return
        parentChildMap[root.val] = parent
        if root.left == None and root.right == None:
            parentLeafList.append([root.val, 1])
            return
        childList = []
        self.findAllLeafNodes(root.left,root, node2LeafLength , childList, parentChildMap)
        self.findAllLeafNodes(root.right,root, node2LeafLength, childList, parentChildMap)
        node2LeafLength[root.val] = childList
        parentLeafListCopy = copy.deepcopy(childList)
        for entry in parentLeafListCopy:
            entry[1] += 1
            parentLeafList.append(entry)
        return


    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return

        node2LeafLength = collections.defaultdict(list)
        parentChildMap = collections.defaultdict(TreeNode)
        self.findAllLeafNodes(root, None, node2LeafLength,[], parentChildMap)

        targetNodeChild = node2LeafLength[k]
        if len(targetNodeChild) == 0:
            return k

        min_distance_leaf = sys.maxint
        result_val = None

        #Check cur_node leaves
        for leaf in node2LeafLength[k]:
            if min_distance_leaf > leaf[1]:
                min_distance_leaf = leaf[1]
                result_val = leaf[0]
        parent = parentChildMap[k]
        add_distance = 0
        while parent != None and add_distance < min_distance_leaf:
            add_distance += 1
            for leaf in node2LeafLength[parent.val]:
                if min_distance_leaf > (leaf[1] + add_distance):
                    min_distance_leaf = leaf[1] + add_distance
                    result_val = leaf[0]

            parent = parentChildMap[parent.val]

        #check all parents
        return result_val


obj = Solution()
# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6
#
# Output: 3
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
root.left.left.left.left= TreeNode(6)
root.right = TreeNode(3)
print obj.findClosestLeaf(root, root.left.val)
# root = TreeNode(1)
# root.left = TreeNode(2)
# # root.right = TreeNode(3)
# print obj.findClosestLeaf(root, root)

