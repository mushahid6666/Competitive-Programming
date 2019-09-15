__author__ = 'mushahidalam'


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List
        """
        #Attempt 2:
        # num2LetterDict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
        #                   7: "pqrs", 8:"tuv", 9:"wxyz"}
        #
        # result = []
        # indexTracker = []
        #
        # if len(digits) == 1:
        #     str = num2LetterDict[int(digits[0])]
        #     for letter in str:
        #         result.append(letter)
        #     return result
        # # queue = {}
        # # for number in digits:
        # #     queue[num2LetterDict[int(number)]] = 0
        # for i in range(len(digits)):
        #     indexTracker.append(0)
        # n = len(indexTracker)
        # j = n-2
        # while j >= 0:
        #     while indexTracker[j] < 3:
        #         k = n - 1
        #         while k != j:
        #             while indexTracker[k] < 3:
        #                 cur_string = ""
        #                 for m in range(len(digits)):
        #                     cur_string = cur_string + num2LetterDict[int(digits[m])][indexTracker[m]]
        #                 result.append(cur_string)
        #                 indexTracker[k] = indexTracker[k] + 1
        #             indexTracker[k] = 0
        #             k = k - 1
        #         indexTracker[j] = indexTracker[j] + 1
        #     indexTracker[j] = 0
        #     j = j -1
        #     if j==0:
        #         indexTracker[j]= indexTracker[j] + 1
        #
        #
        # return result
        # Solution 1: Accepted Leetcode Solution
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
print obj.letterCombinations("324567")





