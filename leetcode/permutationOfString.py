class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)== "" and len(s2) !="" or len(s2) == "" and len(s1) != "":
            return False
        if len(s1)== "" and len(s2) =="":
            return True
        target_str_len = len(s1)
        target_str_dict = dict()
        for char in s1:
            if char in target_str_dict:
                target_str_dict[char] += 1
            else:
                target_str_dict[char] = 1

        target_str_counter = target_str_len
        left_pointer = 0
        right_pointer = 0
        result = []
        while right_pointer < len(s2):
            if s2[right_pointer] in target_str_dict:
                if target_str_dict[s2[right_pointer]] >= 1:
                    target_str_counter -= 1
                target_str_dict[s2[right_pointer]] -= 1


            if target_str_counter == 0:
                return True

            if (right_pointer - left_pointer + 1) == target_str_len:
                if ( s2[left_pointer] in target_str_dict ):
                    if target_str_dict[s2[left_pointer]] >= 0:
                        target_str_counter += 1
                    target_str_dict[s2[left_pointer]] += 1
                left_pointer += 1
            right_pointer += 1
        return False

s1 = "ab"
s2 = "eidbaooo"
obj = Solution()
print obj.checkInclusion(s1, s2)
s1= "ab"
s2 = "eidboaoo"
print obj.checkInclusion(s1, s2)