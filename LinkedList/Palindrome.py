__author__ = 'mushahidalam'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def checkpalin(self, listcontent):
        j = len(listcontent) - 1
        for i in range(0, len(listcontent)):
            if i > j:
                break
            if listcontent[i] == listcontent[j]:
                j -= 1
                continue
            else:
                return 0
            j -= 1
        return 1

    def lPalin(self, A):
        listcontent = []
        temp = A
        while temp != None:
            listcontent.append(temp.val)
            temp = temp.next
        res = self.checkpalin(listcontent)
        return res


A = Solution()
B = ListNode(1)
B.next = ListNode(2)
B.next.next = ListNode(1)
print(A.lPalin(B))
