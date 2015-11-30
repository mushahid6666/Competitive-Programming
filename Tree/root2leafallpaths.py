__author__ = 'mushahidalam'
import sys
class Treenode:
    def __init__(self,x):
        self.left =None
        self.val =x
        self.right = None

class Solution:
    stack = []
    def PrintAllPaths(self,root):
        if root==None:
            return
        self.stack.append(root)
        if root.left==None and root.right==None:
            for i in range(0,len(self.stack)):
                if i==0:
                    print self.stack[i].val,
                    continue
                print "->",self.stack[i].val,
            print "\n"
        self.PrintAllPaths(root.left)
        while self.stack[-1] !=root:
            self.stack.pop()
        self.PrintAllPaths(root.right)

obj = Solution()
A = Treenode(5)
A.left = Treenode(1000)
A.left.right = Treenode(10)
A.right = Treenode(2)
A.right.left = Treenode(6)
A.right.right = Treenode(5)

print obj.PrintAllPaths(A)

