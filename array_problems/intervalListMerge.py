class Solution(object):
    def compare(self, interval1, interval2):
        if interval1[0] > interval2[0]:
            return 1
        elif interval1[0] < interval2[0]:
            return -1
        else:
            return 0


    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return []
        A.sort(cmp = self.compare)
        B.sort(cmp = self.compare)
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            # [1,10]
            # [5,15]
            # [5,15]
            # [1,10]
            # B = [13,23] A = [8,12]
            # A = [1,13] , B = [13,23]                       A[13,23] B[1,13]
            if (A[i][1] >= B[j][0] and B[j][1]>= A[i][1]) or (B[j][1] >= A[i][0] and A[i][1]>= B[j][1]):
                #find the intersection
                # case 1
                # A = [1,10] B = [2,12]
                # output [2,10]
                # A = [1,10] B = [1,10]
                # output [1,10]
                if A[i][0] <= B[j][0] and A[i][1] <= B[j][1]:
                    result.append([B[j][0], A[i][1]])

                # case 2
                # A = [1,10] B = [2,5]
                # output = [2,5]
                # A = [1,12] B = [5,10]
                elif A[i][0] <= B[j][0] and A[i][1] >= B[j][1]:
                    result.append([B[j]])
                # case 3
                # A = [3,10] B = [1,5]
                #output = [3,5]
                elif A[i][0] > B[j][0] and A[i][1] >= B[j][1]:
                    result.append([A[i][0], B[j][1]])
                elif A[i][0] > B[j][0] and A[i][1] < B[j][1]:
                    result.append([A[i][0], A[i][1]])
            # A[9,20]
            # B[11,12][14,15]
            # A[[4, 6], [7, 8], [10, 17]]
            # B[[5, 10]]
            if (A[i][0] >= B[j][0] and B[j][1] < A[i][1]):
                j = j + 1
            else:
                i = i + 1
        return result


objSolution = Solution()
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
#Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# A = [[3,10]]
# B = [[5,10]]
#Output [5,10]
# A = [[8,15]]
# B = [[2,6],[8,10],[12,20]]
#[[8,10],[12,15]]
# A = [[4,6],[7,8],[10,17]]
# B = [[5,10]]
#Output : [[5,6],[7,8],[10,10]]
print objSolution.intervalIntersection(A,B)