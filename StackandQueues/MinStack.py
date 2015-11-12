__author__ = 'mushahidalam'
'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.'''
class MinStack:
    topele = -1
    stack=[]
    minstack = []
    stackmin = -1
    # @param x, an integer
    def push(self, x):
        flag = 0
        if self.topele==-1:
            self.minstack.append((x))
        self.topele+=1
        self.stack.append(x)
        if x <=self.minstack[-1]:
            self.minstack.append(x)


    # @return nothing
    def pop(self):
        if self.topele!=-1:
            # print('stack = ',self.stack)
            k = self.stack.pop()
            # print('****',k,self.stack)
            self.topele= self.topele -1
            if k == self.minstack[-1]:
                self.minstack.pop()
            # print('-----',self.minstack)

    # @return an integer
    def top(self):
        if self.topele!=-1:
            return self.stack[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if self.topele==-1:
            return -1
        else:
            return self.minstack[-1]

A = MinStack()
A.push(10)
A.push(9)
print(A.getMin())
A.push(8)
print(A.getMin())
A.push(7)
print(A.getMin())
A.push(6)
print(A.getMin())
A.pop()
print(A.getMin())
A.pop()
print(A.getMin())
A.pop()
print(A.getMin())
A.pop()
print(A.getMin())
A.pop()
print(A.getMin())

