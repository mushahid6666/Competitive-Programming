# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge2lists(self, list1, list2):
        root = None
        temp = None
        ptr1 = list1
        ptr2 = list2
        while ptr1 != None and ptr2 !=None:
            if ptr1.val < ptr2.val:
                if temp != None:
                    temp.next = ListNode(ptr1.val)
                    temp = temp.next
                else:
                    temp = ListNode(ptr1.val)
                    root = temp
                ptr1 = ptr1.next
            else:
                if temp != None:
                    temp.next = ListNode(ptr2.val)
                    temp = temp.next
                else:
                    temp = ListNode(ptr2.val)
                    root = temp
                ptr2 = ptr2.next
        while ptr1 != None:
            if temp != None:
                temp.next = ListNode(ptr1.val)
                temp = temp.next
            else:
                temp = ListNode(ptr1.val)
                root = temp
            ptr1 = ptr1.next

        while ptr2 !=None:
            if temp != None:
                temp.next = ListNode(ptr2.val)
                temp = temp.next
            else:
                temp = ListNode(ptr2.val)
                root = temp
            ptr2 = ptr2.next
        return root



    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        i=0
        j=1
        while len(lists) != 1:
            if i<len(lists) and j < len(lists):
                list1 = lists[i]
                list2 = lists[j]
                result = self.merge2lists(list1, list2)
                del lists[j]
                del lists[i]
                lists.insert(i, result)
                i+=1
                j+=1
            else:
                i=0
                j=1
        return lists[0]


obj = Solution()
root = ListNode(1)
root.next = ListNode(4)
root.next.next = ListNode(5)
root2 = ListNode(1)
root2.next = ListNode(3)
root2.next.next = ListNode(4)
root3 = ListNode(2)
root3.next = ListNode(6)
lists = [root, root2, root3]
result =  obj.mergeKLists(lists)
temp = result
while temp!=None:
    print temp.val,
    temp = temp.next
print "==="
root4 = ListNode(3)
lists = [root2, root4]
result =  obj.mergeKLists(lists)
temp = result
while temp!=None:
    print temp.val,
    temp = temp.next
