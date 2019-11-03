#Attempt2 Leetcode optimal solution
import heapq
class Solution(object):
    def compare(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(self.compare)
        rooms = [intervals[0][1]]
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if cur_interval[0] >= rooms[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, cur_interval[1])
            else:
                rooms.append(cur_interval[1])
                heapq.heapify(rooms)
        return len(rooms)


class Solution5(object):
    def compare(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1

        intervals.sort(self.compare)
        rooms = [intervals[0]]
        total_rooms = 1
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            allocated = False
            for j in range(len(rooms)):
                if rooms[j][1] < cur_interval[1] and cur_interval[0] >= rooms[j][1]:
                    rooms[j] = cur_interval
                    allocated = True
                    break
            if not allocated:
                rooms.append(cur_interval)
                total_rooms +=1
        return total_rooms










obj = Solution()
intervals = [[1,13], [13,15]]
print obj.minMeetingRooms(intervals)

intervals = [[0, 30],[5, 10],[9, 20]]
print obj.minMeetingRooms(intervals)

intervals = [[0, 30],[5, 10],[15, 20]]
print obj.minMeetingRooms(intervals)

intervals = [[7,10],[2,4]]
print obj.minMeetingRooms(intervals)

intervals = [[7,10]]
print obj.minMeetingRooms(intervals)

class Solution1(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        start_intervals = []
        for cur_int in intervals:
            start_intervals.append(cur_int[0])

        start_intervals.sort()
        end_intervals = []
        for cur_int in intervals:
            end_intervals.append(cur_int[1])
        end_intervals.sort()
        i = 0
        j = 0

        meeting_room_count = 0
        while i < len(start_intervals) :
            if start_intervals[i] >= end_intervals[j]:
                meeting_room_count -= 1
                j+=1
            else:
                meeting_room_count += 1
                i+=1
        return meeting_room_count

#Previous attempted passed leetcode solution
class Solution2(object):
    def compare(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 0
        else:
            return 0
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(self.compare)
        room_count = 1
        room_id = 1
        dict_rooms = dict()
        dict_rooms[1] = intervals[0][1]
        for i in range( len(intervals ) -1):
            if intervals[i][1] > intervals[ i +1][0]:
                values = dict_rooms.values()
                values.sort()
                if intervals[ i +1][0] >= values[0]:
                    for key in dict_rooms.keys():
                        if dict_rooms[key] <= intervals[i+1][0]:
                            dict_rooms[key] = intervals[i +1][1]
                            break
                else:
                    # print "no empty room"
                    room_count += 1
                    room_id += 1
                    dict_rooms[room_id] = intervals[ i +1][1]
            else:
                if len(dict_rooms.keys()) > 1:
                    current_interval_used = 0
                    for key in dict_rooms.keys():
                        if dict_rooms[key] <= intervals[i][1]:
                            if current_interval_used == 0:
                                dict_rooms[key] = intervals[i+1][1]
                                current_interval_used = 1
                            else:
                                dict_rooms[key] = -1
                            # break
                else:
                    for element in dict_rooms:
                        dict_rooms[element] = intervals[i+1][1]
        return room_count