__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def partition(self,arr,l,r):
        if l==r:
            return l+1
        x = arr[r]
        i = l
        for j in range(l,r+1):
            if arr[j]<=x:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                if i+1>r:
                    break
                i+=1
        temp = arr[i]
        arr[i] = arr[r]
        arr[r] = temp
        return i

    def findkthsmallest(self,arr,low,high,k):
        if k-1 > high or k-1 < low:
            return -1
        else:
            i = self.partition(arr,low,high)

            if i==k:
                return arr[i-1]
            if i >k:
                return self.findkthsmallest(arr,low,i-2,k)
            else:
                return self.findkthsmallest(arr,i+1,high,k)

    def kthsmallest(self, A, k):
        B = list(A)
        return self.findkthsmallest(B,0,len(A)-1,k)

A = Solution()
B = (94, 87, 100, 11, 23, 98, 17, 35, 43, 66, 34, 53, 72, 80, 5, 34, 64, 71, 9, 16, 41, 66, 96)
print A.kthsmallest(B,19)
