"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        maxHtLeft = [0] * n
        maxHtRight= [0] * n
        curMaxleft = 0
        for i in range(len(height)):
            curMaxleft = max(height[i], curMaxleft)
            maxHtLeft[i] = curMaxleft
        curMaxRight = 0
        for i in range(len(height)-1, -1 , -1):
            curMaxRight = max(height[i], curMaxRight)
            maxHtRight[i] = curMaxRight
        rainWaterTrapped = 0
        for i in range(len(height)):
            curWaterTrapped = min(maxHtLeft[i], maxHtRight[i])  - height[i]
            if curWaterTrapped > 0:
                rainWaterTrapped += curWaterTrapped
        return rainWaterTrapped


obj = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print obj.trap(heights)
