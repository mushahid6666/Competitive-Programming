import collections, sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 :
            return ""
        if len(t) == 1:
            if t[0] in s:
                return t
        targetLetterMap = collections.defaultdict(int)
        for char in t:
            targetLetterMap[char] +=1
        i = 0
        j = 1
        cur_str = 1
        min_len_str = s[0]
        min_len_str_len = sys.maxint
        target_count = len(t)
        if s[0] in targetLetterMap:
            targetLetterMap[s[0]] -=1
            target_count -=1
        # S = "ADOBECODEBANC"
        #           i    j
        # map = A : 0 , B = 1, C = 1
        while i < len(s) and j < len(s):
            if target_count !=0 and s[j] in targetLetterMap:
                targetLetterMap[s[j]] -= 1
                if targetLetterMap[s[j]] >= 0:
                    target_count-=1
            if target_count == 0:
                while i < j and s[i] not in targetLetterMap:
                    i += 1
                if j-i+1 < min_len_str_len:
                    min_len_str_len = j-1 +1
                    min_len_str = s[i:j+1]
                if i < j:
                    targetLetterMap[s[i]] += 1
                    if targetLetterMap[s[i]] ==1:
                        target_count +=1
                    i += 1
                while i < j and s[i] not in targetLetterMap:
                    i+=1
            j+=1


        if min_len_str_len == sys.maxint:
            return ""
        return min_len_str

obj = Solution()
S = "ADOBECODEBANC"
T = "AE"
print obj.minWindow(S, T)