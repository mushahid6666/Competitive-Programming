__author__ = 'mushahidalam'
class PrevSmallest:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        smalllist = []
        stack = []
        for i in range(len(arr)):
            if len(stack)==0:
                smalllist.append(-1)
                stack.append(arr[i])
            else:
                flag=0
                for j in range(len(stack)-1,-1,-1):
                    if stack[j] < arr[i]:
                        smalllist.append(stack[j])
                        stack.append(arr[i])
                        flag=1
                        break
                    else:
                        stack.pop()
                if j==0:
                    if flag==0:
                        smalllist.append(-1)
                        stack.append(arr[i])
        return smalllist

A = PrevSmallest()
arr = [34, 35, 27, 42, 5, 28, 39, 20, 28]
print A.prevSmaller(arr)
