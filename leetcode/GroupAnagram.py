class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n == 1 or n == 0:
            return [[strs[0]]]
        Strs_sorted_list = []
        strs_map = {}
        for str in strs:
            sorted_str = sorted(str)
            temp = ""
            for j in sorted_str:
                temp += j
            strs_map[temp] = []
            Strs_sorted_list.append(temp)
        for i in range(n):
            list = strs_map[Strs_sorted_list[i]]
            list.append(strs[i])
            strs_map[Strs_sorted_list[i]] = list
        keys = strs_map.keys()
        result = []
        for str in keys:
            result.append(strs_map[str])

        return result


GroupAnagram = Solution()
print GroupAnagram.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
