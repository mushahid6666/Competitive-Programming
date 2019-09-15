# Given an array of characters, compress it in-place.
#
# The length after compression must always be smaller than or equal to the original array.
#
# Every element of the array should be a character (not int) of length 1.
#
# After you are done modifying the input array in-place, return the new length of the array.
# Follow up:
# Could you solve it using only O(1) extra space?
#
# Note:
#
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.
import copy
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return []
        if len(chars) == 1:
            return [chars[0]]
        def append_count(result, count, prev_char):
            result.append(prev_char)
            str_count = str(count)
            if count == 1:
                return
            if count > 9:
                for k in range(len(str_count)):
                    result.append(str_count[k])
            else:
                result.append(str_count)
        result = list()
        prev_char = chars[0]
        count = 1
        j = 1
        while j < len(chars):
            while j < len(chars) and chars[j] == prev_char:
                count += 1
                j+=1
            if j == len(chars):
                break
            append_count(result, count, prev_char)
            count = 1
            prev_char = chars[j]
            j+=1
        append_count(result, count, prev_char)
        for i in range(len(result)):
            chars[i] = result[i]
        chars = chars[:i+1]
        return len(result)

obj = Solution()
#Example 1
chars = ["a","a","b","b","c","c","c"]
result_len  = obj.compress(chars)
print chars, result_len
#
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

#Example 2
# chars = ["a"]
# print  chars, obj.compress(chars)
#
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
#
# Explanation:
# Nothing is replaced.

#Example 3
# chars =["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print  obj.compress(chars)
#
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
#
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.