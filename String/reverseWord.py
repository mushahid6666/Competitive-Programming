class Solution:
    # @param A : string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle == '' or haystack == '':
            return -1
        print(haystack)

        length = len(haystack)
        print(length)
        lenstr = len(needle)
        for i in range(0,length):
            if needle==haystack[i:(i+lenstr)]:
                return i
            print(i,lenstr,haystack[i:i+lenstr])
        return -1



A = Solution()
B = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
C = "babaaa"
print A.strStr(B,C)