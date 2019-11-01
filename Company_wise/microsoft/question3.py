# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(A):
    # write your code in Python 3.6
    number_dict = dict()
    N = len(A)
    for i  in  range(len(A)):
        if A[i] in number_dict:
                number_dict[A[i]].append(i)
        else:
            number_dict[A[i]] = [i]

    # for key in number_dict.keys():
    #     index_array = number_dict[key]
    #     index_array.sort()

    num_identical_pair = int(0)

    for key in number_dict.keys():
        index_length = len(number_dict[key])
        if index_length > 1:
            cur_pairs = 1
            if index_length > 2:
                n_fact = math.factorial(index_length)
                n_minus_two_fact = int(math.factorial(index_length - 2))
                cur_pairs = int((n_fact / (2 * (n_minus_two_fact))))
            num_identical_pair += cur_pairs
    return num_identical_pair

A = [3,3,6,3,3,5]
print solution(A)
