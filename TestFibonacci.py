__author__ = 'mushahidalam'
from Fibonacci import fib_string


# test invalid Number
def test_invalid_Number(n):
    result = fib_string(n)
    if result == '':
        print('TestInvalid_Number Pass')
    else:
        print('TestInvalid_Number Fail')


# Test the fibonacii Series Returned
def test_fib(n, expected):
    result = fib_string(n)
    if result == expected:
        print('Test_fib Pass', n)
    else:
        print('Test_fib Fail', n)


def large_input(n, filename):
    # Reading the expected output from the filename passed
    expected = ""
    for number in open(filename):
        if '\n' in number:
            number = number[:-1]
        expected += str(number)
        expected += ','
    expected = expected.rstrip(',')

    result = fib_string(n)
    if result == expected:
        print('large_input Pass', n)
    else:
        print('large_input Fail', n)


# Test Invalid Number
test_invalid_Number(-24)
# Basic Test Cases
test_fib(0, '0')
test_fib(3, '0,1,1')
test_fib(5, '0,1,1,2,3')
test_fib(24, '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657')

# Test for large Input
large_input(1024, 'Large_Input_1')
large_input(2024, 'Large_Input_2')
