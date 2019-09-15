# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Consider the following binary search tree:
#
#      5
#     / \
#    2   6
#   / \
#  1   3
# Example 1:
#
# Input: [5,2,6,1,3]
# Output: false
# Example 2:
#                              80
#              70                         90
#           60    75             85                    95
#      50      65          82        87           92          97
#  40     55            81    83   86   88   91      93     96    98
#[80,70,60,50,40,55,65,75,90,85,81,83,87,86,88,95,92,91,93,97,96,98]
#
# Input: [5,2,1,3,6]
#         [5,2,1, 3, 6]
# Output: true
# Follow up:
# Could you do it using only constant space complexity?
import sys
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) == 0 or len(preorder) == 1:
            return True
        low_bound = -sys.maxint
        stack = []
        for i in range(len(preorder)):
            if len(stack) == 0 or preorder[i] < preorder[i-1]:
                if preorder[i] < low_bound:
                    return False
                stack.append(preorder[i])
            else:
                while len(stack) > 0 and preorder[i] > stack[-1]:
                    low_bound = stack[-1]
                    stack.pop()
                stack.append(preorder[i])
        return True

obj = Solution()
# preorder = [5,2,1,3,6]
preorder = [5,2,6,1,3]
# preorder = [80,70,60,50,40,55,65,75,90,85,82,81,83,87,86,88,95,92,91,93,97,96,98]
print obj.verifyPreorder(preorder)