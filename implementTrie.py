class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if cur_node.children[index] == None:
                cur_node.children[index] = TrieNode()
            cur_node = cur_node.children[index]

        cur_node.endOfWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if cur_node.children[index] == None:
                return False
            cur_node = cur_node.children[index]
        if cur_node.endOfWord == True:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if cur_node.children[index] == None:
                return False
            cur_node = cur_node.children[index]
        return True

# Your Trie object will be instantiated and called as such:
#Edge Cases:
#TestCase1
obj = Trie()
word = ""
obj.insert(word)
print "search:",word, "result: ",obj.search(word)
#TestCase2
obj = Trie()
word = "a"
obj.insert(word)
print "search:",word, "result: ",obj.search(word)
#TestCase3
obj = Trie()
word = "aaaaaaaaaaaa"
obj.insert(word)
print "search:",word, "result: ",obj.search(word)
word = "aa"
print "search:",word, "result: ",obj.search(word)
#TestCase4
obj = Trie()
word = "apple"
obj.insert(word)
print "search:",word, "result: ",obj.search(word)
prefix = "app"
print "prefix:",prefix, "result: ",obj.search(prefix)
print "startsWith:",prefix, "result: ", obj.startsWith(prefix)
word = "app"
obj.insert(word)
print "search:",word, "result: ", obj.search(word)
word = "appleIndia"
obj.insert(word)
print "search:",word, "result: ", obj.search(word)
prefix = "appleI"
print "startsWith:",prefix, "result: ", obj.startsWith(prefix)
prefix = "appleIndi"
print "search:",prefix, "result: ", obj.search(prefix)

