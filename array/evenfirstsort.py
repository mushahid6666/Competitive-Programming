__author__ = 'mushahidalam'


def partition(ar, low, high):
    if (low == high):
        return low
    key = ar[low]
    index = low
    for i in range(low + 1, high + 1):
        if ar[i] % 2 == 0 < key % 2 != 0:
            temp = ar[i]
            j = index
            k = i
            while k != j:
                ar[k] = ar[k - 1]
                k -= 1
            ar[k] = temp
            index += 1
    return index


def merge(ar, low, high):
    if (low < high):
        pivot = partition(ar, low, high)
        merge(ar, low, pivot - 1)
        merge(ar, pivot + 1, high)
    return ar


# def compare(a,b):
#     if a%2==0 and b%2!=0:
#         return -1
#     elif a%2!=0 and b%2==0:
#         return 1
#     else:
#         return 0

def evenoddsort(arr):
    # arr = sorted(arr,compare)
    # return merge(arr,0,len(arr)-1)
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[j] % 2 == 0:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
        else:
            j -= 1
    return arr


arr = [2, 4, 6, 8, 20, 3]
print(evenoddsort(arr))
