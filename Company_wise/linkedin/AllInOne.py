class ListNode(object):
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

import collections
class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.startNode = None
        self.endNode = None
        self.keyMap = collections.defaultdict(list)

    def insertIntoList(self, key, value):
        newNode = ListNode(key, value)
        if self.startNode == None:
            self.startNode = newNode
        else:

            cur_node = self.startNode
            prev_node = None
            while cur_node != None and newNode.value > cur_node.value:
                prev_node = cur_node
                cur_node = cur_node.next
            if prev_node == None:
                self.startNode = newNode
                newNode.next = cur_node
            else:
                prev_node.next = newNode
                newNode.prev = prev_node
                newNode.next = cur_node
                if cur_node != None:
                    cur_node.prev = newNode
        return newNode

    def updateValueInList(self, key, value):
        nodeAddr = self.keyMap[key][1]
        nodeAddr.value = value
        prev_node = nodeAddr
        cur_node = nodeAddr
        while cur_node.next != None and cur_node.value > cur_node.next.value:
            prev_node = cur_node
            cur_node = cur_node.next
        if prev_node == nodeAddr:
            return nodeAddr
        else:
            nodeAddr.prev.next= nodeAddr.next
            nodeAddr.next.prev = nodeAddr.prev

            nodeAddr.next = cur_node
            nodeAddr.prev = prev_node
            prev_node.next = nodeAddr
            if cur_node != None:
                cur_node.prev = nodeAddr



    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key in self.keyMap:
            self.keyMap[key][0] +=1
            #Update Arr
            nodeAddr =self.updateValueInList(key, self.keyMap[key][0])
            self.keyMap[key][1] = nodeAddr
        else:
            nodeAddr = self.insertIntoList(key, 1)
            self.keyMap[key] = [1, nodeAddr]
    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """

# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("test1")
obj.inc("test1")
obj.inc("test2")
print obj.getMaxKey(),"Expected : test1"
print obj.getMinKey(),"Expected : test2"