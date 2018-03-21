# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        len = 0
        temp = head
        while temp!=None:
            len+=1
            temp = temp.next
        if len == 1:
            return True
        if len ==0:
            return True
        mid = len/2
        if len%2!=0:
            mid +=1
        prev = None
        cur = None
        nextNode = head
        i=0
        while i!=mid:
            cur = nextNode
            nextNode = nextNode.next
            cur.next = prev
            prev = cur
            i+=1

        str1 = cur
        str2 = nextNode
        if len % 2 != 0:
            str1 = str1.next
        while (str1!=None and str2!=None):
            if str1.val == str2.val:
                str1 = str1.next
                str2 = str2.next
            else:
                return False
        return True

def createNode(list):
    if len(list)==0:
        return None
    head = ListNode(list[0])
    temp = head
    for i in range(1,len(list)):
        temp.next = ListNode(list[i])
        temp = temp.next
    return head


IsPaliLinkedList = Solution()
head = createNode(['a','b','c'])
print IsPaliLinkedList.isPalindrome(head)
