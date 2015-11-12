from __future__ import division
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A = A.lstrip('0')
        B = B.lstrip('0')
        if A==B:
            return 1
        str1 = A.split('.')
        str2 = B.split('.')
        len1 = len(str1)
        len2 = len(str2)
        # print(len1)
        # print(len2)
        if len1==1:
            # print(str2[len2-1])
            if str2[len2-1] == '0':
                return 0

        if len2==1:
            # print(str1[len1-1])
            if str1[len1-1] == '0':
                return 0
        # print(str1[0])
        # print(str2[0])
        # print(float(str1[0]) > float(str2[0]))
        if float(str1[0]) > float(str2[0]):
            return 1
        if float(str1[0]) < float(str2[0]):
            return -1
        if len2 < len1:
            length = len2
        else:
            length = len1
        for i in range(1,length):
            if float(str1[i]) > float(str2[i]):
                return 1
        return -1
A = Solution()
B = "01"
C = "1"
print A.compareVersion(B,C)