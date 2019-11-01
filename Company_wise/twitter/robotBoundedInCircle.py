"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation:
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation:
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
"""

import copy
class Solution(object):
    def inc_length(self, cur_direction, east, west, north, south):
        if cur_direction == "E":
            east += 1
        elif cur_direction == "W":
            west +=1
        elif cur_direction == "N":
            north +=1
        elif cur_direction == "S":
            south +=1
        return east, west, north, south

    def update_direction(self, cur_dir, new_dir):
        if cur_dir == "E":
            if new_dir == "L":
                return "N"
            elif new_dir == "R":
                return "S"
        elif cur_dir == "W":
            if new_dir == "L":
                return "S"
            elif new_dir == "R":
                return "N"
        elif cur_dir == "N":
            if new_dir == "L":
                return "W"
            elif new_dir == "R":
                return "E"
        elif cur_dir == "S":
            if new_dir == "L":
                return "E"
            elif new_dir == "R":
                return "W"

    def travelDirectionLength(self, instructions):
        instructions = instructions + instructions
        cur_direction = "E"
        east_length = 0
        west_length = 0
        north_length = 0
        south_length = 0
        for cur_instr in instructions:
            if  cur_instr == "G":
                east_length, west_length, north_length, south_length = self.inc_length(cur_direction, east_length, west_length, north_length, south_length)
            elif cur_instr == "L" or cur_instr == "R":
                cur_direction = self.update_direction(copy.copy(cur_direction), cur_instr)
        if east_length != west_length or north_length != south_length:
            return False
        return True


    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        if not self.travelDirectionLength(instructions):
            second_try = self.travelDirectionLength(instructions + instructions + instructions + instructions)
            if not second_try:
                return False
        return True

obj = Solution()
instructions = "GGLLGG"
print obj.isRobotBounded(instructions)
instructions = "GG"
print obj.isRobotBounded(instructions)
instructions = "GGLL"
print obj.isRobotBounded(instructions)
instructions = "GGRR"
print obj.isRobotBounded(instructions)
instructions = "GGLGGLLGGRG"
instructions = "GGGGGGL"
print obj.isRobotBounded(instructions)