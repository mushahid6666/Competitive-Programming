__author__ = 'mushahidalam'


class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        n = A.bit_length()
        j = 1
        count = 0;
        for i in range(n):
            k = A & j;
            if k == 1:
                count += 1
            A = A >> 1
        return count


obj = Solution()
print obj.numSetBits(4)
