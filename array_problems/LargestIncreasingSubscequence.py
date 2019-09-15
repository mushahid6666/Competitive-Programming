__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def find1(self, arr):
        table = {}
        first = 0
        last = 0
        for i in arr:
            beg = end = i
            if i in table:
                continue
            table[i] = 'EXISTED'
            if i - 1 in table:
                beg = table[i - 1]
            if i + 1 in table:
                end = table[i + 1]
            table[beg] = end
            table[end] = beg
            if end - beg > last - first:
                first = beg
                last = end
        return list(range(first, last + 1))

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = self.find1(nums)
        return len(nums)


A = Solution()
lt = [4, 2, 1, 3]
print A.longestConsecutive(lt)
