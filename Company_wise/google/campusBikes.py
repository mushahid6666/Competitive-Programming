import sys, collections
import heapq
class Solution(object):
    def computeManhatDistance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """

        distances = []
        for i in range(len(workers)):
            cur_worker_co_ord = workers[i]
            distances.append([])
            for j in range(len(bikes)):
                cur_bike_distance = self.computeManhatDistance(cur_worker_co_ord, bikes[j])
                distances[-1].append((cur_bike_distance, i, j))
            distances[-1].sort(reverse=True)

        result = [None] * len(workers)
        used_bikes = set()
        priorityQueue = [distances[i].pop()  for i in range(len(workers))]
        heapq.heapify(priorityQueue)

        while len(used_bikes) < len(workers):
            disance, worker, bike = heapq.heappop(priorityQueue)
            if bike not in used_bikes:
                used_bikes.add(bike)
                result[worker] = bike
            else:
                heapq.heappush(priorityQueue, distances[worker].pop())
        return result


obj = Solution()
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
print obj.assignBikes(workers, bikes)
