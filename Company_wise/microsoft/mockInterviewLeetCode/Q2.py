import collections, copy
class Solution(object):
    def compare(self, a, b):
        if ord(a)-ord('a') < ord(b)-ord('a'):
            return -1
        elif ord(a)-ord('a') > ord(b)-ord('a'):
            return 1
        else:
            return 0
    def compute_all_subsequence(self, text, index, exp, remaining_chars_list,char_dict):
        if index == len(text):
            ans = "".join(exp)
            self.allSubSeq.add(ans)
            return
        char = text[index]
        if char in remaining_chars_list and char_dict[char] > 1:
            new_list2 = copy.deepcopy(remaining_chars_list)
            char_dict_new = copy.deepcopy(char_dict)
            char_dict_new[char] -=1
            self.compute_all_subsequence(text, index + 1, exp, new_list2, char_dict_new)
            exp += char
            new_list = copy.deepcopy(remaining_chars_list)
            new_list.remove(char)
            char_dict_new= copy.deepcopy(char_dict)
            char_dict_new[char] = 0
            self.compute_all_subsequence(text, index + 1, exp, new_list, char_dict_new)
        else:
            if char in remaining_chars_list:
                exp += char
                new_list = copy.deepcopy(remaining_chars_list)
                new_list.remove(char)
                char_dict_new = copy.deepcopy(char_dict)
                char_dict_new[char] = 0
                self.compute_all_subsequence(text, index + 1, exp, new_list, char_dict_new)
            else:
                self.compute_all_subsequence(text, index + 1, exp, remaining_chars_list, char_dict)

    def compare(self, a, b):
        if (ord(a[0])-ord('a')) < (ord(b[0]) - ord('a')):
            if a[1][0] > b[1][-1]:
                return 1
            else:
                return -1
        elif (ord(a[0])-ord('a')) > (ord(b[0]) - ord('a')):
            if a[1][-1] < b[1][0]:
                return -1
            else:
                return 1
        else:
            return 0
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        if len(text) == 0:
            return ""
        self.allSubSeq = set()
        char_dict = collections.defaultdict(list)
        for i in range(len(text)):
            char = text[i]
            char_dict[char].append(i)
        result_list = []
        for key,value in char_dict.items():
            result_list.append([key, value])

        result_list.sort(self.compare)

        result = []
        for entry in result_list:
            result.append(entry[0])
        return  "".join(result)
        # self.distinct_chars = char_dict.keys()
        # self.compute_all_subsequence(text, 0, "", copy.deepcopy(self.distinct_chars), char_dict)
        # all_ans = list(self.allSubSeq)
        # all_ans.sort()
        # return all_ans[0]



obj = Solution()
# string =  "ecbacba"
# print obj.smallestSubsequence(string)
string =  "leetcode"
print obj.smallestSubsequence(string)
# string =  "cdadabcc"
# print obj.smallestSubsequence(string)
# string =  "abcd"
# print obj.smallestSubsequence(string)
# string =  "a"
# print obj.smallestSubsequence(string)
# string = "dbdcbcbeecbbdcdebadbcecccdbaabaeeacbbcab"
# print obj.smallestSubsequence(string)
# Output: "adbc"