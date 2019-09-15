from  numpy.random import choice
class RandomizedCollection(object):

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
        check_if_new = False
        if val not in self.members_set:
            check_if_new = True
            self.members_set.add(val)
        self.members.append(val)
        if not check_if_new:
            self.members_map[val].append(self.index)
        else:
            self.members_map[val] = [self.index]
        self.index += 1

        return check_if_new

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.members_set:
            length = len(self.members)-1
            index_list = self.members_map[val]
            if (index_list == 1 and index_list[0] != length) or length not in index_list:

                index = self.members_map[val][0]
                new_number = self.members[-1]
                self.members[index] = new_number

                self.members = self.members[:-1]

                index_list = self.members_map[new_number]
                if len(index_list) == 1:
                    self.members_map[new_number] = [index]
                else:
                    self.members_map[new_number].remove(length)
                    self.members_map[new_number].append(index)

                if len(self.members_map[val]) == 1:
                    del self.members_map[val]
                    self.members_set.remove(val)
                else:
                    self.members_map[val].remove(index)

            else:

                self.members = self.members[:-1]
                if len(self.members_map[val]) == 1:
                    self.members_set.remove(val)
                    del self.members_map[val]
                else:
                    self.members_map[val].remove(length)
            self.index -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        item_list = []
        probability_list = []
        length = len(self.members)
        for value in self.members_map:
            prob = float(len(self.members_map[value]))/float(length)

            item_list.append(value)
            probability_list.append(prob)

        rand_element = choice(item_list, 1, p = probability_list)
        return rand_element[0]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedCollection()
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
