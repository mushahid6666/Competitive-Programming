__author__ = 'mushahidalam'
import sys
class Treenode:
    def __init__(self,x):
        self.left =None
        self.val =x
        self.right = None

class Solution:
    # Solution 1
    # stack = []
    # def PrintAllPaths(self,root):
    #     if root==None:
    #         return
    #     self.stack.append(root)
    #     if root.left==None and root.right==None:
    #         for i in range(0,len(self.stack)):
    #             if i==0:
    #                 print self.stack[i].val,
    #                 continue
    #             print "->",self.stack[i].val,
    #         print "\n"
    #     self.PrintAllPaths(root.left)
    #     while self.stack[-1] !=root:
    #         self.stack.pop()
    #     self.PrintAllPaths(root.right)


    # 2rd Attempt Time limit exceeded in Online Judge
    # i think it's memory issue
    # result = []
    # def travers(self,A,key,path):
    #     if A==None:
    #         return
    #     path.append(A.val)
    #     key = key - A.val
    #     if key==0:
    #         if A.left==None and A.right==None:
    #             self.result.append(path)
    #             return
    #     self.travers(A.left,key,path[:])
    #     self.travers(A.right,key,path[:])
    #
    # def pathSum(self, root, sum1):
    #     result = []
    #     self.travers(root,sum1,[])
    #     return self.result

    # Online Judge Leetcode,Interviewbit code

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
        if root==None:
            return
        self.pushstack(root)
        self.inorder(root.left, sum)
        if (root.left == None and root.right == None):
            if self.presentsum == sum:
                sublist = []
                for i in self.stack:
                    sublist.append(i.val)
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

obj = Solution()
A = Treenode(5)
A.left = Treenode(1000)
A.left.right = Treenode(10)
A.right = Treenode(2)
A.right.left = Treenode(6)
A.right.right = Treenode(5)

print obj.pathSum(A, 1015)
