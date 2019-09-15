__author__ = 'mushahidalam'
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def compare(self, interval1, interval2):
        if interval1[0] > interval2[0]:
            return 1
        elif interval1[0] < interval2[0]:
            return -1
        else:
            return 0

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1 or len(intervals) == 0:
            return intervals
        # print intervals
        intervals.sort(cmp = self.compare)
        result = [intervals[0]]
        i = len(result) - 1
        j = 1
        while j < len(intervals):
            if result[i][1] >= intervals[j][0]:
                tempInterval = [min(result[i][0],intervals[j][0]), max(result[i][1], intervals[j][1]) ]
                j = j + 1
                while j < len(intervals) and tempInterval[1] > intervals[j][0] :
                    tempInterval = [min(tempInterval[0], intervals[j][0]), max(tempInterval[1], intervals[j][1])]
                    j = j+1
                result.pop(-1)
                result.append(tempInterval)
                i = len(result) - 1
            else:
                result.append(intervals[j])
                i = len(result) - 1
                j = j + 1
        return result

solutionObj = Solution()
# intervals = [[8,10], [9,18], [18,25], [1,3], [2,6]]
intervals = [[1,4],[2,3]]
print solutionObj.merge(intervals)
    # @param intervals, a list of Intervals
    # @return a list of Interval
    # def compare(self,A,B):
    #     if A.start < B.start:
    #         return -1
    #     elif A.start < B.start:
    #         return 1
    #     else:
    #         return 0
    #
    # def merge(self, intervals):
    #     if len(intervals) < 1:
    #         return intervals
    #     intervals.sort(self.compare)
    #     reslist = []
    #     index = 0
    #     prev = intervals[0]
    #     for i in range(1, len(intervals)):
    #         current = intervals[i]
    #         if prev.end >= current.start:
    #             temp = Interval(prev.start, max(prev.end, current.end))
    #             prev = temp
    #         else:
    #             reslist.append(prev)
    #             prev = current
    #         pass
    #     reslist.append(prev)
    #     pass
#
# A = Solution()
# B = Interval(1, 10)
# C = Interval(2, 9)
# D = Interval(3, 8)
# E = Interval(4, 7)
# F = Interval(5, 6)
# G = Interval(6, 6)
# listinterval = [B, C, D, E, F, G]
# A.merge(listinterval)
# pass
