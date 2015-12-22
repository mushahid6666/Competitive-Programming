__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)
        low = 0
        high = len(A) - 1
        while (low <= high):
            if A[low] <= A[high]:
                start = low
                break
            mid = (low + high) / 2
            if A[mid] <= A[(mid + 1) % n] and A[mid] <= A[(mid + n - 1) % n]:
                start = mid
                break
            elif A[mid] <= A[high]:
                high = mid - 1
            elif A[mid] >= A[low]:
                low = mid + 1
        if B > A[n - 1]:
            high = start - 1
            low = 0
        else:
            low = start
            high = len(A) - 1
        while (low <= high):
            mid = (low + high) / 2
            if A[mid] == B:
                return mid
            if A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        return -1


obj = Solution()
arr = [101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100]
print(obj.search(arr, 202))
