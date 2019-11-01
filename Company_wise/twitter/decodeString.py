'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution(object):
    def recursiveComputeString(self, substr, startIndex):

        i = startIndex
        resultStr = ""
        while i < len(substr):
            if substr[i].isdigit():
                childstr = ""
                repeat_count = ""
                while substr[i].isdigit():
                    repeat_count += substr[i]
                    i+=1
                repeat_count = int(repeat_count)
                repeatChar, k = self.recursiveComputeString(substr, i+1)
                for m in range(repeat_count):
                    childstr += repeatChar
                resultStr += childstr
                i = k
            elif substr[i] == "]" and startIndex != 0:
                return resultStr, i+1
            else:
                resultStr +=  substr[i]
                i+=1
        return resultStr, i+1

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)=="":
            return ""
        #Parse the input str
        result, index =  self.recursiveComputeString(s, 0)
        return result



s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
s = "2[3[a2[b]]]"
s = "100[leetcode]"
obj = Solution()
print obj.decodeString(s)