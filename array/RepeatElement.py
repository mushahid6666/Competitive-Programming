__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        # if the number at the A[abs(A[i])]
        # make it negative
        # else
        # return as the postive element
        # Modifies the original array so made a copy
        # B = []
        # for i in range(len(A)):
        #     B.append(A[i])
        # for i in range(0,len(B)):
        #     if B[abs(B[i])] > 0:
        #         B[abs(B[i])] = -B[abs(B[i])]
        #     else:
        #         return A[i]

        # Use a hastable. If the element is already present
        # return it as repeated element
        hastable = {}
        for i in range(len(A)):
            if A[i] in hastable:
                return A[i]
            else:
                hastable[A[i]] = 0


A = Solution()
B = (3, 4, 1, 4, 1)
print A.repeatedNumber(B)
