__author__ = 'mushahidalam'
from collections import OrderedDict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []  # result list
        num = len(words)  # length of the str list
        ls = len(s)
        if num == 0:
            return []
        str_len = len(words[0])  # length of each str
        # create the map: count the occurrance of each string
        # Note that set(L) is used to reduce the time, otherwise will not pass the large test
        map_str = dict((x, words.count(x)) for x in set(words))
        i = 0
        while i + num * str_len - 1 < ls:
            map_str2 = {}
            j = 0
            while j < num:
                subs = s[i + j * str_len:i + j * str_len + str_len]
                if not subs in map_str:
                    break
                else:
                    # Note that dict.get(key, default_val) is used to handel the case that key NOT exist
                    map_str2[subs] = map_str2.get(subs, 0) + 1
                    if map_str2[subs] > map_str[subs]:
                        break
                    j = j + 1
            if j == num:
                res.append(i)
            i = i + 1

        return res


obj = Solution()
s = "abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabaccaacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa "
words = ["cac", "aaa", "aba", "aab", "abc"]
print obj.findSubstring(s, words)
# ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]
