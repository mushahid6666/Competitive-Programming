class Solution(object):
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
                # print "no overlap, Mark previous room empty"

                if len(dict_rooms.keys()) > 1:
                    current_interval_used = 0
                    for key in dict_rooms.keys():
                        if dict_rooms[key] <= intervals[i][1]:
                            # print "make one for current interval"
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
# [[1,15],[1,3],[5,7],[6,9],[10,12],[11,13]]
# 1,1,1,
# ROOM-[15, -1]
# NlongN + n* k

obj = Solution()
intervals = [[2,5],[3,5],[7,8]]
print obj.minMeetingRooms(intervals), "Expected 2"
intervals = [[2,5],[6,7],[8,9]]
print obj.minMeetingRooms(intervals), "Expected 1"
intervals = [[2,5],[3,5],[1,8]]
print obj.minMeetingRooms(intervals), "Expected 3"
intervals = [[1,5],[5,8],[8,10]]
print obj.minMeetingRooms(intervals), "Expected 1"
intervals = [[1,10],[2,5],[4,8],[10,12]]
print obj.minMeetingRooms(intervals), "Expected 3"
intervals = [[1,10],[1,2],[2,3],[3,4],[4,5],[5,6]]
print obj.minMeetingRooms(intervals), "Expected 2"
intervals = [[1,3],[5,7],[6,9],[10,12],[11,13]]
print obj.minMeetingRooms(intervals), "Expected 2"
intervals = [[1,15],[1,3],[5,7],[6,9],[10,12],[11,13]]
print obj.minMeetingRooms(intervals), "Expected 3"
intervals = [[1 ,15] ,[1 ,3] ,[1 ,3] ,[1 ,3] ,[5 ,7] ,[6 ,9] ,[10 ,12] ,[11 ,13]]
print obj.minMeetingRooms(intervals), "Expected 4"
intervals = [[4,9],[4,17],[9,10]]
print obj.minMeetingRooms(intervals), "Expected 2"
intervals = [[1,5],[8,9],[8,9]]
print obj.minMeetingRooms(intervals), "Expected 2"
intervals = [[4,18],[1,35],[12,45],[25,46],[22,27]]
print obj.minMeetingRooms(intervals), "Expected 4"

# ---------------
# ---
# ---
# ---
# .   ---
# .    ---
# .       ---
# .        ---

#
# Your previous Plain Text content is preserved below:
#
# // You are given a list of interview times (start, end), tell me the minimum number of rooms you need to accommodate the interviews.
