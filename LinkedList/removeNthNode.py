# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        previous = None
        start = head
        endPointer = head
        for i in range(n):
            endPointer = endPointer.next
        while endPointer != None:
            endPointer = endPointer.next
            previous = start
            start = start.next
        if previous == None:
            if head.next != None:
                head = head.next
                return head
            return None
        previous.next = start.next
        return head

def printResult(result):
    temp = result
    while temp != None:
        print temp.val, " -> " ,
        temp = temp.next
    print None

solutionObj = Solution()
Head = ListNode(2)
Head.next = ListNode(3)
Head.next.next = ListNode(4)
Head.next.next.next = ListNode(5)
Head.next.next.next.next = ListNode(6)
n = 2
printResult(solutionObj.removeNthFromEnd(Head, 1))


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         if head == None or head.next == None:
#             return None
#         if head.next.next == None and n == 1:
#             head.next = None
#             return head
#         elif head.next.next == None and n == 2:
#             temp = head
#             head = head.next
#             temp.next = None
#             return head
#
#         first_pointer = None
#         second_pointer = None
#         i = 0
#         while i < n + 1:
#             if first_pointer == None:
#                 first_pointer = head
#             else:
#                 first_pointer = first_pointer.next
#             i = i + 1
#         while first_pointer != None:
#             first_pointer = first_pointer.next
#             if second_pointer == None:
#                 second_pointer = head
#             else:
#                 second_pointer = second_pointer.next
#         if second_pointer == None:
#             head = head.next
#             return head
#         second_pointer.next = second_pointer.next.next
#         return head
# [1,2,3]
# 3
