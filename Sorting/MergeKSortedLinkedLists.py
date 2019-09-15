# Definition for singly-linked list.
import  copy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addNode(self, tailNode, newValue):
        newNode = ListNode(newValue)
        if tailNode == None:
            return newNode
        else:
            tailNode.next = newNode
            return newNode
    def merge(self, list1, list2):
        """
        :param list1: ListNode
        :param list2: ListNode
        :return:
        """
        list1_pointer = list1
        list2_pointer = list2
        result_pointer = None
        result_head = None
        while list1_pointer != None and list2_pointer !=None:
            if list1_pointer.val < list2_pointer.val:
                result_pointer = self.addNode(result_pointer, list1_pointer.val)
                if result_head  == None:
                    result_head  = result_pointer
                list1_pointer = list1_pointer.next
            else:
                result_pointer = self.addNode(result_pointer, list2_pointer.val)
                if result_head  == None:
                    result_head  = result_pointer
                list2_pointer = list2_pointer.next
        while list1_pointer != None:
            result_pointer = self.addNode(result_pointer, list1_pointer.val)
            if result_head == None:
                result_head = result_pointer
            list1_pointer = list1_pointer.next

        while list2_pointer != None:
            result_pointer = self.addNode(result_pointer, list2_pointer.val)
            if result_head == None:
                result_head = result_pointer
            list2_pointer = list2_pointer.next
        return result_head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # keep iterating until there is only one list remaining
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        i = 0
        j = 1
        while len(lists) != 1:
            if i < len(lists) and j < len(lists):
                list1 = copy.deepcopy(lists[i])
                list2 = copy.deepcopy(lists[j])
                result = self.merge(list1, list2)
                del lists[j]
                del lists[i]
                lists.insert(i, result)
                i += 1
                j += 1
            else:
                i = 0
                j = 1
        return lists[0]

obj = Solution()
list1 = ListNode(2)
list1.next = ListNode(5)
list1.next.next = ListNode(9)
list2 = ListNode(4)
list2.next = ListNode(7)
list2.next.next = ListNode(12)
lists = [list1, list2]
result =  obj.mergeKLists(lists)
temp = result
print "Test Case 1:",
while temp != None:
    print temp.val,
    temp = temp.next

print "\n"
list1 = ListNode(2)
list1.next = ListNode(5)
list1.next.next = ListNode(9)
list2 = ListNode(4)
list2.next = ListNode(7)
list2.next.next = ListNode(12)
list3 = ListNode(6)
list3.next = ListNode(8)
list3.next.next = ListNode(15)
lists = [list1, list2, list3]
result =  obj.mergeKLists(lists)
temp = result
print "Test Case 2:",
while temp != None:
    print temp.val,
    temp = temp.next
print "\n"

list1 = ListNode(2)
list1.next = ListNode(5)
list1.next.next = ListNode(9)
list2 = ListNode(4)
list2.next = ListNode(7)
list2.next.next = ListNode(12)
list3 = ListNode(8)
list4 = ListNode(-23)
list5 = ListNode(0)
lists = [list1, list2, list3, list4, list5]
result =  obj.mergeKLists(lists)
temp = result
print "Test Case 3:",
while temp != None:
    print temp.val,
    temp = temp.next
print "\n"

lists = []
result =  obj.mergeKLists(lists)
temp = result
print "Test Case 4:",
print result
print "\n"

list1 = ListNode(2)
lists = [list1]
result =  obj.mergeKLists(lists)
temp = result
print "Test Case 5:",
while temp != None:
    print temp.val,
    temp = temp.next
print "\n"

list1 = ListNode(2)
list2 = ListNode(-20)
lists = [list1, list2]
result =  obj.mergeKLists(lists)
temp = result
print "Test Case 6:",
while temp != None:
    print temp.val,
    temp = temp.next
print "\n"