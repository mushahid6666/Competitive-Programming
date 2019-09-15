class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        traverse_right = True
        traverse_down = False
        traverse_left = False
        traverse_up = False
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = 0
        counter = 0
        cell_value = 1
        while cell_value <= pow(n,2):
            if traverse_right:
                while j < cols - counter:
                    matrix[i][j] = cell_value
                    cell_value+=1
                    j += 1
                j-=1
                i += 1
                traverse_right = False
                traverse_down = True
            elif traverse_down:
                while i < rows - counter:
                    matrix[i][j] = cell_value
                    cell_value += 1
                    i += 1
                i-=1
                j -= 1
                traverse_down = False
                traverse_left = True
            elif traverse_left:
                while j >= counter:
                    matrix[i][j] = cell_value
                    cell_value += 1
                    j -= 1
                j+=1
                i -= 1
                traverse_left = False
                traverse_up = True
            elif traverse_up:
                while i > counter:
                    matrix[i][j] = cell_value
                    cell_value += 1
                    i -= 1
                i+=1
                j+= 1
                traverse_up = False
                traverse_right = True
                counter += 1
        return matrix


obj = Solution()
n  =4
print obj.generateMatrix(n)