'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.left_child_count = 0

class Solution(object):
    def __init__(self):
        self.root = None

    def addNode(self, node, val, small_node_count):
        if node == None:
            self.root = TreeNode(val)
            return self.root.left_child_count
        if val > node.val:
            if node.right == None:
                node.right = TreeNode(val)
                return small_node_count + 1 + node.left_child_count
            else:
                return self.addNode(node.right, val, small_node_count + node.left_child_count + 1)
        else:
            if node.left == None:
                node.left = TreeNode(val)
                node.left_child_count += 1
                return small_node_count
            else:
                node.left_child_count += 1
                return self.addNode(node.left, val, small_node_count)



    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.__init__()
        if len(nums) == 0:
            return []
        countArr = []
        for i in range(len(nums) -1, -1, -1):
            countArr.insert(0,self.addNode(self.root, nums[i], 0))
        return countArr

obj = Solution()
print obj.countSmaller([5,2,6,1])
print obj.countSmaller([5,9,10,11,12,1,2,3])
print obj.countSmaller([2,0,1])