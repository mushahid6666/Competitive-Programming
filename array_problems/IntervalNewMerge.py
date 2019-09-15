__author__ = 'mushahidalam'


class Solution(object):
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

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        return self.merge(intervals)

solutionObj = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
# Output: [[1,5],[6,9]]
print solutionObj.insert(intervals, newInterval)
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
print solutionObj.insert(intervals, newInterval)
# # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
#
# class Solution:
#     # @param intervals, a list of Intervals
#     # @param new_interval, a Interval
#     # @return a list of Interval
#     def insert(self, intlist, new_interval):
#         if len(intlist) < 1:
#             reslist = [new_interval]
#             return reslist
#         for i in range(0, len(intlist)):
#             if intlist[i].start >= new_interval.start:
#                 intlist.insert(i, new_interval)
#                 break
#         if i == len(intlist) - 1:
#             reslist = []
#             for i in range(0, len(intlist)):
#                 reslist.append(intlist[i])
#             reslist.append(new_interval)
#             return reslist
#         reslist = []
#         index = 0
#         prev = intlist[0]
#         for i in range(1, len(intlist)):
#             current = intlist[i]
#             if prev.end >= current.start:
#                 temp = Interval(prev.start, max(prev.end, current.end))
#                 prev = temp
#             else:
#                 reslist.append(prev)
#                 prev = current
#             pass
#         reslist.append(prev)
#         pass
#
#
# A = Solution()
# B = Interval(1, 2)
# C = Interval(3, 6)
# newInt = Interval(8, 10)
# listinterval = [B, C]
# A.insert(listinterval, newInt)
# pass
