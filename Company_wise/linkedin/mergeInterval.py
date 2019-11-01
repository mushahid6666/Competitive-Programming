class Solution(object):
    def compare(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <=0:
            return intervals
        intervals.sort(self.compare)
        result = []
        i = 0
        j = i + 1
        while i < len(intervals) and j < len(intervals):
            cur_interval = intervals[i]
            new_interval = intervals[j]
            if cur_interval[1] > new_interval[0]:
                cur_interval[0] = min(cur_interval[0], new_interval[0])
                cur_interval[1] = max(cur_interval[1], new_interval[1])
                j+=1
            else:
                result.append(cur_interval)
                i=j
                j=i+1
        if i< len(intervals):
            result.append(intervals[i])
        return result





obj = Solution()
intervals = [[1,3],[2,6],[15,18],[8,10]]
intervals = [[1,3],[2,6]]
intervals = [[1,3]]
intervals = [[2,6],[15,18],[8,10]]
intervals = [[1,10],[5,20],[3,9]]
print obj.merge(intervals)
