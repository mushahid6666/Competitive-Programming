"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
forEach node in the graph contains a val (int) and a list (List[Node]) of its neighbors.



Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.


Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.

"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



class Solution(object):
    def copyGraph(self, original_node, copied_node, stack):
        for cur_neighbour in original_node.neighbors:
            if cur_neighbour in self.node_map:
                copied_node.neighbors.append(self.node_map[cur_neighbour])
                continue
            new_child = Node(cur_neighbour.val,[])
            copied_node.neighbors.append(new_child)
            stack.append([new_child, cur_neighbour])
            self.node_map[cur_neighbour] = new_child
        for entry in stack:
            self.copyGraph(entry[1], entry[0], [])

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.node_map = {}
        if node == None:
            return None
        root_copy = Node(node.val,[])
        self.node_map[node] = root_copy
        self.copyGraph(node, root_copy, [])
        return root_copy

obj = Solution()
root = Node(3, [])
print obj.cloneGraph(root)
