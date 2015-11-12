__author__ = 'mushahidalam'
class Treenode:
    def __init__(self,x):
        self.left =None
        self.val =x
        self.right = None

class Solution:
    stack = []
    top = -1
    flag=0
    presentsum=0

    def pushstack(self,root):
        self.top+=1
        self.stack.append(root)
        self.presentsum+=root.val
        # print(self.stack)
    def popstack(self):
        self.top-=1
        self.presentsum-=self.stack.pop().val

    def inorder(self,root,sum):
        if root==None:
            return
        self.pushstack(root)
        self.inorder(root.left,sum)
        if(root.left==None and root.right==None):
            if self.presentsum==sum:
                self.flag=1
        if(root.left!=None or root.right!=None):
            if self.stack[self.top]!= root:
                self.popstack()
        self.inorder(root.right,sum)


    def hasPathSum(self, A, B):
        self.inorder(A,B)
        if self.flag==1:
            return 1
        return 0

obj = Solution()
A = Treenode(5)
A.left = Treenode(1000)
A.left.right = Treenode(10)
A.right = Treenode(2)
A.right.left = Treenode(6)
A.right.right = Treenode(5)

print obj.hasPathSum(A,2)
