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
        intervals.sort(self.compare)
        index = 0
        for i in range(0,len(intervals)):
            if index!=0 and intervals[index-1].start <= intervals[i].end:
                intervals[index-1].start,/423

A = Solution()
B = Interval(1,3)
C = Interval(2,6)
D = Interval(8,10)
E = Interval(15,18)
F = Interval(1,6)
G = Interval(8,10)
H = Interval(15,18)
listinterval = [B,C,D,E,F,G,H]
A.merge(listinterval)

