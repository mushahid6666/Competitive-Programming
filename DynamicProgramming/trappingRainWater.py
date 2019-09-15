class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Leetcode: DP Solution
        if len(height) == 0 :
            return 0
        maxLeft = []
        maxRight = []
        currentMaxLeft = 0
        for i in range(len(height)):
            currentMaxLeft = max(currentMaxLeft, height[i])
            maxLeft.append(currentMaxLeft)
        currentMaxRight = 0
        for i in range(len(height)-1, -1, -1):
            currentMaxRight = max(currentMaxRight, height[i])
            maxRight.insert(0, currentMaxRight)

        rainWaterTrapped = 0
        for i in range(len(height)):
            rainWaterTrapped += min(maxLeft[i], maxRight[i]) - height[i]

        return (rainWaterTrapped)



solObject = Solution()
Input= [0,1,0,2,1,0,1,3,2,1,2,1]
result = solObject.trap(Input)
print "Expected: 6 Returned result: ", result