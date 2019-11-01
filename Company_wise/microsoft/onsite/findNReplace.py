# To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).
#
# Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.
#
# For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".
#
# Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.
#
# All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
#
# Example 1:
#
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".
# Example 2:
#
# Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
# "ec" doesn't starts at index 2 in the original S, so we do nothing.
# Notes:
#
# 0 <= indexes.length = sources.length = targets.length <= 100
# 0 < indexes[i] < S.length <= 1000
# All characters in given inputs are lowercase letters.
import copy
class Solution(object):
    def compare(self, a , b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0

    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if len(S)== 0:
            return S

        index_src_targ = list()
        for i in range(len(indexes)):
            index_src_targ.append([indexes[i], sources[i], targets[i]])
        index_src_targ.sort(self.compare)

        result_str = copy.deepcopy(S)
        index_diff = 0
        for i in range(len(index_src_targ)):
            cur_trans = index_src_targ[i]
            index = cur_trans[0]
            src = cur_trans[1]
            src_length = len(cur_trans[1])
            target = cur_trans[2]
            if S[index: index+ src_length] == src:
                result_str = "".join((result_str[:index + index_diff],target,  result_str[index + index_diff + src_length :] ))
                index_diff += len(target) - len(src)
        return result_str


obj = Solution()
S = "abcd"
indexes = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
print obj.findReplaceString(S, indexes, sources, targets)
S = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print obj.findReplaceString(S, indexes, sources, targets)
S = "af"
indexes = [0,1]
sources = ["a","f"]
targets = ["eee","ffff"]
print obj.findReplaceString(S, indexes, sources, targets)