__author__ = 'mushahidalam'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str2 = ''
        str1 = str(x)
        if x < 0:
            flag = 1
            str1 = str1[1:]
            str2=str2+'-'
        lt = len(str1)
        for i in range(0, len(str1)):
            str2 = str2+str1[lt-1-i]
        if int(str2) > 2147483648 or int(str2) < -2147483648:
            return 0
        return int(str2)


obj = Solution()
print(obj.reverse(9646324351))