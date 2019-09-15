class Solution:
    # @param A : list of integers
    # @return an integer
    # def firstMissingPositive(self, A):
    #     A.sort()
    #     print(A)
    #     # if '1' not in B:
    #     #     return 1
    #     lt = len(A)
    #     if A[lt-1] <=0:
    #         return 1
    #     if lt ==1:
    #         return A[0]+1
    #     if A[lt-1] == 1:
    #         return 2
    #     for i in range(0,lt):
    #         if i==0 and A[i]>1:
    #             return 1
    #         if A[i] >0:
    #             try:
    #                 if A[i-1] <=0 and A[i]!=1:
    #                     return 1
    #             except:
    #                 pass
    #             try:
    #                 if A[i]+1 == A[i+1]:
    #                     continue
    #                 else:
    #                     return A[i]+1
    #             except:
    #                 continue
    #     return A[lt-1]+1
    # @param A : list of integers
    # @return an integer
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def segregate(self, arr, size):
        j = 0;
        for i in range(0, size):
            if arr[i] <= 0:
                self.swap(arr, i, j)
                j += 1
        return j

    def findmissingpostive(self, A, start, size):
        for i in range(0, size):
            if (abs(A[start + i]) - 1 < size) and (A[start + (abs(A[start + i]) - 1)] > 0):
                A[start + (abs(A[start + i]) - 1)] = -A[start + (abs(A[start + i]) - 1)]
        for i in range(0, size):
            if A[i + start] > 0:
                return i + 1
        return size + 1

    def firstMissingPositive(self, A):
        size = len(A)
        shift = self.segregate(A, size)
        return self.findmissingpostive(A, shift, size - shift)



A = Solution()
B = [-10, -20, 0, 1, 2, 3]
print A.firstMissingPositive(B)