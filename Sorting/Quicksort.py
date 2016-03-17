__author__ = 'mushahidalam'
# !/bin/python
import math


def partition(ar, low, high):
    if (low == high):
        return low
    key = ar[low]
    index = low
    for i in range(low + 1, high + 1):
        if ar[i] < key:
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


def quickSort(ar):
    return merge(ar, 0, len(ar) - 1)


#
# def  IntersectStrings( first,  second):
#     hashtable1 = dict()
#     for letter in first:
#         if letter in hashtable1:
#             hashtable1[letter]+=1
#         else:
#             hashtable1[letter]=1
#     hashtable2 = dict()
#     for letter in second:
#         if letter in hashtable2:
#             hashtable2[letter]+=1
#         else:
#             hashtable2[letter]=1
#     common = []
#     for key in hashtable1:
#         if key in hashtable2:
#             count = min(hashtable1[key],hashtable2[key])
#             common.extend([key] * count)
#     arr= quickSort(common)
#     result = ''
#     for i in arr:
#         result+=i
#     return result


# m = input()
# ar = [int(i) for i in raw_input().strip().split()]
# def partition(arr,low,high):
#     if(low==high):
#         return low
#     key = arr[low]
#     index = low
#     for i in range(low+1,high+1):
#         if arr[i] > key:
#             temp = arr[i]
#             j = index
#             k = i
#             while i!=j:
#                 arr[k]=arr[k-1]
#                 k-=1
#             arr[k]=temp
#             index+=1
#     return index
#
# def merge(arr,low,high):
#     if(low<high):
#         pivot=partition(arr,low,high)
#         merge(arr,low,pivot-1)
#         merge(arr,pivot+1,high)
#     return arr
#
#
# def quicksort(arr):
#     n=len(arr)
#     return merge(arr,0,n-1)

# arr=[2,10,5,35,3,4]
# quicksort(arr)
arr = [5, 8, 1, 3, 1, 7, 9, 2]
print quickSort(arr)
