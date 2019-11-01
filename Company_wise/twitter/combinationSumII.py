
import copy
class Solution(object):
    def combination(self, k, n, startIndex, result, curComb):
        if len(curComb) ==k and n ==0:
            result.append(copy.deepcopy(curComb))
            return
        if len(curComb) > k:
            return
        for i in range(startIndex, 10):
            curComb.append(i)
            self.combination(k, n-i, i+1, result, curComb)
            curComb.pop()
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n ==0 or k ==0:
            return []
        result = []
        self.combination(k, n, 1, result, [])
        return result

obj = Solution()
k = 3
n = 7
print obj.combinationSum3(k, n)