__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        n = len(A)
        if B > n:
            return []
        result = []
        total = 0
        end = n - B + 1
        dict = {}
        count = 0
        distinct = 0
        for i in range(0, n):
            if count != B:
                if A[i] in dict:
                    dict[A[i]] += 1
                    count += 1
                    if count != B:
                        continue
                else:
                    dict[A[i]] = 1
                    distinct += 1
                    count += 1
                    if count != B:
                        continue
            result.append(distinct)
            total += 1
            if total == end:
                break
            if dict[A[i - (B - 1)]] == 1:
                distinct -= 1
                dict.pop(A[i - (B - 1)])
                count -= 1
            else:
                dict[A[i - (B - 1)]] -= 1
                count -= 1
        return result


obj = Solution()
A = [1, 2, 1, 3, 4, 3]
print obj.dNums(A, 3)
