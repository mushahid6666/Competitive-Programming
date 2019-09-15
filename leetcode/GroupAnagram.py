import copy
class Solution(object):
    #Attempt2
    def merge(self, str1, str2):
        i = 0
        j = 0
        result_str = ""
        while i < len(str1) and j < len(str2):
            if ord(str1[i]) < ord(str2[j]):
                result_str += str1[i]
                i+= 1
            else:
                result_str += str2[j]
                j += 1
        while i < len(str1):
            result_str += str1[i]
            i += 1
        while j < len(str2):
            result_str += str2[j]
            j += 1
        return result_str
    def mergeSort(self, string, low, high):
        if low == high:
            return string[low]
        if low < high:
            mid = (low + high)/ 2
            str1  = self.mergeSort(string, low, mid)
            str2 = self.mergeSort(string, mid+1, high)
            result  = self.merge(str1, str2)
            return result
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        anagram_dict = dict()
        for string in strs:
            original_str = copy.deepcopy(string)
            string = self.mergeSort(string, 0, len(string)-1)
            # print original_str, string,
            # print " Dict: ", anagram_dict
            if string in anagram_dict:
                anagram_dict[string].append(original_str)
            else:
                anagram_dict[string] = [original_str]
        for string in anagram_dict:
            result.append(anagram_dict[string])
        return result

    #Previous Accepted Solution
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     n = len(strs)
    #     if n == 1 or n == 0:
    #         return [[strs[0]]]
    #     Strs_sorted_list = []
    #     strs_map = {}
    #     for str in strs:
    #         sorted_str = sorted(str)
    #         temp = ""
    #         for j in sorted_str:
    #             temp += j
    #         strs_map[temp] = []
    #         Strs_sorted_list.append(temp)
    #     for i in range(n):
    #         list = strs_map[Strs_sorted_list[i]]
    #         list.append(strs[i])
    #         strs_map[Strs_sorted_list[i]] = list
    #     keys = strs_map.keys()
    #     result = []
    #     for str in keys:
    #         result.append(strs_map[str])
    #
    #     return result


GroupAnagram = Solution()
print GroupAnagram.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

print GroupAnagram.groupAnagrams(["eat", "tea", "tan", ])

print GroupAnagram.groupAnagrams(["ate",  "bat"])

print GroupAnagram.groupAnagrams([])
print GroupAnagram.groupAnagrams(["ate"])
