import  md5, collections
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        fileHashDict = collections.defaultdict(list)
        #md5.new("Nobody inspects the spammish repetition").hexdigest()
        for directoryContents in paths:
            directoryContents = directoryContents.split(" ")
            dir_path = directoryContents.pop(0)
            for file in directoryContents:
                file = file.split("(")
                filename = file.pop(0)
                fileContent = file.pop(0)[:-1]
                filePath= dir_path + "/"+ filename
                fileHash = md5.new(fileContent).hexdigest()
                fileHashDict[fileHash].append(filePath)
        result = []
        for value in fileHashDict.values():
            if len(value) > 1:
                result.append(value)
        return result


obj = Solution()
input = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print obj.findDuplicate(input)
input = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
print obj.findDuplicate(input)

