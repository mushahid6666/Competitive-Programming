# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge2Lists(self,list1, list2):
        list1ptr = list1
        list2ptr = list2

        MergeListPtr = None
        MergeListRoot = None
        while list1ptr != None and list2ptr != None:
            if list1ptr.val < list2ptr.val:
                if MergeListRoot == None:
                    MergeListRoot = ListNode(list1ptr.val)
                    MergeListPtr = MergeListRoot
                else:
                    MergeListPtr.next = ListNode(list1ptr.val)
                    MergeListPtr = MergeListPtr.next
                list1ptr = list1ptr.next
            else:
                if MergeListRoot == None:
                    MergeListRoot = ListNode(list2ptr.val)
                    MergeListPtr = MergeListRoot
                else:
                    MergeListPtr.next = ListNode(list2ptr.val)
                    MergeListPtr = MergeListPtr.next
                list2ptr = list2ptr.next
        while list1ptr != None:
            if MergeListRoot == None:
                MergeListRoot = ListNode(list1ptr.val)
                MergeListPtr = MergeListRoot
            else:
                MergeListPtr.next = ListNode(list1ptr.val)
                MergeListPtr = MergeListPtr.next
            list1ptr = list1ptr.next
        while list2ptr != None:
            if MergeListRoot == None:
                MergeListRoot = ListNode(list2ptr.val)
                MergeListPtr = MergeListRoot
            else:
                MergeListPtr.next = ListNode(list2ptr.val)
                MergeListPtr = MergeListPtr.next
            list2ptr = list2ptr.next
        return MergeListRoot




    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) ==0:
            return None
        i = 0
        j = i +1
        while len(lists) != 1:
            list1 = lists[i]
            list2 = lists[j]

            mergedList = self.merge2Lists(list1, list2)
            del lists[j]
            del lists[i]

            lists.insert(i, mergedList)
            i+=1
            j+=1
            if i==len(lists)-1 or i == len(lists):
                i = 0
                j = 1
        return lists[0]




obj = Solution()
list1Root = ListNode(1)
list1Root.next = ListNode(4)
list1Root.next.next = ListNode(5)

list2Root = ListNode(1)
list2Root.next = ListNode(3)
list2Root.next.next = ListNode(4)

list3Root = ListNode(2)
list3Root.next = ListNode(6)
arr = [list1Root, None, list3Root]
result = obj.mergeKLists(arr)
node = result
while node != None:
    print node.val, "->"
    node = node.next
