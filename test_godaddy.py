__author__ = 'mushahidalam'


def wiggleArrangeArray(intArr):
    intArr.sort()
    n = len(intArr)
    mid = n / 2
    result = []
    i = 0
    j = n - 1
    count = 0
    while j > i:
        if count % 2 == 0:
            result.append(intArr[j])
            j = j - 1
        else:
            result.append(intArr[i])
            i = i + 1
        count += 1
    result.append(j)
    return result


arr = [25, -2, 25, 2, 8, 5, 7]
print wiggleArrangeArray(arr)
