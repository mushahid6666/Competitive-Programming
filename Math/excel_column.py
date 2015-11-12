__author__ = 'mushahidalam'
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        alpha = {}
        for i in range(0,27):
            key = ord('A')+i
            alpha[key] = i+1
        if len(A)==1:
            return alpha[ord(A)]
        column =1
        lt = len(A)
        if len(A) > 1:
            for i in range(0,len(A)):
                # print(A[i])
                if i == len(A)-1:
                    return column+alpha[ord(A[i])]
                if i==0:
                    column = column*alpha[ord(A[lt-i-2])]*26
                else:
                    column = column*alpha[ord(A[lt-i-2])]*27


obj = Solution()
print obj.titleToNumber('AAA')