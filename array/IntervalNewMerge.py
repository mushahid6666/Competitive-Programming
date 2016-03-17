__author__ = 'mushahidalam'


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intlist, new_interval):
        if len(intlist) < 1:
            reslist = [new_interval]
            return reslist
        for i in range(0, len(intlist)):
            if intlist[i].start >= new_interval.start:
                intlist.insert(i, new_interval)
                break
        if i == len(intlist) - 1:
            reslist = []
            for i in range(0, len(intlist)):
                reslist.append(intlist[i])
            reslist.append(new_interval)
            return reslist
        reslist = []
        index = 0
        prev = intlist[0]
        for i in range(1, len(intlist)):
            current = intlist[i]
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
B = Interval(1, 2)
C = Interval(3, 6)
newInt = Interval(8, 10)
listinterval = [B, C]
A.insert(listinterval, newInt)
pass
