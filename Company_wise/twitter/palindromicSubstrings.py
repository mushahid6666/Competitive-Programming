class Solution(object):
    def countPaliFromMidpoint(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] ==s[right]:
            count += 1
            left  -= 1
            right += 1
        return count

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        paliCount = 0
        for i in range(len(s)):
            #countEven
            paliCount += self.countPaliFromMidpoint(s, i ,i)
            #countOdd
            paliCount += self.countPaliFromMidpoint(s, i, i +1)
        return paliCount

obj = Solution()
string = "abc"
string = "aaa"
print obj.countSubstrings(string)