"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you
 You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules
  of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
   e
   |
   v
w->r->t
   |
   V
   f

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edje_map = {}
        indegreeCount = [0 for i in range(26)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                indegreeCount[key] = 0
                edje_map[key] = set()

        for i in range(len(words) - 1):
            word1  = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if (word1[j] != word2[j]):
                    key1 = ord(word1[j]) - ord('a')
                    key2 = ord(word2[j]) - ord('a')
                    count = indegreeCount[key2]
                    if key2 not in edje_map[key1]:
                        indegreeCount[key2] = count + 1
                        edje_map[key1].add(key2)
                    break
        dictionary  = collections.deque()
        res = ''
        for i in range(26):
            if indegreeCount[i]==0 and i in edje_map:
                dictionary.appendleft(i)

        while len(dictionary) != 0:
            node = dictionary.pop()
            res += (chr(node + ord('a')))
            outgoing_edjes = edje_map[node]
            for connected_node in outgoing_edjes:
                indegreeCount[connected_node] -=1
                if indegreeCount[connected_node] ==0:
                    dictionary.appendleft(connected_node)

        if len(edje_map) != len(res):
            return ""
        return res


obj = Solution()
alien_dict = ["wrt","wrf","er","ett","rftt"]
alien_dict = ["za","zb","ca","cb"]
print obj.alienOrder(alien_dict)