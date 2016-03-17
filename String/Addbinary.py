__author__ = 'mushahidalam'


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        a = A
        b = B
        carry = 0
        resultStr = ''
        len1 = len(a)
        len2 = len(b)
        i = len1 - 1
        j = len2 - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            resultStr += str((carry % 2))
            carry = carry / 2
            i -= 1
            j -= 1
        return resultStr.reverse()



A = "1"
B = "111"
#   1110000000010110111010101010000
# returned-1001021121111001212201110
# expected-1001110001111010101001110
obj = Solution()
print obj.addBinary(A, B)
