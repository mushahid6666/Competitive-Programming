class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    queue = []

    def connect(self, root):
        if root==None:
            return
        root.next = None
        temp = [root,0]
        level = 0
        while temp[0]!=None:
            if level!=0:
                # print(temp)
                if temp[1]==self.queue[0][1]:
                    temp[0].next = self.queue[0][0]
                else:
                    temp[0].next =None
                self.queue.append([temp[0].left,temp[1]+1])
                self.queue.append([temp[0].right,temp[1]+1])
                temp = self.queue.pop(0)
            else:
                level+=1
                self.queue.append([temp[0].left,level])
                self.queue.append([temp[0].right,level])
                temp = self.queue.pop(0)
        pass


A = Solution()
B = TreeLinkNode(1)
B.left= TreeLinkNode(2)
B.right= TreeLinkNode(3)
# B.left.left= TreeLinkNode(4)
# B.left.right= TreeLinkNode(5)
# B.right.left= TreeLinkNode(6)
# B.right.right= TreeLinkNode(7)
A.connect(B)
print(B.val)