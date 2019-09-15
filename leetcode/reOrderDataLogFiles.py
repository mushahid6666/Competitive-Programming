class Solution(object):

    def compare(self, a , b):
        str1 = a.split(" ")
        str2 = b.split(" ")
        id1 = str1[0]
        id2 = str2[0]
        key1 = a.replace(id1 + " ", "")
        key2 = b.replace(id2 + " ", "")
        if key1< key2 :
            return -1
        elif key1 > key2 :
            return 1
        else:
            if id1 < id2:
                return -1
            elif id1 < id2:
                return 1
            else:
                return 0

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if len(logs) == 0:
            return []
        if len(logs) == 1:
            return logs
        letter_log_list = []
        digit_log_list = []
        for cur_log in logs:
            space_delimited_log_list = cur_log.split(" ")
            if space_delimited_log_list[1].isdigit():
                digit_log_list.append(cur_log)
            else:
                letter_log_list.append(cur_log)
        result = []
        letter_log_list.sort(self.compare)
        if len(letter_log_list) > 0:
            for cur_log in letter_log_list:
                result.append(cur_log)

        if len(digit_log_list) > 0:
            for cur_log in digit_log_list:
                result.append(cur_log)

        return result



obj = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
print obj.reorderLogFiles(logs)