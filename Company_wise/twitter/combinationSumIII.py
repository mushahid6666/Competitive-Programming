import copy
class Solution(object):
    def combination(self, k, n, startIndex, result, cur_comb):
        if len(cur_comb) == k and n==0:
            result.append(copy.deepcopy(cur_comb))
            return
        if len(cur_comb)==k:
            return
        for i in range(startIndex, 10):
            cur_comb.append(i)
            self.combination(k, n-i, i +1, result, cur_comb)
            cur_comb.pop(-1)

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0 or k==0:
            return []
        result = []
        self.combination(k, n, 1, result, [])
        return result

obj = Solution()
k = 3
n = 9
print obj.combinationSum3(k, n)