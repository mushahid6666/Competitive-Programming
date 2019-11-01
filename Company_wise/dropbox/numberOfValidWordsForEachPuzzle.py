"""
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage";
while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).

Return an array answer, where answer[i] is the number of words in the given word list words that are
 valid with respect to the puzzle puzzles[i].


Example :

Input:
words = ["aaaa","asas","able","ability","actt","actor","access"],
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa"
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.


Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
"""
import collections

class TrieNode(object):
    def __init__(self):
        self.word_count = 0
        self.children = [None] * 26
class Solution(object):
    def addNode(self, cur_word, curNode):
        """
        :param cur_word: String
        :param node:  TrieNode
        :return:
        """
        for i in range(len(cur_word)):
            index = ord(cur_word[i]) - ord('a')
            if curNode.children[index] == None:
                childNode = TrieNode()
                curNode.children[index] = childNode
            curNode = curNode.children[index]
        curNode.word_count += 1
    def search(self, rootNode, puzzle, index,  firstSeen, firstLetter):
        if rootNode == None:
            return 0
        count = 0

        if firstSeen:
            count += rootNode.word_count

        for i in range(index, len(puzzle)):
            index = ord(puzzle[i]) - ord('a')
            if puzzle[i] == firstLetter:
                count += self.search(rootNode.children[index], puzzle, i + 1, True, firstLetter)
            else:
                count += self.search(rootNode.children[index], puzzle, i + 1 ,  firstSeen, firstLetter)
        return count

    def findNumOfValidWords(self, words, puzzles):
        rootNode = TrieNode()

        for cur_word in words:
            cur_word_set = set(cur_word)
            cur_word_list = sorted(cur_word_set)
            cur_word_string = ""
            for charecter in cur_word_list:
                cur_word_string += charecter
            self.addNode(cur_word_string, rootNode)
        result = []
        for cur_puzzle in puzzles:
            firstLetter = cur_puzzle[0]
            cur_puzzle = sorted(cur_puzzle)
            result.append(self.search(rootNode, cur_puzzle, 0,  False, firstLetter))
        return result



    def findNumOfValidWords1(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """

        if len(words) == 0:
            result = [0]* len(puzzles)
            return result
        letter_word_map = dict()
        # puzzle_first_word_map = dict()
        for i in range(27):
            letter_word_map[i] = set()
            # puzzle_first_word_map[i] = set()


        for i in range(len(puzzles)):
            # puzzle_first_word_map[ord(puzzles[i][0]) - ord('a')].add(i)
            cur_puzzle = puzzles[i]
            for charecter in cur_puzzle:
                letter_word_map[ord(charecter) - ord('a')].add(i)

        result = [0] * len(puzzles)
        for i  in range(len(words)):
            cur_word = words[i]
            matching_puzzles = letter_word_map[ord(cur_word[0]) - ord('a')]
            cur_word = set(cur_word)
            for charecter in cur_word:
                new_set = letter_word_map[ord(charecter) - ord('a')]
                matching_puzzles = matching_puzzles.intersection(new_set)
            for puzzle_index in matching_puzzles:
                if puzzles[puzzle_index][0] in cur_word:
                    result[puzzle_index] += 1

        return result



obj = Solution()
words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print obj.findNumOfValidWords(words,puzzles), "Output: [1,1,3,2,4,0]"
words = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
print obj.findNumOfValidWords(words,puzzles), "Output: [0,1,3,2,0]"
# [0,1,1,0,0]
