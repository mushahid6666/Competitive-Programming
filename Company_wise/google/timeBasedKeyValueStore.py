'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"],
inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2,
then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"],
 inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]


Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
'''
import collections
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_val_dict = collections.defaultdict(list)
        self.timestamp_index = 0
        self.value_index = 1

    def compare(self, a, b):
        if a[self.timestamp_index] > b[self.timestamp_index]:
            return -1
        else:
            return 1

    def insert_value(self, key, value_timestamp_pair):
        low = 0
        high = len(self.key_val_dict[key])
        while (low < high):
            mid = (low+high)/2
            if self.key_val_dict[key][mid][self.timestamp_index] > value_timestamp_pair[self.timestamp_index]:
                low = mid +1
            else:
                high = mid -1
        self.key_val_dict[key].insert(low, value_timestamp_pair)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.key_val_dict.keys():
            self.insert_value(key, [timestamp, value])
            # self.key_val_dict[key].append([timestamp, value])
            # self.key_val_dict[key].sort(self.compare)
        else:
            self.key_val_dict[key] = [[timestamp, value]]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.key_val_dict:
            return None
        value_timestamp_list = self.key_val_dict[key]
        if timestamp < value_timestamp_list[-1][0]:
            return ""

        low = 0
        high = len(value_timestamp_list) - 1
        while low <= high:
            mid = low+high/2
            if value_timestamp_list[mid][self.timestamp_index] <= timestamp:
                i = mid
                while i-1 >=0 and value_timestamp_list[i-1][self.timestamp_index] <= timestamp:
                    i-=1
                return value_timestamp_list[i][self.value_index]
            elif value_timestamp_list[mid][self.timestamp_index] > timestamp:
                low = mid + 1
            else:
                high = mid-1

        # for i in range(len(value_timestamp_list)):
        #     if value_timestamp_list[i][self.timestamp_index] <= timestamp:
        #         return value_timestamp_list[i][self.value_index]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
#Test Case 2:
obj.set("love","high",10)
obj.set("love","low",20)
print obj.get("love",5)
print obj.get("love",10)
print obj.get("love",15)
print obj.get("love",20)
print obj.get("love",25)


#Test Case1
obj.set("foo","bar",1)
print obj.get("foo",1)
print obj.get("foo",3)
obj.set("foo","bar2",4)
print obj.get("foo",4)
print obj.get("foo",5)
