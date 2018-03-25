class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[1] != s[0]:
                return 2
            return 1
        longest_sub = 0
        cur_longest_sub = 0
        start_index = 0
        for i in range(0, len(s)):
            if s[i] in dict:
                if dict[s[i]] < start_index:
                    dict[s[i]] = i
                    cur_longest_sub += 1
                    continue
                if cur_longest_sub > longest_sub:
                    longest_sub = cur_longest_sub
                start_index = dict[s[i]] + 1
                cur_longest_sub = i - start_index + 1
                dict[s[i]] = i
            else:
                dict[s[i]] = i
                cur_longest_sub += 1
        if cur_longest_sub > longest_sub:
            return cur_longest_sub
        return longest_sub


obj = Solution()
print obj.lengthOfLongestSubstring("abcabcbb")
print obj.lengthOfLongestSubstring("pwwkew")
print obj.lengthOfLongestSubstring("bbtablud")
