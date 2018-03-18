class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_str = len(s)
        if len_str == 1:
            return 1
        if len_str == 2:
            if s[0] == s[1]:
                return 2
            return 1
        dp = [[0 for _ in range(len_str)] for _ in range(len_str)]
        pali_str = ""
        max_length = 0
        for i in range(len_str):
            dp[i][i] = 1
            max_length = 1
            pali_str = s[i:i + 1]
        for i in range(len_str - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                max_length = 2
                pali_str = s[i:i + 2]
        for i in range(len_str - 3, -1, -1):
            for j in range(len_str - 1, 1, -1):
                if dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        pali_str = s[i:j + 1]

        return pali_str


obj = Solution()
print obj.longestPalindrome("ccc")
