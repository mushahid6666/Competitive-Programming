__author__ = 'mushahidalam'


class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        if n == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
        start = 0
        end = 1
        cur_petrol = gas[0] - cost[0]
        while end != start or cur_petrol < 0:
            while cur_petrol < 0 and start != end:
                cur_petrol -= gas[start] - cost[start]
                start = (start + 1) % n
                if start == 0:
                    return -1
            cur_petrol += gas[end] - cost[end]
            end = (end + 1) % n
        return start


obj = Solution()
gas = [2]
cost = [2]
print obj.canCompleteCircuit(gas, cost)
