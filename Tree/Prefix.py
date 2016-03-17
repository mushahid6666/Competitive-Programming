__author__ = 'mushahidalam'
from collections import OrderedDict


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        if len(A) == 0:
            return []
        dict = OrderedDict()
        for i in A:
            str = i
            n = len(str)
            temp = ""
            for i in range(n):
                temp = str[i]
                if temp in dict:
                    dict[temp] += 1
                else:
                    dict[temp] = 1
        print(dict)
        result = OrderedDict()
        for i in A:
            str = i
            n = len(str)
            temp = ""
            for i in range(n):
                temp += str[i]
                key = str[i]
                if dict[key] != 1:
                    continue
                else:
                    result[temp] = 1
                    break
        ret = result.keys()
        return ret


obj = Solution()
arr = ["bearcat", "bert"]
print obj.prefix(arr)
