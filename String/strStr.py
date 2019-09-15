class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) ==0:
            return 0
        if len(needle) > len(haystack):
            return -1
        needleIndex = 0
        for i in range(len(haystack)):
            if haystack[i]== needle[needleIndex]:
                k = i
                while k<len(haystack) and needleIndex < len(needle) and haystack[k] == needle[needleIndex]:
                    needleIndex = needleIndex + 1
                    k = k +1
                if needleIndex == len(needle):
                    return i
                needleIndex = 0
        return -1

solObject = Solution()
haystack = "hello"
needle = "ll"
haystack = "aaaaa"
needle = "bba"
haystack = "random"
needle = "random"
print solObject.strStr(haystack, needle)