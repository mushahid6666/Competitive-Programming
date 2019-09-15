import copy
class Solution(object):
    def compare(self, str1, str2):
        if (ord(str1[0])-ord('a')) < (ord(str2[0])-ord('a')):
            diff  = (ord(str2[0])-ord('a')) -  (ord(str1[0])-ord('a'))
            for i in range(1,len(str1)):
                if  (ord(str2[i])-ord('a')) - (ord(str1[i])-ord('a'))  == diff:
                    continue
                if (ord(str1[i])-ord('a')) == 25:
                    if (ord(str2[i])-ord('a')) == diff - 1:
                        continue
                return False
            return True
        elif(ord(str1[0])-ord('a')) > (ord(str2[0])-ord('a')):
            diff = (ord(str1[0]) - ord('a')) - (ord(str2[0]) - ord('a'))
            for i in range(1,len(str1)):
                if (ord(str1[i])-ord('a')) - (ord(str2[i])-ord('a')) == diff:
                    continue
                if (ord(str1[i])-ord('a')) == 25:
                    if (ord(str2[i])-ord('a')) == diff - 1:
                        continue
                return False
            return True
        else:
            if str1 == str2:
                return True
            return False
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if len(strings)== 0:
            return []
        if len(strings) == 1:
            return [[strings[0]]]
        string_dict = dict()
        for cur_string in strings:
            if len(cur_string) in string_dict:
                string_dict[len(cur_string)].append(cur_string)
            else:
                string_dict[len(cur_string)] = [cur_string]
        result = []
        string_list_copy = []
        for key,string_list in string_dict.items():
            string_list_copy = copy.deepcopy(string_list)
            if len(string_list) == 1:
                result.append([string_list[0]])
                continue
            for i in range(len(string_list)-1):
                if string_list[i] in string_list_copy:
                    cur_group = [string_list[i]]
                    for j in range(i+1, len(string_list)):
                        if string_list[j] in string_list_copy:
                            shift_seq = self.compare(string_list[i],string_list[j])
                            if shift_seq:
                                cur_group.append(string_list[j])
                                string_list_copy.remove(string_list[j])
                    result.append(cur_group)
                    string_list_copy.remove(string_list[i])
            for string in string_list_copy:
                result.append([string])
        return result

obj = Solution()

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
strings = ["fpbnsbrkbcyzdmmmoisaa","cpjtwqcdwbldwwrryuclcngw","a","fnuqwejouqzrif","js","qcpr","zghmdiaqmfelr","iedda","l","dgwlvcyubde","lpt","qzq","zkddvitlk","xbogegswmad","mkndeyrh","llofdjckor","lebzshcb","firomjjlidqpsdeqyn","dclpiqbypjpfafukqmjnjg","lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil","yxgkdlwtkekavapflheieb","oraxvssurmzybmnzhw","ohecvkfe","kknecibjnq","wuxnoibr","gkxpnpbfvjm","lwpphufxw","sbs","txb","ilbqahdzgij","i","zvuur","yfglchzpledkq","eqdf","nw","aiplrzejplumda","d","huoybvhibgqibbwwdzhqhslb","rbnzendwnoklpyyyauemm"]
# strings = ["ab","bc","cd","bc"]
# strings = ["a","a"]
# strings = ["abc","am"]
print obj.groupStrings(strings)