# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        while temp.next.next != None:
            temp.val = temp.next.val
            temp = temp.next
        temp.val = temp.next.val
        delte_node = temp.next
        temp.next = None
        del delte_node
        return

obj = Solution()
#Test Case 1
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
obj.deleteNode(head.next.next)
temp = head
while temp != None:
    print temp.val,
    temp = temp.next
print "\n"

#Test Case 2
head = ListNode(4)
head.next = ListNode(5)
obj.deleteNode(head)
temp = head
while temp != None:
    print temp.val,
    temp = temp.next
print "\n"