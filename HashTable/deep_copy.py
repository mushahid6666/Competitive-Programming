__author__ = 'mushahidalam'
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    hashtable = {}
    hashlist = {}
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        temp = head
        i=0
        while temp!=None:
            if temp.random!=None:
                self.hashtable[i] = [temp.label,temp.random.label]
            else:
                self.hashtable[i] = [temp.label,None]
            i+=1
            temp= temp.next
        newhead=None
        temp = newhead
        for j in range(0,i):
            newnode = RandomListNode(self.hashtable[j][0])
            newnode.next=None
            newnode.random=None
            self.hashlist[newnode.label] = newnode
            if j==0:
                newhead=newnode
                temp = newhead
                continue
            temp.next=newnode
            temp = temp.next
        #print(self.hashtable)
        #print(self.hashlist)
        k=0
        temp = newhead
        while temp!=None:
            if self.hashtable[k][1]!= None:
                temp.random = self.hashlist[self.hashtable[k][1]]
                temp = temp.next
                ##print("setting to =",self.hashlist[self.hashtable[k][1]].label)
            else:
                temp.random = None
                temp = temp.next
            ##print("k=",k,"hastable=",self.hashtable[k][0],"haslist=",self.hashtable[k][1])
            k+=1
        return newhead


A = Solution()
head = RandomListNode(83)
head.next = RandomListNode(188)
head.next.next = RandomListNode(253)
head.next.next.next = RandomListNode(281)
head.random = head.next.next.next
head.next.next.next.random = head.next.next
newhead = A.copyRandomList(head)
temp = newhead
while temp!=None:
    if temp.next!=None and temp.random!=None:
        #print(temp.label,temp.next.label,temp.random.label)
    else:
        if temp.next == None and temp.random!=None:
            #print(temp.label,None,temp.random.label)
        if temp.next !=None and temp.random==None:
            #print(temp.label,temp.next.label,None)
        else:
            #print(temp.label,None,None)
    temp = temp.next

