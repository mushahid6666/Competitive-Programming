__author__ = 'mushahidalam'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.links = []


class Solution():
    dict_start_letters = {}

    def CreateTrie(self, wordlist):
        for word in wordlist:
            if word[0] in self.dict_start_letters:
                root = self.dict_start_letters[word[0]]
            else:
                self.dict_start_letters[word[0]] = TreeNode(word[0])
                root = self.dict_start_letters[word[0]]
            prev = root
            next = root
            for i in range(1, len(word)):
                letter = word[i]
                while next != None:
                    for link in prev.links:
                        if link.val == letter:
                            next = link
                            prev = next
                            continue
                    next = None
                next = TreeNode(letter)
                prev.links.append(next)
                prev = next
        return self.dict_start_letters

    def checkword(self, word):
        if word[0] in self.dict_start_letters:
            root = self.dict_start_letters[word[0]]
        else:
            return False
        for i in range(1, len(word)):
            letter = word[i]
            if len(root.links) == 0:
                return False
            flag = 0
            for link in root.links:
                if link.val == letter:
                    root = link
                    flag = 1
                    break
            if flag != 1:
                return False
        if len(root.links) == 0:
            return True
        else:
            return False


obj = Solution()
wordlist = ['abc', 'adb', 'bcd', 'def']
obj.CreateTrie(wordlist)
print obj.checkword('adb')
