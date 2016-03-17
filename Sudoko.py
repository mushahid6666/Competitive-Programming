__author__ = 'mushahidalam'


# Object for each cell
class Cell:
    def __init__(self, rw, col, val):  # Intialize with row,Column and current value , -1 if empty
        self.row = rw  # Indicate Row Number
        self.column = col  # Indicate Column Number
        self.value = val  # Indicate Value
        self.hints = [1, 2, 3, 4, 5, 6, 7, 8,
                      9]  # Indicate possible values , Intially intializaed to all possible values


cell_list = dict()  # Contains Cell obj for each cell
# Separte Grid and affecting cells in rows and columns to avoid redundency of data for each cell
lookup = dict()  # Contains all affecting cells in row and column for a given cell i
grid = dict()  # Contains all affecting cells in the grid for the given cell i


def get_hints(row, col):
    # assume row and col will be input in range 1 to 9
    if row > 9 or row < 1 or col > 9 or col < 1:
        print "ERROR: Input is not in range"
        return None
    if len(cell_list) == 0:
        print "ERROR: Call SudokuHint with valid SudokuBoard"
        return None
    index = (row - 1) * 9 + (col - 1)
    return cell_list[index].hints


def SudukoHint(arr, flag):
    global cell_list
    global lookup
    global grid
    if is_valid(arr) == False:
        return False
    rows = len(arr)
    columns = len(arr)
    cell_no = 0
    # Setup the cells in a grid
    # grid[i] will give all possible cells in the grid
    for i in range(rows):
        for j in range(columns):
            cell_list[cell_no] = Cell(i, j, arr[i][j])  # Intialze the cell object for each cell
            grid_no = ((i / 3) * 3) + (j / 3)  # Caculate the grid number
            # Add the cell to the corresponding grid
            if grid_no in grid:
                grid[grid_no].append(cell_no)
            else:
                grid[grid_no] = [cell_no]
            # ** Cell Number ranges from 0 till n*n where n is size of row
            cell_no += 1
    # Set the lookup the table
    # lookup[i] will give the cells affecting the ith cell except the once in the grid.
    cell_no = 0
    # Update the lookup table for each cell
    for i in range(rows):
        for j in range(columns):
            # Add all the affecting cells in the row to the lookup
            for k in range(9):
                affecting_cell = i * 9 + k
                grid_no = ((i / 3) * 3) + (j / 3)
                if affecting_cell not in grid[
                    grid_no]:  # if the affecting cell is not in grid then add it, Avoiding redundency
                    if cell_no in lookup:
                        lookup[cell_no].append(affecting_cell)
                    else:
                        lookup[cell_no] = [affecting_cell]
            # Add all the affecting cells in the column to the lookup
            for k in range(9):
                affecting_cell = j + k * 9
                grid_no = ((i / 3) * 3) + (j / 3)
                if affecting_cell not in grid[
                    grid_no]:  # if the affecting cell is not in grid then add it, Avoiding redundency
                    if cell_no in lookup:
                        lookup[cell_no].append(affecting_cell)
                    else:
                        lookup[cell_no] = [affecting_cell]
            cell_no += 1
    # updating the cell_obj_list for a cell
    current_cell_no = 0
    for i in range(rows):
        for j in range(columns):
            grid_no = ((i / 3) * 3) + (j / 3)
            # Remove all values which are already present in the grid for picked cell
            for cell in grid[grid_no]:
                # If the cell is not empty and the value is present in hint list of the cell
                if cell_list[cell].value != -1 and cell_list[cell].value in cell_list[current_cell_no].hints:
                    # remove the value from hint list
                    cell_list[current_cell_no].hints.remove(cell_list[cell].value)
            # Remove all values which are already present in the rows and columns for picked cell
            for cell in lookup[current_cell_no]:
                # If the cell is not empty and the value is present in hint list of the cell
                if cell_list[cell].value != -1 and cell_list[cell].value in cell_list[current_cell_no].hints:
                    # remove the value from hint list
                    cell_list[current_cell_no].hints.remove(cell_list[cell].value)
            current_cell_no += 1
    # return True

    # Uncomment the below code to see all the hints generated
    if flag == 1:
        n = len(arr)
        max = n * n
        letter = ord('A')
        i = 0
        for cell_no in range(max):
            row = letter + (cell_no / 9)
            if cell_list[cell_no].value == -1 and len(cell_list[cell_no].hints) != 0:
                print chr(row), i + 1,
                print cell_list[cell_no].hints
            i = ((i + 1) % 9)


def is_board_size_correct(arr):
    row = len(arr)
    if row != 9:
        print "ERROR: Board row size not correct!"
        return False
    for i in range(row):
        columns = len(arr[i])
        if columns != 9:
            print "ERROR: Board size not correct!"
            return False
    return True


def type_check(arr):
    if type(arr) is not list:
        print "ERROR: Input should be list of lists!"
        return False
    return True


def is_valid(arr):
    if not type_check(arr):  # Type check
        return False
    if not is_board_size_correct(arr):  # Board size check
        return False
    row = len(arr)
    columns = len(arr)
    for i in range(row):
        for j in range(columns):
            cell_value = arr[i][j]
            if cell_value != -1:  # If non empty cell then proceed
                # Checking values are not duplicate in Row and Column
                if cell_value < 1 or cell_value > 9:
                    print('ERROR: cell value', i, j, 'is not in range 1-9')
                for k in range(row):
                    if arr[i][k] == cell_value and k != j:
                        print('ERROR:', i, k, 'value', cell_value, 'is same as ', i, j)
                        return False
                    if arr[k][j] == cell_value and k != i:
                        print('ERROR:', k, j, 'value', cell_value, 'is same as ', i, j)
                        return False
                # Checking if values are not duplicate in Grid
                irow = i / 3 * 3
                icol = j / 3 * 3
                for k in range(irow, irow + 3, 1):
                    for l in range(icol, icol + 3, 1):
                        if arr[k][l] == cell_value and (k != i or l != j):
                            print('ERROR:Grid has duplicate values', k, l, 'value ', cell_value, 'is same as ', i, j)
                            return False
    return True


# SudukoHint(arr)
def main(arr, flag):
    return SudukoHint(arr, flag)
