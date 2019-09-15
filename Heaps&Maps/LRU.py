__author__ = 'mushahidalam'
import sys

class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    counter = int()
    capacity = int()
    current_capacity = int()
    keyDict = dict()
    head = None
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current_capacity = 0
        self.keyDict = dict()
        self.head = None
        self.last = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keyDict:

            node_address = self.keyDict[key]
            if node_address.key != self.last.key:
                if node_address.key == self.head.key:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    node_address.next.prev = node_address.prev
                    node_address.prev.next = node_address.next
                self.last.next = node_address
                node_address.prev = self.last
                self.last = node_address
            return node_address.val
        else:
            return -1

    def remove_least_recently_used_item(self):
        #O(1) solution using hashmap and linkedlist

        previous_head = self.head
        if self.last == self.head:
            self.head = None
            self.last = None
        else:
            previous_head = self.head
            self.head = self.head.next
            self.head.prev = None

        del self.keyDict[previous_head.key]
        del previous_head

        #O(n) solution using just hashmap
        # least_used_item = sys.maxint
        # least_used_item_key = int()
        # for key, value in self.keyDict.items():
        #     if value[1] < least_used_item:
        #         least_used_item = value[1]
        #         least_used_item_key = key
        # del self.keyDict[least_used_item_key]
        # self.current_capacity -= 1

    def update_existing_key(self, key, value):
        # O(1) solution using hashmap and linkedlist
        node_address = self.keyDict[key]
        if node_address.key != self.last.key:
            if node_address.key == self.head.key:
                self.head = self.head.next
                self.head.prev = None
            else:
                node_address.next.prev = node_address.prev
                node_address.prev.next = node_address.next
            self.last.next = node_address
            node_address.prev = self.last
            self.last = node_address

        node_address.val = value

        # O(n) solution using just hashmap
        # self.counter += 1
        # self.keyDict[key] = [value, self.counter]
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keyDict:
            self.update_existing_key(key, value)
            return
        if self.current_capacity == self.capacity:
            self.remove_least_recently_used_item()
        else:
            self.current_capacity += 1
        new_node = ListNode(key, value)
        if self.head == None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        self.keyDict[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Working Solution
# class LRUCache:
#     capacity = 0
#     dict = {}
#     count = 0
#     total = 0
#     # @param capacity, an integer
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.dict = {}
#         self.count = 0
#         self.total = 0
#
#     # @return an integer
#     def get(self, key):
#         if key in self.dict:
#             self.count += 1
#             self.dict[key][1] = self.count
#             return self.dict[key][0]
#         else:
#             return -1
#
#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def set(self, key, value):
#         if self.total != self.capacity:
#             if key in self.dict:
#                 self.count += 1
#                 self.dict[key][1] = self.count
#                 self.dict[key][0] = value
#                 return
#             else:
#                 self.count += 1
#                 self.dict[key] = [value, self.count]
#                 self.total += 1
#         else:
#             if key in self.dict:
#                 if self.dict[key][0] == value:
#                     self.count += 1
#                     self.dict[key][1] = self.count
#                     return
#                 else:
#                     self.count += 1
#                     self.dict[key][1] = self.count
#                     self.dict[key][0] = value
#                     return
#
#             lowest = sys.maxint
#             delkel = -1
#             for ele in self.dict:
#                 if self.dict[ele][1] < lowest:
#                     lowest = self.dict[ele][1]
#                     delkel = ele
#             del self.dict[delkel]
#             self.count += 1
#             self.dict[key] = [value, self.count]
#

# G 13 G 11 S 4 13 S 12 8 S 11 15 S 3 14 G 10 S 7 12 S 8 5 S 10 10 G 3 S 11 11 G 10 S 12 4
# S 11 6 S 2 14 S 4 8 S 7 7 G 7 G 8 G 13 S 3 8 G 11 S 2 15 S 11 11 S 8 10 S 6 4 G 4 S 9 6 G 3
# G 1 G 1 S 14 11 S 5 8 G 14 S 8 10 G 4 G 15 G 12 G 7 G 4 S 11 3 G 13 G 8

# -1 -1 -1 14 10 7 -1 -1 6 -1 -1 -1 -1 11 -1 -1 -1 -1 -1 -1 -1
# -1 -1 -1 14 10 7 -1 -1 6 -1 -1 -1 -1 11 -1 -1 -1 -1 -1 -1 10
obj = LRUCache(5)
print obj.get(13),
print obj.get(11),
obj.put(4, 13)
obj.put(12, 8)
obj.put(11, 15)
obj.put(3, 14)
print obj.get(10),
obj.put(7, 12)
obj.put(8, 5)
obj.put(10, 10)
print obj.get(3),
obj.put(11, 11)
print obj.get(10),
obj.put(12, 4)
obj.put(11, 6)
obj.put(2, 14)
obj.put(4, 8)
obj.put(7, 7)
print obj.get(7),
print obj.get(8),
print obj.get(13),
obj.put(3, 8)
print obj.get(11),
obj.put(2, 15)
obj.put(11, 11)
obj.put(8, 10)
obj.put(6, 4)
print obj.get(4),
obj.put(9, 6)
print obj.get(3),
print obj.get(1),
print obj.get(1),
obj.put(14, 11)
obj.put(5, 8)
print obj.get(14),
obj.put(8, 10)
print obj.get(4),
print obj.get(15),
print obj.get(12),
print obj.get(7),
print obj.get(4),
obj.put(11, 3)
print obj.get(13),
print obj.get(8)

print "Test Case 2:"
#TestCase 2:
obj = LRUCache(1)
obj.put(2,1)
print obj.get(2),
obj.put(3,2)
print obj.get(2),
print obj.get(3),
