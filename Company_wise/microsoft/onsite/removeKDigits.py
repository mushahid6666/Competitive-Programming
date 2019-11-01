class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        index = 0
        rem_digits = 0
        while rem_digits != k and index +1 < len(num):
            if num[index] > num[index +1]:
                num = "".join(num[:index] + num[index +1 :] )
                rem_digits += 1
                if index >0:
                    index -=1
            else:
                index += 1


        if rem_digits !=k:
            digits_to_del = k-rem_digits
            num = num[:-digits_to_del]
        while len(num) > 1 and num[0] == '0':
            num= num[1 :]
        return num

obj = Solution()
number = "5132219"
k = 2
print obj.removeKdigits(number, k) #"12219"
number = "1432219"
k = 3
print obj.removeKdigits(number, k)
number = "10200"
k = 2
print obj.removeKdigits(number, k)
number = "10"
k = 2
print obj.removeKdigits(number, k)
number = "1133"
k = 2
print obj.removeKdigits(number, k)

number = "12345264"
k = 4
print obj.removeKdigits(number, k)
number = "34521"
k = 4
print obj.removeKdigits(number, k)
number = "115"
k = 1
print obj.removeKdigits(number, k)
number = "1173"
k = 2
print obj.removeKdigits(number, k)
