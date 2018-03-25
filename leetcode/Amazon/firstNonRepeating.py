class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        if len(s) == 0:
            return -1
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
                continue
            dict[s[i]] = 1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1


obj = Solution()
print obj.firstUniqChar("loveleetcode")
