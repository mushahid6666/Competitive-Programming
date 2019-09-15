import copy
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        if len(paths) == 0:
            return []
        file_contents_set = set()
        result_group = dict()
        for i in range(len(paths)):
            cur_directory = paths[i]
            dir_path = cur_directory.split(" ")[0]
            file_list  = cur_directory.split(" ")[1:]
            for file in file_list:
                cur_file_content = file.split("(")
                cur_file_path = cur_file_content[0]
                cur_file_content= cur_file_content[1]
                cur_file_content = cur_file_content[:-1]
                result_str = dir_path + "/" +cur_file_path
                if cur_file_content in file_contents_set:
                    result_group[cur_file_content].append(result_str)
                else:
                    file_contents_set.add(cur_file_content)
                    result_group[cur_file_content] = [result_str]
        result_list = []
        for entry in result_group:
            if len(result_group[entry]) > 1:
                result_list.append(result_group[entry])
        return result_list
                # print cur_file_content, cur_file_path, dir_path




paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
# Output:
# [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
obj = Solution()
print obj.findDuplicate(paths)