class Solution(object):
    def __init__(self):
        self.allPaliSubStrs = set()
    def checkIfPalindrome(self, subStr, startIndex, EndIndex):
        if subStr[startIndex] == subStr[EndIndex]:
            self.allPaliSubStrs.add(subStr[startIndex: EndIndex + 1])
            return True
        return False
    def findAllPalindromes(self, string):
        n = len(string)
        for i in range(len(string)):
            j = 0
            isPaliOdd = True
            isPaliEven = True
            while j< n/2:

                if i-j >=0 and i+j < n and isPaliOdd:
                    isPaliOdd = self.checkIfPalindrome(string, i - j, i+j)

                if i - j >= 0 and i + j + 1 < n and isPaliEven:
                    isPaliEven = self.checkIfPalindrome(string, i -j, i+j+1)
                if not isPaliEven and not isPaliOdd:
                    break
                j+=1
        return self.allPaliSubStrs


obj = Solution()
string = "abac"
string = "geek"
string = "abaaa"
print obj.findAllPalindromes(string)
