__author__ = 'mushahidalam'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Attempt 2:
        int_max = pow(2,31)
        if x > int_max or x < -(int_max):
            return 0
        negativeNumber = False
        if x < 0 :
            negativeNumber = True
            x = x * -1

        input = x
        stack = []
        while input != 0:
            number = input % 10
            stack.append(number)
            input = input / 10
        result = 0
        power = 0
        base = pow(10, power)
        while len(stack) != 0:
            result = result + stack.pop(-1) * base
            power = power + 1
            base = pow(10, power)
        if negativeNumber:
            result = result * -1
        return result

        #Working Accepted Solution.
        # str2 = ''
        # str1 = str(x)
        # if x < 0:
        #     flag = 1
        #     str1 = str1[1:]
        #     str2=str2+'-'
        # lt = len(str1)
        # for i in range(0, len(str1)):
        #     str2 = str2+str1[lt-1-i]
        # if int(str2) > 2147483648 or int(str2) < -2147483648:
        #     return 0
        # return int(str2)


obj = Solution()
print(obj.reverse(123))
print(obj.reverse(9646324351))
print(obj.reverse(-9646324351))