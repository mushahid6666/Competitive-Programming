__author__ = 'mushahidalam'


class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        MOD = 10000003
        n = len(A)
        position = [0] * n
        for i in range(0, n):
            if A[i] == '.':
                position[i] = 0
            else:
                position[i] = 1
        steps = 0
        i = 0
        group = 1
        while i < n:
            if (i == 0 and position[i] == 1) or (i != 0 and position[i] == 1 and position[i - 1] == 0):
                k = i + 1
                prev = steps
                while k < n and position[k] != 1:
                    steps += 1
                    k += 1
                if k == n and position[k - 1] != 1:
                    steps = prev
                group += 1
                i = k
                position[k - 1] = 1
            elif i != n - 1 and position[i] == 1 and position[i + 1] != 1:
                k = i + 1
                prev = steps
                count = 0
                while k < n and position[k] != 1:
                    steps = steps + group
                    k += 1
                    count += 1
                if k == n and position[k - 1] != 1:
                    steps = prev
                    break
                if k != n - 1 and position[k + 1] == 0:
                    steps = prev + count
                    position[k] = 0
                    position[i + 1] = 1
                    i += 1
                elif k == n - 1:
                    steps = prev + count
                    i = k
                else:
                    position[k - 1] = 1
                    position[i] = 0
                    i = k
                group += 1
            elif i != n - 1 and position[i] == 1 and position[i + 1] == 1:
                group += 1
                i += 1
            else:
                i += 1
        steps = steps % MOD
        return steps


obj = Solution()
str = "x........."
print obj.seats(str)
