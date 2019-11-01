class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(buildings)

        if n ==0:
            return []

        if n==1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y],[x_end, 0]]

        left_skyline = self.getSkyline(buildings[:n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])

        return self.mergeSkyline(left_skyline, right_skyline)

    def mergeSkyline(self, left, right):

        def update_output(x, y):

            if not output or output[-1][0] != x:
                output.append([x,y])
            else:
                output[-1][1] = y

        def append_skyline(p, list, n, y, curr_y):
            while p < n:
                x,y = list[p]
                p+=1
                if curr_y != y:
                    update_output(x,y)
                    curr_y = y

        #Merge 2 skylines
        n_l = len(left)
        n_r = len(right)
        p_l = 0
        p_r = 0
        left_y = right_y = curr_y = 0
        output = []

        while p_l < n_l and p_r < n_r:
            point_l = left[p_l]
            point_r = right[p_r]

            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1

            max_y = max(left_y, right_y)

            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        append_skyline(p_l, left, n_l, left_y, curr_y)

        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output

solObj = Solution()
input = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print solObj.getSkyline(input)
print "[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]"

