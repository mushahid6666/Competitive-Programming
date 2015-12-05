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
        hastlist = []
        hastlist.append(A[0])
        length = 1
        for i in range(1, size):
            if A[i] < hastlist[0]:
                hastlist[0] = A[i]
            elif A[i] > hastlist[length - 1]:
                hastlist.insert(length, A[i])
                length += 1
            else:
                hastlist[self.findindex(hastlist, -1, length - 1, A[i])] = A[i]
        return length


A = Solution()
list = [69, 54, 19, 51, 16, 54, 64, 89, 72, 40, 31, 43, 1, 11, 82, 65, 75, 67, 25, 98, 31, 77, 55, 88, 85, 76, 35, 101,
        44, 74, 29, 94, 72, 39, 20, 24, 23, 66, 16, 95, 5, 17, 54, 89, 93, 10, 7, 88, 68, 10, 11, 22, 25, 50, 18, 59,
        79, 87, 7, 49, 26, 96, 27, 19, 67, 35, 50, 10, 6, 48, 38, 28, 66, 94, 60, 27, 76, 4, 43, 66, 14, 8, 78, 72, 21,
        56, 34, 90, 89]
print A.lis(list)
