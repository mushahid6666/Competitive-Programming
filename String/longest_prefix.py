__author__ = 'mushahidalam'
import string
import _List
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #Attempt 3:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        common_prefix_stack = strs[0]
        for i in range(1, len(strs)):
            str = strs[i]
            j = 0
            EOS = True
            while j < len(str) and j < len(common_prefix_stack):
                if str[j] == common_prefix_stack[j]:
                    j = j + 1
                else:
                    if j == 0:
                        return ""
                    common_prefix_stack = common_prefix_stack[:j]
                    EOS = False
                    break
            if EOS == True:
                common_prefix_stack = common_prefix_stack[:j]
        return common_prefix_stack

obj = Solution()
strs = ["flower", "flow", "flight"]
print strs , " Common prefix = " + obj.longestCommonPrefix(strs)

strs = ["dog","racecar","car"]
print strs , " Common prefix = " + obj.longestCommonPrefix(strs)

strs = ["ad","ada","adag"]
print strs , " Common prefix = " + obj.longestCommonPrefix(strs)

strs = ["masdada","ada","adag"]
print strs , " Common prefix = " + obj.longestCommonPrefix(strs)

        #Leetcode Accepted Solution
        # if len(strs) == 0:
        #     return ""
        # if len(strs) == 1:
        #     return strs[0]
        # result = strs[0]
        # for i in range(1, len(strs)):
        #     str1 = strs[i - 1]
        #     str2 = strs[i]
        #     j = 0
        #     k = 0
        #     temp_result = ""
        #     while j < len(str1) and k < len(str2):
        #         if str1[j] == str2[k]:
        #             temp_result += str1[j]
        #             j += 1
        #             k += 1
        #         else:
        #             break
        #     if len(temp_result) < len(result):
        #         result = temp_result
        # return result
# class Solution:
#     # @param A : list of strings
#     # @return a strings
#     def longestCommonPrefix(self, A):
#         #Leetcode Accepted Solution
#         length = len(A)
#         if length==1:
#             return A[0]
#         ele = 0
#         small = 9999
#         for i in range(0,length):
#             temp= len(A[i])
#             if temp < small:
#                 small = temp
#                 ele = i
#         # print(small)
#         # print(A[ele])
#         i=0
#         longpre = A[ele][0]
#         while i<small:
#             for k in range(0,length):
#                 if longpre[i] == A[k][i]:
#                     continue
#                 else:
#                     # print(longpre)
#                     return longpre[:-1]
#             i=i+1
#             if i<small:
#                 longpre = longpre+A[ele][i]
#         return longpre





A = Solution()
B = ["aaa",
     "aaaaaaaa",
     "aaaaaaaaaaa",
]
print A.longestCommonPrefix(B)
