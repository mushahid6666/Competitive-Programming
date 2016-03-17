__author__ = 'mushahidalam'
import sys


class LRUCache:
    capacity = 0
    dict = {}
    count = 0
    total = 0
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.count = 0
        self.total = 0

    # @return an integer
    def get(self, key):
        if key in self.dict:
            self.count += 1
            self.dict[key][1] = self.count
            return self.dict[key][0]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.total != self.capacity:
            if key in self.dict:
                self.count += 1
                self.dict[key][1] = self.count
                self.dict[key][0] = value
                return
            else:
                self.count += 1
                self.dict[key] = [value, self.count]
                self.total += 1
        else:
            if key in self.dict:
                if self.dict[key][0] == value:
                    self.count += 1
                    self.dict[key][1] = self.count
                    return
                else:
                    self.count += 1
                    self.dict[key][1] = self.count
                    self.dict[key][0] = value
                    return

            lowest = sys.maxint
            delkel = -1
            for ele in self.dict:
                if self.dict[ele][1] < lowest:
                    lowest = self.dict[ele][1]
                    delkel = ele
            del self.dict[delkel]
            self.count += 1
            self.dict[key] = [value, self.count]


# G 13 G 11 S 4 13 S 12 8 S 11 15 S 3 14 G 10 S 7 12 S 8 5 S 10 10 G 3 S 11 11 G 10 S 12 4
# S 11 6 S 2 14 S 4 8 S 7 7 G 7 G 8 G 13 S 3 8 G 11 S 2 15 S 11 11 S 8 10 S 6 4 G 4 S 9 6 G 3
# G 1 G 1 S 14 11 S 5 8 G 14 S 8 10 G 4 G 15 G 12 G 7 G 4 S 11 3 G 13 G 8

# -1 -1 -1 14 10 7 -1 -1 6 -1 -1 -1 -1 11 -1 -1 -1 -1 -1 -1 -1
# -1 -1 -1 14 10 7 -1 -1 6 -1 -1 -1 -1 11 -1 -1 -1 -1 -1 -1 10
obj = LRUCache(5)
print obj.get(13),
print obj.get(11),
obj.set(4, 13)
obj.set(12, 8)
obj.set(11, 15)
obj.set(3, 14)
print obj.get(10),
obj.set(7, 12)
obj.set(8, 5)
obj.set(10, 10)
print obj.get(3),
obj.set(11, 11)
print obj.get(10),
obj.set(12, 4)
obj.set(11, 6)
obj.set(2, 14)
obj.set(4, 8)
obj.set(7, 7)
print obj.get(7),
print obj.get(8),
print obj.get(13),
obj.set(3, 8)
print obj.get(11),
obj.set(2, 15)
obj.set(11, 11)
obj.set(8, 10)
obj.set(6, 4)
print obj.get(4),
obj.set(9, 6)
print obj.get(3),
print obj.get(1),
print obj.get(1),
obj.set(14, 11)
obj.set(5, 8)
print obj.get(14),
obj.set(8, 10)
print obj.get(4),
print obj.get(15),
print obj.get(12),
print obj.get(7),
print obj.get(4),
obj.set(11, 3)
print obj.get(13),
print obj.get(8),
