class computeUgly:
    def __init__(self):
        self.ugly_list = [1]
        p2 = p3 = p5 = 0
        i = 0
        while i < 1690:
            ugly = min(self.ugly_list[p2] * 2, self.ugly_list[p3] * 3, self.ugly_list[p5] * 5)
            self.ugly_list.append(ugly)
            if ugly == self.ugly_list[p2] * 2:
                p2 += 1
            if ugly == self.ugly_list[p3] * 3:
                p3 += 1
            if ugly == self.ugly_list[p5] * 5:
                p5 += 1
            i += 1


class Solution(object):
    ugly = computeUgly()
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ugly.ugly_list[n-1]


obj = Solution()
print obj.nthUglyNumber(1)