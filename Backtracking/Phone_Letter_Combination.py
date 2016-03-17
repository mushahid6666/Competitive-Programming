__author__ = 'mushahidalam'


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        resut = ['']
        if len(digits) < 1:
            return []
        Map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for i in range(len(digits)):
            num = int(digits[i]) - int('0')
            if num < 0 or num > 9: break
            candidate = Map[num]
            temp = []
            for j in range(len(candidate)):
                for k in range(len(resut)):
                    temp.append(resut[k] + candidate[j])
            resut = temp[:]
        return resut


obj = Solution()
print obj.letterCombinations('23')
