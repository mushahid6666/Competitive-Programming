class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)== "" and len(s) !="" or len(s) == "" and len(p) != "":
            return []
        if len(p)== "" and len(s) =="":
            return [0]
        target_str_len = len(p)
        target_str_dict = dict()
        for char in p:
            if char in target_str_dict:
                target_str_dict[char] += 1
            else:
                target_str_dict[char] = 1

        target_str_counter = target_str_len
        left_pointer = 0
        right_pointer = 0
        result = []
        while right_pointer < len(s):
            if s[right_pointer] in target_str_dict:
                if target_str_dict[s[right_pointer]] >= 1:
                    target_str_counter -= 1
                target_str_dict[s[right_pointer]] -= 1


            if target_str_counter == 0:
                result.append(left_pointer)

            if (right_pointer - left_pointer + 1) == target_str_len:
                if ( s[left_pointer] in target_str_dict ):
                    if target_str_dict[s[left_pointer]] >= 0:
                        target_str_counter += 1
                    target_str_dict[s[left_pointer]] += 1
                left_pointer += 1
            right_pointer += 1
        return result

obj = Solution()
s = "cbaebabacd"
p = "abc"
print obj.findAnagrams(s, p)
s= "abab"
p= "ab"
print obj.findAnagrams(s, p)
s = "baa"
p = "aa"
print obj.findAnagrams(s, p)