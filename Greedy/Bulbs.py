__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0
        invert = 0
        for i in range(0, len(A)):
            if invert % 2 == 0:
                if A[i] == 0:
                    A[i] == 1
                    count += 1
                    invert += 1
            else:
                if A[i] == 1:
                    A[i] == 1
                    count += 1
                    invert += 1
                else:
                    A[i] = 1
        return count


obj = Solution()
arr = [0, 1, 0, 1]
print obj.bulbs(arr)
