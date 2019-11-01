import sys
def smallest_subarray_with_given_sum(s, arr):

    i = 0
    cursum = arr[i]
    j = i
    minSubArr = sys.maxsize
    while i < len(arr) and j < len(arr):
        if cursum >= s:
            minSubArr = min(minSubArr, j-i + 1)
        if (cursum < s or i == j) and j < len(arr) -1:
            j+=1
            cursum += arr[j]
        else:
            cursum -= arr[i]
            i+=1
    return minSubArr




arr = [2, 1, 5, 2, 3, 2]
S=7
print smallest_subarray_with_given_sum(S, arr)
arr = [2, 1, 5, 2, 8]
S=7
print smallest_subarray_with_given_sum(S, arr)
arr = [3, 4, 1, 1, 6]
S=8
print smallest_subarray_with_given_sum(S, arr)
