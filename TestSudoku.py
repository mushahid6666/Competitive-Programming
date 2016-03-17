__author__ = 'MushahidAlam'
from Sudoko import main
from Sudoko import get_hints


def generate2d(input_str):
    k = 0
    arr = []
    for i in range(9):
        temp = []
        for j in range(9):
            if input_str[k] == '.':
                temp.append(-1)
            else:
                temp.append(int(input_str[k]))
            k += 1
        arr.append(temp)
    return arr


def test_invalid_grid():
    arr = generate2d('..9.7...5..21..9..1...28....7...5..1..851.....5....3.......3..68........21.....87')
    output = main(arr, 0)
    if not output:
        print 'TestCase Invalid Grid Passed'
    else:
        print 'TestCase Invalid Grid Failed'


def test_invalid_column():
    arr = generate2d('6.159.....9..1............4.7.314..6.24.....5..3....1...6.....3...9.2.4......16..')
    output = main(arr, 0)
    if not output:
        print 'TestCase Invalid column Passed'
    else:
        print 'TestCase Invalid column Failed'


def test_invalid_row():
    arr = generate2d('.4.1..35.............2.5......4.89..26.....12.5.3....7..4...16.6....7....1..8..2.')
    output = main(arr, 0)
    if not output:
        print 'TestCase Invalid row Passed'
    else:
        print 'TestCase Invalid row Failed'


def test_valid1():
    arr = generate2d('3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.965124.8')
    main(arr, 0)
    # Checking elements from all  Grids
    if cmp(get_hints(1, 2), [6]) == 0 and cmp(get_hints(1, 6), [7]) == 0 and cmp(get_hints(1, 9), [9]) == 0 and \
                    cmp(get_hints(4, 3), [2]) == 0 and cmp(get_hints(5, 5), [4]) == 0 and cmp(get_hints(4, 7),
                                                                                              [6]) == 0 and \
                    cmp(get_hints(9, 1), [7]) == 0 and cmp(get_hints(7, 5), [8]) == 0 and cmp(get_hints(7, 7),
                                                                                              [7]) == 0:
        print 'TestCase valid1 Passed'
    else:
        print 'TestCase valid1 Failed'


def test_valid2():
    arr = generate2d('7...8...2..3.249...4...9....8421...5..9...2..1...9543....4...5...165.3..2...3...4')
    main(arr, 0)
    # Checking elements from all  Grids
    if cmp(get_hints(1, 2), [1, 5, 6, 9]) == 0 and cmp(get_hints(1, 4), [1, 3, 5]) == 0 and cmp(get_hints(1, 7),
                                                                                                [1, 5, 6]) == 0 and \
                    cmp(get_hints(4, 1), [3, 6]) == 0 and cmp(get_hints(4, 6), [3, 6, 7]) == 0 and cmp(get_hints(5, 8),
                                                                                                       [1, 6, 7,
                                                                                                        8]) == 0 and \
                    cmp(get_hints(7, 1), [3, 6, 8, 9]) == 0 and cmp(get_hints(8, 6), [2, 7, 8]) == 0 and cmp(
        get_hints(9, 7), [1, 6, 7, 8]) == 0:
        print 'TestCase valid2 Passed'
    else:
        print 'TestCase valid2 Failed'


def test_invalid_board_size():
    arr = [[3, -1, 5, 4, 2, -1, 8, 1, -1],
           [4, 8, 7, 9, -1, 1, 5, -1, 6],
           [-1, 2, 9, -1, 5, 6, 3, 7, 4],
           [8, 5, -1, 7, 9, 3, -1, 4, 1],
           [6, 1, 3, 2, -1, 8, 9, 5, 7],
           [-1, 7, 4, -1, 6, 5, 2, 8, -1, 5],  # row has has 10 columns
           [2, 4, 1, 3, -1, 9, -1, 6, 5],
           [5, -1, 8, 6, 7, -1, 1, 9, 2],
           [-1, 9, 6, 5, 1, 2, 4, -1, 8, 3]]  # row has has 10 columns
    output = main(arr, 0)
    if not output:
        print 'TestCase Invalid row Passed'
    else:
        print 'TestCase Invalid row Failed'


def rangeCheck():
    arr = [[3, -1, 5, 4, 2, -1, 8, 1, -1],
           [4, 8, 7, 9, -1, 1, 5, -1, 6],
           [-1, 2, 9, -1, 5, 6, 3, 7, 4],
           [8, 5, -1, 7, 9, 3, -1, 4, 1],
           [6, 1, 3, 2, -1, 8, 9, 5, 7],
           [-1, 7, 4, -1, 6, 5, 2, 8, -1],
           [2, 4, 1, 3, -1, 9, -1, 6, 5],
           [5, -1, 8, 6, 7, -1, 1, 9, 2],
           [-1, 9, 6, 5, 1, 2, 4, -1, 15]]  # last cell value is 15 which is not correct
    output = main(arr, 0)
    if not output:
        print 'TestCase range check Passed'
    else:
        print 'TestCase range check Failed'


def test_type_check():
    arr = 'String Input'
    output = main(arr, 0)
    if not output:
        print 'TestCase type check Passed'
    else:
        print 'TestCase type check Failed'


test_invalid_grid()
test_invalid_column()
test_invalid_row()
test_valid1()
test_valid2()
test_invalid_board_size()
rangeCheck()
test_type_check()
