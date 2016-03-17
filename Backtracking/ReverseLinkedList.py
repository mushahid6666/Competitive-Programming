__author__ = 'mushahidalam'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    head = None

    def reverse(self, node, prev):
        if node == None: return None
        if (node.next == None): self.head = node
        self.reverse(node.next, node)
        node.next = prev

    def reverseList(self, A):
        # Using Space O(n)
        # if A==None:
        #     return None
        # if A.next==None:
        #     return A
        # temp = A
        # result = []
        # while temp!=None:
        #     result.append(temp.val)
        #     temp = temp.next
        # temp = A
        # i=len(result)-1
        # while temp!=None:
        #     temp.val = result[i]
        #     temp = temp.next
        #     i-=1
        # return A

        # Using Recurssion
        if A == None:
            return None
        if A.next == None:
            return A
        self.head = None
        self.reverse(A, None)
        return self.head


obj = Solution()
root = ListNode(2)
root.next = ListNode(3)
root.next.next = ListNode(4)
temp = obj.reverseList(root)
while temp != None:
    print(temp.val)
    temp = temp.next
