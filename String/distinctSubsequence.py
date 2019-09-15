import copy
class Solution(object):
    def findsubstrs(self, s,t):
        if len(t) == 0:
            self.result += 1
            return
        while t[0] in s:
            index  = s.index(t[0])
            self.findsubstrs(s[index +1 :], t[1:])
            s = s[index +1 :]


    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if (len(s) == 0 and len(t)==0) or (len(t) == 0):
            return 1
        if len(s)==0:
            return 0
        # Recursive Solution
        # self.result = 0
        # self.findsubstrs(s, t)
        # return self.result

        #Dynamic Programming
        #2d array(len(t) + 1 * len(s) + 1) column=t , row = s,

        # first column already set to 0 as s> 1 doesn't match string t of len 0 except s=0
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t)+ 1)]

        # first row = empty t string
        for j in range(len(s) + 1):
            dp[0][j] = 1

        for i in range(0, len(t)) :
            for j in range(0, len(s) ):
                #Now if char[t.i] doesn't match s[j] we have same number of distinct subsequence as before
                if t[i] != s[j]:
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    # if they match we will have
                    # number of distinct subsequence as before + number of distinct subsequence with t[i-1]s[j-1]
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]

        return dp[len(t)][len(s)]


# s = "babgbag"
# t = "bag"
s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
t = "bddabdcae"
obj = Solution()
print obj.numDistinct(s,t)