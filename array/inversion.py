class Solution:
    # @param A : list of integers
    # @return an integer
    def compare(self,a,b):
        if(a>b):
            return a
        else:
            return b

    def countInversions(self, A):
        subarr = []
        count = 0
        for i in range(0,len(A)):
            if i == len(A)-1:
                break
            subarr = A[i+1:]
            subarr.sort()
            n = len(subarr)
            j=0
            while j<n and A[i] > subarr[j]:
                # print(A[i],subarr[n-1-j])
                count+=1
                j+=1
            # print(subarr)
        return count
            
        
A = Solution()
B = [2, 4, 1, 3, 5]
# print((int(B)-2000)/100)
print A.countInversions(B)