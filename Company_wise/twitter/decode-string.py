"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
 Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
[3 ]
s = "3[a2[c]]", return "accaccacc".

s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c=="]":
                num= stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString



obj = Solution()
# s = "3[a]2[bc]"
# print obj.decodeString(s), "return aaabcbc"
s = "3[a]2[b4[F]c]"
print obj.decodeString(s)


# s = "3[a2[c]]"
# print obj.decodeString(s), "return accaccacc"
# s = "3[a2[c2[d]]]"
# print obj.decodeString(s), "return accaccacc"
# s = "asd"
# print obj.decodeString(s), "return accaccacc"
# s = "10[a]"
# print obj.decodeString(s), "return accaccacc"
#
# s = "2[abc]3[cd]ef",
# print obj.decodeString(s), "return abcabccdcdcdef"