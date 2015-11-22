# Definition for a  binary tree node
'''Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    reslist = []
    locresu = []
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        self.reslist = []
        direction = 1
        i = 0;
        ht = 0;
        ht = self.height(A);
        for i in range(0, ht):
            self.locresu = []
            self.PrintGivenLevel(i, A, direction)
            self.reslist.append(self.locresu)
            if direction == 0:
                direction = 1
            else:
                direction = 0
                # print(self.locresu,self.reslist)
        return self.reslist

    def maxresult(self, a, b):
        if a > b:
            return a
        else:
            return b

    def height(self, root):
        if (root == None):
            return 0;
        else:
            return (self.maxresult(self.height(root.left), self.height(root.right)) + 1);

    def PrintGivenLevel(self, level, root, dir):
        if (dir == 0):
            if (root == None):
                return
            if (level == 0):
                self.locresu.append(root.val)
                return
            self.PrintGivenLevel(level - 1, root.right, dir)
            self.PrintGivenLevel(level - 1, root.left, dir)
        else:
            if (root == None):
                return
            if (level == 0):
                self.locresu.append(root.val)
                return
            self.PrintGivenLevel(level - 1, root.left, dir)
            self.PrintGivenLevel(level - 1, root.right, dir)


A = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)
print(A.zigzagLevelOrder(root))
