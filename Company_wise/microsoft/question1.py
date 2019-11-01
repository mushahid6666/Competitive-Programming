# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    res = []
    target  =0
    for i in range( N -1):
        res.append(i)
        target += i
    res.append(-target)
    return res

print solution(4)