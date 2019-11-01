class Solution(object):
    def __init__(self):
        self.decodeCount = 0
    def decodeStr(self, s, index, memo):
        if index == len(s):
            self.decodeCount += 1
            return 1
        if memo[index] !=0:
            self.decodeCount += memo[index]
            return memo[index]
        digit = int(s[index])
        count = 0
        if digit != 0:
            count += self.decodeStr(s, index +1, memo)
        if digit != 0 and index + 1 < len(s):
            nextDigit = int(s[index+1])
            number = digit * 10 + nextDigit
            if number > 0 and number < 27:
                count +=self.decodeStr(s, index +2 , memo)
        memo[index] += count
        return count

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.__init__()
        if len(s)==0 or s[0] == "0":
            return 0
        memo = [0] * len(s)
        self.decodeStr(s, 0, memo)
        return self.decodeCount

solObj = Solution()
Input= "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
print solObj.numDecodings(Input), "ExpOutput: 2"
Input= "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
print solObj.numDecodings(Input), "ExpOutput: 3"
Input = "1212121212"
print solObj.numDecodings(Input), "ExpOutput: 89"
Input = "01"
print solObj.numDecodings(Input), "ExpOutput: 0"
Input = "101"
print solObj.numDecodings(Input), "ExpOutput: 1"