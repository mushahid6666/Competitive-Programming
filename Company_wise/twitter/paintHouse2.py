import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        min1 = sys.maxint
        min2 = sys.maxint
        for i in range(len(costs[0])):
            if costs[0][i] <= min1:
                min2 = min1
                min1 = costs[0][i]
            elif costs[0][i] <= min2:
                min2 = costs[0][i]

        for i in range(1, len(costs)):
            cur_row_min1 = sys.maxint
            cur_row_min2 = sys.maxint
            for j in range(len(costs[0])):
                prev_row_min = min1
                if min1 == costs[i-1][j]:
                    prev_row_min = min2
                costs[i][j] += prev_row_min
                if costs[i][j] <= cur_row_min1:
                    cur_row_min2 = cur_row_min1
                    cur_row_min1 = costs[i][j]
                elif costs[i][j] <= cur_row_min2:
                    cur_row_min2 = costs[i][j]
            min1 = cur_row_min1
            min2 = cur_row_min2

        return min1



matrix = [[17,2,17]]
matrix = [[7,19,11,3,7,15,17,5,6,18,1,15,18,11],
 [13,18,18,8,13,12,11,13,4,8,2,4,5,20],
 [14,5,18,4,7,6,1,6,11,6,16,6,13,17],
 [18,17,11,3,12,4,8,6,2,7,10,9,19,3],
 [4,3,2,14,11,15,18,1,17,1,6,14,14,9],
 [9,13,15,14,5,1,1,6,11,15,16,12,10,18],
 [19,2,11,3,13,4,13,7,16,16,20,18,20,8],
 [8,19,20,9,18,13,17,1,2,4,3,20,15,9],
 [9,10,11,6,14,20,4,1,5,15,13,10,13,5],
 [13,11,9,11,9,16,3,19,1,11,6,7,12,13],
 [14,1,15,14,11,12,7,14,12,11,6,9,5,5]]
obj = Solution()
print obj.minCostII(matrix)

