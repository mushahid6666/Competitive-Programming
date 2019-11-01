"""
# Definition for a Node."""
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections
class Solution(object):
    def __init__(self):
        self.BFSResult = collections.defaultdict(list)

    def bfsTravers(self, root, level):
        if root == None:
            return
        self.BFSResult[level].append(root)
        self.bfsTravers(root.left, level + 1)
        self.bfsTravers(root.right, level + 1)

    def connect1(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return
        self.__init__()
        self.bfsTravers(root, 1)
        for key in self.BFSResult.keys():
            cur_level_nodes = self.BFSResult[key]
            if len(cur_level_nodes) > 1:
                cur_node = cur_level_nodes.pop(0)
                next_node = cur_level_nodes.pop(0)
                while next_node != None:
                    cur_node.next = next_node
                    cur_node = next_node
                    if len(cur_level_nodes) !=0:
                        next_node = cur_level_nodes.pop(0)
                    else:
                        next_node = None
        return root

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        


obj = Solution()
second_left_node = Node(4, None, None, None)
second_right_node = Node(5, None, None, None)
second_right_left_node = Node(6, None, None, None)
second_right_right_node = Node(7, None, None, None)

first_left_node = Node(2, second_left_node, second_right_node, None)
first_right_node = Node(3, second_right_left_node, second_right_right_node, None)
root = Node(1,first_left_node, first_right_node, None)
obj.connect(root)
root = Node(1,None, None, None)
obj.connect(root)