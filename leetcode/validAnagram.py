class Solution(object):
    def merge(self, str1, str2):
        i = 0
        j = 0
        result_str = ""
        while i < len(str1) and j < len(str2):
            if ord(str1[i]) < ord(str2[j]):
                result_str += str1[i]
                i+= 1
            else:
                result_str += str2[j]
                j += 1
        while i < len(str1):
            result_str += str1[i]
            i += 1
        while j < len(str2):
            result_str += str2[j]
            j += 1
        return result_str
    def mergeSort(self, string, low, high):
        if low == high:
            return string[low]
        if low < high:
            mid = (low + high)/ 2
            str1  = self.mergeSort(string, low, mid)
            str2 = self.mergeSort(string, mid+1, high)
            result  = self.merge(str1, str2)
            return result

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (s == "" and t != "") or (s != "" and t == ""):
            return False
        if (s == "" and t == ""):
            return True
        str1_sorted = self.mergeSort(s, 0, len(s)- 1)
        str2_sorted = self.mergeSort(t, 0, len(t)- 1)
        temp_dict = dict()
        temp_dict[str1_sorted]  = 0
        if str2_sorted in temp_dict:
            return True
        return False

obj = Solution()
s = "anagram"
t = "nagaram"
print obj.isAnagram(s,t)
s = ""
t = "car"
print obj.isAnagram(s,t)
s = ""
t = "anagram"
print obj.isAnagram(s,t)
s = ""
t = ""
print obj.isAnagram(s,t)
s = "anagram"
t = "a"
print obj.isAnagram(s,t)
