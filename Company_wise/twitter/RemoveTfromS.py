class Solution(object):
    def __init__(self):
        self.deleteCount = 0

    def removalCount(self, s, t, curIndex):
        if len(s) == 0:
            return 0
        for i in range(curIndex, len(s)):
            endIndex = i + len(t)
            if endIndex >len(s):
                return 0
            elif s[i:endIndex] == t:
                newS = s[0:i] + s[endIndex:]

                newIndex = curIndex-len(t) + 1
                if newIndex < 0 :
                    newIndex = 0
                count = self.removalCount(newS, t, newIndex)
                return count + 1
        return 0
    def maxRemove(self, s, t):
        allStartIndexes = []
        for i in range(len(s)):
            j = i + len(t)
            if j <= len(s):
                if s[i:j] == t:
                    allStartIndexes.append(i)
        # for startIndex in allStartIndexes:
        count = self.removalCount(s, t, 0)
        self.deleteCount = max(self.deleteCount, count)
        return self.deleteCount


obj = Solution()
s = "aabcbc"
t = "abc"
print obj.maxRemove(s, t)
s = "abababaaba"
t = "ababa"
print obj.maxRemove(s, t)
s = "rogerabcroger"
t = "roger"
print obj.maxRemove(s, t)