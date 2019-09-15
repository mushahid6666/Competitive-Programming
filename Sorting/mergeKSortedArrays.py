# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution(object):
    def merge(self, list1, list2):
        i = 0
        j = 0
        result = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j += 1
        while i <len(list1):
            result.append(list1[i])
            i+=1

        while j <len(list2):
            result.append(list2[j])
            j+=1
        return result

    def mergeKLists(self, lists):
        """
        :type lists: List[List]
        :rtype: ListNode
        """
        # keep iterating until there is only one list remaining
        if len(lists) == 0:
            return []
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
                i+=1
                j+=1
            else:
                i = 0
                j = 1
        return lists[0]

obj = Solution()
lists = [[2, 5, 9], [3,6,11]]
print obj.mergeKLists(lists)
lists = [[2, 5, 9]]
print obj.mergeKLists(lists)
lists = [[2, 5, 9], [3, 6, 11], [-1, 1, 2]]
print obj.mergeKLists(lists)
lists = [[2, 5, 9], [3], [9],[2, 10]]
print obj.mergeKLists(lists)
lists = [[2, 5, 9], [3],[9]]
print obj.mergeKLists(lists)
lists = []
print obj.mergeKLists(lists)
