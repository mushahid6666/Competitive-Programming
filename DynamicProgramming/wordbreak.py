__author__ = 'mushahidalam'


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        size = len(s)
        wb = [0] * (size + 1)
        for i in range(1, size + 1):
            if wb[i] == 0 and s[0:i] in wordDict:
                wb[i] = 1

            if wb[i] == 1:

                if i == size:
                    return True
                for j in range(i + 1, size + 1):

                    if wb[j] == 0 and s[i:j] in wordDict:
                        wb[j] = 1

                    if j == size and wb[j] == 1:
                        return True
        return False


obj = Solution()
worDict = {"mobile", "samsung", "sam", "sung", "man", "mango",
           "icecream", "and", "go", "i", "like", "ice", "cream"}
print obj.wordBreak('ilikesamsung', worDict)
