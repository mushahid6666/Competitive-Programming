import random
from numpy.random import choice
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.indexArr = []
        self.values = w
        self.probDist = [0] * len(w)
        sum = 0
        for i in range(len(w)):
            sum += w[i]
            self.indexArr.append(i)
        distribution = 1/float(sum)
        for i in range(len(w)):
            self.probDist[i] = w[i] * distribution

        # generate probably distribution
    def pickIndex(self):
        """
        :rtype: int
        """
        print self.indexArr,self.probDist
        answer = choice(self.indexArr, 1, self.probDist)
        return answer[0]
# Your Solution object will be instantiated and called as such:
w= [3,14,1,7]
obj = Solution(w)
print obj.pickIndex()