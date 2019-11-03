import collections
class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        m = len(str1)
        n = len(str2)
        if m != n:
            return False
        if m==1 and n==1:
            if str1[0] != str2[0]:
                return False
            return True
        letterMap1 = collections.defaultdict(list)
        letterMap2 = collections.defaultdict(list)
        for i in range(len(str1)):
            cur_char = str1[i]
            letterMap1[cur_char].append(i)
            cur_char = str2[i]
            letterMap2[cur_char].append(i)

        indexes_to_check = []
        for val in letterMap1.values():
            if len(val) > 1:
                indexes_to_check.append(val)
        if len(letterMap1) == 26 and len(letterMap2) == 26:
            return False
        for cur_arr in indexes_to_check:
            char_to_check = str2[cur_arr[0]]
            for i in range(1, len(cur_arr)):
                if str2[cur_arr[i]] != char_to_check:
                    return False
        return True




obj = Solution()
# str1 = "aabcc"
# str2 = "ccdee"
# print obj.canConvert(str1, str2)
# str1 = "leetcode"
# str2 = "codeleet"
# print obj.canConvert(str1, str2)
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "bcdefghijklmnopqrstuvwxyza"
print obj.canConvert(str1, str2)
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "bcdefghijklmnopqrstuvwxyzq"
print obj.canConvert(str1, str2)
