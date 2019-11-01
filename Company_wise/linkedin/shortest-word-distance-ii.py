import collections, bisect, sys
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordsDict = collections.defaultdict(list)
        for i in range(len(words)):
            cur_word = words[i]
            if cur_word in self.wordsDict:

                index = bisect.bisect(self.wordsDict[cur_word], i, 0, len(self.wordsDict[cur_word]))
                self.wordsDict[cur_word].insert(index, i)
            else:
                self.wordsDict[cur_word] = [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = 0
        j = 0
        word1_indexes = self.wordsDict[word1]
        word2_indexes = self.wordsDict[word2]
        cur_distance = sys.maxint
        while i < len(word1_indexes) and j < len(word2_indexes):
            cur_distance = min(cur_distance, abs(word1_indexes[i] - word2_indexes[j]))
            if word1_indexes[i] < word2_indexes[j]:
                i+=1
            else:
                j+=1
        return cur_distance

# Your WordDistance object will be instantiated and called as such:

words = ["practice", "makes", "perfect", "coding", "makes","practice","coding"]
obj = WordDistance(words)
print obj.shortest("coding","practice")
print obj.shortest("makes","coding")