__author__ = 'mushahidalam'


def sort(arrays):
    result = arrays[0]


for listindex in range(1, len(arrays)):
    temp = arrays[listindex]
    i = 0
    j = 0
    tempresult = []
    while i < len(result) and j < len(temp):
        if result[i] > temp[j]:
            tempresult.append(temp[j])
            j += 1
        else:
            tempresult.append(result[i])
            i += 1
    while i < len(result):
        tempresult.append(result[i])
        i += 1
    while j < len(temp):
        tempresult.append(temp[j])
        j += 1
    result = tempresult
    print(result)
arrays = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
sort(arrays)
