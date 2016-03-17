__author__ = 'mushahidalam'


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        temp = head
        if temp == None:
            return None
        if temp.next == None:
            ResultHead = RandomListNode(temp.label)
            if head.random == None:
                return ResultHead
            if head.random == head:
                ResultHead.random = ResultHead
                return ResultHead
        while temp != None:
            newNode = RandomListNode(temp.label)
            newNode.next = temp.next
            temp.next = newNode
            temp = newNode.next
        ResultHead = head.next
        temp = head;
        while temp != None:
            if temp.random != None:
                temp.next.random = temp.random.next
                temp = temp.next.next
            else:
                temp.next.random = None
                if temp.next != None:
                    temp = temp.next.next
                else:
                    temp = temp.next
        temp = head;
        while temp != None:
            if temp.next != None:
                temp2 = temp.next.next
                if temp.next.next != None:
                    temp.next.next = temp.next.next.next
                else:
                    temp.next.next = None
                temp.next = temp2
            temp = temp.next
        return ResultHead


def ListGenerate(list):
    n = len(list)
    if n != 0:
        head = RandomListNode(list[0])
    temp = head
    for i in range(1, n):
        temp.next = RandomListNode(list[i])
        temp = temp.next


obj = Solution()
A = RandomListNode(1)
B = RandomListNode(-1)
A.random = None
B.random = None
obj.copyRandomList(A)
