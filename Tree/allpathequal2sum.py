__author__ = 'mushahidalam'


class Solution:
    stack = []
    top = -1
    flag = 0
    presentsum = 0
    pathlist = []

    def pushstack(self, root):
        self.top += 1
        self.stack.append(root)
        self.presentsum += root.val
        # print(self.stack)

    def popstack(self):
        self.top -= 1
        self.presentsum -= self.stack.pop().val

    def inorder(self, root, sum):
        if root == None:
            return
        self.pushstack(root)
        self.inorder(root.left, sum)
        if (root.left == None and root.right == None):
            if self.presentsum == sum:
                sublist = []
                for i in self.stack:
                    sublist.append(i)
                self.pathlist.append(sublist)
                self.flag = 1
        if (root.right != None):
            while self.stack[self.top] != root:
                self.popstack()
                if self.top == -1:
                    break
        self.inorder(root.right, sum)

    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        self.pathlist = []
        self.stack = []
        self.top = -1
        self.flag = 0
        self.presentsum = 0
        self.inorder(root, sum1)
        return self.pathlist
