class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2 :
            return x
        low, high = 2, x // 2
        while low <= high:
            mid = (low + high) /2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid -1
            else:
                low = mid + 1
        return high



obj = Solution()
x = 3
print obj.mySqrt(x)
# x = 8
# print obj.mySqrt(x)
x = 10230
print obj.mySqrt(x)
