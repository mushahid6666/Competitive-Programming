class Solution:
    # @param A : list of integers
    # @return an integer
    def compare(self,a,b):
        if(a>b):
            return a
        else:
            return b

    def countInversions(self, A):
        count = 0
        for i in range(0,len(A)):
            k = i+1
            temp  = A[i+1:]
            temp.sort()
            # print(temp)
            for j in range(0,len(temp)):
                # print("found",A[i],A[j])
                if A[i] > temp[j]:
                    count+=1
                    # print("found",A[i],A[j])
                else:
                    break
        return count
            
        
A = Solution()
B = [2, 4, 1, 3, 5]
# print((int(B)-2000)/100)
print A.countInversions(B)