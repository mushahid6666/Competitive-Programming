import sys
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        

matrix = [
   [ 1,  5,  8, 9],
   [10, 15, 19, 21],
   [13, 16, 20, 22],
   [17, 18, 21, 50],
]
k = 8
obj = Solution()
print obj.kthSmallest(matrix, k)
