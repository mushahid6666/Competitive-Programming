__author__ = 'mushahidalam'


#Pending Not done. 2 solutions available . 2 stacks or 1 stack




# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        list = []
        current = A
        stack= []
        done =0
        while(done!=1):
            if current!=None:
                stack.append(current)
                current = current.left
            else:
                if len(stack)!=0:
                    current = stack.pop()
                    list.append(current.val)
                    current = current.right
                else:
                    done=1



