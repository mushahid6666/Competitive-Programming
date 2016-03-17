__author__ = 'mushahidalam'


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n = len(x)
        i = 0;
        while i + 3 < n:
            if x[i] >= x[i + 2]:
                if x[i + 1] <= x[i + 3]:
                    return True
            i = i + 1
        return False


obj = Solution()
x1 = [2, 1, 1, 2]
x2 = [1, 2, 3, 4]
x3 = [1, 1, 1, 1]
x4 = [1, 1, 2, 2, 1, 1]

print obj.isSelfCrossing(x1)
print obj.isSelfCrossing(x2)
print obj.isSelfCrossing(x3)
print obj.isSelfCrossing(x4)
