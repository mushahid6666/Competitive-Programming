__author__ = 'mushahidalam'


# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing

    def connect(self, root):
        queue = []
        if root == None:
            return root
        root.next = None
        if root.left == None and root.right == None:
            return root
        temp = [root, 0]
        level = 0
        while temp[0] != None:
            if level != 0:
                # print(temp)
                if temp[1] == queue[0][1]:
                    temp[0].next = queue[0][0]
                else:
                    temp[0].next = None
                queue.append([temp[0].left, temp[1] + 1])
                queue.append([temp[0].right, temp[1] + 1])
                temp = queue.pop(0)
            else:
                level += 1
                queue.append([temp[0].left, level])
                queue.append([temp[0].right, level])
                temp = queue.pop(0)
        return root
        # print root.next,root.left.next,root.right.next


obj = Solution()
root = TreeLinkNode(2)
root.left = TreeLinkNode(3)
root.right = TreeLinkNode(4)
root.left.left = TreeLinkNode(5)
root.left.right = TreeLinkNode(6)
root.right.left = TreeLinkNode(5)
root.right.right = TreeLinkNode(6)

root = obj.connect(root)
