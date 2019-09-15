__author__ = 'mushahidalam'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Attempt 2
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        list1NodeDict = dict()
        temp = headA
        while temp != None:
            list1NodeDict[temp] = 0
            temp = temp.next
        temp = headB
        while temp !=None:
            if temp in list1NodeDict:
                return temp
            temp = temp.next

{ #Previous Accepted Leetcode Solution
# class Solution:
#     # @param A : head node of linked list
#     # @param B : head node of linked list
#     # @return the head node in the linked list
#     def getIntersectionNode(self, A, B):
#         len1 =0
#         temp = A
#         while temp!=None:
#             temp = temp.next
#             len1+=1
#         len2=0
#         temp = B
#         while temp!=None:
#             temp = temp.next
#             len2+=1
#         if len1>len2:
#             d = len1-len2
#             temp = A
#             for i in range(0,d):
#                 temp = temp.next
#             temp2 = B
#             while temp!=None:
#                 if temp==temp2:
#                     return temp
#                 temp = temp.next
#                 temp2 = temp2.next
#             return None
#         else:
#             d = len2-len1
#             temp = B
#             for i in range(0,d):
#                 temp = temp.next
#             temp2 = A
#             while temp!=None:
#                 if temp!=temp2:
#                     return temp
#                 temp = temp.next
#                 temp2 = temp2.next
#             return None
}
A = Solution()
B = ListNode(1)
B.next = ListNode(5)
C = ListNode(8)
# C.next = ListNode(9)
C.next = B.next
B.next.next = ListNode(2)
B.next.next.next = ListNode(3)
temp =  A.getIntersectionNode(B,C)
while temp!=None:
    print(temp.val)
    temp = temp.next






