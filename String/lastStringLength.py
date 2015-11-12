class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        A = A.split(' ')
        print(A)
        length = len(A)
        return len(A[length-1])


A = Solution()
B = "the sky is blue"
print A.lengthOfLastWord(B)