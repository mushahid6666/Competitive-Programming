__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        hashDict = dict()
        n = len(A)
        for i in range(n):
            if A[i] in hashDict:
                return [hashDict[A[i]]+1,i+1]
            elif B-A[i] not in hashDict:
                hashDict[B-A[i]]=i
        return []

obj = Solution()
k = (2,3,4,5)
print obj.twoSum(k,90)
