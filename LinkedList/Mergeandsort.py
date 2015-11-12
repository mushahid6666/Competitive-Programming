# Befinition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        mergehead = None
        merge = None
        if A==None and B==None:
            return None
        if A==None:
            return B
        if B==None:
            return A
        flag=0
        indexA = A
        indexB = B
        merge = A
        while indexA!=None and indexB!=None:
            if indexA.val < indexB.val:
                if mergehead == None:
                    mergehead = A
                    merge = A
                    indexA = indexA.next
                    continue
                merge.next = indexA
                merge = merge.next
                indexA = indexA.next
            else:
                if mergehead == None:
                    mergehead = B
                    merge = B
                    indexB = indexB.next
                    continue
                merge.next = indexB
                merge = merge.next
                indexB = indexB.next

        while indexA!=None:
            # print(i.val)
            merge.next = indexA
            merge = merge.next
            indexA = indexA.next
        while indexB!=None:
            # print(i.val)
            merge.next = indexB
            merge = merge.next
            indexB = indexB.next

        i=mergehead
        while i !=None:
            print(i.val)
            i=i.next
        return mergehead





A = Solution()
A = ListNode(8)
A.next = ListNode(10)
B = ListNode(9)
B.next = ListNode(11)
A.mergeTwoLists(A,B)