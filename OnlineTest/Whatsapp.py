__author__ = 'mushahidalam'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, List1, List2):
        MergedListHead = None
        CurrentMergePointer = None
        if List1 == None and List2 == None:
            return None
        if List1 == None:
            return List2
        if List2 == None:
            return List1
        flag = 0
        List1Pointer = List1
        List2Pointer = List2
        CurrentMergePointer = List1
        while List1Pointer != None and List2Pointer != None:
            if List1Pointer.val < List2Pointer.val:
                if MergedListHead == None:
                    MergedListHead = List1
                    CurrentMergePointer = List1
                    List1Pointer = List1Pointer.next
                    continue
                CurrentMergePointer.next = List1Pointer
                CurrentMergePointer = CurrentMergePointer.next
                List1Pointer = List1Pointer.next
            else:
                if MergedListHead == None:
                    MergedListHead = List2
                    CurrentMergePointer = List2
                    List2Pointer = List2Pointer.next
                    continue
                CurrentMergePointer.next = List2Pointer
                CurrentMergePointer = CurrentMergePointer.next
                List2Pointer = List2Pointer.next

        while List1Pointer != None:
            CurrentMergePointer.next = List1Pointer
            CurrentMergePointer = CurrentMergePointer.next
            List1Pointer = List1Pointer.next
        while List2Pointer != None:
            CurrentMergePointer.next = List2Pointer
            CurrentMergePointer = CurrentMergePointer.next
            List2Pointer = List2Pointer.next

        i = MergedListHead
        while i != None:
            print(i.val)
            i = i.next
        return MergedListHead

    def split(self, list1, list2):

    def MergeSort(self, List):
        if List == None or List.next == None:
            return List
        self.split(List, A, B)
        self.MergeSort(A)
        self.MergeSort(B)


obj = Solution()
A = ListNode(8)
A.next = ListNode(10)
B = ListNode(9)
B.next = ListNode(11)
obj.mergeTwoLists(A, B)
