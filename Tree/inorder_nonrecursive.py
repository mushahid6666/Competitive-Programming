__author__ = 'mushahidalam'
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
                current = stack.pop()
                current = current.right
                stack.append(current)
                if len(stack)!=0:
                    current = stack.pop()
                    current = current.right
                    stack.append(current)
                    list.append(current.val)
                else:
                    done=1