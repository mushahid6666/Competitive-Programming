__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def compkey(self,x,y):
        return x[1]-y[1]
    def twoSum(self, A, B):
        hashresult = {0:[]}
        hashtable={}
        for i in range(0,len(A)):
            hashtable[A[i]]=i
        for i in range(0,len(A)):
            target = B-A[i]
            if target in hashtable:
                hashresult[0].append([i,hashtable[target]])
        if len(hashresult[0])>1:
            lst = hashresult[0]
            print(lst)
            lst.sort(self.compkey)
            print(lst)
            return lst[0]
        if len(hashresult[0])==1:
            return hashresult[0]
        else:
            return []
        # print(lst)
obj = Solution()
A = (4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 )
print obj.twoSum(A,-3)

