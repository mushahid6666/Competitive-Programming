__author__ = 'mushahidalam'
import string
import _List
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        length = len(A)
        if length==1:
            return A[0]
        ele = 0
        small = 9999
        for i in range(0,length):
            temp= len(A[i])
            if temp < small:
                small = temp
                ele = i
        # print(small)
        # print(A[ele])
        i=0
        longpre = A[ele][0]
        while i<small:
            for k in range(0,length):
                if longpre[i] == A[k][i]:
                    continue
                else:
                    # print(longpre)
                    return longpre[:-1]
            i=i+1
            if i<small:
                longpre = longpre+A[ele][i]
        return longpre





A = Solution()
B = ["aaa",
     "aaaaaaaa",
     "aaaaaaaaaaa",
]
print A.longestCommonPrefix(B)
