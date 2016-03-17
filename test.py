# #Given an unsorted array nums, reorder it such that
# nums[0] <= nums[1] >= nums[2] <= nums[3]....

# Given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
def reorder(arr):
    arr.sort()
    n = len(arr)
    # 132546
    if n == 0 or n == 1:
        return arr
    if n == 2:
        if arr[1] < arr[0]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return arr
    i = 1
    while (i + 1 < n):
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
        i = i + 2
    return arr


arr = [10, 25, 30]
print reorder(arr)

# 3 5 2 6 1 6 4


# 1 3 2 5 4 6 8 7 9
# 11 20 15 70 25
# 11 12 6 15 4 10
