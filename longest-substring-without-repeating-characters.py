"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or len(s)== 1:
            return len(s)
        curSubStrSet = set()
        i = 0
        j = i +1
        curSubStrSet.add(s[i])
        maxSubStrLen = 0
        while i < len(s) and j < len(s):
            if s[j] not in curSubStrSet:
                curSubStrSet.add(s[j])
                maxSubStrLen = max(maxSubStrLen, j - i + 1)
                j+=1
                continue
            else:
                while s[j] in curSubStrSet:
                    curSubStrSet.remove(s[i])
                    i+=1

        return maxSubStrLen

obj = Solution()
Input= "abcabcbb"
print obj.lengthOfLongestSubstring(Input), "Output: 3"
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

Input= "bbbbb"
print obj.lengthOfLongestSubstring(Input), "Output: 1"
# Explanation: The answer is "b", with the length of 1.
# Example 3:

Input= "pwwkew"
print obj.lengthOfLongestSubstring(Input), "Output: 3"