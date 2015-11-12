__author__ = 'mushahidalam'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def postorderTraversal(self, A):
        self.values = []
        self.traverse(A)

    def traverse(self, root):
        if root.left is None and root.right is None:
            self.values.append(root.val)
            return

        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)
        self.values.append(root.val)

    def __init__(self, root):
        self.postorderTraversal(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.values) > 0:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        return self.values.pop()


# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

