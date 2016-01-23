__author__ = 'mushahidalam'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        unsorted = []
        for i in range(0, len(A)):
            list = A[i]
            while list != None:
                unsorted.append(list.val)
                list = list.next
        unsorted.sort()
        result = None
        temp = None
        for i in range(0, len(unsorted)):
            if result == None:
                result = ListNode(unsorted[i])
                temp = result
            else:
                temp.next = ListNode(unsorted[i])
                temp = temp.next
        return result
