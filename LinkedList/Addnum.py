__author__ = 'mushahidalam'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        temp1 = A
        temp2 = B
        carry = -1
        i = 0
        if temp1.val == 0 and temp1.next == None:
            while temp2 != None:
                if i == 0:
                    newhead = ListNode(temp2.val)
                    finaltemp = newhead
                    i += 1
                else:
                    finaltemp.next = ListNode(temp2.val)
                    finaltemp = finaltemp.next
                temp2 = temp2.next
            return newhead
        if temp2.val == 0 and temp2.next == None:
            while temp1 != None:
                if i == 0:
                    newhead = ListNode(temp1.val)
                    finaltemp = newhead
                    i += 1
                else:
                    finaltemp.next = ListNode(temp1.val)
                    finaltemp = finaltemp.next
                temp1 = temp1.next
            return newhead
        while temp1 != None and temp2 != None:
            if carry != -1:
                k = temp1.val + temp2.val + carry
            else:
                k = temp1.val + temp2.val
            if k > 9:
                # print(k)
                num = k % 10
                carry = k / 10
                # print(num,carry)
            else:
                num = k
                carry = -1
            if i == 0:
                newhead = ListNode(num)
                finaltemp = newhead
                i += 1
            else:
                finaltemp.next = ListNode(num)
                finaltemp = finaltemp.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp2 == None and temp1 != None and carry != -1:
            k = temp1.val + carry
            if k > 9:
                num = k % 10
                carry = k / 10
            else:
                num = k
                carry = -1
            if i == 0:
                newhead = ListNode(num)
                finaltemp = newhead
                i += 1
            else:
                finaltemp.next = ListNode(num)
                finaltemp = finaltemp.next
            temp1 = temp1.next
        while temp1 == None and temp2 != None and carry != -1:
            k = temp2.val + carry
            if k > 9:
                num = k % 10
                carry = k / 10
            else:
                num = k
                carry = -1
            if i == 0:
                newhead = ListNode(num)
                finaltemp = newhead
                i += 1
            else:
                finaltemp.next = ListNode(num)
                finaltemp = finaltemp.next
                temp2 = temp2.next
        while temp1 != None and temp2 == None:
            finaltemp.next = ListNode(temp1.val)
            finaltemp = finaltemp.next
            temp1 = temp1.next
        while temp2 != None and temp1 == None:
            finaltemp.next = ListNode(temp2.val)
            finaltemp = finaltemp.next
            temp2 = temp2.next
        if carry != -1:
            finaltemp.next = ListNode(carry)
            finaltemp = finaltemp.next
        return newhead


head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(3)
head2 = ListNode(7)
head2.next = ListNode(1)
# head2.next.next = ListNode(4)
obj = Solution()
newlist = obj.addTwoNumbers(head, head2)
newlist.val
