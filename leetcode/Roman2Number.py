class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convertmap = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = s[0]
        for i in range(len(s)):
            if convertmap[prev] < convertmap[s[i]]:
                result -= convertmap[prev]
                result += (convertmap[s[i]] - convertmap[prev])
                prev = s[i]
            else:
                result += convertmap[s[i]]
                prev = s[i]
        return result


obj = Solution()
print obj.romanToInt("XCV")
print obj.romanToInt("MCMXCVI")
print obj.romanToInt("MDCCCLXXXIV")
