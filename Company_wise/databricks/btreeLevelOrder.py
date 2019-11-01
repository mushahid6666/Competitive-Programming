import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
    def BFS(self,root, level):
        if root == None:
            return
        if level not in self.level_map:
            self.level_map[level] =[]
        self.level_map[level].append(root.val)
        self.BFS(root.left, level +1)
        self.BFS(root.right, level + 1)


    # def add_level2result(self, level_nodes):


    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.__init__()
        if root == None:
            return []
        self.level_map = collections.OrderedDict()
        self.BFS(root, 0)
        self.result = []
        for key,value in self.level_map.items():
            self.result.append(value)

        return self.result
solObj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print solObj.verticalOrder(root)
root = TreeNode(3)
print solObj.verticalOrder(root)
root = TreeNode(50)
root.left = TreeNode(40)
root.right = TreeNode(60)
root.left.left = TreeNode(30)
root.left.left.left = TreeNode(91)
root.left.left.right = TreeNode(92)
root.left.right = TreeNode(45)
root.left.right.left = TreeNode(93)
root.left.right.right = TreeNode(94)
root.right.left = TreeNode(55)
root.right.left.left = TreeNode(95)
root.right.left.right= TreeNode(96)
root.right.right = TreeNode(65)
root.right.right.left = TreeNode(97)
root.right.right.right = TreeNode(98)

print solObj.verticalOrder(root)
root = None
print solObj.verticalOrder(root)


