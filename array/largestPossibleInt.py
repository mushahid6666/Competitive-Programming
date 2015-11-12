

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def compare(self,x,y):
        # print(x,y)
        temp1 = str(x)+str(y)
        temp2 = str(y)+str(x)
        # print("result",temp1,temp2)
        if int(temp1)>int(temp2):
            return -1
        elif int(temp1)==int(temp2):
            return 0
        else:
            return 1
    def largestNumber(self, A):
        str3 = ''
        A = sorted(A,cmp = self.compare)
        # print(A)
        # sortedlist = [A[0]]
        # for i in range(1,len(A)):
        #     str1 = int(repr(A[i])[0])
        #     for j in range(0,len(sortedlist)):
        #         str2 = int(repr(sortedlist[j])[0])
        #         # print(int(str2),str1)
        #         if int(str1) >= int(str2):
        #             sortedlist.insert(j,A[i])
        #             # print(A[i])
        #             break
        #         else:
        #             continue
        # print(sortedlist)
        for i in range(0,len(A)):
            str3 = str3+str(A[i])
        if str3[0] == '0':
            return 0
        return str3
A = Solution()
B = [472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412]
print A.largestNumber(B)