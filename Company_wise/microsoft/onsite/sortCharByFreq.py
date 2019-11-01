"""Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters."""
import collections
class Solution(object):
    def compare(self, a, b):
        if a[1] < b[1]:
            return 1
        elif a[1] > b[1]:
            return -1
        else:
            return 0
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0 or len(s)==1:
            return s
        freq_dict = collections.defaultdict(int)
        for char in s:
            freq_dict[char] += 1
        key_value_list = freq_dict.items()
        key_value_list.sort(self.compare)
        result = []
        for entry in key_value_list:
            for i in range(entry[1]):
                result.append(entry[0])
        return "".join(result)


obj = Solution()
string = "cccaaa"
print obj.frequencySort(string)
string = "tree"
print obj.frequencySort(string)
string = "Aabb"
print obj.frequencySort(string)