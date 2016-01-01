__author__ = 'mushahidalam'


class Solution(object):
    def compute(self, n, string):
        key = string
        result = ''
        count = 1
        for i in range(len(key)):
            if i == len(key) - 1:
                result += str(count) + key[i]
            elif key[i] == key[i + 1]:
                count += 1
            else:
                result += str(count) + key[i]
                count = 1
        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        key = "11"
        for _ in range(2, n):
            key = self.compute(n, key)
        return int(key)


obj = Solution()
print obj.countAndSay(3)
