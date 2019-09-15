class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        traverse_right = True
        traverse_down = False
        traverse_left = False
        traverse_up = False
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = 0
        counter = 0
        while len(result) != (rows * cols):
            if traverse_right:
                while j < cols - counter:
                    result.append(matrix[i][j])
                    j += 1
                j-=1
                i += 1
                traverse_right = False
                traverse_down = True
            elif traverse_down:
                while i < rows - counter:
                    result.append(matrix[i][j])
                    i += 1
                i-=1
                j -= 1
                traverse_down = False
                traverse_left = True
            elif traverse_left:
                while j >= counter:
                    result.append(matrix[i][j])
                    j -= 1
                j+=1
                i -= 1
                traverse_left = False
                traverse_up = True
            elif traverse_up:
                while i > counter:
                    result.append(matrix[i][j])
                    i -= 1
                i+=1
                j+= 1
                traverse_up = False
                traverse_right = True
                counter += 1
        return result


obj = Solution()
matrix =[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
matrix = [[3,2],
          [4,5]]
print obj.spiralOrder(matrix)