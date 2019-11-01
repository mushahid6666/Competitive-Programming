# Definition for a binary tree node.
import copy, collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMap(self, node):
        if node == None:
            return
        self.node_map[node.val] = node
        self.constructMap(node.left)
        self.constructMap(node.right)
    def findPath(self,root, p, cur_path, p_or_q):
        if root == None:
            return
        new_path = copy.deepcopy(cur_path)
        new_path.append(root.val)
        if root == p:
            if p_or_q:
                self.q_path = copy.deepcopy(new_path)
            else:
                self.p_path = copy.deepcopy(new_path)
        self.findPath(root.left, p, new_path, p_or_q)
        self.findPath(root.right, p, new_path, p_or_q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        self.node_map = collections.defaultdict(TreeNode)
        self.constructMap(root)
        self.p_path = []
        self.q_path = []
        self.findPath(root, p, [], 0)
        self.findPath(root, q, [], 1)
        for i in range(len(self.p_path)-1 , -1, -1):
            number = self.p_path[i]
            if number in self.q_path:
                return self.node_map[number]

obj = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left  = TreeNode(6)
root.left.right  = TreeNode(2)
root.left.right.left  = TreeNode(7)
root.left.right.right  = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = root.left
q  = root.left.left
node = obj.lowestCommonAncestor(root, p, q)
print node.val

