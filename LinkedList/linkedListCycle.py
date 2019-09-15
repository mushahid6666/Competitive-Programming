# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        oneStepPointer = head
        twoStepPointer = head
        while twoStepPointer !=None:
            if twoStepPointer.next == None:
                return False
            oneStepPointer = oneStepPointer.next
            twoStepPointer = twoStepPointer.next.next
            if oneStepPointer == twoStepPointer:
                return True

        return False

obj = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(-4)
head.next.next.next = head.next
print obj.hasCycle(head)
head = ListNode(3)
print obj.hasCycle(head)
