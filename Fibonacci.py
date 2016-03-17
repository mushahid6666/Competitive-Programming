__author__ = 'mushahidalam'
import logging


def fib_string(n):
    # If n is negative return error
    if n < 0:
        logging.error('N should be positive')
        return ''

    # return 0th element
    if n == 0:
        return "0"

    # return 1th element
    if n == 1:
        return "0,1"

    # Intializing the 0th and 1st number of the series
    fib_i_minus_2 = 0
    fib_i_minus_1 = 1


    # Compute the series from 3 till n
    result = "0,1"
    for i in range(3, n + 1):
        result += ','

        # Calculate the fib[i]
        fib_i = fib_i_minus_1 + fib_i_minus_2

        # Append the calculated nth number to result string
        result += str(fib_i)

        # Update the fib[i-1] and fib[i-2]
        fib_i_minus_2 = fib_i_minus_1
        fib_i_minus_1 = fib_i

    return result
