__author__ = 'mushahidalam'


class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1 or p[1] != '*':
            if (len(s) < 1 or (p[0] != '.' and s[0] != p[0])):
                return 0
            return self.isMatch(s[1:], p[1:])
        else:
            lt = len(s)
            i = -1
            while (i < lt and (i < 0 or p[0] == '.' or p[0] == s[i])):
                if self.isMatch(s[i + 1:], p[2:]):
                    return 1
                i += 1
            return 0
            # if len(p) >1:
            #     if p[1]!= '*':
            #         if p[0]=='*':
            #             return 0
            #         return  ((p[0]==s[0]) or  (p[0]=='.' and len(s)!=0)) and self.isMatch(s[1:],p[1:])
            #
            # while ((p[0] == s[0]) or (p[0]=='.' and len(s)!=0)):
            #     if self.isMatch(s,p[2:]):
            #         return 1
            #     s = s[1:]
            # return self.isMatch(s,p[2:])


obj = Solution()
print obj.isMatch("aab", "c*a*b")
