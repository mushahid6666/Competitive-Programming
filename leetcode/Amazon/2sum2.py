class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(0, len(numbers)):
            if numbers[i] in dict:
                dict[numbers[i]].append(i)
            dict[numbers[i]] = [i]
        for i in range(0, len(numbers)):
            num1 = numbers[i]
            num2 = target - num1
            if num2 in dict:
                if len(dict[num2]) > 1:
                    for k in dict[num2]:
                        if k != i:
                            return [i + 1, k + 1]
                else:
                    if i != dict[num2][0]:
                        return [i + 1, dict[num2][0] + 1]


obj = Solution()
obj.twoSum([2, 7, 11, 15], 9)
