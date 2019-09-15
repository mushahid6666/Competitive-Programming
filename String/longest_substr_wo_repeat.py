class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        #Attempt 2:
        LongestSubstrNR = 0
        curLongestSubstr = 0
        hash_map_letters = {}
        start = 0
        end = 0
        while end < len(s):
            # if duplicate letter detected in substr
            if s[end] in hash_map_letters:
                #Update LongestSubstrNR
                if LongestSubstrNR < curLongestSubstr:
                    LongestSubstrNR = curLongestSubstr
                #Move start pointer and remove the letter from hash_map
                #untill uniqueness in substr achieved
                while s[end] in hash_map_letters and start != end:
                    del hash_map_letters[s[start]]
                    start = start + 1
                    curLongestSubstr = curLongestSubstr - 1
                #Insert the end pointer letter and update curLongestSubstr & continue
                hash_map_letters[s[end]] = end
                curLongestSubstr = curLongestSubstr + 1
                end = end + 1
            else:
                #if not insert into hash_map
                hash_map_letters[s[end]]= end
                #Move the end pointer
                end = end + 1
                # increase curLongestSubstr len
                curLongestSubstr = curLongestSubstr + 1

        #Return curLongestSubstr if greater than LongestSubstrNR
        if curLongestSubstr > LongestSubstrNR:
            return curLongestSubstr
        return LongestSubstrNR

        {
        #Optimized Solution 1, PASSING LEETCODE
        # if len(s) == 0:
        #     return 0
        # if len(s)== 1:
        #     return 1
        # dict = {}
        # cur_longest_str = 1
        # max_longest_str = 1
        # start = 0
        # end = 1
        # dict[s[start]]= 1
        # #"pwwkew"
        # while end < len(s):
        #     if s[end] in dict:
        #         if cur_longest_str > max_longest_str:
        #             max_longest_str = cur_longest_str
        #         while s[end] in dict:
        #             del dict[s[start]]
        #             start = start + 1
        #             cur_longest_str = cur_longest_str - 1
        #         dict[s[end]] = 1
        #         cur_longest_str = cur_longest_str + 1
        #     else:
        #         dict[s[end]] = 1
        #         cur_longest_str = cur_longest_str + 1
        #     end = end + 1
        # if cur_longest_str > max_longest_str:
        #     max_longest_str = cur_longest_str
        # return max_longest_str

        #Brute Force Solution
        # if len(s) == 0:
        #     return 0
        # if len(s)== 1:
        #     return 1
        # dict = {}
        # cur_longest_str = 0
        # max_longest_str = 0
        # for i in range(len(s)):
        #     start = i
        #     for j in range(start, len(s)):
        #         if s[j] in dict:
        #             if cur_longest_str > max_longest_str:
        #                 max_longest_str = cur_longest_str
        #             cur_longest_str = 0
        #             dict = {}
        #             break
        #         dict[s[j]] = 1
        #         cur_longest_str += 1
        # return max_longest_str
        }

obj = Solution()
test_str1 = "abcabcbb"
test_str2 = "bbbbb"
test_str3 = "pwwkew"
test_str4 = ""
test_str5 = "a"
test_str6 = "awwa"
test_str7 = "jbpnbwwd"
test_str8 = "au"
print "test_str1: " + test_str1 + " result: ", obj.lengthOfLongestSubstring(test_str1)
print "test_str2: " + test_str2 + " result: ", obj.lengthOfLongestSubstring(test_str2)
print "test_str3: " + test_str3 + " result: ", obj.lengthOfLongestSubstring(test_str3)
print "test_str4: " + test_str4 + " result: ", obj.lengthOfLongestSubstring(test_str4)
print "test_str5: " + test_str5 + " result: ", obj.lengthOfLongestSubstring(test_str5)
print "test_str6: " + test_str6 + " result: ", obj.lengthOfLongestSubstring(test_str6)
print "test_str7: " + test_str7 + " result: ", obj.lengthOfLongestSubstring(test_str7)
print "test_str8: " + test_str8 + " result: ", obj.lengthOfLongestSubstring(test_str8)
# Working Solution, Previous Attempt
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0 or len(s)==1:
#             return len(s)
#         i=0
#         j=1
#         str_map={}
#         str_map[s[i]]=1
#         max_substr_len=1
#         while(j<len(s)):
#             if(s[j] in str_map):
#                 #move i till s[j] not in str_map
#                 #insert s[j] and update max_len if required
#                 while i!=j and str_map[s[j]]==1:
#                     str_map[s[i]]=0
#                     i+=1
#                 str_map[s[j]] = 1
#                 if j - i + 1 > max_substr_len:
#                     max_substr_len = j - i + 1
#                     result_i = i
#                     result_j = j
#             else:
#                 #insert and update max_len if required
#                 str_map[s[j]]=1
#                 if j-i+1 > max_substr_len:
#                     max_substr_len=j-i+1
#                     result_i = i
#                     result_j = j
#             j += 1
#         return max_substr_len