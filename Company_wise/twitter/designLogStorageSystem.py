'''You are given several logs that each log contains a unique id and timestamp.
 Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second,
 for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within
the range from start to end. Start and end all have the same format as timestamp. However, granularity means the
 time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", i
 t means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return
all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.'''
import datetime, calendar
class LogSystem(object):

    def __init__(self):
        self.logArrSortTZ= list()

    def addLogToList(self, new_log):

        for i in range(len(self.logArrSortTZ)):
            if new_log[1] < self.logArrSortTZ[i][1]:
                self.logArrSortTZ.insert(i, new_log)
                return
        self.logArrSortTZ.append(new_log)

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        timestamp = timestamp.split(":")
        new_log = [id, datetime.datetime(int(timestamp[0]),int(timestamp[1]),int(timestamp[2]),int(timestamp[3]),int(timestamp[4]), int(timestamp[5]))]
        self.addLogToList(new_log)

    def get_id_list(self, start, end):
        result = []
        for i in range(len(self.logArrSortTZ)):
            if self.logArrSortTZ[i][1] >= start and self.logArrSortTZ[i][1] <= end:
                result.append(self.logArrSortTZ[i][0])
        return result
    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        s = s.split(":")
        e = e.split(":")
        if gra == "Year":
            start = datetime.datetime(int(s[0]), 1, 1, 0, 0, 0)
            end = datetime.datetime(int(e[0]), 12, 31, 23, 59, 59)
            return self.get_id_list(start, end)
        elif gra == "Month":

            start = datetime.datetime(int(s[0]), int(s[1]), 1, 0, 0, 0)
            month_range = calendar.monthrange(int(e[0]), int(e[1]))
            end = datetime.datetime(int(e[0]), int(e[1]), month_range[1], 23, 59, 59)
            return self.get_id_list(start, end)
        elif gra == "Day":

            start = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), 0, 0, 0)
            end = datetime.datetime(int(e[0]), int(e[1]), int(e[2]), 23, 59, 59)
            return self.get_id_list(start, end)
        elif gra == "Hour":
            start = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), 0, 0)
            end = datetime.datetime(int(e[0]), int(e[1]), int(e[2]), int(e[3]), 59, 59)
            return self.get_id_list(start, end)
        elif gra == "Minute":
            start = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), 0)
            end = datetime.datetime(int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]), 59)
            return self.get_id_list(start, end)
        else:
            start = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5]))
            end = datetime.datetime(int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]), int(e[5]))
            return self.get_id_list(start, end)


# Your LogSystem object will be instantiated and called as such:
obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
print obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")
print obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour")
print obj.retrieve("2017:01:01:23:00:00","2017:01:01:23:59:59","Second")