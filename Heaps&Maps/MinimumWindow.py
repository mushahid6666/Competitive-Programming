__author__ = 'mushahidalam'
import sys


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hasmap = dict()
        for c in t:
            if c in hasmap:
                hasmap[c] += 1
            else:
                hasmap[c] = 1
        start = 0;
        end = 0;
        counter = len(t)
        minStart = 0;
        minLen = sys.maxint
        size = len(s)
        while end < size:
            if s[end] in hasmap and hasmap[s[end]] > 0:
                counter -= 1
            elif s[end] not in hasmap:
                hasmap[s[end]] = 0
            hasmap[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - start < minLen:
                    minStart = start
                    minLen = end - start
                hasmap[s[start]] += 1
                if hasmap[s[start]] > 0:
                    counter += 1
                start += 1
        if minLen < sys.maxint:
            return s[minStart:minStart + minLen]
        return ''


if __name__ == '__main__':
    obj = Solution()
    answer = obj.minWindow('ADOBECODEBANC', 'ABC')
    print 'MinimumString=' + answer
