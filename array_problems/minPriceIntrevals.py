import sys
class Solution:
    def compare(self, interval1, interval2):
        if interval1[0] > interval2[0]:
            return 1
        elif interval1[0] < interval2[0]:
            return -1
        else:
            return 0
    def minPriceInterval(self, intervals):
        if len(intervals) == 1 or len(intervals) == 0:
            return intervals
        intervals.sort(cmp=self.compare)
        start_date = sys.maxint
        end_date = -sys.maxint
        for interval in intervals:
            start_date = min(start_date, interval[0])
            end_date = max(end_date, interval[1])
        result = []
        prices = [sys.maxint for i in range(end_date+2)]
        for interval in intervals:
            j = interval[0]
            while j <= interval[1]:
                prices[j] = min(prices[j], interval[2])
                j += 1
        j = start_date
        while j <= end_date:
            start = j
            while j <= end_date and prices[j] == prices[j+1]:
                j += 1
            end = j
            result.append([start, end, prices[j]])
            j += 1
        return result


intervals = [[1, 2, 20], [3, 6, 15], [7, 12, 18], [13, 31, 22]]
#Output = (1, 2, $20), (3, 6, $15), (7, 12, $18), (13, 31, $22)
solutionObj = Solution()
print solutionObj.minPriceInterval(intervals)