# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nums1 = []
        nums2 = []
        iter = l1
        while iter != None:
            nums1.insert(0, iter.val)
            iter = iter.next
        iter = l2
        while iter != None:
            nums2.insert(0, iter.val)
            iter = iter.next
        n1 = len(nums1)
        n2 = len(nums2)

        i, j = n1 - 1, n2 - 1
        result = []
        carry = 0
        while i >= 0 and j >= 0:
            sum_digit = nums1[i] + nums2[j] + carry
            if sum_digit > 9:
                carry = 1
                result.insert(0, sum_digit % 10)
            else:
                carry = 0
                result.insert(0, sum_digit)
            i -= 1
            j -= 1

        if i >= 0:
            while i >= 0:
                sum_digit = carry + nums1[i]
                if sum_digit > 9:
                    carry = 1
                    result.insert(0, sum_digit % 10)
                else:
                    carry = 0
                    result.insert(0, sum_digit)
                i -= 1

        if j >= 0:
            while j >= 0:
                sum_digit = carry + nums2[j]
                if sum_digit > 9:
                    carry = 1
                    result.insert(0, sum_digit % 10)
                else:
                    carry = 0
                    result.insert(0, sum_digit)
                j -= 1
        if i < 0 and j < 0 and carry == 1:
            result.insert(0, carry)

        head = ListNode(result[-1])
        prev_node = head
        for i in range(len(result) - 2, -1, -1):
            new_node = ListNode(result[i])
            prev_node.next = new_node
            prev_node = prev_node.next
        return head


def create_list(num):
    head = ListNode(num[-1])
    prev_node = head
    n = len(num)
    if n > 1:
        for j in range(n - 2, -1, -1):
            new_node = ListNode(num[j])
            if j == n - 2:
                head.next = new_node
                prev_node = new_node
            else:
                prev_node.next = new_node
                prev_node = prev_node.next
    return head


def print_number(result):
    iter = result
    while iter != None:
        print iter.val
        iter = iter.next


AddTwoNumbers = Solution()
result = AddTwoNumbers.addTwoNumbers(create_list([1]), create_list([9, 9]))
print_number(result)
