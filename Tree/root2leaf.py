__author__ = 'mushahidalam'
class Treenode:
    def __init__(self,x):
        self.left =None
        self.val =x
        self.right = None

class Solution:
    # Using Stack
    # stack = []
    # top = -1
    # flag=0
    # presentsum=0
    #
    # def pushstack(self,root):
    #     self.top+=1
    #     self.stack.append(root)
    #     self.presentsum+=root.val
    #     # print(self.stack)
    # def popstack(self):
    #     self.top-=1
    #     self.presentsum-=self.stack.pop().val
    #
    # def inorder(self,root,sum):
    #     if root==None:
    #         return
    #     self.pushstack(root)
    #     self.inorder(root.left,sum)
    #     if(root.left==None and root.right==None):
    #         if self.presentsum==sum:
    #             self.flag=1
    #             return
    #     if(root.right!=None):
    #         while self.stack[self.top]!= root:
    #             self.popstack()
    #             if self.top==-1:
    #                 break
    #     self.inorder(root.right,sum)
    #
    #
    # def hasPathSum(self, A, B):
    #     self.stack = []
    #     self.top = -1
    #     self.flag = 0
    #     self.presentsum = 0
    #     self.inorder(A,B)
    #     if self.flag==1:
    #         return 1
    #     return 0
    # Better Solution
    flag = 0

    def travers(self, A, key):
        if A == None:
            return
        key = key - A.val
        if key == 0:
            if A.left == None and A.right == None:
                self.flag=1
                return
        self.travers(A.left, key)
        self.travers(A.right, key)

    def hasPathSum(self, A, B):
        flag = 0
        self.travers(A, B)
        return self.flag

obj = Solution()
# A = Treenode(-2)
# A.right = Treenode(-3)

A = Treenode(5)
A.left = Treenode(0)
A.left.left = Treenode(0)
A.left.left.left = Treenode(1)
A.left.left.right = Treenode(2)
A.left.right = Treenode(0)
A.left.right.left = Treenode(0)
A.left.right.right = Treenode(0)
A.right = Treenode(2)
A.right.left = Treenode(6)
A.right.right = Treenode(5)
A.right.left.left = Treenode(7)
A.right.left.right = Treenode(8)
A.right.right.left = Treenode(9)
A.right.right.right = Treenode(10)

print obj.hasPathSum(A, 21)
