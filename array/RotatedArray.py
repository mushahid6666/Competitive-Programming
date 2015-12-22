__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        low = 0
        high = len(A) - 1
        if A[low] <= A[high]:
            return A[low]
        while (low <= high):
            mid = (low + high) / 2
            if A[mid] <= A[(mid + 1) % n] and A[mid] <= A[(mid + n - 1) % n]:
                return A[mid]
            elif A[mid] <= A[high]:
                high = mid - 1
            elif A[mid] >= A[low]:
                low = mid + 1
        return -1


obj = Solution()
arr = [2, 1]
print obj.findMin(arr)
