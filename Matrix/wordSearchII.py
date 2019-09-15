class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.word = None

class Solution(object):
    def recursiveSearch(self, board, i, j, node, result):
        rows = len(board)
        cols = len(board[0])

        if i<0 or j <0 or i >=rows or j >= cols:
            return

        char = board[i][j]
        if char == "#" or node.children[ord(char)-ord('a')] == None:
            return
        node = node.children[ord(char)-ord('a')]

        if node.word != None:
            result.append(node.word)
            node.word = None

        tmp = board[i][j]
        board[i][j]="#"

        result = (self.recursiveSearch(board,   i+1, j, node, result)
            or self.recursiveSearch(board,  i-1, j, node, result)
            or self.recursiveSearch(board,   i, j + 1, node, result)
            or self.recursiveSearch(board,  i, j-1 , node, result))
        board[i][j] = tmp
        return result

    def constructTrie(self, root, words):
        for word in words:
            node = root
            for c in word:
                if node.children[ord(c)-ord('a')] == None:
                    node.children[ord(c) - ord('a')] = TrieNode()
                node = node.children[ord(c) - ord('a')]
            node.word = word
        return root

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return []

        #Construct Trie
        root = TrieNode()
        self.constructTrie(root, words)
        result = []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                self.recursiveSearch(board, i, j, root, result)
        return result


obj = Solution()
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
board = [["a","a"]]
words = ["a"]
print obj.findWords(board, words)
# Output: ["eat","oath"]