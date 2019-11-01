class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy


class Solution(object):
    def __init__(self):
        self.ans = None
    def findLCA(self, root, p, q, left, right, mid):
        if root == None:
            return False
        left = self.findLCA(root.left, p, q, left, right, mid)
        right = self.findLCA(root.right, p, q, left, right, mid)

        if root == p or root == q:
            mid = True

        if left + right + mid >=2:
            self.ans = root

        return left or right or mid
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.findLCA(root, p, q, False, False, False)
        return self.ans

class Solution1(object):
    def __init__(self):
        self.path2p = []
        self.path2q = {}

    def findLCA(self, root, p, q):
        if root == None:
            return
        if p.val < root.val < q.val or q.val < root.val < p.val or root.val == p.val or root.val == q.val:
            return root
        if root.val > p.val and root.val > q.val:
            return self.findLCA(root.left, p, q)
        else:
            return self.findLCA(root.right, p, q)
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.findLCA(root, p, q)

import copy
class Solution(object):
    def __init__(self):
        self.path2p = []
        self.path2q = {}

    def findPath(self, root, value, p_path, cur_path):
        if root == None:
            return
        if root.val == value:

            if p_path:
                cur_path.append(root.val)
                self.path2p = copy.deepcopy(cur_path)
            else:
                cur_path[root.val] = root
                self.path2q = copy.deepcopy(cur_path)

        if p_path:
            cur_path.append(root.val)
        else:
            cur_path[root.val] = root
        self.findPath(root.left, value, p_path, cur_path)
        self.findPath(root.right, value, p_path, cur_path)
        if p_path:
            cur_path.pop()
        else:
            del cur_path[root.val]
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.findPath(root, p.val, True, [])
        self.findPath(root, q.val, False, {})
        for i in range(len(self.path2p)-1 , -1 ,-1):
            number = self.path2p[i]
            if number in self.path2q:
                return self.path2q[number]

obj = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
node =  obj.lowestCommonAncestor(root, root.left, root.left.right)
print node.val
