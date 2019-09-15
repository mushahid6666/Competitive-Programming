import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, s):
        """
            :type s: str
            :rtype: bool
        """
        if len(s) == 0 or len(s) == 1 :
            return True
        plan_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                plan_str = plan_str + s[i]
        # print plan_str
        i= 0
        j = len(plan_str) - 1
        mid = len(plan_str)/2
        plan_str = plan_str.lower()
        while i < mid and j >= mid:
            if plan_str[i] == plan_str[j]:
                i  = i + 1
                j = j - 1
                continue
            return False
        return True
        #Previous Solution
        # A = ''.join(e for e in A if e.isalnum())
        # reverse = ''
        # last = len(A)
        # for i in range(0,len(A)):
        #     reverse = reverse+A[last-i-1]
        # A= A.lower()
        # reverse = reverse.lower()
        # if reverse==A:
        #     print True
        # else:
        #     print False
        # print reverse
        # print A

A = Solution()
# print A.isPalindrome("A man, a plan, a canal: Panama")
# print A.isPalindrome("race a car")
print A.isPalindrome("0P")