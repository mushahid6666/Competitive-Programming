import Math
class Solution(object):

    def euc_distance(self, point1, point2):
        return Math.sqrt(Math.pow((point1[0] - point2[0]), 2) + Math.pow((point1[1] - point2[1]), 2))

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if K ==0 or len(points) < 1:
            return []
        if len(points) == 1 and K == 1:
            return []
        distance_dict = dict()
        for given_point in points:
            euc_distance = self.euc_distance(given_point, [0,0])
            if euc_distance in distance_dict:
                distance_dict[euc_distance].append(given_point)
            else:
                distance_dict[euc_distance] = [given_point]
        euc_distance_list =  distance_dict.keys()
        euc_distance_list.sort()
        # print euc_distance_list
        i= 0
        result = []
        while i < K:
            points = distance_dict[euc_distance_list[i]]
            while len(points) > 0:
                result.append(points.pop())
                i+=1
        return result




obj = Solution()
points = [[1,3],[-2,2]]
K = 1
print obj.kClosest(points,K)

points = [[3,3],[5,-1],[-2,4]]
K = 2
print obj.kClosest(points,K)