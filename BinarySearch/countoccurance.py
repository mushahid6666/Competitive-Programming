__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        if len(A)==1:
            if A[0]==B:
                return 1
            else:
                return 0
        high = len(A)-1
        low = 0
        mid = (low+high)/2
        index = 0
        while(low <= high):
            # print(low,high)
            if A[mid] == B:
                index=mid
                break
            if A[mid]>B:
                high= mid-1
            else:
                low=mid+1
            mid = (low+high)/2
            # print(low,high)
        print(index)
        i=index
        if index!=0:
            while A[i-1] == B:
                index-=index
                i-=1
                if index==0:
                    break
        count=0
        for i in range(index,len(A)):
            if A[i]==B:
                count+=1
        return count


A = Solution()
B = (8, 8, 8, 8,8, 8)
print A.findCount(B,8)
