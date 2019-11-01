# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
import collections
class Solution(object):
    def groupAnagroupUsingDict(self,strs):
        if len(strs) == 0:
            return []
        anagram_dict = dict()
        for i in range(len(strs)):
            string = strs[i]
            orig_str = string
            string = "".join(sorted(string))
            if string in anagram_dict:
                anagram_dict[string].append(orig_str)
            else:
                anagram_dict[string] = [orig_str]
        result = []
        for key,value in anagram_dict.items():
            result.append(value)
        return result

    def groupAnagramUsingCount(self,strs):
        countDict = collections.defaultdict(list)
        for i in range(len(strs)):
            string = strs[i]
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            countDict[tuple(count)].append(string)
        return countDict.values()
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return self.groupAnagramUsingCount(strs)


obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print obj.groupAnagrams(strs)
strs = ["eat"]
print obj.groupAnagrams(strs)