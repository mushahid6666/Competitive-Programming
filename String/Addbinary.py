__author__ = 'mushahidalam'


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        len1 = len(A)
        len2 = len(B)
        if len1 > len2:
            carry = 0
            total = ""
            diff = len1 - len2
            for i in range(len2 - 1, -1, -1):
                temp = int(A[i + diff]) + int(B[i]) + carry
                if temp == 2:
                    total = '0' + total
                    carry = 1
                elif temp == 3:
                    total = '1' + total
                    carry = 1
                else:
                    total = str(temp) + total
                    carry = 0
            if carry == 1:
                i = len1 - len2 - 1
                while i != -1:
                    temp = int(A[i]) + carry
                    if temp == 2:
                        total = '0' + total
                        carry = 1
                    elif temp == 3:
                        total = '1' + total
                        carry = 1
                    else:
                        total = str(temp) + total
                        carry = 0
                    i -= 1
                if carry != 0:
                    total = '1' + total
            else:
                i = len1 - len2 - 1
                while i != -1:
                    total = A[i] + total
                    i -= 1
            return int(total)
        else:
            # len2(b) > len1(a)
            carry = 0
            total = ""
            diff = len2 - len1
            for i in range(len1 - 1, -1, -1):
                temp = int(A[i]) + int(B[i + diff]) + carry
                if temp == 2:
                    total = '0' + total
                    carry = 1
                elif temp == 3:
                    total = '1' + total
                    carry = 1
                else:
                    total = str(temp) + total
                    carry = 0
            if carry == 1:
                i = len2 - len1 - 1
                while i != -1:
                    temp = int(B[i]) + carry
                    if temp == 2:
                        total = '0' + total
                        carry = 1
                    elif temp == 3:
                        total = '1' + total
                        carry = 1
                    else:
                        total = str(temp) + total
                        carry = 0
                    i -= 1
                if carry != 0:
                    total = '1' + total
            else:
                i = len2 - len1 - 1
                while i != -1:
                    total = B[i] + total
                    i -= 1
            return int(total)


A = "1"
B = "111"
#   1110000000010110111010101010000
# returned-1001021121111001212201110
# expected-1001110001111010101001110
obj = Solution()
print obj.addBinary(A, B)
