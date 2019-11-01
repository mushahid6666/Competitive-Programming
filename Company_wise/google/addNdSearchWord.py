class TrieNode(object):
    def __init__(self, char):
        self.node_char = char
        self.child_nodes =  [None] * 26
        self.child_words = set()
        self.used_letter_index = set()
        self.end_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rootNode = TrieNode("##")

    def addNode(self, word, root_node):
        cur_node = root_node
        for i in range(len(word)):
            cur_charecter = word[i]
            cur_node.child_words.add(word[i:])
            cur_node.used_letter_index.add(ord(cur_charecter) - ord('a'))
            if cur_node.child_nodes[ord(cur_charecter) - ord('a')] == None:
                new_child_node = TrieNode(cur_charecter)
                cur_node.child_nodes[ord(cur_charecter) - ord('a')] = new_child_node
                cur_node = new_child_node
            else:
                cur_node  = cur_node.child_nodes[ord(cur_charecter)- ord('a')]

        cur_node.end_word = True

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.addNode(word, self.rootNode)

    def searchWord(self, word, cur_node):
        if word =="" and cur_node.end_word == True:
            return True
        elif word =="" and cur_node.end_word == False:
            return False
        if word in cur_node.child_words:
            return True
        for i in range(len(word)):
            cur_charecter = word[i]
            if cur_charecter == ".":
                for index in cur_node.used_letter_index:
                    subTreeFound = self.searchWord(word[1:], cur_node.child_nodes[index])
                    if subTreeFound == True:
                        return True
            elif cur_node.child_nodes[ord(cur_charecter) - ord('a')] != None:
                return self.searchWord(word[1:], cur_node.child_nodes[ord(cur_charecter) - ord('a')])
            else:
                return False
        return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchWord(word, self.rootNode)




# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
print obj.search("a") #-> false
print obj.search("at") #-> true

