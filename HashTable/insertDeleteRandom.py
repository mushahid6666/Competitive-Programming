import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.members_set = set()
        self.members = []
        self.members_map = dict()
        self.index = 0
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.members_set:
            return False
        else:
            self.members_set.add(val)
            self.members.append(val)
            self.members_map[val] = self.index
            self.index += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.members_set:

            if self.members_map[val] != len(self.members)-1:
                index = self.members_map[val]
                new_number = self.members[-1]
                self.members[index] = new_number
                self.members = self.members[:-1]
                self.members_map[new_number] = index
                self.members_set.remove(val)
            else:
                self.members_set.remove(val)
                self.members = self.members[:-1]
                del self.members_map[val]
            self.index -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand_index = random.randint(0,len(self.members)-1)
        return self.members[rand_index]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print obj.insert(3)
print obj.insert(-2)
print obj.remove(2)
print obj.insert(1)
print obj.insert(-3)
print obj.insert(-2)
print obj.remove(-2)
print obj.remove(3)
print obj.insert(-1)

print obj.remove(-3)
print obj.insert(1)
print obj.insert(-2)
print obj.insert(-2)
print obj.insert(-2)
print obj.insert(1)
print obj.getRandom()
print obj.insert(-2)
print obj.remove(0)
print obj.insert(-3)
print obj.insert(1)
