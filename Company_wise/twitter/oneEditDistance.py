class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        if n1 > n2:
            return self.isOneEditDistance(t, s)

        if n1 - n1 > 1:
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                if n1 == n2:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return n1 + 1 == n2



    def isOneEditDistance1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) ==0  and len(t)==0:
            return False
        editDistance=[[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(1,len(t) + 1):
            editDistance[0][i] = editDistance[0][i-1] + 1

        for i in range(1,len(s) +1):
            editDistance[i][0] = editDistance[i-1][0] + 1

        for i in range(1, len(s) +1):
            for j in range(1, len(t) + 1):
                if s[i-1]==t[j-1]:
                    editDistance[i][j] = editDistance[i-1][j-1]
                else:
                    editDistance[i][j] = 1 + min(editDistance[i - 1][j - 1], editDistance[i][j - 1], editDistance[i -1][j])
        if editDistance[len(s)][len(t)] == 1:
            return True
        return False

obj = Solution()
s = "cab"
t = "ad"
print obj.isOneEditDistance(s,t)
s = "a"
t = "abc"
print obj.isOneEditDistance(s,t)