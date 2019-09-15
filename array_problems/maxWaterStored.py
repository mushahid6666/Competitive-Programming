class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Attempt  2

        len_array = len(height)
        if len_array == 0:
            return 0
        if len_array == 2:
            return min(height[0], height[1])

        left_ptr = 0
        right_ptr = len_array - 1
        max_area = 0
        cur_max_area = 0
        while left_ptr != right_ptr:
            cur_max_area = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            if cur_max_area > max_area:
                max_area = cur_max_area
            if height[left_ptr] < height[right_ptr]:
                left_ptr = left_ptr + 1
            else:
                right_ptr = right_ptr - 1
        return max_area


        #Accepted Solution 1
        # n = len(height)
        # i = 0
        # j = n - 1
        # max_area = 0
        # while i < j:
        #     max_area = max(max_area, min(height[i], height[j]) * (j - i))
        #     if height[i] < height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return max_area

obj = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print height, " result: ", obj.maxArea(height)
height = [1, 8]
print height, " result: ", obj.maxArea(height)
height = [1, 8, 7]
print height, " result: ", obj.maxArea(height)
height = [1, 8, 6, 5, 4, 3, 2, 7]
print height, " result: ", obj.maxArea(height)
height = [100, 8, 3, 10]
print height, " result: ", obj.maxArea(height)
height = [10, 1, 200, 5, 4, 6, 500]
print height, " result: ", obj.maxArea(height)
height = [1, 5, 10, 0]
print height, " result: ", obj.maxArea(height)
