__author__ = 'mushahidalam'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        result = []
        stack = []
        stack.append(root)
        current_node = root
        # Termination condition
        while len(stack) != 0 and current_node != None:
            while current_node.left != None:
                stack.append(current_node.left)
                current_node = current_node.left
            print_node = stack.pop(-1)
            result.append(print_node.val)
            while current_node.right == None and len(stack) != 0:
                current_node = stack.pop(-1)
                result.append(current_node.val)
            stack.append(current_node.right)
            current_node = current_node.right
        return result

        #random attempt
        # list = []
        # current = root
        # stack= []
        # done =0
        # while(done!=1):
        #     if current!=None:
        #         stack.append(current)
        #         current = current.left
        #     else:
        #         current = stack.pop()
        #         current = current.right
        #         stack.append(current)
        #         if len(stack)!=0:
        #             current = stack.pop()
        #             current = current.right
        #             stack.append(current)
        #             list.append(current.val)
        #         else:
        #             done=1
        #

obj = Solution()
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(5)
# root.left.right = TreeNode(6)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(8)

print obj.inorderTraversal(root)