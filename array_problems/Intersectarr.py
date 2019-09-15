__author__ = 'mushahidalam'
import collections


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        num1Dict = dict()
        for element in nums1:
            if element in num1Dict:
                num1Dict[element] += 1
            else:
                num1Dict[element] = 1
        result = []
        for element in nums2:
            if element in num1Dict:
                if num1Dict[element] > 0:
                    result.append(element)
                    num1Dict[element] -=1
        return result
    # def intersect(self, A, B):
    #     # Utilizting bot the arrays is sorted Complexity O(m+n)
    #     len1 = len(A)
    #     len2 = len(B)
    #     i = 0;
    #     j = 0;
    #     result = []
    #     while i < len1 and j < len2:
    #         if A[i] == B[j]:
    #             result.append(A[i])
    #             i += 1;
    #             j += 1
    #         elif A[i] > B[j]:
    #             j += 1
    #         else:
    #             i += 1
    #     return result
        # Using Hash table COmplexity : O(m+n) , Doesn't work if set A contains 1 billion elements
        # result=collections.OrderedDict()
        # for i in range(0,len(A)):
        #     if A[i] in result:
        #         prev=result[A[i]]
        #         prev.append(i)
        #         result[A[i]]= prev
        #     else:
        #         result[A[i]]=[i]
        # for i in B:
        #     if i in result:
        #         if len(result[i]) > 1:
        #             result[i].pop()
        #         else:
        #             result.pop(i)
        # # print(result)
        # for i in A:
        #     if i in result:
        #         if result[i][0]!=-1:
        #             if len(result[i])>1:
        #                 result[i].pop()
        #             else:
        #                 result.pop(i)
        #         else:
        #             prev = result[i]
        #             prev.append(-1)
        #             result[i]=prev
        #     else:
        #         result[i]=[-1]
        # total = []
        # for i in result:
        #     if len(result[i])> 1:
        #         for k in range(0,len(result[i])):
        #             total.append(i)
        #     else:
        #         total.append(i)
        # return total


obj = Solution()
A = [1, 3, 8, 10, 10, 14, 16, ]
B = [4, 7, 10, 10, 3]

# 7 10 10
print obj.intersect(A, B)
