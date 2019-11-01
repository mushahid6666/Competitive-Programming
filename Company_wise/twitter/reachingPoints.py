'''A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence
of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].'''
class Solution(object):
    def computeReachableRecursive(self, sx, sy, tx, ty):

        if sx > tx or sy > ty:
            return

        if self.reachable == True:
            return

        if sx == tx and sy==ty:
            self.reachable = True
            return

        new_pair = tuple([sx, sy])
        if new_pair in self.alreadyVisitedPoints:
            return

        self.computeReachableRecursive(sx + sy, sy, tx, ty)

        self.computeReachableRecursive(sx, sx + sy, tx, ty)

    def backTracking(self, sx, sy, tx, ty):
        while tx>=sx and ty>=sy:
            if tx==sx and ty==sy:
                return True

            if tx > ty:
                tx = tx-ty
            else:
                ty = ty-tx

        return False


    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        self.reachable = False
        self.alreadyVisitedPoints = set()
        #Recursive Solution
        # self.computeReachableRecursive(sx, sy, tx, ty)
        # return self.reachable
        #BackTrackking Solution
        return self.backTracking(sx, sy, tx, ty)


obj = Solution()
sx = 1
sy = 1
tx = 3
ty = 5
print obj.reachingPoints(sx, sy, tx, ty)
sx = 35
sy = 13
tx = 455955547
ty = 420098884
print obj.reachingPoints(sx, sy, tx, ty)