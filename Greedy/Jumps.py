__author__ = 'mushahidalam'


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        edge = 0
        maxEdge = 0
        for i in range(len(nums)):
            if i > edge:
                edge = maxEdge
                res += 1
            maxEdge = max(maxEdge, i + nums[i])
        return res


obj = Solution()
arr = [3, 1, 2, 3, 4, 1, 2, 1, 0, 3]
print obj.jump(arr)
