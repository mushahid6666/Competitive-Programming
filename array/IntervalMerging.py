__author__ = 'mushahidalam'
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def compare(self,A,B):
        if A.start < B.start:
            return -1
        elif A.start < B.start:
            return 1
        else:
            return 0

    def merge(self, intervals):
        if len(intervals) < 1:
            return intervals
        intervals.sort(self.compare)
        reslist = []
        index = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if prev.end >= current.start:
                temp = Interval(prev.start, max(prev.end, current.end))
                prev = temp
            else:
                reslist.append(prev)
                prev = current
            pass
        reslist.append(prev)
        pass

A = Solution()
B = Interval(1, 10)
C = Interval(2, 9)
D = Interval(3, 8)
E = Interval(4, 7)
F = Interval(5, 6)
G = Interval(6, 6)
listinterval = [B, C, D, E, F, G]
A.merge(listinterval)
pass
