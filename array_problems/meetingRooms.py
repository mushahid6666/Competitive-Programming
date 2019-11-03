class Solution(object):
    def compare(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] < b[0]:
            return 1
        else:
            return 0

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return True
        intervals.sort(self.compare)
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

obj = Solution()
meetings =[[0,30],[5,10],[15,20]]
print obj.canAttendMeetings(meetings)
meetings = [[7,10],[2,4]]
print obj.canAttendMeetings(meetings)