class Solution:
    # @param A : list of integers
    # @return an integer
    def mergesort(self, arr, low, high):
        invcount = 0
        if (high > low):
            mid = (low + high) / 2
            invcount = self.mergesort(arr, low, mid)
            invcount += self.mergesort(arr, mid + 1, high)
            invcount += self.merge(arr, low, mid + 1, high)
        return invcount

    def merge(self, arr, low, mid, high):
        temparr = []
        invcount = 0
        i = low
        j = mid
        # k = low
        while i <= mid - 1 and j <= high:
            if arr[i] <= arr[j]:
                temparr.append(arr[i])
                i += 1
            else:
                temparr.append(arr[j])
                invcount += mid - i
                j += 1
        while i <= mid - 1:
            temparr.append(arr[i])
            i += 1
        while j <= high:
            temparr.append(arr[j])
            j += 1
        for i in range(low, high + 1):
            arr[i] = temparr.pop(0)
        return invcount

    def countInversions(self, A):
        return self.mergesort(A, 0, len(A) - 1)


A = Solution()
B = [84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84,
     93, 67, 85, 16, 22, 60]
# print((int(B)-2000)/100)
print A.countInversions(B)
