__author__ = 'mushahidalam'


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        n = len(A)

        if n == 0:
            return 0
        if n == 1:
            if A[0] > '0':
                return 1
            else:
                return 0

        if A[0] == '0':
            return 0
        result = [0] * (n + 1)

        result[0] = 1
        result[1] = 1

        for i in range(2, n + 1):
            if A[i - 1] > '0':
                result[i] = result[i - 1]

            if (A[i - 2] > '0' and A[i - 2] < '2') or (A[i - 2] == '2' and A[i - 1] < '7'):
                result[i] += result[i - 2]

            if A[i - 1] == '0' and A[i - 2] > '2':
                return 0

        return result[n]


obj = Solution()
print obj.numDecodings('2611055971756562')
