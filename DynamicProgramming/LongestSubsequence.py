__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findindex(self, arr, left, right, key):
        while right - left > 1:
            mid = left + (right - left) / 2
            if arr[mid] >= key:
                right = mid
            else:
                left = mid
        return right

    def lis(self, A):
        size = len(A)
        Long_subseq = []
        Long_subseq.append(A[0])
        length = 1
        for i in range(1, size):
            if A[i] < Long_subseq[0]:
                Long_subseq[0] = A[i]
            elif A[i] > Long_subseq[length - 1]:
                Long_subseq.insert(length, A[i])
                length += 1
            else:
                Long_subseq[self.findindex(Long_subseq, 0, length - 1, A[i])] = A[i]
        return length


obj = Solution()
print obj.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
