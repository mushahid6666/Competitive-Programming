import sys, collections
import heapq
class Solution(object):
    def getManHatDistance(self, worker, bike):
        return abs((worker[0] - bike[0])) + abs((worker[1] - bike[1]))
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        distances = []
        for i in range(len(workers)):
            distances.append([])
            cur_worker = workers[i]
            for j in range(len(bikes)):
                cur_bike = bikes[j]
                cur_distance = self.getManHatDistance(cur_worker, cur_bike)
                distances[-1].append((cur_distance, i, j))
            distances[-1].sort(reverse=True)

        result = [-1] * len(workers)
        priorityQueue = [distances[i].pop() for i in range(len(workers))]
        heapq.heapify(priorityQueue)
        used_bikes = set()
        while len(used_bikes) < len(workers):
            cur_distance, worker, bike = heapq.heappop(priorityQueue)
            if bike not in used_bikes:
                used_bikes.add(bike)
                result[worker] = bike
            else:
                heapq.heappush(priorityQueue, distances[worker].pop())
        return result



class Solution1(object):
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
# workers = [[0,0],[2,1]]
# bikes = [[1,2],[3,3]]
# print obj.assignBikes(workers, bikes)
workers = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
bikes = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999]]
print obj.assignBikes(workers, bikes)
