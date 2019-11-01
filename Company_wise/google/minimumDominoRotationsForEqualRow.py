"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.



Example 1:



Input: A = [2,1,2,4,2,2], B =
           [3,3,3,3,3,2]
           [1,2]
           [2,1]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [2,2,2,2,3], B =
           [1,6,5,3,2]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""
import collections, sys

class Solution(object):

    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        domino_tile_tracker_A = collections.defaultdict(list)
        domino_tile_tracker_B = collections.defaultdict(list)
        for i in range(1,7):
            domino_tile_tracker_A[i] = [0,0]
            domino_tile_tracker_B[i] = [0,0]

        for i in range(len(A)):

            # Update A[i]
            domino_tile_tracker_A[A[i]][0] +=1

            if A[i] != B[i]:
                domino_tile_tracker_A[B[i]][0] += 1
                domino_tile_tracker_A[B[i]][1] += 1

            #Update B[i]
            domino_tile_tracker_B[B[i]][0] += 1

            if A[i]!= B[i]:
                domino_tile_tracker_B[A[i]][0] += 1
                domino_tile_tracker_B[A[i]][1] += 1

        same_tile_achievable = False
        min_rotations = sys.maxint
        for key in domino_tile_tracker_A.keys():
            if domino_tile_tracker_A[key][0] == len(A):
                same_tile_achievable = True
                min_rotations = min(min_rotations, domino_tile_tracker_A[key][1])

        for key in domino_tile_tracker_B.keys():
            if domino_tile_tracker_B[key][0] == len(B):
                same_tile_achievable = True
                min_rotations = min(min_rotations, domino_tile_tracker_B[key][1])

        if same_tile_achievable == False:
            return -1
        else:
            return min_rotations

obj = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print obj.minDominoRotations(A, B)
A = [1,2,1]
B = [2,1,2]
print obj.minDominoRotations(A, B)
